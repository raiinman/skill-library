---
name: godot-voxel
description: Integrate Zylann Voxel Tools for Godot volumetric terrain, caves, editable
  blocks, procedural generators, streaming and persistence. Use for voxel module or
  GDExtension setup and runtime issues.
license: MIT
---

# Voxel Tools for Godot

Read [the source map](references/source-map.md) for pinned official docs and archived inputs. Before using API/build syntax, use Context7 for this exact library where available; otherwise use its official version-matched docs and headers. Honor the project's existing engine and dependency choices. Gather compatibility details from the project first, and request only genuinely missing blocking information.

Inspect Godot version, platform, renderer, scripting language and current Voxel Tools edition. The upstream supports a custom-engine module edition and a GDExtension edition, with different maturity and export requirements. Select a compatible release/build and verify whether matching export templates are needed. Do not load the module and extension editions together, which can produce conflicting classes.

Choose blocky versus smooth/LOD terrain based on the actual game. Define voxel/chunk dimensions, world coordinates, seed, generator and material mapping. Test a small region before increasing view distance. Editable volumetric terrain supports caves and overhangs but requires corresponding mesh, collision and storage work; visual terrain alone is not persistence.

Separate generation, streaming, editing and saving. Use the selected version's VoxelViewer, stream and terrain interfaces, obeying thread rules for generation jobs. Define where modified data is stored, how saves are flushed/completed, and how existing world data will be migrated or backed up before generator/format changes. Asynchronous saving must finish before reporting durable completion.

Test dig/place operations across chunk boundaries, cave collision, high-speed streaming, unload/reload and a process restart restoring edits. Confirm release export templates and target-platform support separately from editor operation. Report measured memory and generation/meshing costs rather than promising unlimited terrain.

Deliver the scoped integration or authored asset with reproducible dependency/conversion settings and the checks actually performed. Installation of this skill supplies guidance and source snapshots, not compiled SDKs, an engine plug-in, a live MCP service or evidence of game integration. Install/build a project dependency when the user's concrete integration task needs it. Preserve unrelated project files and existing assets; keep outputs and migrations recoverable.
