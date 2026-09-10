"use client";

import { useI18n } from "@/lib/i18n";

type Block = Record<string, unknown>;

function Html({ html }: { html: string }) {
  return <span dangerouslySetInnerHTML={{ __html: html }} />;
}

export function NoteBlocks({ blocks }: { blocks: Block[] }) {
  const { t } = useI18n();
  return (
    <div className="prose-notes space-y-3">
      {blocks.map((b, i) => {
        const type = b.type as string;
        if (type === "lead")
          return (
            <p key={i} className="text-[1.02rem] text-[var(--ust-soft-black)]">
              <Html html={String(b.html)} />
            </p>
          );
        if (type === "h2")
          return (
            <h2 key={i} className="mt-8 text-xl font-bold">
              {String(b.text)}
            </h2>
          );
        if (type === "h3")
          return (
            <h3 key={i} className="mt-5 text-base font-bold">
              {String(b.text)}
            </h3>
          );
        if (type === "p")
          return (
            <p key={i}>
              <Html html={String(b.html)} />
            </p>
          );
        if (type === "ul" || type === "ol") {
          const Tag = type;
          return (
            <Tag key={i}>
              {(b.items as string[]).map((it, j) => (
                <li key={j}>
                  <Html html={it} />
                </li>
              ))}
            </Tag>
          );
        }
        if (type === "callout") {
          const kind = String(b.kind || "note");
          const border =
            kind === "warn"
              ? "border-[var(--ust-coral)]"
              : kind === "success"
                ? "border-[var(--ust-green)]"
                : "border-[var(--ust-dark-teal)]";
          return (
            <div
              key={i}
              className={`rounded-r-lg border-l-4 bg-white px-4 py-3 ${border}`}
            >
              <div className="mb-1 text-[10px] font-bold uppercase tracking-[0.12em] text-[var(--ust-muted2)]">
                {String(b.title || "")}
              </div>
              <p className="mb-0">
                <Html html={String(b.html)} />
              </p>
            </div>
          );
        }
        if (type === "table") {
          return (
            <div key={i} className="overflow-x-auto">
              <table>
                <thead>
                  <tr>
                    {(b.headers as string[]).map((h) => (
                      <th key={h}>{h}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {(b.rows as string[][]).map((row, ri) => (
                    <tr key={ri}>
                      {row.map((c, ci) => (
                        <td key={ci}>
                          <Html html={c} />
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          );
        }
        if (type === "links") {
          return (
            <div key={i}>
              <h2 className="mt-8 text-xl font-bold">
                {String(b.heading || "Docs")}
              </h2>
              <ul>
                {(
                  b.items as {
                    title: string;
                    url: string;
                    note?: string;
                  }[]
                ).map((it) => (
                  <li key={it.url}>
                    <a href={it.url} target="_blank" rel="noreferrer">
                      {it.title}
                    </a>
                    <div className="break-all text-xs text-[var(--ust-light-teal)]">
                      {it.url}
                    </div>
                    {it.note ? <div>{it.note}</div> : null}
                  </li>
                ))}
              </ul>
            </div>
          );
        }
        if (type === "card") {
          return (
            <div key={i} className="rounded-lg border border-[var(--border)] bg-white p-4">
              {b.title ? (
                <h3 className="mt-0 text-base font-bold">{String(b.title)}</h3>
              ) : null}
              <NoteBlocks blocks={(b.blocks as Block[]) || []} />
            </div>
          );
        }
        return null;
      })}
      <p className="pt-6 text-xs text-[var(--ust-muted2)]">{t.disclaimer}</p>
    </div>
  );
}
