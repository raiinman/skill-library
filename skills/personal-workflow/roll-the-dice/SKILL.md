---
name: roll-the-dice
description: Break a delegated decision deadlock by randomly choosing a viable path and carrying it through to completion. Use when the user invokes Roll the dice, asks for a coin flip between acceptable options, or explicitly delegates a choice to chance. Follow existing decisions normally unless the user asks to reopen them.
license: MIT
---

# Roll the Dice

Choose by chance. Follow through with judgment.

This skill combines the user's definition of Flipism with the commitment theme of Charles Bukowski's poem. See [SOURCE.md](SOURCE.md) for the inspirations. Its chosen behavior is: **pick a viable path, then complete the work.**

## Find the real choice

Read the task, constraints, existing decisions, and relevant work. Identify the decision the user has delegated. Use their supplied options when present; otherwise form a short list of genuinely different ways to accomplish the requested outcome.

Every candidate must fit the requirements, available resources, and authorized scope. Explain material tradeoffs briefly. Randomness settles a choice between acceptable paths; it does not determine facts, erase requirements, or create permission for additional actions.

If only one path is viable, say so and take it. If none is viable, explain the blocker and continue useful work that is possible. Ask only for missing information that would change what can be done.

## Make a real draw

Fix the candidate list and its order before drawing. Give each option equal probability unless the user explicitly requests a different method; the bundled helper supports equal probability only.

Run the standard-library helper from this skill's folder:

```text
python -X utf8 scripts/roll.py "Option A" "Option B" "Option C"
```

Use the full script path when the working directory is elsewhere. Pass labels as data with appropriate shell quoting; use `--` before labels that begin with a hyphen. For two options, this is a coin flip; for more, it is a uniform draw over the numbered options.

The helper reports the options, one-based draw, and selected label. State the real result in one short line and name the next action. If no randomizer can be run, explain that limitation rather than inventing a roll. Do not redraw merely because you prefer another outcome.

## Carry it through

Proceed with the selected path through the normal implementation or creative workflow. Finish its callers, supporting work, meaningful checks, and repairs needed for the requested outcome. Do not stop at a recommendation when execution is authorized, or keep switching approaches to avoid the difficult part.

Use ordinary judgment for subsequent implementation details. Draw again only for a distinct choice the user has delegated to chance. Revisit the chosen path when new evidence makes it unsuitable, the user changes direction, or a real constraint blocks it; explain the reason before choosing again. Keep valid progress when changing course.

Required approvals and user requests to pause or stop remain in effect. Prepare any approval-dependent action so the user can review the concrete result; a draw is not approval.

End with what was chosen, what was completed, and any material limit or unresolved work. Commitment means completing the requested outcome honestly, not promising persistence without a stopping condition.
