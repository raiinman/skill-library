# Runtime setup

The first 27 imported skills include their source files and local supporting resources. Their runtime setup is recorded below. Most skills are instruction-only and require no extra install. Choose project libraries and engine versions when using a skill; this collection does not install a game engine, Next.js app, or graphics framework globally.

## Existing-skill collection

An additional 73 existing skills were collected from your personal skill folders, installed engineering plugin, and standalone GitHub sources. Installed copies were preserved. Original entrypoints are saved byte-for-byte and identified by SHA256 in `sources.json`; Codex-compatible library copies retain local customizations and supporting files.

The complete engineering plugin layout is retained under `collections/agent-skills` for plugin commands and shared infrastructure. The reverse-skill layout is under `collections/reverse-skill`; three reference documents flagged by Windows Defender are replaced by pinned source pointers and listed in `MISSING-REFERENCES.md`.

Some existing skills refer to machine-specific MCP services, local checkouts, cloud accounts, or tools. Collecting them does not configure those services on another computer. Consult each package's original instructions and `SOURCE.md` when restoring it. The existing Codex system skills and vendor plugin caches remain managed by their providers.

| Skill | Runtime prerequisite | Status on the installation machine |
| --- | --- | --- |
| img2threejs | Python 3.10+, browser/vision tools; Node for generated Three.js projects | Python and Node available; forge scripts included |
| image-to-code | Codex image generation | imagegen tool available |
| game-design-document | python-docx 1.1.2, fpdf2 2.8.3, python-pptx 1.0.2 | Installed in isolated `~/.codex/tools/skill-library-gdd` environment |
| adversarial-review | Authenticated Claude CLI for opposite-model reviews | Native CLI installed; sign-in must be completed by the user |
| map-systems / day-one-patch | Studio config/docs/roles and optional Git Bash YAML helper | Supporting files included in each package; Git Bash already available |
| okx-cex-portfolio | `@okx_ai/okx-trade-cli` 1.4.8 and account authentication | CLI and its verified auth/pilot binaries installed; user sign-in remains |
| okx-dex-market | OnchainOS CLI and account authentication | Windows release installed with SHA256 verification; user sign-in remains |

## Brainstorming

The adapted `brainstorming` skill includes its original source, MIT license, builder prompt, and optional visual companion. Its companion uses Node.js standard-library modules and Bash; both Node and Git Bash are available on this machine. No npm dependencies or Superpowers plugin install are needed. The Codex launch guide is bundled in the package, and the launcher disables upstream branding telemetry. ADHD-friendly facilitation guidance adds flexible idea capture, optional mind maps and short rounds, and restart checkpoints; bundled research notes record the sources and evidence limits.

## REA reverse engineering

`reverse-engineer-anything` is aligned with the published `rea-agents@6.4.0` release. Its single installed copy is in `~/.agents/skills/reverse-engineer-anything`, the shared skill root used by Codex and REA's readiness check; use that destination when restoring this package. The REA CLI is installed globally, and its stdio MCP registration is configured only for Codex, using the installed Node launcher and a 30-second startup timeout. The original Codex configuration is backed up as `~/.codex/config.toml.rea.backup`; unrelated settings are preserved. Restart or reconnect Codex after installation to load the new tools.

The package includes its seven released workflow files, original repository entrypoint, MIT license, upstream README, and 44 release guides. Restore the runtime with `npm install --global rea-agents@6.4.0`. Node.js 22.19+, 24.11+, or 26+ is required on the supported release lines. Static JavaScript analysis works without a disassembler. Native decompilation needs a supported configured Ghidra, Hopper, or IDA provider; other specialized workflows have their own host and tool prerequisites. No native analysis engine was configured during this installation.

## Windows paths

- Claude and OnchainOS: `~/.local/bin/claude.exe`, `~/.local/bin/onchainos.exe`.
- Git Bash: normally `C:/Program Files/Git/bin/bash.exe`.
- GDD Python: `~/.codex/tools/skill-library-gdd/Scripts/python.exe`. Use that interpreter with the included generator scripts. On another computer, create an environment and install the skill's `requirements.txt`.
- Account sign-in: start `claude` for Claude, `okx config init` for OKX CEX, and follow the DEX shared preflight/login references for OnchainOS. Do not paste credentials into chat or this repository.

## Import limitations

- `next-best-practices` and `managing-timelines` are pinned archived versions of the exact requested skills. Upstream replaced or removed them. Use current official documentation for version-specific guidance.
- The current img2threejs source references some external domain plugins and `runtime/` scripts that it does not include. The base forge package is installed. Optional animation/domain workflows need those additional upstream packages; their absence is not a successful gate result.
- Claude-specific tool names and dynamic prompt expansion were adapted with notes for Codex. Studio workflow dependencies are bundled as `WORKFLOW.md` references rather than registering every studio workflow in your skill picker.
- Adversarial review's 16 required principles and their available linked context are included. Some historical links are already missing upstream; the package lists those in `references/upstream-missing-links.md`. Do not invent the missing context or recursively reread cycles.
- OKX routing targets beyond the requested portfolio and market skills are not registered as additional skills. The CEX authentication workflow is included as a reference. OnchainOS's full installer may also install other skills and an A2A daemon; this import installed the verified CLI directly to preserve the requested scope.
- Chaos experiments require the infrastructure and failure-injection tool chosen for the actual experiment. No production chaos experiment was run as part of installation.

Validation covers Codex metadata, packaged resources, installed-file parity, CLI versions, and small generator checks. It does not claim every skill workflow has been executed.
