# Wrapped Video

Build a "Spotify Wrapped"-style recap: take a row of data about one person, account, team, or year and turn it into a punchy, shareable vertical video. The core pattern is one template × a data table → many personalized videos — write the template once, render a unique film for every row. Built for creators and educators making year-in-review and per-user stat videos.

## When it activates

- "Make a Spotify Wrapped style video" or "build a year-in-review video."
- "Create a personalized data video" or "generate a recap video."
- "Turn a data table into shareable videos" or "make per-user stat videos."
- "Build a wrapped video generator."

## Example prompts

- "Build a Spotify Wrapped style video from this CSV of users."
- "Make a 'your 2026 wrapped' recap with a big-number reveal and a top-5 list."
- "Batch-render a personalized recap video for every row in this data table."

## What's inside

- `SKILL.md` — the data row → one shareable video pattern, the Wrapped scene grammar (big-number reveals, top-X lists, superlatives), a typed schema, the signature count-up counter, 9:16 safe-area framing, and the batch render loop.
- `references/scene-grammar.md` — full 7-scene storyboard with frame timings, crescendo logic, superlative & percentile copy patterns, and the 9:16 safe-area map.
- `references/remotion-recipes.md` — runnable scene components: staggered top-X list, percentile bar, `<Series>` sequencing, transitions, fonts, and the no-flicker rules.
- `references/batch-pipeline.md` — CSV/JSON → many MP4s: schema validation, the render loop, concurrency, Lambda fan-out, and file naming.

---
Part of **[Explainer Video Skills](../)** · Built by **[iart.ai](https://iart.ai)** — the AI motion agent for editable, on-brand motion graphics.
