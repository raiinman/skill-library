---
name: cursify
description: Evaluate and integrate a Cursify cursor effect while preserving native
  pointer usability, touch fallback and performance.
license: MIT
---

# Cursify

Select a cursor from the official ui-layouts/cursify repository and inspect its code and per-file terms before reuse. The pinned tree contains no license file, so do not label its components MIT or treat public GitHub visibility as a reuse license. This package is an original integration guide with links only, not a copy of component code. Clarify permission or use an independently authored equivalent before shipping source whose reuse terms remain unclear.

The repository examples use React and may require motion, clsx and tailwind-merge; inspect the chosen component's actual imports. Reuse existing utilities and dependencies. Keep the system pointer as the accessible default, limit decorative cursor effects to fine pointers, and disable or simplify for touch and reduced-motion preferences.

Keep overlays pointer-events:none so links and controls work. Remove pointer listeners and cancel requestAnimationFrame loops on teardown, constrain high-DPI canvas work, and test scroll, focus, text selection and route changes. A cursor effect should not become the only indication of interaction.

Read [source and licensing](SOURCE.md) and [source map](references/source-map.md) before choosing code or commands. This guide is shared across Codex, Claude and DSI Skills. Install component dependencies only into the actual target project; installing this guide does not initialize or change a project. Use current official docs when integrating, then validate the actual target route.
