#!/usr/bin/env python3
"""
Voxify MCP Server
Model Context Protocol server for Blender procedural voxelization and mesh modifier workflows.
Zero-dependency JSON-RPC 2.0 stdio implementation compatible with Antigravity and Codex.
"""

from __future__ import annotations

import io
import json
import os
import socket
import subprocess
import sys
import traceback
from typing import Any, Dict, List, Optional

# Force UTF-8 stdio streams on Windows
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8", newline="\n")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n", write_through=True)

BLENDER_HOST = os.environ.get("BLENDER_HOST", "127.0.0.1")
BLENDER_PORT = int(os.environ.get("BLENDER_PORT", "9876"))
BLENDER_PATH = os.environ.get(
    "BLENDER_PATH", r"C:\Program Files\Blender Foundation\Blender 5.2\blender.exe"
)
VOXIFY_BLEND_PATH = os.environ.get(
    "VOXIFY_BLEND_PATH",
    os.path.expandvars(
        r"%APPDATA%\Blender Foundation\Blender\5.2\scripts\addons\voxify\assets\Voxify_V1.2.blend"
    ),
)


def run_in_live_blender(code: str, timeout: float = 15.0) -> Dict[str, Any]:
    """Execute Python code in the live Blender instance via the Blender MCP socket."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((BLENDER_HOST, BLENDER_PORT))
        req = {"type": "execute_code", "params": {"code": code}}
        s.sendall(json.dumps(req).encode("utf-8"))

        raw_data = b""
        while True:
            chunk = s.recv(8192)
            if not chunk:
                break
            raw_data += chunk
            try:
                decoded = raw_data.decode("utf-8")
                resp = json.loads(decoded)
                return resp
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
        raise RuntimeError("Incomplete response from Blender socket")
    except ConnectionRefusedError:
        raise RuntimeError(
            f"Could not connect to Blender at {BLENDER_HOST}:{BLENDER_PORT}. "
            "Please make sure Blender is open with the 'Interface: Blender MCP' add-on server started."
        )
    finally:
        s.close()


def run_headless_blender(blend_path: str, code: str, timeout: float = 45.0) -> str:
    """Execute Python code in a headless Blender CLI process."""
    if not os.path.exists(BLENDER_PATH):
        raise FileNotFoundError(f"Blender executable not found at: {BLENDER_PATH}")

    args = [BLENDER_PATH, "-b"]
    if blend_path and os.path.exists(blend_path):
        args.append(blend_path)
    args.extend(["--python-expr", code])

    proc = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    if proc.returncode != 0:
        raise RuntimeError(f"Headless Blender exited with code {proc.returncode}:\n{proc.stderr}")
    return proc.stdout


# ─── Tool Implementations ───────────────────────────────────────────────────────

def tool_voxify_mesh(args: Dict[str, Any]) -> str:
    target_obj = args.get("object_name")
    voxel_size = args.get("voxel_size")
    viewport_as = args.get("viewport_as", "Voxels")
    render_as = args.get("render_as", "Voxels")
    generation_mode = args.get("generation_mode", "Fast")
    custom_voxel = args.get("custom_voxel", False)
    custom_voxel_object = args.get("custom_voxel_object")
    keep_insides = args.get("keep_insides", False)
    prune_overlaps = args.get("prune_overlaps", False)
    assembly_anim = args.get("assembly_animation", False)
    anim_factor = args.get("anim_factor", 0.5)
    hide_source = args.get("hide_source", True)

    escaped_target = json.dumps(target_obj)
    escaped_vsize = json.dumps(voxel_size)
    escaped_vpas = json.dumps(viewport_as)
    escaped_rendas = json.dumps(render_as)
    escaped_gen = json.dumps(generation_mode)
    escaped_cvox = json.dumps(custom_voxel)
    escaped_cvox_obj = json.dumps(custom_voxel_object)
    escaped_insides = json.dumps(keep_insides)
    escaped_prune = json.dumps(prune_overlaps)
    escaped_anim = json.dumps(assembly_anim)
    escaped_factor = json.dumps(anim_factor)
    escaped_hide = json.dumps(hide_source)
    escaped_blend_path = json.dumps(VOXIFY_BLEND_PATH)

    code = f"""
import bpy, os, json

