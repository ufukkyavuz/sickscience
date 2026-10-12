# Video 01 — NetWork × BCRF pilot (2026-10-04)

Kredisiz akış: Higgsfield Unlimited görselleri (yeni üretim yok) + yerel hareket/tipografi (Python/PIL, Founders Grotesk) + ffmpeg + ElevenLabs seslendirme.

| Sahne | Görsel | Ekran metni | Seslendirme |
|---|---|---|---|
| phone | batch-13 phone.png + kilit ekranı bildirimi | ADD ONE STEP / TO YOUR ROUTINE. | This October, add one step to your routine. |
| set | batch-13 set2_story.png (stüdyo set, kenardan muayene, ürün gerçek ölçü) | THE MONTHLY / SELF-CHECK. | Your monthly self-check. |
| pair | batch-15 pair_a.png (tepeden iki kapsül, ring ışık) | A PAIR WORTH / CHECKING. | Because it's a pair worth checking. |
| donation | batch-13 hand2.png | 20% + bağış cümlesi | And this October, twenty percent of NetWork sales on SickScienceLabs dot com go to The Breast Cancer Research Foundation. |
| end | logo + ürün PNG | NetWork Rich Concentrated Serum · SickScienceLabs.com | — |

Çalıştırma: `ELEVENLABS_API_KEY` ortam değişkeni tanımlıyken `tts.py` → `vo.mp3` + `timings.json`; sonra `render.py timings.json` → `out/video-01.mp4`. Anahtar dosyaya yazılmaz.
Python: scratchpad venv (cairosvg, pillow, imageio-ffmpeg).
