# Camera fitting before proportion changes

## Establish the evidence

Read local EXIF where available, such as with Pillow's `getexif()`. Preserve the reference file and orientation. Record pixel size, crop, pixel aspect, projection hypothesis, and any focal-length evidence. A phone's physical focal length and its 35mm-equivalent value are different quantities: use physical focal length with the actual sensor size, or equivalent focal length with a 36mm-wide sensor approximation. Do not combine equivalent focal length with the small physical sensor. EXIF is a starting hypothesis; cropping and editing can invalidate it.

Distinguish orthographic art from a long-lens photograph. Perspective can change near/far wheel sizes even when parallel edges seem almost parallel. An uncalibrated photo supplies projected ratios, not manufacturing dimensions. Preserve the existing project's units and state which sizes are inferred.

## Fit with a blockout

Record several stable landmarks appropriate to the subject: roof corners, wheel centers, a jaw point, joint centers, base contacts, or opening corners. Use the same visible physical point in the photo and model. A shared camera error often shifts several landmarks coherently; an isolated part error suggests geometry. Off-axis views remain necessary because projected point matches do not determine hidden depth.

Fit projection, camera direction, focal length/distance, shift, and framing before changing individual part dimensions. Lock the candidate camera while testing a geometry correction. If a later camera change is necessary, record it and recapture all geometry comparisons; do not compare evidence from different cameras as a material improvement.

Keep full-frame overlays or pixel-coordinate errors. A separately centered/resized silhouette comparison can diagnose shape, but it hides absolute placement and scale. World-registered silhouette gates need a cleaned orthographic reference, known scale, and common axes. Background segmentation from a photo can mistake shadows or pale surfaces for foreground/background, so inspect masks before trusting IoU. Use subject-specific tolerances; there is no universal passing likeness percentage.

## Optional projected landmark report

Pass `--landmarks C:/project/landmarks.json` to `review_scene.py`. Coordinates in `reference_px` are measured from the top-left of the full reference, before helper output resizing. `local` is a point in the named object's local coordinate system, not a guessed mesh index. An explicitly placed empty in the model collection is useful for attachment landmarks.

```json
{
  "reference_size": [1024, 668],
  "points": [
    {"id": "front-wheel-center", "object": "FrontWheel", "local": [0, 0, 0], "reference_px": [830, 560], "tolerance_px": 12}
  ]
}
```

These example values illustrate the toy-train test; measure the actual subject rather than copying them. The helper validates the data, requires the saved reference camera, and reports projected coordinates and pixel residuals in the original reference frame. A tolerance result concerns that point alone, not 3D fidelity. Image coordinates do not establish metric scale. Occluded, ambiguous, or behind-camera points cannot establish a passing landmark.

For material review, keep renderer, camera, view transform, exposure, and lights fixed. Diagnose lighting, roughness, reflections, and base color separately. A moving-light render is useful when the requested material must work beyond one studio view; it is not a required animation deliverable for a static prop.
