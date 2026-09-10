# Chapter JSON spec

Write one file per chapter: `/workspace/ccd-notes/content/M{module}-C{chapter}.json`

It MUST be a JSON **array of two objects**: English first, Spanish (es-ES, tú/vosotros) second.

Schema per object:
```
{
  "lang": "en" | "es",
  "module_id": "01",
  "chapter_id": "01",
  "eyebrow": "Module 01 · Chapter 01 · 3 August 2026",
  "chapter_title": "...",
  "subtitle": "Claude Certified Developer, Foundation (CCDV-F) · UST masterclass",
  "meta": "Session N of 12 · English notes",
  "running_header": "UST CCD Foundation · M01 · C01 · EN",
  "blocks": [ ... ]
}
```

Block types: lead, h2, h3, p, ul, ol, card (title + blocks), callout (kind: note|warn|success, title, html), table (headers, rows), links (heading, items[{title,url,note}]).

In `p`/`lead`/`callout.html`/`ul items`/`td`, simple HTML is allowed: `<strong>`, `<em>`, `<a href="https://...">`.

Quality bar:
- Highly detailed teaching notes, not a transcript dump and not a thin summary.
- Skip filler (hello, screen share, mute).
- Keep product names in English (Claude, Cowork, Claude Code, MCP, RAG, Skilljar).
- Spanish is Spain (es-ES): vosotros, ordenador/portátil, not Latin American ustedes as default.
- Every chapter ends with a `links` block using real URLs from `/workspace/ccd-notes/ANTHROPIC-LINKS.md`.
- Include a callout when the live class UI may have changed; tell readers to trust docs.claude.com.
- Tables where they help (products, cert tracks, permission modes).
- 4–8 h2 sections per chapter.
