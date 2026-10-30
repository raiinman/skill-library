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

## Roll the dice

`roll-the-dice` uses a Python standard-library helper for an actual uniform draw among viable options, then follows the selected path through the authorized task. Python is already available; no package installation is needed. Run its bundled check with `python -X utf8 scripts/test_roll.py` from the skill folder. The poem is an attributed inspiration, with no poem text included.

## Video and audio

Three packages are in `skills/video-and-audio`: `video-editing`, `seedance-2-0-prompter`, and `ai-video-generation`. Their pinned originals and all requested-skill supporting files are included. The first two retain their upstream MIT licenses. The inference-sh source has no license file or explicit grant in its pinned tree; no license is assigned to that package. Confirm permission before further redistribution or reuse that requires a license.

- Local editing: FFmpeg and ffprobe 8.1.2 are already installed through WinGet. A synthetic cut/export/decode check verifies the local editing route. Remotion is optional and belongs in a project that needs programmable composition. Cloud voice, transcription, stock, and generation services are optional and need their own accounts or tools.
- Seedance prompting: instruction-only, with all three reference guides. No Pexo CLI or account is needed. Generation uses a chosen provider's actual upload identifiers and schema, not just `@filename` prose.
- AI generation: native inference.sh `belt` v1.25.9 installed in `~/.local/bin`, with `infsh` and `inferencesh` aliases. The vendor manifest ZIP SHA256 was verified: `d1a63616e8ecc932872aaff1bb65f29480328d924e9a4721af4855e1d48dda0d`. CLI version/help checks passed. Sign in with `belt login` before cloud generation. No paid generation, upload, or account creation was performed during installation.
- Fusion: both complete preset bundles, their provenance, and original macOS Lua installers are retained. Windows installation guidance is bundled separately. DaVinci Resolve is optional and was not found at its standard Windows location; no native Fusion import or render was tested here. Upstream native-test claims remain labeled as upstream results.

## Arcads marketing skills

All 16 requested Arcads skills are packaged in `skills/marketing-and-ads` with the `arcads-` prefix for clear Codex discovery. Each includes its original entrypoint, creative workflow, needed references, runtime compatibility notes, and picker entry. The complete 28-file upstream source at commit `7af9117e45a8f4ddc2cae60283baf701eae66b4b` is preserved in `collections/arcads-skills`, including both plugin manifests and the original build script. Both manifests declare MIT; upstream supplies no standalone license text.

The official remote MCP server `https://mcp.arcads.ai` is registered in this computer's Codex configuration. A read-only preflight returned HTTP 401 with OAuth resource discovery, so authentication and actual generation remain untested. Complete `codex mcp login arcads` when ready to use Arcads and reconnect Codex. An Arcads account and its credits are separate from Google AI Pro and inference.sh. No Arcads subscription, upload, or generation was performed.

No local Arcads daemon or package installation is required. FFmpeg/ffprobe are already installed for local video assembly. Competitor research uses the connected browser's supported download methods, and prompt-only templates work without an Arcads account. The upstream `jq`/`zip` build script is optional for recreating plugin ZIPs; it is not needed for these installed Codex skill folders. Codex configuration before registration is backed up locally in `~/.codex/tmp/arcads-import/config-before.toml`; it is not included in this repository.

## Interface design and motion

Five skills were added on 2026-10-17: `antigravity-design-expert`, `mobile-app-ui-design`, `ui-animation`, `game-ui-design`, and Anthropic's `frontend-design`. Each includes its original entrypoint, available supporting resources, source commit/hash, licenses or license declarations, and Codex picker metadata. These are local filesystem skills for the desktop app/Codex. This does not publish them as cloud workspace skills or universal-directory plugins.

Four are instruction-only and require no additional runtime. Their suggested frameworks and services are task-specific choices, not global prerequisites. The `ui-animation` package includes all three upstream Python tools, 18 reference guides, and its evaluation fixtures. Its `extract_frames.py` uses a numbered PNG sequence for Windows compatibility, validates extraction arguments, and refuses to overwrite prior extraction files. The original changed script is archived. Run the bundled pipeline regression check to verify extraction, tracking, fitting, and prior-output protection.

