"""Capture a saved Blender scene without saving changes to its source file.

Run with Blender --background file.blend --python-exit-code 1 --python this.py -- ...
SPDX-License-Identifier: Apache-2.0
"""

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def collect_geometry(collection):
    members = {obj.as_pointer() for obj in collection.all_objects}
    graph = bpy.context.evaluated_depsgraph_get()
    records = []
    lower = [math.inf] * 3
    upper = [-math.inf] * 3
    for instance in graph.object_instances:
        obj = instance.object
        parent = instance.parent
        if instance.is_instance:
            in_model = parent is not None and parent.original.as_pointer() in members
        else:
            in_model = obj.original.as_pointer() in members
        if not in_model or obj.hide_render or (parent and parent.hide_render):
            continue
        if obj.type not in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:
            continue
        mesh = obj.to_mesh()
        try:
            if not mesh or not mesh.vertices:
                continue
            mesh.calc_loop_triangles()
            for vertex in mesh.vertices:
                point = instance.matrix_world @ vertex.co
                if not all(math.isfinite(value) for value in point):
                    raise ValueError(f'Non-finite geometry: {obj.name}')
                for axis in range(3):
                    lower[axis] = min(lower[axis], point[axis])
                    upper[axis] = max(upper[axis], point[axis])
            records.append({
                'name': obj.original.name,
                'instance': bool(instance.is_instance),
                'parent': parent.original.name if parent else None,
                'vertices': len(mesh.vertices),
                'triangles': len(mesh.loop_triangles),
                'negative_transform': instance.matrix_world.determinant() < 0,
                'materials': [slot.material.name if slot.material else None for slot in obj.material_slots],
            })
        finally:
            obj.to_mesh_clear()
    if not records:
        raise ValueError(f'No evaluated mesh geometry in collection {collection.name!r}')
    center = (Vector(lower) + Vector(upper)) / 2
    radius = (Vector(upper) - Vector(lower)).length / 2
    if radius <= 0:
        raise ValueError('Model has zero-size bounds')
    return records, lower, upper, center, radius


def dependency_warnings():
    warnings = []
    for image in bpy.data.images:
        if image.source == 'FILE' and not image.packed_file:
            path = bpy.path.abspath(image.filepath, library=image.library)
            if not path or not Path(path).is_file():
                warnings.append(f'Missing image: {image.name}: {path}')
        elif image.source in {'TILED', 'SEQUENCE', 'MOVIE'}:
            warnings.append(f'Manual dependency check needed for {image.source}: {image.name}')
    for library in bpy.data.libraries:
        path = bpy.path.abspath(library.filepath)
        if not Path(path).is_file():
            warnings.append(f'Missing linked library: {path}')
    return warnings


def capture(scene, out, name):
    path = out / (name + '.png')
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    if not path.is_file() or path.stat().st_size < 32:
        raise RuntimeError(f'Render did not produce a PNG: {path}')
    camera = scene.camera
    return {
        'path': path.name,
        'sha256': sha256(path),
        'camera': camera.name,
        'matrix_world': [list(row) for row in camera.matrix_world],
        'projection': camera.data.type,
        'lens_mm': camera.data.lens,
        'ortho_scale': camera.data.ortho_scale,
        'sensor_mm': [camera.data.sensor_width, camera.data.sensor_height],
        'sensor_fit': camera.data.sensor_fit,
        'shift': [camera.data.shift_x, camera.data.shift_y],
        'clip': [camera.data.clip_start, camera.data.clip_end],
        'resolution': [scene.render.resolution_x, scene.render.resolution_y],
        'pixel_aspect': [scene.render.pixel_aspect_x, scene.render.pixel_aspect_y],
    }


