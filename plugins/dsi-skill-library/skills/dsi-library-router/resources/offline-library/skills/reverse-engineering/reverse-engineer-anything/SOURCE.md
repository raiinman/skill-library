# Source

- Repository: [morluto/rea](https://github.com/morluto/rea).
- Pinned release commit: `a56f7bb668ab23fec8d33f7af353ac7ed2fe1895`.
- Original entrypoint: [`.agents/skills/reverse-engineer-anything/SKILL.md`](https://github.com/morluto/rea/blob/a56f7bb668ab23fec8d33f7af353ac7ed2fe1895/.agents/skills/reverse-engineer-anything/SKILL.md).
- Runtime: npm `rea-agents@6.4.0`, from the same release commit.
- Registry integrity: `sha512-Vj1zWfSlna5bphGoaoI/TcVBuYvze9u+OyPC3Shz8YkBqaCTqB4COnnRoX7XDwMpwI24ZlFEel2yEj0k8LTWEQ==`.
- License: MIT, preserved in `LICENSE`.
- Added: 2026-10-13.

## Packaging

The active entrypoint and six workflow references are copied unchanged from the published npm release. That entrypoint supplies its generated tool count and pins fallback package invocation to 6.4.0. The original repository entrypoint is preserved byte-for-byte in `references/upstream-skill.md`. Codex picker metadata is added separately.

All 44 English Markdown guides from this release are backed up under `docs/`, with the upstream README and license. Their Git blob hashes were verified while downloading. Start with [installation and supported agents](docs/installation.md#supported-agents) or [the documentation index](docs/index.md); the skill's main on-demand workflow guides remain in `references/`. These files can be restored independently of the upstream repository. Runtime binaries, third-party engines, and unrelated repository development skills are not part of this skill package.

## This machine

REA 6.4.0 is installed globally. The skill is installed in `~/.agents/skills/reverse-engineer-anything`, the shared skill location used by Codex and REA's readiness check. Its Codex MCP entry launches the installed public `scripts/rea.mjs` through Node, with a 30-second startup timeout. Setup was restricted to Codex, with the skill installed separately from this library; existing configuration was preserved and backed up in `~/.codex/config.toml.rea.backup`.

Restart or reconnect Codex to make the new MCP server available in the app. Some operations require separately configured providers or task-specific tools. Static JavaScript analysis and several artifact inspections work without Hopper or Ghidra; native decompilation needs a supported configured engine. The installed CLI and actual connected tool schemas determine which capabilities are available.
