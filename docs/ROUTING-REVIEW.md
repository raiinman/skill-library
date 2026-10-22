# Routing instruction review

Evaluation: **manual instruction review only**. No actual fresh-host selection tests were performed. The cases in `tests/routing-cases.json` document expected model behavior after reading instructions; they are not results from an implemented routing algorithm, a hosted model evaluation, or installed workflow execution.

The router supplies sensible selection constraints: preserve explicit selections, compare native descriptions, prefer a focused match, avoid revisiting IDs, and skip routine conversation and small follow-ups. Its source contract consistently requires one full commit for the index and dependent resources. Discovery, retrieval, installed availability and executed behavior remain separate states.

Representative interface, debugging, Blender, UEFN, explicit skill/provider, greeting, follow-up and source-failure cases were reviewed against relevant canonical entrypoints. Specific task wording is important: visual direction maps naturally to `frontend-design`; existing accessible component implementation to `frontend-ui-engineering`; general Blender modeling to `blender`; reference reconstruction to `img2blender`; browser export to `blender-web-pipeline`. These are defensible expected choices, not guaranteed host dispatch results. Broad UI polish requests can reasonably match several descriptions; the router does not establish deterministic tie-breaking.

## Native discovery metadata

The relevant reviewed canonical skills already have native `name` and `description` frontmatter. No custom routing field is needed for host discovery. Two small improvements would reduce ambiguity without changing the architecture:

- `high-end-visual-design`: add a focused use condition to its description, for explicitly requested premium agency-style visual direction, and an exclusion for maintaining an established design system. Its current description advertises quality but does not clearly delimit when to select it over the other frontend skills.
- `uefn-toolbelt`: change the description's assertion of a globally installed server to an available or configured server. Its body contains historical installation paths and live test claims; add an early environment note that those records do not establish availability or authorized project paths on the current host. The umbrella router already says this, but the canonical entrypoint should remain safe when explicitly invoked on its own.

`using-agent-skills` has a broad session-start description, but its body is an engineering phase router. Narrowing the description to engineering workflow selection would improve direct discovery and avoid overlap with this library router. A focused debugging task should go directly to `debugging-and-error-recovery`.

## Source reader review

`source.mjs` uses argument-array process execution, contained repository resource paths, full SHA reads, a lock index hash, byte-preserving outputs and exclusive output creation. It does not execute retrieved scripts. Its Git fixture tests exercise source updates and binary retrieval; those tests are not model routing tests.

Two correctness concerns were reported during review:

1. Git `begin` fetches into shared `FETCH_HEAD`, then resolves it in a second process. Concurrent tasks fetching different branches through the same checkout can race and lock the other task's commit. Fetch into a unique temporary ref and resolve that ref, or use another mechanism with an isolated per-task commit result.
2. Git `begin --repo` does not verify that `origin` identifies the intended `raiinman/skill-library`. A mistaken checkout with a compatible index can silently become the source. Validate the expected canonical origin, or require and record a deliberate caller source-identity check before invoking this adapter. This matters because the router promises a particular source, while the lock currently records only the checkout path.

Both concerns were addressed after review: the reader now fetches into a unique
temporary ref and records the origin URL, while retrieval instructions require checking
that origin against the DSI authority. The helper also accepts alternative explicitly
supplied checkouts for fixtures. Neither concern occurred during this task. The three
targeted metadata suggestions above were also implemented. Fresh-chat dispatch and
workflow execution still require separate host tests.
