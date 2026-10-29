---
name: krita-layer-rebuild
description: Recreate a reference image 1:1 in editable Krita layers using native drawing and painting and visual comparison. Use for reconstruction of illustrations, painterly scenes, posters or photographs, tutorial reproduction and requested style transfer.
---

# Krita Recreate

Target a 1:1 visual reconstruction of the supplied image in editable Krita layers. A flattened reference supplies visible appearance; the new ownership tree and hidden continuation are designed, not recovered original layers. Selected native edits and save/reopen/repeat behavior have been exercised, as has one seven-codepoint font subset. Broad fidelity, complete fine-detail ownership, native typesetting and general font reliability remain unmet or unvalidated; new research adaptations require their own trials.

## 1:1 target and completion

For this user, 1:1 means a faithful visual reconstruction at full size in editable Krita layers, rather than pixel-for-pixel equality with a JPEG. Match the supplied image's composition, geometry, proportions, wording, colors, lighting, material treatment, edges and visible details in the faithful master. Reproduction is the default task; create a different subject or style-transfer variant only when requested.

Compare the saved reconstruction with the exact target at matching dimensions, crop and orientation, using whole-image and full-size regional views. Keep an explicit list of remaining visible mismatches and their responsible owners; repair them and recheck protected regions. Assess editable ownership separately through real edits and save/reopen checks. Preserve promised editability when it conflicts with fidelity and report both unmet requirements.

Declare the 1:1 target achieved only when comparison supports the requested visual match and the promised editability checks pass. An unresolved material, geometry or detail mismatch leaves reproduction partial. A user stop, agreed budget or unavailable tool can end a run with a saved partial result, but does not establish 1:1 completion. A user-approved lower target applies to that job only; the Revoy test's approximate80% stop is not the default quality threshold. Report subjective judgments as such, without invented accuracy percentages.

## Connect to Krita

Prefer the **Krita Prototype** connector (`mcp__krita_prototype__*`) for this user's reconstruction work. Before editing, call its `krita_health`, `krita_state` and `krita_compatibility`; inspect the explicit document with `krita_preview`. Use document/layer IDs and allowed output roots from that connector's fresh state. API availability is not execution or persistence evidence.

Use the currently exposed Prototype schemas. Its `krita_stroke` paints line segments with one native undo entry per segment; calibrate the result before treating it as a continuous brush path or tutorial pressure replay. Its `krita_fill` paints a disk, not a flood fill. For `krita_command`, submit with a caller-owned operation ID once and use `krita_operation_status` to resolve an uncertain outcome. If state cannot fingerprint a filter mask, preserve that limitation; use checkpoints, explicit layer state and projection comparison rather than claiming a complete revision guard. Historical temporary study actions are not assumed installed.

If Prototype is unavailable, report the connection gap. Use the separate `mcp__krita__*` connector and its krita-control guidance only when that backend is selected for the task and independently verified. Keep one connector's IDs, operation recovery and schemas throughout a live job; refresh them when switching. The skill supplies the reconstruction method; a connector supplies Krita controls.

## Inspect and plan

Inspect the reference with view_image or the selected connector's preview. Preserve the source and existing documents. Create a separate working document, use unique filenames beneath configured bridge roots, and verify explicit document state after lifecycle changes. Ask for a reference only when none is available.

Honor requested dimensions, transparency and fidelity. Establish one coordinate frame; record object bounds, contour landmarks, negative spaces, overlap/contact relations, dominant value/color regions and edge/material behavior. Compare thumbnail and native-size views. Source transcription and intentional irregularities are part of the target.

Create a nested inventory before construction: whole objects, components and individually identified visible details. Map each promised item to its group/layers/shape data and declare omissions. Dense texture stored as one field does not make each visible mark editable. Record shared boundaries/joins, caster/receiver effects, reflection/refraction and attachments. Mark unseen continuation inferred, with the edit that reveals it.

Select methods from the observed reference before constructing each relevant owner:

| Reference feature or problem | Required guide |
| --- | --- |
| Receding planes, repeated spacing, rims, openings, complex volumes or surface-mapped graphics | [Construction and perspective](references/construction-and-perspective.md) |
| Skin, cloth, wood, metal, gems, glass, liquid, hair/fur, vegetation or atmosphere | [Materials and light](references/materials-and-light.md) |
| Character proportions, expression, hair attachment, line/fill depiction, clothing or prop contacts | [Character illustration](references/character-illustration.md) |
| Text, logos, custom lettering, dimensional glyphs or requested reusable font | [Text and fonts](references/text-and-fonts.md) |
| Repeated owners, palette variants, tonal mapping, glow, cast shadows, mist or reversible finish | [Layout and effects](references/layout-and-effects.md) |
| Uncertain construction route, boundary/fringe repair, brush behavior or regression diagnosis | [Drawing decisions](references/drawing-decisions.md) |
| Following a complete tutorial, matching its final revision or transferring its visual treatment to a new subject | [Tutorial reproduction and style transfer](references/tutorial-reproduction.md) |

