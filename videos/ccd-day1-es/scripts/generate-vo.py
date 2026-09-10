#!/usr/bin/env python3
"""Generate Spain-Spanish TTS (es-ES-ElviraNeural) per scene and a timings.json."""
from __future__ import annotations

import asyncio
import json
import subprocess
import sys
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
VOICE = "es-ES-ElviraNeural"
RATE = "-8%"


async def synth(text: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    comm = edge_tts.Communicate(text, VOICE, rate=RATE)
    await comm.save(str(dest))


def duration_seconds(path: Path) -> float:
    out = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        text=True,
    )
    return float(out.strip())


async def build(video_id: str) -> None:
    scenes = json.loads((ROOT / "src" / "data" / f"{video_id}.json").read_text())
    audio_dir = PUBLIC / "audio" / video_id
    audio_dir.mkdir(parents=True, exist_ok=True)
    fps = 30
    cursor = 0.0
    out_scenes = []
    pad = 0.35

    for i, scene in enumerate(scenes):
        mp3 = audio_dir / f"{i:02d}-{scene['id']}.mp3"
        print(f"TTS {video_id} {i:02d} {scene['id']}…", flush=True)
        await synth(scene["vo"], mp3)
        dur = duration_seconds(mp3) + pad
        start = cursor
        end = cursor + dur
        out_scenes.append(
            {
                **scene,
                "src": f"audio/{video_id}/{mp3.name}",
                "startSec": round(start, 3),
                "endSec": round(end, 3),
                "durationSec": round(dur, 3),
                "fromFrame": int(round(start * fps)),
                "durationInFrames": max(1, int(round(dur * fps))),
            }
        )
        cursor = end

    total = cursor
    manifest = {
        "fps": fps,
        "width": 1920,
        "height": 1080,
        "durationSec": round(total, 3),
        "durationInFrames": int(round(total * fps)),
        "scenes": out_scenes,
    }
    dest = ROOT / "src" / "data" / f"{video_id}.timings.json"
    dest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    print(f"Wrote {dest} ({manifest['durationSec']}s)", flush=True)


async def main() -> None:
    ids = sys.argv[1:] or ["video01", "video02"]
    for vid in ids:
        await build(vid)


if __name__ == "__main__":
    asyncio.run(main())
