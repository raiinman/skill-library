---
name: superdesign
description: Design and iterate personal UI mockups, pages and components as local HTML or SVG files. Use for the user's offline Superdesign workflow, local design canvas, visual alternatives or revisions, without Superdesign's hosted agent, account or CLI.
license: MIT
---

# Superdesign Personal

Use the current coding assistant to design locally. The deliverable is real code on the user's computer, visible in the personal design canvas or a local browser preview. No Superdesign account, cloud canvas, CLI, paid generation or upload is required. The assistant's own model connection is separate from this file-based workflow.

## Start from the actual brief

Read the requested screen, product and existing brand before choosing a direction. For an existing application, inspect the relevant page, tokens and components; preserve its features and conventions. For a new idea, use the context already supplied. Ask only when missing information materially changes the design; otherwise state a brief interpretation and proceed.

Choose typography, spacing, contrast, composition and one purposeful accent from the product. Make the result feel specific through hierarchy and content. Preserve the user's explicit colors and branding. Design for keyboard focus, readable contrast, reduced motion and responsive layouts.

## Create local iterations

1. Use the project folder chosen by the user or already open in the personal app. Read an existing `.superdesign/briefs/` brief when the user points to one.
2. Save each draft directly in `.superdesign/design_iterations/` as a complete HTML or SVG file. Use an unused name such as `dashboard_1.html`. The app watches this directory. Do not overwrite a previous variant merely to add another.
3. For standalone HTML drafts, embed CSS, SVG and any permitted images as data assets. Use system or bundled fonts. Avoid CDN scripts, remote fonts, analytics and external service dependencies so the preview works without network access. Native CSS is sufficient; an existing project build may use its installed tools.
4. Build one strong direction when the user asks for one design. When they ask to explore or compare, create two or three meaningfully different compositions and explain their tradeoffs. Do not spawn agents merely to produce variants.
5. Keep source editable. Use the project's real components when implementing a selected design into an application, instead of shipping a standalone mockup as a replacement for its stack.

## Preview and refine

Open the project in Superdesign Personal when installed, or use the host's permitted local preview tools. The personal app discovers local HTML/SVG drafts, compares them at desktop/mobile widths, and offers a source editor, duplication, import and export.

The app's embedded previews disable scripts and remote assets. A script-dependent interaction needs a separate permitted local browser check; do not call it tested from a static thumbnail. Inspect desktop and narrow viewports, typography, clipping, focus and relevant interactions. If visual tools are unavailable, distinguish source checks from unviewed results.

For requested revisions, refine the selected direction and keep a recoverable checkpoint. Save an alternative under a new name only when the user wants an alternative. Respect edits made outside the app and never replace a newer file from stale editor state.

Return the actual local files, the chosen direction, and checks really performed. Do not promise an online canvas URL or generate a first design merely because the skill is being installed.

## Provenance and app integration

See [local integration notes](references/integration.md) and [source attribution](SOURCE.md). The preserved upstream primary and service manuals are archival reference material, not the active personal workflow. Do not execute their login, initialization, upload or remote-generation instructions for this skill.
