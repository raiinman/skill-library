---
name: ozz-animation
description: Integrate ozz-animation offline asset conversion, runtime skeleton/clip
  loading, sampling, blending and local-to-model transforms in a custom engine or
  animation pipeline.
license: MIT
---

# ozz-animation

Read [the source map](references/source-map.md) for pinned official docs and archived inputs. Before using API/build syntax, use Context7 for this exact library where available; otherwise use its official version-matched docs and headers. Honor the project's existing engine and dependency choices. Gather compatibility details from the project first, and request only genuinely missing blocking information.

Separate offline authoring/import data from compact runtime skeleton and animation structures. Inspect the project's toolchain, clip format, skeleton, coordinate system and skinning/rendering code before replacing playback. ozz is renderer/engine agnostic, not an automatic humanoid retargeter or complete game animation controller.

Use the version-matched conversion tools or implement an importer with the offline libraries. Keep source assets and conversion settings reproducible. Validate skeleton/clip compatibility, joint hierarchy/order, rest pose, duration, unit scale and serialized archive type/version before runtime use. Review individual sample/model licenses separately from the code license when redistributing assets.

At runtime, load validated archives, allocate buffers for the skeleton's SoA transform counts and model-space matrices, and size each sampling context correctly. Sample clips into local transforms, blend required layers/masks/rest-pose contributions, then convert through LocalToModelJob before passing the resulting transforms to the host's skinning pipeline. Coordinate root motion, attachments and update order with gameplay rather than applying movement twice.

Test clip endpoints, loop boundaries, reverse/seek behavior, crossfades, zero or partial weights, missing data and differently sized skeletons. Inspect actual deformation and attachment motion, not only the existence of sampled arrays. Measure memory/playback cost on representative character counts.

Deliver the scoped integration or authored asset with reproducible dependency/conversion settings and the checks actually performed. Installation of this skill supplies guidance and source snapshots, not compiled SDKs, an engine plug-in, a live MCP service or evidence of game integration. Install/build a project dependency when the user's concrete integration task needs it. Preserve unrelated project files and existing assets; keep outputs and migrations recoverable.
