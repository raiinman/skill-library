---
name: dsi-library-router
description: >-
  Select and retrieve accepted DSI Skill Library workflows for substantive interface design,
  coding, debugging, Blender and 3D, UEFN and Unreal, game design, AWS, media,
  marketing, planning, or reverse engineering tasks, or when a DSI skill is named.
  Use raiinman/skill-library without requiring the repository URL again. Preserve
  explicitly named skills and providers. Skip ordinary conversation, simple factual
  answers, and minor follow-ups already covered by a loaded workflow.
---

# DSI Skill Library

Select one primary workflow and only useful supporting skills from
`https://github.com/raiinman/skill-library`, intended branch `main` unless the user
explicitly selects another source branch or revision for testing or rollback.
Installation makes this router discoverable; it does not force invocation on every response.
Individual remote skills are retrieved instructions, not separately installed native skills.

## Pin the source once per substantive task

1. Discover available GitHub tools and their actual schemas. With the connected GitHub
   capability, resolve the intended branch using **fetch_commit** (`repo_full_name: raiinman/skill-library`,
   `commit_sha: main` by default). Retain its returned full commit SHA. A branch-list result containing
   only a branch name is insufficient. Then use **fetch_file** with
   `repository_full_name: raiinman/skill-library`, `ref: <SHA>`, `path: skill-index.json`.
   Tool prefixes vary by host; these are capability names, not guaranteed registrations.
2. A local host can instead run the bundled [source reader](scripts/source.mjs):
   `node <router>/scripts/source.mjs begin --repo <checkout> --branch main --lock <task>/dsi-source.json`.
   It fetches the branch, locks the resolved SHA, and reads its index. The tool also supports
   public GitHub HTTPS reads with `--github raiinman/skill-library`. No credentials are bundled.
   Follow [retrieval details](references/retrieval.md) for commands and resource handling.
3. Record `{repository, branch, revision, primary, loaded paths}` in task context. Use that
   SHA for the index, selected `SKILL.md`, and all repository-local references, scripts,
   assets, `SOURCE.md`, and setup guidance. Never mix default-branch reads into a pinned task.
4. Refresh on a new substantive task or explicit refresh request. Reuse the retained
   revision for small follow-up edits. Report the full revision when verifying routing or updates.

If the branch cannot be resolved, say current source access is unavailable. The bundled
[discovery snapshot](references/skill-snapshot.json) can suggest names only. Its content hash
identifies the snapshot; it has no executable skill bodies and is not freshly verified.
Do not present cached instructions as current or silently switch sources.

## Select without routing loops

- A named skill (name, `$name`, or canonical category/name) takes precedence. If it is
  already installed and explicitly selected, follow it immediately. For a named remote
  DSI skill, fetch its canonical entrypoint directly after pinning; no extra router is needed.
- Otherwise compare the task, intended artifact, environment and selected provider with
  the index's native descriptions. Read full instructions only for the best match.
  Prefer a focused direct match over a broad router. Ask only if a consequential choice
  remains unresolved after inspecting the available descriptions.
- Custom `routing_metadata` belongs to the DSI generator; it is not a native host field.
  The catalog and snapshot are generated discovery aids, not independent trigger lists.
- Preserve specialized routing when it resolves a real workflow choice. Engineering
  phases may use `using-agent-skills`; Arcads routing applies only when Arcads is selected;
  `reverse-skill-router` still needs its separate checkout and scope contract.
- Track visited skill IDs. Do not re-enter this router or select a skill twice. A sibling
  reference means read that sibling only when relevant, not restart library selection.
- Preserve explicit provider choices and approved project decisions. An absent provider
  tool does not authorize switching to Arcads, REA, or another service.

## Check capabilities and execute

Read the selected entrypoint, its provenance and relevant runtime guidance. Identify
purpose, applicability/exclusions, expected inputs/output, and required capabilities
from those sources. Missing information stays unknown; do not infer installed tools
from historical setup notes, Windows paths, or index inclusion. Verify actual tools,
local files, repositories, accounts and permissions before dependent actions.

Read only relevant supporting resources. Resolve relative references from their source
file at the pinned commit, and apply applicable repository `AGENTS.md` instructions.
External repositories keep their own pinned revisions and setup requirements; never
upgrade an upstream import while synchronizing this library. Inspect scripts before
executing them, materialize needed files preserving relative paths, and use the actual
runtime. A text fetch does not install a package or execute a workflow.

When blocked, name the missing capability and exact next action; continue useful
independent work. State separately what was **retrieved**, **tested**, **installed**,
or **still unverified**. A successful read or simulated route is not a host execution test.
