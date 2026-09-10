# G.A.Menon Academy — Claude Certification Learning Hub

Static Next.js site: notes, quizzes, video link slots. **No database. No login.**

## Local

```bash
cd academy
npm install
npm run dev
```

## Add session videos

Edit `academy/data/videos.json` and set `url` on each module. Redeploy.

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

EN / ES toggle in the header (saved in `localStorage`). Notes, UI, quizzes, and video titles are bilingual.
