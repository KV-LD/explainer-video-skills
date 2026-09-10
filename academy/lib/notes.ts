import fs from "fs";
import path from "path";

export type OutlineModule = {
  id: string;
  date: string;
  title_en: string;
  title_es: string;
  chapters: { id: string; title_en: string; title_es: string }[];
};

export type NoteDoc = {
  lang: string;
  module_id: string;
  chapter_id: string;
  eyebrow: string;
  chapter_title: string;
  subtitle: string;
  meta: string;
  blocks: Record<string, unknown>[];
};

const dataDir = path.join(process.cwd(), "data");

export function getOutline(): { modules: OutlineModule[] } {
  return JSON.parse(
    fs.readFileSync(path.join(dataDir, "outline.json"), "utf8")
  );
}

export function getChapter(moduleId: string, chapterId: string): NoteDoc[] {
  const file = path.join(
    dataDir,
    "notes",
    `M${moduleId}-C${chapterId}.json`
  );
  return JSON.parse(fs.readFileSync(file, "utf8"));
}

export function chapterExists(moduleId: string, chapterId: string) {
  return fs.existsSync(
    path.join(dataDir, "notes", `M${moduleId}-C${chapterId}.json`)
  );
}
