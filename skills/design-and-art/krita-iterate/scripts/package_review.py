"""Package declared numbered artwork exports; preserve originals and exclude unrelated files."""
import argparse
import base64
import hashlib
import html
import json
from pathlib import Path
import re
import zipfile


def package(manifest_path, output):
    manifest_path, output = Path(manifest_path).resolve(), Path(output).resolve()
    if output.exists():
        raise ValueError('Output directory already exists; choose a new path')
    if manifest_path.stat().st_size > 1024*1024:
        raise ValueError('Version manifest exceeds 1 MiB')
    raw = manifest_path.read_bytes()
    manifest = json.loads(raw)
    if not isinstance(manifest, dict) or not isinstance(manifest.get('project'), str):
        raise ValueError('Manifest needs a project name and versions')
    versions = manifest.get('versions')
    if not isinstance(versions, list) or not 1 <= len(versions) <= 64:
        raise ValueError('Declare 1..64 versions')
    root, identities, inputs, frames = manifest_path.parent, set(), {}, []
    total_images = 0
    for version in versions:
        if not isinstance(version, dict):
            raise ValueError('Each version must be an object')
        identifier = version.get('id', '')
        if not isinstance(identifier, str) or not re.fullmatch(r'v\d{3,6}', identifier) or identifier in identities:
            raise ValueError('Version IDs must be unique v001-style identifiers')
        identities.add(identifier)
        if not isinstance(version.get('accepted', False), bool):
            raise ValueError('accepted must be a boolean')
        for key in ('change', 'review'):
            if not isinstance(version.get(key), str) or len(version[key]) > 4096:
                raise ValueError('Each version needs bounded change and review text')
        for key in ('kra', 'png'):
            relative = version.get(key)
            if not isinstance(relative, str) or Path(relative).is_absolute():
                raise ValueError('Artwork paths must be relative')
            path = (root/relative).resolve()
            if not path.is_relative_to(root) or path.suffix.lower() != '.'+key or not path.is_file():
                raise ValueError('Artwork must exist inside the manifest folder with the declared extension')
            size = path.stat().st_size
            if size <= 0 or size > (256*1024*1024 if key == 'kra' else 16*1024*1024):
                raise ValueError('Artwork size exceeds the package limit')
            data = path.read_bytes()
            if key == 'png':
                if not data.startswith(b'\x89PNG\r\n\x1a\n'):
                    raise ValueError('Declared PNG lacks a PNG signature')
                total_images += len(data)
                if total_images > 64*1024*1024:
                    raise ValueError('Total PNG data exceeds 64 MiB')
                frames.append({**version, 'image': 'data:image/png;base64,'+base64.b64encode(data).decode('ascii')})
            else:
                if not zipfile.is_zipfile(path):
                    raise ValueError('Declared KRA is not a ZIP document')
                with zipfile.ZipFile(path) as kra:
                    if 'maindoc.xml' not in kra.namelist():
                        raise ValueError('Declared KRA lacks maindoc.xml')
            archive_name = path.relative_to(root).as_posix()
            inputs[archive_name] = (path, hashlib.sha256(data).hexdigest(), len(data))
    # Validate every input before creating any output. New directory avoids overwrites.
    output.mkdir(parents=True)
    records = [{'path': name, 'sha256': digest, 'bytes': size} for name, (_, digest, size) in inputs.items()]
    (output/'archive-manifest.json').write_text(json.dumps({'project': manifest['project'], 'files': records}, indent=2), encoding='utf-8')
    with zipfile.ZipFile(output/'progression.zip', 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('versions.json', raw)
        for name, (path, digest, size) in inputs.items():
            data = path.read_bytes()
            if hashlib.sha256(data).hexdigest() != digest:
                raise ValueError('Artwork changed during packaging; discard this incomplete package')
            archive.writestr(name, data)
        archive.write(output/'archive-manifest.json', 'archive-manifest.json')
    title = html.escape(manifest['project'])
    cards = ''.join('<figure><img alt="'+html.escape(frame['id'])+'" src="'+frame['image']+'"><figcaption><strong>'+html.escape(frame['id'])+'</strong> '+('Chosen' if frame.get('accepted') else 'Retained')+'<p>'+html.escape(frame['change'])+'</p><p>'+html.escape(frame['review'])+'</p></figcaption></figure>' for frame in frames)
    data_json = json.dumps(frames).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+title+'''</title>
<style>body{font:16px system-ui;margin:24px;background:#f1f1f1;color:#17242b}button,select{font:inherit;padding:8px}.sheet{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}figure{margin:0;background:white;padding:16px;border-radius:8px}img{width:100%;height:240px;object-fit:contain;background:repeating-conic-gradient(#ddd 0% 25%,#fff 0% 50%) 0/20px 20px}#frame{height:360px}figcaption p{line-height:1.4}#viewer{max-width:800px;margin-bottom:24px}</style>
<h1>'''+title+'''</h1><p>Numbered development versions. Playback shows revisions, not a Krita animation timeline.</p>
<section id="viewer"><button id="play">Play progression</button> <label>Frame <select id="choose"></select></label><figure><img id="frame" alt=""><figcaption id="caption"></figcaption></figure></section>
<h2>Contact sheet</h2><section class="sheet">'''+cards+'''</section><script>
const frames='''+data_json+''';let index=0,timer=null;const choose=document.getElementById('choose'),play=document.getElementById('play');
frames.forEach((frame,i)=>{const option=document.createElement('option');option.value=i;option.textContent=frame.id;choose.appendChild(option)});
function show(){const f=frames[index];document.getElementById('frame').src=f.image;document.getElementById('frame').alt=f.id;document.getElementById('caption').textContent=f.id+' — '+f.change+' — '+f.review;choose.value=index}
choose.onchange=()=>{index=Number(choose.value);show()};play.onclick=()=>{if(timer){clearInterval(timer);timer=null;play.textContent='Play progression'}else{timer=setInterval(()=>{index=(index+1)%frames.length;show()},1200);play.textContent='Pause'}};show();
</script></html>'''
    (output/'review.html').write_text(page, encoding='utf-8')
    return {'archive': str(output/'progression.zip'), 'review': str(output/'review.html'), 'frames': len(frames)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(package(args.manifest, args.output)))
        return 0
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        parser.exit(1, str(error)+'\n')


if __name__ == '__main__':
    raise SystemExit(main())
