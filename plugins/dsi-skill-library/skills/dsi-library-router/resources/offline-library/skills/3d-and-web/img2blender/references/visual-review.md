# Visual review and correction

## Compare like with like

Keep the reference camera, aspect, framing, view transform, and lighting stable while diagnosing geometry. A reference camera is fitted by observing the image; automatic orbit cameras do not solve that calibration. Put the reference and current render side by side using the host's vision tools. Inspect close crops for small identity features.

Review neutral clay before materials and retain it beside the final beauty render. The helper's clay override removes material colors and photo labels, but also removes transparency/displacement from materials; alpha-cutout hair/leaves, glass, and shader-displaced forms need a separate appropriate geometry or opacity-preserving check. Scene modifiers still evaluate. Neutral clay is a diagnostic, not the final appearance.

Measure corresponding landmarks or full-frame bounds before accepting a proportion correction. Inspect the uncropped reference frame as well as any aligned silhouettes. For an actual game asset, also inspect the intended on-screen pixel size; do not impose a game-camera test on every Blender illustration.

Review in this order:

1. Camera, overall scale, and perspective.
2. Silhouette, negative spaces, depth, cross-sections, and major proportions.
3. Continuous surfaces, connections, attached parts, and symmetry or intended asymmetry.
4. Internal identity features, face landmarks when applicable, and small defining details.
5. Material boundaries, pattern alignment, texture coverage, roughness, and lighting.
6. Requested motion, exported representation, and the measured performance budget.

Change one related defect group, then recapture. A bevel or lighting tweak cannot repair the wrong volume. Check the same model from the primary view and meaningful off-axis views; a good outline can hide a flat cutout, open skull, floating accessory, or wrong thickness.

Critical features are individually blocking. A global resemblance score cannot compensate for missing eyes, the wrong grip, a mirrored marking, or a detached part. Describe likeness with evidence; pixel similarity varies with framing and background and is not an automatic fidelity verdict.

## Blender-specific checks

- Inspect scale, outward normals, modifier results, intersections, UV seams, and material assignments. Negative scale is a review clue, not proof of wrong normals. Manifold requirements depend on intended use; thin cards are not automatically invalid for a game asset.
- Evaluate geometry after modifiers and instances when estimating the actual target budget. The helper's viewport dependency-graph counts are descriptive and can differ from final render or exported geometry. Audit those routes separately where the budget matters.
- Inspect the file's external textures and linked libraries, then reopen the delivered file in a fresh process. Packed assets still need source attribution and appropriate usage rights.
- Test requested exports by reimporting into a clean scene or the chosen target. Compare orientation, scale, hierarchy, material support, and animation. A correct `.blend` does not prove a correct GLB/FBX/STL.

## Motion branch

Adding an armature is not proof of a working rig. Check parent/inverse transforms, weights, joint placement, rest/bind pose, and modifier order. Render representative frame samples and extreme required poses. Verify that the mesh actually deforms, attached parts stay attached, the root moves as intended, and neutral pose retains the approved likeness. Review looping separately from root travel. Report untested motions.

## Finish or stop

Continue only when the current pass meets its subject-specific acceptance criteria. Refine the spec when the planned structure is wrong; refine code when a sound plan was implemented incorrectly. At the correction limit, preserve evidence and state what new view, manual step, or accepted approximation would unblock progress. Do not inflate a score or replace critical criteria to make a run pass.
