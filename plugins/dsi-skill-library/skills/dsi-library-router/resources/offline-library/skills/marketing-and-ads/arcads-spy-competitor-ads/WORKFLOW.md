# Codex execution note

Read SKILL.md and references/codex-runtime.md first. Their provider, authorization, browser, path, and live-schema rules take precedence over historical host-specific examples below.

# Competitor ad research in Codex

1. Establish the target brand, named competitors, region, and media type from the request. If a missing choice materially affects the research, ask one compact question. When competitors are unnamed, research a relevant shortlist and show it before collecting a large swipe file.
2. Use the connected browser to open the public Meta Ad Library and its visible search/filter controls. Apply video, image, or both consistently. Distinguish the requested brand from similar page names and record source ad/page links and observed metadata.
3. Inspect the relevant ad cards and use the browser's supported media download or pageAssets capability for accessible creative files. Follow the active browser skill. A masked CDN URL is not a reason to inject fetch/download scripts or copy cookies into another client. If the browser cannot retrieve an asset, provide its source link and explain the limit.
4. Put only files from this run into its output directory, using new names and preserving original downloads. Verify media type and that each file is nonempty/playable; deduplicate within the run and label by competitor and source. Deliver a concise linked inventory with useful creative observations.
5. If the user requested adaptation, pass the chosen reference to `$arcads-clone-hook` for video hooks or `$arcads-clone-static-ad` for images, retaining the user's scope. Research does not automatically authorize paid generation or ad publication.

The original detailed guide is retained in references/upstream-skill.md for source history. Its browser mutation scripts and forced Downloads-to-/tmp moves are intentionally replaced here.
