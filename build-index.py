#!/usr/bin/env python3
"""Build index.html for GitHub Pages from fractional-distillation.html.

fractional-distillation.html is the Claude artifact version of the lab. The
artifact viewer wraps it in a document skeleton (doctype, charset, viewport,
a few base styles), so the file itself has none. This script adds that
skeleton and writes a standalone index.html that works on any web host.

Run it again after every change to fractional-distillation.html:

    python3 build-index.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "fractional-distillation.html"
TARGET = HERE / "index.html"

# What the artifact viewer normally supplies around the page.
HEAD_START = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Interactive crude oil fractional distillation lab for Grade 6, in English and Thai.">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
</style>
"""


def main() -> None:
    src = SOURCE.read_text(encoding="utf-8")
    # The title, meta tags, font links and the main <style> block belong in <head>;
    # everything after the first </style> is page content and scripts.
    cut = src.index("</style>") + len("</style>")
    head, body = src[:cut].strip(), src[cut:].strip()
    page = f"{HEAD_START}{head}\n</head>\n<body>\n{body}\n</body>\n</html>\n"
    TARGET.write_text(page, encoding="utf-8")
    print(f"Wrote {TARGET.name} ({len(page.encode('utf-8')) // 1024} KB)")


if __name__ == "__main__":
    main()
