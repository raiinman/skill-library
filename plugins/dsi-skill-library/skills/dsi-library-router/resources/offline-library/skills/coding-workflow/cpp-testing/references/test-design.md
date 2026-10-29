# Focused C++ test design

- Reuse fixtures, runner and ownership conventions. Keep unit tests in-memory where practical; real files, handles and services belong in explicitly scoped integration checks.
- Prefer injection and stateful fakes for behavior; mock required interactions, not private implementation details. Assert production outcomes as well as call counts.
- With GoogleTest already in use, use fatal assertions for preconditions before dereferencing; nonfatal assertions for independent observations. A sample fixture always returning a constant is not an independent oracle.
- Use fresh fixtures. For concurrency use conditions/latches with bounded waits, not sleeps as synchronization. Diagnose a timeout; do not extend retries indefinitely.
- Inject clocks/randomness when approved. Preserve seeds/replay data and reduced inputs. Cover empty, zero, one-element, boundaries, malformed input and repeated use as the contract requires.
- Check ownership/lifetime and failure transitions where safely injectable: exact capacity, operation failure, cancellation, repeated cleanup and invalid states. Do not deliberately invoke undefined behavior to test rejection.
- Define floating-point tolerances/special values and valid signed arithmetic ranges.
- Keep temporary paths unique within the approved root; preserve failure evidence privately before cleanup.
- For property-shaped domains use property-based-testing guidance, but do not silently add a library.
- Coverage identifies unexercised code, not correctness or original-game equivalence.

In the existing result format record baseline/test revision, requirement, command/configuration, true RED or characterization, GREEN/regressions, exact observed assertion/error, review and not-run platform/oracle/integration checks. Create no new ledger.