Python 3.11 with OpenCV, NumPy, and SciPy is installed in `~/.codex/tools/skill-library-ui-animation`; use its `Scripts/python.exe` on Windows. Dependencies are pinned in the skill's `requirements.txt`. FFmpeg/ffprobe are already installed. Framework packages such as GSAP or Motion belong in the actual project only when required. No paid service or account sign-in is needed for these five skills.

The spatial design skill's prose is CC BY 4.0 under its included content notice, with MIT for upstream tooling. Mobile UI's README declares MIT but has no standalone license file. Anthropic's requested entrypoint was byte-identical to its official `anthropics/skills` copy, whose Apache-2.0 LICENSE.txt is bundled to resolve the missing license reference. Provenance records both locations.

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

## Unity development

`unity-developer` and `unity-ecs-patterns` are instruction-only packages in `skills/game-development`. Both include pinned originals, supporting examples where provided, MIT licenses, and Codex picker metadata. They require no extra Python, npm, or cloud service installation. The adapted ECS entrypoint routes through caveats for the upstream snippets before reuse.

Unity compilation, profiling, tests, and builds require the actual project, its editor version, packages, applicable license, and target modules. The separately installed local `unity-cli` skill and Unity CLI can support editor work when the target project provides a compatible connection. This import does not install or upgrade an editor or add packages to any project. No Unity project compilation or runtime test was performed during packaging.

Local installs are discoverable by Codex and compatible local ChatGPT desktop workflows. Publishing these files on GitHub does not install skills into the ChatGPT web or mobile account.

## Image to Blender

`img2blender` is the native Blender adaptation of the pinned library `img2threejs` skill. It uses Blender's bundled Python, editable `.blend` files, subject-specific build scripts, and visual correction passes. It does not require Three.js, npm, a neural model, or a Blender MCP server. Blender 5.2.1 LTS is already installed on this machine; no application or global configuration changes were needed.

The bundled headless review helper captures a reference camera and four orbit views, reports evaluated geometry and resource warnings, and preserves the source file. Its real Blender smoke test covers reopen/render behavior, modifier and instance reporting, image dimensions, and refusal to overwrite evidence. Fidelity, rigging, and exported assets need their own visual and target-specific checks. See the package's `references/blender-execution.md` for commands and limits.

The revised helper defaults to both beauty and neutral clay captures (ten views with a reference camera), with `--mode beauty` retaining the original five-image route. Optional landmarks report projected pixel residuals; the standard-library checkpoint helper freezes explicitly selected build/spec/input files with hashes and the recorded build command. The workflow fits camera evidence before proportion changes, separates geometry from textured likeness, and adds a conditional flat-graphic/relief route. External tutorial and game-skill review findings are bundled as references; the external game-skill package itself is not installed.

## Additional Blender skills, 2026-10-18

`blender-web-pipeline`, `blender`, `blender-addon-engineer` and `blender-mcp` are installed as separate Codex skills in the 3D and Web category. All four include pinned original instructions, supporting files and MIT licenses. The web pipeline replaces its unsafe historical scripts with an explicit-collection helper for GLB export, batch conversion and editable optimization/LOD copies. Its smoke test uses installed Blender 5.2.1 and standard-library Python; no additional pip/npm packages are needed for those operations.

The MCP skill supports an available live bridge and a native saved-file fallback. This import does not register a live Blender MCP server, enable an interactive Blender add-on, authenticate external asset services or install every optional browser engine/compression tool mentioned upstream. Those are selected for actual projects. The local Blender fallback is usable immediately; skill discovery refreshes on the next turn.

## Blender agent and specialist bundles, 2026-10-18

