# Claude Certified Developer — vídeos 1 y 2 (es-ES)

Narración en español de España (`tú` / `vosotros`, voz `es-ES-ElviraNeural`). Masterclass Foundation, día 1.

| Vídeo | Archivo | Duración |
|---|---|---|
| 1 · Cómo es el examen | `out/video-01-examen.mp4` | 7 min 35 s |
| 2 · Dónde estudias e inscribes | `out/video-02-academy.mp4` | 7 min 13 s |

1920×1080, 30 fps, voz + subtítulos quemados.

## Regenerar voz y tiempos

```bash
python3 scripts/generate-vo.py
```

## Render

```bash
npm install
npx remotion render Video01 out/video-01-examen.mp4 --concurrency=4
npx remotion render Video02 out/video-02-academy.mp4 --concurrency=4
```
