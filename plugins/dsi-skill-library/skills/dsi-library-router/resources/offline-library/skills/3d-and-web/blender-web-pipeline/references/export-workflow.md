# Saved-file export workflow

Use the installed Blender executable and version-matched Python API. The local installation is `C:/Program Files/Blender Foundation/Blender 5.2/blender.exe`; this is an environment example, not a portable requirement. API checked through Context7 against [the current export operator](https://docs.blender.org/api/current/bpy.ops.export_scene.html) on 2026-10-18.

PowerShell example, replacing paths and collection with the actual inputs:

```powershell
& 'C:/Program Files/Blender Foundation/Blender 5.2/blender.exe' --background --factory-startup --disable-autoexec 'C:/project/source.blend' --python-exit-code 1 --python 'C:/Users/mikea/.codex/skills/blender-web-pipeline/scripts/web_pipeline.py' -- export --collection Model --out 'C:/project/output-new.glb' --apply-modifiers
```

Choose `--apply-modifiers` only when evaluated modifier geometry is wanted. Without it, some scene features may be omitted; it does not automatically turn arrays into portable instancing. Inspect the artifact. Rigged assets and shape keys need their own verification, and the exporter may handle them differently from static modifiers.

Other operations use the same Blender invocation with these arguments after `--`:

```text
optimize --collection Model --ratio 0.5 --out C:/project/reduced-copy.blend
lods --collection Model --levels 0.75 0.5 0.25 --out C:/project/lod-copy.blend
batch --collection Model --input-dir C:/project/sources --out C:/project/new-exports
```

Quote paths containing spaces in the actual shell. Batch opens each top-level `.blend` with embedded scripts disabled and stops on a failure. Its output folder must be new. Optimize and LOD output paths must be new blend files. Their Decimate modifiers remain editable. Rigged/shape-key meshes are rejected for these generic reduction operations. Originals and meshes outside the requested collection remain unchanged; LODs are placed in a separate collection. Missing, empty, hidden or excluded target collections/objects require attention before processing.

Each operation writes `<output>.report.json` with source/output hashes, processed objects, settings and warnings. A failed batch can leave partial exports; inspect them and choose a new output folder after fixing the cause. This is explicit output refusal, not an atomic transaction or a generic asset validator. Packed/external images, rigs and procedural shader losses still need task-specific inspection. LOD selection distances and browser loader integration are the consuming project's responsibility.

## Validation and optional compression

Reimport GLB in an empty scene. Compare evaluated bounds and intentional modifier effects, units/orientation, UVs, images, transparency, normals, material slots, instances, skinning and required animation clips. Then load it in the intended web viewer, checking console/network errors and appearance. A local script test does not prove a particular project's exported asset looks correct.

Use the project's existing compression tools when needed. Query their current documentation before selecting CLI options. Keep raw GLB and each intermediate; simplify or reduce texture size only against an accepted visual/performance budget. PNG, WebP and KTX2 have different runtime/extension requirements. Configure the loader's decoder/transcoder for whichever compression is actually present. File size is not GPU memory usage.

## Helper smoke test

From ordinary Python:

```powershell
python -B scripts/test_web_pipeline.py --blender 'C:/Program Files/Blender Foundation/Blender 5.2/blender.exe' --out 'C:/temp/new-web-pipeline-test'
```

This creates an isolated fixture with a packed non-square texture, an array modifier and unrelated geometry. It checks native export/reimport, collection isolation, modifier policy, finite LOD generation, optimization copies, batch conversion, source hashes and overwrite/empty/invalid-ratio rejection. It does not test browser playback or arbitrary rigs.
