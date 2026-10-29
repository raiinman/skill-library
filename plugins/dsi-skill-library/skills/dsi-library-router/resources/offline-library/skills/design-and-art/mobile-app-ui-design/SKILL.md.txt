---
name: mobile-app-ui-design
description: "Design and improve mobile app screens, navigation, onboarding, and interactive prototypes. Use for mobile UI/UX work, including React Native, Flutter, SwiftUI, and mobile web interfaces."
license: MIT
---

# Mobile app UI design

Start with the user's task, primary action, platform, and current design system. Design the screen in its flow, including back navigation, entry/exit states, and what the next action does. Preserve the chosen native or web framework; an HTML mockup is not a finished native app.

## Design and implement

- Establish a clear hierarchy and a small type/color/spacing system. Prefer the existing brand tokens. The upstream 60/30/10 split, type-size limits, F-pattern, thumb-zone placement, and 4/8-point grid are starting heuristics, not rules that override content, accessibility, or platform conventions.
- Group related elements, keep primary actions reachable without obstructing content, and account for safe areas, the software keyboard, orientation, text expansion, and long/localized strings. Avoid importing desktop-sized section padding into every phone screen.
- Use consistent imagery, tinted depth where useful, and restrained motion tied to actions. Keep labels and exact values readable. Contrast must hold on the actual surface; lowering text opacity is not an accessibility guarantee.
- Handle loading, empty, error, success, disabled, and offline states as needed by the task. Use real data or clearly labeled placeholders. Show genuine recent searches or recommendations only when the product has them; don't invent user history.
- Review at a small phone width and a wider viewport with enlarged text. Check focus order, screen-reader labels, platform-appropriate touch targets, scroll reachability, contrast, and reduced motion. State which native/device checks remain unperformed.

Read [industry conventions](references/industry-conventions.md) when selecting a domain-specific interaction or visual direction. Read [the detailed design workflow](WORKFLOW.md) for examples and visual recipes. Treat its brand examples and psychology claims as design inspiration, not validated requirements for this user's product.

## Tooling

Use the user's chosen React Native, Flutter, SwiftUI, or web stack. Tailwind, Lucide, and Recharts are optional examples for compatible web projects, not universal dependencies. Check current library/platform documentation before API-specific implementation. Use available visual tools for requested mockups and screenshots; preserve editable implementation when code was requested.
