# Planar images, emblems, and reliefs

Use this branch when the requested object is actually an extruded graphic, relief, stencil, sign, or similar shallow form. A displaced plane is not a substitute for rebuilding the volume of a photographed vehicle or character.

## Choose the simplest appropriate geometry

- Existing vector paths: import or reconstruct closed outlines as Blender curves, retain holes as interior contours, then extrude and bevel to the requested thickness. Inspect fill direction, disconnected islands, and scale. Raster tracing may help when only a clean graphic exists, but review its paths rather than trusting an automatic trace.
- Raster silhouette: extract a reliable outline or mask, preserve holes and disconnected components, simplify within a visible error bound, then give the shape thickness. Dimensions remain inferred unless supplied.
- Intended height field: image or height-map displacement can create relief. State which value controls height, its range and polarity, sampling density, and the assumed flat backing. Luminance is not physical scene depth; lighting and painted detail can become false bumps.

Keep a coarse preview before increasing mesh density. Choose sampling from the smallest required feature and memory budget. Repeatedly subdividing a dense grid can multiply geometry rapidly. Review the outline after smoothing and simplification, since those operations can shrink corners, close holes, and erase identifying features.

For closed objects, inspect side walls, backing, normals, and manifoldness after extrusion or Solidify. Filling every loop with one face can erase a hole. Keep reversible modifiers or a pre-application checkpoint; apply them to a delivery copy only when the target requires it. A print-ready claim needs its own dimensions and topology checks.

## Tutorial interpretation

[Reality Fakers' tutorial](https://www.youtube.com/watch?v=BcjPCjxsCZo) demonstrates a plane matched to image aspect, dense subdivision, image displacement, removal/flattening of unwanted regions, outline smoothing, simplification, and thickness/bevel cleanup. Useful stages occur around 0:24 (aspect), 1:33 (displacement), 3:33 (smoothing), 4:44 (simplification), and 5:39 (holes/thickness). This is an extruded graphic workflow, not general single-photo 3D recovery. Its demonstrated subdivision and smoothing amounts are example settings, not defaults for every image.

The review used the exported auto-generated transcript and sampled video frames. Operator intent was checked against the visible demonstration; transcript key names can be inaccurate. Current Blender APIs and hole/normal behavior need verification in the installed version.
