# Skill Library

Your home for skills. 103 skill packages are organized by purpose, including the first 27 imports, your existing GitHub, local, and engineering-plugin skills, and brainstorming, REA, and random decision workflows.

## Find what you need

| Folder | Skills |
| --- | ---: |
| [3D And Web](skills/3d-and-web/) | 6 |
| [Business Planning](skills/business-planning/) | 1 |
| [Cloud And Aws](skills/cloud-and-aws/) | 23 |
| [Coding Workflow](skills/coding-workflow/) | 33 |
| [Design And Art](skills/design-and-art/) | 3 |
| [Engineering](skills/engineering/) | 1 |
| [Finance](skills/finance/) | 2 |
| [Game Design](skills/game-design/) | 5 |
| [Game Development](skills/game-development/) | 4 |
| [Personal Workflow](skills/personal-workflow/) | 9 |
| [Planning](skills/planning/) | 2 |
| [Programming](skills/programming/) | 1 |
| [Reverse Engineering](skills/reverse-engineering/) | 3 |
| [Review And Resilience](skills/review-and-resilience/) | 2 |
| [Sports](skills/sports/) | 1 |
| [Unreal Engine](skills/unreal-engine/) | 7 |

[Browse all skills by name](CATALOG.md) · [Find your GitHub projects](REPOSITORIES.md) · [Runtime setup](SETUP.md)

## Tool bundles

- [agent-skills](collections/agent-skills/) — 26 skill files, with original routing, plugin files, and shared resources.
- [reverse-skill](collections/reverse-skill/) — 89 skill files, with original routing, plugin files, and shared resources.

These collections preserve layouts required by their tools. Individual skills under `skills/` are the convenient Codex packages; the collection entries overlap with some of those packages.

[Three reverse-skill references](collections/reverse-skill/MISSING-REFERENCES.md) flagged by Windows Defender are retained as source links.

## Install or restore

The category folders organize GitHub browsing. A Codex skill still lives at `$CODEX_HOME/skills/<name>` (normally `~/.codex/skills/<name>`), with all files inside its package. Use the skill-installer with this repository and the paths in `sources.json`; it refuses to overwrite existing skills. Local snapshots were added to this library without changing your installed copies.

## Sources and updates

Each package has a `SOURCE.md` and a preserved original entrypoint. GitHub sources carry pinned commits; local snapshots carry original SHA256 hashes. The repository has no blanket license: each upstream package retains its own license or lack of one. Keep original repositories for active development and upstream updates; this library is your organized collection. Codex system skills and vendor plugin caches are managed by their providers; the personal engineering plugin is included here.

`next-best-practices` and `managing-timelines` use archived upstream versions. See [SETUP.md](SETUP.md) for runtime requirements and import limitations.
