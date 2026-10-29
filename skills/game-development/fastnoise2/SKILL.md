---
name: fastnoise2
description: Integrate Auburn FastNoise2 C++ SIMD noise graphs, seeded field generation
  and serialized node trees for procedural terrain or textures. Use for FastNoise2
  rather than the separate FastNoise Lite API.
license: MIT
---

# FastNoise2

Read [the source map](references/source-map.md) for pinned official docs and archived inputs. Before using API/build syntax, use Context7 for this exact library where available; otherwise use its official version-matched docs and headers. Honor the project's existing engine and dependency choices. Gather compatibility details from the project first, and request only genuinely missing blocking information.

Verify the exact library: FastNoise2 and FastNoise Lite have different APIs and are not interchangeable. Inspect the host C++ toolchain, supported SIMD targets, build configuration and existing generator. The pinned source describes a C++17 SIMD node-graph library with a separate visual Node Editor.

Prototype the smallest graph that produces the intended field: a base noise, useful fractal/blend/domain operations and explicit parameters. Store the graph/serialized representation, seed and library revision with the generated asset or world recipe. Verify decoding and compatibility when moving graphs between Node Editor and runtime versions.

Define world-space sampling coordinates, frequency, scale and numeric output interpretation before converting values to height, density or pixels. Generate neighboring chunks from a shared global coordinate convention so borders agree. Include required overlap for downstream meshing or normal calculation. Decide whether cross-platform reproducibility is required and test it under the chosen SIMD/backend settings rather than assuming bitwise equality.

Check constant/range edge cases, deterministic regeneration for the supported configuration, chunk seams, negative/large coordinates and representative generation throughput. The Node Editor preview is not a terrain runtime, persistence system or mesh/collision implementation. Preserve current world data or version the generation recipe when changing noise settings.

Deliver the scoped integration or authored asset with reproducible dependency/conversion settings and the checks actually performed. Installation of this skill supplies guidance and source snapshots, not compiled SDKs, an engine plug-in, a live MCP service or evidence of game integration. Install/build a project dependency when the user's concrete integration task needs it. Preserve unrelated project files and existing assets; keep outputs and migrations recoverable.
