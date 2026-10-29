"""Exercise real Blender build, reopen, render, instance, and preservation behavior.

Artifacts stay in the printed temporary directory (or a new --out directory).
SPDX-License-Identifier: Apache-2.0
"""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import struct
import subprocess
import tempfile


FIXTURE = '''
import sys
import bpy
from mathutils import Vector

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
scene = bpy.context.scene
model = bpy.data.collections.new('Model')
scene.collection.children.link(model)

def move_to_model(obj):
    for collection in list(obj.users_collection):
        collection.objects.unlink(obj)
    model.objects.link(obj)

def material(name, color):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    shader = mat.node_tree.nodes.get('Principled BSDF')
    shader.inputs['Base Color'].default_value = (*color, 1)
    shader.inputs['Roughness'].default_value = 0.3
    return mat

blue = material('Blue ceramic', (0.025, 0.2, 0.6))
gold = material('Orange detail', (0.9, 0.22, 0.02))
bpy.ops.mesh.primitive_cube_add(size=2)
body = bpy.context.object
body.name = 'Body'
body.scale = (1, 0.6, 0.8)
body.data.materials.append(blue)
modifier = body.modifiers.new('Editable bevel', 'BEVEL')
modifier.width = 0.12
modifier.segments = 3
move_to_model(body)
bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0.6, -0.8, 0.5))
detail = bpy.context.object
detail.name = 'Detail'
detail.scale.x = -1
detail.data.materials.append(gold)
move_to_model(detail)

prototype = bpy.data.collections.new('Prototype')
mesh = detail.data.copy()
part = bpy.data.objects.new('InstancedPart', mesh)
part.data.materials.clear()
part.data.materials.append(gold)
prototype.objects.link(part)
instance = bpy.data.objects.new('Instance', None)
instance.instance_type = 'COLLECTION'
instance.instance_collection = prototype
instance.location = (-0.6, 0.2, 1.1)
model.objects.link(instance)
anchor = bpy.data.objects.new('CalibrationAnchor', None)
anchor.location = (0, 0, 0.2)
model.objects.link(anchor)

# The same mesh object instanced outside Model must not inflate its bounds/counts.
outside_prototype = bpy.data.collections.new('OutsidePrototype')
outside_prototype.objects.link(body)
outside = bpy.data.objects.new('OutsideInstance', None)
outside.instance_type = 'COLLECTION'
outside.instance_collection = outside_prototype
outside.location = (50, 0, 0)
scene.collection.objects.link(outside)

camera_data = bpy.data.cameras.new('ReferenceCamera')
camera = bpy.data.objects.new('ReferenceCamera', camera_data)
scene.collection.objects.link(camera)
camera.location = (3.5, -5, 3)
camera.rotation_euler = (Vector((0, 0, 0.2)) - camera.location).to_track_quat('-Z', 'Y').to_euler()
scene.camera = camera
for location, energy in [((3, -4, 5), 500), ((-4, 0, 3), 350)]:
    data = bpy.data.lights.new('Area', 'AREA')
    data.energy = energy
    data.shape = 'DISK'
    data.size = 4
    light = bpy.data.objects.new('Area', data)
    scene.collection.objects.link(light)
    light.location = location
    light.rotation_euler = (-light.location).to_track_quat('-Z', 'Y').to_euler()
scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = 8
scene.render.resolution_x = 240
scene.render.resolution_y = 160
scene.render.resolution_percentage = 100
scene.render.image_settings.color_depth = '8'
bpy.ops.wm.save_as_mainfile(filepath=sys.argv[-1])
'''


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--blender', default=shutil.which('blender'))
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    if not args.blender or not Path(args.blender).is_file():
        parser.error('Provide --blender with the installed executable path')
    if args.out:
        out = args.out.resolve()
        out.mkdir(parents=True, exist_ok=False)
    else:
        out = Path(tempfile.mkdtemp(prefix='img2blender-smoke-'))
    fixture = out / 'fixture.py'
    fixture.write_text(FIXTURE, encoding='utf-8')
    blend = out / 'fixture.blend'
    base = [args.blender, '--background', '--factory-startup', '--disable-autoexec']

    def run(arguments, expected_success=True, message=None):
        result = subprocess.run(base + arguments, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=180)
        (out / ('last-success.log' if expected_success else 'last-rejection.log')).write_text(result.stdout + result.stderr, encoding='utf-8')
        assert (result.returncode == 0) == expected_success, (result.returncode, result.stdout[-3000:], result.stderr[-3000:])
        if message:
            assert message in result.stdout + result.stderr
        return result

    run(['--python-exit-code', '1', '--python', str(fixture), '--', str(blend)])
    before = digest(blend)
    helper = Path(__file__).with_name('review_scene.py').resolve()
    review = out / 'review'
    landmarks = out / 'landmarks.json'
    landmarks.write_text(json.dumps({'reference_size': [240, 160], 'points': [
        {'id': 'target', 'object': 'CalibrationAnchor', 'local': [0, 0, 0], 'reference_px': [120, 80], 'tolerance_px': 0.1},
        {'id': 'offset', 'object': 'CalibrationAnchor', 'local': [0, 0, 0], 'reference_px': [126, 80], 'tolerance_px': 1},
    ]}), encoding='utf-8')
    command = [str(blend), '--python-exit-code', '1', '--python', str(helper), '--', '--out', str(review), '--size', '96', '--landmarks', str(landmarks)]
    run(command)
    report = json.loads((review / 'report.json').read_text(encoding='utf-8'))
    assert report['source_sha256'] == before == digest(blend)
    assert len(report['geometry']) == 3, report['geometry']
    assert any(row['instance'] and row['name'] == 'InstancedPart' for row in report['geometry'])
    assert next(row for row in report['geometry'] if row['name'] == 'Body')['triangles'] > 12
    assert next(row for row in report['geometry'] if row['name'] == 'Detail')['negative_transform']
    assert report['bounds']['min'][1] < -1
    assert report['bounds']['max'][2] > 1.3
    assert report['bounds']['max'][0] < 2
    assert len(report['renders']) == 10
    points = report['landmarks']['points']
    assert points[0]['error_px'] < 0.1 and points[0]['within_tolerance']
    assert abs(points[1]['error_px'] - 6) < 0.1 and not points[1]['within_tolerance']
    for render in report['renders']:
        path = review / render['path']
        data = path.read_bytes()
        assert data[:8] == b'\x89PNG\r\n\x1a\n'
        assert list(struct.unpack('>II', data[16:24])) == render['resolution']
        assert digest(path) == render['sha256']
    assert report['renders'][0]['resolution'] == [96, 64]
    assert all(row['resolution'] == ([96, 64] if 'reference' in row['path'] else [96, 96]) for row in report['renders'])
    assert len({row['sha256'] for row in report['renders']}) == 10
    assert sum(row['mode'] == 'clay' for row in report['renders']) == 5
    snapshot = {p.name: digest(p) for p in review.iterdir()}
    run(command, False, 'Output directory already exists')
    assert snapshot == {p.name: digest(p) for p in review.iterdir()}
    invalid = out / 'invalid'
    run([str(blend), '--python-exit-code', '1', '--python', str(helper), '--', '--collection', 'Absent', '--out', str(invalid)], False, 'Collection is missing')
    assert not invalid.exists()
    bad_landmarks = out / 'bad-landmarks.json'
    bad = json.loads(landmarks.read_text(encoding='utf-8'))
    bad['points'][0]['local'][0] = float('nan')
    bad_landmarks.write_text(json.dumps(bad), encoding='utf-8')
    bad_output = out / 'bad-landmarks-output'
    run([str(blend), '--python-exit-code', '1', '--python', str(helper), '--', '--out', str(bad_output), '--landmarks', str(bad_landmarks)], False, 'finite 3D/2D numbers')
    assert not bad_output.exists()
    assert digest(blend) == before
    print('PASS: Blender build/reopen, modifier and instance geometry, 10 beauty/clay PNGs, calibrated landmark residuals, aspect, hashes, source preservation, overwrite and invalid-collection refusal')
    print('Artifacts:', out)


if __name__ == '__main__':
    main()
