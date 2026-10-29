# Compatibility and validation

The bundle contains all 195 original tracked files and 30 specialist skill guides, retaining the actual plugin layout, shared references, helpers, tests and evidence. Nested guides are loaded as reference from the runtime root, rather than copied into 30 competing global skill folders.

## Verified on this machine

- Blender 5.2.1 LTS: 35 deterministic core recipe checks passed, covering modeling/modifiers, material sockets, lighting, cameras, animation, still rendering, GLB/FBX/OBJ exports, a decimation round trip and six small scene fixtures.
- Blender 5.2.1 LTS: all 12 original export/collision/Multires-bake regression checks passed, including validation failures, source/context restoration, scoped FBX, UV coverage and GLB export.
- The image-helper synthetic test passed using the existing isolated Python environment at `C:/Users/mikea/.codex/tools/skill-library-ui-animation/Scripts/python.exe`. NumPy, SciPy, OpenCV and Pillow are available there; Pillow 13.0.0 was added for this bundle. Its name predates this install. This is an environment path, not a portable requirement.
- The standard-library materializer passed exact-byte extraction, overwrite refusal, escaping/absolute/drive/backslash path refusal and corrupt-archive rejection checks. Every original source blob was verified against GitHub's pinned tree before packaging.

These are script/recipe and packaging checks, not proof of natural-language routing, every art direction, GUI screenshots, authenticated MCP connections or actual Unreal imports. Live official/legacy MCP servers and external asset providers remain unconfigured here. The local Blender fallback works.

## Narrow Windows test correction

The unmodified upstream core test inserts `str(Path(...))` into quoted Python snippets. On Windows those backslashes can form escapes such as `\U`, causing SyntaxError before the export recipe runs. `scripts/test_blender_recipes.py` reads the original test and changes only those path substitutions to `as_posix()` in memory. The archive and materialized original remain unchanged. This wrapper passed all 35 checks:

```powershell
& 'C:/Program Files/Blender Foundation/Blender 5.2/blender.exe' --background --factory-startup --disable-autoexec --python-exit-code 1 --python scripts/test_blender_recipes.py -- --source 'C:/Users/mikea/.codex/tools/blender-bundles/cc-blender-toolkit' --out 'C:/temp/new-recipe-test'
```

Run in a fresh process without loading user work: these tests intentionally replace their own fixture scenes. Export regression tests also use fixture scenes and write only their configured test output. Use a new destination.

## Recipe interpretation

World reset is a new-fixture or targeted repair operation, not a prerequisite to every edit of an existing scene. Source GEO/MAT naming, display transforms, metallic/roughness values and numeric quality thresholds are conventions or starting points. Use the actual project's accepted needs. Reference metrics require valid, nonempty inputs, compatible frames and human inspection. A report script exiting zero does not make a failed or vacuous quality result pass. Bounded visible comparison remains required for the requested fidelity.

Read current Blender API documentation before adapting historical or untested examples, especially animation action slots, compositor, EEVEE options and exporter arguments. Check the actual backend's tool schemas; no assumed tool alias or source manifest auto-configures Codex. No self-refinement loop authorizes unrelated skill publishing or unbounded retries.
