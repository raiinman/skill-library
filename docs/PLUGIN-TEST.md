# Debugging smoke test

Run `node --test tests/plugin-smoke.test.mjs` or the full suite with `npm test`.
The two new tests use no external accounts or network access:

- Invoke the packaged source reader as a real CLI process against an isolated clone
  of this committed library. Verify debugging skill discovery, exact commit-pinned
  skill/provenance bytes, and explicit failure for missing resources and invalid options.
- Verify that the fresh-chat fixture really fails with its intended missing export.

The suite now contains eleven automated tests. CLI retrieval coverage is not a model
selection test; it locates the expected skill by ID and does not implement a mock router.

For a host-level debugging exercise, copy `tests/fixtures/failing-build/` to a new
directory, open that copy in a fresh chat, and follow `TEST-PROMPT.txt`. The fixture
has no dependencies and needs only Node/npm. It intentionally starts broken; the
normal library test checks this, so do not fix the original fixture in the repository.
The independent fixture verifier checks application exit status and expected output.

Record the reported source commit, selected skill, actual initial failure, final checks,
and whether the small follow-up reused the task revision. Explicit invocation and an
optional separate implicit-selection trial are distinct tests. Neither is automatically
established by the CLI smoke test.
