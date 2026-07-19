# Humanization Playbook — make an OWNED draft genuinely human + original

For `humanizer` and `originality-transformer`. This is real editing craft, not a bypass trick. It only runs on the user's own / AI-assisted / licensed text (Gate 0). The goal is **quality and genuine originality** — which is also, not coincidentally, what reads as human and what survives classifier-based detectors. We never promise a detector score.

## The two levers that actually matter
1. **Burstiness** — break the flat rhythm. Mix very short sentences with long ones. Use a fragment. Start a sentence with "And" or "But" where it earns it. Let one line land hard, then breathe. Vary paragraph length too.
2. **Genuine perplexity through real specificity** — replace generic claims with concrete ones the author actually knows: a name, a number, a date, a place, a small lived detail, a real opinion. This raises lexical surprise *truthfully*. (Synonym-swapping raises perplexity falsely and reads worse — don't.)

## The seven moves
1. **Cut the connective scaffolding.** Delete most "Moreover / Furthermore / Additionally / It's worth noting / In conclusion." Let ideas abut directly.
2. **Kill the formulaic skeleton.** Don't restate the prompt in the intro; don't summarize in a tidy "Ultimately." Open mid-thought, end on a real point.
3. **Add a point of view.** AI hedges both sides forever. Take a position; let the author's judgment show.
4. **Inject voice.** Idiom, rhythm, register, an aside, a touch of humor or bluntness — whatever is true to the author and the audience.
5. **Replace generic examples with specific ones.** "Many businesses struggle with X" → "A 4-person agency I worked with lost two days a month to X."
6. **Allow controlled imperfection.** Slight asymmetry, a parenthetical, a sentence that trails — humans aren't perfectly parallel. (Never introduce factual errors.)
7. **Tighten.** AI pads. Remove filler; if a word can go and the meaning stays, cut it.

## Romanian naturalization (always with `romanian-grammar`)
- Strip anglicisme/calcuri ("face sens" → "are sens"; "în termeni de" → "din punct de vedere al").
- Vary the connectors; don't start three sentences with "De asemenea / În plus."
- Add natural oralitate and register appropriate to the audience; allow short, elliptical sentences.
- Keep diacritics correct, but let the rhythm be human, not textbook.

## Anti-patterns — never do these
- **Synonym spinners / word salad** — detectable, lowers quality, dishonest.
- **Invisible characters, homoglyphs, zero-width spaces, unicode look-alikes** — a cheap trick that classifier detectors and copy-paste checks catch, and that corrupts the file.
- **Padding to dilute** — adds nothing, reads worse.
- **Fabricating specificity** — never invent fake names/numbers/quotes to "sound human." Specificity must be true.

## What to tell the user afterward (honesty)
Report what changed and why. State plainly: this is now stronger, more original writing; it is **not** "undetectable." If a classifier-based detector still reads it as AI-assisted and the draft genuinely was AI-assisted, that is not a bug to defeat — `qc-rescan` reports the residual read honestly and, if the use case requires attested sole authorship, says so.
