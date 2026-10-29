---
name: spimdisasm
description: Use an already available, version-checked spimdisasm runtime for bounded static MIPS instruction-word decoding of explicitly authorized inputs. Validate hex encoding, complete four-byte words and explicit byte order/category before invocation. Not PS-X loading, GTE execution, game boot, a REA provider or installation automation.
---

# spimdisasm instruction wrapper

Use this original instruction-only wrapper with the existing DSI source/handoff workflow. [SOURCE.md](SOURCE.md) records the public tool revision and [LICENSE](LICENSE) retains licensing. The library helper discovers instructions; it does not dispatch or install the tool.

## Verify the selected environment

The reviewed baseline is spimdisasm **1.42.4** with Rabbitizer **1.16.2**; upstream requires Python 3.9+ and Rabbitizer >=1.14.0,<2.0.0. Version numbers are not proof of availability or compatibility on another environment.

Before any requested tool operation, resolve the actual selected environment and an already installed interpreter/tool through its approved capability record. Check its installed package versions and that its existing native Rabbitizer dependency can load; use the same interpreter for metadata, help/version and decoding. Use isolated Python invocation (`-I`, with `-B` to avoid bytecode writes) and an approved trusted working directory for module-based probes and decoding. Verify the resulting spimdisasm and Rabbitizer module locations belong to the intended trusted installation, and keep those paths/receipts private. `-I` is module-resolution hygiene, not a security sandbox; it does not make untrusted installed code safe. Do not infer availability from this skill, the helper catalog, a historical receipt, PATH guesses or a different host.

If a prerequisite is missing, incompatible or inaccessible, report that capability gap. Do not download, install, upgrade, alter PATH/providers/security settings, switch environments or repair a denied launcher as a side effect. An installation request needs its own supported authorization and environment scope.

## Bound the question and input

Confirm the intended static question, permitted inputs, word count/time budget, explicit endianness and instruction category. Default to original constructed instructions. A target name, file path or tool installation grants no access to game bytes; original binary/file work requires separate input authorization and source-eligibility review.

Read [input-contract.md](references/input-contract.md) **before every new input representation**. Validate the entire representation and expected length before starting spimdisasm. Its raw CLI silently skips nonhex characters, concatenates hex digits and zero-pads partial words; it is not the validation boundary. Reject malformed input yourself rather than claiming the tool rejects it.

This wrapper covers only the `disasmdis` word-decoding lane. Do not silently advance to file/ELF frontends, overlays, target loading, dynamic execution or wider analysis.

## Invoke only validated words

Use a process argument vector, not shell interpolation. Give one validated eight-ASCII-hex-digit token per four input bytes, with no `0x` prefix. Pass endianness and category explicitly; close stdin or attach the platform's empty input device so unrelated piped data cannot also be decoded. Keep pseudo-instruction selection explicit and recorded; omit `--pseudos` for the constructed example below.

Illustrative argument vector, **after** selecting the verified interpreter and validating the single word:

```text
[verified interpreter, "-I", "-B", "-m", "spimdisasm", "disasmdis",
 "--instr-category", "r3000gte", "--endian", "little", "0100184a"]
```

Here `0100184a` denotes four bytes in little-endian memory order, yielding instruction value `0x4A180001` and the mnemonic `rtps`. It is an original standalone synthetic decoding example, not a game-derived fixture or GTE execution test. Do not reinterpret an integer-looking hex token as bytes without an agreed representation.

Capture exit status, stdout/stderr and the exact validated input count privately. Unexpected output, `.word`, truncation, count mismatch or incompatible version is a limited decode result to investigate, not permission to relax validation, pad bytes, force a category or broaden the input.

## Report honestly

Record tool/dependency versions, category, endian, pseudo choice, input identity/representation, executed/not-run status and the narrow observed result in the existing evidence/handoff system. Create no competing ledger.

Instruction text is static tool output, not authoritative behavioral evidence or eligible replacement implementation. A mnemonic does not establish PS-X EXE loading, correct GP/overlays, delay slots, GTE arithmetic/execution, BIOS behavior, provenance clearance, clean-room certification, game equivalence or boot. This wrapper neither updates nor configures REA and does not establish Windows availability or universal runtime installation. Preserve existing project holds, stopped work and acceptance ownership.
