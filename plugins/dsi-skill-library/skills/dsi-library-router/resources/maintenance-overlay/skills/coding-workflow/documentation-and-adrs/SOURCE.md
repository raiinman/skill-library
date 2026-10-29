# Source

- Origin: installed-plugin-snapshot
- Original skill SHA256: `00cfbc625adf6ad21b3203e6845267bbd599dc2d4314d7b0a8c35820371352a3`
- Added: 2026-10-09
- License: MIT
- Related pinned GitHub source: https://github.com/raiinman/agent-skills/blob/09644278517cb57a9447cbeaddb3395b6fcf4a56/skills/documentation-and-adrs/SKILL.md

This preserves the installed version, including local customizations. A related GitHub commit is provenance context, not a claim that this local version is identical.

## Packaging

- Backup of existing skill; installed copy left intact
- Codex-compatible frontmatter; original SKILL.md preserved byte-for-byte

## Targeted upstream follow-up

- Repository: https://github.com/addyosmani/agent-skills
- Revision: `aeac41d4d005999432bb7312f7ff06383a91d59d` (Agent Skills 0.6.13, released 2026-10-13)
- Reviewed entrypoint: https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/documentation-and-adrs/SKILL.md
- Incorporated change: Preserve names, commands, paths, caveats and uncertainty during prose editing.
- Existing installed-snapshot hash and original reference are retained; this is a selective update, not a wholesale replacement of the local fork.
- License: MIT; existing attribution remains in place.
