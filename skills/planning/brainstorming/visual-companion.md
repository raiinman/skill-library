# Visual companion for Codex

Use this optional local browser companion when mockups, layouts, or clickable alternatives would help the user decide. It requires Node.js and Bash; Node and Git Bash are already available on the installation machine. The scripts use Node's standard library, so no npm packages are required.

Start it when the user requests or accepts a browser companion. Keep ordinary scope and requirements questions in chat. Read the preserved [upstream guide](references/upstream-visual-companion.md) for the frame's CSS classes, content examples, and event format; its other-host launch instructions are historical reference.

## Launch on Windows

Resolve `scripts/start-server.sh` relative to this skill's directory. From PowerShell, use Git Bash with forward-slash paths and keep the server in foreground mode so Codex retains the process:

```powershell
& 'C:/Program Files/Git/bin/bash.exe' 'C:/Users/mikea/.codex/skills/brainstorming/scripts/start-server.sh' --project-dir 'C:/path/to/project' --foreground
```

Replace the skill path if installed elsewhere. Launch through a persistent execution session and retain its session ID. Show the returned complete URL in a Codex browser panel; open a system browser only if the user wants that. The launcher disables upstream branding telemetry, binds to loopback by default, and retains the upstream authentication and lifecycle checks.

The startup JSON gives `url`, `screen_dir`, and `state_dir`; it is also saved in `state_dir/server-info`. The URL's `?key=...` authenticates HTTP and WebSocket access. Preserve it when opening the browser and keep session files and tokens out of commits. Project sessions live under `.superpowers/brainstorm/`; follow the project's ignore conventions.

## Iterate

1. Confirm the process is alive, `server-info` exists, and `server-stopped` does not. Restart with the same project directory if needed; the launcher preserves the port and token.
2. Write a fresh, meaningfully named HTML fragment in `screen_dir`. The included frame supplies styling and interaction helpers; full HTML documents are also supported. Use local assets when possible.
3. Show the mockup and summarize the decision it illustrates. Ask for feedback through the host's question interface or the final response.
4. On the next turn, read `state_dir/events` if present and combine it with the user's chat feedback. Click events show selections; they do not authorize unrelated implementation or external actions.
5. Use a new filename for each revision. When moving back to text, replace the stale choice with a simple waiting screen.

## Stop

Terminate the retained execution session when finished; this stops the process Codex launched. Alternatively, the included `scripts/stop-server.sh` accepts the exact session directory and checks its server-instance identity before signaling it. Verify that the process stopped. Persistent project mockups remain available; delete them only within authorized cleanup scope.
