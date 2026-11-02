---
name: motion-primitives
description: Integrate Motion Primitives React animation components with the project's
  Motion and Tailwind setup.
license: MIT
---

# Motion Primitives

Choose a specific primitive at https://motion-primitives.com/docs. The official CLI supports `npx motion-primitives add <component-name>`, for example text-morph, and installs component dependencies. Read the pinned CLI README before selecting that route. Check the installed project's Motion version and import conventions, such as motion/react, rather than adding a second incompatible animation runtime.

Preserve the project's Tailwind version, cn helper, tokens and aliases. The repository is beta and source components can change, so record which component revision or CLI version you installed. Use the smallest client boundary needed in SSR frameworks.

Respect reduced motion, keep essential text readable to assistive technology during text transitions, and verify keyboard interaction and layout stability. Unmount and remount the route to catch orphaned animation or observer work. Preserve MIT notices when copying source.

Read [source and licensing](SOURCE.md) and [source map](references/source-map.md) before choosing code or commands. This guide is shared across Codex, Claude and DSI Skills. Install component dependencies only into the actual target project; installing this guide does not initialize or change a project. Use current official docs when integrating, then validate the actual target route.
