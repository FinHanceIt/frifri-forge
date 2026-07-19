#!/usr/bin/env python3
"""
textstats.py — real, dependency-free text metrics for OriginForge.

Used by ai-forensics (analysis) and qc-rescan (re-scan). Computes the
quantitative signals that AI detectors actually lean on: sentence-length
distribution (burstiness), lexical diversity, transition density, and
punctuation profile. EN + RO aware. Output is JSON.

These are SIGNALS, not proof. Interpret them with references/ai-tells.md.
Short texts (<300 words) are unreliable — the script flags this.

Usage:
    python3 textstats.py path/to/file.txt
    python3 textstats.py -            # read from stdin
"""
import sys, re, json, math
from collections import Counter

EN_TRANSITIONS = {
    "moreover","furthermore","additionally","however","therefore","thus",
    "consequently","nevertheless","nonetheless","hence","accordingly",
    "indeed","notably","importantly","ultimately","overall","subsequently",
    "in addition","in conclusion","that said","it is worth noting",
    "it's worth noting","on the other hand","as a result","for instance",
}
RO_TRANSITIONS = {
    "de asemenea","în plus","prin urmare","totodată","astfel","așadar",
    "în concluzie","pe de altă parte","de exemplu","în consecință",
    "cu toate acestea","totuși","în primul rând","în al doilea rând",
    "merită menționat","este important de menționat","prin urmare",
}
AI_PHRASES_EN = [
    "delve into","it's worth noting","in today's fast-paced world","crucial role",
    "pivotal role","navigate the complexities","a testament to","underscores the importance",
    "rich tapestry","ever-evolving","in conclusion","it is important to note",
]
AI_PHRASES_RO = [
    "merită menționat","este important de menționat","în lumea de azi",
    "joacă un rol crucial","un rol esențial","în concluzie","la sfârșitul zilei",
    "are sens","în termeni de",
]

def split_sentences(text):
    # split on . ! ? … and newlines; keep it simple and language-agnostic
    parts = re.split(r"(?<=[.!?…])\s+|\n+", text.strip())
    return [p.strip() for p in parts if p.strip()]

def words(text):
    # letters + Romanian diacritics; treat hyphen/apostrophe as separators
    return re.findall(r"[A-Za-zĂÂÎȘȚăâîșț]+", text)

def mean(xs):
    return sum(xs)/len(xs) if xs else 0.0

def stdev(xs):
    if len(xs) < 2:
        return 0.0
    m = mean(xs)
    return math.sqrt(sum((x-m)**2 for x in xs)/(len(xs)-1))

def main():
    if len(sys.argv) < 2:
        print("usage: textstats.py <file|->", file=sys.stderr); sys.exit(1)
    src = sys.argv[1]
    text = sys.stdin.read() if src == "-" else open(src, encoding="utf-8", errors="ignore").read()

    sents = split_sentences(text)
    toks = [w.lower() for w in words(text)]
    n_words = len(toks)
    n_sents = len(sents)
    slens = [len(words(s)) for s in sents] or [0]

    types = set(toks)
    ttr = len(types)/n_words if n_words else 0.0
    hapax = sum(1 for _, c in Counter(toks).items() if c == 1)
    hapax_ratio = hapax/n_words if n_words else 0.0

    low = text.lower()
    trans_hits = sum(low.count(t) for t in EN_TRANSITIONS) + sum(low.count(t) for t in RO_TRANSITIONS)
    trans_density = trans_hits/n_sents if n_sents else 0.0

    ai_phrase_hits = {p: low.count(p) for p in (AI_PHRASES_EN + AI_PHRASES_RO) if low.count(p) > 0}

    sl_mean = mean(slens)
    sl_sd = stdev(slens)
    # burstiness: coefficient of variation of sentence length (higher = more human)
    burstiness = (sl_sd/sl_mean) if sl_mean else 0.0

    punct = {
        "em_dash": text.count("—"),
        "semicolon": text.count(";"),
        "colon": text.count(":"),
        "exclaim": text.count("!"),
        "question": text.count("?"),
        "parens": text.count("("),
    }

    # crude readability proxy
    avg_word_len = mean([len(w) for w in toks]) if toks else 0.0

    report = {
        "word_count": n_words,
        "sentence_count": n_sents,
        "sentence_len_mean": round(sl_mean, 2),
        "sentence_len_stdev": round(sl_sd, 2),
        "burstiness_cv": round(burstiness, 3),
        "type_token_ratio": round(ttr, 3),
        "hapax_ratio": round(hapax_ratio, 3),
        "avg_word_len": round(avg_word_len, 2),
        "transition_density_per_sentence": round(trans_density, 3),
        "ai_phrase_hits": ai_phrase_hits,
        "punctuation": punct,
        "reliability": ("LOW — under 300 words, treat as weak signal"
                         if n_words < 300 else "OK — 300+ words"),
        "reading_guide": {
            "burstiness_cv": "≳0.5 leans human; ≲0.3 leans uniform/AI (rough)",
            "transition_density": "high (>0.4/sentence) suggests AI scaffolding",
            "ttr": "very low TTR + low hapax suggests flat, predictable lexis",
            "note": "Signals only. Never accuse on numbers alone. See ai-tells.md.",
        },
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
