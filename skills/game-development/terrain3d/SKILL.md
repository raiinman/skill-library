---
name: terrain3d
description: Install and configure Terrain3D for Godot landscapes, heightmap import,
  terrain materials, collision and foliage LOD. Use for heightfield landscapes rather
  than volumetric caves.
license: MIT
---

# Terrain3D

Read [the source map](references/source-map.md) for pinned official docs and archived inputs. Before using API/build syntax, use Context7 for this exact library where available; otherwise use its official version-matched docs and headers. Honor the project's existing engine and dependency choices. Gather compatibility details from the project first, and request only genuinely missing blocking information.

Inspect the Godot version, renderer, target platform and existing add-ons. Choose a Terrain3D release whose documented compatibility matches them; a current development source snapshot is not automatically the correct binary release. Prefer a supported release/package and verify the upstream demo in an isolated project before introducing it into an existing world.

Preserve existing scenes and terrain data. Use a separate data directory for each distinct terrain map; share it between scenes only intentionally. Save shared material/assets resources when reuse is required. Back up data and review migration notes before replacing an installed add-on, avoiding stale mixed-version binaries.

For heightmaps, record resolution, orientation, horizontal spacing, vertical scale and offsets. Preserve adequate height precision, using supported high-bit-depth formats rather than treating an ordinary 8-bit color image as a calibrated height source. Start with one region and a known-height landmark, then add layers and foliage. Terrain3D is a heightfield; route caves/overhangs requiring actual terrain volume to a compatible volumetric solution instead of promising heightfield geometry can represent them.

Check camera-distance detail, region edges, collision against the visible surface, material texture channels, foliage density/LOD and persistence after reopening. Validate the target export and renderer; editor success alone does not prove release binaries or all platform renderers work.

Deliver the scoped integration or authored asset with reproducible dependency/conversion settings and the checks actually performed. Installation of this skill supplies guidance and source snapshots, not compiled SDKs, an engine plug-in, a live MCP service or evidence of game integration. Install/build a project dependency when the user's concrete integration task needs it. Preserve unrelated project files and existing assets; keep outputs and migrations recoverable.
