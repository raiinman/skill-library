# Reference analysis

Adapted from img2threejs's image-analysis and suitability workflow for native Blender modeling.

## Inspect before coding

1. Identify the target and distinguish it from the background. Establish whether the request concerns one object, a character, or an entire scene. Scene work needs a spatial layout and separate subjects; an ambiguous target needs clarification.
2. Describe the bounding proportions, silhouette, symmetry, major curves, negative spaces, and camera perspective. Use relative measurements when no real scale is known. Separate object-space directions from image-space observations.
3. Decompose major assemblies into visible subparts and local features. Name how parts attach: continuous shell, overlap, socket, hinge, embedded element, or free space. An organic volume needs an appropriate connected surface, not a pile of disconnected primitives.
4. Describe material response by region: base color, metallic versus dielectric, roughness, transparency, subsurface behavior, bump/displacement, and patterned finish. Distinguish illumination in the photo from surface pigment. Material estimates are hypotheses, not recovered physical measurements.
5. Inventory identity features such as an unusual notch, face proportions, markings, fastener layout, lettering, or wear. Tie each to its visible image region, model component, and review view. Include a close-up when the feature would disappear in a full-frame render.
6. Record hidden, occluded, blurred, and ambiguous regions with a confidence description and consequence. State assumptions about unseen backs and interiors. More views improve confidence but do not establish real-world scale without a measurement.

Keep the user's requested realistic, stylized, or low-poly direction. If none is specified, follow the reference's visual language and state the approximation. Do not require an arbitrary feature count for a simple object.

## Character branch

Record head-to-body proportion, shoulder/hip width, limb lengths, joint and facial landmarks, pose, asymmetry, clothing boundaries, and hair silhouette. Establish the subject's own left/right in the project's coordinate frame. A reflected part can require normal correction; rotating one limb is not a substitute for mirroring its shape.

Match head and body volumes before hair or accessories. Build hair with Blender curves, sculpted clumps, geometry, or cards as appropriate to the requested style and target. Verify scalp coverage and roots in angled views. Rig or simulate hair only when needed for the requested motion.

For likeness-sensitive work, review eyes, nose, mouth, jaw, and head shape individually. Report the limits of the supplied evidence without an unsupported exact-likeness claim.

## Image textures and projected details

Use procedural materials for suitable unpatterned surfaces. A supplied painted pattern, decal, or logo may need a cropped image texture, UVs, or camera projection. Record its source and permitted use. Photo highlights and shadows are baked illumination; mitigate double lighting through careful source preparation and shading choices, and explain residual artifacts. Single-view projection stretches on unseen surfaces, so inspect coverage from other views and distinguish inferred back-side treatment.

Prefer extracting a decal's color/alpha from its underlying surface when practical, rather than wrapping the entire photographed side as presumed albedo. Keep raw and prepared versions and document preparation. Do not promise that one photo can be perfectly de-lit. Inspect the material under fixed neutral lighting and, when useful, another light direction. Preserve the same color-management settings across iterations and treat Standard versus AgX as a project/look choice, not a universal correction.

Keep two findings: geometry fidelity from clay/landmarks, and appearance fidelity with materials. Explicitly identify details that come directly from source pixels so a photo-textured label does not overstate independent modeling accuracy.

Silhouette-changing features need geometry. Surface color does not replace a notch, opening, seam depth, or continuous contour.