target_name = {escaped_target}
v_size = {escaped_vsize}
vp_as = {escaped_vpas}
rd_as = {escaped_rendas}
gen_mode = {escaped_gen}
custom_vox = {escaped_cvox}
custom_obj_name = {escaped_cvox_obj}
keep_in = {escaped_insides}
prune_ov = {escaped_prune}
anim_on = {escaped_anim}
anim_fac = {escaped_factor}
hide_src = {escaped_hide}
blend_path = {escaped_blend_path}

# Resolve source object
source_obj = None
if target_name:
    source_obj = bpy.data.objects.get(target_name)
    if not source_obj:
        print(json.dumps({{"error": f"Object '{{target_name}}' not found in Blender scene."}}))
        exit()
else:
    source_obj = bpy.context.active_object

if not source_obj or source_obj.type != 'MESH':
    print(json.dumps({{"error": "Target object must be a valid Mesh object."}}))
    exit()

# Load Voxify container
with bpy.data.libraries.load(blend_path, link=False) as (df, dt):
    if 'Voxify' in df.objects:
        dt.objects = ['Voxify']

vox_obj = bpy.data.objects.get('Voxify')
if not vox_obj:
    print(json.dumps({{"error": "Failed to load Voxify container object from library."}}))
    exit()

col = bpy.context.collection or bpy.context.scene.collection
col.objects.link(vox_obj)

vox_obj.name = f"Voxify.{{source_obj.name}}"
vox_obj.matrix_world = source_obj.matrix_world.copy()

mod = vox_obj.modifiers.get('GeometryNodes')
if mod and hasattr(mod, 'properties') and hasattr(mod.properties, 'inputs'):
    inputs = mod.properties.inputs
    if hasattr(inputs, 'Socket_3'):
        inputs.Socket_3.value = source_obj

    if source_obj.data.uv_layers and source_obj.data.uv_layers.active:
        if hasattr(inputs, 'Socket_6'):
            inputs.Socket_6.value = source_obj.data.uv_layers.active.name

    # Adaptive voxel size
    max_dim = max(source_obj.dimensions) if any(source_obj.dimensions) else 2.0
    actual_size = v_size if v_size is not None else max(0.01, min(0.5, max_dim / 35.0))

    if hasattr(inputs, 'Socket_12'):
        inputs.Socket_12.value = float(actual_size)
    if hasattr(inputs, 'Socket_31'):
        inputs.Socket_31.value = float(actual_size)
    if hasattr(inputs, 'Socket_41'):
        inputs.Socket_41.value = float(actual_size)
    if hasattr(inputs, 'Socket_5'):
        inputs.Socket_5.value = float(actual_size)

    if hasattr(inputs, 'Socket_46'):
        inputs.Socket_46.value = vp_as
    if hasattr(inputs, 'Socket_28'):
        inputs.Socket_28.value = rd_as
    if hasattr(inputs, 'Socket_35'):
        inputs.Socket_35.value = gen_mode
    if hasattr(inputs, 'Socket_37'):
        inputs.Socket_37.value = bool(keep_in)
    if hasattr(inputs, 'Socket_40'):
        inputs.Socket_40.value = bool(prune_ov)

    if hasattr(inputs, 'Socket_51'):
        inputs.Socket_51.value = bool(custom_vox)
    if custom_obj_name and hasattr(inputs, 'Socket_52'):
        c_obj = bpy.data.objects.get(custom_obj_name)
        if c_obj:
            inputs.Socket_52.value = c_obj

    if hasattr(inputs, 'Socket_59'):
        inputs.Socket_59.value = bool(anim_on)
    if hasattr(inputs, 'Socket_55'):
        inputs.Socket_55.value = float(anim_fac)

if hide_src:
    source_obj.hide_viewport = True
    source_obj.hide_render = True

bpy.ops.object.select_all(action='DESELECT')
vox_obj.select_set(True)
bpy.context.view_layer.objects.active = vox_obj

result_info = {{
    "status": "success",
    "voxify_object": vox_obj.name,
    "source_object": source_obj.name,
    "voxel_size": actual_size,
    "viewport_display": vp_as,
    "render_display": rd_as,
    "generation_mode": gen_mode,
    "custom_voxel": custom_vox,
    "assembly_animation": anim_on,
    "source_hidden": hide_src
}}
print(json.dumps(result_info))
"""
    res = run_in_live_blender(code)
    return res.get("result", {}).get("result", str(res))


def tool_voxify_list_objects(args: Dict[str, Any]) -> str:
    code = """
import bpy, json

