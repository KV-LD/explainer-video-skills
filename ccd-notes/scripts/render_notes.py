#!/usr/bin/env python3
"""Render UST-branded chapter PDFs from JSON content files."""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

from weasyprint import CSS, HTML

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
OUT = ROOT / "pdf"
CSS_PATH = ROOT / "templates" / "ust-notes.css"

FONT_LINK = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&display=swap" rel="stylesheet">
"""


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def render_block(b: dict) -> str:
    t = b.get("type")
    if t == "lead":
        return f'<p class="lead">{b["html"]}</p>'
    if t == "h2":
        return f"<h2>{esc(b['text'])}</h2>"
    if t == "h3":
        return f"<h3>{esc(b['text'])}</h3>"
    if t == "p":
        return f"<p>{b['html']}</p>"
    if t == "ul":
        items = "".join(f"<li>{i}</li>" for i in b["items"])
        return f"<ul>{items}</ul>"
    if t == "ol":
        items = "".join(f"<li>{i}</li>" for i in b["items"])
        return f"<ol>{items}</ol>"
    if t == "card":
        body = "".join(render_block(x) for x in b.get("blocks", []))
        title = f"<h3>{esc(b['title'])}</h3>" if b.get("title") else ""
        return f'<div class="card">{title}{body}</div>'
    if t == "callout":
        kind = b.get("kind", "note")
        label = esc(b.get("title") or {"note": "Note", "warn": "Watch", "success": "Remember"}.get(kind, "Note"))
        return f'<div class="callout {kind}"><div class="label">{label}</div><p>{b["html"]}</p></div>'
    if t == "table":
        heads = "".join(f"<th>{esc(h)}</th>" for h in b["headers"])
        rows = ""
        for row in b["rows"]:
            cells = "".join(f"<td>{c}</td>" for c in row)
            rows += f"<tr>{cells}</tr>"
        return f"<table><thead><tr>{heads}</tr></thead><tbody>{rows}</tbody></table>"
    if t == "links":
        lis = ""
        for it in b["items"]:
            note = f"<div>{it.get('note','')}</div>" if it.get("note") else ""
            lis += (
                f'<li><a href="{esc(it["url"])}">{esc(it["title"])}</a>'
                f'<span class="url">{esc(it["url"])}</span>{note}</li>'
            )
        return f'<h2>{esc(b.get("heading") or "Official documentation")}</h2><ul class="links">{lis}</ul>'
    return ""


def document_html(doc: dict) -> str:
    lang = doc["lang"]
    footer = doc.get(
        "footer",
        "Study notes distilled from the UST CCD Foundation masterclass. "
        "Prefer Anthropic’s current docs over session anecdotes. Not official exam material.",
    )
    blocks = "".join(render_block(b) for b in doc["blocks"])
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
{FONT_LINK}
<title>{esc(doc['chapter_title'])}</title>
</head>
<body>
<div class="running-header">{esc(doc.get('running_header') or doc['eyebrow'])}</div>
<header class="page-head">
  <p class="eyebrow">{esc(doc['eyebrow'])}</p>
  <h1>{esc(doc['chapter_title'])}</h1>
  <p class="subtitle">{esc(doc.get('subtitle', ''))}</p>
  <p class="meta"><span class="lang-pill">{esc(lang.upper())}</span>{esc(doc.get('meta', ''))}</p>
</header>
<main class="full-band">
{blocks}
<p class="footer-note">{esc(footer)}</p>
</main>
</body>
</html>
"""


def slugify(s: str) -> str:
    keep = []
    for ch in s.lower():
        if ch.isalnum():
            keep.append(ch)
        elif ch in " -_/" and (not keep or keep[-1] != "-"):
            keep.append("-")
    return "".join(keep).strip("-")[:60]


def render_one(path: Path) -> Path:
    data = json.loads(path.read_text())
    docs = data if isinstance(data, list) else [data]
    written = []
    css = CSS(filename=str(CSS_PATH))
    for doc in docs:
        html_str = document_html(doc)
        lang = doc["lang"]
        mid = doc["module_id"]
        cid = doc["chapter_id"]
        name = f"M{mid}-C{cid}-{lang}-{slugify(doc['chapter_title'])}.pdf"
        dest_dir = OUT / f"module-{mid}-{lang}"
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / name
        HTML(string=html_str, base_url=str(ROOT)).write_pdf(dest, stylesheets=[css])
        written.append(dest)
        print("wrote", dest.relative_to(ROOT), flush=True)
    return written[-1]


def main() -> None:
    files = sorted(CONTENT.glob("*.json"))
    if len(sys.argv) > 1:
        files = [Path(a) for a in sys.argv[1:]]
    if not files:
        print("no json in", CONTENT)
        sys.exit(1)
    for f in files:
        render_one(f)


if __name__ == "__main__":
    main()
