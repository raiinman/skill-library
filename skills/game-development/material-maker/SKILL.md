---
name: material-maker
description: Create procedural materials or paint 3D models in Material Maker, then
  export and validate texture sets for Blender, Godot, Unreal, Unity or a custom renderer.
license: MIT
---

# Material Maker

Read [the source map](references/source-map.md) for pinned official docs and archived inputs. Before using API/build syntax, use Context7 for this exact library where available; otherwise use its official version-matched docs and headers. Honor the project's existing engine and dependency choices. Gather compatibility details from the project first, and request only genuinely missing blocking information.

Treat Material Maker as a separate authoring tool built with Godot, not a runtime engine plug-in. Locate an existing installation first. For installation, select a supported release and platform from upstream documentation; preserve editable material graph projects alongside their exported images.

Determine the intended surface, scale, UV mapping, tileability, target shader and texture budget from the destination project. Build the smallest useful node graph, preview it on the intended geometry and vary a few exposed parameters. For model painting, inspect UVs, seams and material assignments before committing detail.

Export a named PBR texture set appropriate to the destination. Specify which maps are base color, roughness, metallic, normal, height and ambient occlusion; verify the actual export preset rather than assuming channel packing. Keep scalar/vector maps in the destination's expected non-color interpretation and check normal-map convention, transparency and height/displacement scale. A procedural Material Maker graph is not automatically portable as a live Blender or engine shader graph.

Validate the exported files in the target shader under neutral lighting: tiling/seams, resolution, texture paths, packing, channel orientation and scale. Deliver the editable graph, textures and concise material hookup notes. Use batch/CLI features only after verifying they exist in the selected version; do not invent an automation API.

Deliver the scoped integration or authored asset with reproducible dependency/conversion settings and the checks actually performed. Installation of this skill supplies guidance and source snapshots, not compiled SDKs, an engine plug-in, a live MCP service or evidence of game integration. Install/build a project dependency when the user's concrete integration task needs it. Preserve unrelated project files and existing assets; keep outputs and migrations recoverable.
