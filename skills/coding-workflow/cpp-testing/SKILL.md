---
name: cpp-testing
description: Write, review or diagnose native C++ unit and integration tests, genuine RED/GREEN evidence, flaky tests and MSVC-specific test configurations. Reuse existing project runners and dependencies; inspect CMake/CTest or GoogleTest only when the project uses them. Not general feature implementation or a game-behavior oracle.
---

# C++ Testing

Adapted from Affaan Mustafa's ECC skill under [MIT](LICENSE). See [SOURCE.md](SOURCE.md) for the exact pin and changes. Use as a companion to existing planning/spec/TDD, not a replacement build system.

## Establish the slice

Read applicable project contracts and the owning specification. Obtain the exact baseline, compiler/frontend/version, architecture, configuration, runtime-library choice, runner and known test command from the project. Do not invent private paths or infer compiler identity from the host OS.

Retain the existing framework, layout and acceptance owner. GoogleTest, Catch2, doctest, CTest and custom runners are alternatives, not installation requirements. Do not add FetchContent downloads, dependencies, hooks, CI jobs, global flags, software or security changes as a side effect. A missing tool is a reported prerequisite, not permission to install it.

For Rock Man x64, preserve independent native implementation, no BIOS/emulator runtime, source-eligibility holds, stopped initializer/IDE and S2 gates. Use synthetic inputs unless original-input access is separately authorized. Passing synthetic tests do not supply an original-game oracle or establish boot.

## Behavior-focused loop

1. Bind one observable behavior and edge/error cases to the owning contract. Separate native-design requirements from inferred original-game behavior.
2. For a behavior change, demonstrate genuine behavior-specific RED on the intended baseline. Missing includes, dependencies, unsupported commands and compile/setup failures are not behavioral RED. For a refactor, capture characterization first.
3. Make the smallest approved correction for GREEN. Keep expected effects independent of production logic; do not copy the algorithm into its oracle.
4. Run the focused case, relevant regressions and broader applicable suite. Record actual commands/configuration, exit status and evidence. Do not replace failure with deleted assertions, blind warning suppression or unbounded retries.
5. Resolve independent review before claiming acceptance; the existing acceptance owner/system remains authoritative.

Use [test-design.md](references/test-design.md) for isolation, assertions, lifecycle/failure cases and reproducibility. Read [msvc.md](references/msvc.md) before compiler/sanitizer or Windows configuration decisions.

## Evidence levels

Report separately: source review; compile/link; synthetic component behavior; real Windows execution; visible/input/audio behavior; eligible original-reference comparison; full-game integration. Linux/cross-compile results are not MSVC execution. Compile success is not an AddressSanitizer runtime result.

If a required check cannot run, name the missing capability and mark it not-run. Installing these instructions verifies no compiler, framework, provider or target.

The byte-preserved [upstream entrypoint](upstream/SKILL.md.txt) is source history only. Do not execute its generic download/build/sanitizer examples instead of the verified project workflow.
