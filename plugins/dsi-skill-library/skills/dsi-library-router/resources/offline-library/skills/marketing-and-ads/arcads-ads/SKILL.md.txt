---
name: arcads-ads
description: "Plan and create Arcads ad creatives from a marketing goal, brand research, and product facts. Use for Arcads campaigns, UGC ads, hook variants, and ad localization."
metadata:
  upstream: "arcads-ai/skills"
  upstream-name: "ads"
---

# Arcads Ads

Ground ad claims in the actual product and sources. Offer a format tied to the marketing goal. Treat post-production and extra variants as scoped work, not automatic additions.

Read [Codex runtime guidance](references/codex-runtime.md) for tools, authorization, Windows paths, uploads, jobs, and delivery. Then read [the creative workflow](WORKFLOW.md), loading only the references needed for the current branch. The runtime guidance governs host-specific examples in that workflow.

Creative analysis and planning can proceed without Arcads generation. If rendering is requested, use the chosen provider and report missing access rather than silently switching services.

Sibling names use `$arcads-<upstream-name>` in Codex. Read only a sibling that matches the task; no separate Claude plugin is required.
