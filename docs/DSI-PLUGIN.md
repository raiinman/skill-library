# DSI Skill Library 0.1.0

This plugin bundles one native `dsi-library-router` skill and indexes 137 canonical
packages across 18 categories. Nested skill copies and preserved `collections/`
bundles are not additional registrations. Original snapshots, customizations,
attribution, licenses and upstream pins remain in place; no blanket license is assigned.

## Package and routing

The portable package is `plugins/dsi-skill-library/`, with root Agent Plugins 1.0
`plugin.json` and a synchronized `.codex-plugin/plugin.json` compatibility manifest.
The marketplace is `.agents/plugins/marketplace.json`. No hosted server, new provider,
or speculative app dependency is required. The environment exposes connected GitHub
`fetch_commit` and `fetch_file`; their schemas support commit-pinned retrieval.

The router compares native descriptions in the generated `skill-index.json`, gives
explicit skill/provider choices precedence, and loads one primary workflow plus the
smallest useful supporting set. `using-agent-skills`, `arcads-media-router` and
`reverse-skill-router` retain their distinct scope. Small follow-ups reuse loaded
context. Automatic discovery remains a host/model decision, not a forced pre-response hook.

`scripts/build-plugin.mjs` generates the discovery index, full provenance and file
hashes in `skill-resources.json`, a Markdown reference report in `resource-report.json`,
and the packaged discovery snapshot. Native `description` comes from each canonical
`SKILL.md`; optional custom `metadata.dsi` is recorded as `routing_metadata` and is
not a native discovery field. No duplicate handwritten trigger catalog is maintained.

The first audit finds 91 active and 419 archived unresolved/outside-package Markdown
references. This is a pre-existing resource backlog, not proof every indexed workflow
is executable. The report distinguishes files and link targets, and is reviewed as a
generated diff. Bare code paths, archive contents, tools, accounts and local applications
need task-time checks. Existing entrypoints were preserved except targeted discovery
corrections for UEFN, the engineering phase router, and premium visual design. Historical
global installation no longer implies current availability; engineering session-start
activation and premium design activation now have focused boundaries. Further metadata
improvements should follow concrete routing evidence.

## Install locally

On this machine, Codex CLI `0.163.0-alpha.10.2` supports the following commands.
The CLI surface is newer than the documentation's desktop-only local installation advice.

```powershell
codex plugin marketplace add "<absolute path to this repository>" --json
codex plugin add "dsi-skill-library@dsi-skill-library" --json
codex plugin list --marketplace dsi-skill-library --json
```

Restart Codex and start a new chat if the router has not entered the skill catalog.
Ask: “Use DSI Skill Library to choose a workflow for debugging this failing build.”
For this unmerged implementation, explicitly add “Use source branch
`feat/dsi-skill-library-plugin`.” Default `main` does not contain the generated index
until the PR is merged. Do not describe the branch as accepted main content.

After the PR is accepted, a Git-backed marketplace can be registered using:

```powershell
codex plugin marketplace add raiinman/skill-library --ref main --json
codex plugin marketplace upgrade dsi-skill-library --json
```

Use either the local development source or Git-backed source for this marketplace
identity. Remove the existing marketplace registration before switching its source;
inspect installed state first. Avoid registering duplicate marketplace identities.

## Refresh and rollback

Skill content and router releases have separate update paths:

- **Content:** commit accepted changes to canonical packages, run `npm ci --ignore-scripts`,
  `npm run build`, `npm run check`, `npm test`, and commit generated outputs together.
  A new substantive task resolves the intended branch to a new commit. Existing task
  locks retain their original commit. Upstream imports are never upgraded by the generator.
- **Router:** change the package, bump both manifest versions, validate, and refresh the
  marketplace. `marketplace upgrade` updates Git marketplace snapshots. For local
  development, refresh the installed copy by removing and re-adding the plugin, then
  restart the app; source edits alone do not demonstrate the cached copy is current.
- **Rollback:** retain the versioned private ZIP and implementation commit. Remove the
  plugin, restore the previous reviewed package/checkout, re-add and verify it. For
  content rollback, explicitly select a prior repository revision for the next task;
  retain existing locks. Do not reset unrelated working-tree changes.

```powershell
codex plugin remove "dsi-skill-library@dsi-skill-library" --json
codex plugin add "dsi-skill-library@dsi-skill-library" --json
# To remove the marketplace too:
codex plugin marketplace remove dsi-skill-library --json
```

There is no claimed native rollback command. Inspect versions and cached files after
reinstallation. Router instructions support explicit revision selection through GitHub;
the local helper accepts branch names and records their immutable resolved SHA.

## Personal ChatGPT and workspace administration

No `create_plugin` account-upload tool is exposed in this environment. The private
ZIP is preserved, but account saving and ChatGPT web/mobile installation remain
unverified. A local Codex installation does not install it into those products.
If an account package-creation surface becomes available, upload the private plugin
ZIP, inspect its component diagnostics, install it, and verify the router in a fresh
chat with GitHub connected. MCP-imported native skills remain snapshots requiring
rescan and a new plugin version; this router's explicit source reads are a separate path.

Workspace admins with the actual interface can use Admin > Plugins > Add > Import
marketplace, repository `https://github.com/raiinman/skill-library`, empty Path, and
the intended branch (default `main` after merge). New marketplaces default to daily
sync; use Marketplaces > Sync now for an explicit refresh. Review import results and
required connections. This workflow was checked in documentation, not this account's UI;
Pro does not establish administrator access.

## Suggested persistent preference (not applied)

ChatGPT Custom Instructions:

> For applicable substantive tasks, use the installed DSI Skill Library router to select
> a focused workflow. Honor explicitly named skills, providers and approved project
> decisions. Pin current repository instructions once per task; reuse them for small
> follow-ups. Report unavailable tools or source access honestly. Skip routing for
> ordinary conversation and simple answers.

Codex equivalent: place the same paragraph in the intended project's `AGENTS.md`, or
in `~/.codex/AGENTS.md` for a personal default after reviewing its broader scope.
Neither preference has been changed by this implementation.

## Evidence and limits

Automated tests exercise inventory failures, malformed YAML, resource changes,
deterministic generation, CRLF handling, and a real temporary Git origin update.
The reader test proves a retained revision stays fixed, explicit refresh reads a new
commit, binary delivery is unchanged, and local edits survive. Invalid paths, missing
resources, failed fetches and overwrite attempts fail explicitly.

Representative prompt decisions are instruction-level review, recorded separately in
`ROUTING-REVIEW.md` and `tests/routing-cases.json`. They do not establish fresh-chat
implicit selection or successful Blender/UEFN/provider execution. GitHub-connected
reads, local installation, and any remote CI results are recorded in `DSI-HANDOFF.md`.

## Official documentation checked 2026-10-20

- [Package format, marketplaces and updates](https://developers.openai.com/plugins/build/plugins)
- [Build skills](https://developers.openai.com/plugins/build/skills)
- [Skill discovery](https://learn.chatgpt.com/docs/build-skills)
- [Create plugins](https://learn.chatgpt.com/docs/build-plugins)
- [Workspace GitHub import and sync](https://learn.chatgpt.com/docs/enterprise/plugin-management)
- [Plugin availability](https://learn.chatgpt.com/docs/plugins)
- [Personal instructions](https://learn.chatgpt.com/docs/personalize)
