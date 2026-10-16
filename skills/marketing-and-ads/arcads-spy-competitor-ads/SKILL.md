---
name: arcads-spy-competitor-ads
description: "Find and download competitor video or image ads from the public Meta Ad Library with a connected browser. Use for competitor creative research and swipe files."
metadata:
  upstream: "arcads-ai/skills"
  upstream-name: "spy-competitor-ads"
---

# Arcads Competitor Ad Research

Use the Codex browser workflow in WORKFLOW.md. The original is archived for provenance; its injected download scripts and forced /tmp moves are not the active workflow.

Read [Codex runtime guidance](references/codex-runtime.md) for tools, authorization, Windows paths, uploads, jobs, and delivery. Then read [the creative workflow](WORKFLOW.md), loading only the references needed for the current branch. The runtime guidance governs host-specific examples in that workflow.

Creative analysis and planning can proceed without Arcads generation. If rendering is requested, use the chosen provider and report missing access rather than silently switching services.

Sibling names use `$arcads-<upstream-name>` in Codex. Read only a sibling that matches the task; no separate Claude plugin is required.
