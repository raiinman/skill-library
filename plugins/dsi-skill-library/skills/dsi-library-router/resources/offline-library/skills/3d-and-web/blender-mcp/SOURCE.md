# Source and adaptation

- Requested listing: https://explainx.ai/skills/vladmdgolam/agent-skills/blender-mcp
- Repository: https://github.com/vladmdgolam/agent-skills
- Pinned entrypoint: https://github.com/vladmdgolam/agent-skills/blob/b66d157341c7c08023f6ef61324bd3ba3c1b6f85/skills/blender-mcp/SKILL.md
- Commit: `b66d157341c7c08023f6ef61324bd3ba3c1b6f85`
- Original entrypoint SHA256: `8721e51d4b47d429fbf490c5c5cf304fdac49c4677e2f0718bfc8771b9a7aa73`
- License: [MIT](LICENSE), original copyright retained.
- Adapted: 2026-10-18.

The original entrypoint is preserved byte-for-byte in `references/upstream-skill.md`. Every supporting file from the selected upstream skill folder is preserved under `references/upstream/`. Active instructions are the Codex-adapted `SKILL.md`, with current-version API checks, recoverable output handling and task-specific export decisions. Archived examples are provenance, not automatically executable instructions.

The selected package is self-contained. Related Claude plugin commands and unrelated skills from the source repository are outside this import. Blender is already installed locally; live MCP connections, third-party asset accounts, optional compression tools and engine runtimes are separate capabilities, not implied by a skill install.

## Adaptation details

- Codex entrypoint and picker metadata; original entrypoint and all supporting resources archived byte-for-byte
- Version-aware native Blender fallback; corrected unsafe or unconditional export, API and state assumptions
- Made MCP conditional and corrected universal name-mapping, array preservation, timeout and compression claims; isolated original examples as archive.
