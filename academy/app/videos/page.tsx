"use client";

import { useI18n } from "@/lib/i18n";
import videosFile from "@/data/videos.json";

export default function VideosPage() {
  const { lang, t } = useI18n();
  return (
    <div className="mx-auto max-w-5xl px-5 py-10">
      <h1 className="font-sans text-2xl font-semibold">{t.videosTitle}</h1>
      <p className="mt-2 max-w-2xl text-[var(--ust-muted)]">{t.videosLead}</p>
      <ul className="mt-8 space-y-3">
        {videosFile.videos.map((v) => (
          <li
            key={v.id}
            className="rounded-xl border border-[var(--border)] bg-white p-5"
          >
            <div className="text-[10px] font-bold uppercase tracking-[0.12em] text-[var(--ust-muted2)]">
              M{v.moduleId}
            </div>
            <div className="mt-1 font-semibold text-[var(--ust-teal-deep)]">
              {lang === "es" ? v.title_es : v.title_en}
            </div>
            <p className="mt-1 text-sm text-[var(--ust-muted)]">
              {lang === "es" ? v.note_es : v.note_en}
            </p>
            {v.url ? (
              <a
                className="mt-3 inline-block text-sm"
                href={v.url}
                target="_blank"
                rel="noreferrer"
              >
                {t.openVideo}
              </a>
            ) : (
              <p className="mt-3 text-sm text-[var(--ust-coral)]">{t.missingUrl}</p>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
