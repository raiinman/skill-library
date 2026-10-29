---
name: effekseer
description: Author or integrate Effekseer particle effects, runtime playback and
  renderer-specific or engine plug-in handoffs. Use for effect assets, resource loading
  and VFX playback issues.
license: MIT
---

# Effekseer

Read [the source map](references/source-map.md) for pinned official docs and archived inputs. Before using API/build syntax, use Context7 for this exact library where available; otherwise use its official version-matched docs and headers. Honor the project's existing engine and dependency choices. Gather compatibility details from the project first, and request only genuinely missing blocking information.

Separate effect authoring in the editor from playback in the destination engine. Inspect the host engine, render API, effect editor/runtime versions and the platform. Use the supported engine integration where one exists; for a custom host, follow the matching runtime and renderer sample. The upstream master branch explicitly identifies itself as development, so select a supported production release rather than treating this documentation pin as a release recommendation.

Keep the editable source effect and export it with all referenced textures, models, materials and other dependencies required by the chosen runtime. Use version-matched formats and resource loaders. Establish axes, handedness, effect scale, camera/projection matrices, update timing and any depth/soft-particle requirements.

Manage effect handles, manager/renderer ownership, resource loading/unloading and device resets within the host lifecycle. Update and draw at the intended point in the frame; avoid accidentally advancing an effect twice through both an engine plug-in and a manual tick. Do not assume an effect is self-contained merely because its main file loads.

Test playback start/stop, looping, pause/time scale, resource reload, off-screen behavior and representative effect overdraw. Verify packaged dependencies in an exported game, not just the editor preview. Scope budgets for particle count and transparency from the target platform; retain license notices for the editor/runtime components actually redistributed.

Deliver the scoped integration or authored asset with reproducible dependency/conversion settings and the checks actually performed. Installation of this skill supplies guidance and source snapshots, not compiled SDKs, an engine plug-in, a live MCP service or evidence of game integration. Install/build a project dependency when the user's concrete integration task needs it. Preserve unrelated project files and existing assets; keep outputs and migrations recoverable.
