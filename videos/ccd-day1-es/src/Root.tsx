import React from "react";
import { Composition } from "remotion";
import { z } from "zod";
import { Explainer } from "./Explainer";
import video01 from "./data/video01.timings.json";
import video02 from "./data/video02.timings.json";

export const explainerSchema = z.object({
  videoId: z.string(),
});

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Video01"
        component={Explainer}
        durationInFrames={video01.durationInFrames}
        fps={video01.fps}
        width={video01.width}
        height={video01.height}
        schema={explainerSchema}
        defaultProps={{ videoId: "video01" }}
      />
      <Composition
        id="Video02"
        component={Explainer}
        durationInFrames={video02.durationInFrames}
        fps={video02.fps}
        width={video02.width}
        height={video02.height}
        schema={explainerSchema}
        defaultProps={{ videoId: "video02" }}
      />
    </>
  );
};
