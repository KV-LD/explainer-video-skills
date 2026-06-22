---
name: map-animation
description: This skill should be used when the user asks to "make a Vox-style map animation", "animate a map zoom", "draw a route on a map", "highlight a country/region", "drop pins on a map", "add location labels/callouts", "use Google Earth Studio", or "make a map fly-over for an explainer video". Covers Earth Studio camera moves → After Effects, vector/GeoJSON map motion, pins/routes/highlights/labels, and the 12fps stutter cadence.
version: 0.1.0
---

# Map Animation

Build editorial, Vox-style map motion: a camera that zooms, orbits, and pans over terrain while location pins drop, routes draw on, regions highlight, and labels call out — finished with the signature 12fps "stutter" cadence that makes it read as documentary, not video-game flythrough. Two production paths: photoreal base motion from **Google Earth Studio** composited in After Effects, and data-driven 2D vector maps (GeoJSON/SVG) rendered programmatically with Remotion.

## When to use

- A camera fly-over, zoom-in, or orbit over a real location for an explainer or news piece.
- A route or journey drawing itself across the map (flight path, supply chain, migration).
- Highlighting a country, state, or region and labeling places with callouts.
- Dropping location pins in sequence, synced to narration beats.
- Anything that should read in the "Vox/editorial" map style with the 12fps stutter.

## Pick the path

| Look | Tool | Output | Best for |
|---|---|---|---|
| Photoreal terrain, satellite, 3D cities | Google Earth Studio → After Effects | image sequence + camera `.jsx` | establishing fly-overs, real geography |
| Flat vector, on-brand colors, data-driven | Remotion / SVG + GeoJSON | MP4/GIF from code | routes, highlights, pins from a coords array |
| Hybrid | Earth Studio base + AE/vector overlays | composited MP4 | the full Vox look — real terrain *with* clean graphics on top |

The signature look is almost always **hybrid**: Earth Studio gives the move, the 2D graphics layer (pins/routes/labels) goes on top, and the whole graphics comp runs at 12fps.

## Google Earth Studio → After Effects

Earth Studio is a browser tool that keyframes a camera over Google's 3D globe and exports an **image sequence** plus a camera/track-point **`.jsx`** for After Effects.

