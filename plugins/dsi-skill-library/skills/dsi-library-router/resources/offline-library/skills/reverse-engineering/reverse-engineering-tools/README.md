# Reverse Engineering Tools

A standalone agent skill and read-only evidence collector for reproducible binary analysis. Adapted from [gmh5225/awesome-game-security](https://github.com/gmh5225/awesome-game-security), as listed on [explainx.ai](https://explainx.ai/skills/gmh5225/awesome-game-security/reverse-engineering-tools).

## Quick start

Requires Python 3.11 or newer. No dependencies or external reverse-engineering tools are required for the evidence collector.

```sh
git clone https://github.com/raiinman/reverse-engineering-tools.git
cd reverse-engineering-tools
python scripts/evidence.py path/to/program.exe
python scripts/evidence.py path/to/program.exe --output evidence.json
python -m unittest discover -s tests -v
```

On Windows, `py -3` can replace `python`.

The collector streams SHA-256 hashing, records size and UTC collection time, recognizes PE and ELF headers, and records architecture when the machine ID is known. It distinguishes header observations from runtime evidence and inferred behavior. Existing output files are preserved. Parent output directories must already exist.

It never executes the supplied artifact. It does not disassemble, decompile, unpack, acquire memory, detect protections, or validate the full executable structure. Unsupported files remain `unknown`; malformed recognized headers produce an error. Analyze a stable local copy. Reports include the absolute file path and collector environment, so review them before sharing.

## Use as an agent skill

The repository root is the skill folder: [SKILL.md](SKILL.md), [references](references/evidence-and-tools.md), and [scripts/evidence.py](scripts/evidence.py) travel together. Copy the complete folder into your agent's skill directory, for example `.agents/skills/reverse-engineering-tools/` for a project using Codex, or `.claude/skills/reverse-engineering-tools/` for Claude Code.

Invoke `$reverse-engineering-tools` with an artifact and a specific analysis question. The bundled collector provides the initial evidence record; deeper analysis uses separately installed tools such as Ghidra, x64dbg, or WinDbg. Related domain skills are optional upstream resources and are not installed by this repository.

## Reference material

- [Evidence and tools](references/evidence-and-tools.md): evidence conventions, debugger selection, and instrumentation limits.
- [Analysis and protection](references/analysis-and-protection.md): engine workflows and obfuscation concepts.
- [Ecosystem and advanced work](references/ecosystem-and-advanced.md): plugins, MCP interfaces, and binary diffing.
- [Repository resources](references/repository-resources.md): tool families and evidence requirements.
- [Repository map](references/repository-map.md): upstream resource discovery.

## Provenance and license

[SOURCE.md](SOURCE.md) records the immutable source revision and adaptations. The upstream MIT license and copyright are preserved in [LICENSE](LICENSE). Third-party tools are not bundled and retain their own licenses. CI runs the collector and link-integrity tests on Windows and Linux.
