# Whiteboard Animation

The VideoScribe / Doodly look: a hand draws illustrations and handwriting onto a board, stroke by stroke, synced to narration. Built from SVG stroke draw-on plus a marker hand that tracks the drawing tip, with elements revealed in narration order so the board fills up.

## When it activates

- "Make a whiteboard animation" or "do a doodle / scribe video."
- "Draw-on explainer" or "VideoScribe-style" / "hand-drawn explainer video."
- "Animate a sketch being drawn" or "show a hand drawing the illustration."
- "Animate handwriting appearing on a whiteboard."

## Example prompts

- "Make a 30s whiteboard animation explaining how our app works."
- "Animate our logo being drawn by a hand, stroke by stroke."
- "Turn this sketch into a draw-on explainer with handwriting synced to a voiceover."

## What's inside

- `SKILL.md` — the core SVG `stroke-dashoffset` draw-on, a marker hand that follows the path tip via `getPointAtLength`, narration-order reveal, converting art to drawable single-stroke paths, erase/wipe transitions, pacing to VO, and the standalone-HTML deliver-and-verify loop.
- `references/draw-on-recipes.md` — runnable draw-on mechanics: hand-follows-path, GSAP DrawSVG/MotionPath variants, multi-stroke staggering, handwriting, fill-after-outline, erase/reverse-draw, and the Remotion frame-driven port.
- `references/whiteboard-pipeline.md` — art-to-drawable-SVG conversion, draw-order authoring, handwriting/stroke fonts, the marker hand asset and nib calibration, pacing draw time to the VO, and the storyboard-to-board build sequence.

---
Part of **[Explainer Video Skills](../)** · Built by **[iart.ai](https://iart.ai)** — the AI motion agent for editable, on-brand motion graphics.
