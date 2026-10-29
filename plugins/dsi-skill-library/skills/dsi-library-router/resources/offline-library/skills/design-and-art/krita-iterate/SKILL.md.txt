---
name: krita-iterate
description: Draw or improve a fox on a bicycle in Krita through reference study, editable objects, numbered versions and a final progression review. Use for the fox-bike illustration workflow, not plugin installation or compatibility debugging.
metadata:
  library_source:
    kind: installed-local-snapshot
    original_skill_sha256: 702703a39c20c4aa1d635bcbe13c467db9ed23e1e6d8c4f2cb3b9b1992a7dc12
---

# Fox Bike Drawing

Adapted from edithatogo/krita-cli's pelican-bike workflow at commit `8245fd4c92ed2b413cb975230891f4e8cda61d0a`; MIT terms are included in LICENSE. The unchanged source packet and change analysis are in [the workflow study](C:/Users/mikea/work/krita-mcp/docs/workflows/krita-cli/analysis.md).

Use the copied workflow skeleton for our fox-on-a-bike example: preserve a rough baseline, study fox references, use a dedicated illustrator brief, save numbered revisions, record lessons and archive the progression. The [example workflow](C:/Users/mikea/work/krita-mcp/docs/workflows/krita-cli/example-workflow.md) links all four adapted artifacts.

## Core approach

Study useful fox profile/head views and bicycle-rider geometry before a new drawing pass. Extract structure before detail: pointed ears, narrow muzzle, connected torso/head, bushy tail, wheels, frame and rider contacts. Follow the requested style and fidelity. The [fox anatomy notes](references/fox-anatomy.md) own the visual checklist and reference-use guidance.

## Fox and bicycle construction

Start with wheels/frame and broad fox masses. Keep a clear frame opening beneath the torso. Plan saddle support, hind paws on pedals and forepaws on handlebars for the intended pose. Give the tail a visible attachment and the muzzle/head/neck a continuous join. Add character through ear angle, gaze and pose after the rider/bike relationship works; fur and spokes cannot fix detached parts.

Keep bike, torso, limbs, head/tail shapes and wording editable. Use the [fox-bike illustrator agent](references/fox-bike-illustrator.md) for pass planning and failure review. It is an agent brief for the current operator, not automatic delegation.

## Establish the work

- State the subject, reference/fidelity target, intended viewing size, editable elements and reasonable pass budget. Use the user's existing answers; ask only for consequential missing information.
- Preserve reference files and existing documents. Use a separate work document unless the user requested an existing-document edit. Read prototype health/state to obtain actual allowed roots, runtime capabilities and explicit document/layer IDs before issuing edits.
- Prefer `krita-prototype` tools when available; the separate Codex Bridge is a different implementation. CLI `krita-mcp` shares the prototype contract.
- Record reference URLs/source/license where known and distinguish observations from inferred hidden structure. Follow the requested original illustration, faithful reconstruction or corrected reconstruction goal; do not silently switch between them.
- When continuing existing fox versions, read the [fox-bike learning log](C:/Users/mikea/work/krita-mcp/docs/workflows/krita-cli/fox-bike-learning-log.md) before choosing the next correction. Keep executed findings separate from proposed passes.

## Build and preserve the baseline

Create meaningful object groups and native paint/vector/text layers for the promised editable parts. Plan overlap, depth, contact points and dependent shadows/reflections before detail. A named layer that contains the whole image does not provide object editability.

Draw broad masses and structural geometry first. Choose an exact native brush preset and deliberate size/opacity/flow. Native line shapes and segmented strokes both depend on the current brush; select geometry for the intended mark. Native vector shapes are useful where individual shape edits are required. Vector positions are points, not canvas pixels.

Preserve the first rough result as `v001.kra` and `v001.png` under a new run folder inside an already allowed output root. Record actual returned hashes/byte counts. Never label the rough baseline final or overwrite it to hide a failed pass.

## Iterate toward the stated goal

Use normal canvas previews as drawing feedback; formal automated/live validation runs at the end after planned edits. Review at the intended viewing size and inspect a useful detail crop where joins, lettering or contact points matter. Fix the largest observed problem first: composition/silhouette, depth/overlap, proportion/pose, contour hierarchy, then local polish as relevant to the requested style.

For each numbered pass, record the observed problem, one bounded change hypothesis, affected objects and intended improvement. Keep successful geometry unless a specific problem justifies rebuilding it. Use fresh state after lifecycle/history operations, and optional `expected_revision` guards when a complete revision is available. Missing/unsupported fingerprints are not protected work.

Give generic mutations a caller-owned operation ID. A timeout is an unresolved outcome: inspect that ID and the document before further work. Our batches accept at most 16 commands, stop on failure and report completed work; they are not atomic or single-undo edits. Split plans at meaningful dependency boundaries rather than replaying a failed whole batch.

Save each retained pass with unique numbered KRA/PNG names and a short honest review. Keep rejected versions in the progression and mark acceptance explicitly. Stop when the requested goal is met, the pass budget is used, progress regresses, or a missing capability prevents the required result. Do not manufacture 21 passes to imitate the source log.

## Final validation and delivery

After all planned edits, validate the final exports and save/reopen representative native content with fresh IDs. Check actual object movement/recoloring and wording changes when those forms of editability were promised; preserve the saved deliverable before disposable edits. Inspect overlap repairs and dependent effects. Native calls succeeding alone do not prove appearance or editability after reopening.

Record unsupported requirements, font/file dependencies, color/profile limits and unresolved operation outcomes. Archive only intended outputs; exclude tokens, connection settings, journals and unrelated user files. Use [package_review.py](scripts/package_review.py) with the schema in [review-package.md](references/review-package.md) to produce a ZIP, contact sheet and playback review from the completed numbered exports. Playback illustrates the development sequence; it is not editable Krita animation authoring.

Deliver the chosen editable KRA, PNG, version manifest, review/archive links, principal changes and remaining limitations. Keep all development local unless the user separately authorizes publishing.

## Failure review and current lessons

Diagnose the picture before rebuilding it. A hidden frame needs overlap correction; a generic animal needs clearer muzzle/ears/tail; a floating rider needs support/contact; detached head/tail shapes need connected joins. Preserve successful geometry while correcting the largest visible defect.

Our V001/V002 fox fixtures demonstrate frame separation and changed pedal contact. The reopened copy demonstrates body movement/recolor and POST-to-MAIL editing. Tail/head joins, saddle support and forelimb contact remain open art problems. The [learning log](C:/Users/mikea/work/krita-mcp/docs/workflows/krita-cli/fox-bike-learning-log.md) is the authoritative version history. Do not copy the original's 21 passes or treat its stroke/export workaround as a finding about our native renderer.
