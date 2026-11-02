---
name: trickle-ui-kit
description: Add Trickle UI Kit CSS text animation components to React while preserving
  SSR behavior, accessibility and reduced motion.
license: MIT
---

# Trickle Ui Kit

Trickle is distributed as copy-in source through a shadcn registry, not an installable trickle npm package. The official example is `npx shadcn@latest add https://tricklekit.dev/r/typewriter.json`. Read the pinned README for the selected component and inspect registry changes before merging them into globals.css. Tailwind v4 is the primary target; check v3 conversion rather than assuming compatibility.

Keep the shared text-root component and required CSS custom properties/keyframes when supplied. Most components are server-renderable CSS effects; only stateful primitives need client state. Do not add Motion or Framer Motion just for these CSS animations.

Provide meaningful stable text to assistive technology, preserve the reduced-motion override, and verify wrapping, initial SSR render, hydration and mobile layout. Avoid repeating animation that blocks reading. Components are MIT; upstream registry examples have a separate CC0 license. Preserve the correct notices.

Read [source and licensing](SOURCE.md) and [source map](references/source-map.md) before choosing code or commands. This guide is shared across Codex, Claude and DSI Skills. Install component dependencies only into the actual target project; installing this guide does not initialize or change a project. Use current official docs when integrating, then validate the actual target route.
