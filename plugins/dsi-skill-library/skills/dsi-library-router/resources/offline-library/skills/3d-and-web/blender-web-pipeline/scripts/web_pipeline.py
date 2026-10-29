"""Explicit-collection web exports and editable optimization copies, run with Blender's Python."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import bpy


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def collection_objects(name):
    collection = bpy.data.collections.get(name)
    if collection is None or collection not in tuple(bpy.context.scene.collection.children_recursive):
        raise ValueError('Collection is not in the active scene: ' + name)
    objects = tuple(collection.all_objects)
    if not any(obj.type == 'MESH' for obj in objects):
        raise ValueError('Collection contains no mesh objects: ' + name)
    unavailable = [obj.name for obj in objects if obj.name not in bpy.context.view_layer.objects or obj.hide_get() or obj.hide_select]
    if unavailable:
        raise ValueError('Unhide/include objects in the view layer before processing: ' + ', '.join(unavailable))
    return objects


def export_glb(path, objects, apply_modifiers):
    bpy.ops.object.select_all(action='DESELECT')
    for obj in objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = next(obj for obj in objects if obj.type == 'MESH')
    result = bpy.ops.export_scene.gltf(filepath=str(path), export_format='GLB',
        use_selection=True, use_active_scene=True, export_apply=apply_modifiers,
        export_extras=True, export_animations=True, export_cameras=False, export_lights=False,
        export_draco_mesh_compression_enable=False)
    if result != {'FINISHED'} or not path.is_file() or path.stat().st_size < 20:
        raise RuntimeError('GLB export failed: ' + str(path))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['export', 'batch', 'optimize', 'lods'])
    parser.add_argument('--collection', required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--input-dir', type=Path)
    parser.add_argument('--apply-modifiers', action='store_true')
    parser.add_argument('--ratio', type=float, default=.5)
    parser.add_argument('--levels', type=float, nargs='+', default=[.75, .5, .25])
    args = parser.parse_args(sys.argv[sys.argv.index('--')+1:])
    out = args.out.resolve()
    report_path = out.with_name(out.name+'.report.json')
    if out.exists() or report_path.exists():
        raise FileExistsError('Choose a new output path: ' + str(out))
    if args.operation == 'batch':
        if args.input_dir is None or not args.input_dir.is_dir():
            raise ValueError('batch requires --input-dir with saved blend files')
        files = sorted(p for p in args.input_dir.iterdir() if p.suffix.lower() == '.blend')
        if not files:
            raise ValueError('No blend inputs')
    else:
        if not bpy.data.filepath:
            raise ValueError('Load a saved blend file before processing')
        files = [Path(bpy.data.filepath).resolve()]
        expected = '.glb' if args.operation == 'export' else '.blend'
        if out.suffix.lower() != expected:
            raise ValueError('Output must end in ' + expected)
    ratios = args.levels if args.operation == 'lods' else [args.ratio]
    if any(not 0 < ratio < 1 for ratio in ratios):
        raise ValueError('Reduction ratios must be finite, above zero and below one')
    records = []
    if args.operation == 'batch':
        out.mkdir(parents=True, exist_ok=False)
    for source in files:
        before = digest(source)
        if args.operation == 'batch':
            bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
        if bpy.context.mode != 'OBJECT':
            raise ValueError('Save the source in Object Mode before processing')
        objects = collection_objects(args.collection)
        meshes = tuple(obj for obj in objects if obj.type == 'MESH')
        warnings = []
        destination = out/source.with_suffix('.glb').name if args.operation == 'batch' else out
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            raise FileExistsError(destination)
        if args.operation in {'export', 'batch'}:
            if not args.apply_modifiers and any(obj.modifiers for obj in meshes):
                warnings.append('Modifiers were not evaluated; compare required geometry and enable --apply-modifiers when appropriate.')
            export_glb(destination, objects, args.apply_modifiers)
        else:
            if any(obj.data.shape_keys or any(mod.type == 'ARMATURE' for mod in obj.modifiers) for obj in meshes):
                raise ValueError('Rigged/shape-key meshes need a task-specific simplification workflow')
            lod_collection = None
            if args.operation == 'lods':
                lod_collection = bpy.data.collections.new(args.collection+'_LODs')
                bpy.context.scene.collection.children.link(lod_collection)
            for obj in meshes:
                for index, ratio in enumerate(ratios):
                    target = obj
                    if lod_collection:
                        target = obj.copy()
                        target.name = obj.name+f'_LOD{index+1}'
                        lod_collection.objects.link(target)
                    target.data = obj.data.copy()
                    modifier = target.modifiers.new('Web pipeline reduction', 'DECIMATE')
                    modifier.ratio = ratio
                    modifier.use_collapse_triangulate = True
            result = bpy.ops.wm.save_as_mainfile(filepath=str(destination), check_existing=False)
            if result != {'FINISHED'}:
                raise RuntimeError('Could not save output copy')
            warnings.append('Decimate modifiers remain editable; inspect silhouette, materials and evaluated topology before export.')
        if digest(source) != before:
            raise RuntimeError('Source file changed during processing: ' + str(source))
        records.append(dict(source=str(source), source_sha256=before, output=str(destination),
            output_sha256=digest(destination), objects=[obj.name for obj in objects], warnings=warnings))
    report = dict(blender_version=bpy.app.version_string, operation=args.operation,
        collection=args.collection, apply_modifiers=args.apply_modifiers, ratios=ratios, files=records)
    report_path.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('WEB_PIPELINE_REPORT', report_path)


if __name__ == '__main__':
    main()
