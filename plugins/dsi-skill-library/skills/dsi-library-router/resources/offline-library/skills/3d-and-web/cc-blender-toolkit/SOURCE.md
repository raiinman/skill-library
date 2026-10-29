# Source and adaptation

- Repository: https://github.com/RobLe3/cc-blender-skill
- Commit: `a2634b588e80265e796aa53f8ab178d75105c2af`
- Source entrypoint: https://github.com/RobLe3/cc-blender-skill/blob/a2634b588e80265e796aa53f8ab178d75105c2af/plugin/skills/text-to-blender/SKILL.md
- Original entrypoint SHA256: `be8b2f7726e217bf78e65a77dff99a983aa86823ece22c52b71048bae2e2289e`
- License: [MIT](LICENSE).
- Packaged: 2026-10-18.
- Specialist modules: 30 unique guides in the canonical tree.

The entire pinned repository is backed up in `assets/upstream.zip`. `archive-manifest.json` lists every original path, byte count and SHA256; no source files or client mirrors are omitted. The selected original entrypoint is also copied byte-for-byte into `references/upstream-entrypoint.md`. Packaging never executes extracted files. Selected reviewed tests ran separately in isolated processes, as recorded in the compatibility notes.

This Codex adaptation adds a focused entrypoint, picker metadata, module routing, a checked archive materializer and native saved-file fallback. Original scripts, manifests and configuration remain unchanged inside the archive. They are reference and optional runtime resources, not automatic permission to reset scenes, change client configuration, start arbitrary-code services, call paid providers or download generation weights. Optional dependencies are installed only for a concrete requested runtime branch. The source UI/plugin and an authenticated live bridge are not claimed as configured.

The local runtime is outside skill discovery roots so original nested skills and duplicate client mirrors do not collide with installed skills. Source examples must be checked against the installed Blender API before use. Test evidence and compatibility limits are in `references/compatibility.md`.
