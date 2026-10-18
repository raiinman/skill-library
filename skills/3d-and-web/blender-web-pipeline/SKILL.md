---
name: blender-web-pipeline
description: Export Blender assets to glTF/GLB for web delivery, optimize export copies,
  generate LODs and batch-convert blend files. Use for Blender-to-Three.js, Babylon.js
  or browser asset handoffs.
license: MIT
---

# Blender Web Pipeline

Deliver a web-ready asset while preserving the editable source. Inspect the installed Blender version, source file, intended collection, target viewer and required animations before selecting export settings. Set geometry, texture and download budgets from the actual project rather than universal triangle or file-size limits.

## Export and review

1. Inspect hierarchy, transforms, materials, modifiers, instances, linked resources, rigs, shape keys and actions. Record which parts and animation clips must survive.
2. Use a fresh background Blender process with `--disable-autoexec` and `--python-exit-code 1`. Work from the saved scene or a separate working copy; save live unsaved work intentionally before CLI processing.
3. Export only the intended collection. Decide modifier evaluation explicitly: applying modifiers preserves evaluated shape but can expand arrays; disabling evaluation can omit essential geometry. Preserve skinning, shape keys and instancing when required. A runtime-recreated array requires an explicit placement manifest and working consumer code.
4. Preserve supported PBR images and alpha. Bake unsupported procedural shading on a copy, keeping original material graphs connected until baking is complete. Preserve texture aspect ratios and channel color spaces. Do not replace all materials or convert all textures to JPEG as a default.
5. Start with an uncompressed GLB, then choose compression supported by the target loader. Keep each input so lossy processing can be undone by rebuilding. Read [export and script usage](references/export-workflow.md) for local commands and limits.
6. Reimport the actual export in a clean scene and inspect it in the intended viewer. Compare bounds, orientation, material slots, texture coverage, mesh/instance counts and requested animation/deformation. Verify runtime node names from the exported data rather than assuming renaming rules. Inspect both file size and rendered appearance.

## Included tools

`scripts/web_pipeline.py` provides explicit-collection `export`, `optimize`, `lods`, and `batch` operations. Outputs must be new; source files are not saved. Geometry changes are made only in a background process and written to a separate blend file. LOD generation snapshots the source mesh list and copies mesh data before adding modifiers. It does not claim automatic rig-safe simplification or texture baking.

Report artifact paths, selected settings, measurements and checks actually performed. Deliver the source plus export and any runtime import requirements.

Original source, scripts and guides are preserved under `references/upstream/` and `references/upstream-skill.md` for provenance. They include historical examples, obsolete arguments and mentions of template assets absent from upstream. Use the adapted workflow and current API instead of executing archived scripts. See [SOURCE.md](SOURCE.md).
