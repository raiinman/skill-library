---
name: ponytail-full
description: Use Ponytail full mode when the user selects $ponytail-full or requests Ponytail full.
license: MIT
metadata:
  library_source:
    kind: installed-local-snapshot
    original_skill_sha256: bcb941c2494e4bac70f07adf2ce5f8f7afbf4c6420ac3321c6178c70db9ea1dc
---

# Ponytail Full

Read the shared Ponytail instructions before doing the task:

- Installed alongside the main skill: [../ponytail/SKILL.md](../ponytail/SKILL.md).

Use the first available location. After reading, set the active Ponytail level to `full`, overriding the initial full default.

Apply the smallest complete change rules.

Keep this level active for the session until the user switches levels or says "stop ponytail" or "normal mode". Honor a later explicit level choice.
