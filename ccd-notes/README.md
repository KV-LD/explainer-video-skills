# CCD Foundation — branded bilingual chapter notes

Study notes from the UST **Claude Certified Developer, Foundation** masterclass (August 2026).

- **English** and **Spanish (es-ES)** are separate PDFs, in separate folders.
- **One PDF per chapter**, UST brand colors/typography from `brand-tokens`.
- Anthropic documentation links are on every chapter.

## Start here

| Language | Index PDF |
|---|---|
| English | [pdf/module-00-en/](pdf/module-00-en/) |
| Español | [pdf/module-00-es/](pdf/module-00-es/) |

Then open `pdf/module-01-en/` or `pdf/module-01-es/` and continue through module 12.

## Layout

```
ccd-notes/
  outline.json          # modules and chapter titles
  content/              # bilingual JSON sources
  pdf/module-NN-en/     # English PDFs
  pdf/module-NN-es/     # Spanish PDFs
  templates/ust-notes.css
  scripts/render_notes.py
```

Re-render:

```bash
python3 ccd-notes/scripts/render_notes.py
```

A 10 August stub recording (~11 min, no teaching) is omitted. Module 04 is the full 10 August afternoon session.

These notes are **not** official Anthropic or Pearson exam materials. Prefer https://docs.claude.com/en/home when a recording is out of date.
