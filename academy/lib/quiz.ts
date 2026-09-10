import questions from "../data/questions.json";

export type Domain =
  | "applications"
  | "models"
  | "agents"
  | "prompt"
  | "tools"
  | "security"
  | "claude-code"
  | "eval";

export type Question = {
  id: string;
  domain: Domain;
  module: string;
  type: "single" | "multi";
  select: number;
  en: { stem: string; options: string[]; correct: number[]; why: string };
  es: { stem: string; options: string[]; correct: number[]; why: string };
};

export const BANK = questions as Question[];

const WEIGHT: Record<Domain, number> = {
  applications: 33,
  models: 17,
  agents: 15,
  prompt: 11,
  tools: 11,
  security: 8,
  "claude-code": 3,
  eval: 2,
};

function shuffle<T>(arr: T[], seed: number): T[] {
  const a = [...arr];
  let s = seed || 1;
  for (let i = a.length - 1; i > 0; i--) {
    s = (s * 16807 + 11) % 2147483647;
    const j = s % (i + 1);
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export function samplePractice(n: number, seed: number): Question[] {
  return shuffle(BANK, seed).slice(0, n);
}

export function sampleWeighted(n: number, seed: number): Question[] {
  const by = new Map<Domain, Question[]>();
  for (const q of BANK) {
    by.set(q.domain, [...(by.get(q.domain) || []), q]);
  }
  const picked: Question[] = [];
  const domains = Object.keys(WEIGHT) as Domain[];
  let remaining = n;
  domains.forEach((d, idx) => {
    const want =
      idx === domains.length - 1
        ? remaining
        : Math.max(1, Math.round((WEIGHT[d] / 100) * n));
    const pool = shuffle(by.get(d) || [], seed + idx * 17);
    const take = pool.slice(0, Math.min(want, pool.length, remaining));
    picked.push(...take);
    remaining -= take.length;
  });
  if (remaining > 0) {
    const rest = shuffle(
      BANK.filter((q) => !picked.includes(q)),
      seed + 99
    );
    picked.push(...rest.slice(0, remaining));
  }
  return shuffle(picked, seed + 3).slice(0, n);
}

export function sampleModule(moduleId: string, seed: number): Question[] {
  const pool = BANK.filter((q) => q.module === moduleId);
  const src = pool.length >= 8 ? pool : BANK;
  return shuffle(src, seed).slice(0, Math.min(12, src.length || 12));
}

export function isCorrect(q: Question, chosen: number[]): boolean {
  const a = [...chosen].sort().join(",");
  const b = [...q.en.correct].sort().join(",");
  return a === b;
}