vox_objects = []
for obj in bpy.context.scene.objects:
    for mod in obj.modifiers:
        if mod.type == 'NODES' and mod.node_group and mod.node_group.name.startswith("Voxify"):
            inputs = getattr(getattr(mod, 'properties', None), 'inputs', None)
            src_obj = getattr(getattr(inputs, 'Socket_3', None), 'value', None)
            v_size = getattr(getattr(inputs, 'Socket_12', None), 'value', None)
            vp_as = getattr(getattr(inputs, 'Socket_46', None), 'value', None)
            gen_mode = getattr(getattr(inputs, 'Socket_35', None), 'value', None)
            vox_objects.append({
                "name": obj.name,
                "source_object": src_obj.name if src_obj else None,
                "voxel_size": v_size,
                "viewport_display": vp_as,
                "generation_mode": gen_mode,
                "hidden_viewport": obj.hide_viewport
            })

print(json.dumps({"count": len(vox_objects), "objects": vox_objects}))
"""
    res = run_in_live_blender(code)
    return res.get("result", {}).get("result", str(res))


def tool_voxify_get_settings(args: Dict[str, Any]) -> str:
    obj_name = args.get("voxify_object_name")
    escaped_name = json.dumps(obj_name)
    code = f"""
import bpy, json

name = {escaped_name}
obj = bpy.data.objects.get(name) if name else bpy.context.active_object
if not obj:
    print(json.dumps({{"error": f"Object '{{name}}' not found."}}))
    exit()

mod = None
for m in obj.modifiers:
    if m.type == 'NODES' and m.node_group and m.node_group.name.startswith("Voxify"):
        mod = m
        break

if not mod:
    print(json.dumps({{"error": f"No Voxify modifier found on object '{{obj.name}}'."}}))
    exit()

inputs = mod.properties.inputs
settings = {{"object_name": obj.name}}
for item in mod.node_group.interface.items_tree:
    if item.item_type == 'SOCKET' and item.in_out == 'INPUT':
        sock = getattr(inputs, item.identifier, None)
        if sock and hasattr(sock, 'value'):
            val = sock.value
            val_out = val.name if hasattr(val, 'name') else str(val) if isinstance(val, (int, float, bool, str)) else repr(val)
            settings[item.name] = val_out

print(json.dumps(settings, indent=2))
"""
    res = run_in_live_blender(code)
    return res.get("result", {}).get("result", str(res))


def tool_voxify_set_settings(args: Dict[str, Any]) -> str:
    obj_name = args.get("voxify_object_name")
    escaped_args = json.dumps(args)
    code = f"""
import bpy, json

params = {escaped_args}
name = params.get("voxify_object_name")
obj = bpy.data.objects.get(name) if name else bpy.context.active_object
if not obj:
    print(json.dumps({{"error": f"Object '{{name}}' not found."}}))
    exit()

mod = None
for m in obj.modifiers:
    if m.type == 'NODES' and m.node_group and m.node_group.name.startswith("Voxify"):
        mod = m
        break

if not mod:
    print(json.dumps({{"error": f"No Voxify modifier found on object '{{obj.name}}'."}}))
    exit()

inputs = mod.properties.inputs
updated = {{}}

if "voxel_size" in params and hasattr(inputs, 'Socket_12'):
    inputs.Socket_12.value = float(params["voxel_size"])
    inputs.Socket_31.value = float(params["voxel_size"])
    inputs.Socket_41.value = float(params["voxel_size"])
    inputs.Socket_5.value = float(params["voxel_size"])
    updated["voxel_size"] = params["voxel_size"]

if "viewport_as" in params and hasattr(inputs, 'Socket_46'):
    inputs.Socket_46.value = str(params["viewport_as"])
    updated["viewport_as"] = params["viewport_as"]

if "render_as" in params and hasattr(inputs, 'Socket_28'):
    inputs.Socket_28.value = str(params["render_as"])
    updated["render_as"] = params["render_as"]

if "generation_mode" in params and hasattr(inputs, 'Socket_35'):
    inputs.Socket_35.value = str(params["generation_mode"])
    updated["generation_mode"] = params["generation_mode"]

if "keep_insides" in params and hasattr(inputs, 'Socket_37'):
    inputs.Socket_37.value = bool(params["keep_insides"])
    updated["keep_insides"] = params["keep_insides"]

if "prune_overlaps" in params and hasattr(inputs, 'Socket_40'):
    inputs.Socket_40.value = bool(params["prune_overlaps"])
    updated["prune_overlaps"] = params["prune_overlaps"]

