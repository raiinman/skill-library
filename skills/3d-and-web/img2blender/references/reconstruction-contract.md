# Reconstruction contract and progress

Use ordinary project-local JSON, not the Three.js `ObjectSculptSpec` schema. Keep the contract specific enough to rebuild and review this subject. The following is a shape example, not a substitute for inspecting the user's image:

```json
{
  "subject": "reference subject",
  "references": [{"path": "reference.png", "role": "primary"}],
  "intendedUse": "editable static Blender asset",
  "style": "follow reference",
  "coordinates": {"up": "+Z", "front": "-Y", "scaleBasis": "overall height = 1, inferred"},
  "collection": "Model",
  "components": [
    {"id": "body", "parent": null, "form": "observed volume and dimensions", "construction": "chosen Blender geometry strategy", "material": "body-finish", "evidence": "named region in reference"}
  ],
  "materials": [{"id": "body-finish", "response": "observed finish", "textureSource": null}],
  "criticalFeatures": [{"id": "distinctive-feature", "component": "body", "acceptance": "specific visible shape and placement", "reviewView": "reference camera and close-up"}],
  "review": {"primaryCamera": "ReferenceCamera", "otherViews": ["front", "right", "rear", "left"], "maxCorrectionsPerPass": 3, "maxCorrectionsTotal": 6},
  "budget": {"triangles": null, "reason": "set only if target requires a bound"},
  "unknowns": [{"region": "rear", "assumption": "subject-specific inference", "confidence": "low"}]
}
```

Use Blender's Z-up convention by default for a new scene, but retain an existing project's frame. Define anatomical left/right separately from camera-left. `front = -Y` is an example convention, not an automatic interpretation of a photograph or the helper's axis labels.

For articulated objects, add joints, local origins, attachment constraints, and required motions. For game assets, add topology/UV/texture requirements and the requested export target. For print models, add actual dimensions, closed-surface requirements, and printability checks; a visual reference alone cannot supply calibrated dimensions.

## State on disk

Keep `.img2blender/spec.json`, `build_scene.py`, versioned `.blend` files, and per-pass evidence directories. Append one JSON object per review to `.img2blender/reviews.jsonl`, for example:

```json
{"pass":"blockout","iteration":1,"action":"refine-code","blend":"passes/blockout-01.blend","evidence":["review-01/reference.png","review-01/orbit-000.png"],"changes":"named parameters changed this iteration","defects":["specific mismatch with reference"],"reason":"volume differs despite matching front outline"}
```

Actions: `continue`, `refine-spec`, `refine-code`, `request-input`, or `stop`. Count correction rounds from the recorded `refine-*` decisions. Record the best version so a later correction cannot silently replace it with a worse result. A record without inspected render evidence cannot establish visual acceptance.

No extra state daemon, plugin registry, neural model, or scoring service is required. The agent owns semantic review; the helper owns capture and descriptive scene measurements.
