---
name: blender-addon-engineer
description: Create and debug Blender Python add-ons, operators, panels, asset validators
  and pipeline exporters. Use when repetitive Blender work needs artist-facing tools
  or reliable batch automation.
license: MIT
---

# Blender Add-on Engineer

Turn a repeated artist task or demonstrated handoff error into the smallest useful Blender tool. Start with the target Blender version, existing add-on layout, actual asset rules and a representative scene. Extend existing conventions; choose a script rather than an add-on when no persistent interface is needed.

## Implementation

- Separate inspection and validation from fixes. Return structured findings with object, rule, severity and actionable details. Rules come from the destination pipeline: a duplicate suffix, space in a name or unapplied transform is not inherently invalid.
- Prefer `bpy.data` and direct property edits. Use operators where necessary with explicit `poll`, mode, selection and context handling. Fail with actionable reports and return `CANCELLED` when required inputs are absent or export validation fails.
- Keep class registration deterministic and unregister in reverse order. Remove owned properties, handlers, timers, menus and keymaps on unregister. Use version-appropriate extension metadata or legacy packaging for the requested Blender versions.
- Persist settings through the smallest suitable property group, scene property or preferences. Place panels where artists perform the task. Add progress and cancellation to long batches when practical.
- Establish explicit collection inclusion and exclusion. Preserve material-slot order and hierarchy where downstream consumers depend on them. Validate location, rotation and scale separately; applying every transform may break rigs or intentional pivots.
- Honor the user's existing authorization for requested fixes. Preview uncertain/destructive changes and preserve recoverable copies; keep exporters from changing the source scene as an incidental cleanup step.

## Verification and delivery

Exercise register, unregister and reload without duplicate handlers or orphaned properties. Test empty selection, wrong object types, dirty scenes, failed validation, write failures and successful authorized fixes. Export tools must enforce their validator in the export path and verify the actual downstream artifact. State which Blender versions and scenarios were tested.

Deliver the installable module/extension or script, minimal usage instructions and test evidence. The [original agent profile](references/upstream-skill.md) includes validator, panel and naming-report examples; these are illustrative fragments, not a complete registered add-on. Adapt them to actual conventions instead of enforcing arbitrary names or invented performance targets. [SOURCE.md](SOURCE.md) preserves attribution.
