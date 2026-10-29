---
name: unity-ecs-patterns
description: Implement and review Unity ECS/DOTS components, systems, baking, queries, command buffers, Jobs, and Burst. Use for data-oriented Unity code and measured entity-processing bottlenecks.
license: MIT
---

# Unity ECS Patterns

Use ECS for an existing DOTS project or a requested, justified data-oriented system. An entity count alone does not justify migrating a working GameObject design.

## Match the installed stack

Inspect the Unity editor version, package manifest and lockfile, relevant assembly definitions, and nearby systems. Identify the installed Entities, Collections, Burst, Mathematics, Physics, and Graphics packages that this change actually touches. Use current official documentation for those versions through Context7 when available. Preserve the project's supported APIs and architecture.

## Implement and check the system

1. Define the data and query ownership: component read/write access, optional components, enabled state, world, update group, and ordering. Keep managed and UnityEngine object work in a supported main-thread path; use Burst only for compatible code.
2. Choose plain `SystemAPI.Query` iteration or an explicit job based on dependencies and measured workload. A query `foreach` is main-thread iteration, not an automatically scheduled job. Maintain every producer/consumer dependency, including dependencies on native containers that ECS cannot infer.
3. For structural changes in jobs, use an appropriate entity command buffer and playback point. Check prefab component presence before choosing add versus set, validate entity references, and account for deferred playback timing. Direct EntityManager changes on the main thread can be appropriate when their synchronization cost is acceptable.
4. Give each native allocation an owner and bounded lifetime. Complete or chain outstanding jobs before main-thread reuse, resize, clear, or disposal. Retain disposal handles where later work or system teardown must wait for them. Honor enabled masks when writing custom chunk iteration.
5. Validate baking inputs and dependencies with the installed Baker API. Preserve authoring data and scene/prefab references. Require singleton prerequisites before use and handle absent optional data deliberately.
6. Compile in the actual project and run a small relevant test: empty and representative queries, changed enabled state, structural playback, or lifetime teardown as the change requires. Keep safety checks on during development. Compare profiling results before claiming a speedup.

Report the implemented behavior, checks run, and any unverified package or runtime assumptions. If no Unity project/editor is available, state that compilation and runtime behavior remain untested.

## Worked examples

When a concrete pattern is needed, read [the example guide and caveats](references/details.md) first. It routes to preserved upstream examples for components, systems, queries, ECBs, aspects, singletons, baking, and native jobs. Adapt examples to the installed API and verify them before reuse.
