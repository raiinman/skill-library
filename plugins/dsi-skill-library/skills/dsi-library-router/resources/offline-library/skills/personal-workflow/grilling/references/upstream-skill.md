---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round using the question form below. Then wait for the user's answers before the next round.

## Question form and waiting

- Present every interview round with `functions.request_user_input_async`, using its `questions` array. Number each question in its `title` and include enough context to answer. For choices, put your recommended answer first and label it "(Recommended)"; omit `options` when a free-text answer is needed. A preselected option becomes an answer only when the user submits it.
- If the asynchronous form is unavailable, use `functions.request_user_input` when it is available and permitted in the current mode. If neither form is available, explain the limitation and ask in chat.
- After opening an asynchronous form, wait with `clock.sleep` using `duration_ms: 30000`. Continue waiting in 30-second intervals until the user answers, explicitly skips the question, or stops the interview. User input may interrupt a wait early; process it immediately.
- A timeout or an empty tool response is not an answer. Keep the question pending across wait intervals. Do not end the turn, dismiss or replace the form, choose an answer, or advance the interview merely because 30 seconds elapsed. If a blocking form returns without answers, keep the question pending and use the same waiting cadence.

## Continue the interview

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent to find it; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.
