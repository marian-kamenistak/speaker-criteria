#!/usr/bin/env python3
"""Print the text and speaker notes of every slide in a .pptx. Standard library only.
Usage: pptx_text.py deck.pptx"""
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"


def paragraphs(xml):
    out = []
    for p in ET.fromstring(xml).iter(A + "p"):
        line = "".join(t.text or "" for t in p.iter(A + "t")).strip()
        if line:
            out.append(line)
    return out


def main(path):
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        slides = sorted(
            (n for n in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
            key=lambda n: int(re.search(r"\d+", n.rsplit("/", 1)[1]).group()),
        )
        for i, name in enumerate(slides, 1):
            print(f"\n=== Slide {i} ===")
            for line in paragraphs(z.read(name)):
                print(line)
            rels = name.replace("slides/", "slides/_rels/") + ".rels"
            if rels not in names:
                continue
            for rel in ET.fromstring(z.read(rels)).iter(REL + "Relationship"):
                if rel.get("Type", "").endswith("/notesSlide"):
                    notes = "ppt/" + rel.get("Target").replace("../", "")
                    lines = [l for l in paragraphs(z.read(notes)) if not l.isdigit()]
                    if lines:
                        print("--- notes ---")
                        print("\n".join(lines))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
