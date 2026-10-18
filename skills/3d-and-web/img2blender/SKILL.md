---
name: img2blender
description: Reconstruct an object or character from reference images as an editable Blender model, with reproducible bpy scripts and visual correction passes. Use for image-to-Blender modeling, reference matching, materials, and requested rigging or export.
license: Apache-2.0
---

# Image to Blender

Rebuild the visible subject in native Blender geometry, materials, and collections. Deliver an editable `.blend`, its reproducible build script, and renders showing what matches and what remains approximate. A single photograph supports inference, not exact hidden geometry or manufacturing dimensions.

## Start or resume

Inspect the reference with vision before modeling. If it is missing or unreadable, request it. On resuming, read the project's `.img2blender/spec.json`, review history, build script, and latest renders before changing geometry. Keep reconstruction artifacts in the user's project, outside the installed skill.

Locate Blender from the environment or standard application locations, then check its version. Use the installed version's official Python API and available tools. A Blender MCP connection is optional: background `bpy` scripts are a complete local route. Read [Blender execution](references/blender-execution.md) before building or running the review helper.

## Analyze and specify

Read [reference analysis](references/reference-analysis.md). Record observable silhouette, proportions, component hierarchy, attachment points, materials, repeated details, and identity-defining features separately from inferred hidden surfaces. For characters, include landmark proportions, pose, facial features, clothing, and hair masses.

Write a compact `.img2blender/spec.json` using [the reconstruction contract](references/reconstruction-contract.md). It records reference paths, intended use, coordinate convention, components, material strategy, critical features, review views, and unresolved assumptions. Derive the detail and performance budget from the subject and requested use. Default to an editable static asset matching the supplied style; rigging, simulation, destruction, and engine export apply when requested.

Proceed with stated reasonable assumptions when they are reversible. Request additional views only when the missing evidence blocks the requested fidelity. Analysis-only requests end with the assessment and plan.

## Build and correct

Author a subject-specific `build_scene.py` using Blender's Python API. Keep parameters and deterministic seeds visible. Put model parts in a named collection (default `Model`); staging, cameras, and lights belong outside it. Preserve useful part names, parenting, pivots, modifiers, and UVs. Use connected surfaces for continuous forms, curves for swept forms, and instances for repeated details where appropriate. Do not substitute a reference image plane for a volumetric reconstruction.

Work in passes: blockout and matched camera, structure and form, materials and identifying details, then requested rig/export and optimization. Small subjects can combine adjacent passes, but verify silhouette and volume before polishing. Choose Blender-native modifiers, Geometry Nodes, sculpting, curves, or mesh operations to fit the shape. Retain meaningful editability rather than applying every modifier or joining all parts by default.

After each meaningful pass, save a versioned `.blend` and capture the matched reference camera plus useful off-axis views. The bundled [review helper](scripts/review_scene.py) produces camera/orbit PNGs and a geometry/dependency report without saving changes to the source `.blend`. It does not calculate likeness or prove topology quality.

Inspect those images with vision alongside the reference. Check the silhouette, internal features, actual depth, attachments, and materials. Read [visual review](references/visual-review.md) for the correction order and character/rig checks. Fix the cause in the spec or build script, then recapture. Persist each decision in `.img2blender/reviews.jsonl` with the pass, evidence paths, changed parameters, remaining defects, and next action. Carry interactive edits back into reproducible source or an explicit documented manual step.

Use up to three correction rounds for one pass and six for the reconstruction by default. Stop earlier on repeated defects or no progress. At that point preserve the best result, state the blocker, and offer a concrete way forward. Do not quietly weaken the quality contract or label missing evidence a pass. Existing explicit user authorization can extend the iteration budget.

## Deliver

Reopen the saved `.blend` in a fresh Blender process and rerun the relevant review checks. Resolve missing external dependencies or pack eligible textures with provenance. Rigged assets need actual pose/playback and deformation evidence; exports need a separate reopen/import check in their intended route.

Link the `.blend`, build script, reference-camera render, and useful orbit views. State which critical features matched, which surfaces were inferred, and any remaining limitations. A successful Blender render is execution evidence, not proof of reference fidelity.

This is a Blender-native adaptation of img2threejs. Its provenance and replacement boundaries are in [SOURCE.md](SOURCE.md); the archived source entrypoint is for attribution and comparison, not an executable dependency.
