"""Verify and extract this skill's pinned source archive into a new runtime folder."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile


def materialize(bundle, out):
    bundle = Path(bundle).resolve()
    out = Path(out).resolve()
    if out.exists():
        raise FileExistsError('Choose a new runtime folder: '+str(out))
    manifest = json.loads((bundle/'archive-manifest.json').read_text(encoding='utf-8'))
    archive = bundle/manifest['archive']
    if not archive.resolve().is_relative_to(bundle):
        raise ValueError('Archive must be inside the bundle')
    if hashlib.sha256(archive.read_bytes()).hexdigest() != manifest['sha256']:
        raise ValueError('Archive checksum mismatch')
    with zipfile.ZipFile(archive) as source:
        files = source.infolist()
        names = [item.filename for item in files]
        if len(set(names)) != len(names) or set(names) != set(manifest['files']):
            raise ValueError('Archive file inventory mismatch')
        for item in files:
            name = item.filename
            path = PurePosixPath(name)
            target = (out/Path(*path.parts)).resolve()
            if path.is_absolute() or not path.parts or '\\' in name or ':' in name or not target.is_relative_to(out):
                raise ValueError('Invalid archive path: '+name)
            if name=='.bundle-source.json' or stat.S_ISLNK(item.external_attr >> 16):
                raise ValueError('Unsupported archive entry: '+name)
            data = source.read(item)
            expected = manifest['files'][name]
            if len(data)!=expected['bytes'] or hashlib.sha256(data).hexdigest()!=expected['sha256']:
                raise ValueError('File checksum mismatch: '+name)
        out.mkdir(parents=True,exist_ok=False)
        for item in files:
            target = out/Path(*PurePosixPath(item.filename).parts)
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(source.read(item))
        for name,expected in manifest['files'].items():
            if hashlib.sha256((out/name).read_bytes()).hexdigest()!=expected['sha256']:
                raise RuntimeError('Extracted file checksum mismatch: '+name)
    (out/'.bundle-source.json').write_text(json.dumps({k:manifest[k] for k in ('repository','commit','sha256')},indent=2)+'\n',encoding='utf-8')
    return out


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    print('Prepared runtime:',materialize(Path(__file__).resolve().parents[1],args.out))
