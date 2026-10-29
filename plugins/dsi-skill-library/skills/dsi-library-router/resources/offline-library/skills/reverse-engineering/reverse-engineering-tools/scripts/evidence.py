"""Collect reproducible, read-only binary metadata using Python's standard library."""

import argparse
import hashlib
import json
import platform
import struct
import sys
from datetime import datetime, timezone
from pathlib import Path

VERSION = "0.1.0"
PE_MACHINES = {0x14C: "x86", 0x8664: "x86-64", 0xAA64: "ARM64", 0x1C4: "ARMv7"}
ELF_MACHINES = {3: "x86", 62: "x86-64", 40: "ARM", 183: "ARM64", 243: "RISC-V"}


def identify(stream, size):
    """Identify header metadata, without claiming the file is a valid executable."""
    header = stream.read(64)
    if header.startswith(b"MZ"):
        if len(header) < 64:
            raise ValueError("Truncated DOS header")
        offset = struct.unpack_from("<I", header, 0x3C)[0]
        if offset < 64 or offset + 24 > size:
            raise ValueError("PE header offset is outside the file")
        stream.seek(offset)
        pe = stream.read(24)
        if len(pe) < 24 or pe[:4] != b"PE\0\0":
            raise ValueError("Missing or truncated PE signature/COFF header")
        machine, sections = struct.unpack_from("<HH", pe, 4)
        return {"format": "PE", "architecture": PE_MACHINES.get(machine, "unknown"),
                "machine_id": machine, "section_count": sections,
                "pe_header_file_offset": offset}
    if header.startswith(b"\x7fELF"):
        if len(header) < 16 or header[4] not in (1, 2) or header[5] not in (1, 2):
            raise ValueError("Invalid ELF class or byte order")
        minimum = 52 if header[4] == 1 else 64
        if len(header) < minimum or header[6] != 1:
            raise ValueError("Truncated or unsupported ELF header")
        endian = "<" if header[5] == 1 else ">"
        machine = struct.unpack_from(endian + "H", header, 18)[0]
        return {"format": "ELF", "architecture": ELF_MACHINES.get(machine, "unknown"),
                "machine_id": machine, "bits": 32 if header[4] == 1 else 64,
                "byte_order": "little" if endian == "<" else "big"}
    return {"format": "unknown", "architecture": "unknown"}


def collect(path):
    path = Path(path).resolve(strict=True)
    if not path.is_file():
        raise ValueError("Artifact must be a regular file")
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        before = path.stat()
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
        stream.seek(0)
        metadata = identify(stream, size)
        after = path.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns) or size != after.st_size:
        raise ValueError("Artifact changed during collection; retry with a stable copy")
    return {
        "schema_version": 1,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "collector": {"name": "reverse-engineering-tools/evidence", "version": VERSION,
                      "python": platform.python_version(), "platform": platform.platform()},
        "artifact": {"path": str(path), "size_bytes": size, "sha256": digest.hexdigest(), **metadata},
        "static_observations": ["SHA-256 and byte size collected from the supplied file",
                                "Format and architecture classified from header fields only"],
        "runtime_observations": [],
        "inferences": [],
        "limitations": ["No execution, disassembly, decompilation, symbol matching or protection detection",
                        "Headers are not a full validation of executable structure",
                        "Unknown formats and machine IDs require an external analysis tool",
                        "Path and collector environment are included; review before sharing"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path, help="File to inspect without executing it")
    parser.add_argument("--output", type=Path, help="Create a new JSON report; existing files are preserved")
    parser.add_argument("--version", action="version", version=VERSION)
    args = parser.parse_args()
    try:
        report = json.dumps(collect(args.artifact), indent=2) + "\n"
        if args.output:
            with args.output.open("x", encoding="utf-8") as stream:
                stream.write(report)
        else:
            sys.stdout.write(report)
    except (OSError, ValueError) as error:
        parser.exit(1, f"error: {error}\n")


if __name__ == "__main__":
    main()
