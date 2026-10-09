---
name: build
description: Provides the build command adapter. Use when the user invokes build, build auto, or build all to execute a pending task or an authorized plan.
---

# Build

## Overview

Expose the inherited `/build` modes as a discoverable skill. This adapter selects execution scope and delegates implementation to the existing workflows.

## When to Use

Use for an explicit build invocation in a project with work to implement. Ordinary implementation requests can use `incremental-implementation` directly; requests to diagnose compiler or build-system errors belong to `debugging-and-error-recovery`.

## Modes

- `@build` in Codex desktop or `$build` in Codex CLI: implement the next pending task, verify it, commit it, then stop.
- `@build auto` or `$build auto`: execute the authorized plan in dependency order, continuing after each verified task and commit. `all` is an alias for `auto`.

Read the mode from the user's invocation text; skills receive the message rather than an expanded `$ARGUMENTS` placeholder. Select whole-plan mode only when `auto`, `all`, or an explicit request to complete the plan is supplied. Preserve any narrower scope or review checkpoint the user specifies.

## Process

1. Inspect the current request, prior authorization, repository state, and existing spec or task plan. Reuse settled requirements and pending tasks. Small, clear work can proceed directly; substantial work with unresolved requirements uses [spec-driven-development](../spec-driven-development/SKILL.md), then [planning-and-task-breakdown](../planning-and-task-breakdown/SKILL.md) when a dependency-ordered plan is needed. A plan-only request ends at that deliverable.
2. Load and follow [incremental-implementation](../incremental-implementation/SKILL.md) for the selected tasks. Apply [test-driven-development](../test-driven-development/SKILL.md) to executable behavior changes; validate static edits with relevant content or configuration checks and repository-required checks. Use [git-workflow-and-versioning](../git-workflow-and-versioning/SKILL.md) for scoped commits that preserve unrelated changes.
3. Load conditional workflows when their branch applies: [frontend-ui-engineering](../frontend-ui-engineering/SKILL.md) for UI rendering or interaction, [browser-testing-with-devtools](../browser-testing-with-devtools/SKILL.md) when the required browser capability is available, and [security-and-hardening](../security-and-hardening/SKILL.md) for authentication, authorization, or untrusted-input boundaries. Resolve verification failures with [debugging-and-error-recovery](../debugging-and-error-recovery/SKILL.md).
4. After verification, update the task's completion status and commit that task's changes together. In single-task mode, stop after the selected task. In whole-plan mode, continue until every authorized task is complete or a consequential unresolved decision blocks dependent work. Carry prior authorization forward; `auto` changes continuation, not permission. After the user resolves a blocker, resume the same run without requiring another invocation.
5. Report completed tasks, verification, commits, and any remaining decisions or unverified behavior.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "Auto means every action is approved." | Execute within the user's established scope and authorization. |
| "One commit is enough to finish auto mode." | Continue through the remaining authorized tasks after each verified commit. |
| "The adapter replaces the implementation workflow." | Load the linked workflow and follow its verification and commit discipline. |

## Red Flags

- Running the whole plan after a bare build invocation.
- Stopping after one task in auto mode while authorized tasks remain.
- Marking failed or unverified tasks complete, or committing unrelated changes.

## Verification

- [ ] Execution matched the requested mode, scope, and reserved review checkpoints.
- [ ] Each completed task has relevant verification evidence and a scoped commit.
- [ ] Whole-plan mode completed all authorized tasks or identified the actual blocker.
- [ ] The report distinguishes completed work from pending or unverified work.
