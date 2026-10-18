# Source and adaptation

- Requested listing: https://explainx.ai/skills/davincidreams/agent-team-plugins/blender
- Repository: https://github.com/davincidreams/agent-team-plugins
- Pinned entrypoint: https://github.com/davincidreams/agent-team-plugins/blob/826a409e23fde79a322d8e7680d0a23ff5cad9d5/teams/3d-design/skills/blender/SKILL.md
- Commit: `826a409e23fde79a322d8e7680d0a23ff5cad9d5`
- Original entrypoint SHA256: `17b71c9fae475bfca5774f3093ee78afafb05d01969db454a17470309e5ef515`
- License: [MIT](LICENSE), original copyright retained.
- Adapted: 2026-10-18.

The original entrypoint is preserved byte-for-byte in `references/upstream-skill.md`. Every supporting file from the selected upstream skill folder is preserved under `references/upstream/`. Active instructions are the Codex-adapted `SKILL.md`, with current-version API checks, recoverable output handling and task-specific export decisions. Archived examples are provenance, not automatically executable instructions.

The selected package is self-contained. Related Claude plugin commands and unrelated skills from the source repository are outside this import. Blender is already installed locally; live MCP connections, third-party asset accounts, optional compression tools and engine runtimes are separate capabilities, not implied by a skill install.

## Adaptation details

- Codex entrypoint and picker metadata; original entrypoint and all supporting resources archived byte-for-byte
- Version-aware native Blender fallback; corrected unsafe or unconditional export, API and state assumptions
