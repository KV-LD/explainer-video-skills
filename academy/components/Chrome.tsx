"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useI18n } from "@/lib/i18n";

export function Header() {
  const { lang, setLang, t } = useI18n();
  const path = usePathname();
  const item = (href: string, label: string) => (
    <Link
      href={href}
      className={`text-sm font-semibold ${
        path === href || path.startsWith(href + "/")
          ? "text-white"
          : "text-white/80 hover:text-white"
      }`}
    >
      {label}
    </Link>
  );

  return (
    <header className="bg-[var(--ust-teal-deep)] text-white">
      <div className="mx-auto flex max-w-5xl items-center justify-between gap-4 px-5 py-3">
        <Link href="/" className="text-white no-underline">
          <div className="text-[10px] font-bold uppercase tracking-[0.14em] text-white/70">
            {t.academy}
          </div>
          <div className="text-sm font-semibold">{t.hub}</div>
        </Link>
        <nav className="flex items-center gap-5">
          {item("/notes", t.navNotes)}
          {item("/quiz", t.navQuiz)}
          {item("/videos", t.navVideos)}
          <div className="ml-2 flex overflow-hidden rounded border border-white/30 text-xs font-bold">
            <button
              type="button"
              className={`px-2 py-1 ${lang === "en" ? "bg-white text-[var(--ust-teal-deep)]" : "text-white"}`}
              onClick={() => setLang("en")}
            >
              EN
            </button>
            <button
              type="button"
              className={`px-2 py-1 ${lang === "es" ? "bg-white text-[var(--ust-teal-deep)]" : "text-white"}`}
              onClick={() => setLang("es")}
            >
              ES
            </button>
          </div>
        </nav>
      </div>
    </header>
  );
}

export function Footer() {
  const { t } = useI18n();
  return (
    <footer className="mt-16 border-t border-[var(--border)] px-5 py-8 text-center text-xs text-[var(--ust-muted2)]">
      {t.footer}
    </footer>
  );
}
