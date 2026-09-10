# UST Brand Tokens — Colors & Typography

Source: [brand.ust.com/color](https://brand.ust.com/color) and [brand.ust.com/typography](https://brand.ust.com/typography).

## Primary palette

| Token | Hex | RGB | Usage |
|-------|-----|-----|-------|
| Dark Teal | `#006E74` | 0, 110, 116 | Primary brand, top bars, links, CTAs, progress fills |
| Light Teal | `#0097AC` | 0, 151, 172 | Accents, hover states, gradients, focus rings |
| Teal Deep | `#004851` | 0, 72, 81 | Deep backgrounds, strong emphasis text |
| Soft Black | `#231F20` | 35, 31, 32 | Body text, headings (never pure `#000`) |
| White | `#FFFFFF` | 255, 255, 255 | Cards, deck surface, text on dark teal |
| Off White | `#EEF6F7` | 238, 246, 247 | Content area background |

## Secondary / semantic accents

Use sparingly for status, quadrants, and data viz — not as primary UI chrome.

| Token | Hex | Usage |
|-------|-----|-------|
| Green | `#0a9b72` | Success, positive metrics |
| Coral | `#e0604a` | Warning, alert, negative emphasis |
| Warm | `#c75b45` | Secondary warm accent |

## Derived tokens

```css
--ust-muted: rgba(35, 31, 32, 0.72);   /* body secondary text */
--ust-muted2: rgba(35, 31, 32, 0.55);  /* labels, captions */
--border: rgba(0, 110, 116, 0.18);
--border-strong: rgba(0, 151, 172, 0.35);
```

## Layout

**Default for documents and reference pages** (full screen, split layout):

- `body` background fills the viewport: `var(--ust-off)` — no floating inner card/box
- **Page title only**: `.page-head` — `max-width: 52rem`, left-aligned (eyebrow, `h1`, subtitle, meta)
- **All body content**: `.full-band` — `width: 100%` with edge padding only; leads, tabs, legends, tables, callouts, footer
- Page vertical padding on `body`; horizontal padding via `--page-pad-x: clamp(20px, 4vw, 40px)`

**Optional for slide decks only**: teal gradient shell, ambient orbs, centered deck chrome — use only when the user explicitly wants a presentation deck.

## Background treatments

- **Document pages**: flat `var(--ust-off)` full-screen background
- **Slide deck shell** (optional): `linear-gradient(165deg, var(--ust-teal-deep) 0%, var(--ust-dark-teal) 45%, #003840 100%)`
- **Cards on documents**: `var(--ust-white)` with `var(--border)`
- **Card hover**: `box-shadow: 0 8px 28px rgba(0, 110, 116, 0.08)`

## Typography

UST licensed fonts live on the brand portal. For standalone HTML decks, use these **approved Google Font substitutes**:

| Role | CSS variable | Stack | Weights |
|------|--------------|-------|---------|
| Display / headings | `--font-display` | `"Source Serif 4", Georgia, "Times New Roman", serif` | 400, 600, 700 |
| Body / UI | `--font-body` | `"Source Sans 3", system-ui, -apple-system, sans-serif` | 400, 500, 600, 700 |

### Google Fonts link

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&display=swap" rel="stylesheet">
```

### Type scale

| Element | Font | Size | Weight | Notes |
|---------|------|------|--------|-------|
| Page title (`h1`) | body | `1.5rem` | 600 | Plain — no italic, line breaks, or display-serif styling |
| Section title (`h2`) | display | `clamp(1.12rem, 2.35vw, 1.42rem)` | 700 | `letter-spacing: -0.02em` |
| Section label | body | `10px` | 700 | uppercase, `letter-spacing: 0.12em`, `--ust-muted2` |
| Card title | display | `15px` | 700 | |
| Body / card desc | body | `15px` | 400 | `line-height: 1.62`, `--ust-muted`, left-aligned |
| Links | body | inherit | 600 | `color: var(--ust-dark-teal)` |

### Rules

- Page title (`h1`) → `var(--font-body)`, plain single line, no decorative markup (`<em>`, `<br>`)
- Section headings (`h2`+) and card titles → `var(--font-display)`
- Body, buttons, nav, tables → `var(--font-body)`
- Never use dark-theme palettes, neon accents, or unrelated font families (Fraunces, IBM Plex, Spline Sans, Inter-only stacks, etc.)
- Set `color-scheme: light` on `:root`
- Enable `-webkit-font-smoothing: antialiased` on `body`

## Logo colors

Logo approved colors: soft black (`#231F20`) and white only.
