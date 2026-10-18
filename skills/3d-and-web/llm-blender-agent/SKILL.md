---
name: llm-blender-agent
description: Create and edit Blender scenes from natural language using the LLM-Blender-Agent
  workflow. Use for saofund agent integration, its socket protocol and optional provider
  or Hunyuan workflows; native bpy supports ordinary local modeling without cloud
  APIs.
license: Apache-2.0
---

# LLM Blender Agent

Turn the user's description into scoped Blender edits, inspect the actual result and carry corrections through to a saved artifact. Codex supplies planning and code generation directly; an additional commercial model/API account is unnecessary for ordinary local `bpy` work.

The upstream repository is a Python application and Blender socket add-on, not an agent skill. This entrypoint adapts its inspect, execute, observe and correct workflow to Codex. Read the module index for its client protocol and app structure. For live integration, first check whether a compatible bridge is already configured. The add-on exposes Python execution, so keep it local and identify the correct instance. Do not replace a working official/legacy add-on with this fork merely to model an object.

The optional Gradio app uses provider SDKs and separate user credentials. Provider names/models in the original config are historical examples; choose a supported model from the user's account. Keep credentials in local untracked settings. Hunyuan requires a configured service and potentially large model downloads, not just this skill. The upstream add-on's private LAN default endpoint is the author's environment, not the user's: supply an actual local/user-provided URL before any request. Ordinary Blender work continues through native `bpy` without starting that UI or downloading model weights.

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
