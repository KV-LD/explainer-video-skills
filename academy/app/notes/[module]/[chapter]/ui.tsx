"use client";

import Link from "next/link";
import { NoteBlocks } from "@/components/NoteBlocks";
import { useI18n } from "@/lib/i18n";
import type { NoteDoc } from "@/lib/notes";

export function ChapterView({
  moduleId,
  chapterId,
  docs,
}: {
  moduleId: string;
  chapterId: string;
  docs: NoteDoc[];
}) {
  const { lang } = useI18n();
  const doc = docs.find((d) => d.lang === lang) || docs[0];
  return (
    <div className="mx-auto max-w-3xl px-5 py-10">
      <Link href={`/notes/${moduleId}`} className="text-sm">
        ← M{moduleId}
      </Link>
      <p className="mt-4 text-[10px] font-bold uppercase tracking-[0.12em] text-[var(--ust-muted2)]">
        {doc.eyebrow}
      </p>
      <h1 className="mt-1 font-sans text-2xl font-semibold">{doc.chapter_title}</h1>
      <p className="mt-2 text-sm text-[var(--ust-muted)]">{doc.subtitle}</p>
      <p className="mt-1 text-xs text-[var(--ust-muted2)]">{doc.meta}</p>
      <div className="mt-8">
        <NoteBlocks blocks={doc.blocks} />
      </div>
      <p className="mt-10 text-sm">
        <Link href={`/quiz/run?mode=module&module=${moduleId}`}>Quiz M{moduleId}</Link>
        {" · "}
        <span>
          C{chapterId}
        </span>
      </p>
    </div>
  );
}
