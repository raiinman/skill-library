---
name: meshoptimizer
description: Integrate meshoptimizer mesh indexing, cache/fetch optimization, simplification,
  quantization, meshlets and mesh compression. Use for measured asset-pipeline or
  renderer mesh-efficiency work.
license: MIT
---

# meshoptimizer

Read [the source map](references/source-map.md) for pinned official docs and archived inputs. Before using API/build syntax, use Context7 for this exact library where available; otherwise use its official version-matched docs and headers. Honor the project's existing engine and dependency choices. Gather compatibility details from the project first, and request only genuinely missing blocking information.

Inspect the input vertex layout, index type, topology, submeshes, material boundaries, skinning/morph streams and target renderer/asset format. Retain source geometry and define accepted visual/error limits before lossy changes. Use an existing engine/import pipeline integration if it already provides the requested operation.

Follow the version-matched recommended order. Establish indexing/remaps, optimize triangle order for vertex cache, optionally optimize overdraw when valid, and optimize vertex fetch after finalizing triangle order. Apply the selected quantization/filtering and encoding steps against target requirements. Reorder every affected attribute stream, not just positions; preserve per-primitive and animation data mappings.

Treat simplification as a separate error-controlled operation with appropriate border/seam/attribute handling. Ratios and returned counts are not visual acceptance. Triangle reordering can change alpha-blended rendering or primitive-ID semantics; preserve required ordering. Quantization requires explicit decode transforms and bounds handling. Compression saves storage/bandwidth and still requires a compatible decoder, version and runtime format integration.

Test index bounds, degenerate handling, material/UV seams, skinning and morph data, decode round trips and representative silhouettes/LOD transitions. Measure file size, decode time and rendering/cache metrics separately. Keep a reversible artifact chain and report lossy versus lossless changes clearly.

Deliver the scoped integration or authored asset with reproducible dependency/conversion settings and the checks actually performed. Installation of this skill supplies guidance and source snapshots, not compiled SDKs, an engine plug-in, a live MCP service or evidence of game integration. Install/build a project dependency when the user's concrete integration task needs it. Preserve unrelated project files and existing assets; keep outputs and migrations recoverable.
