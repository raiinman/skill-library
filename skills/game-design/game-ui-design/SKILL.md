---
name: game-ui-design
description: "Design and review game HUDs, menus, inventory, minimaps, reticles, and input prompts. Use for readable game interfaces, controller focus, safe zones, and accessible cross-platform game UI."
license: Apache-2.0
---

# Game UI design

Make the player's current choices and critical state readable at gameplay speed. Choose HUD elements by their job, frequency, and consequence, keeping the game world visible. Match the game's visual language and the target hardware rather than imposing one menu style.

## Workflow

1. Read the genre, target platforms, engine, input methods, and existing HUD/menu structure. Reuse the current UI framework. For creation consult [patterns](references/patterns.md); for a failure consult [sharp edges](references/sharp_edges.md); for review consult [validations](references/validations.md).
2. Prioritize information by urgency. Keep health, threats, interaction prompts, cooldowns, and navigation legible against real scenes and at target viewing distances. Group related state; reserve motion and sound for meaningful feedback.
3. Implement navigation for the actual controls: predictable controller focus and back behavior, visible keyboard focus, useful pointer targets, and touch interaction when targeted. Use platform/device-aware button glyphs and remapping rather than hardcoded prompts.
4. Handle safe areas, overscan where relevant, aspect ratios, UI scaling, localization, and accessibility preferences. Preserve explicit user requirements and platform rules when a historical reference suggests a different design.
5. Validate in the target game context: busy backgrounds, intense action, small displays, couch-distance text, menu transitions, and each supported input. Report checks that require hardware or editor access you do not have.

The reference regexes and thresholds are review clues, not proof of a defect. Inspect actual units, layout context, and engine behavior before reporting a finding; a universal CSS font-size or safe-zone number cannot establish every platform's requirements. Do not claim AAA shipping experience or real-device validation from following a document.
