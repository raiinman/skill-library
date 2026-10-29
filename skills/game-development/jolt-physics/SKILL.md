---
name: jolt-physics
description: Integrate or debug Jolt Physics rigid bodies, collision layers, constraints,
  queries and simulation stepping in a native game engine or an existing engine binding.
license: MIT
---

# Jolt Physics

Read [the source map](references/source-map.md) for pinned official docs and archived inputs. Before using API/build syntax, use Context7 for this exact library where available; otherwise use its official version-matched docs and headers. Honor the project's existing engine and dependency choices. Gather compatibility details from the project first, and request only genuinely missing blocking information.

Identify the host engine and its current physics backend first. If the engine already exposes a supported Jolt integration, use that route rather than embedding a second physics world. For a custom C++ host, inspect the pinned Build guide and HelloWorld example before writing initialization code.

Establish scale, coordinate axes, body ownership, lifetime, collision layers and thread boundaries. Set up the allocator, factory/type registration, physics system, temporary allocator and job system using the selected version's supported sequence. Keep globally shared registration alive until dependent systems are destroyed. Use body IDs and locking interfaces correctly across threads; callbacks must obey the API's update/thread restrictions.

Drive simulation with a fixed-step accumulator and a bounded catch-up policy, separating render interpolation from physics time. Configure moving/static collision filters, activation and shape settings explicitly. Inspect collision-step and CCD needs against measured high-speed contacts rather than increasing every solver setting. Preserve the project's existing units and shutdown ownership.

Verify a falling dynamic body resting on static ground, layer-filter exclusion, queries, body removal, repeated init/shutdown and a large-frame spike. Test character/vehicle/ragdoll features only when requested. Compare behavior and frame cost with the previous backend before replacing project-wide physics.

Deliver the scoped integration or authored asset with reproducible dependency/conversion settings and the checks actually performed. Installation of this skill supplies guidance and source snapshots, not compiled SDKs, an engine plug-in, a live MCP service or evidence of game integration. Install/build a project dependency when the user's concrete integration task needs it. Preserve unrelated project files and existing assets; keep outputs and migrations recoverable.