Three additional top-level Codex skills preserve whole upstream repositories inside checksummed ZIP archives: `llm-blender-agent` (saofund application adapter), `cc-blender-toolkit` (30 RobLe3 specialist guides) and `blender-studio` (94 arjun988 specialist guides, plus its archived Cursor mirror). Each has one picker entry and an on-demand module index. Sources are extracted outside skill discovery under `~/.codex/tools/blender-bundles/<skill-name>` so original nested skills do not create name collisions. The bundled materializer verifies archive and file hashes, refuses existing destinations and never runs source code.

The saofund add-on import/register/unregister check passed in an isolated Blender 5.2.1 process. RobLe3's 35 core recipe checks passed with a narrow Windows path-safe test adapter, and its 12 export/collision/bake regressions passed unchanged. Its synthetic image-helper test passed using the existing isolated `skill-library-ui-animation` Python environment (NumPy, SciPy, OpenCV and newly installed Pillow 13.0.0). This does not imply every source script, art style, external provider or target-engine import was tested.

Native saved-file Blender work is available. Original Gradio/provider apps, Hunyuan model weights, external credentials and live MCP services are separate optional runtime branches. No source client configuration was applied by this import. Complete code, documentation, support files and images remain backed up in the published skill packages; source archives are pinned rather than fetched again at task time.

## Reviewed testing and evidence guidance

Three instruction-only packages were added on 2026-10-27: `property-based-testing`, `cpp-testing` and `native-evidence-review`. Each includes its pinned original entrypoint, full original license and source/change notice. Property-based testing includes all five upstream Markdown reference guides under CC BY-SA 4.0; the other two preserve their MIT notices. The C++ adaptation links primary Microsoft documentation instead of applying GCC/Clang sanitizer or coverage commands to MSVC. The evidence review is manual and reuses the existing DSI/REA specification, evidence records and acceptance owner rather than creating a second case ledger.

No dependency, executable helper, hook, target-input access, compiler, test framework or analysis engine is installed by these packages. Use already available authorized tools; missing runtimes/dependencies remain separate prerequisites. Generated/property tests and synthetic fixtures do not supply original-game expected behavior or establish game boot. Existing stopped/gated work and source-eligibility holds remain unchanged.

The installed DSI live-source helper discovers these canonical entries through `CATALOG.md` and their native `SKILL.md` frontmatter; the router separately requires reading the adjacent `SOURCE.md` provenance. Discovery is not provenance validation. No helper code/provider change or replacement of the older offline bundle is required. Library publication, successful live retrieval, native skill registration and target-runtime execution are different states and must be reported separately.

## Native game systems and authoring tools, 2026-10-29

Ten integration skills cover Jolt Physics, Terrain3D, Material Maker, Effekseer, Voxel Tools for Godot, Recast Navigation, ozz-animation, The Forge, meshoptimizer and FastNoise2. Each retains pinned official documentation and root licenses. The complete upstream repositories are forked under raiinman and indexed in [GAME-TOOLS.md](GAME-TOOLS.md). Integration guides are host-neutral Markdown with Codex picker metadata and Claude-compatible names.

These software repositories are libraries/editors rather than pre-existing agent skills. Installing their integration guides does not compile ten SDKs, replace an engine backend or install external engine plugins into unrelated projects. Choose a supported release and install/build dependencies in the specific project that needs them. Target-engine binaries, platform SDKs and runtime integration still require project-specific verification.

The DSI router package includes current canonical discovery and bundled resources, retaining its maintained workflow overlays. Root Agent Plugins, Codex compatibility and Claude plugin/marketplace manifests refer to the same router package. It loads focused guide content on demand rather than registering every archived copy as another native skill. Local standalone skills and the plugin keep distinct source ownership.

## Unslop

`unslop` is available as a shared local skill for Codex and Claude and through the DSI Skills router. It retains Damir Sokolovsky's attribution, CC BY 4.0 license, references, example pages and both Node helpers. Optional helper dependencies are installed separately in `C:/Users/mikea/.codex/tools/unslop`; FFmpeg is already on PATH. See [runtime notes](skills/design-and-art/unslop/references/runtime.md). Installing this skill does not redesign any current project or configure a paid image service.
