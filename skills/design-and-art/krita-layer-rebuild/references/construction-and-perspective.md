# Construction and perspective

Read for rigid objects, architecture, vehicles, repeated elements, openings, curved surfaces or lettering attached to a surface. These procedures adapt Scott Robertson and Thomas Bertling, *How to Draw* (2013), to reconstruction. Page numbers below are one-based PDF pages in the studied 211-page copy. They are construction methods, not evidence of executed Krita behavior.

## Measure the projection before drawing details

1. Record reference dimensions and choose stable anchors: extremities, contact points, major corners and centers. Express their positions in the same image coordinates. Use ratios within an object as well as its bounding box; a correct box can contain the wrong contour.
2. Identify parallel-direction families from visible edges. Estimate horizon and convergence where supported. Rotated objects can have different vanishing points on a shared horizon. Sloping roofs have additional directions. Do not force an inconsistent generated image into a single ideal camera in the faithful master.
3. Draw a separate construction guide for the major planes, centerlines and overlaps. Establish near/far ordering before surface detail. Record uncertain camera assumptions and inferred hidden continuation.
4. Match extrema, bends and important empty spaces on the untextured scaffold. Compare both images mirrored if proportion drift becomes difficult to see. Adjust a local bend when the bend is wrong; scaling the entire object can break correct anchors.

**Check:** compare guide intersections, silhouette and gap ratios at equal scale. Every large discrepancy has an identified responsible contour or plane before rendering begins. Preserve source inconsistencies and list them for a separate corrected version.

Source: Robertson/Bertling PDF 19–26, 57–63, 99–100, 185–186; measured relations also follow the existing Proko/Mullins study synthesis. Perspective construction is a hypothesis about the image, not recovered camera metadata.

## Subdivide and repeat on a receding plane

For windows, tiles, ribs or a ruled label, establish the parent quadrilateral first. Its diagonals locate its projective center. Through that center, draw toward the relevant vanishing directions to divide the plane. For repeated adjacent units, use the midpoint/diagonal recurrence to extend spacing in perspective. For an arbitrary division count, divide an auxiliary line into equal intervals and transfer those divisions projectively to the target plane.

Keep a recipe for the shared module, but create independently owned instances for every promised visible unit. Record local deviations rather than replacing observed irregularities with a perfect grid. Equal world spacing normally becomes unequal screen spacing; distributing marks at equal pixel intervals can flatten the plane.

**Check:** near and far intervals shrink consistently with the observed projection; changing one window preserves its neighbors and supporting wall. Hide the repetition guides and inspect grouping and gaps again.

Source: Robertson/Bertling PDF 29–32. Numeric spacing comes from the reference, not a universal module size.

## Fit circles, rims and hinges to their planes

Construct the supporting plane or box before its ellipse. Locate center, cardinal contacts and the portions hidden by foreground lips. Fit the observed conic to these constraints; a convenient ellipse-axis heuristic is not an exact rule for every arbitrary projection. Give a cup's front lip, back lip, inner wall and liquid surface separate ownership where visible. A tilted lid rotates about a spatial hinge; simply rotating its flat screen drawing will generally produce the wrong opening.

**Check:** ellipse contacts agree with the plane, thickness stays plausible around the rim, and front/back contour interruptions match the reference. Editing the liquid level leaves the rim intact. Moving the lid preserves its hinge contact or explicitly updates the attachment.

Source: Robertson/Bertling PDF 71–78, 107–108. The faithful target can contain imperfect ellipses; do not silently regularize them.

## Build curved volumes from profiles and sections

Use a side profile and top footprint with corresponding stations for a vehicle, handle, bottle or other complex solid. At each station, define a cross-section; shared intersections must agree. The visible envelope follows the sections and their tangent transitions. Use these guides to resolve a local contour rather than adding texture over a malformed volume.

For a rounded corner, construct the tangent transition between adjacent faces; blurring a sharp corner does not change its geometry. For a handle or arch, define the outer boundary, inner aperture, thickness and attachment roots. The aperture must expose whatever background is underneath. Keep inferred rear geometry separate from observed contours.

**Check:** section intersections agree; attachment roots meet their receiver; the opening remains transparent over a changed background. Moving a handle carries its owned shading and updates contact shadows, without carrying a background-colored plug.

The inspected bridge path implementation connects supplied points with straight segments; it does not expose editable Bezier controls. Use sufficiently resolved manually authored coordinates or another verified native route, and inspect actual curvature at output size. Calling a sampled polygon a curve does not establish editable curve handles.

Source: Robertson/Bertling PDF 81–91, 175. A sectional construction is useful when volume is ambiguous; simple flat graphics need only their actual contour geometry.

## Put graphics on a surface

Construct the wording or motif in a flat local coordinate system first. Record its baseline, bounds and repeated spacing. Apply a common plane transform for planar signs. A cylindrical label additionally needs curvature-aware mapping; one planar warp cannot reproduce all wrapping. Preserve the unwarped editable master and document the mapping between master and visible instance.

**Check:** editing one glyph or motif updates its mapped instance; counters remain open; the label follows the surface rather than floating on it. If available tools cannot preserve that editing route, report the limitation instead of calling a baked surface patch editable text.

For fabric or another locally uneven receiver, establish broad perspective/curvature before local wrinkle deformation. Retain the flat master, broad transform, local mapping guide and material response as distinct controls. Build guides from owned surface construction; brightness alone confounds pigment, lighting and height. After a motif or fold edit, regenerate the affected instance and compare with local deformation disabled to detect doubled wrinkles or unintended waviness. Preserve each promised motif's identity through both stages.

Source: Smith, [surface displacement workflow](https://photoshopcafe.com/best-way-to-make-displacement-maps-in-photoshop-wrap-anything-around-any-surface/). The source uses photographic channel maps; native guide construction is our adaptation. Krita [transform masks](https://docs.krita.org/en/reference_manual/layers_and_masks/transformation_masks.html) offer reversible transforms in the application, but require an exercised agent route. Complex previews may lag, and changing transform mode can discard the stored transform; checkpoint before changing modes and inspect the settled projection.

Source: Robertson/Bertling PDF 92; typography construction is detailed in [text-and-fonts.md](text-and-fonts.md).
