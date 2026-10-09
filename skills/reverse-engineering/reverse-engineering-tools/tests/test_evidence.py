import hashlib
import importlib.util
import json
import re
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "evidence.py"
spec = importlib.util.spec_from_file_location("evidence", SCRIPT)
evidence = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evidence)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.sample = Path(self.temp.name) / "sample.bin"

    def collect(self, data):
        self.sample.write_bytes(data)
        return evidence.collect(self.sample)

    def test_unknown_and_empty(self):
        for data in (b"", b"hello world", b"a" * (1024 * 1024 + 7)):
            with self.subTest(size=len(data)):
                result = self.collect(data)
                self.assertEqual(result["artifact"]["sha256"], hashlib.sha256(data).hexdigest())
                self.assertEqual(result["artifact"]["size_bytes"], len(data))
                self.assertEqual(result["artifact"]["format"], "unknown")
                self.assertEqual(result["runtime_observations"], [])

    def test_pe(self):
        data = bytearray(88)
        data[:2] = b"MZ"
        struct.pack_into("<I", data, 0x3C, 64)
        data[64:68] = b"PE\0\0"
        struct.pack_into("<HH", data, 68, 0x8664, 3)
        result = self.collect(data)["artifact"]
        self.assertEqual((result["format"], result["architecture"], result["section_count"]),
                         ("PE", "x86-64", 3))
        struct.pack_into("<H", data, 68, 0xFFFF)
        self.assertEqual(self.collect(data)["artifact"]["architecture"], "unknown")

    def test_elf_endianness_and_class(self):
        for bits, byte_order, machine, expected in ((1, 1, 3, "x86"), (2, 2, 183, "ARM64")):
            data = bytearray(52 if bits == 1 else 64)
            data[:7] = b"\x7fELF" + bytes([bits, byte_order, 1])
            struct.pack_into(("<" if byte_order == 1 else ">") + "H", data, 18, machine)
            self.assertEqual(self.collect(data)["artifact"]["architecture"], expected)

    def test_malformed_headers(self):
        for data in (b"MZ", b"MZ" + bytes(62), b"\x7fELF", b"\x7fELF" + bytes(60)):
            with self.subTest(data=data):
                with self.assertRaises(ValueError):
                    self.collect(data)

    def test_missing_file_and_directory(self):
        with self.assertRaises(OSError):
            evidence.collect(self.sample)
        with self.assertRaises(ValueError):
            evidence.collect(self.sample.parent)

    def test_cli_and_preservation(self):
        self.sample.write_bytes(b"demo")
        report = self.sample.with_suffix(".json")
        command = [sys.executable, str(SCRIPT), str(self.sample), "--output", str(report)]
        first = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        original = report.read_bytes()
        self.assertEqual(json.loads(original)["artifact"]["size_bytes"], 4)
        second = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(second.returncode, 1)
        self.assertEqual(report.read_bytes(), original)
        missing = subprocess.run([sys.executable, str(SCRIPT), str(report) + ".missing"],
                                 capture_output=True, text=True)
        self.assertEqual(missing.returncode, 1)
        self.assertNotIn("Traceback", missing.stderr)

    def test_local_markdown_links(self):
        for source in ROOT.rglob("*.md"):
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
                if "://" not in link and not link.startswith("#"):
                    self.assertTrue((source.parent / link.split("#")[0]).exists(), f"{source}: {link}")


if __name__ == "__main__":
    unittest.main()
