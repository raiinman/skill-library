# Source and adaptation

- Requested listing: https://explainx.ai/skills/msitarzewski/agency-agents/Blender%20Add-on%20Engineer
- Repository: https://github.com/msitarzewski/agency-agents
- Pinned entrypoint: https://github.com/msitarzewski/agency-agents/blob/652b2692f8d8ec2b1f1a38e559073e287dfdc469/game-development/blender/blender-addon-engineer.md
- Commit: `652b2692f8d8ec2b1f1a38e559073e287dfdc469`
- Original entrypoint SHA256: `e9a778fb9a78c31b6c2e2d8a0912cccd32652c1627be4794ae70f5ceb0021076`
- License: [MIT](LICENSE), original copyright retained.
- Adapted: 2026-10-18.

The original entrypoint is preserved byte-for-byte in `references/upstream-skill.md`. Every supporting file from the selected upstream skill folder is preserved under `references/upstream/`. Active instructions are the Codex-adapted `SKILL.md`, with current-version API checks, recoverable output handling and task-specific export decisions. Archived examples are provenance, not automatically executable instructions.

The selected package is self-contained. Related Claude plugin commands and unrelated skills from the source repository are outside this import. Blender is already installed locally; live MCP connections, third-party asset accounts, optional compression tools and engine runtimes are separate capabilities, not implied by a skill install.

## Adaptation details

- Codex entrypoint and picker metadata; original entrypoint and all supporting resources archived byte-for-byte
- Version-aware native Blender fallback; corrected unsafe or unconditional export, API and state assumptions
