---
name: arcads-fpv-drone-path
description: "Write an FPV drone flythrough prompt from a landmark image and a drawn flight path. Use for continuous first-person camera routes and landmark world-tour shots."
metadata:
  upstream: "arcads-ai/skills"
  upstream-name: "fpv-drone-path"
---

# Arcads FPV Drone Path

Use the template as a starting point for the actual supplied image and route. Remove guide marks from the output and specify a continuous physically plausible camera path. Do not insert unrelated landmarks merely because they appear in the example.

Read [Codex runtime guidance](references/codex-runtime.md) for tools, authorization, Windows paths, uploads, jobs, and delivery. Then read [the creative workflow](WORKFLOW.md), loading only the references needed for the current branch. The runtime guidance governs host-specific examples in that workflow.

Prompt and script drafting work without an Arcads account. Use the provider selected by the user for rendering, translating the prompt to its supported controls.

Sibling names use `$arcads-<upstream-name>` in Codex. Read only a sibling that matches the task; no separate Claude plugin is required.
