---
name: recast-navigation
description: Integrate Recast Navigation navmesh generation, Detour path queries,
  tiled navigation, tile-cache obstacles and crowd movement. Use for native navigation
  systems or debugging existing engine integrations.
license: Zlib
---

# Recast Navigation

Read [the source map](references/source-map.md) for pinned official docs and archived inputs. Before using API/build syntax, use Context7 for this exact library where available; otherwise use its official version-matched docs and headers. Honor the project's existing engine and dependency choices. Gather compatibility details from the project first, and request only genuinely missing blocking information.

Identify whether the engine already owns a Recast/Detour integration. Use its navigation APIs for ordinary engine gameplay; embed the native libraries only for a requested custom navigation layer. Separate Recast mesh generation, Detour query/path runtime, optional DetourTileCache updates and DetourCrowd local steering.

Establish world axes, geometry winding, scale and the agent's radius, height, step/climb and maximum slope. Recast settings mix world units and voxel counts: derive them from chosen horizontal/vertical cell sizes instead of treating every value as meters. Choose tiled generation and memory/query budgets from level size and streaming needs.

Build a small navmesh from actual walkable geometry. Locate start/end polygons with meaningful extents and filters, inspect query status/partial paths and resolve off-mesh links and area costs deliberately. A successful path query is not proof the full destination was reached. Make asynchronous tile or obstacle updates observable and wait for their completion before assuming a new obstacle affects pathing.

Validate narrow doors, low ceilings, stairs, disconnected islands, blocked routes, large/small agents, tile borders and changing obstacles. Crowd avoidance is local steering, not a general collision/locomotion replacement. Test serialization/version compatibility and target-engine integration if navmesh data is shipped or streamed.

Deliver the scoped integration or authored asset with reproducible dependency/conversion settings and the checks actually performed. Installation of this skill supplies guidance and source snapshots, not compiled SDKs, an engine plug-in, a live MCP service or evidence of game integration. Install/build a project dependency when the user's concrete integration task needs it. Preserve unrelated project files and existing assets; keep outputs and migrations recoverable.
