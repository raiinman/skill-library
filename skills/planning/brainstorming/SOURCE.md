# Source

- Upstream: [obra/superpowers brainstorming](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/brainstorming)
- Pinned commit: `bb92a77741419a4ab5f06e711a283343f1ada0c3`
- License: MIT, copyright 2025 Jesse Vincent; included in `LICENSE`.
- Added: 2026-10-11

## Adaptation for Codex

- Focused discovery on brainstorming and materially unclear ideas; clear tasks and existing authorization remain usable directly.
- Preserved intent discovery, one question at a time, the skip option, design playback, optional spikes, design approval, and the builder check.
- Replaced the mandatory `superpowers:writing-plans` handoff with the available planning workflow and the project's document conventions.
- Adapted question placement, process lifetime, browser presentation, and cleanup for Codex on Windows.
- Bundled the builder prompt, visual companion, all five runtime/template files, and the original skill and visual guide. The launcher adds `SUPERPOWERS_DISABLE_TELEMETRY=1`; its original is preserved in `references/upstream-start-server.sh`. Other runtime files and the builder prompt are unchanged.

The skill and companion can be restored from this package without the upstream repository. Node.js, Bash, and any host browser tools are runtime prerequisites, not bundled installations.