def project_landmarks(scene, collection, path):
    data = json.loads(path.read_text(encoding='utf-8'))
    size = data['reference_size']
    if len(size) != 2 or any(type(v) is not int or v <= 0 for v in size):
        raise ValueError('reference_size must contain two positive integer dimensions')
    width, height = size
    ratio = scene.render.resolution_x / scene.render.resolution_y
    if not math.isclose(width / height, ratio, rel_tol=0.002):
        raise ValueError('Landmark reference aspect differs from the saved camera frame')
    if scene.camera is None:
        raise ValueError('Landmarks require an active reference camera')
    rows, seen = [], set()
    for entry in data['points']:
        name = entry['id']
        if not isinstance(name, str) or not name or name in seen:
            raise ValueError('Landmark IDs must be nonempty and unique')
        seen.add(name)
        obj = collection.all_objects.get(entry['object'])
        if obj is None:
            raise ValueError('Landmark object not in model collection: ' + entry['object'])
        local, reference = entry['local'], entry['reference_px']
        if len(local) != 3 or len(reference) != 2 or not all(type(v) in (int, float) and math.isfinite(v) for v in local + reference):
            raise ValueError('Landmark coordinates must be finite 3D/2D numbers')
        if not (0 <= reference[0] <= width and 0 <= reference[1] <= height):
            raise ValueError('Reference landmark is outside the image')
        point = world_to_camera_view(scene, scene.camera, obj.matrix_world @ Vector(local))
        projected = [point.x * width, (1 - point.y) * height]
        residual = [projected[i] - reference[i] for i in (0, 1)]
        tolerance = entry.get('tolerance_px')
        if tolerance is not None and (type(tolerance) not in (int, float) or not math.isfinite(tolerance) or tolerance < 0):
            raise ValueError('Landmark tolerance must be a finite nonnegative pixel value')
        error = math.hypot(*residual)
        rows.append({'id': name, 'reference_px': reference, 'projected_px': projected,
                     'residual_px': residual, 'error_px': error, 'behind_camera': point.z <= 0,
                     'tolerance_px': tolerance,
                     'within_tolerance': None if tolerance is None else point.z > 0 and error <= tolerance})
    if not rows:
        raise ValueError('Landmark points must not be empty')
    return {'source': str(path.resolve()), 'sha256': sha256(path), 'reference_size': size, 'points': rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--collection', default='Model')
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--size', type=int, default=512)
    parser.add_argument('--mode', choices=['beauty', 'clay', 'both'], default='both')
    parser.add_argument('--landmarks', type=Path)
    args = parser.parse_args(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else [])
    if not 64 <= args.size <= 2048:
        parser.error('--size must be between 64 and 2048')
    source = Path(bpy.data.filepath)
    if not bpy.data.filepath or not source.is_file():
        parser.error('Load a saved .blend file before this script')
    out = args.out.expanduser().resolve()
    if out.exists():
        parser.error('Output directory already exists; use a new versioned directory')
    collection = bpy.data.collections.get(args.collection)
    if collection is None or collection not in tuple(bpy.context.scene.collection.children_recursive):
        parser.error('Collection is missing from the active scene: ' + args.collection)
    before = sha256(source)
    records, lower, upper, center, radius = collect_geometry(collection)
    scene = bpy.context.scene
    warnings = dependency_warnings()
    landmarks = project_landmarks(scene, collection, args.landmarks) if args.landmarks else None
    report = {
        'schema': 'img2blender-review-v2',
        'source': str(source),
        'source_sha256': before,
        'blender_version': bpy.app.version_string,
        'frame': scene.frame_current,
        'engine': scene.render.engine,
        'view_transform': scene.view_settings.view_transform,
        'exposure': scene.view_settings.exposure,
        'gamma': scene.view_settings.gamma,
        'requested_mode': args.mode,
        'landmarks': landmarks,
        'collection': collection.name,
        'bounds': {'min': lower, 'max': upper},
        'evaluated_viewport_triangles': sum(row['triangles'] for row in records),
        'geometry': records,
        'warnings': warnings,
        'limits': [
            'Descriptive viewport dependency-graph geometry; final-render/export topology may differ.',
            'Geometry visibility may differ from render-layer exclusions; inspect the captures.',
            'No automatic likeness, topology, intersection, rigging, or export verdict.',
            'Compositor and sequencer bypassed; the rest of the scene remains renderable.',
            'Clay overrides remove material transparency and shader displacement; review those forms separately.',
        ],
        'renders': [],
    }
    out.mkdir(parents=True, exist_ok=False)
    scene.render.use_compositing = False
    scene.render.use_sequencer = False
    scene.render.use_border = False
    scene.render.use_crop_to_border = False
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    longest = max(scene.render.resolution_x, scene.render.resolution_y)
    scene.render.resolution_x = max(1, round(scene.render.resolution_x * args.size / longest))
    scene.render.resolution_y = max(1, round(scene.render.resolution_y * args.size / longest))
    reference_camera = scene.camera
    reference_resolution = (scene.render.resolution_x, scene.render.resolution_y)
    reference_aspect = (scene.render.pixel_aspect_x, scene.render.pixel_aspect_y)
    if reference_camera is None:
        warnings.append('No active reference camera; only automatic orbit views were captured.')
    data = bpy.data.cameras.new('img2blender-review')
    camera = bpy.data.objects.new('img2blender-review', data)
    scene.collection.objects.link(camera)
    data.type = 'PERSP'
    data.lens = 50
    distance = radius / math.sin(data.angle / 2) * 1.25
    data.clip_start = max(radius * 0.001, 0.000001)
    data.clip_end = max(distance * 4, data.clip_start * 100)
    modes = ['beauty', 'clay'] if args.mode == 'both' else [args.mode]
    for mode in modes:
        prefix = ''
        if mode == 'clay':
            prefix = 'clay-'
            material = bpy.data.materials.new('img2blender-neutral-clay')
            if bpy.app.version < (5, 0, 0):
                material.use_nodes = True
            shader = next(node for node in material.node_tree.nodes if node.type == 'BSDF_PRINCIPLED')
            shader.inputs['Base Color'].default_value = (0.4, 0.4, 0.4, 1)
            shader.inputs['Roughness'].default_value = 0.8
            for layer in scene.view_layers:
                layer.material_override = material
        if reference_camera:
            scene.camera = reference_camera
            scene.render.resolution_x, scene.render.resolution_y = reference_resolution
            scene.render.pixel_aspect_x, scene.render.pixel_aspect_y = reference_aspect
            bpy.context.view_layer.update()
            record = capture(scene, out, prefix + 'reference')
            record['mode'] = mode
            report['renders'].append(record)
        scene.camera = camera
        scene.render.resolution_x = scene.render.resolution_y = args.size
        scene.render.pixel_aspect_x = scene.render.pixel_aspect_y = 1
        for angle in (0, 90, 180, 270):
            radians = math.radians(angle)
            direction = Vector((math.sin(radians), -math.cos(radians), 0.35)).normalized()
            camera.location = center + direction * distance
            camera.rotation_euler = (center - camera.location).to_track_quat('-Z', 'Y').to_euler()
            bpy.context.view_layer.update()
            record = capture(scene, out, prefix + f'orbit-{angle:03d}')
            record['mode'] = mode
            report['renders'].append(record)
    if sha256(source) != before:
        raise RuntimeError('Source .blend changed during capture')
    (out / 'report.json').write_text(json.dumps(report, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    print('IMG2BLENDER_REVIEW', out / 'report.json')


if __name__ == '__main__':
    main()
