---
name: reverse-engineering-tools
description: Analyze supplied game binaries, protection components, drivers, dumps, or traces through reproducible disassembly, decompilation, debugging, diffing, and interface reconstruction.
---

# Reverse-engineering tools

Record the artifact hash, format, architecture, tool version, environment, and observed addresses. Separate static inference from runtime evidence and label protection-induced uncertainty.

## Topic routing

- [Evidence and tools](references/evidence-and-tools.md) for binary findings, debuggers, disassemblers, memory tools, and DBI.
- [Analysis and protection](references/analysis-and-protection.md) for anti-analysis, game targets, workflow, and obfuscation.
- [Ecosystem and advanced work](references/ecosystem-and-advanced.md) for plugins, MCP tools, diffing, anti-debugging, virtualization, and exploit-oriented analysis.
- [Repository resources](references/repository-resources.md) and [repository map](references/repository-map.md) for source selection.

For specialized context, consult upstream [Windows kernel contracts](https://github.com/gmh5225/awesome-game-security/blob/416a2b935fa607b89ef89692f96f93400290f46c/.claude/skills/windows-kernel/SKILL.md), [engine models](https://github.com/gmh5225/awesome-game-security/blob/416a2b935fa607b89ef89692f96f93400290f46c/.claude/skills/game-engine/SKILL.md), and [research rigor](https://github.com/gmh5225/awesome-game-security/blob/416a2b935fa607b89ef89692f96f93400290f46c/.claude/skills/research-rigor/SKILL.md). These optional skills are not bundled; state missing context when it affects a conclusion.

## Initial evidence collection

Run the bundled [collector](scripts/evidence.py) with `python <skill-folder>/scripts/evidence.py <artifact> --output <new-report.json>` to record SHA-256, size, header format, architecture, and collector environment. It reads the file without executing it. Use a stable copy and preserve provenance separately. Header recognition is not full executable validation; unknown formats need an external tool. Record each external tool version, configuration, symbols, and address convention with subsequent findings. Keep observed facts, inferred semantics, runtime observations, and limitations separate.
