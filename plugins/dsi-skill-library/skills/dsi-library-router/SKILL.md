---
name: dsi-library-router
description: >-
  Select DSI workflows for coding/debugging, UI/design, Blender/3D, Unreal/UEFN, AWS, media, marketing, planning and reverse engineering. Route named activation such as "activate ponytail" or "use a named skill" without a $ marker; retain requested session modes until stopped. "Locally enabled" selects DSI with live GitHub by default. Bundle requires explicit bundle/offline/local-files-only restrictions; shell limits do not ban permitted connectors. Check named absence live. Preserve skills/providers. Read the primary before fresh failing-test code changes. Skip ordinary chat, simple facts and covered minor follow-ups. Open the exact SKILL.md path supplied by the host skill list, preserving every segment, including repeated directory names; do not reconstruct it from a project note or plugin cache layout. Verify the supplied entrypoint exists before opening; if missing, discover it by filename rather than trying a reconstructed path.
---

# DSI Skill Library

Before retrieving a workflow, retain a source decision for the active task:
`source_mode: live` by default, or `source_mode: bundle` with the explicit source
constraint that selects it. For a user constraint, retain its exact short wording;
for a higher-priority task-wide restriction, retain its scope without quoting private
instructions. Do not choose bundle without this evidence.

Scope words such as **only** to what the request restricts:

- “Use only the locally enabled workflow package” selects DSI and excludes other
  workflow packages. DSI's configured GitHub retrieval is part of that selected
  package. This wording selects **live**, including when the task's editable files
  must stay inside an isolated folder. Reading permitted remote guidance does not
  modify that folder or install another plugin.
- “Use only local files/sources”, “offline”, “no network”, “no external sources”,
  or an explicit bundle request selects **bundle**. If both package selection and
  a source restriction apply, honor the source restriction.
- A shell or execution-sandbox network limit restricts that transport. It does not
  prohibit a permitted connected GitHub reader. A task-wide remote-source ban
  includes connectors; never use one to evade that ban.

For **live**, the next source operation is to discover the available GitHub adapter
and resolve the selected branch/revision (current `main` by default), then read the
primary and provenance at the returned full SHA. A continuing task reuses its valid
live pin. For **bundle**, follow the explicitly restricted source section below.
If the selected source is inaccessible, report the actual blocker without silently
changing modes. Identify the mode and actual source revision with the primary used.

For an unrestricted task, **do not open `resources/offline-library/` for discovery or
workflow instructions before the live pin/read steps**. Its availability, verified
hashes, matching revision, or convenient local paths do not select bundled mode.
The plugin's router, helper documentation and maintenance overlay are local plugin
resources; reading them does not replace the required live workflow-source reads.
Classify task changes using the turn rules below, so a correction retains a valid
pin and a new unrelated task obtains its own pin.

A requested skill name must be checked against the task's selected source before
declaring it missing. In default-online mode, resolve or retain the live task pin
and check the canonical entrypoint or catalog at that pin. A bundle search is not
evidence of current-source absence, even if its packaged SHA happens to equal main
today. In explicit offline/bundle mode, check only the bundle and scope any absence
claim to that packaged revision. Authentication, transport and resource-reader
failures do not establish absence.

When the user corrects a missing name, reuse only a pin obtained through the valid
source mode for that task. If no valid task pin exists yet, perform the selected
source's pinning step before reading the corrected primary and provenance.

Select one primary workflow and only useful supporting skills from
`https://github.com/raiinman/skill-library`, intended branch `main` unless the user
explicitly selects another source branch or revision for testing or rollback.
Installation makes this router discoverable; it does not force invocation on every response.
Individual library workflows are retrieved instructions, not separately installed native skills.
Resolve bundled relative resources from the parent directory of the entrypoint you
actually opened; do not guess or shorten its installation path.
Retain and reuse the exact successfully verified host entrypoint as the resource
anchor across turns. Once it is valid, do not probe reconstructed cache alternatives.

Reading this router starts discovery; it does not load a DSI workflow. Once you
select or open this router for a substantive task, complete source pinning, primary
selection, and reading the primary entrypoint and its provenance before implementing
the task. Do not silently stop after reading the router. If the task is excluded or
retrieval is blocked, state that exclusion or blocker explicitly and distinguish any
useful independent work from a DSI workflow run. Ordinary conversation, simple factual
answers, and minor follow-ups covered by a loaded workflow still skip discovery.

## Pin the source once per substantive task

For default online mode, use either adapter below. Explicit bundled tasks instead
follow the bundle section at the end; they do not resolve branches. Shared retention
and turn rules apply to both modes.

