"""Exercise the actual DSI reader, provenance retrieval and tamper rejection without model calls."""
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
ROUTER=ROOT/'plugins/dsi-skill-library/skills/dsi-library-router'
TOOLS=['jolt-physics','terrain3d','material-maker','effekseer','godot-voxel','recast-navigation','ozz-animation','the-forge','meshoptimizer','fastnoise2']


def run(*args,success=True):
    result=subprocess.run(['node',str(ROUTER/'scripts/source.mjs'),*map(str,args)],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=120)
    if success:
        if result.returncode:raise AssertionError(result.stderr)
        return json.loads(result.stdout)
    if result.returncode==0:raise AssertionError('Corrupted data was accepted')
    return result.stderr


class WiringTests(unittest.TestCase):
    def test_complete_snapshot_and_named_retrieval(self):
        snapshot=ROUTER/'resources/offline-library'
        verified=run('verify','--snapshot',snapshot)
        self.assertEqual(verified['skills'],len(json.loads((ROOT/'sources.json').read_text())))
        with tempfile.TemporaryDirectory(prefix='dsi-reader-') as temp:
            lock=Path(temp)/'source.json'
            run('begin','--snapshot',snapshot,'--lock',lock)
            for name in TOOLS:
                with self.subTest(skill=name):
                    primary=run('read','--lock',lock,'--path',f'skills/game-development/{name}/SKILL.md')
                    provenance=run('read','--lock',lock,'--path',f'skills/game-development/{name}/SOURCE.md')
                    self.assertEqual(primary['revision'],verified['revision'])
                    self.assertIn('name: '+name,primary['content'])
                    self.assertIn('https://github.com/raiinman/',provenance['content'])

    def test_tampered_primary_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix='dsi-tamper-') as temp:
            root=Path(temp);files={}
            for relative,data in {
                'skills/game-development/jolt-physics/SKILL.md':b'---\nname: jolt-physics\ndescription: Fixture\n---\nOriginal body\n',
                'skills/game-development/jolt-physics/SOURCE.md':b'Fixture provenance\n',
            }.items():
                stored=relative+'.txt' if relative.endswith('/SKILL.md') else relative
                p=root/stored;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
                files[relative]=dict(stored_path=stored,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
            index=dict(schema_version=1,revision='1'*40,count=1,skills=[dict(id='game-development/jolt-physics',name='jolt-physics',description='Fixture',path='skills/game-development/jolt-physics/SKILL.md')])
            data=json.dumps(index).encode();(root/'skill-index.json').write_bytes(data)
            files['skill-index.json']=dict(stored_path='skill-index.json',sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
            manifest=dict(schema_version=1,repository='raiinman/skill-library',revision='1'*40,branch='fixture',index_path='skill-index.json',files=files)
            (root/'snapshot-manifest.json').write_text(json.dumps(manifest))
            self.assertEqual(run('verify','--snapshot',root)['skills'],1)
            (root/'skills/game-development/jolt-physics/SKILL.md.txt').write_text('Replaced content')
            self.assertIn('integrity mismatch',run('verify','--snapshot',root,success=False))

    def test_same_native_router_and_version_in_both_hosts(self):
        plugin=ROOT/'plugins/dsi-skill-library'
        manifests=[json.loads((plugin/p).read_text()) for p in ['plugin.json','.codex-plugin/plugin.json','.claude-plugin/plugin.json']]
        self.assertEqual(len({m['name'] for m in manifests}),1)
        self.assertEqual(len({m['version'] for m in manifests}),1)
        self.assertEqual(list(plugin.rglob('SKILL.md')),[plugin/'skills/dsi-library-router/SKILL.md'])
        snapshots=json.loads((ROUTER/'resources/offline-library/skill-index.json').read_text())
        indexed={s['name'] for s in snapshots['skills']}
        self.assertTrue(set(TOOLS).issubset(indexed))


if __name__=='__main__':unittest.main()
