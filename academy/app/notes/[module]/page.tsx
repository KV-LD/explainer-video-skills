import { notFound } from "next/navigation";
import { getOutline } from "@/lib/notes";
import { ModuleView } from "./ui";

export function generateStaticParams() {
  return getOutline().modules.map((m) => ({ module: m.id }));
}

export default async function ModulePage({
  params,
}: {
  params: Promise<{ module: string }>;
}) {
  const { module } = await params;
  const m = getOutline().modules.find((x) => x.id === module);
  if (!m) notFound();
  return <ModuleView mod={m} />;
}
