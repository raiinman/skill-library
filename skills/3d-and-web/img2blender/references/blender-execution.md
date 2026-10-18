# Blender execution and capture

Use Blender's bundled Python for `bpy`. System Python runs the smoke-test launcher but cannot normally import `bpy`. No pip packages, Three.js runtime, or Blender MCP server are required.

Locate `blender` on PATH or find the installed application. On this installation it is `C:/Program Files/Blender Foundation/Blender 5.2/blender.exe`. Check the actual version; this path is a local example, not a portable dependency.

## Build a native asset

Use an isolated project output folder and a subject-specific Python script. For a new asset, factory startup is appropriate. When extending an existing scene, load its working copy and preserve unrelated objects, collections, and materials. Never clear a user's live scene as a default setup step.

PowerShell example, with project-specific absolute paths:

```powershell
& $blender --background --factory-startup --disable-autoexec --python-exit-code 1 --python 'C:/project/build_scene.py' -- --out 'C:/project/passes/blockout-01.blend'
```

Here `$blender` is the resolved executable path. `build_scene.py` is authored for the subject; it is not a bundled universal generator. Parse its own arguments after `--`, preserve existing files by using versioned outputs, and save explicitly with `bpy.ops.wm.save_as_mainfile`. Blender processes arguments in order. Place `--python-exit-code 1` before `--python` so script failures reach the caller.

Prefer direct data-block and mesh APIs where an operator would depend on selection, mode, or UI context. When an operator is useful, establish its required context. Discover Principled BSDF socket names and render-engine identifiers from the installed version instead of carrying over legacy numeric indices. Preserve linked resources or pack eligible images before delivery. Keep manual/sculpt operations reproducible through saved checkpoints and documented steps when a complete procedural rebuild is impractical.

An optional live Blender tool connection may help with interactive sculpting or scene inspection. Discover its actual tools and confirm the target file first. Persist its edits in the `.blend` and source or documented manual steps. Installing this skill does not configure or require such a connection.

## Review a saved file

```powershell
& $blender --background --disable-autoexec 'C:/project/passes/blockout-01.blend' --python-exit-code 1 --python 'C:/Users/mikea/.codex/skills/img2blender/scripts/review_scene.py' -- --collection Model --out 'C:/project/review-01' --size 512
```

The output directory must not already exist. The script creates:

- `reference.png` if the scene has an active camera, retaining its aspect ratio and camera.
- Four square, elevated orbit renders around the model bounds at `000`, `090`, `180`, and `270` degrees. These are world-axis views, not automatically identified anatomical sides.
- Matching `clay-reference.png` and four `clay-orbit-*.png` views using a neutral material override. The default `--mode both` captures ten images when a reference camera exists. `--mode clay` captures only the geometry diagnostic; `--mode beauty` retains the earlier five-image behavior.
- `report.json` with the source `.blend` hash, Blender version, frame, evaluated geometry bounds and triangle counts, materials, dependency warnings, and each render's camera settings and file hash.

Use `--landmarks C:/project/landmarks.json` for optional projected point errors in the original reference image coordinates. See [camera and landmark data](camera-and-landmarks.md). The report includes sensor dimensions/fit, lens, camera shift/clipping, view transform, exposure and gamma; these settings plus the source `.blend` hash make capture changes traceable. The helper does not automatically fit the camera or accept the model.

Capture uses the scene's renderer, lights, materials, and view transform. It bypasses the compositor and sequencer to avoid their output nodes writing elsewhere; a composited final image needs its own intentional capture. Geometry statistics use the current viewport dependency graph, including evaluated instances, not a final-render topology guarantee. Missing collection geometry is an error. Missing camera or missing dependencies are recorded for the agent to resolve; they are not silently passed.

The helper opens no network connection, does not save the source file, and refuses output reuse. A failed run may leave a partial evidence directory; inspect it and use a new versioned directory. Review all images with vision. It does not prove likeness, nonintersection, manifoldness, correct rigging, or export readiness.

Clay overrides do not preserve material cutouts, transmission, or shader displacement. Hair cards, leaves, glass, and displaced surfaces need their own appropriate check. Scene modifiers still run. Preserve material appearance separately from this neutral geometry diagnostic.

## Freeze the exact checkpoint inputs

From the project directory, run the standard-library helper before editing the next version:

```powershell
python -X utf8 'C:/Users/mikea/.codex/skills/img2blender/scripts/snapshot_checkpoint.py' --project 'C:/project' --blend 'passes/blockout-01.blend' --build 'build_scene.py' --spec '.img2blender/spec.json' --include 'reference.png' --include 'textures/paint.png' --out 'C:/project/checkpoints/blockout-01' --command 'blender --background --python build_scene.py -- --out passes/blockout-01.blend'
```

Only include actual dependencies. Paths are resolved within `--project` and copied under the same relative layout. The destination must be new. `checkpoint.json` is the completion marker and includes file hashes and the recorded command, which is never executed by the snapshot helper. Copy inputs into the project first if they are external. Include imported local modules and prepared textures explicitly, along with a manual-step note if a sculpt cannot be regenerated from the build script. This is explicit file capture, not automatic dependency discovery or an atomic filesystem transaction. Inspect a partial destination after failure and use a new checkpoint name.

## Smoke test

```powershell
python -X utf8 'C:/Users/mikea/.codex/skills/img2blender/scripts/test_review_scene.py' --blender $blender
python -X utf8 'C:/Users/mikea/.codex/skills/img2blender/scripts/test_snapshot_checkpoint.py'
```

The Blender test reopens a small fixture, captures ten beauty/clay PNGs, checks known zero and six-pixel landmark errors, modifier/instance geometry, source preservation, and rejection of invalid collection/landmark data. The checkpoint test verifies restoration bytes after source edits, output refusal, path containment, and rejection of changes during copying. These establish helper behavior, not arbitrary subject reconstruction quality.

Official references checked 2026-10-17 through Context7:

- [Command-line arguments and order](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html)
- [Render operation](https://docs.blender.org/api/current/bpy.ops.render.html)
- [Saving a Blender file](https://docs.blender.org/api/current/bpy.ops.wm.html)
- [Render settings](https://docs.blender.org/api/current/bpy.types.RenderSettings.html)
- [Camera-space point projection](https://docs.blender.org/api/current/bpy_extras.object_utils.html)
- [View-layer material override](https://docs.blender.org/api/current/bpy.types.ViewLayer.html)
