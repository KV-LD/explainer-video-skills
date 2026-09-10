"use client";

import Link from "next/link";
import { useI18n } from "@/lib/i18n";

export default function HomePage() {
  const { t } = useI18n();
  return (
    <div className="mx-auto max-w-5xl px-5 py-14">
      <p className="text-[10px] font-bold uppercase tracking-[0.14em] text-[var(--ust-muted2)]">
        {t.academy}
      </p>
      <h1 className="mt-2 font-sans text-3xl font-semibold tracking-tight">
        {t.hub}
      </h1>
      <p className="mt-3 max-w-2xl text-[var(--ust-muted)]">{t.tagline}</p>
      <div className="mt-8 grid gap-4 sm:grid-cols-3">
        <Link
          href="/notes"
          className="rounded-xl border border-[var(--border)] bg-white p-5 no-underline shadow-sm hover:shadow-md"
        >
          <div className="text-[10px] font-bold uppercase tracking-[0.12em] text-[var(--ust-muted2)]">
            01
          </div>
          <div className="mt-2 text-lg font-semibold text-[var(--ust-teal-deep)]">
            {t.startNotes}
          </div>
        </Link>
        <Link
          href="/quiz"
          className="rounded-xl border border-[var(--border)] bg-white p-5 no-underline shadow-sm hover:shadow-md"
        >
          <div className="text-[10px] font-bold uppercase tracking-[0.12em] text-[var(--ust-muted2)]">
            02
          </div>
          <div className="mt-2 text-lg font-semibold text-[var(--ust-teal-deep)]">
            {t.startQuiz}
          </div>
        </Link>
        <Link
          href="/videos"
          className="rounded-xl border border-[var(--border)] bg-white p-5 no-underline shadow-sm hover:shadow-md"
        >
          <div className="text-[10px] font-bold uppercase tracking-[0.12em] text-[var(--ust-muted2)]">
            03
          </div>
          <div className="mt-2 text-lg font-semibold text-[var(--ust-teal-deep)]">
            {t.startVideos}
          </div>
        </Link>
      </div>
      <p className="mt-10 max-w-2xl text-sm text-[var(--ust-muted2)]">
        {t.disclaimer}
      </p>
    </div>
  );
}
