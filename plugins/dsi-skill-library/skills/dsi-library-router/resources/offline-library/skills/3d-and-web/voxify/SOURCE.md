# Source and adaptation

- Upstream Tool: Voxify - Mesh To Voxel Modifier v1.2 for Blender
- Author: Masoud Rezaei (Cartesian Caramel)
- Product: https://superhivemarket.com/products/voxify
- Target Environment: Blender 4.0+ and 5.2+ (LTS)
- Adapted: 2026-10-21.

## Adaptation details

- Packaged as a native Blender add-on with automatic Asset Library registration and 3D Viewport N-panel sidebar UI.
- Implemented standalone zero-dependency JSON-RPC 2.0 stdio Model Context Protocol (MCP) server for Antigravity and Codex.
- Provides 7 dedicated MCP tools (`voxify_mesh`, `voxify_list_objects`, `voxify_get_settings`, `voxify_set_settings`, `voxify_bake_to_mesh`, `voxify_toggle_source`, `voxify_add_demo`).
- Supports non-destructive source mesh referencing, automatic bounding-box adaptive voxel resolution, and one-click instance realization/baking.
