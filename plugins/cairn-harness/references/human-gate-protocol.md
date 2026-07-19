# The Human Gate Protocol — reviewing when you're not the compiler

The human who reviews does not read code line by line, and should not have to. But they cannot
be the gate for something they don't understand — a review you can't understand is theatre. So
making the human able to review is not a courtesy; it is the mechanism.

Whenever an agent needs the human to verify something, it STOPS and emits a **Gate Card** — in
the human's language, plain words, max 15 lines.

```
--- GATE ---

WHAT I'M PROVING
<one sentence, zero jargon. If you use a technical term, gloss it in parentheses.>

ANALOGY (optional)
<"Like a wax seal on an envelope: it doesn't stop anyone opening it, but you can see if they did.">

WHAT YOU SEE BELOW
<the literal command output. Copied, not summarized.>

WHAT IT MEANS
<plain translation. "The test failed. That's good — I haven't written the code yet.">

HOW I COULD BE LYING TO YOU HERE
<the concrete mechanism. "I could write a test that passes no matter what. Check that it asks the code for something real.">

WHAT YOU DO
<one action. "Read the test. If you understand what it asks of the code, say GO. If not, tell me what's unclear — that's on me.">
```

Three moments always require a Gate Card: **RED** (test fails, before implementation), **GREEN**
(test passes, after), **STUCK** (anything the agent can't do, or a test it believes is wrong).

If the agent can't write the "what I'm proving" sentence without jargon, it doesn't understand the
test. Stop and simplify the test.

## Glossary (gloss on first use in any Gate Card)

- **exit code** — the number a command leaves behind. 0 = worked, anything else = failed. The only thing we trust.
- **hash / SHA-256** — a fingerprint of a file. Change one letter, the fingerprint changes completely.
- **vacuous test** — a test that passes no matter what the code does. Worthless, and dangerous because it looks green.
- **mutation testing** — deliberately breaking the code to see if the tests notice. If they don't, the tests weren't checking anything.
- **shadow mode** — a gate that watches and writes down what it *would* have blocked, but doesn't block yet.
