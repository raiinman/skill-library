---
name: arcads-clone-static-ad
description: "Adapt a reference static ad to the user's brand with Arcads, preserving visual hierarchy while replacing product imagery and copy. Use for static ad recreation."
metadata:
  upstream: "arcads-ai/skills"
  upstream-name: "clone-static-ad"
---

# Arcads Clone Static Ad

Preserve the reference composition and hierarchy while replacing brand-specific assets and claims. Retain the actual uploaded reference. Scope the number of variants to the user's request and budget.

Read [Codex runtime guidance](references/codex-runtime.md) for tools, authorization, Windows paths, uploads, jobs, and delivery. Then read [the creative workflow](WORKFLOW.md), loading only the references needed for the current branch. The runtime guidance governs host-specific examples in that workflow.

Creative analysis and planning can proceed without Arcads generation. If rendering is requested, use the chosen provider and report missing access rather than silently switching services.

Sibling names use `$arcads-<upstream-name>` in Codex. Read only a sibling that matches the task; no separate Claude plugin is required.
