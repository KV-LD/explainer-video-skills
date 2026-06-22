# Isometric Animation

Build geometric 2.5D isometric scenes — stacked layers, extruded blocks, isometric grids, and exploded-view diagrams — for explainers, UI walkthroughs, and infographics. Depth from consistent axes and per-face shading; motion from revealing structure one layer at a time.

## When it activates

- "Make an isometric animation" or "build a 2.5D isometric scene."
- "Create an isometric infographic" or "show stacked layers / a tech-stack tower."
- "Animate an exploded diagram" that pulls apart and reassembles.
- "Do an isometric city/stack build" or "add a gentle camera drift to an iso scene."

## Example prompts

- "Make an isometric animation of our architecture stack building bottom-up."
- "Animate an exploded diagram of this device, then assemble it."
- "Build a 2.5D isometric infographic with a slow camera drift."

## What's inside

- `SKILL.md` — the projection (true-iso ±30° vs 2:1 dimetric), the `rotateX(60deg) rotateZ(45deg)` iso plane, building scenes (stacked Z layers, extruded blocks with per-face shading, iso grids, exploded views), the motion table (build / explode / drift / parallax / hover), a Three.js `OrthographicCamera` alternative, and the standalone-HTML deliver-and-verify loop.
- `references/isometric-recipes.md` — fuller runnable code: projection math and inverse picking, flat → iso-plane conversion (transform and matrix), extruded-block faces in CSS and SVG, stacked-layer and exploded-view builds, the iso grid, camera drift / parallax / hover, and a complete Three.js orthographic iso scene with a seekable build.

---
Part of **[Explainer Video Skills](../)** · Built by **[iart.ai](https://iart.ai)** — the AI motion agent for editable, on-brand motion graphics.