For each owner, record the observed problem, chosen procedure, intended layers/controls, dependent owners and a concrete check. For example: a curved bottle needs a fitted rim and transparent interior, separate liquid level and optical effects, then a move over another background to check those dependencies. Read applicable branches, not every guide indiscriminately. Source methods and our ownership adaptations are distinct; neither reading nor structural validation establishes successful execution.

## Construct with ownership

Establish background continuity and broad object structure, then apply the selected procedure's construction and checks. Flat graphics favor controlled contours; outlined illustrations separate contour from color; painterly scenes start with broad shape/value relationships. Keep construction guides separate and hide them for delivery. Before finish, compare silhouette landmarks, negative spaces, overlaps and large value/color regions. Repair each identified error at its responsible owner or explicitly retain the limitation. Texture cannot close that check. Retain all inventoried detail targets.

Use native Krita shapes, brush paths and supported selections. Inspect preset names and schemas. Group objects with independently owned bases, components, tones and distinguishing marks. Place finish within its owner; preserve independent owners through delivery even when a studied painter merges. Reference imports stay locked/separate and hidden in reconstruction exports. Artwork construction uses native marks rather than reference slices or generated replacement composites.

Compare local light/color and boundary relationships against the reference. Calibrate an unfamiliar brush on a separate sample before relying on pressure, blending, texture or erasing behavior. Regional mark size/orientation matters; a global texture cannot substitute for missing geometry. If a mark/blend destroys a boundary or contaminates a sibling, repair the local owned transition and recheck the composite.

Use alpha inheritance inside the object's group above an opaque base when clipping is needed; it depends on the combined transparency below in that group. Keep the full-canvas background outside. Alpha lock affects existing pixels on its layer. Choose a supported native fill for the intended region: Prototype shapes use explicit fill/stroke booleans, while the separate Krita Control schema uses fill_style/stroke_style. A selection-fill action requires the intended selection and deselection afterward; it is not line-art flood fill. Confirm the visible result.

Treat caster/receiver marks as explicit dependencies. After moving, removing, recoloring or reshaping an item, rebuild affected contacts, shadows, reflections/refraction and exposed areas. Translating a painted reflection can leave baked surroundings wrong. The tested runtime did not move pixels with direct group translation; translate verified owned paint descendants/dependent marks or use a separately exercised transform, then inspect the projection.

## Compare and repair

Serialize live mutations. Refresh state after hierarchy/lifecycle changes and preview after a meaningful object or pass. A mutation timeout is an unknown outcome: inspect state/preview before deciding what remains. Save KRA checkpoints before long sequences; create output directories inside allowed roots before saving.

Compare with the reference hidden, in the same frame at whole-image and cropped scales. Diagnose placement/silhouette/spacing first, then local value/color, edges/materials and distinguishing detail. Mirror both comparison views when familiarity hides proportion drift; diagnostic viewing does not alter the deliverable. A pleasant palette, plausible texture or close bounding box does not prove contour fidelity.

Make each correction answer a concrete failure. Preserve prior candidates and reject regressions; the newest pass is not automatically best. Use the agreed job budget and record remaining errors instead of extending one case indefinitely. Historical project benchmark budgets do not authorize new trials or impose a fixed pass count on unrelated jobs.

Before a large corrective pass, classify the defect as geometry, ownership, light/volume, stroke flow, paint order or effect behavior. Use the [drawing diagnosis and native-operation checks](references/drawing-decisions.md#test-a-correction-before-extending-it), paint a limited region and compare the actual saved result before extending the procedure. If the same defect remains, change the procedure rather than repeat more of it.

Keep source flaws/ambiguity in the faithful master. When a justified anatomy, wording or light correction is needed, create a separate corrected version and list intentional changes. Expressive asymmetry, broken marks, wear and historical revisions are not automatic defects. Hidden geometry and absent glyphs remain labeled inference.

An explicitly requested wording/object change is a content variant; retain the reference master and name the variant by its requested change. Reserve defect-correction claims for an identified source flaw. Inventory actual visible geometry: a flower junction need not be a separate disk merely because a template says center.

## Verify and deliver

Exercise actual whole-object, component and identified-detail edits, including move/remove and recolor. Check vacated regions, dependent effects, shared joins and unrelated surroundings. Layer names/counts are not edit evidence. Save, reopen and repeat representative edits; raw serialization can change on reopen, so compare subsequent payload changes against a reopened/resaved baseline.

Deliver saved KRA and PNG, inventory-to-layer mapping, effect/inference record, selected edit variants and a concise limitations report. Hide guides/reference and restore intended visibility. Report fidelity, granularity, dependencies, text/font behavior and persistence separately. RGB error can supplement matching-frame inspection, but does not establish perceptual quality or editing coverage. Keep faithful and corrected fidelity judgments separate.

Match the actual exposed bridge schema; native API availability alone does not expose a usable vector/text creation action or every Krita UI feature. If an essential capability is unavailable, preserve supported work and report that requirement tool-limited. Painting a title does not fulfill editable typesetting or reusable-font delivery. Do not install tools, widen roots or modify user configuration without authorization.
