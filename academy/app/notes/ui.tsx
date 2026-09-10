"use client";

import Link from "next/link";
import { useI18n } from "@/lib/i18n";
import type { OutlineModule } from "@/lib/notes";

export function NotesIndex({ modules }: { modules: OutlineModule[] }) {
  const { lang, t } = useI18n();
  return (
    <div className="mx-auto max-w-5xl px-5 py-10">
      <h1 className="font-sans text-2xl font-semibold">{t.modulesTitle}</h1>
      <p className="mt-2 max-w-2xl text-[var(--ust-muted)]">{t.modulesLead}</p>
      <ol className="mt-8 space-y-4">
        {modules.map((m) => (
          <li key={m.id}>
            <Link
              href={`/notes/${m.id}`}
              className="block rounded-xl border border-[var(--border)] bg-white p-5 no-underline hover:shadow-md"
            >
              <div className="text-[10px] font-bold uppercase tracking-[0.12em] text-[var(--ust-dark-teal)]">
                {lang === "es" ? "Módulo" : "Module"} {m.id} · {m.date}
              </div>
              <div className="mt-1 text-lg font-semibold text-[var(--ust-teal-deep)]">
                {lang === "es" ? m.title_es : m.title_en}
              </div>
              <div className="mt-1 text-sm text-[var(--ust-muted2)]">
                {m.chapters.length} {t.chapters}
              </div>
            </Link>
          </li>
        ))}
      </ol>
    </div>
  );
}
