---
name: frontend-motion-wizard
description: Add responsive UI motion, spring animations, and micro-interactions to React or Svelte/SvelteKit frontends. Use when auditing or improving overlays, active indicators, hover and press feedback, mobile breakpoints, or reduced-motion accessibility. Use the project's existing styling system and framework-native motion where appropriate.
metadata:
  source-id: frontend-motion-wizard-v1
  library_source:
    kind: installed-local-snapshot
    original_skill_sha256: 5b0e97cd81a09318cac1e1a3aee7d44f874100acd2730e5addc12cc17bf55e8c
---

# Frontend Motion Wizard

Improve interaction feedback and responsive motion while preserving the project's visual identity, semantics, and behavior. Apply changes only when requested; explanation or audit requests do not authorize implementation.

## Framework routing

- Inspect the installed framework version, existing animation dependencies, and styling conventions before choosing APIs. Keep Tailwind where present; ordinary CSS and component styles are equally supported.
- For React, use the installed Framer Motion/Motion integration. For Svelte/SvelteKit, prefer native transitions, animation directives, and `svelte/motion`; preserve existing Svelte syntax and reactivity conventions. Keep the project on its current framework.
- Fetch current documentation through Context7 before using version-sensitive APIs. Resolve the library first, then query the particular motion concept. If unavailable, consult official documentation and report the limitation.

## Shared motion contracts

- Preserve semantic elements, event handlers, state bindings, forms, focus management, tracking, and keyboard behavior. Motion must not delay actions or change application rules.
- Prefer opacity and transforms. Avoid repeatedly animating width, height, margin, or padding; use a supported layout animation when geometry changes need interpolation.
- Keep movement inside the viewport at mobile widths. Scale or remove offsets at narrow breakpoints and test interrupted transitions and rapid repeated input.
- Compose with existing transforms, especially positioning and dragging. Use a separate wrapper when necessary so motion does not overwrite them.
- Prefer tight springs for direct manipulation; short eased native transitions are appropriate for entry/exit and simple feedback. Tune to the framework's parameter model.
- Respect reduced motion in both CSS and JavaScript. Snap springs to their targets and disable spatial transitions when reduced motion is requested; a CSS media rule alone does not stop JavaScript animation. Essential state changes must remain visible.
- Apply hover feedback only on hover-capable pointers. Keep press feedback subtle (a scale near 0.97 is a starting point), preserve focus rings, and restore the resting state on cancellation, blur, or disabled controls.

## React implementation

- Use `AnimatePresence` for conditional entry/exit with stable keys. Choose sequencing based on whether simultaneous exit/entry or waiting suits the interaction.
- Use `layoutId` for shared active indicators and the installed library's layout facilities for supported geometry changes. Check flex/grid axis changes at breakpoints for distortion.
- Use `whileHover` and `whileTap` for feedback while preserving existing handlers. A spring with stiffness 400 and damping 30 is a starting point, not a universal requirement.
- In React Server Component applications, keep motion in interactive client components; preserve server-rendered boundaries and data access.

## Svelte and SvelteKit implementation

- Use `transition:`, or separate `in:` and `out:` directives from `svelte/transition`, on elements inside conditional blocks. `fade` and `fly` provide native opacity/transform transitions. Prefer reversible transitions for frequently toggled controls; use separate entry/exit behavior when intentional.
- Transitions are local by default. Use `|global` only when transitions should also run as an ancestor block is created or destroyed. Account for outgoing nodes remaining mounted until transitions complete: closed overlays must not retain focus or interactive access.
- Use `animate:flip` from `svelte/animate` for reordered lists, on the sole immediate element child of a keyed `{#each}` block with stable keys. It handles reordering, not entry/exit or a generic shared tab highlight. For active indicators, animate a persistent indicator's transform; use documented `crossfade` pairs when elements actually move between keyed locations.
- For Svelte 5 versions that expose them, use `Spring` and `prefersReducedMotion` from `svelte/motion`. Render `spring.current`, update `spring.target`, and use `spring.set(value, { instant: true })` to snap when reduced motion applies. Svelte stiffness and damping use a 0-1 scale; a starting profile is stiffness 0.2 and damping 0.8. React's 400/30 values cannot be transferred directly.
- On older Svelte versions, use supported store-based motion APIs and a browser media-query listener with cleanup. Avoid unrelated migrations to runes or newer APIs.
- For native transitions, set duration to zero when reduced motion applies. Handle preference changes during active animation, including snapping an existing spring and cancelling or finishing in-flight transitions where necessary.
- Keep DOM measurement, `window`, and media-query listeners in browser lifecycle code (`onMount`, actions, or supported client effects), with cleanup. Preserve deterministic SSR output and hydration; SvelteKit does not use React's `"use client"` directive.
- Preserve the existing event syntax (`onclick` in modern Svelte or legacy `on:click` where used), bindings, and state ownership. Implement hover/press feedback with native events or scoped CSS rather than React motion props.

## Verification

- Run the project's relevant existing typecheck/build checks after implementation.
- Inspect changed interactions in a real browser at desktop and mobile widths, with keyboard navigation and reduced motion. Verify rapid open/close, focus return, pointer cancellation, disabled states, viewport clipping, and console errors.
- Report the changed behavior and any unverified browser or accessibility checks. Keep gameplay surfaces steady unless their motion is explicitly requested.
