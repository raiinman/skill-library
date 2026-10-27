# MSVC corrections and verification

These are decision checks, not a standalone build recipe. Recheck primary docs against the actual compiler version before changing an approved configuration.

## Configuration

- Reuse the verified environment/preset/toolchain. Distinguish MSVC cl, clang-cl, MinGW and cross-compilers. Do not hard-code a Visual Studio edition/path or equate Linux checks with Windows execution.
- Inspect existing configure/build/test preset relationships and target system; do not introduce a preset because this skill mentions one. Preserve architecture, generator, configuration and private user settings. [Microsoft CMake presets](https://learn.microsoft.com/en-us/cpp/build/cmake-presets-vs?view=msvc-170).
- Keep runtime-library choices consistent across linked modules; diagnose mismatch instead of hiding it with linker exclusions. [Microsoft runtime-library options](https://learn.microsoft.com/en-us/cpp/build/reference/md-mt-ld-use-run-time-library?view=msvc-170), [LNK4098](https://learn.microsoft.com/en-us/cpp/error-messages/tool-errors/linker-tools-warning-lnk4098?view=msvc-170).

## Sanitizers and coverage

- Do not copy GCC/Clang -fsanitize flags onto cl. MSVC ASan uses /fsanitize=address; verify required components already exist. Missing components need separate installation authority.
- ASan requires an instrumented program to execute before yielding runtime evidence. It does not prove race-freedom, absence of every memory defect or gameplay correctness. Microsoft's documented platform is x86/x64 on Windows 10 and later, not an arbitrary target. [Microsoft ASan overview](https://learn.microsoft.com/en-us/cpp/sanitizers/asan?view=msvc-170).
- Do not recommend /fsanitize=thread, /fsanitize=undefined or GCC/Clang equivalents as supported cl configurations. That overview lists other sanitizers as future directions. Other toolchains need separately verified support and authority.
- Check incompatibilities first: /RTC, incremental linking and Edit-and-Continue conflict with MSVC ASan; further limits appear in [Microsoft known issues](https://learn.microsoft.com/en-us/cpp/sanitizers/asan-known-issues?view=msvc-170). Propose a separately scoped diagnostic configuration; do not silently weaken normal builds, disable security controls or activate a stopped target.
- Prefer target-scoped approved diagnostics, retaining normal settings. Microsoft does not recommend ASan for production.
- Upstream GCC/gcov/lcov and Clang profile/llvm-cov examples are not MSVC coverage commands. Use already approved, version-verified tooling or mark coverage not-run. No coverage tool ships here.

## Commands and evidence

Use only verified owner-supplied commands and configuration-specific binary locations. Configure steps may download dependencies or run build logic: inspect effects before execution. For multi-configuration builds, select the actual requested configuration consistently rather than assuming CMAKE_BUILD_TYPE selects it.

Retain compiler/version/frontend, architecture, runtime configuration and commands privately. Public summaries use sanitized evidence IDs, never private paths or source.
