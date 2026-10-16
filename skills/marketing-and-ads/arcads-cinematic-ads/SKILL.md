---
name: arcads-cinematic-ads
description: "Develop cinematic e-commerce product films with Arcads, including scripts, casting sheets, locations, linked shots, and assembly. Use for story-driven film-look ads."
metadata:
  upstream: "arcads-ai/skills"
  upstream-name: "cinematic-ads"
---

# Arcads Cinematic Ads

Preserve continuity through approved character/location references and sequential clips. Agree on the film scope and review stages before costly multi-clip work; render only within that scope. Reuse context already supplied rather than restarting the intake.

Read [Codex runtime guidance](references/codex-runtime.md) for tools, authorization, Windows paths, uploads, jobs, and delivery. Then read [the creative workflow](WORKFLOW.md), loading only the references needed for the current branch. The runtime guidance governs host-specific examples in that workflow.

Creative analysis and planning can proceed without Arcads generation. If rendering is requested, use the chosen provider and report missing access rather than silently switching services.

Sibling names use `$arcads-<upstream-name>` in Codex. Read only a sibling that matches the task; no separate Claude plugin is required.
