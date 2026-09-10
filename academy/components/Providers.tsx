"use client";

import { Header, Footer } from "@/components/Chrome";
import { I18nProvider } from "@/lib/i18n";
import { Analytics } from "@vercel/analytics/react";

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <I18nProvider>
      <Header />
      <main className="min-h-[70vh]">{children}</main>
      <Footer />
      <Analytics />
    </I18nProvider>
  );
}