1. Discover available GitHub tools and their actual schemas. With the connected GitHub
   capability, resolve the intended branch using **fetch_commit** (`repo_full_name: raiinman/skill-library`,
   `commit_sha: main` by default). Retain its returned full commit SHA. A branch-list result containing
   only a branch name is insufficient. Then use **fetch_file** with
   `repository_full_name: raiinman/skill-library`, `ref: <SHA>`, `path: skill-index.json`.
   Tool prefixes vary by host; these are capability names, not guaranteed registrations.
   If that exact pinned file is absent, the live repository may predate generated indexes:
   retrieve `CATALOG.md` at the same SHA and use its canonical `skills/<category>/<name>/SKILL.md`
   links as discovery paths. Retrieve each candidate's native YAML `name` and `description`
   at that SHA before selecting it. Label this **derived from the pinned live catalog**;
   do not treat a missing generated file as an unavailable library. Authentication errors,
   malformed indexes and network failures do not permit this compatibility path.
2. A local host can instead run the bundled [source reader](scripts/source.mjs):
   `node <router>/scripts/source.mjs begin --repo <checkout> --branch main --lock <task>/dsi-source.json`.
   It fetches the branch, locks the resolved SHA, and reads its index. The tool also supports
   public GitHub HTTPS reads with `--github raiinman/skill-library`. No credentials are bundled.
   This helper automatically derives a complete live discovery index when `skill-index.json`
   is absent, using the pinned catalog and native YAML. Node availability alone does not
   establish shell network access. Prefer the connected GitHub adapter when shell egress
   is unavailable or an attempted helper read fails with `fetch failed`, DNS, TLS or proxy errors.
   Follow [retrieval details](references/retrieval.md) for commands and resource handling.
3. Retain each task's objective/artifact, explicit skill/provider choices,
   `{source_mode, source_constraint, repository, branch, revision, primary, loaded paths, lock path when used}` in conversation context. Use that
   SHA for the index, selected `SKILL.md`, and all repository-local references, scripts,
   assets, `SOURCE.md`, and setup guidance. Never mix default-branch reads into a pinned task.
4. Refresh on a new substantive task or explicit refresh request, following the turn
   rules below. Report the full revision when verifying routing or updates.

## Apply the latest request across turns

Classify the user's change before retrieving instructions or acting. Keep this task
context in the conversation; no separate ledger file or user-facing state format is required.
If both the objective and skill change, the new-task rule takes precedence over a
skill-only correction. Cancellation does not transfer the cancelled task's source choice
or provider constraints to a new, unrelated task.

- A new, unrelated objective or artifact starts a new substantive task: pin its source
  and select/read its matching primary before implementation, even if the same skill
  was used for another task earlier in this chat.
- A correction to the same objective/artifact retains its valid source pin. This
  includes correcting a mistyped or nonexistent skill name, revising the brief, or
  changing output details. Do not resolve `main` again just because another turn arrived.
  Reuse applicable loaded instructions and read only newly needed resources.
- An explicit skill or provider change replaces the earlier choice for that task.
  Follow the latest user choice, select/read any newly needed entrypoint and provenance
  at the retained revision, and verify its capabilities before dependent work. A skill
  change alone does not start a new source pin. Never silently switch providers because
  a tool is unavailable.
- An explicit return to earlier work restores that task's retained source pin, skill,
  provider and applicable constraints, updated by the latest request. Do not carry over
  the intervening task's choices. Reuse valid read evidence rather than restarting
  discovery. A simple factual interlude does not erase this context.
- An explicit refresh or source branch/revision change obtains a new pin for the
  requested task only; reload instructions needed at that revision. If prior pin/read
  evidence is unavailable, retrieve it honestly before claiming to reuse it.

The latest explicit user correction supersedes conflicting earlier constraints.
Continue only the active requested work; remembering an earlier task does not authorize
continuing it while the user has switched tasks or cancelled it.
When using helper locks, keep separate lock paths for independently resumable tasks.
Do not overwrite a suspended task's lock to start another task; refresh only the selected
task's lock when its source must change.

In online mode, if a local helper fails on network transport, discover and try available connected GitHub
tools before declaring the library unavailable. Preserve any already resolved full SHA:
use it as the connector's exact file `ref`, without resolving `main` again. If no SHA was
resolved, pin the intended branch with the connector's `fetch_commit`, then retrieve the
index or, only if absent, the pinned live catalog and candidate native descriptions.
Changing retrieval adapters does not authorize changing repository, branch, skill or provider.
Never replace a transport failure with cached instructions or invent a successful read.

If no available adapter can resolve the branch, say current source access is unavailable. The bundled
[discovery snapshot](references/skill-snapshot.json) can suggest names only. Its content hash
identifies the snapshot; it has no executable skill bodies and is not freshly verified.
Do not present cached instructions as current or silently switch sources.
The executable offline bundle is a separate explicitly selected source, not this
discovery-only snapshot and not a way to claim current-source success.

