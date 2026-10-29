---
name: unity-developer
description: Build, debug, and optimize Unity gameplay, rendering, assets, UI, and platform builds. Use for Unity C# development and Unity-specific performance or deployment work.
license: MIT
---

# Unity Developer

Work in the project's existing Unity version and conventions. Complete the requested behavior with the smallest change that fits the game.

## Establish the project

Read `ProjectSettings/ProjectVersion.txt`, `Packages/manifest.json`, and the relevant entries in `Packages/packages-lock.json`. Inspect the affected scripts, assembly definitions, scenes or prefabs, and callers. Identify the target platform, render pipeline, input system, and UI stack from the project before choosing APIs.

Use current official documentation for that editor and package version, through Context7 when available. Resolve uncertainty from the files and tools first; ask only when a missing decision blocks the requested result. A skill install does not authorize a Unity upgrade, render-pipeline migration, or new service subscription.

## Implement the requested change

- Follow existing MonoBehaviour, ScriptableObject, ECS, networking, and asset-loading patterns. Introduce another architecture or package only when the task needs it. Jobs, pooling, Addressables, and async code solve specific problems; they are not defaults for every feature.
- Preserve serialized field compatibility, prefab links, `.meta` GUIDs, asset ownership, and existing validation. Include affected callers and assembly references. Use the project's migration convention when a serialized field must change.
- Keep Unity object access on its supported thread. Pair event subscriptions, native allocations, loaded asset handles, and cancellation resources with the appropriate lifetime cleanup.
- For performance work, measure the bottleneck with the project's profiler tools, make a focused change, and compare the same scenario and target. Treat editor measurements as provisional when the issue concerns a device build.
- For UI, retain the current UI stack and support its input, focus, readable scaling, and accessibility requirements. For builds, use the existing target, scripting backend, and build configuration.

## Editor tools and verification

When a compatible Unity editor connection is available, use its discovered commands for scenes, prefabs, imports, and live checks. Confirm the intended project before editor mutations. The separately installed `unity-cli` skill covers that tool; load it only when using the CLI. These development instructions also work without that optional connection.

Run the relevant editor compilation, existing EditMode or PlayMode tests, and a targeted gameplay or build check when the environment supports them. Add a focused regression test for changed non-trivial behavior using the project's test setup. Report which checks actually ran and any missing editor, license, module, device, or project dependency. Do not equate a text review with a successful Unity compile or player build.

## Further reference

For the upstream capability coverage, consult [the preserved original](references/upstream-skill.md). It is broad background, including version-specific and legacy product names; the actual project and current official documentation determine which guidance applies.
