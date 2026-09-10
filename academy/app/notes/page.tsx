import { getOutline } from "@/lib/notes";
import { NotesIndex } from "./ui";

export default function NotesPage() {
  const outline = getOutline();
  return <NotesIndex modules={outline.modules} />;
}