## Select without routing loops

- Plain-language activation such as “activate ponytail”, “use ponytail”, or “enable
  <workflow> for this conversation” is a named-skill request without a marker. Check
  the selected source catalog before asking what the name means. Read the actual
  primary and provenance before claiming activation. If that primary defines a
  session mode, retain its active level across task changes until the user switches
  or stops it; an unrelated task does not silently deactivate the mode. This does
  not transfer the earlier task's source pin to a new substantive task. Ordinary
  uses of the same word, such as a hairstyle request, are not mode activation.
- A named skill (name, `$name`, or canonical category/name) takes precedence. If it is
  already installed and explicitly selected, follow it immediately. For a named remote
  DSI skill, fetch its canonical entrypoint directly after pinning; no extra router is needed.
  Verify absence against the pinned canonical path or live catalog, not local package
  contents. An authentication or transport error does not establish a nonexistent skill.
- Otherwise compare the task, intended artifact, environment and selected provider with
  the index's native descriptions. For a relevant candidate listed in the maintenance
  overlay, fetch its pinned entrypoint and apply the hash gate below before comparing
  its effective native name and description. Do not select from superseded base metadata
  or load every overlay file merely to route. Read full instructions for the best match.
  Prefer a focused direct match over a broad router. Ask only if a consequential choice
  remains unresolved after inspecting the available descriptions.
- Custom `routing_metadata` belongs to the DSI generator; it is not a native host field.
  The catalog and snapshot are generated discovery aids, not independent trigger lists.
- Preserve specialized routing when it resolves a real workflow choice. Engineering
  phases may use `using-agent-skills`; Arcads routing applies only when Arcads is selected;
  `reverse-skill-router` still needs its separate checkout and scope contract.
- Track visited skill IDs within the current selection chain to prevent routing loops.
  Do not re-enter this router or select a skill twice within that chain. This is not a
  conversation-wide ban: a later task, explicit skill switch, or return to earlier work
  may use that skill again, reusing applicable loaded instructions at its task's pin.
  A sibling reference means read that sibling only when relevant, not restart selection.
- Preserve explicit provider choices and approved project decisions. An absent provider
  tool does not authorize switching to Arcads, REA, or another service.

## Check capabilities and execute

Read the selected entrypoint, its provenance and relevant runtime guidance. Identify
purpose, applicability/exclusions, expected inputs/output, and required capabilities
from those sources. Missing information stays unknown; do not infer installed tools
from historical setup notes, Windows paths, or index inclusion. Verify actual tools,
local files, repositories, accounts and permissions before dependent actions.

For every selected path listed in `resources/maintenance-overlay/manifest.json`,
including `SOURCE.md` and needed references, obtain a successful source-to-effective
verification receipt before using its maintained replacement. Hashing only the local
replacement proves its integrity, not that the downloaded original permits substitution.

For online connector reads on a Node host, fetch the complete pinned file with
`encoding: base64`, then run this existing helper's read-only operation with the
actual returned base64, retained live revision and canonical path:

```text
node <router>/scripts/source.mjs verify-source --repository raiinman/skill-library --revision <full-live-SHA> --path <canonical-path> --source-base64 <actual-connector-base64>
```

Use `--source-base64 -` with base64 on stdin for a long response. The helper performs
both checks and returns `source_sha256`, `match`, overlay identity, `effective_sha256`,
byte count and verified effective content. Use this shared operation when available
instead of a separate replacement-only hash command. On another host, use equivalent
byte-preserving hashing to prove the original matches the declared base or effective
hash and the replacement matches its declared hash/size. A Git blob SHA, copied
manifest constant or reserialized JSON is not a computed source SHA-256.

The input bytes must come from the witnessed pinned source read; the command's revision
argument records that pin and does not independently attest a download. Preserve that
read evidence with the successful receipt. Conflicting bytes or unavailable hashing
block substitution; do not silently use a replacement or fall back to the bundle.
For offline mode, verify the manifest-mapped effective bundle and overlay instead;
do not fetch a live original. Node remains optional for ordinary host resource access.
Record the source revision and overlay identity/effective hash separately. This does
not change source selection, named-absence checks or permissions.

For installed-plugin metadata, use the package inventory rather than conventions
from another host. Relative to this router directory, the portable manifest is
`../../plugin.json`; the Codex compatibility manifest is
`../../.codex-plugin/plugin.json`. Enumerate the package root with hidden items and,
when needed, its actual metadata directories. Open only inventory-listed files.
An optional manifest absent from that inventory needs no attempted lookup. Do not
construct additional `.claude-plugin`, `.codex-plugin` or other host-layout candidates
merely because another plugin uses them. On hosts with a package-file API, use its
returned exact file paths instead. This also applies to existence/type probes:
checking an invented candidate is still a guessed path.

