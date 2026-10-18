# Using the upstream ECS examples

The [preserved worked examples](upstream-details.md) cover eight patterns. They are illustrative fragments, not a complete project or a verified package-version baseline. Read only the pattern relevant to the task, then check it against the installed packages and compile it in the project.

| Pattern | Before reusing it |
| --- | --- |
| 1. Components | Choose component layout from actual access and grouping requirements. Shared components affect chunk grouping; their use needs a concrete reason. |
| 2. Systems | The comment saying query `foreach` auto-generates a job is incorrect. `SystemAPI.Query` iterates on the main thread. Explicitly schedule an appropriate job when useful; choose between `ISystem` and `SystemBase` from version support and managed requirements. |
| 3. Queries | Supply missing component definitions such as `Dead`, establish required singleton availability, and dispose owned temporary arrays. Avoid creating an ECB for every matched entity when one per update suffices. |
| 4. Command buffers | Supply a consistent `Spawner` definition. Choose playback timing deliberately: a buffer queued to a group that has already updated waits until its next playback. Ensure the prefab has components used with `SetComponent`, and handle existing components appropriately when using add operations. Track producer dependencies. |
| 5. Aspects | Confirm aspect support in the installed Entities version. `TakeDamage` reads shield capacity but never consumes it; define and test the intended shield behavior before reuse. Optional component references require presence checks. |
| 6. Singletons | Ensure required singletons exist before their first read, with `RequireForUpdate` or an appropriate explicit check. A check after an unconditional read does not protect it. |
| 7. Baking | Several referenced types are omitted. The two spawner examples assume different fields. Validate prefab inputs and use the installed Baker dependency API for each referenced object, rather than assuming the shown array call is valid. |
| 8. Native collections | The persistent hash map is cleared and resized without explicitly completing its previous writer. Establish ownership and synchronize before main-thread reuse and teardown. Retain deferred disposal handles where needed. Validate positive cell size, handle hash collisions, and check capacity. |

The later `IJobChunk` performance fragment accepts an enabled mask but ignores it. Honor the mask, for example with the installed version's enabled-entity enumerator, or explicitly establish why enabled filtering cannot apply to that query. A plain loop over every entity can process entities excluded by enabled state.

Use Burst for supported unmanaged code. Managed components and main-thread UnityEngine operations can be valid parts of a hybrid design. Measure scheduling, synchronization, memory use, and representative entity counts before asserting an improvement.

## Documentation used for the adaptation

Checked 2026-10-17 against official Entities 1.4 documentation through Context7. These links establish the example caveats, not a requirement to use Entities 1.4 in every project. Resolve the target project's own package version before implementation.

- [SystemAPI.Query main-thread iteration](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/systems-systemapi-query.html)
- [Synchronization points](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/performance-sync-points.html)
- [Job overhead and main-thread tradeoffs](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/job-overhead.html)
- [Migration examples for query iteration and IJobEntity](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/upgrade-guide.html)
