# Retrieval adapters

The connected GitHub adapter is the preferred cloud route. Resolve the branch with
`fetch_commit`, retain `commit.sha`, and call `fetch_file` with that exact `ref` for
every resource. Check returned errors and truncation; use ranges or binary/base64
retrieval when necessary. Never confuse a file's blob SHA with the repository commit.
If these capabilities are missing, report the connection requirement rather than
inventing tools or an app ID. This plugin does not declare an unverified app dependency.

On a local host, the bundled Node 22+ helper uses Git or public GitHub HTTPS:

```text
node <router>/scripts/source.mjs begin --repo <checkout> --branch main --lock <task>/dsi-source.json
node <router>/scripts/source.mjs read --lock <task>/dsi-source.json --path skills/<category>/<skill>/SKILL.md
node <router>/scripts/source.mjs read --lock <task>/dsi-source.json --path skills/<category>/<skill>/references/example.md --out <task>/resources/example.md
node <router>/scripts/source.mjs begin --github raiinman/skill-library --branch main --lock <task>/dsi-source.json
```

`begin` resolves the branch and reads the index before writing the lock. It refuses
to replace a lock; use `--refresh` only for a new substantive task or explicit refresh.
Git mode fetches only the chosen branch into an isolated temporary ref without changing
the worktree, FETCH_HEAD, or local branch. It records the origin URL; verify that URL
identifies `raiinman/skill-library` before using the checkout as the DSI authority.
Public HTTPS mode needs no token and fails honestly for inaccessible
content. The lock is the revision authority; subsequent `read` calls never resolve a branch.
Resource paths must stay in the repository. Normal relative parent references may resolve
elsewhere inside the repository; do not execute arbitrary downloaded scripts without inspection.

For scripts importing adjacent files, materialize all required resources with their
original paths under one task directory. `--out` writes bytes unchanged. Verify hashes
against the index when hashes are available. Keep external provider and engine checks
separate from successful retrieval. No fallback executable snapshot is bundled.