if "custom_voxel" in params and hasattr(inputs, 'Socket_51'):
    inputs.Socket_51.value = bool(params["custom_voxel"])
    updated["custom_voxel"] = params["custom_voxel"]

if "custom_voxel_object" in params and hasattr(inputs, 'Socket_52'):
    c_obj = bpy.data.objects.get(params["custom_voxel_object"])
    if c_obj:
        inputs.Socket_52.value = c_obj
        updated["custom_voxel_object"] = params["custom_voxel_object"]

if "assembly_animation" in params and hasattr(inputs, 'Socket_59'):
    inputs.Socket_59.value = bool(params["assembly_animation"])
    updated["assembly_animation"] = params["assembly_animation"]

if "anim_factor" in params and hasattr(inputs, 'Socket_55'):
    inputs.Socket_55.value = float(params["anim_factor"])
    updated["anim_factor"] = params["anim_factor"]

print(json.dumps({{"status": "success", "object": obj.name, "updated": updated}}))
"""
    res = run_in_live_blender(code)
    return res.get("result", {}).get("result", str(res))


def tool_voxify_bake_to_mesh(args: Dict[str, Any]) -> str:
    obj_name = args.get("voxify_object_name")
    escaped_name = json.dumps(obj_name)
    code = f"""
import bpy, json

name = {escaped_name}
obj = bpy.data.objects.get(name) if name else bpy.context.active_object
if not obj:
    print(json.dumps({{"error": f"Object '{{name}}' not found."}}))
    exit()

mod = None
for m in obj.modifiers:
    if m.type == 'NODES' and m.node_group and m.node_group.name.startswith("Voxify"):
        mod = m
        break

if not mod:
    print(json.dumps({{"error": f"No Voxify modifier found on object '{{obj.name}}'."}}))
    exit()

# Add Realize Instances node tree
realize_tree = bpy.data.node_groups.new("RealizeTemp", 'GeometryNodeTree')
in_node = realize_tree.nodes.new('NodeGroupInput')
out_node = realize_tree.nodes.new('NodeGroupOutput')
realize_node = realize_tree.nodes.new('GeometryNodeRealizeInstances')
realize_tree.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
realize_tree.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
realize_tree.links.new(in_node.outputs['Geometry'], realize_node.inputs['Geometry'])
realize_tree.links.new(realize_node.outputs['Geometry'], out_node.inputs['Geometry'])

mod_realize = obj.modifiers.new(name="RealizeVoxels", type='NODES')
mod_realize.node_group = realize_tree

bpy.context.view_layer.objects.active = obj
obj.select_set(True)
bpy.ops.object.convert(target='MESH')
bpy.data.node_groups.remove(realize_tree, do_unlink=True)

print(json.dumps({{
    "status": "success",
    "object": obj.name,
    "vertices_count": len(obj.data.vertices),
    "polygons_count": len(obj.data.polygons),
    "message": f"Successfully baked voxels on '{{obj.name}}' into real polygon mesh."
}}))
"""
    res = run_in_live_blender(code)
    return res.get("result", {}).get("result", str(res))


def tool_voxify_toggle_source(args: Dict[str, Any]) -> str:
    obj_name = args.get("voxify_object_name")
    escaped_name = json.dumps(obj_name)
    code = f"""
import bpy, json

name = {escaped_name}
obj = bpy.data.objects.get(name) if name else bpy.context.active_object
if not obj:
    print(json.dumps({{"error": f"Object '{{name}}' not found."}}))
    exit()

mod = None
for m in obj.modifiers:
    if m.type == 'NODES' and m.node_group and m.node_group.name.startswith("Voxify"):
        mod = m
        break

if not mod:
    print(json.dumps({{"error": f"No Voxify modifier found on object '{{obj.name}}'."}}))
    exit()

inputs = mod.properties.inputs
src_obj = getattr(getattr(inputs, 'Socket_3', None), 'value', None)
if not src_obj:
    print(json.dumps({{"error": "No source object linked in Voxify modifier."}}))
    exit()

new_state = not src_obj.hide_viewport
src_obj.hide_viewport = new_state
src_obj.hide_render = new_state

print(json.dumps({{
    "status": "success",
    "source_object": src_obj.name,
    "hidden": new_state,
    "visibility": "Hidden" if new_state else "Visible"
}}))
"""
    res = run_in_live_blender(code)
    return res.get("result", {}).get("result", str(res))


def tool_voxify_add_demo(args: Dict[str, Any]) -> str:
    loc = args.get("location", [0.0, 0.0, 0.0])
    escaped_loc = json.dumps(loc)
    escaped_blend_path = json.dumps(VOXIFY_BLEND_PATH)
    code = f"""
