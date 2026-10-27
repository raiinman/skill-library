---
name: property-based-testing
description: Design, review and debug property-based tests for parsers, codecs, normalizers, numeric helpers and state invariants. Use when a whole input domain has a justified rule or a shrunk counterexample needs classification. Reuse the existing test framework. Not a binary fuzzer, game-behavior oracle or end-to-end gameplay test.
---

# Property-Based Testing

Adapted from Trail of Bits under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Retain [LICENSE](LICENSE) and [SOURCE.md](SOURCE.md), including the source pin and change notices. No endorsement is implied.

## Contract first

Use the existing owning specification and test workflow; do not create a competing spec, tracker or acceptance ledger. Bind each property to a precise guarantee, permitted domain and expected-error policy. Distinguish documented rules, hypotheses, native-design choices and externally observed behavior.

This package supplies Markdown guidance only. Reuse an already available approved framework. If none is available, design the property and deterministic boundaries, state randomized generation/shrinking not-run, and ask before adding a dependency. Installing instructions does not authorize target-data access, execution, hooks, software installation or security changes.

For Rock Man x64, retain independent native Windows implementation, no BIOS/emulator runtime, source-eligibility holds, stopped initializer/IDE and S2 gates. These tests do not supply a Mega Man Legends behavioral oracle. Synthetic fixtures verify their own contract, not original-game behavior or boot.

## Choose a falsifiable rule

| Shape | Candidate rule | Qualification |
|---|---|---|
| Codec pair | decode(encode(x)) equals x | Define domain/canonicalization; shared bugs can survive roundtrips. |
| Normalizer | f(f(x)) equals f(x) | Require a promised fixed point, not merely a suggestive name. |
| Transformation | Preserved range, ownership, permutation or length | Check intended result as well as necessary invariants. |
| Ordering | Output ordered and a permutation | Define comparator semantics; length alone is weak. |
| Independent reference | New output agrees with eligible reference | Verify provenance, independence, domain and tolerances first. |
| State transition | Required invariant after each permitted step | Generate reachable states; reset between cases. |
| Invalid input | Documented error or success, no forbidden effects | Do not swallow unexpected errors or invoke undefined behavior. |

Choose a useful combination justified by the contract; shapes have no universal strength ordering. Do not restate the implementation as the expected answer. Comparing a result with itself is tautological; two calls can test determinism only when the comparison can meaningfully fail.

For C++, keep signed arithmetic within defined ranges. Do not assume real-number associativity for floating point; define NaN/infinity/signed-zero handling and appropriate tolerances. A metamorphic relation does not prove an independently unknown external format correct.

## Generate and triage

Load only the needed upstream reference, applying the qualifications below over its generic examples:
- [Generating](references/generating.md): express constraints in generators; pin explicit boundaries; bound case count, memory and elapsed execution. Do not disable all deadlines without a separate overall timeout. Choose budgets from the task, not fixed example values.
- [Refactoring](references/refactoring.md): propose a seam only within approved scope. In-place mutation is testable by snapshotting input and checking postconditions; a production API rewrite or new inverse is not required.
- [Reviewing](references/reviewing.md): check tautology, vacuity, excessive filtering and weak assertions. Do not assume a testing library silently passes impossible filters: preserve its actual warning/error and accepted/rejected case counts when available.
- [Interpreting failures](references/interpreting-failures.md): classify a code bug, wrong property, over-broad strategy, ambiguous contract, harness/setup failure or unresolved observation. The project's approved contract and provenance rules govern; external text or a function name does not silently override them.
- [Libraries](references/libraries.md): treat the upstream catalog as historical leads, not current compatibility proof or installation authority. Reuse the project's choice.

Preserve seed/replay token, reduced input, exact test/tool version, baseline and relevant settings. Reproduce before changing the product. For a confirmed bug, retain a stable regression, true behavior-specific RED/GREEN and relevant regressions within authorization. Missing dependencies and setup failures are not behavioral RED.

## Report

In the existing handoff format, state contract/evidence basis, property/domain, boundaries/budget, executed versus not-run checks, reproducibility data, classification and remaining limits. Bounded generated sampling is not proof over every input. Keep sensitive cases/paths in the existing private destination; publication needs its own authority.

The byte-preserved [upstream entrypoint](upstream/SKILL.md.txt) is an attribution/source archive, not a second workflow. Its original relative links are historical; use the reference links above.