Before reading local file contents, verify the target exists and is a file; enumerate
directories instead of passing them to a content reader. Check the actual item type
rather than inferring it from a name or extension. In Git repositories, `.git` may be
a directory or a worktree pointer file: inspect its type before deciding how to read it.
Include hidden items in metadata checks, using `Get-Item -Force -LiteralPath` in
PowerShell or the platform equivalent. Distinguish a failed or filtered lookup from
verified absence; do not infer that a file or directory is missing from such a failure.

Read only relevant supporting resources. Resolve relative references from their source
file at the pinned commit, and apply applicable repository `AGENTS.md` instructions.
External repositories keep their own pinned revisions and setup requirements; never
upgrade an upstream import while synchronizing this library. Inspect scripts before
executing them, materialize needed files preserving relative paths, and use the actual
runtime. A text fetch does not install a package or execute a workflow.

The optional Node adapter is `scripts/source.mjs`, relative to this router's actual
directory. Its operations are subcommands of that file; do not infer another helper
filename from an operation's name. Reuse a verified helper path. If it is unavailable,
discover the actual files before attempting another path.

In reports, identify the installed skill by name and version when a local path is
unnecessary. When giving a local path, copy the exact path from its successful tool
read; do not reconstruct or abbreviate it into a different path. Label remote paths
as relative to the pinned repository revision. Reuse the recorded read evidence;
reporting alone does not require another tool call.

For literal excerpts, copy the original returned text, preserving its whitespace,
punctuation and line breaks. Parsing and reserializing JSON does not produce a literal
excerpt. When excerpts are requested from several files, quote each requested file or
identify the missing one; claim complete coverage only when all are included.

For clickable links to local files, resolve the actual file to its absolute path and
use the host's native Markdown file-link format, including any supported line suffix.
Do not use a relative repository path as the link target. Keep repository-relative
paths for describing remote resources, and use their pinned GitHub URLs when linking
to those remote resources.

Before sending the final answer, check every clickable local-file target: it must be
the actual file's absolute path in the host's supported syntax. Correct relative
targets; plain filenames need no link. Keep remote source links as pinned remote URLs.

When blocked, name the missing capability and exact next action; continue useful
independent work. State separately what was **retrieved**, **tested**, **installed**,
or **still unverified**. A successful read or simulated route is not a host execution test.

## Read the bundle only for explicitly bundled or restricted tasks

For explicit bundled operation or a task-wide offline, no-network, local-files-only
or no-external-source requirement, use [the bundled manifest](resources/offline-library/snapshot-manifest.json)
and [its native-description index](resources/offline-library/skill-index.json).
They identify `raiinman/skill-library` at packaged revision
`697672c69dcb87834cf5c75cdcd0cbd85082c6cf`, containing 137 accepted canonical workflows,
their provenance and supporting files. Label this **bundled base at the packaged
revision plus maintenance overlay `dsi-0.1.13`**, not raw upstream bytes or a current
branch check. It cannot establish whether upstream changed.
Do not resolve branches or make network calls in this mode. Do not silently fall back
from an unavailable online source to a different bundled revision.

Use the host's actual skill/resource reader, or available permitted file access, to
open bundled resources relative to this router. This works without requiring Node,
Git, a shell, Windows paths or a particular connector. If the host does not expose
packaged resource access, state that capability blocker instead of inventing a read.
The optional Node helper offers hash verification and canonical-path reads on hosts
with a suitable runtime; it is not a prerequisite for reading the bundle.

Select one primary from the index and read its entrypoint, `SOURCE.md` and needed
supporting resources. The manifest maps every canonical source path to `stored_path`.
Entrypoints named `SKILL.md` are stored as `SKILL.md.txt` solely to prevent extra native
skill registrations. Unpatched bytes remain unchanged; paths listed in the maintenance
overlay use its declared effective bytes and provenance after verification. Use this mapping
for **all** bundled reads, including sibling skill links and relative references:
resolve the reference against the canonical source path, then obtain its stored path.
The index also gives each primary's `resource_path`. Do not read the canonical
`SKILL.md` filename directly inside the bundle. Verify hashes with available tools
when needed; do not claim runtime verification that was not performed.

The [bundle scope report](resources/offline-library/bundle-report.json) records
unresolved links already present upstream. Bundling does not install external
applications, provider accounts, dependencies or archived runtimes. Report a missing
resource or capability before dependent work; do not invent successful setup.

For bundled mode, retain the manifest's repository, base revision, source kind,
maintenance overlay identity and resource mapping as the task pin. No lock file or
command is required.
