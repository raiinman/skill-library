---
name: blender
description: Build and revise Blender scenes through modeling, sculpting, UVs, materials,
  rigging, animation and engine handoff. Use for general Blender production workflows
  and interface guidance.
license: MIT
---

# Blender Workflows

Produce editable Blender assets or explain the relevant interface workflow at the user's level. Inspect the existing file and intended output before changing it. Use the installed version's documentation for API details, shortcuts and exporters.

## Choose the production path

- Modeling: choose mesh, curve, sculpt or modifier workflows from the form and editability needs. Preserve object structure, useful pivots and material assignments. Inspect silhouette, normals and intersections from multiple views before adding detail.
- UVs and shading: establish texel needs, unwrap only affected parts and preserve existing UV sets. Use color textures as color and scalar/vector data with appropriate non-color settings. Compare the rendered result under relevant lighting.
- Rigging and animation: inspect bone collections, parenting, constraints, weights, actions and frame range in the current Blender version. Test the intended motion and deformation. The presence of an armature or action is not sufficient evidence of working animation.
- Grease Pencil: inspect the installed version's data model before using historical examples or converting assets.
- Engine handoff: define source units, destination units, forward/up axes, pivot and root-motion requirements from the actual importer. Do a known-size/orientation round trip before publishing a batch. The archived source contains contradictory engine-axis and scale presets; do not copy those as universal defaults.

Use native `bpy` and background Blender for repeatable saved-file work; a live MCP connection is optional. Prefer direct data access where operators would depend on UI context, and establish the correct mode/selection when an operator is needed. Save versioned outputs, preserve unrelated scene contents and keep the edits reproducible through scripts or documented manual steps.

Deliver the blend file and relevant render, motion samples or target-import evidence. Describe inferred geometry and untested output routes. For image reconstruction, use the dedicated img2blender skill when available; this general workflow does not replace its reference comparison.

The [archived upstream workflow](references/upstream-skill.md) preserves the original interface, modeling, sculpting, UV, rigging and export notes for attribution. Consult it for topic discovery, verifying version-specific facts before use. [SOURCE.md](SOURCE.md) records provenance and corrections.
