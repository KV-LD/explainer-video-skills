import React from "react";
import {
  AbsoluteFill,
  Audio,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadFont } from "@remotion/google-fonts/Inter";
import video01 from "./data/video01.timings.json";
import video02 from "./data/video02.timings.json";

const { fontFamily } = loadFont("normal", {
  weights: ["500", "600", "700"],
  subsets: ["latin", "latin-ext"],
});

type Scene = {
  id: string;
  beat: string;
  kicker: string;
  title: string;
  points: string[];
  vo: string;
  src: string;
  startSec: number;
  endSec: number;
  durationSec: number;
  fromFrame: number;
  durationInFrames: number;
};

type Manifest = {
  fps: number;
  durationInFrames: number;
  scenes: Scene[];
};

const manifests: Record<string, Manifest> = {
  video01: video01 as Manifest,
  video02: video02 as Manifest,
};

const COLORS: Record<string, string> = {
  problem: "#FF6B4A",
  stakes: "#FF9F0A",
  solution: "#30D158",
  how: "#0A84FF",
  payoff: "#BF5AF2",
};

const BEAT_LABEL: Record<string, string> = {
  problem: "Problema",
  stakes: "Qué os jugáis",
  solution: "La idea",
  how: "Cómo va",
  payoff: "Para llevar",
};

function captionFor(vo: string, localFrame: number, durationInFrames: number): string {
  const parts = vo
    .split(/(?<=[.!?…])\s+/)
    .map((s) => s.trim())
    .filter(Boolean);
  if (parts.length === 0) return "";
  const t = Math.min(0.999, Math.max(0, localFrame / Math.max(1, durationInFrames)));
  const idx = Math.min(parts.length - 1, Math.floor(t * parts.length));
  const line = parts[idx];
  if (line.length <= 84) return line;
  const cut = line.slice(0, 82);
  const sp = cut.lastIndexOf(" ");
  return (sp > 40 ? cut.slice(0, sp) : cut) + "…";
}

const SceneView: React.FC<{ scene: Scene; index: number; total: number }> = ({
  scene,
  index,
  total,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const accent = COLORS[scene.beat] ?? "#0A84FF";
  const enter = spring({
    frame: frame + 10,
    fps,
    config: { damping: 16, stiffness: 120, mass: 0.7 },
  });
  const y = interpolate(enter, [0, 1], [28, 0]);
  const caption = captionFor(scene.vo, frame, scene.durationInFrames);

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#0B0F14",
        fontFamily,
        color: "#F5F7FA",
      }}
    >
      <Audio src={staticFile(scene.src)} />
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "radial-gradient(1200px 600px at 12% -10%, rgba(10,132,255,0.16), transparent 55%), radial-gradient(900px 500px at 100% 110%, rgba(255,107,74,0.12), transparent 50%)",
        }}
      />
      <div
        style={{
          position: "absolute",
          top: 56,
          left: 80,
          right: 80,
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          opacity: 0.9,
        }}
      >
        <div style={{ fontSize: 22, fontWeight: 600, letterSpacing: 0.4, color: "#A8B0BD" }}>
          Claude Certified Developer · Foundation
        </div>
        <div style={{ fontSize: 20, color: "#A8B0BD" }}>
          {String(index + 1).padStart(2, "0")} / {String(total).padStart(2, "0")}
        </div>
      </div>

      <div
        style={{
          position: "absolute",
          top: 118,
          left: 80,
          display: "flex",
          alignItems: "center",
          gap: 14,
          transform: `translateY(${y}px)`,
          opacity: enter,
        }}
      >
        <div
          style={{
            background: accent,
            color: "#0B0F14",
            fontWeight: 700,
            fontSize: 18,
            padding: "8px 14px",
            borderRadius: 8,
            letterSpacing: 0.3,
          }}
        >
          {BEAT_LABEL[scene.beat] ?? scene.beat}
        </div>
        <div style={{ fontSize: 22, color: "#C5CCD6", fontWeight: 500 }}>{scene.kicker}</div>
      </div>

      <div
        style={{
          position: "absolute",
          top: 190,
          left: 80,
          right: 120,
          transform: `translateY(${y}px)`,
          opacity: enter,
        }}
      >
        <h1
          style={{
            margin: 0,
            fontSize: scene.title.length > 42 ? 56 : 64,
            lineHeight: 1.15,
            fontWeight: 700,
            letterSpacing: -0.8,
            maxWidth: 1400,
          }}
        >
          {scene.title}
        </h1>
      </div>

      <div
        style={{
          position: "absolute",
          top: 430,
          left: 80,
          right: 80,
          display: "flex",
          flexDirection: "column",
          gap: 18,
        }}
      >
        {scene.points.map((p, i) => {
          const s = spring({
            frame: frame - 6 - i * 4,
            fps,
            config: { damping: 14, stiffness: 110 },
          });
          return (
            <div
              key={p}
              style={{
                display: "flex",
                alignItems: "center",
                gap: 16,
                opacity: s,
                transform: `translateX(${interpolate(s, [0, 1], [24, 0])}px)`,
              }}
            >
              <div
                style={{
                  width: 12,
                  height: 12,
                  borderRadius: 12,
                  background: accent,
                  flexShrink: 0,
                }}
              />
              <div style={{ fontSize: 32, fontWeight: 500, color: "#E8ECF1" }}>{p}</div>
            </div>
          );
        })}
      </div>

      <div
        style={{
          position: "absolute",
          left: 80,
          right: 80,
          bottom: 72,
          minHeight: 88,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <div
          style={{
            background: "rgba(11,15,20,0.82)",
            border: "1px solid rgba(255,255,255,0.12)",
            borderRadius: 16,
            padding: "16px 28px",
            maxWidth: 1600,
            textAlign: "center",
            fontSize: 28,
            fontWeight: 600,
            lineHeight: 1.35,
            color: "#F5F7FA",
          }}
        >
          {caption}
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const Explainer: React.FC<{ videoId: string }> = ({ videoId }) => {
  const manifest = manifests[videoId];
  if (!manifest) {
    throw new Error(`Unknown videoId ${videoId}`);
  }
  return (
    <AbsoluteFill style={{ background: "#0B0F14" }}>
      {manifest.scenes.map((scene, i) => (
        <Sequence
          key={scene.id}
          from={scene.fromFrame}
          durationInFrames={scene.durationInFrames}
          name={scene.title}
        >
          <SceneView scene={scene} index={i} total={manifest.scenes.length} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
