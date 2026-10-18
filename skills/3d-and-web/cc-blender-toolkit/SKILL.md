---
name: cc-blender-toolkit
description: Plan and execute Blender modeling, shading, rendering, animation, reference
  reconstruction and checked export using the 30-guide cc-blender toolkit. Use for
  multi-stage Blender production, multiview fitting, texture coverage and collision/bake
  handoffs.
license: MIT
---

# CC Blender Toolkit

Use this as one entrypoint to the 30-guide RobLe3 toolkit. Route complete scenes through the text-to-Blender production concepts, and read only the relevant specialist paths from the module index. For template or reference work, combine reference analysis, camera/orthographic registration, source segmentation, contour/mesh construction, atlas/closed-surface UV coverage, multiview fit, look calibration and measured repair as the evidence requires. Collision preflight and Multires cage baking apply to requested engine exports.

The archive preserves the full original plugin, shared references, helper scripts and tests. These guides can be read directly from the materialized runtime, retaining their relative links. Installed global skills such as img2blender and blender-web-pipeline remain independent; this package does not overwrite them or register 30 competing picker entries.

Before using a recipe, read [compatibility notes](references/compatibility.md). In particular, world reset and fixed GEO/MAT naming are source conventions, not global cleanup requirements. A default metalness or display transform is a starting choice, not a universal rule. When generating Python containing Windows paths, use forward-slash paths or `repr`, not unescaped backslashes inside code strings. Upstream regression tests need the same path treatment.

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
