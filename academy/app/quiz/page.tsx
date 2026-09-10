"use client";

import Link from "next/link";
import { useI18n } from "@/lib/i18n";
import outline from "@/data/outline.json";

export default function QuizIndex() {
  const { lang, t } = useI18n();
  return (
    <div className="mx-auto max-w-5xl px-5 py-10">
      <h1 className="font-sans text-2xl font-semibold">{t.quizTitle}</h1>
      <p className="mt-2 max-w-2xl text-[var(--ust-muted)]">{t.quizLead}</p>
      <div className="mt-8 grid gap-4 sm:grid-cols-2">
        <Link
          href="/quiz/run?mode=practice"
          className="rounded-xl border border-[var(--border)] bg-white p-5 no-underline"
        >
          <div className="text-lg font-semibold text-[var(--ust-teal-deep)]">
            {t.practice20}
          </div>
        </Link>
        <Link
          href="/quiz/run?mode=exam"
          className="rounded-xl border border-[var(--border)] bg-white p-5 no-underline"
        >
          <div className="text-lg font-semibold text-[var(--ust-teal-deep)]">
            {t.exam25}
          </div>
        </Link>
      </div>
      <h2 className="mt-12 text-lg">{t.byModule}</h2>
      <ul className="mt-3 grid gap-2 sm:grid-cols-2">
        {outline.modules.map((m) => (
          <li key={m.id}>
            <Link
              href={`/quiz/run?mode=module&module=${m.id}`}
              className="block rounded-lg border border-[var(--border)] bg-white px-4 py-3 no-underline"
            >
              M{m.id} · {lang === "es" ? m.title_es : m.title_en}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
