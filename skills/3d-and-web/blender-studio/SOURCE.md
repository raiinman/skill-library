# Source and adaptation

- Repository: https://github.com/arjun988/blender-skills
- Commit: `8f778d2405a214b508d4c7d80742be8e43acdd52`
- Source entrypoint: https://github.com/arjun988/blender-skills/blob/8f778d2405a214b508d4c7d80742be8e43acdd52/.claude/skills/blender-director/SKILL.md
- Original entrypoint SHA256: `ba10ae3243590f94fb114b6cb1e476f8f0510f0a99de100e8c14651d081bc008`
- License: [MIT](LICENSE).
- Packaged: 2026-10-18.
- Specialist modules: 94 unique guides in the canonical tree.

The entire pinned repository is backed up in `assets/upstream.zip`. `archive-manifest.json` lists every original path, byte count and SHA256; no source files or client mirrors are omitted. The selected original entrypoint is also copied byte-for-byte into `references/upstream-entrypoint.md`. Packaging never executes extracted files. Selected reviewed tests ran separately in isolated processes, as recorded in the compatibility notes.

This Codex adaptation adds a focused entrypoint, picker metadata, module routing, a checked archive materializer and native saved-file fallback. Original scripts, manifests and configuration remain unchanged inside the archive. They are reference and optional runtime resources, not automatic permission to reset scenes, change client configuration, start arbitrary-code services, call paid providers or download generation weights. Optional dependencies are installed only for a concrete requested runtime branch. The source UI/plugin and an authenticated live bridge are not claimed as configured.

The local runtime is outside skill discovery roots so original nested skills and duplicate client mirrors do not collide with installed skills. Source examples must be checked against the installed Blender API before use. Test evidence and compatibility limits are in `references/compatibility.md`.
