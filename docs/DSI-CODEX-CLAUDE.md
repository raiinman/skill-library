# DSI wiring for Codex and Claude Code

The canonical library contains 155 top-level integration/workflow packages. DSI Skills 0.1.22 exposes one router and bundles all 155 packages with hash-verified provenance and resources. It preserves the existing 29 reviewed workflow replacements, rebased only after their original-source hashes match. The ten new game-system repositories are forked under raiinman and cataloged in [GAME-TOOLS.md](../GAME-TOOLS.md).

## Host formats

- `plugins/dsi-skill-library/plugin.json`: portable account plugin manifest.
- `plugins/dsi-skill-library/.codex-plugin/plugin.json`: matching Codex compatibility metadata.
- `.agents/plugins/marketplace.json`: Codex marketplace entry for that package.
- `plugins/dsi-skill-library/.claude-plugin/plugin.json`: Claude's native plugin manifest.
- `.claude-plugin/marketplace.json`: Claude marketplace entry for the same package.

The native router entrypoint and resource reader are shared across hosts. Archived entrypoints inside the offline library use `SKILL.md.txt`, so they are not competing native registrations. Explicit skill names still select the corresponding canonical guide through the router; source/provider constraints and task revision pinning remain unchanged.

## Install or refresh

Claude Code:

```text
claude plugin marketplace add raiinman/skill-library
claude plugin install dsi-skill-library@dsi-skill-library --scope user
```

For an existing registration, inspect the marketplace and update the existing plugin rather than creating another identity. Codex can use the existing private DSI Skills account installation or the repository marketplace:

```text
codex plugin marketplace add raiinman/skill-library --ref main --json
codex plugin add dsi-skill-library@dsi-skill-library --json
```

Do not install both copies merely to refresh one existing source. Keep unrelated marketplace registrations and settings intact. Restart the host or start a new session to load refreshed discovery. Installation/discovery is different from proving a future model will implicitly select the right workflow.

For direct local discovery, install a canonical skill into `~/.agents/skills/<name>` for Codex. Claude user skills use `~/.claude/skills/<name>`. A directory junction to the shared canonical copy avoids two drifting copies on this Windows machine. Existing legacy skills are outside this maintenance change.

## Maintain and verify

Commit accepted canonical changes first, then run:

```text
python -B scripts/sync-dsi-library.py --revision <committed-canonical-revision>
python -B tests/test_dsi_game_tools.py
claude plugin validate plugins/dsi-skill-library
claude plugin validate .claude-plugin/marketplace.json
node plugins/dsi-skill-library/skills/dsi-library-router/scripts/source.mjs verify --snapshot plugins/dsi-skill-library/skills/dsi-library-router/resources/offline-library
```

The maintenance script requires PyYAML and Git. It reads committed Git blobs, preserves their exact bytes, and refuses to rebase a maintained replacement against an unexpected original hash. It excludes unrelated working-tree edits. No runtime npm install is required for the bundled Node reader; its YAML parser is preserved with its license.

The tests exercise all ten named primaries and SOURCE.md retrieval through the actual pinned reader, complete snapshot integrity, tampered-body rejection and equal host plugin identities/versions. Regeneration was checked for determinism. These checks do not compile ten SDKs or claim real project/engine integration; those need a target project and its compatibility constraints.

A private account release update must use the existing plugin ID and observed current release guard. Preserve its audience, metadata and unrelated configuration. This repository contains the reproducible source; the host's installed cached version remains a separate verification step.

## Branding

DSI Skills is the display name. The stable package identity remains `dsi-skill-library` so existing installations keep their settings. The custom app icon is packaged at `plugins/dsi-skill-library/assets/dsi-skills-icon.png` and is shared by the listing and composer. Claude Code retains its native text-based plugin listing.
