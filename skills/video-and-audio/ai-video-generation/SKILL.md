---
name: ai-video-generation
description: Generate or transform videos through inference.sh using its belt CLI, including text-to-video, image animation, reference-based clips, lipsync, and upscaling. Use when the user requests AI video generation or names an inference.sh video model.
---

# AI video generation with inference.sh

Use the real `belt` CLI (`infsh` and `inferencesh` are aliases). No Claude Bash tool allowlist or additional skill installation is required. The model catalog and examples in [the pinned upstream guide](references/upstream-skill.md) are discovery starting points; availability, schemas, and prices must be checked at use time.

## Prepare the request

- Identify the intended clip, supplied references, delivery format, and authorized spend. Choose a model that supports that operation. Prefer existing user assets and keep their reference roles explicit.
- Run `belt --version` and `belt auth status --no-input`. If authentication is missing, tell the user to run `belt login` in a terminal, or configure `INFSH_API_KEY` through their secret-management path. Keep credentials out of chat, committed files, and command output. See [CLI setup](references/cli-setup.md) if the executable is missing.
- Discover with `belt app list --category video --json` or `belt app search --help`. Inspect the selected app with `belt app get namespace/name --json`, and read its actual input/output schema. Account access and model availability can differ. Verify supported assets, duration, resolution, audio, and aspect ratio rather than copying another model's fields.
- Upload local media only through a supported provider route authorized by the task; a local path or an `@filename` in prompt prose does not upload it. Check the CLI's current file/upload help for that route. If an attachment type is unsupported, disclose the limit and adapt the shot or provider within scope.

## Submit and finish

Write a UTF-8 JSON input file matching the selected app schema. This avoids PowerShell's inline-JSON quoting pitfalls. For example, a schema that accepts `prompt` could use `{"prompt":"A slow aerial shot over a misty pine forest"}`. Check cost using the same final input before submission:

```sh
belt app run namespace/name --input input.json --estimate --json --no-input
```

When generation and the expected cost are authorized, submit one task and save its receipt:

```sh
belt app run namespace/name --input input.json --no-wait --save receipt.json --json --no-input
```

Replace `namespace/name` with the verified app ID, optionally pinned to its chosen version. Use the returned task ID to monitor with `belt task get TASK_ID --json --no-input` (see `--help` for follow mode). Avoid repeated submissions: after an ambiguous timeout, inspect the receipt and existing task before considering a retry. A failed job is not permission for an unbounded paid retry loop.

On completion, retrieve the actual output using the returned file links and documented download support. Probe the downloaded video, inspect representative frames, and check audio when possible. Report the deliverable and any material mismatch or review limit. Authentication, an accepted request, and a completed, reviewed video are separate states; never claim generation from a prompt draft or queued task.

For Seedance prompt construction, the installed `seedance-2-0-prompter` can help if available. It is optional; its provider-neutral prompt must still be mapped to this app's current schema.
