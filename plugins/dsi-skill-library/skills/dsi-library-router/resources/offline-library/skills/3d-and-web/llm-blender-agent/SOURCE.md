# Source and adaptation

- Repository: https://github.com/saofund/LLM-Blender-Agent
- Commit: `bcbb6863b4ca60275332ee791df5e7dab84821f8`
- Source entrypoint: https://github.com/saofund/LLM-Blender-Agent/blob/bcbb6863b4ca60275332ee791df5e7dab84821f8/README.md
- Original entrypoint SHA256: `39c0c6dae3b0bb4c3d7b07266c71c11180f4f289c3b5c7165c4928107d19ab88`
- License: [Apache-2.0](LICENSE).
- Packaged: 2026-10-18.
- Specialist modules: 0 unique guides in the canonical tree.

The entire pinned repository is backed up in `assets/upstream.zip`. `archive-manifest.json` lists every original path, byte count and SHA256; no source files or client mirrors are omitted. The selected original entrypoint is also copied byte-for-byte into `references/upstream-entrypoint.md`. Packaging never executes extracted files. Selected reviewed tests ran separately in isolated processes, as recorded in the compatibility notes.

This Codex adaptation adds a focused entrypoint, picker metadata, module routing, a checked archive materializer and native saved-file fallback. Original scripts, manifests and configuration remain unchanged inside the archive. They are reference and optional runtime resources, not automatic permission to reset scenes, change client configuration, start arbitrary-code services, call paid providers or download generation weights. Optional dependencies are installed only for a concrete requested runtime branch. The source UI/plugin and an authenticated live bridge are not claimed as configured.

The local runtime is outside skill discovery roots so original nested skills and duplicate client mirrors do not collide with installed skills. Source examples must be checked against the installed Blender API before use. Test evidence and compatibility limits are in `references/compatibility.md`.

The upstream README says MIT, while the actual root LICENSE is Apache-2.0. This package retains and identifies the root LICENSE rather than silently relabeling it.
