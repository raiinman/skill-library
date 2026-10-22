# DSI plugin implementation handoff — 2026-10-20

## Decisions and status

- **Implemented:** native portable plugin 0.1.0 plus Codex compatibility manifest,
  repository marketplace, one router, deterministic canonical indexes, resource audit,
  revision-locked reader, and Windows/Linux CI definition. No hosted MCP server.
- **Indexed:** 137 canonical packages /18 categories; only `dsi-library-router` is bundled
  as an installed skill. Discovery snapshot contains metadata, not executable bodies.
- **Tested:** nine automated tests and package/reference validation pass on Windows.
  Fourteen representative routing cases have manual instruction review; they are not
  fresh-chat selection tests. The real temporary Git-origin test verifies updates,
  retained task revisions, binary reads, missing resources, and preserved local edits.
- **Installed:** Codex CLI confirms `dsi-skill-library@dsi-skill-library`, version 0.1.0,
  installed and enabled. A remove/re-add refresh also succeeded. This CLI caches the
  package under a version directory `0.1.0`, although official documentation describes
  `local` for some local sources. Use the actual CLI-returned installedPath.
- **Still unverified:** fresh-chat implicit selection, ChatGPT account saving and web/mobile
  installation, administrator UI access, and Blender/UEFN/provider workflow execution.
  No account `create_plugin` upload tool is available. Do not infer access from Pro.

## Source baseline and review

Started from clean `main`, revision `697672c69dcb87834cf5c75cdcd0cbd85082c6cf`,
matching the supplied checkpoint. Implementation branch: `feat/dsi-skill-library-plugin`.
The final implementation revision is the branch head; use `git rev-parse HEAD` or the PR.
Only three canonical entrypoint descriptions were narrowed based on review; UEFN also
received an early input/output/capability contract. Original snapshots and pins remain intact.

Connected GitHub successfully resolved `main` with `fetch_commit` and read `README.md`
at that exact revision using `fetch_file`. The local branch-list tool did not return
a SHA, so it is not sufficient for source locking. GitHub CLI is absent; shell Git
push required unavailable credential-manager authentication, so connected GitHub Git
object APIs provide the authorized alternative for publishing the implementation branch.

The resource audit reports 91 active and 419 archived unresolved/outside-package
Markdown references. These include legacy relative links in nested documents. Review
`resource-report.json` before treating a selected workflow's resources as executable.
The scan is deliberately bounded to Markdown links, not all bare paths or archive internals.

## Continue and verify

Default source `main` lacks the new index until this PR is accepted. Test this unmerged
package with explicit source branch `feat/dsi-skill-library-plugin`; do not silently
call that accepted main content. No merge or public directory publication is authorized.

Restart Codex and open a fresh chat. Ask:

> Use DSI Skill Library with source branch feat/dsi-skill-library-plugin. Choose the
> workflow for debugging a failing build. Report the source commit, selected skill,
> and any unavailable capabilities before starting the workflow.

Expected: resolve the branch to one SHA, read its index and
`skills/coding-workflow/debugging-and-error-recovery/SKILL.md` at the same SHA, preserve
the revision on a minor follow-up, and distinguish retrieval from actual debugging.
Repeat the representative prompts in `tests/routing-cases.json` in clean chats for
host-level acceptance. Ordinary greetings and minor edits should avoid rerouting.

Installation, refresh, rollback and the suggested persistent routing instruction are
in `DSI-PLUGIN.md`. Account preferences were not changed. For ChatGPT installation,
use an available private package upload/account tool or a real workspace admin import;
inspect component diagnostics and verify GitHub access independently.
