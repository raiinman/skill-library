---
name: arcads-clone-hook
description: "Analyze a reference video ad opening and adapt its hook to the user's product through Arcads. Use for hook breakdowns, brand swaps, and rebuilt opening sequences."
metadata:
  upstream: "arcads-ai/skills"
  upstream-name: "clone-hook"
---

# Arcads Clone Hook

Analyze the opening from real footage and record its hook boundary, beat timing, and reproduction details. Keep supplied brand assets accurate. Separate the requested analysis from an optional paid recreation.

Read [Codex runtime guidance](references/codex-runtime.md) for tools, authorization, Windows paths, uploads, jobs, and delivery. Then read [the creative workflow](WORKFLOW.md), loading only the references needed for the current branch. The runtime guidance governs host-specific examples in that workflow.

Creative analysis and planning can proceed without Arcads generation. If rendering is requested, use the chosen provider and report missing access rather than silently switching services.

Sibling names use `$arcads-<upstream-name>` in Codex. Read only a sibling that matches the task; no separate Claude plugin is required.