1. **Block the move in the browser**: set keyframes for the camera (Latitude, Longitude, Altitude/Distance, Pan, Tilt, Rotation). Keep moves slow and eased — Earth Studio's default is linear; switch keyframe interpolation to **Ease In/Out** so the camera glides and settles instead of sliding to a hard stop.
2. **Add track points** for every place you'll label or pin (right-click a location → add as a 3D track point). These export into the `.jsx` as nulls so 2D graphics stick to the ground as the camera moves.
3. **Export**: set resolution (1080p/4K), frame rate (export at 30fps even if delivering 24 — you'll re-time), and check **"3D Camera Export (.jsx)"** and **"Track Points"**. You get `Footage/####.jpeg` + `Project.jsx`.
4. **Import into AE**: run the `.jsx` (File → Scripts → Run Script File). It builds a comp with the image sequence on a layer, a 3D **camera** matching Earth Studio's move, and a **null per track point** locked to its geographic position.
5. **Parent 2D graphics to the nulls**: a pin or label parented to a track-point null now follows that location across the whole move — it pins to the ground, not the screen.

See `references/earth-studio-to-ae.md` for export settings, the coordinate/altitude fields, re-timing to 24fps, and the null-parenting recipe in detail.

## Vector / GeoJSON map motion (data-driven)

For flat, on-brand maps that animate from data, drive everything off coordinates. A **projection** (e.g. d3-geo `geoMercator`/`geoOrthographic`) turns `[lng, lat]` into screen `[x, y]`; animate the projection's `scale`/`center`/`rotate` to zoom and orbit, and animate SVG paths for routes and region fills.

```jsx
import {geoMercator, geoPath} from 'd3-geo';
import {useCurrentFrame, interpolate} from 'remotion';

// zoom: interpolate the projection scale + recenter on a target lng/lat
const frame = useCurrentFrame();
const scale  = interpolate(frame, [0, 36], [180, 1400], {extrapolateRight: 'clamp'});
const proj   = geoMercator().center([targetLng, targetLat]).scale(scale).translate([960, 540]);
const path   = geoPath(proj);
// <path d={path(countryFeature)} fill="#1b2433" stroke="#33405a" />
```

Because the projection is a pure function of the frame, the zoom, the pins, and the routes all stay locked together. **Pins, routes, and highlights are all driven from the same coordinate arrays** — see below and `references/vector-maps.md`.

## Pins, routes, highlights, labels

- **Pins (drop-on)**: project `[lng, lat]` → `[x, y]`, then animate a quick scale/overshoot drop with a small shadow. Stagger multiple pins so they land one per narration beat, not all at once.
- **Routes (draw-on)**: build the path between coordinates (great-circle via `geoInterpolate` for long hauls, or a curved bezier for editorial flair), then reveal it with `stroke-dashoffset` len→0. A traveling dot at the route head sells motion.
- **Region highlight**: render the GeoJSON feature as a filled path; bring it up with opacity + a subtle stroke draw-on, and dim everything else (focus + context — same color-grammar discipline as diagrams).
- **Labels / callouts**: a leader line from the pin to a text chip; fade/slide the chip in *after* the pin lands. Keep labels on-screen ≥1.0s and avoid collisions by offsetting in screen space.

```jsx
// pin drop driven by a coords array — one entry per place, staggered
const PINS = [{name: 'Kyiv', lng: 30.52, lat: 50.45}, {name: 'Lviv', lng: 24.03, lat: 49.84}];
PINS.map((p, i) => {
  const [x, y] = proj([p.lng, p.lat]);
  const t = spring({frame: frame - i * 8, fps, config: {damping: 12}}); // stagger 8 frames
  return <g transform={`translate(${x},${y}) scale(${t})`}>{/* pin + label */}</g>;
});
```

## The 12fps stutter cadence (signature look)

The Vox/editorial feel comes from animating the **graphics on twos** — effectively 12 distinct poses per second inside a 24fps timeline. The camera/terrain can stay smooth; the *overlay motion* (pins, routes, labels, even the map pan in pure-vector pieces) snaps at 12fps.

- **In After Effects**: set the graphics precomp's frame rate to 12fps (Composition Settings), or apply **Posterize Time** at 12 to the graphics layer/precomp. Keep the Earth Studio footage layer smooth underneath.
- **In Remotion**: quantize the frame before computing overlay motion so values only update every other frame.

```jsx
// snap overlay animation to 12fps inside a 24fps composition
const frame = useCurrentFrame();          // 24fps timeline
const fps   = 24, stutter = 12;
const step  = Math.round(fps / stutter);  // 2
const f12   = Math.floor(frame / step) * step;  // holds each value for 2 frames
const pinScale = spring({frame: f12, fps, config: {damping: 12}});
```

Apply the stutter to overlays only — stuttering the photoreal terrain underneath looks broken, not stylish.

## Output checklist

- Camera move is eased (no linear slides), slow enough to read the geography.
- Pins/routes/highlights all derive from the same coordinate arrays — nothing hand-placed in screen space.
- Routes draw on (dashoffset), regions use focus+context (highlight one, dim the rest).
- Labels land after their pin, stay ≥1.0s, and don't collide.
- Overlay graphics run at the 12fps stutter; terrain stays smooth.
- Color grammar is consistent and meaningful; one type scale for all labels.

## Deliver & verify (rendered stills → MP4)

The data-driven vector path is a Remotion composition — frame-deterministic, so any exact frame renders headlessly with **no seek harness**. Use this tier when the deliverable is an MP4/GIF carrying exact geography (a route must hit the right cities, a highlight must cover the right country). For an Earth Studio + AE comp, the equivalent verify is rendering the same start/mid/end frames out of AE and checking the track-point nulls still pin their labels.

**Output contract:**
- A Remotion project with the composition registered (`<Composition>` + zod `schema` + `defaultProps`), all motion frame-driven (no timers / `Date.now()` / `Math.random()`).
- Map geometry from a checked-in GeoJSON; pins/routes/highlights driven from a coordinates array in props — never hand-placed in pixels.
- Deliverable = the rendered `out/*.mp4` (plus the project, so coordinates/route can be re-rendered).
- Camera zoom/pan and the 12fps stutter both derived from `useCurrentFrame()`; duration data-dependent? compute it in `calculateMetadata`, not by hand.

**Verify loop — render stills → inspect → encode.** Render single frames first (cheap, no encode), inspect them, encode only once the frames are right.

```bash
# Frame-exact stills at start / mid / end — render with the SHIPPED props (real coords), not just defaults
npx remotion still MapAnim out/f-start.png --frame=0   --props='{...}'
npx remotion still MapAnim out/f-mid.png   --frame=N   --props='{...}'   # mid-zoom / route partly drawn
npx remotion still MapAnim out/f-end.png   --frame=L   --props='{...}'   # L = durationInFrames - 1

# Inspect each PNG: the projected pins sit ON their cities (not offset), the route connects the right
# places in order, the highlighted region is the correct country, labels are legible and not colliding,
# and overlays show the 12fps hold while terrain/zoom stays smooth. Then encode:
npx remotion render MapAnim out/map.mp4 --props='{...}'
```

- `npx remotion compositions` reads `durationInFrames`/`fps` to pick the end frame and a mid-zoom frame to sample.
- **Verify ONE representative coordinate set** via stills before batch-rendering many locations — catch a bad projection/center once, not N times.
- **README demo GIF for free**: `npx remotion render MapAnim out/demo.gif --codec=gif`.

**Before you finish:**
1. `npx remotion still` renders cleanly at frame 0, mid-zoom, and last — no errors, no missing GeoJSON/fonts.
2. Every projected pin lands exactly on its coordinate; the route connects the right cities in order; the highlighted feature is the correct region.
3. Camera move is eased and legible; overlays run at the 12fps stutter while terrain/zoom stay smooth.
4. Frame-driven only — no `Date.now()` / `Math.random()` / timers; the **shipped** props (real coords) render correctly, not just `defaultProps`.
5. Labels inside safe areas, ≥1.0s on screen, no collisions; full MP4 encoded and plays; (optional) GIF rendered for the README.

## Reference files

- `references/earth-studio-to-ae.md` — Google Earth Studio camera keyframing, export settings (image sequence + 3D camera `.jsx` + track points), importing the `.jsx` into After Effects, parenting 2D pins/labels to track-point nulls so they stick to the ground, re-timing 30fps exports to a 24fps edit, and applying the 12fps stutter to the graphics layer with Posterize Time.
- `references/vector-maps.md` — GeoJSON/SVG vector map motion: d3-geo projections and frame-driven zoom/orbit, the coordinate-array → pins/routes/highlights/labels recipes (drop-on pins, dashoffset route draw-on with great-circle paths, region highlight with focus+context, collision-aware callouts), and the 12fps stutter quantizer for Remotion.
