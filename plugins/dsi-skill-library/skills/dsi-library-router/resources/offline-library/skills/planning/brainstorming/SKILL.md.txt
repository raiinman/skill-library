---
name: brainstorming
description: Turn an unclear idea into a concrete design through a focused conversation, with ADHD-friendly idea capture and optional mind maps. Use when the user asks to brainstorm, explore an idea, compare directions, or clarify a project before building. Clear tasks and already-approved plans can proceed directly.
license: MIT
---

# Brainstorming

Find out what the user wants and why, then produce a description a capable builder can act on. Adapted from Jesse Vincent's Superpowers brainstorming skill; provenance and changes are in [SOURCE.md](SOURCE.md).

## Decide whether a conversation is needed

Read the request and relevant existing work. If the important decisions are already clear, complete the task through the normal workflow. Keep existing authorization and preferences in effect.

When an idea needs exploration, briefly say the user can skip the questions and have you start. If they choose that, state significant assumptions or choices plainly and proceed; brainstorming is finished.

Otherwise, start from what the user has already given you. Capture an existing brain dump before asking for more. When a question will help, ask one grounded in a real situation: what prompted the idea, who needs it, or what success would look like. Use the host's question interface when appropriate; questions belong there or in the final response, not in progress commentary.

## Capture first, then shape

Use these defaults to reduce the work the user must hold in their head. They do not require an ADHD diagnosis or disclosure.

- Accept fragments, tangents, pasted notes, and available voice transcripts in whatever order they arrive. Preserve meaningful details and conflicting ideas before organizing them; mark uncertain wording for clarification.
- During idea generation, capture possibilities without ranking or dismissing them. In the later shaping phase, check feasibility, constraints, and tradeoffs. Keep unrealistic ideas available as prompts for alternatives, while distinguishing them from an actionable plan.
- Maintain one working note in the current conversation or an existing project document. Show the active topic, decisions, unresolved questions, and ideas parked for later when a checkpoint would help. A tangent may change the goal; infer clear steering and clarify only genuine ambiguity.
- Keep responses brief and ask at most one needed question at a time. When the user seems overloaded or asks where to start, reduce the current demand to one small, concrete action. Reuse captured context after a pause instead of restarting the interview.
- Read [ADHD-friendly facilitation](references/adhd-facilitation.md) when nonlinear capture, mind mapping, optional timeboxes, group brainstorming, or restarting after a pause would help. Offer the relevant technique; keep the user's established preferences and option to skip questions in effect.

## Discover the intent

- Ask one question at a time, building on the last answer. Let the user describe the situation before narrowing the choices; offer a short menu when they are stuck.
- Explore the purpose, audience, current state, constraints, goals, non-goals, and outcomes they want to avoid. Treat these as topics to cover when relevant, rather than a questionnaire to recite.
- Find out which platform, medium, tool, and resource decisions they care about and which they delegate. Build on the project's existing choices. Label your own assumptions and recommendations accurately.
- Inspect relevant code, files, or public sources within the authorized task scope. Explain what the inspection resolved. Ask only when access or an action requires additional authorization.
- When ready to shape the ideas, compare the few meaningful directions and recommend the simplest one that meets the need. Avoid asking the user to rank a whole brain dump; preserve the remaining ideas for later.
- Reflect each understood part back briefly and invite correction. Keep the length proportional to the decision; distinguish what they said from your interpretation.

Chat during work is steering. Incorporate it and continue independent work; pause only actions that depend on an unanswered decision or conflict with the new input.

## Use a sketch or spike when it helps

Use a diagram, comparison, or mockup when seeing it would clarify the decision. If the user wants an interactive browser companion, read [visual-companion.md](visual-companion.md); its scripts and templates are included here. A diagram in chat does not require starting that server.

A throwaway prototype can test an uncertain idea cheaply. Agree on its purpose and limits before building it. Report what it taught you; discuss turning it into the deliverable before doing that additional work. Preserve security and data integrity even in a spike.

## Produce the design and hand it over

Match the output to the work:

- A small change needs a concise description in chat.
- A substantial project needs a written design covering intent, success criteria, scope, constraints, key behavior, the user's decisions, your assumptions, and choices left to the builder.
- Follow the project's document conventions. If none exist, use `docs/design/YYYY-MM-DD-<topic>-design.md` for a software repository. Save or commit documents within the user's authorized scope.

For a substantial written design, use [builder-check-prompt.md](builder-check-prompt.md) for one independent review when delegation is permitted and useful; otherwise read it yourself from the builder's perspective. Fill gaps already answered by the conversation or project. Settle minor implementation choices and label them as your calls. Bring only unresolved decisions that materially change the design back to the user, in one focused round.

When the user requested a brainstorming discussion, get their approval of the complete proposed design before beginning implementation. Approval covers what you actually presented. An existing approved design, an explicit request to proceed, or the user's choice to skip brainstorming already supplies that authorization; avoid asking again for it.

After approval, prepare an implementation plan proportional to the work, using the available planning workflow if helpful. End with one concrete next action and a short restart note when the session is paused. Captured ideas are not approved features; bring proposed scope changes back through the applicable authorization boundary. The skill is complete when the direction, remaining assumptions, and next action are clear. It does not require other Superpowers skills.
