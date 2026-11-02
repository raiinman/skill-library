---
name: paper-shaders
description: Add Paper Design canvas shaders to React or vanilla web apps, with correct
  package choice, sizing, lifecycle and performance checks.
license: MIT
---

# Paper Shaders

Choose `@paper-design/shaders-react` for React and `@paper-design/shaders` for vanilla JavaScript or TypeScript. Pin a compatible package version; upstream warns of breaking changes during 0.0.x versioning. Read the corresponding packaged README before copying a shader example.

Give the shader an explicit size or a parent with a measurable size. In server-rendered apps isolate browser and WebGL work behind the appropriate client boundary. Use the actual selected shader's props and uniforms, not another shader's example. Keep a static fallback when WebGL fails and preserve readable foreground content.

For a manually created ShaderMount, inspect the versioned lifecycle API and release it on teardown. Limit simultaneous canvases, pixel density and offscreen animation. Provide a reduced-motion or static state, inspect low-power/mobile rendering, and check both initial render and navigation teardown.

Read [source and licensing](SOURCE.md) and [source map](references/source-map.md) before choosing code or commands. This guide is shared across Codex, Claude and DSI Skills. Install component dependencies only into the actual target project; installing this guide does not initialize or change a project. Use current official docs when integrating, then validate the actual target route.
