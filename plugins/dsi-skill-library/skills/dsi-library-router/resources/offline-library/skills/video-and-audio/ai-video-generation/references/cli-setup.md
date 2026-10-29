# CLI setup and Windows use

Official setup: https://inference.sh/docs/extend/cli-setup
Pinned upstream installation notes: [upstream-cli-install.md](upstream-cli-install.md).

On this computer, `belt.exe`, `infsh.exe`, and `inferencesh.exe` are installed in `C:/Users/mikea/.local/bin`, already on the user PATH. Native Windows CLI v1.25.9 was downloaded from the official `dist.inference.sh` manifest and its ZIP SHA256 verified on 2026-10-16:

`d1a63616e8ecc932872aaff1bb65f29480328d924e9a4721af4855e1d48dda0d`

On another computer, use the current official installer for that OS. Review the script, download the native architecture, verify its published SHA256, and install to a user-local binary folder. Installing a CLI is separate from account sign-in and paid generation; no background daemon or MCP server is needed for this skill.

`belt auth status --no-input` checks readiness without printing an API key. `belt login` is the interactive sign-in step. For Codex, use noninteractive commands and JSON files for request inputs; quote absolute paths containing spaces. If PATH has not refreshed, use the executable's full path. Never use `belt auth token` merely to check sign-in.

The CLI's built-in `app get`, `app run`, and `task get` help is the authoritative source for installed-version flags. Before adapting APIs or CLI syntax, consult current official documentation. The pinned upstream model examples are not promises of availability or a universal schema.
