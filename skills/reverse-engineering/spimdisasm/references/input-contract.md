# Strict caller-side input contract

## Accepted representation

For this narrow lane, accept a nonempty explicit list of complete instruction-byte tokens. Each token must contain **exactly eight ASCII characters from 0-9, A-F or a-f**, representing four bytes in the already agreed memory order.

If the user supplies text rather than a token list, accept only this whole-string grammar:

```text
[0-9A-Fa-f]{8}(?: [0-9A-Fa-f]{8})*
```

Use a true full-string match, not a substring search or an end-anchor that permits a trailing newline. The only separator is one ordinary ASCII space. Reject tabs, newlines, repeated/leading/trailing spaces, Unicode lookalikes, labels, comments, addresses, prefixes such as `0x`, punctuation, option-like text and any incomplete or excess digits. Do not trim, filter, concatenate fragments, pad or truncate to make an input valid.

Before invocation, verify the agreed word count and resource budget, exactly four bytes per token, selected endianness and supported instruction category. Split validated text only at the validated spaces; pass each token separately as an argument. If input representation or expected length is uncertain, ask for clarification before decoding.

A binary file or byte-array request is outside this default lane. Do not open a file or convert original bytes just to fill a missing token list. A separately authorized bounded byte-array adaptation must establish its source identity and exact byte count first; reject empty or non-multiple-of-four lengths before conversion, preserving byte order without padding. Do not silently switch to a file frontend.

## Upstream caveat

At the reviewed public source revision, `wordGeneratorFromStrList` skips characters outside the ASCII hex set, combines digits across arguments and emits each group of eight digits. Its final partial group goes through `getWordFromStr`, which appends zero bytes to complete a word. The command can also read stdin before processing positional arguments.

Therefore a successful raw command is **not** evidence that input was valid, complete or only came from the intended arguments. Caller validation, explicit empty stdin, argument-vector invocation and result-count checks are required by this wrapper. The malformed-input rejection belongs to the caller, not spimdisasm.

Do not send malformed cases to the tool merely to demonstrate this known source behavior. Reuse an existing authorized original-synthetic receipt where available; no new broad smoke suite is required for a documentation/routing addition.

Primary source: [DisasmdisInternals.py at the reviewed revision](https://github.com/Decompollaborate/spimdisasm/blob/4b5d4c68eeb9f9eae14b3bb713971433ae2c3c43/spimdisasm/disasmdis/DisasmdisInternals.py).
