#!/usr/bin/env python3
"""Weighted speaker score. Usage: score.py s1 s2 s3 s4 s5 s6 s7   ('-' = not scored)"""
import sys

CRITERIA = [
    ("Audience relevance", 20),
    ("Lived story", 20),
    ("Practical, not generic", 15),
    ("Contrarian edge", 15),
    ("Audience interaction", 10),
    ("Next-day call to action", 10),
    ("English delivery", 10),
]
TARGET = 8.0


def main(args):
    if len(args) != len(CRITERIA):
        sys.exit(f"need {len(CRITERIA)} scores in rubric order, '-' for not scored")
    scores = [None if a == "-" else float(a) for a in args]
    if any(s is not None and not 0 <= s <= 10 for s in scores):
        sys.exit("scores are 0-10")
    if all(s is None for s in scores):
        sys.exit("nothing scored")

    scored_weight = sum(w for (_, w), s in zip(CRITERIA, scores) if s is not None)
    total = round(sum(w * s for (_, w), s in zip(CRITERIA, scores) if s is not None) / scored_weight, 1)
    provisional = scores[-1] is None
    low = [n for (n, _), s in zip(CRITERIA, scores) if s is not None and s < 5]

    print("| # | Criterion | Weight | Score | Points | Gain at 8 |")
    print("|---|---|---|---|---|---|")
    for i, ((name, w), s) in enumerate(zip(CRITERIA, scores), 1):
        if s is None:
            print(f"| {i} | {name} | {w} | not scored | - | - |")
            continue
        gain = max(0.0, w * (TARGET - s) / scored_weight)
        print(f"| {i} | {name} | {w} | {s:g} | {w * s / scored_weight:.2f} | +{gain:.2f} |")

    if total >= 9.0 and not low:
        verdict = "Ready on content. Send the video to finish" if provisional else "Ready for the stage"
    elif total >= 8.0 and not low:
        verdict = "Accepted level. The talk can be accepted; work with the speaking coach to reach 9.0 before the stage"
    elif total >= 6.0:
        verdict = "Close"
    else:
        verdict = "Rework"
    note = " (provisional: English delivery not scored)" if provisional else ""
    print(f"\nTotal: {total} / 10 - {verdict}{note}")
    if low:
        print("Below 5: " + ", ".join(low))
    print(f"\nSPEAKER SCORE: {total}/10")


if __name__ == "__main__":
    main(sys.argv[1:])
