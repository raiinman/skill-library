# Source and adaptation

- Requested source: https://github.com/raiinman/skill-library/tree/1ff8501e6f5378a65b5dac987514e7498baa7cd5/skills/3d-and-web/img2threejs
- Pinned source entrypoint: https://github.com/raiinman/skill-library/blob/1ff8501e6f5378a65b5dac987514e7498baa7cd5/skills/3d-and-web/img2threejs/SKILL.md
- Source commit: `1ff8501e6f5378a65b5dac987514e7498baa7cd5`
- Original entrypoint SHA256: `e0c29eca4bba7759a2f8703dc4acd8aaabcc3f60aedf938b283b6ffd51531bcc`
- Original project: https://github.com/hoainho/img2threejs
- Original upstream pin recorded by that package: `d508b596cb221f1509f6e50ab68fce275a5cfb44`
- License: [Apache-2.0](LICENSE), with attribution in [NOTICE](NOTICE)
- Adapted: 2026-10-17

## Retained ideas

Reference suitability and observation before inference; macro-to-micro decomposition; subject-specific quality contracts; staged construction; matched-camera and off-axis review; critical-feature acceptance; bounded correction; honest uncertainty; and actual deformation evidence for requested rigs.

## Blender-native replacements

- Editable Blender collections, meshes, curves, modifiers, materials, and optional armatures replace TypeScript factories and browser scene objects.
- A subject-specific `build_scene.py` and saved `.blend` checkpoints replace the Three.js factory generator. No generic automatic image-to-mesh generator is claimed.
- Project-local JSON specifications and review history replace the upstream forge schema, state machinery, plugin registry, numeric scoring gates, and domain harness.
- `scripts/review_scene.py` captures beauty and neutral clay views from the saved Blender camera and four orbit angles, optionally reports projected landmark residuals, records geometry/resource warnings, hashes its evidence, and preserves the source file. Its measurements do not establish likeness or model validity.
- New reference guides adapt camera, materials, projection, characters, rigging, and export checks. Their conditional branches replace browser-only interaction and mandatory explode/click requirements.

The original entrypoint is archived byte-for-byte in `references/upstream-skill.md`. Its forge commands, linked internal documents, Three.js runtime, and optional plugins are archival context, not dependencies of this skill. The original `img2threejs` package remains available separately in the library. This is an independently runnable Blender workflow, not a claim that its entire forge suite was ported.

## Runtime and validation

Requires an installed Blender with its bundled Python. No pip or npm packages are required. The headless helper was tested with Blender 5.2.1 LTS on Windows using a generated asymmetric fixture with a modifier and a collection instance. Test artifacts are local, not included in the package. The revised smoke test verifies reopening, ten beauty/clay PNG captures, known landmark residuals, aspect and geometry reporting, source preservation, refusal to overwrite evidence, and invalid collection/landmark rejection. The standard-library checkpoint helper has separate preservation, containment, and changing-input tests. Subject fidelity, advanced rigs, and individual export formats still require task-specific testing.

## Evidence-driven revision, 2026-10-17

The toy-train reconstruction prompted camera/EXIF fitting before geometry corrections, neutral-clay acceptance, named landmark comparison, separate photo-material appearance findings, and exact build/spec/input snapshots per accepted checkpoint. The optional planar-image route reflects analysis of [Reality Fakers' tutorial](https://www.youtube.com/watch?v=BcjPCjxsCZo). Additional workflow ideas were reviewed against [blender-game-skills at f0ef29385a03de139957e6f700b801cdc00b7e29](https://github.com/majidmanzarpour/blender-game-skills/tree/f0ef29385a03de139957e6f700b801cdc00b7e29), MIT, copyright 2026 Majid Manzarpour. No code from that repository is vendored or installed. See [research findings](references/research-findings.md) for the inspected files, useful ideas, and limitations.
