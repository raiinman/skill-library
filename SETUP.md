# Runtime setup

All 27 skills include their source files and local supporting resources. Most are instruction-only and require no extra install. Choose project libraries and engine versions when using a skill; this collection does not install a game engine, Next.js app, or graphics framework globally.

| Skill | Runtime prerequisite | Status on the installation machine |
| --- | --- | --- |
| img2threejs | Python 3.10+, browser/vision tools; Node for generated Three.js projects | Python and Node available; forge scripts included |
| image-to-code | Codex image generation | imagegen tool available |
| game-design-document | python-docx 1.1.2, fpdf2 2.8.3, python-pptx 1.0.2 | Installed in isolated `~/.codex/tools/skill-library-gdd` environment |
| adversarial-review | Authenticated Claude CLI for opposite-model reviews | Native CLI installed; sign-in must be completed by the user |
| map-systems / day-one-patch | Studio config/docs/roles and optional Git Bash YAML helper | Supporting files included in each package; Git Bash already available |
| okx-cex-portfolio | `@okx_ai/okx-trade-cli` 1.4.8 and account authentication | CLI and its verified auth/pilot binaries installed; user sign-in remains |
| okx-dex-market | OnchainOS CLI and account authentication | Windows release installed with SHA256 verification; user sign-in remains |

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
