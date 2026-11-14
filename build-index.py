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

SITE = "https://ssutee.github.io/fractional-distillation-lab/"
DESCRIPTION = ("See how a refinery tower sorts crude oil into petrol, jet fuel, diesel and roads. "
               "An interactive lab for Grade 6, in English and Thai.")

# What the artifact viewer normally supplies around the page, plus the tags that
# give the live link a preview card (social-preview.png) when it is shared.
HEAD_START = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="__DESCRIPTION__">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Fractional Distillation Lab">
<meta property="og:title" content="Fractional Distillation Lab">
<meta property="og:description" content="__DESCRIPTION__">
<meta property="og:url" content="__SITE__">
<meta property="og:image" content="__SITE__social-preview.png">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="640">
<meta property="og:image:alt" content="Fractional Distillation Lab: a refinery tower with its fractions, from gases at the top to bitumen at the bottom.">
<meta name="twitter:card" content="summary_large_image">
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
    head_start = HEAD_START.replace("__SITE__", SITE).replace("__DESCRIPTION__", DESCRIPTION)
    page = f"{head_start}{head}\n</head>\n<body>\n{body}\n</body>\n</html>\n"
    TARGET.write_text(page, encoding="utf-8")
    print(f"Wrote {TARGET.name} ({len(page.encode('utf-8')) // 1024} KB)")


if __name__ == "__main__":
    main()
