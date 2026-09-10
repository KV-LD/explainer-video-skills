"use client";

import { createContext, useContext, useEffect, useMemo, useState } from "react";
import { copy, type Lang } from "./copy";

type Copy = (typeof copy)[Lang];

const Ctx = createContext<{
  lang: Lang;
  setLang: (l: Lang) => void;
  t: Copy;
} | null>(null);

export function I18nProvider({ children }: { children: React.ReactNode }) {
  const [lang, setLangState] = useState<Lang>("en");

  useEffect(() => {
    const saved = window.localStorage.getItem("gam-lang");
    if (saved === "en" || saved === "es") setLangState(saved);
  }, []);

  const setLang = (l: Lang) => {
    setLangState(l);
    window.localStorage.setItem("gam-lang", l);
    document.documentElement.lang = l === "es" ? "es" : "en";
  };

  const value = useMemo(
    () => ({ lang, setLang, t: copy[lang] }),
    [lang]
  );

  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
}

export function useI18n() {
  const ctx = useContext(Ctx);
  if (!ctx) throw new Error("I18nProvider missing");
  return ctx;
}
