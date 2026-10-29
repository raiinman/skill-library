# Source and adaptation

- Requested listing: https://explainx.ai/skills/freshtechbro/claudedesignskills/blender-web-pipeline
- Repository: https://github.com/freshtechbro/claudedesignskills
- Pinned entrypoint: https://github.com/freshtechbro/claudedesignskills/blob/1da73febff0c3e1dfefc07f8a5ef8f7d1dfdb6cd/.claude/skills/blender-web-pipeline/SKILL.md
- Commit: `1da73febff0c3e1dfefc07f8a5ef8f7d1dfdb6cd`
- Original entrypoint SHA256: `788e4c2fa8d559b5f682a0c49c87159bed06207fd04119ec6f8c3fc7203a7b4c`
- License: [MIT](LICENSE), original copyright retained.
- Adapted: 2026-10-18.

The original entrypoint is preserved byte-for-byte in `references/upstream-skill.md`. Every supporting file from the selected upstream skill folder is preserved under `references/upstream/`. Active instructions are the Codex-adapted `SKILL.md`, with current-version API checks, recoverable output handling and task-specific export decisions. Archived examples are provenance, not automatically executable instructions.

The selected package is self-contained. Related Claude plugin commands and unrelated skills from the source repository are outside this import. Blender is already installed locally; live MCP connections, third-party asset accounts, optional compression tools and engine runtimes are separate capabilities, not implied by a skill install.

## Adaptation details

- Codex entrypoint and picker metadata; original entrypoint and all supporting resources archived byte-for-byte
- Version-aware native Blender fallback; corrected unsafe or unconditional export, API and state assumptions
- Archived all three upstream scripts; replaced active execution with explicit-collection output-copy CLI and real Blender smoke test. Absent advertised templates are not claimed as included.
