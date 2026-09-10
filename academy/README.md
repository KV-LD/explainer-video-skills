# G.A.Menon Academy — Claude Certification Learning Hub

Static Next.js site: notes, quizzes, video link slots. **No database. No login.**

## Local

```bash
cd academy
npm install
npm run dev
```

## Add session videos

Recordings are **English only** — **one URL per module**. Notes and quizzes stay bilingual.

Do **not** put large MP4s in git. The **Videos** page reads `academy/data/videos.json`.

1. Open `academy/data/videos.json`.
2. For each module (`m01`–`m12`), set `"url"` to the LMS, Microsoft Stream, or Drive share link for that English session.
3. There is no Spanish video field. Leave `"url": ""` until the recording is published.
4. Redeploy (Vercel root directory must be `academy`).

Module note pages show the same single English link under “English session recording”.

## Quizzes

`academy/data/questions.json` holds **100** original practice items (not official exam dumps). Each attempt samples 20 (practice), 25 weighted (exam-style), or a module slice.

## Usage metrics without a DB

Use **Vercel Web Analytics** (already wired via `@vercel/analytics`):

1. Deploy on Vercel
2. Project → **Analytics** → enable **Web Analytics**

That captures page views and top routes. No user accounts. It is anonymous traffic, not quiz scores.

Optional: Vercel **Speed Insights**. Still no database.

This app does **not** store quiz answers. Scores stay in the browser for that attempt only.

## Deploy

From `academy/`:

```bash
npx vercel --yes
```

Production:

```bash
npx vercel --prod --yes
```

Root directory on Vercel must be `academy` if the Git repo is the parent pack.

## i18n

EN / ES toggle in the header (saved in `localStorage`). Notes, UI, and quizzes are bilingual. Session video titles and links are English only.
