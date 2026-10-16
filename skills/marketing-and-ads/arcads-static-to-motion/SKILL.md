---
name: arcads-static-to-motion
description: "Turn a finished static ad into a short Arcads video using restrained motion or one creative transformation. Use for animated product statics, offer cards, and paid social clips."
metadata:
  upstream: "arcads-ai/skills"
  upstream-name: "static-to-motion"
---

# Arcads Static to Motion

Fit aspect ratio before animation and preserve the source ad's product, layout, and exact offer text. Define simple motion or one creative transformation according to the brief; do not automatically generate both versions.

Read [Codex runtime guidance](references/codex-runtime.md) for tools, authorization, Windows paths, uploads, jobs, and delivery. Then read [the creative workflow](WORKFLOW.md), loading only the references needed for the current branch. The runtime guidance governs host-specific examples in that workflow.

Creative analysis and planning can proceed without Arcads generation. If rendering is requested, use the chosen provider and report missing access rather than silently switching services.

Sibling names use `$arcads-<upstream-name>` in Codex. Read only a sibling that matches the task; no separate Claude plugin is required.
