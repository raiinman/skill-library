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
- `report.json` with the source `.blend` hash, Blender version, frame, evaluated geometry bounds and triangle counts, materials, dependency warnings, and each render's camera settings and file hash.

Capture uses the scene's renderer, lights, materials, and view transform. It bypasses the compositor and sequencer to avoid their output nodes writing elsewhere; a composited final image needs its own intentional capture. Geometry statistics use the current viewport dependency graph, including evaluated instances, not a final-render topology guarantee. Missing collection geometry is an error. Missing camera or missing dependencies are recorded for the agent to resolve; they are not silently passed.

The helper opens no network connection, does not save the source file, and refuses output reuse. A failed run may leave a partial evidence directory; inspect it and use a new versioned directory. Review all images with vision. It does not prove likeness, nonintersection, manifoldness, correct rigging, or export readiness.

## Smoke test

```powershell
python -X utf8 'C:/Users/mikea/.codex/skills/img2blender/scripts/test_review_scene.py' --blender $blender
```

This builds a small temporary fixture, reopens it in Blender, tests modifier/instance geometry capture and renders, verifies source preservation and output refusal, and checks an invalid collection failure. It establishes helper behavior, not arbitrary subject reconstruction quality.

Official references checked 2026-10-17 through Context7:

- [Command-line arguments and order](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html)
- [Render operation](https://docs.blender.org/api/current/bpy.ops.render.html)
- [Saving a Blender file](https://docs.blender.org/api/current/bpy.ops.wm.html)
- [Render settings](https://docs.blender.org/api/current/bpy.types.RenderSettings.html)
