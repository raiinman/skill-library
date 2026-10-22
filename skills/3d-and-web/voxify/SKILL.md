---
name: voxify
description: Procedural mesh-to-voxel modifier workflows in Blender using Voxify Geometry Nodes. Use when voxelizing meshes, adjusting voxel resolution, configuring procedural materials, setting up assembly/disassembly animations, or baking instances into real geometry.
---

# Voxify: Mesh to Voxel Toolkit

Voxify is a Geometry Nodes modifier and procedural voxelization system for Blender created by Masoud Rezaei (Cartesian Caramel). This skill provides direct control over Voxify via the `voxify` MCP tools or Blender Python API.

---

## When to Use This Skill

Activate this skill when:
- Converting 3D meshes into stepped voxel or Lego-style structures.
- Controlling procedural voxel size, grid density, or inside/outside volume filling.
- Animating voxel build-up or assembly/disassembly sequences.
- Realizing and baking procedural voxel instances into editable polygon meshes for game engines (Unreal, Unity, Godot, Three.js) or 3D printing.
- Inspecting or batch-voxelizing assets in Blender scenes.

---

## MCP Tools Reference

The `voxify` MCP server exposes high-level tools communicating directly with Blender:

| Tool | Purpose | Key Parameters |
| :--- | :--- | :--- |
| `voxify_mesh` | Voxelize a target mesh object | `object_name`, `voxel_size`, `viewport_as` ("Voxels" / "PointCloud"), `generation_mode` ("Fast" / "Exact"), `custom_voxel`, `keep_insides`, `assembly_animation`, `anim_factor` |
| `voxify_list_objects` | List all Voxify objects in scene | None |
| `voxify_get_settings` | Get full modifier socket inputs | `voxify_object_name` |
| `voxify_set_settings` | Dynamically update parameters | `voxify_object_name`, `voxel_size`, `viewport_as`, `render_as`, `generation_mode`, `keep_insides`, `prune_overlaps`, `custom_voxel`, `custom_voxel_object`, `assembly_animation`, `anim_factor` |
| `voxify_bake_to_mesh` | Convert voxel instances to real mesh | `voxify_object_name` |
| `voxify_toggle_source` | Toggle source mesh visibility | `voxify_object_name` |
| `voxify_add_demo` | Spawn demo voxelized Suzanne | `location` ([x, y, z]) |

---

## Core Workflows

### 1. Voxelizing an Object

When voxelizing a mesh:
1. Ensure the source object has its scale applied (`Ctrl + A > Scale`).
2. Call `voxify_mesh` with the target object name and desired voxel size:
   ```json
   {
     "object_name": "CharacterMesh",
     "voxel_size": 0.04,
     "viewport_as": "Voxels",
     "generation_mode": "Fast",
     "hide_source": true
   }
   ```
3. A container object named `Voxify.CharacterMesh` is generated, linking the source mesh in non-destructive evaluation mode.

### 2. Tuning Quality and Insides
- **Hollow shell vs Solid interior**:
  - `keep_insides: false` generates only the outer surface shell of voxels (lightest performance).
  - `keep_insides: true` fills the internal volume completely with solid voxels.
- **Fast vs Exact generation**:
  - `Fast`: OpenVDB density grid; recommended for standard manifold 3D models.
  - `Exact`: Raycast grid test; recommended for thin geometry, flat planes, or non-manifold meshes.

### 3. Custom Voxels (e.g. Lego Bricks)
To replace standard cubic voxels with Lego-style blocks:
```json
{
  "voxify_object_name": "Voxify.CharacterMesh",
  "custom_voxel": true,
  "custom_voxel_object": "LegoBrick"
}
```

### 4. Assembly / Build Animation
To animate voxels assembling over time:
1. Set `assembly_animation: true`.
2. Keyframe or interpolate `anim_factor` from `0.0` (fully disassembled / scattered) to `1.0` (fully built).

### 5. Baking to Real Polygon Mesh
Procedural voxels in Geometry Nodes are rendered as instances. To export to FBX, glTF, OBJ, or send to a game engine:
```json
{
  "voxify_object_name": "Voxify.CharacterMesh"
}
```
`voxify_bake_to_mesh` realizes all instances into real geometry, applies materials, and yields standard vertices and faces.

---

## Native Blender UI Access

When working directly in the Blender interface:
- **3D Viewport Sidebar**: Press `N` > **Voxify** tab.
- **Quick Effects**: `Object > Quick Effects > Quick Voxify`.
- **Asset Browser**: Switch library to **`Voxify`** to drag and drop assets.
