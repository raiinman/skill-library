---
name: ponytail-lite
description: Use Ponytail lite mode when the user selects $ponytail-lite or requests Ponytail lite.
license: MIT
metadata:
  library_source:
    kind: installed-local-snapshot
    original_skill_sha256: d0e0c0c2be2d85f8a9b96a7e07a002ccab8c2faed11e1a3ad534caf3f8e1db70
---

# Ponytail Lite

Read the shared Ponytail instructions before doing the task:

- Installed alongside the main skill: [../ponytail/SKILL.md](../ponytail/SKILL.md).

Use the first available location. After reading, set the active Ponytail level to `lite`, overriding the initial full default.

Build what was asked. Name the smaller option in one line and let the user pick.

Keep this level active for the session until the user switches levels or says "stop ponytail" or "normal mode". Honor a later explicit level choice.
