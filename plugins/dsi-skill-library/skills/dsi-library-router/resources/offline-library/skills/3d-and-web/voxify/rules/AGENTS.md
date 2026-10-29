# Voxify Voxelization Rules

These rules govern all voxelization, Geometry Nodes modifier manipulation, and mesh baking tasks performed with Voxify.

## 1. Scale Hierarchy and Bounding Box Integrity
- Always apply object scale (`Ctrl + A > Scale`) on the source mesh prior to voxelization, or verify that object dimensions match intended real-world proportions.
- Do not set arbitrarily small voxel sizes (< 0.005m) on large objects (> 10m) without checking the bounding volume first, as dense 3D grids can consume substantial memory.
- Default to `max(dimensions) / 35.0` to maintain responsive viewport interactive feedback before refining voxel granularity.

## 2. Non-Destructive Source Mesh Preservation
- The Voxify modifier operates via a distinct container object referencing the source mesh via `ObjectToVoxelize`.
- Never delete or permanently alter the source mesh during voxelization. Keep the original intact and toggle its viewport/render visibility (`hide_viewport`, `hide_render`).

## 3. Display and Generation Efficiency
- Use `ViewportAs: PointCloud` when working with high vertex counts or complex scenes for rapid navigation.
- Switch to `ViewportAs: Voxels` for final composition, lighting, silhouette critique, and camera alignment.
- Use `Generation: Fast` (OpenVDB density grid) for standard manifold meshes; switch to `Generation: Exact` (raycast grid) when handling non-manifold or thin-walled surfaces.

## 4. Baking and Export Preparation
- When preparing voxel assets for game engines (Unreal, Unity, Godot, Three.js) or 3D printing, realize instances and bake to real geometry using `voxify_bake_to_mesh`.
- Verify resulting polygon counts and material slot assignments post-bake.
