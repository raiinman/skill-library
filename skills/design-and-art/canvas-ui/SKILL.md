---
name: canvas-ui
description: Integrate Canvas UI interactive GPU effects into a real interface, choosing
  framework, renderer and browser fallback deliberately.
license: MIT
---

# Canvas Ui

Canvas UI uses a source registry rather than a universal runtime package. Select the existing framework and WebGL or WebGPU build before choosing the effect. The current registry example is `npx shadcn@latest add @canvas-ui/liquid-react`; the WebGPU variant adds `-webgpu`. Resolve current registry configuration from https://canvasui.dev/docs/installation before executing it.

Keep interactive DOM content functional. HTML-in-canvas is experimental and may need an origin trial or developer flag; test an ordinary browser without flags and verify the overlay or unchanged-content fallback. Do not turn on browser flags globally. Feature-detect GPU support, preserve keyboard focus and reduced motion, and check touch devices. Dispose GPU resources when the component unmounts.

The upstream MIT plus Commons Clause terms allow use within products but restrict redistribution of the components themselves. This guide contains no component source, templates, original manual or model assets. Retrieve components from the official registry for a specific target project; retain its notices and check any separately licensed model assets.

Read [source and licensing](SOURCE.md) and [source map](references/source-map.md) before choosing code or commands. This guide is shared across Codex, Claude and DSI Skills. Install component dependencies only into the actual target project; installing this guide does not initialize or change a project. Use current official docs when integrating, then validate the actual target route.
