---
name: arcads-omniflash-restyle
description: "Restyle talking-head footage with Arcads Omni Flash using a reference edit and script. Use for matching typography, backgrounds, cuts, and overlays while preserving identity and source voice."
metadata:
  upstream: "arcads-ai/skills"
  upstream-name: "omniflash-restyle"
---

# Arcads Omni Flash Restyle

Use the supplied script for spelling and the source transcript for timing. Keep source voice as a separate master and relay it after visual editing when needed. Verify live duration limits before chunking and stitching.

Read [Codex runtime guidance](references/codex-runtime.md) for tools, authorization, Windows paths, uploads, jobs, and delivery. Then read [the creative workflow](WORKFLOW.md), loading only the references needed for the current branch. The runtime guidance governs host-specific examples in that workflow.

Creative analysis and planning can proceed without Arcads generation. If rendering is requested, use the chosen provider and report missing access rather than silently switching services.

Sibling names use `$arcads-<upstream-name>` in Codex. Read only a sibling that matches the task; no separate Claude plugin is required.
