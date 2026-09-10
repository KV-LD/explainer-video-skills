import { notFound } from "next/navigation";
import { chapterExists, getChapter, getOutline } from "@/lib/notes";
import { ChapterView } from "./ui";

export function generateStaticParams() {
  const params: { module: string; chapter: string }[] = [];
  for (const m of getOutline().modules) {
    for (const c of m.chapters) {
      params.push({ module: m.id, chapter: c.id });
    }
  }
  return params;
}

export default async function ChapterPage({
  params,
}: {
  params: Promise<{ module: string; chapter: string }>;
}) {
  const { module, chapter } = await params;
  if (!chapterExists(module, chapter)) notFound();
  const docs = getChapter(module, chapter);
  return <ChapterView moduleId={module} chapterId={chapter} docs={docs} />;
}
