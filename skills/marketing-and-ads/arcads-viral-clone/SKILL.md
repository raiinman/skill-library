---
name: arcads-viral-clone
description: "Adapt a reference viral video ad to the user's product with Arcads and FFmpeg, preserving shots and pacing while checking product identity, timing, and source audio."
metadata:
  upstream: "arcads-ai/skills"
  upstream-name: "viral-clone"
---

# Arcads Viral Ad Adaptation

Measure the real reference before generating. Keep per-shot timing and product checks, preserve authorized source audio, and inspect identity and label continuity. Choose edit or per-shot reconstruction from actual tool capability rather than a hardcoded historical limit.

Read [Codex runtime guidance](references/codex-runtime.md) for tools, authorization, Windows paths, uploads, jobs, and delivery. Then read [the creative workflow](WORKFLOW.md), loading only the references needed for the current branch. The runtime guidance governs host-specific examples in that workflow.

Creative analysis and planning can proceed without Arcads generation. If rendering is requested, use the chosen provider and report missing access rather than silently switching services.

Sibling names use `$arcads-<upstream-name>` in Codex. Read only a sibling that matches the task; no separate Claude plugin is required.
