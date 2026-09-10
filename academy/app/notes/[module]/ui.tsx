"use client";

import Link from "next/link";
import { useI18n } from "@/lib/i18n";
import type { OutlineModule } from "@/lib/notes";
import videosFile from "@/data/videos.json";

export function ModuleView({ mod }: { mod: OutlineModule }) {
  const { lang, t } = useI18n();
  const vids = videosFile.videos.filter((v) => v.moduleId === mod.id);
  return (
    <div className="mx-auto max-w-5xl px-5 py-10">
      <Link href="/notes" className="text-sm">
        ← {t.navNotes}
      </Link>
      <p className="mt-4 text-[10px] font-bold uppercase tracking-[0.12em] text-[var(--ust-muted2)]">
        {lang === "es" ? "Módulo" : "Module"} {mod.id} · {mod.date}
      </p>
      <h1 className="mt-1 font-sans text-2xl font-semibold">
        {lang === "es" ? mod.title_es : mod.title_en}
      </h1>
      <h2 className="mt-8 text-lg">{t.chapters}</h2>
      <ol className="mt-3 space-y-2">
        {mod.chapters.map((c) => (
          <li key={c.id}>
            <Link
              href={`/notes/${mod.id}/${c.id}`}
              className="block rounded-lg border border-[var(--border)] bg-white px-4 py-3 no-underline hover:shadow-sm"
            >
              <span className="text-[var(--ust-dark-teal)]">C{c.id}</span>{" "}
              {lang === "es" ? c.title_es : c.title_en}
            </Link>
          </li>
        ))}
      </ol>
      <h2 className="mt-10 text-lg">{t.relatedVideos}</h2>
      <ul className="mt-3 space-y-2">
        {vids.map((v) => (
          <li key={v.id} className="rounded-lg bg-white px-4 py-3">
            {v.url ? (
              <a href={v.url} target="_blank" rel="noreferrer">
                {v.title}
              </a>
            ) : (
              <span className="text-[var(--ust-muted)]">
                {v.title} — {t.addLink}
              </span>
            )}
            <div className="mt-1 text-[10px] font-bold uppercase tracking-[0.12em] text-[var(--ust-muted2)]">
              {t.videoLangBadge}
            </div>
          </li>
        ))}
      </ul>
      <p className="mt-8">
        <Link href={`/quiz/run?mode=module&module=${mod.id}`}>{t.startQuiz}</Link>
      </p>
    </div>
  );
}
