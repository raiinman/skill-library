"""Real Blender export/reimport, isolation and finite LOD smoke test. Artifacts remain in --out."""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--blender', required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    root = args.out.resolve()
    root.mkdir(parents=True, exist_ok=False)
    fixture = root/'fixture.blend'
    builder = root/'fixture.py'
    builder.write_text('''import bpy
from pathlib import Path
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
model=bpy.data.collections.new('Model')
bpy.context.scene.collection.children.link(model)
empty=bpy.data.collections.new('Empty')
bpy.context.scene.collection.children.link(empty)
bpy.ops.mesh.primitive_uv_sphere_add(segments=16,ring_count=8)
obj=bpy.context.object
obj.name='Wheel Rim.001'
for c in tuple(obj.users_collection): c.objects.unlink(obj)
model.objects.link(obj)
obj['pipeline_id']='sphere'
mod=obj.modifiers.new('Repeated part','ARRAY')
mod.count=2
mod.relative_offset_displace=(2.5,0,0)
mat=bpy.data.materials.new('Packed painted material')
image=bpy.data.images.new('Test non-square paint',width=8,height=4)
image.generated_color=(.8,.2,.1,1)
image.pack()
node=mat.node_tree.nodes.new('ShaderNodeTexImage')
node.image=image
shader=next(n for n in mat.node_tree.nodes if n.type=='BSDF_PRINCIPLED')
mat.node_tree.links.new(node.outputs['Color'],shader.inputs['Base Color'])
obj.data.materials.append(mat)
bpy.ops.mesh.primitive_cube_add(location=(20,0,0))
bpy.context.object.name='Unrelated'
bpy.ops.wm.save_as_mainfile(filepath=str(Path(__file__).with_name('fixture.blend')))
''',encoding='utf-8')
    def run(script, blend=None, tail=(), succeeds=True):
        cmd=[args.blender,'--background','--factory-startup','--disable-autoexec']
        if blend:cmd.append(str(blend))
        cmd += ['--python-exit-code','1','--python',str(script)]
        if tail:cmd += ['--',*map(str,tail)]
        result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=120)
        with (root/'test.log').open('a',encoding='utf-8') as stream:stream.write(result.stdout+result.stderr)
        assert (result.returncode==0)==succeeds, result.stdout+result.stderr
    run(builder)
    before=hashlib.sha256(fixture.read_bytes()).hexdigest()
    pipeline=Path(__file__).with_name('web_pipeline.py')
    def operation(name,filename,*extra,succeeds=True,collection='Model'):
        run(pipeline,fixture,[name,'--collection',collection,'--out',root/filename,*extra],succeeds)
        assert hashlib.sha256(fixture.read_bytes()).hexdigest()==before
    operation('export','raw.glb')
    operation('export','evaluated.glb','--apply-modifiers')
    def document(path):
        data=path.read_bytes()
        magic,version,size=struct.unpack_from('<4sII',data)
        assert magic==b'glTF' and version==2 and size==len(data)
        chunk_size,chunk_type=struct.unpack_from('<I4s',data,12)
        assert chunk_type==b'JSON'
        return json.loads(data[20:20+chunk_size])
    raw=document(root/'raw.glb'); evaluated=document(root/'evaluated.glb')
    for doc in (raw,evaluated):
        assert any(node.get('extras',{}).get('pipeline_id')=='sphere' for node in doc['nodes'])
        assert all(node.get('name')!='Unrelated' for node in doc['nodes'])
        assert doc.get('materials') and doc.get('images')
        assert all('bufferView' in image for image in doc['images'])
    def vertex_count(doc):
        return sum(doc['accessors'][prim['attributes']['POSITION']]['count'] for mesh in doc['meshes'] for prim in mesh['primitives'])
    assert vertex_count(evaluated)>vertex_count(raw)
    operation('export','raw.glb',succeeds=False)
    operation('export','empty.glb',succeeds=False,collection='Empty')
    assert not (root/'empty.glb').exists()
    operation('optimize','optimized.blend','--ratio','.4')
    operation('lods','lods.blend','--levels','.5','.25')
    operation('lods','invalid.blend','--levels','nan',succeeds=False)
    operation('batch','batch','--input-dir',root)
    assert (root/'batch/fixture.glb').is_file()
    checker=root/'check.py'
    checker.write_text('''import bpy
from pathlib import Path
root=Path(__file__).parent
bpy.ops.wm.open_mainfile(filepath=str(root/'lods.blend'),use_scripts=False)
assert len(bpy.data.collections['Model_LODs'].objects)==2
assert len(bpy.data.collections['Model'].all_objects)==1
assert tuple(bpy.data.objects['Unrelated'].location)==(20,0,0)
bpy.ops.wm.open_mainfile(filepath=str(root/'optimized.blend'),use_scripts=False)
assert bpy.data.objects['Wheel Rim.001'].modifiers[-1].type=='DECIMATE'
assert not bpy.data.objects['Unrelated'].modifiers
bpy.ops.wm.read_factory_settings(use_empty=True)
assert bpy.ops.import_scene.gltf(filepath=str(root/'evaluated.glb'))=={'FINISHED'}
assert any(obj.type=='MESH' for obj in bpy.context.scene.objects)
assert any(obj.get('pipeline_id')=='sphere' for obj in bpy.context.scene.objects)
''',encoding='utf-8')
    run(checker)
    assert hashlib.sha256(fixture.read_bytes()).hexdigest()==before
    (root/'result.json').write_text(json.dumps(dict(status='passed',source_sha256=before,
        raw_vertices=vertex_count(raw),evaluated_vertices=vertex_count(evaluated),
        checks=['GLB export/reimport','packed non-square image','modifier policy','collection isolation','source preservation','finite LOD generation','optimization copy','batch conversion','overwrite/empty/NaN rejection']),indent=2)+'\n')
    print('WEB_PIPELINE_TEST_PASSED',root/'result.json')


if __name__=='__main__':
    main()
