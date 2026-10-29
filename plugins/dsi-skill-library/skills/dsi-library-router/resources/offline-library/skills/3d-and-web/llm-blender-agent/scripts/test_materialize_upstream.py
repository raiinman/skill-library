"""Check exact extraction, source preservation and preflight refusal of unsafe archives."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

spec=importlib.util.spec_from_file_location('materializer',Path(__file__).with_name('materialize_upstream.py'))
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class MaterializerTest(unittest.TestCase):
    def make_bundle(self,root,files):
        bundle=root/'bundle';bundle.mkdir()
        archive=bundle/'upstream.zip'
        with zipfile.ZipFile(archive,'w') as z:
            for name,data in files.items():z.writestr(name,data)
        manifest=dict(repository='test/source',commit='fixture',archive='upstream.zip',sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),
            files={name:dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest()) for name,data in files.items()})
        (bundle/'archive-manifest.json').write_text(json.dumps(manifest))
        return bundle

    def test_exact_and_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);files={'folder/example.py':b'print("archived, not run")\r\n','LICENSE':b'license\n'}
            bundle=self.make_bundle(root,files);before=(bundle/'upstream.zip').read_bytes()
            out=module.materialize(bundle,root/'runtime')
            for name,data in files.items():self.assertEqual((out/name).read_bytes(),data)
            self.assertEqual((bundle/'upstream.zip').read_bytes(),before)
            with self.assertRaises(FileExistsError):module.materialize(bundle,out)

    def test_escaping_path_and_hash(self):
        for name in ('../escaped','/absolute','C:/outside','..\\outside'):
            with self.subTest(name=name),tempfile.TemporaryDirectory() as temp:
                root=Path(temp);bundle=self.make_bundle(root,{name:b'payload'})
                with self.assertRaises(ValueError):module.materialize(bundle,root/'runtime')
                self.assertFalse((root/'runtime').exists())
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);bundle=self.make_bundle(root,{'file':b'original'})
            (bundle/'upstream.zip').write_bytes(b'changed')
            with self.assertRaises(ValueError):module.materialize(bundle,root/'runtime')
            self.assertFalse((root/'runtime').exists())


if __name__=='__main__':unittest.main()
