---
name: ui-layouts
description: Select and integrate UI Layouts components and interactive layouts into
  an existing React and Tailwind project.
license: MIT
---

# Ui Layouts

Find the exact component at https://www.ui-layouts.com/components and inspect its source and dependencies. The repository is a component and examples collection, not one npm package that installs all UI. Its examples use React, Tailwind, Motion and shared class-name helpers; individual components can additionally require Embla, Three.js or other libraries.

Match the project's Tailwind version, import aliases and existing cn utility. Install only the chosen component's required dependencies. Copy the complete component and its utility/style requirements, preserve its license, and integrate with existing tokens. Do not copy the demo application around it.

Check keyboard interaction, focus, responsive layout and reduced motion. Remove event listeners and animation resources on unmount. Check the target route in the actual application, including client/server boundaries and navigation, rather than treating a compiling snippet as acceptance.

Read [source and licensing](SOURCE.md) and [source map](references/source-map.md) before choosing code or commands. This guide is shared across Codex, Claude and DSI Skills. Install component dependencies only into the actual target project; installing this guide does not initialize or change a project. Use current official docs when integrating, then validate the actual target route.
