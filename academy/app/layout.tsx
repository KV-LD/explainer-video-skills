import type { Metadata } from "next";
import { Source_Sans_3, Source_Serif_4 } from "next/font/google";
import { Providers } from "@/components/Providers";
import "./globals.css";

const body = Source_Sans_3({
  subsets: ["latin", "latin-ext"],
  variable: "--font-body",
  weight: ["400", "500", "600", "700"],
});

const display = Source_Serif_4({
  subsets: ["latin", "latin-ext"],
  variable: "--font-display",
  weight: ["400", "600", "700"],
});

export const metadata: Metadata = {
  title: "G.A.Menon Academy · Claude Certification Learning Hub",
  description:
    "CCDV-F notes and quizzes in English and Spanish; session recordings in English (one link per module).",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body className={`${body.variable} ${display.variable} antialiased`}>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
