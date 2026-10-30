# Optional helper runtime

The design workflow itself requires no npm package, paid account, or image provider. The included snapshot and story helpers need Node.js, the `playwright` npm library and its Chromium browser. Story export also needs FFmpeg on PATH. They work in Codex or Claude when local execution is available; hosted chats without local execution use their permitted browser/image tools and cannot promise these exports.

Install Playwright in a dedicated runtime directory with `npm install --save-exact playwright@1.64.1`, then run `npx playwright install chromium` there. The scripts resolve Playwright from their own installation or the working directory. On this Windows machine that dedicated directory is `C:/Users/mikea/.codex/tools/unslop`; run Node from there with absolute script and input/output paths. FFmpeg is already on PATH. No user browser profile is used.

The snapshot helper saves an HTML copy and a sibling `.live.png`. Existing output paths are overwritten. Saved pages can retain external resources, inline handlers and page data, so use a fresh output directory, inspect what was captured and do not treat the file as sanitized or as an editable live-site deployment.

The story helper overwrites its video output and recursively replaces the `.story-frames` folder beside its input HTML. Use a fresh dedicated story directory with no existing `.story-frames` directory, and verify resolved paths before running it. Default output is a roughly 10-second square video; `--play` opens a foreground browser only when the user wants that preview. Prefer headless export. Inspect the result before claiming a finished video.

These upstream helpers are retained without code changes. Their dependency error messages include macOS examples; use the local runtime and existing FFmpeg on Windows rather than `brew`. Image generation uses the host's installed capabilities and its authorization rules, without configuring another account automatically.
