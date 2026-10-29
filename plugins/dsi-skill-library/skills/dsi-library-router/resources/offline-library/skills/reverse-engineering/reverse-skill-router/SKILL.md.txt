---
name: reverse-skill-router
description: Use the reverse-skill repository from Codex for authorized reverse engineering, security analysis, CTF, and defensive testing tasks. Requires the reverse-skill repository to be available as the current workspace or an explicitly supplied local path.
metadata:
  library_source:
    kind: installed-local-snapshot
    original_skill_sha256: b798cac13d9ead65f7bf512037c09fc991ba16e0c7920d01ed9f1273b94811bc
---

# Reverse Skill Codex adapter

This plugin is an optional Codex entry point. The repository remains the canonical, client-neutral implementation.

## Local installation

The repository path supplied by this installation is `C:/Users/mikea/.codex/repositories/reverse-skill` (source: `https://github.com/raiinman/reverse-skill`, revision `cab634bd855fc287f6e420c1f36fd1a6b9245960`). When the current workspace is elsewhere, use this checkout as the repository root for the workflow below. Resolve package files and scripts from this root while keeping analysis artifacts in the user's current project.

If `skills/tool-index.md` is absent when tools are needed, consult `README_AI.md` in that checkout for the package-local initialization workflow.

When the current workspace is the `reverse-skill` repository:

1. Read `RULES.md` at the repository root.
2. Run the platform-native `skills/scripts/master-route` entry with the user's task to select the PRIMARY skill from `skills/config/routing.json`.
3. Before any target action, create and validate `work/<case>/scope.md` with the platform-native `case-init` and `case-guard` scripts.
4. Open the selected `skills/<PRIMARY>/SKILL.md` and follow its task-specific instructions.
5. Resolve tools only through the generated `skills/tool-index.md`; do not register MCP servers or install tools unless the user requested that action.

If the repository is not the current workspace and no local repository path was supplied, explain that this adapter does not bundle a second copy of the router. Ask the user to open or clone `https://github.com/zhaoxuya520/reverse-skill` and then continue from its `RULES.md`.

Do not treat the presence of this plugin, a target name, or a sample path as authorization. Authorization comes from the repository's scope contract.
