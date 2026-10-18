"""Check actual restoration bytes, path containment, and output preservation."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from snapshot_checkpoint import snapshot, sha256


class CheckpointTests(unittest.TestCase):
    def test_snapshot_freezes_inputs_and_refuses_reuse_or_escape(self):
        with tempfile.TemporaryDirectory(prefix='img2blender-checkpoint-') as name:
            root = Path(name).resolve()
            self.assertEqual(root.parent, Path(tempfile.gettempdir()).resolve())
            project = root / 'project'
            for relative, data in [('scene.blend', b'BLENDER-fixture'), ('build/main.py', b'print(1)\n'),
                                   ('spec.json', b'{"version":1}\n'), ('textures/paint.png', b'paint-fixture')]:
                path = project / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
            out = root / 'checkpoint'
            inputs = [Path('textures/paint.png')]
            manifest = snapshot(project, Path('scene.blend'), Path('build/main.py'), Path('spec.json'), inputs, out, 'recorded command')
            self.assertEqual(len(manifest['files']), 4)
            for record in manifest['files']:
                self.assertEqual(sha256(out / record['path']), record['sha256'])
            (project / 'build/main.py').write_text('print(2)\n', encoding='utf-8')
            self.assertEqual((out / 'build/main.py').read_bytes(), b'print(1)\n')
            marker = (out / 'checkpoint.json').read_bytes()
            with self.assertRaises(FileExistsError):
                snapshot(project, Path('scene.blend'), Path('build/main.py'), Path('spec.json'), inputs, out, 'changed')
            self.assertEqual((out / 'checkpoint.json').read_bytes(), marker)
            outside = root / 'outside.py'
            outside.write_text('outside', encoding='utf-8')
            with self.assertRaises(ValueError):
                snapshot(project, Path('scene.blend'), Path('../outside.py'), Path('spec.json'), [], root / 'rejected', 'no')
            self.assertFalse((root / 'rejected').exists())
            (project / 'checkpoint.json').write_text('{}', encoding='utf-8')
            with self.assertRaises(ValueError):
                snapshot(project, Path('scene.blend'), Path('build/main.py'), Path('checkpoint.json'), [], root / 'reserved', 'no')
            self.assertFalse((root / 'reserved').exists())

    def test_changed_input_does_not_get_completion_marker(self):
        with tempfile.TemporaryDirectory(prefix='img2blender-checkpoint-') as name:
            root = Path(name).resolve()
            self.assertEqual(root.parent, Path(tempfile.gettempdir()).resolve())
            for filename in ('scene.blend', 'build.py', 'spec.json'):
                (root / filename).write_text('original', encoding='utf-8')
            import shutil
            original_copy = shutil.copy2

            def changed_copy(source, target):
                result = original_copy(source, target)
                if Path(source).name == 'spec.json':
                    (root / 'build.py').write_text('changed during copy', encoding='utf-8')
                return result

            with patch('snapshot_checkpoint.shutil.copy2', side_effect=changed_copy):
                with self.assertRaises(RuntimeError):
                    snapshot(root, Path('scene.blend'), Path('build.py'), Path('spec.json'), [], root / 'copy', 'no')
            self.assertFalse((root / 'copy/checkpoint.json').exists())


if __name__ == '__main__':
    unittest.main()
