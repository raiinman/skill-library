# Findings used in this revision

Reviewed 2026-10-17. These are scoped findings, not a requirement to install either an external skill package or a new Blender addon.

## Toy-train test

The local Chessie System toy-train reconstruction exposed five concrete weaknesses: camera evidence was used late; photo paint made the model look closer than its geometry alone; wheel centers and roof corners needed measured comparisons; photographed shading was lit again in Blender; and earlier `.blend` checkpoints did not retain their exact earlier build scripts.

The revised workflow therefore fits a camera first, reviews clay and named landmarks before texture, separates geometry from appearance findings, records photo-material preparation and lighting limits, and snapshots each accepted checkpoint's exact script/spec/explicit inputs. The revised helper supports neutral captures and projected pixel residuals. Neither feature assigns an automatic likeness score.

Rechecking the saved train at its original 1024 x 668 reference size exposed about 38 pixels of rear-wheel-center error versus about 7 pixels at the front wheel, using manually estimated image landmarks. This confirms that convincing photo paint concealed a localized placement mismatch. Those residuals are approximate image-space diagnostics, not metric dimensions or an overall fidelity percentage. A clay-only capture and a seven-file build checkpoint were also created without changing the delivered `.blend`.

## Tutorial

[Reality Fakers: Turn Any 2D Image to 3D Model](https://www.youtube.com/watch?v=BcjPCjxsCZo) was reviewed through its exported auto-generated transcript and sampled browser playback. The demonstrated method targets a graphic outline: displacement separates image regions, then cleanup and extrusion create a shallow solid. Its useful addition is the conditional [planar-image route](planar-images.md). It does not recover a photographed object's unseen sides or infer physical depth from luminance. This is a workflow analysis, not a frame-by-frame reproduction; no tutorial assets or transcript are redistributed.

## blender-game-skills repository

Source: [majidmanzarpour/blender-game-skills](https://github.com/majidmanzarpour/blender-game-skills/tree/f0ef29385a03de139957e6f700b801cdc00b7e29), pinned at `f0ef29385a03de139957e6f700b801cdc00b7e29`. MIT, copyright 2026 Majid Manzarpour. Reviewed the entrypoint, Blender-version notes, build template, comparison script, world-registration script, validator, and round-trip script. No upstream code is copied or installed by this revision; implementations added here are independent.

Useful ideas: clay before surface polish, measured proportions, persistent build phases, full-frame/world-registered checks where calibrated, checks at actual gameplay size for game assets, and export/reimport evidence. Rig, LOD, collision, baking, and animation branches belong only to requests that need them.

Specific limitations found by code inspection at this pin:

- `compose_review.py` normalizes and centers silhouettes for its IoU. This helps shape comparison but conceals translation and uniform scale errors. Its render mask uses alpha, so an opaque background becomes foreground. The reference corner-color heuristic needs a reviewed mask for photographs.
- `world_gate.py` computes measurements but does not enforce a pass threshold or nonzero failure exit. Successful execution is not gate acceptance.
- `validate.py` silently skips missing requested collections and can finish with an empty mesh selection and no failures. A consumer must assert that intended geometry was actually selected.
- `roundtrip.py` inventories imported bones and clips and checks height/resources, but accepts no manifest argument and does not automatically compare those names or clip lengths against the export manifest. That comparison remains a separate required check.
- The build template disables backup versions before saving the master. Our workflow keeps explicit immutable checkpoints instead of relying on overwrite/backup behavior.

These findings are static source review, not an end-to-end evaluation of the external package. Do not adopt fixed IoU thresholds for every photo, assume an empty validator result is success, or describe a manifest inventory as a verified manifest match.

## Verified API basis

Current official Blender API documentation was consulted through Context7 for [material overrides](https://docs.blender.org/api/current/bpy.types.ViewLayer.html), [camera projection](https://docs.blender.org/api/current/bpy_extras.object_utils.html), and [curve extrusion](https://docs.blender.org/api/current/bpy.types.Curve.html). Runtime behavior is tested on the installed Blender 5.2.1 LTS; this does not establish compatibility with every older release.
