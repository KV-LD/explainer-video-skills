"use client";

import Link from "next/link";
import { useMemo, useState } from "react";
import { useI18n } from "@/lib/i18n";
import {
  isCorrect,
  sampleModule,
  samplePractice,
  sampleWeighted,
  type Domain,
} from "@/lib/quiz";

function seedNow() {
  return Date.now() % 2147483647;
}

export function QuizClient({
  mode,
  moduleId,
}: {
  mode: string;
  moduleId?: string;
}) {
  const { lang, t } = useI18n();
  const [seed, setSeed] = useState(seedNow);
  const questions = useMemo(() => {
    if (mode === "exam") return sampleWeighted(25, seed);
    if (mode === "module" && moduleId) return sampleModule(moduleId, seed);
    return samplePractice(20, seed);
  }, [mode, moduleId, seed]);

  const [idx, setIdx] = useState(0);
  const [chosen, setChosen] = useState<Record<string, number[]>>({});
  const [done, setDone] = useState(false);

  const q = questions[idx];
  const loc = q ? q[lang] : null;
  const need = q ? q.select : 1;

  function toggle(i: number) {
    if (!q) return;
    setChosen((prev) => {
      const cur = prev[q.id] || [];
      if (need === 1) {
        return { ...prev, [q.id]: [i] };
      }
      const set = new Set(cur);
      if (set.has(i)) {
        set.delete(i);
      } else if (set.size < need) {
        set.add(i);
      } else {
        const rest = [...set].filter((x) => x !== i);
        rest.shift();
        set.clear();
        rest.forEach((x) => set.add(x));
        set.add(i);
      }
      return { ...prev, [q.id]: [...set].sort((a, b) => a - b) };
    });
  }

  function results() {
    const by: Record<string, { ok: number; n: number }> = {};
    let ok = 0;
    for (const item of questions) {
      const d = item.domain;
      by[d] = by[d] || { ok: 0, n: 0 };
      by[d].n += 1;
      if (isCorrect(item, chosen[item.id] || [])) {
        ok += 1;
        by[d].ok += 1;
      }
    }
    const strong: Domain[] = [];
    const weak: Domain[] = [];
    (Object.keys(by) as Domain[]).forEach((d) => {
      const r = by[d].ok / by[d].n;
      if (r >= 0.75) strong.push(d);
      else if (r < 0.6) weak.push(d);
    });
    return { ok, total: questions.length, by, strong, weak };
  }

  if (!q || !loc) return null;

  if (done) {
    const r = results();
    const pct = Math.round((r.ok / r.total) * 100);
    return (
      <div className="mx-auto max-w-3xl px-5 py-10">
        <h1 className="text-2xl font-semibold">
          {t.score}: {r.ok}/{r.total} ({pct}%)
        </h1>
        <div className="mt-6 space-y-4">
          {r.strong.length > 0 && (
            <div className="rounded-lg border border-[var(--border)] bg-white p-4">
              <div className="text-[10px] font-bold uppercase tracking-[0.12em] text-[var(--ust-green)]">
                {t.strong}
              </div>
              <ul className="mt-2 list-disc pl-5 text-[var(--ust-muted)]">
                {r.strong.map((d) => (
                  <li key={d}>{t.domains[d]}</li>
                ))}
              </ul>
              <p className="mt-2 text-sm">{t.wellDone}</p>
            </div>
          )}
          {r.weak.length > 0 && (
            <div className="rounded-lg border border-[var(--border)] bg-white p-4">
              <div className="text-[10px] font-bold uppercase tracking-[0.12em] text-[var(--ust-coral)]">
                {t.weak}
              </div>
              <ul className="mt-2 list-disc pl-5 text-[var(--ust-muted)]">
                {r.weak.map((d) => (
                  <li key={d}>{t.domains[d]}</li>
                ))}
              </ul>
              <p className="mt-2 text-sm">{t.studyHint}</p>
              <Link href="/notes" className="mt-2 inline-block text-sm">
                {t.reviewNotes}
              </Link>
            </div>
          )}
        </div>
        <h2 className="mt-10 text-lg font-bold">{t.question}</h2>
        <ol className="mt-4 space-y-6">
          {questions.map((item) => {
            const L = item[lang];
            const good = isCorrect(item, chosen[item.id] || []);
            return (
              <li key={item.id} className="rounded-lg bg-white p-4">
                <div
                  className={`text-xs font-bold ${good ? "text-[var(--ust-green)]" : "text-[var(--ust-coral)]"}`}
                >
                  {good ? "✓" : "✗"} · {t.domains[item.domain]}
                </div>
                <p className="mt-1 font-medium">{L.stem}</p>
                <p className="mt-2 text-sm text-[var(--ust-muted)]">{L.why}</p>
              </li>
            );
          })}
        </ol>
        <button
          type="button"
          className="mt-8 rounded bg-[var(--ust-dark-teal)] px-4 py-2 text-sm font-semibold text-white"
          onClick={() => {
            setSeed(seedNow());
            setIdx(0);
            setChosen({});
            setDone(false);
          }}
        >
          {t.retry}
        </button>
      </div>
    );
  }

  const selected = chosen[q.id] || [];
  const canNext = selected.length === need;
  const inputType = need === 1 ? "radio" : "checkbox";

  return (
    <div className="mx-auto max-w-3xl px-5 py-10">
      <div className="text-[10px] font-bold uppercase tracking-[0.12em] text-[var(--ust-muted2)]">
        {t.progress} · {idx + 1} {t.of} {questions.length} · {t.domains[q.domain]}
      </div>
      <div className="mt-2 h-1.5 overflow-hidden rounded bg-white">
        <div
          className="h-full bg-[var(--ust-dark-teal)]"
          style={{ width: `${((idx + 1) / questions.length) * 100}%` }}
        />
      </div>
      <h1 className="mt-6 text-xl font-semibold leading-snug">
        {t.question} {idx + 1}. {loc.stem}
      </h1>
      <p
        className={`mt-3 rounded-md px-3 py-2 text-sm ${
          need > 1
            ? "bg-white text-[var(--ust-teal-deep)] ring-1 ring-[var(--ust-light-teal)]"
            : "text-[var(--ust-muted2)]"
        }`}
      >
        {need === 1
          ? t.selectOne
          : t.selectN
              .replace("{n}", String(need))
              .replace("{have}", String(selected.length))}
      </p>
      <ul className="mt-6 space-y-2" role={need === 1 ? "radiogroup" : "group"}>
        {loc.options.map((opt, i) => {
          const on = selected.includes(i);
          const letter = String.fromCharCode(65 + i);
          return (
            <li key={`${q.id}-${i}`}>
              <label
                className={`flex cursor-pointer items-start gap-3 rounded-lg border px-4 py-3 text-left text-sm ${
                  on
                    ? "border-[var(--ust-dark-teal)] bg-white ring-2 ring-[var(--ust-light-teal)]"
                    : "border-[var(--border)] bg-white hover:border-[var(--ust-light-teal)]"
                }`}
              >
                <input
                  className="mt-1 shrink-0"
                  type={inputType}
                  name={q.id}
                  value={i}
                  checked={on}
                  onChange={() => toggle(i)}
                />
                <span>
                  <span className="mr-2 font-bold text-[var(--ust-dark-teal)]">
                    {letter}.
                  </span>
                  {opt}
                </span>
              </label>
            </li>
          );
        })}
      </ul>
      <div className="mt-8 flex gap-3">
        <button
          type="button"
          disabled={idx === 0}
          className="rounded border border-[var(--border)] bg-white px-4 py-2 text-sm font-semibold disabled:opacity-40"
          onClick={() => setIdx((n) => Math.max(0, n - 1))}
        >
          {t.back}
        </button>
        {idx < questions.length - 1 ? (
          <button
            type="button"
            disabled={!canNext}
            className="rounded bg-[var(--ust-dark-teal)] px-4 py-2 text-sm font-semibold text-white disabled:opacity-40"
            onClick={() => setIdx((n) => n + 1)}
          >
            {t.next}
          </button>
        ) : (
          <button
            type="button"
            disabled={!canNext}
            className="rounded bg-[var(--ust-dark-teal)] px-4 py-2 text-sm font-semibold text-white disabled:opacity-40"
            onClick={() => setDone(true)}
          >
            {t.submit}
          </button>
        )}
      </div>
      {!canNext && (
        <p className="mt-3 text-xs text-[var(--ust-muted2)]">
          {need === 1
            ? t.pickAnswer
            : t.pickAnswers
                .replace("{n}", String(need))
                .replace("{have}", String(selected.length))}
        </p>
      )}
    </div>
  );
}
