"use client";

import { useSearchParams } from "next/navigation";
import { Suspense } from "react";
import { QuizClient } from "@/components/QuizClient";

function Inner() {
  const sp = useSearchParams();
  const mode = sp.get("mode") || "practice";
  const moduleId = sp.get("module") || undefined;
  return <QuizClient mode={mode} moduleId={moduleId} />;
}

export default function QuizRunPage() {
  return (
    <Suspense fallback={<div className="p-10">…</div>}>
      <Inner />
    </Suspense>
  );
}
