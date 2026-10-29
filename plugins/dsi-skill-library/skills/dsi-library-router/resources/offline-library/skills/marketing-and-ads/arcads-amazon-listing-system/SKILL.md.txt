---
name: arcads-amazon-listing-system
description: "Plan and generate Amazon listing image sets from a product URL and photo using Arcads. Use for product benefits, features, lifestyle, and genuine review graphics."
metadata:
  upstream: "arcads-ai/skills"
  upstream-name: "amazon-listing-system"
---

# Arcads Amazon Listing System

Use genuine product facts and reviews. Verify current Amazon image requirements before producing a listing-ready set. In particular, the main product hero must follow main-image rules; place promotional headlines and claim graphics in secondary images rather than copying the upstream headline-on-hero example. Never invent customer reviews.

Read [Codex runtime guidance](references/codex-runtime.md) for tools, authorization, Windows paths, uploads, jobs, and delivery. Then read [the creative workflow](WORKFLOW.md), loading only the references needed for the current branch. The runtime guidance governs host-specific examples in that workflow.

Creative analysis and planning can proceed without Arcads generation. If rendering is requested, use the chosen provider and report missing access rather than silently switching services.

Sibling names use `$arcads-<upstream-name>` in Codex. Read only a sibling that matches the task; no separate Claude plugin is required.
