"""Refresh DSI discovery and its byte-verified offline snapshot from a committed library revision."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import yaml


ROOT=Path(__file__).resolve().parents[1]
PLUGIN=ROOT/'plugins/dsi-skill-library'
ROUTER=PLUGIN/'skills/dsi-library-router'


def encode(data):
    return (json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode('utf-8')


def put(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(data if isinstance(data,bytes) else encode(data))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def frontmatter(data):
    match=re.match(r'^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)',data.decode('utf-8-sig'))
    if not match:raise ValueError('Missing native skill frontmatter')
    meta=yaml.safe_load(match[1])
    if not isinstance(meta,dict) or not all(isinstance(meta.get(k),str) and meta[k].strip() for k in ['name','description']):
        raise ValueError('Missing native skill name/description')
    return meta


def sync(revision):
    revision=subprocess.check_output(['git','rev-parse',revision+'^{commit}'],cwd=ROOT).decode().strip()
    tree=subprocess.check_output(['git','ls-tree','-rz',revision],cwd=ROOT)
    objects={}
    for record in tree.split(b'\0'):
        if not record:continue
        header,path=record.split(b'\t',1);mode,kind,blob=header.decode().split()
        if kind=='blob':objects[path.decode('utf-8')]=(mode,blob)
    process=subprocess.Popen(['git','cat-file','--batch'],cwd=ROOT,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    def blob(path):
        process.stdin.write((objects[path][1]+'\n').encode());process.stdin.flush()
        header=process.stdout.readline().decode().split()
        if len(header)!=3 or header[1]!='blob':raise RuntimeError('Cannot read Git blob: '+path)
        data=process.stdout.read(int(header[2]));assert process.stdout.read(1)==b'\n'
        return data
    try:
        sources=json.loads(blob('sources.json'))
        packages={entry['path']:entry for entry in sources}
        if len(packages)!=len(sources):raise ValueError('Duplicate canonical packages')
        selected=[p for p in objects if p in ['README.md','CATALOG.md','SETUP.md','REPOSITORIES.md','GAME-TOOLS.md','collections.json','sources.json','readme-banner.png']
            or any(p.startswith(package+'/') for package in packages)]
        contents={p:blob(p) for p in selected}
        overlay_path=ROUTER/'resources/maintenance-overlay/manifest.json'
        overlay=json.loads(overlay_path.read_text(encoding='utf-8'))
        for path,entry in overlay['files'].items():
            if path not in contents or sha(contents[path])!=entry['base_sha256']:
                raise ValueError('Maintained replacement requires review against changed source: '+path)
            replacement=(overlay_path.parent/entry['resource_path']).read_bytes()
            if sha(replacement)!=entry['sha256'] or len(replacement)!=entry['bytes']:
                raise ValueError('Maintained replacement integrity mismatch: '+path)
        overlay['base_revision']=revision
        overlay['id']='dsi-'+json.loads((PLUGIN/'plugin.json').read_text())['version']
        put(overlay_path,overlay)
        descriptor=dict(id=overlay['id'],repository=overlay['repository'],base_revision=revision,manifest_sha256=sha(overlay_path.read_bytes()))
        base_skills=[];effective_skills=[]
        for package,entry in sorted(packages.items()):
            path=package+'/SKILL.md'
            if path not in contents or package+'/SOURCE.md' not in contents:raise ValueError('Primary/provenance missing: '+package)
            for effective,rows in [(False,base_skills),(True,effective_skills)]:
                data=contents[path]
                if effective and path in overlay['files']:
                    data=(overlay_path.parent/overlay['files'][path]['resource_path']).read_bytes()
                meta=frontmatter(data)
                if meta['name']!=entry['name']:raise ValueError('Native skill name differs from canonical path: '+path)
                rows.append(dict(id=entry['category']+'/'+entry['name'],name=meta['name'],category=entry['category'],
                    path=path,source_path=package+'/SOURCE.md',description=meta['description'],routing_metadata=meta.get('metadata',{}).get('dsi',{})))
        categories=sorted({s['category'] for s in base_skills})
        if len({s['name'] for s in base_skills})!=len(base_skills):raise ValueError('Duplicate skill name')
        base_index=dict(schema_version=1,discovery='canonical-native-frontmatter',count=len(base_skills),categories=categories,skills=base_skills)
        base_index['content_sha256']=sha(encode(base_skills))
        put(ROOT/'skill-index.json',base_index)
        snapshot=ROUTER/'resources/offline-library'
        records={}
        for path,data in contents.items():
            stored=path+'.txt' if path.endswith('/SKILL.md') else path
            record=dict(sha256=sha(data),bytes=len(data),stored_path=stored,git_blob=objects[path][1])
            if path in overlay['files']:
                record['base_sha256']=record['sha256'];record['base_git_blob']=record.pop('git_blob')
                data=(overlay_path.parent/overlay['files'][path]['resource_path']).read_bytes()
                record.update(sha256=sha(data),bytes=len(data),maintenance_overlay=overlay['id'])
            put(snapshot/stored,data);records[path]=record
        for skill in effective_skills:skill['resource_path']=skill['path']+'.txt'
        index=dict(schema_version=1,discovery='bundled-from-pinned-catalog',revision=revision,
            maintenance_overlay=descriptor,count=len(effective_skills),categories=categories,skills=effective_skills)
        data=encode(index);put(snapshot/'skill-index.json',data)
        records['skill-index.json']=dict(sha256=sha(data),bytes=len(data),stored_path='skill-index.json',derived=True)
        manifest=dict(schema_version=1,repository='raiinman/skill-library',branch='main',revision=revision,
            source_kind='bundled-snapshot',default_git_mode='100644',maintenance_overlay=descriptor,
            freshness='Immutable committed source revision plus hash-gated maintained replacements; not a live branch check.',
            index_path='skill-index.json',canonical_skill_count=len(base_skills),
            storage_note='Canonical SKILL.md bodies are stored as SKILL.md.txt to avoid duplicate native registrations. Resolve canonical resources through files[path].stored_path.',files=records)
        put(snapshot/'snapshot-manifest.json',manifest)
        discovery=dict(schema_version=1,content_sha256=sha(encode(effective_skills)),count=len(base_skills),categories=categories,skills=effective_skills)
        put(ROUTER/'references/skill-snapshot.json',discovery)
        report_path=snapshot/'bundle-report.json'
        report=json.loads(report_path.read_text())
        report['refresh']=dict(revision=revision,canonical_skill_count=len(base_skills),tracked_resources=len(records),
            source='Committed canonical packages; retained pre-existing link diagnostics are historical, not a current all-links-pass claim.')
        put(report_path,report)
        return dict(revision=revision,skills=len(base_skills),resources=len(records),maintained_replacements=len(overlay['files']))
    finally:
        process.stdin.close();process.stdout.close();process.wait()


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--revision',required=True,help='Committed canonical source revision; working-tree changes are excluded')
    args=parser.parse_args()
    print(json.dumps(sync(args.revision),indent=2))
