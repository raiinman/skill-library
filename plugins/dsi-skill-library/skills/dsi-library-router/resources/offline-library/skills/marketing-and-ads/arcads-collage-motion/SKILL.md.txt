---
name: arcads-collage-motion
description: "Decode halftone and paper-collage references into editable visual specs, then generate and animate on-brand creatives with Arcads. Use for collage assemble-in motion."
metadata:
  upstream: "arcads-ai/skills"
  upstream-name: "collage-motion"
---

# Arcads Collage Motion

Read references/collage-dimensions.md when decoding a look. Keep an editable spec for halftone, cut edges, layers, paper grain, palette, and typography. An assemble-from-empty motion prompt must define reveal order and a readable final hold.

Read [Codex runtime guidance](references/codex-runtime.md) for tools, authorization, Windows paths, uploads, jobs, and delivery. Then read [the creative workflow](WORKFLOW.md), loading only the references needed for the current branch. The runtime guidance governs host-specific examples in that workflow.

Creative analysis and planning can proceed without Arcads generation. If rendering is requested, use the chosen provider and report missing access rather than silently switching services.

Sibling names use `$arcads-<upstream-name>` in Codex. Read only a sibling that matches the task; no separate Claude plugin is required.
