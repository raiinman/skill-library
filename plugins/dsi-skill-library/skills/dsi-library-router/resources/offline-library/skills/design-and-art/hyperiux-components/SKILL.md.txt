---
name: hyperiux-components
description: Integrate Hyperiux Vault effects through its CLI or source catalogue,
  respecting account access and per-effect licenses.
license: MIT
---

# Hyperiux Components

The supplied legacy URL is gone; the verified current project is Hyperiux-Immersion-Labs/hyperiux-components. Choose one effect from https://vault.hyperiux.com/ai-components and inspect its dependency list and free/Pro status. CLI workflow is `npx hyperiux init`, `npx hyperiux login`, then `npx hyperiux add <effect>`. The pinned README requires an account for installs, including free effects; verify access with whoami instead of assuming the CLI being installed means authentication. Do not purchase Pro or bypass its controls.

Preview an add with `--dry-run` where supported; avoid overwrite unless replacing the intended file. Preserve aliases, tokens and existing components. Verify keyboard/touch usability, reduced motion, client boundaries, GSAP/Three.js cleanup when used, and responsive performance.

Licenses differ: the CLI and MCP server are MIT; the free registry effects are MPL-2.0 under LICENSE_EFFECTS; Pro effects have separate proprietary terms. The current license file takes precedence over README marketing that calls everything MIT. Keep per-file notices and applicable source-distribution obligations. This guide does not bundle paid effects.

Read [source and licensing](SOURCE.md) and [source map](references/source-map.md) before choosing code or commands. This guide is shared across Codex, Claude and DSI Skills. Install component dependencies only into the actual target project; installing this guide does not initialize or change a project. Use current official docs when integrating, then validate the actual target route.
