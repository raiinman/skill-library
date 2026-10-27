# Source and scope

This is an **original instruction wrapper**, not an upstream agent skill, copied implementation or bundled tool distribution.

- Referenced tool: [Decompollaborate/spimdisasm](https://github.com/Decompollaborate/spimdisasm).
- Public source revision: `4b5d4c68eeb9f9eae14b3bb713971433ae2c3c43`.
- Reviewed tool version: **1.42.4**; reviewed Rabbitizer baseline: **1.16.2**.
- [Upstream README](https://github.com/Decompollaborate/spimdisasm/blob/4b5d4c68eeb9f9eae14b3bb713971433ae2c3c43/README.md) documents static disassembly, frontends, R3000GTE category and experimental overlay limitations.
- [Project metadata](https://github.com/Decompollaborate/spimdisasm/blob/4b5d4c68eeb9f9eae14b3bb713971433ae2c3c43/pyproject.toml) identifies version 1.42.4 and Python >=3.9.
- [Dependency requirement](https://github.com/Decompollaborate/spimdisasm/blob/4b5d4c68eeb9f9eae14b3bb713971433ae2c3c43/requirements.txt): Rabbitizer >=1.14.0,<2.0.0.
- [CLI implementation](https://github.com/Decompollaborate/spimdisasm/blob/4b5d4c68eeb9f9eae14b3bb713971433ae2c3c43/spimdisasm/disasmdis/DisasmdisInternals.py) is the primary basis for explicit endian/category, nonhex filtering, partial-word padding and stdin cautions.
- [Original MIT license](https://github.com/Decompollaborate/spimdisasm/blob/4b5d4c68eeb9f9eae14b3bb713971433ae2c3c43/LICENSE) retained in [LICENSE](LICENSE).
- [Python command-line reference](https://docs.python.org/3.12/using/cmdline.html) documents isolated mode (`-I`) and bytecode-write suppression (`-B`); neither is a security sandbox.
- Wrapper prepared: 2026-10-27 UTC.

## Wrapper decisions

Require per-environment capability/version verification, trusted module locations and working directory, isolated Python invocation, strictly validated complete-word input, explicit byte order/category, argument-vector invocation and empty stdin. Keep the original synthetic example and static decode limits separate from target support. The caller rejects malformed input; no claim is made that upstream does.

No executable helper, package download, binary, private environment path, runtime receipt or game input is bundled. Runtime availability is environment-specific. Library installation and successful helper retrieval do not install a tool on other hosts. No REA entries, providers, source pins or runtime settings are changed.

The original wrapper instructions use the MIT terms in LICENSE. Referencing the upstream source and version does not assert a reproducible build, source-to-distribution attestation, upstream endorsement or provenance clearance for any target data.
