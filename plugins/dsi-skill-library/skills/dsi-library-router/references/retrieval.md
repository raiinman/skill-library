# Retrieval adapters

## Maintained corrections

Read `resources/maintenance-overlay/manifest.json` relative to the verified router.
Its entries include primary instructions, provenance and shared references. Each
online replacement requires a receipt for the actual complete source bytes at the
retained pin before dependent work. A local replacement hash alone is incomplete.

On a Node host, request the pinned `fetch_file` body with `encoding: base64` and use:

```text
node <router>/scripts/source.mjs verify-source --repository raiinman/skill-library --revision <full-live-SHA> --path <canonical-path> --source-base64 <actual-returned-base64>
```

For long inputs, `--source-base64 -` reads the base64 from stdin. Pass the actual
connector payload, not the tool's JSON wrapper, a quoted excerpt or invented bytes.
This operation has no network call, branch resolution, lock or file write. It uses
the same maintenance gate as ordinary helper reads: original bytes matching the
declared base yield the verified replacement; already-effective bytes are retained;
conflicting bytes fail with no effective body. The receipt reports the actual
`source_sha256`, `match`, `maintenance_overlay`, `effective_sha256`, `bytes`, and
`content_base64`; valid UTF-8 also has `content`. For a listed path, verify the
successful match and use that returned effective content.

Repository/revision/path record the caller's witnessed connector read; arguments do
not independently prove a remote download. Retain the actual pinned read with its
receipt. Other hosts may supply equivalent byte-preserving source/effective hash
evidence. A Git blob SHA or copied manifest digest is not that source calculation.
If unavailable, report the verification blocker instead of substituting silently.

Offline mode verifies the permitted manifest-mapped effective bundle and overlay;
it does not fetch a live original. Ordinary host resource reads do not require Node.
Keep source revision, overlay identity and effective hash separate. Unlisted paths
retain their selected source and pin. The helper does not authorize installs,
instruction execution, network access or writes.

Before automatic selection, apply this gate to any relevant listed candidate's pinned
entrypoint and compare its effective native YAML name/description. Connector discovery
must do this too; an older catalog/index description is only a shortlist hint for that
candidate. Do not read all replacement bodies just to choose a workflow.

## Online adapters

The connected GitHub adapter is the preferred cloud route. Resolve the branch with
`fetch_commit`, retain `commit.sha`, and call `fetch_file` with that exact `ref` for
every resource. Check returned errors and truncation; use ranges or binary/base64
retrieval when necessary. Never confuse a file's blob SHA with the repository commit.
If these capabilities are missing, report the connection requirement rather than
inventing tools or an app ID. This plugin does not declare an unverified app dependency.

Shell networking and connected tools are separate capabilities. A working Node runtime
does not prove shell HTTPS works. If a helper reports `fetch failed`, DNS, TLS or proxy
failure, discover available GitHub connector tools and continue retrieval through them.
Prefer the connector immediately when shell egress is known unavailable. A local transport
failure alone is not evidence that the library is inaccessible through the connector.

Preserve the task's full SHA when changing adapters, including a SHA resolved before a
later helper failure. Use the connector's exact `ref` on every read. If the failed helper
never returned or recorded a SHA, resolve the intended branch once through `fetch_commit`.
After branch resolution, failed helper discovery emits a `dsi-source-error` JSON record
on stderr containing `source.repository`, `source.branch`, `source.revision` and
`source.adapter`. Retain that exact revision for connector recovery. This error record
is not a valid discovery lock and does not mean the index or any skill was loaded.
Then read the pinned index; a genuinely absent index permits the pinned `CATALOG.md`
compatibility route and candidate entrypoint native YAML described below. Authentication
or transport failure does not establish index absence. The Node helper cannot call host
connector tools itself: this failover is the agent's responsibility. Record the adapter
change and continue with actual returned source contents, never the bundled snapshot.

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
If and only if the pinned `skill-index.json` is absent, `begin` reads `CATALOG.md` and
all its canonical entrypoints at that same commit. The bundled YAML 2.9.1 parser preserves
native names, descriptions (including folded/quoted YAML) and DSI metadata. The result
is labeled `derived-from-pinned-catalog`, with a revision, a hash of the resulting index,
and hashes of every source read. This is live discovery, never the bundled discovery snapshot.
The task lock retains that derived index, so reading `skill-index.json` through this helper
returns the same hash-checked task discovery data without fetching every entrypoint again.
That read is explicitly marked `virtual: true`; no generated file is claimed to exist
upstream. The command returns the full index once, outside its source summary, while
the on-disk task lock retains the derived discovery data for subsequent reads.
Invalid frontmatter, duplicate names, malformed published indexes and transport failures
fail before writing the lock. The parser's ISC license is bundled in `scripts/vendor/yaml/LICENSE`.
Resource paths must stay in the repository. Normal relative parent references may resolve
elsewhere inside the repository; do not execute arbitrary downloaded scripts without inspection.

For scripts importing adjacent files, materialize all required resources with their
original paths under one task directory. `--out` writes bytes unchanged. Verify hashes
against the index when hashes are available. Keep external provider and engine checks
separate from successful retrieval. The bundled offline library is a separately
selected immutable source; never silently use it to replace an online task's pin.

## Bundled resources for explicit offline or bundle mode

Use the actual host skill/resource reader to open `resources/offline-library/`
relative to the router. Read `snapshot-manifest.json` and `skill-index.json`; select
the primary and its provenance at the manifest's immutable revision. Every canonical
source path maps through `manifest.files[path].stored_path`. In particular, canonical
`SKILL.md` files are stored as `SKILL.md.txt`. Unpatched bytes are unchanged; listed
maintenance corrections use separately verified effective bytes and provenance. Resolve relative
and sibling references against canonical paths before applying that mapping. These
are supporting resources, not additional native skills.

Do not require Node, Git, a shell or a connector for host-provided resource reads. If
resource access is unavailable, report that blocker honestly. The bundle is not a
live branch refresh; external tools and provider setup remain separate requirements.

An optional Node host can verify and read the bundle without network access or writes:

`scripts/source.mjs` is the single adapter helper, resolved from the router directory
you actually opened. `verify`, `begin` and `read` are its subcommands, not filenames.

```text
node <router>/scripts/source.mjs verify --snapshot <router>/resources/offline-library
node <router>/scripts/source.mjs read --snapshot <router>/resources/offline-library --path skills/<category>/<skill>/SKILL.md
node <router>/scripts/source.mjs read --snapshot <router>/resources/offline-library --path skills/<category>/<skill>/SOURCE.md
```

`verify` checks the complete base and maintenance inventory and hashes. Direct `read --snapshot`
also verifies the complete bundle first, returns effective bytes as text or writes
binary bytes only with an explicitly chosen `--out`, and creates no lock. For an
editable task, `begin --snapshot <bundle> --lock <task>/dsi-source.json` records the
same verified identity; subsequent normal `read --lock` calls recheck that manifest
identity and the requested file hash. It never fetches or invokes Git. A changed
manifest, locked revision, unsafe path, symlink or file hash fails rather than mixing
sources. Do not create a lock when the task forbids writes.

Keep original returned file text when literal excerpts are requested. A helper's JSON
wrapper and a reserialized parsed document are not the quoted source. Select excerpts
from the original text and retain a separate excerpt for each requested file.

