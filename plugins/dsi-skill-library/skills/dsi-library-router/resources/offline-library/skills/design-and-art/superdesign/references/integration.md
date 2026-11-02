# Personal local integration

This adaptation replaces the upstream service-dependent workflow with local design authoring. It needs no Superdesign CLI, account, hosted project or API key. Do not install or initialize the modern Superdesign agent to use it.

The standalone Superdesign Personal app stores ordinary project folders and watches `.superdesign/design_iterations` for HTML and SVG changes. Use Open a folder to attach an existing project. Briefs copied from the app include the exact project and output directory, so Codex and Claude can write drafts directly there.

The app provides local starter templates, desktop/mobile comparisons, source editing, import/export and new-file duplication. Templates are examples, not AI generation. Editor saves preserve previous content in `.superdesign/history` and reject a stale save after an external edit.

Use self-contained documents with embedded CSS, SVG, data images and available fonts. Scripts and external resources are disabled in preview frames. Export preserves original source, so use a separately permitted local browser for JavaScript interactions. Do not enable network access or upload assets to resolve missing resources.

The original modern Superdesign primary remains in upstream-skill.md; inherited manuals preserve provenance and are not active instructions. The local workflow takes precedence over their hosted-service commands. The user's agent host may itself require a model connection; this app is not an offline language-model runtime.
