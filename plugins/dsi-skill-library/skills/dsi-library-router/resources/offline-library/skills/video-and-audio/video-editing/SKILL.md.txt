---
name: video-editing
description: Edit existing video footage with cuts, ordered segments, captions, overlays, audio cleanup, and reframing. Use for vlogs, demos, tutorials, and clips made from real recordings.
license: MIT
---

# Video editing

Use local FFmpeg and ffprobe for ordinary editing. Add Remotion only when programmable composition earns it, or use the user's existing editor. Select the tools the edit needs; a full multi-service pipeline is optional.

## From footage to verified export

1. Inspect source files with `ffprobe -v error -show_format -show_streams -of json input.mp4`. Establish the requested output, aspect ratio, and clips to keep. Use provided transcripts or an available transcription tool; don't invent spoken content or timestamps.
2. Keep an ordered edit decision list (source, start, end, purpose). Preserve that order when concatenating; alphabetical file order can scramble a story. Keep originals and render to new paths. Before changing a native editor project, save a versioned checkpoint and verify it exists; save again after the edit.
3. Cut and assemble the story, then add the requested captions, overlays, reframing, or audio treatment. Inspect subject position before cropping; center crop can remove the subject. Burn captions or deliver a subtitle file according to the request, checking timing and readability.
4. Probe the export for expected streams, duration, dimensions, and playable codecs. Decode it to check errors, inspect frames around cuts and overlays, and listen to audio when playback is available. Distinguish a successful render from visual or audio review you could not perform. Hand off the rendered file and any requested editable project.

## FFmpeg examples

These commands work in PowerShell and Bash. Quote actual paths, use new output names, and check exit codes.

```sh
# Accurate 3.25-second cut beginning at 12.5 seconds, re-encoded.
ffmpeg -n -ss 12.5 -i input.mp4 -t 3.25 -c:v libx264 -crf 18 -preset medium -c:a aac -movflags +faststart cut.mp4

# Extract mono audio for a transcription tool.
ffmpeg -n -i input.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le transcript-audio.wav

# Inspect silence; choose cuts after reviewing the result.
ffmpeg -i input.mp4 -af silencedetect=noise=-30dB:d=2 -f null -

# Decode an export to check errors.
ffmpeg -v error -i output.mp4 -f null -
```

`-c copy` is fast but cuts may follow keyframes rather than exact requested frames. Use re-encoding when timing matters. A concat demuxer list must explicitly preserve edit order and use compatible streams; normalize differing codecs, dimensions, frame rates, and audio before joining. Use a two-pass loudness workflow when a precise delivery target is required.

## Optional composition and generated assets

Use an existing Remotion project for repeated graphic compositions, checking current official docs before API-specific code. Install project dependencies in that project, not globally. Voiceover, stock assets, and cloud generation require the relevant provider access and authorization to upload media or spend credits. Use available tools or the provider API; upstream `generate(...)` snippets are conceptual, not installed Codex tools. Missing `videodb`, `fal-ai-media`, or taste skills do not block local editing. Detailed historical examples are in [the upstream reference](references/upstream-skill.md); check current APIs before reusing them.

## Optional DaVinci Resolve / Fusion presets

Read [Fusion host notes](references/fusion-hosts.md) before installation. [ITO Production v1](assets/fusion/ito-production-v1/README.md) contains restrained bloom, RGB fringe, and luminance halo starting presets. [ITO V28](assets/fusion/ito-v28/README.md) preserves compatibility examples with documented visual defects; it is not a production default. A luminance mask is not subject tracking. Review on the actual shot.
