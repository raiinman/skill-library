---
name: arcads-media-router
description: "Route an explicitly chosen Arcads media generation or editing request to its live MCP tools. Use for Arcads image, video, captioning, voice, translation, and enhancement operations."
metadata:
  upstream: "arcads-ai/skills"
  upstream-name: "media-router"
---

# Arcads Media Router

Use only when Arcads is the chosen provider. Preserve a user-selected provider such as Google Flow, Gemini, or inference.sh. Discover the actual catalog and required parameters; route only to tools that exist and match the task.

Read [Codex runtime guidance](references/codex-runtime.md) for tools, authorization, Windows paths, uploads, jobs, and delivery. Then read [the creative workflow](WORKFLOW.md), loading only the references needed for the current branch. The runtime guidance governs host-specific examples in that workflow.

Creative analysis and planning can proceed without Arcads generation. If rendering is requested, use the chosen provider and report missing access rather than silently switching services.

Sibling names use `$arcads-<upstream-name>` in Codex. Read only a sibling that matches the task; no separate Claude plugin is required.