import bpy, json

loc = {escaped_loc}
blend_path = {escaped_blend_path}

with bpy.data.libraries.load(blend_path, link=False) as (df, dt):
    dt.objects = [n for n in ['Voxify.Suzanne', 'Suzanne'] if n in df.objects]

col = bpy.context.collection or bpy.context.scene.collection
suz = bpy.data.objects.get('Suzanne')
vox_suz = bpy.data.objects.get('Voxify.Suzanne')

if suz:
    col.objects.link(suz)
    suz.location = (loc[0], loc[1], loc[2])
    suz.hide_viewport = True
    suz.hide_render = True

if vox_suz:
    col.objects.link(vox_suz)
    vox_suz.location = (loc[0], loc[1], loc[2])
    bpy.ops.object.select_all(action='DESELECT')
    vox_suz.select_set(True)
    bpy.context.view_layer.objects.active = vox_suz

print(json.dumps({{
    "status": "success",
    "demo_object": vox_suz.name if vox_suz else None,
    "location": loc
}}))
"""
    res = run_in_live_blender(code)
    return res.get("result", {}).get("result", str(res))


# ─── MCP Definitions ────────────────────────────────────────────────────────────

TOOLS = [
    {
        "name": "voxify_mesh",
        "description": "Voxelize a 3D mesh object in Blender using the Voxify Geometry Nodes modifier.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "object_name": {
                    "type": "string",
                    "description": "Name of the target mesh object in Blender. Defaults to the currently active object if omitted.",
                },
                "voxel_size": {
                    "type": "number",
                    "description": "Voxel grid resolution in meters (e.g. 0.04). If omitted, an adaptive size is automatically calculated from the bounding box.",
                },
                "viewport_as": {
                    "type": "string",
                    "enum": ["Voxels", "PointCloud"],
                    "description": "Viewport display mode: 'Voxels' for full 3D cubic meshes, or 'PointCloud' for fast lightweight points.",
                },
                "render_as": {
                    "type": "string",
                    "enum": ["Voxels", "PointCloud"],
                    "description": "Render display mode.",
                },
                "generation_mode": {
                    "type": "string",
                    "enum": ["Fast", "Exact"],
                    "description": "Voxel generation algorithm: 'Fast' (OpenVDB density grid) or 'Exact' (raycast grid test).",
                },
                "custom_voxel": {
                    "type": "boolean",
                    "description": "Whether to instance custom voxel mesh geometry (e.g. LegoBrick).",
                },
                "custom_voxel_object": {
                    "type": "string",
                    "description": "Name of custom voxel object to instance (defaults to 'LegoBrick' if available).",
                },
                "keep_insides": {
                    "type": "boolean",
                    "description": "Whether to fill the inside volume with solid voxels instead of a hollow surface shell.",
                },
                "prune_overlaps": {
                    "type": "boolean",
                    "description": "Prune overlapping faces or boundary intersections.",
                },
                "assembly_animation": {
                    "type": "boolean",
                    "description": "Enable procedural build-up / assembly animation.",
                },
                "anim_factor": {
                    "type": "number",
                    "description": "Assembly progress factor (0.0 = completely disassembled, 1.0 = fully assembled).",
                },
                "hide_source": {
                    "type": "boolean",
                    "description": "Hide the source mesh in viewport and render after creating voxels (default: true).",
                },
            },
        },
    },
    {
        "name": "voxify_list_objects",
        "description": "List all active Voxify voxelizer objects and their parameters in the current Blender scene.",
        "inputSchema": {
            "type": "object",
            "properties": {},
        },
    },
    {
        "name": "voxify_get_settings",
        "description": "Retrieve full parameters and socket inputs of a specific Voxify voxelizer object.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "voxify_object_name": {
                    "type": "string",
                    "description": "Name of the Voxify object (e.g. 'Voxify.Suzanne'). Defaults to active object.",
                }
            },
        },
    },
    {
        "name": "voxify_set_settings",
        "description": "Dynamically update parameters (voxel size, display mode, generation, assembly animation) on a Voxify object.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "voxify_object_name": {
                    "type": "string",
                    "description": "Name of the Voxify object to adjust. Defaults to active object.",
                },
                "voxel_size": {"type": "number", "description": "Voxel size in meters."},
                "viewport_as": {"type": "string", "enum": ["Voxels", "PointCloud"]},
                "render_as": {"type": "string", "enum": ["Voxels", "PointCloud"]},
                "generation_mode": {"type": "string", "enum": ["Fast", "Exact"]},
                "keep_insides": {"type": "boolean"},
                "prune_overlaps": {"type": "boolean"},
                "custom_voxel": {"type": "boolean"},
                "custom_voxel_object": {"type": "string"},
                "assembly_animation": {"type": "boolean"},
                "anim_factor": {"type": "number"},
            },
        },
    },
    {
        "name": "voxify_bake_to_mesh",
        "description": "Realize and bake voxel instances on a Voxify object into a permanent, editable polygon mesh (for exporting to glTF/FBX/OBJ or 3D printing).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "voxify_object_name": {
                    "type": "string",
                    "description": "Name of the Voxify object to bake. Defaults to active object.",
                }
            },
        },
    },
    {
        "name": "voxify_toggle_source",
        "description": "Toggle viewport and render visibility of the source mesh linked to a Voxify object.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "voxify_object_name": {
                    "type": "string",
                    "description": "Name of the Voxify object.",
                }
            },
        },
    },
    {
        "name": "voxify_add_demo",
        "description": "Spawn the pre-configured Voxify Suzanne monkey demo object into the Blender scene.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "array",
                    "items": {"type": "number"},
                    "description": "[x, y, z] coordinates to place the demo object.",
                }
            },
        },
    },
]

TOOL_HANDLERS = {
    "voxify_mesh": tool_voxify_mesh,
    "voxify_list_objects": tool_voxify_list_objects,
    "voxify_get_settings": tool_voxify_get_settings,
    "voxify_set_settings": tool_voxify_set_settings,
    "voxify_bake_to_mesh": tool_voxify_bake_to_mesh,
    "voxify_toggle_source": tool_voxify_toggle_source,
    "voxify_add_demo": tool_voxify_add_demo,
}


def send_json(data: Dict[str, Any]) -> None:
    line = json.dumps(data) + "\n"
    sys.stdout.write(line)
    sys.stdout.flush()


def handle_request(msg: Dict[str, Any]) -> None:
    msg_id = msg.get("id")
    method = msg.get("method")
    params = msg.get("params", {})

    if method == "initialize":
        send_json({
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "voxify",
                    "version": "1.2.0"
                }
            }
        })
    elif method == "notifications/initialized":
        pass  # Notification, no response
    elif method == "ping":
        send_json({"jsonrpc": "2.0", "id": msg_id, "result": {}})
    elif method == "tools/list":
        send_json({
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "tools": TOOLS
            }
        })
    elif method == "tools/call":
        tool_name = params.get("name")
        tool_args = params.get("arguments", {})
        handler = TOOL_HANDLERS.get(tool_name)
        if not handler:
            send_json({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {
                    "code": -32601,
                    "message": f"Method or tool '{tool_name}' not found"
                }
            })
            return

        try:
            output = handler(tool_args)
            send_json({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": output
                        }
                    ],
                    "isError": False
                }
            })
        except Exception as e:
            send_json({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": f"Error executing '{tool_name}': {str(e)}\n{traceback.format_exc()}"
                        }
                    ],
                    "isError": True
                }
            })
    else:
        if msg_id is not None:
            send_json({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {
                    "code": -32601,
                    "message": f"Method '{method}' not found"
                }
            })


def main() -> None:
    # Handle stdin buffer with both newline-delimited and Content-Length framing
    while True:
        line = sys.stdin.readline()
        if not line:
            break

        line_str = line.strip()
        if not line_str:
            continue

        # Check for Content-Length framing (LSP style)
        if line_str.lower().startswith("content-length:"):
            try:
                length = int(line_str.split(":", 1)[1].strip())
                # Read empty separator line
                sep = sys.stdin.readline()
                # Read payload of 'length' bytes
                body = sys.stdin.read(length)
                msg = json.loads(body)
                handle_request(msg)
            except Exception as e:
                sys.stderr.write(f"Error parsing framed payload: {e}\n")
            continue

        # Check for standard newline-delimited JSON
        if line_str.startswith("{"):
            try:
                msg = json.loads(line_str)
                handle_request(msg)
            except Exception as e:
                sys.stderr.write(f"Error parsing JSON-RPC line: {e}\n")


if __name__ == "__main__":
    main()
