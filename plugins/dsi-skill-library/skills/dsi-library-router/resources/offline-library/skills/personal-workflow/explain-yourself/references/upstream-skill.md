---
name: explain-yourself
description: Show and explain actual agent work when the user asks what you did, cannot understand a progress report, or wants evidence behind claims. Connect concrete changes and results to plain-language explanations.
---

# Explain Yourself

Answer "What did you actually do?" so the user can understand and inspect the work. Show the work behind each material claim. Apply this to any kind of task.

## Inspect before explaining

Use the relevant conversation, tool results, files, diffs, artifacts, and verification records to establish what actually happened. Keep inspection scoped to the work in question. Separate intended actions, attempted actions, completed changes, and verified outcomes. If records are missing, say what cannot be established.

## Show the work

Start with the concrete result and whether it meets the user's request. For each meaningful change or attempt, connect:

- **What you did:** Name the specific thing changed or attempted and explain it in everyday language.
- **Show it:** Include the relevant before/after excerpt, diff, image, artifact preview, or observed tool result. Add a usable reference when available. A file link supports the explanation; it does not replace showing the relevant part in the answer.
- **Why:** Explain what problem that action was intended to solve. Identify retrospective reasoning as inference when the original reason is not recorded.
- **What happened:** State the observed result, its practical effect, and what remains broken or unverified.

Choose evidence suited to the work: a short code diff for a code change, a visible comparison for visual work, a concrete passage for a document edit, or actual output for a command. Translate technical names into what they do. Show enough detail to make the claim inspectable without dumping raw logs or entire files. Keep secrets and unrelated private information out of excerpts.

Explain consequential failed attempts, repeated work, abandoned approaches, and reversals as well as successful changes. If asked where time went, reconstruct only what the records support; timestamps do not establish continuous activity. Mark unexplained gaps explicitly.

Statements such as "I improved it," "I fixed the logic," or "I tested it" require concrete evidence: what changed, which behavior was checked, what was observed, and what that proves. An artifact's existence proves it was created, not that it works.

Finish with a clear account of what exists now and what the user can actually use. Keep the response centered on explaining the completed and attempted work. Add future plans or perform repairs only when the user requests them. When evidence is unavailable, state the limitation instead of inventing work, reasons, or results.
