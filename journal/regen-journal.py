#!/usr/bin/env python3
"""Regenerate Rook's journal read-online HTML in the library page from the journal files."""
import glob
import os
import re

JOURNAL_DIR = "/home/hatch/workspace/journal"
INDEX = "/home/hatch/workspace/library/index.html"


def inline(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


def convert(lines):
    out = []
    buf = []

    def flush_p():
        if buf:
            out.append("<p>" + inline(" ".join(buf).strip()) + "</p>")
            buf.clear()

    for ln in lines:
        s = ln.strip()
        if not s:
            flush_p(); continue
        if s == "---":
            flush_p(); out.append("<hr>"); continue
        if s.startswith("## "):
            flush_p(); out.append("<h2>" + inline(s[3:].strip()) + "</h2>"); continue
        if s.startswith("# "):
            flush_p(); out.append("<h1>" + inline(s[2:].strip()) + "</h1>"); continue
        buf.append(s)
    flush_p()
    return out


def main():
    body = []
    for path in sorted(glob.glob(os.path.join(JOURNAL_DIR, "????-??-??.md"))):
        with open(path, encoding="utf-8") as f:
            body.extend(convert(f.read().splitlines()))

    with open(INDEX, encoding="utf-8") as f:
        html = f.read().splitlines()

    start = next(i for i, l in enumerate(html) if '<main class="book" id="journal">' in l)
    end = next(i for i, l in enumerate(html) if i > start and l.strip() == "</main>")
    new_block = [html[start]] + body + [html[end]]
    html[start:end + 1] = new_block

    with open(INDEX, "w", encoding="utf-8") as f:
        f.write("\n".join(html) + "\n")
    print("journal block replaced: lines %d-%d, %d content lines" % (start + 1, end + 1, len(body)))


if __name__ == "__main__":
    main()
