"""Freeze explicitly selected project files under their original relative paths.

SPDX-License-Identifier: Apache-2.0
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def snapshot(project, blend, build, spec, includes, out, command):
    project = Path(project).resolve(strict=True)
    out = Path(out).resolve()
    if out.exists():
        raise FileExistsError('Checkpoint already exists: ' + str(out))
    selected = [(blend, 'blend'), (build, 'build'), (spec, 'spec')]
    selected += [(path, 'input') for path in includes]
    records, seen = [], set()
    for name, role in selected:
        path = (project / name).resolve(strict=True)
        relative = path.relative_to(project)
        if not path.is_file() or relative in seen or relative == Path('checkpoint.json'):
            raise ValueError('Inputs must be distinct files within the project: ' + str(path))
        seen.add(relative)
        records.append({'path': relative.as_posix(), 'role': role, 'sha256': sha256(path)})
    out.mkdir(parents=True, exist_ok=False)
    for record in records:
        source, target = project / record['path'], out / record['path']
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        if sha256(source) != record['sha256'] or sha256(target) != record['sha256']:
            raise RuntimeError('Input changed during checkpoint: ' + record['path'])
    if any(sha256(project / row['path']) != row['sha256'] for row in records):
        raise RuntimeError('Project input changed while other checkpoint files were copied')
    manifest = {'schema': 'img2blender-checkpoint-v1', 'project': str(project),
                'build_command': command, 'files': records,
                'limits': 'Only explicitly selected files; imports and external dependencies are not automatically discovered.'}
    # The manifest is the completion marker; a partial copy is not an accepted checkpoint.
    (out / 'checkpoint.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, default=Path.cwd())
    parser.add_argument('--blend', type=Path, required=True)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--spec', type=Path, required=True)
    parser.add_argument('--include', action='append', type=Path, default=[])
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--command', required=True, help='Record only; never executed')
    args = parser.parse_args()
    manifest = snapshot(args.project, args.blend, args.build, args.spec, args.include, args.out, args.command)
    print('Checkpoint:', args.out.resolve(), 'files:', len(manifest['files']))


if __name__ == '__main__':
    main()
