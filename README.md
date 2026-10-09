# Skill Library

Private collection of 27 requested skills, organized by category and packaged for Codex. Original instructions, pinned source commits, supporting files, and upstream licenses travel with each package.

## 3D And Web

- [`$img2threejs`](skills/3d-and-web/img2threejs/SKILL.md) — [source](skills/3d-and-web/img2threejs/SOURCE.md)
- [`$image-to-code`](skills/3d-and-web/image-to-code/SKILL.md) — [source](skills/3d-and-web/image-to-code/SOURCE.md)
- [`$next-best-practices`](skills/3d-and-web/next-best-practices/SKILL.md) — [source](skills/3d-and-web/next-best-practices/SOURCE.md)
- [`$threejs-postprocessing`](skills/3d-and-web/threejs-postprocessing/SKILL.md) — [source](skills/3d-and-web/threejs-postprocessing/SOURCE.md)

## Engineering

- [`$civil-engineer`](skills/engineering/civil-engineer/SKILL.md) — [source](skills/engineering/civil-engineer/SOURCE.md)

## Finance

- [`$okx-cex-portfolio`](skills/finance/okx-cex-portfolio/SKILL.md) — [source](skills/finance/okx-cex-portfolio/SOURCE.md)
- [`$okx-dex-market`](skills/finance/okx-dex-market/SKILL.md) — [source](skills/finance/okx-dex-market/SOURCE.md)

## Game Design

- [`$pixel-art-sprites`](skills/game-design/pixel-art-sprites/SKILL.md) — [source](skills/game-design/pixel-art-sprites/SOURCE.md)
- [`$game-design-core`](skills/game-design/game-design-core/SKILL.md) — [source](skills/game-design/game-design-core/SOURCE.md)
- [`$game-designer`](skills/game-design/game-designer/SKILL.md) — [source](skills/game-design/game-designer/SOURCE.md)
- [`$game-design-document`](skills/game-design/game-design-document/SKILL.md) — [source](skills/game-design/game-design-document/SOURCE.md)
- [`$level-designer`](skills/game-design/level-designer/SKILL.md) — [source](skills/game-design/level-designer/SOURCE.md)

## Game Development

- [`$game-development`](skills/game-development/game-development/SKILL.md) — [source](skills/game-development/game-development/SOURCE.md)
- [`$game-architecture`](skills/game-development/game-architecture/SKILL.md) — [source](skills/game-development/game-architecture/SOURCE.md)
- [`$map-systems`](skills/game-development/map-systems/SKILL.md) — [source](skills/game-development/map-systems/SOURCE.md)
- [`$day-one-patch`](skills/game-development/day-one-patch/SKILL.md) — [source](skills/game-development/day-one-patch/SOURCE.md)

## Planning

- [`$managing-timelines`](skills/planning/managing-timelines/SKILL.md) — [source](skills/planning/managing-timelines/SOURCE.md)

## Programming

- [`$lua`](skills/programming/lua/SKILL.md) — [source](skills/programming/lua/SOURCE.md)

## Review And Resilience

- [`$adversarial-review`](skills/review-and-resilience/adversarial-review/SKILL.md) — [source](skills/review-and-resilience/adversarial-review/SOURCE.md)
- [`$chaos-engineer`](skills/review-and-resilience/chaos-engineer/SKILL.md) — [source](skills/review-and-resilience/chaos-engineer/SOURCE.md)

## Sports

- [`$sports-betting-analyzer`](skills/sports/sports-betting-analyzer/SKILL.md) — [source](skills/sports/sports-betting-analyzer/SOURCE.md)

## Unreal Engine

- [`$unreal-multiplayer-architect`](skills/unreal-engine/unreal-multiplayer-architect/SKILL.md) — [source](skills/unreal-engine/unreal-multiplayer-architect/SOURCE.md)
- [`$unreal-engine-cpp-pro`](skills/unreal-engine/unreal-engine-cpp-pro/SKILL.md) — [source](skills/unreal-engine/unreal-engine-cpp-pro/SOURCE.md)
- [`$unreal-technical-artist`](skills/unreal-engine/unreal-technical-artist/SKILL.md) — [source](skills/unreal-engine/unreal-technical-artist/SOURCE.md)
- [`$unreal-systems-engineer`](skills/unreal-engine/unreal-systems-engineer/SKILL.md) — [source](skills/unreal-engine/unreal-systems-engineer/SOURCE.md)
- [`$unreal-world-builder`](skills/unreal-engine/unreal-world-builder/SKILL.md) — [source](skills/unreal-engine/unreal-world-builder/SOURCE.md)
- [`$unreal-engine`](skills/unreal-engine/unreal-engine/SKILL.md) — [source](skills/unreal-engine/unreal-engine/SOURCE.md)

## Install in Codex

Each category folder is for GitHub browsing. Install the individual package folders into `$CODEX_HOME/skills/<name>` (normally `~/.codex/skills/<name>`), retaining every file inside them. Use Codex's skill-installer with this repository and the paths in `sources.json`; it refuses to overwrite existing skills. The `agents/openai.yaml` files supply readable picker names.

See [SETUP.md](SETUP.md) for runtime prerequisites and import limitations. This repository has no blanket license: each upstream package retains its own license or lack of one.

`next-best-practices` and `managing-timelines` use archived versions because their exact requested skills were removed upstream. Agent profiles were packaged as skills; Claude-specific workflows include Codex compatibility notes.
