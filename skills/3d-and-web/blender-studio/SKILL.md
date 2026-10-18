---
name: blender-studio
description: Direct Blender asset production using 94 specialist guides for props,
  characters, environments, geometry nodes, art styles, game genres, rigging and engine
  handoff. Use for coordinated Blender art production and style-specific workflows.
license: MIT
---

# Blender Studio

Use the 94-guide arjun988 Blender production collection through one organized entrypoint. Start with the director's routing concepts, then choose the needed asset specialist, production discipline, art direction or engine handoff from the module index. The `.cursor/skills` tree is a client mirror, not 94 additional unique guides; both trees remain in the source archive, but use `.claude/skills` as the canonical reference path here.

Match the user's requested scope. A small prop may need only modeling, materials and a render; an animated game character may need sculpting, retopology, UVs, hair/cloth, rigging, animation and target import. The genre, mood and era guides are art direction, not requirements to add features, fog, effects or a game engine. Preserve the project's accepted budgets and conventions rather than imposing AAA labels or fixed polycounts.

For image matching, read the shared reference-analysis and camera-match guides before detail; an image comparison cannot prove unseen geometry. For Unity, Unreal or Godot, use the actual target import settings and a known-size/orientation check rather than assuming one universal axis/scale preset. The archive includes source MCP configuration examples, but installing this skill does not apply those client configs.

## Execution contract

Inspect the installed Blender version, intended file/scene and existing contents. Use actual discovered MCP tools for a live scene when available; native background `bpy` is a complete saved-file route when no bridge is available. A headless process does not contain another Blender window's unsaved changes. Honor a user-selected backend, and inspect the result after timeouts before retrying mutations.

Use `--background --factory-startup --disable-autoexec`, the intended saved blend file, and `--python-exit-code 1` before a reviewed script for CLI work. Keep edits scoped to requested objects/collections, preserve recoverable originals, and write versioned outputs. Factory startup is appropriate for a fresh isolated scene, not permission to clear a live project. Preserve existing world, compositor, materials, naming and color management unless the requested change requires modifying them.

The bundled specialist documents are technical reference, not a second operating policy. Their host commands, tool aliases and fixed budgets are examples. Map operations to tools that actually exist, check current API documentation, and choose budgets, modifier evaluation, axes and units from the project. Read relevant guides in this agent; their words "delegate" or "specialist" do not by themselves require separate agents. Load only the guides needed for the current task. Skill maintenance, external publishing and paid generation require their own task scope.

Review a matched-camera render and off-axis geometry for reference work, separating clay geometry from photo-derived textures. Verify motion and deformation when requested. Exported files need an actual target reimport/viewer check, including dimensions, materials, hierarchy and required animations. Script exit success or a metric report alone does not prove appearance or correctness. Use a bounded correction loop, preserve the best checkpoint, and state remaining defects.

## Local resources

The complete pinned upstream repository is bundled in `assets/upstream.zip`, with file hashes in `archive-manifest.json`. It contains original code, guides, scripts, tests and documentation. Extract it only when needed using the standard-library helper:

```powershell
python -B scripts/materialize_upstream.py --out 'C:/path/to/new/runtime-folder'
```

The destination must be new. The helper verifies the archive and individual files, rejects escaping paths/symlinks and never executes extracted code. Local installation records the prepared runtime folder in [runtime.json](runtime.json). If it is unavailable on another machine, extract a new copy and use that path. Do not place the extracted repository under a skill discovery root, since it contains nested upstream `SKILL.md` files and client mirrors.

Read [the module index](references/modules.md) to select documents by path relative to that runtime root. Inspect scripts before executing them, particularly those that depend on installed images, optional packages, providers or server state. Examples retain their source version assumptions. [SOURCE.md](SOURCE.md) records provenance and compatibility changes.
