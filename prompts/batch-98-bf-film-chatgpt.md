# Batch-98: Black Friday film, scenario by ChatGPT (2026-11-03)

User: "şu senaryo ve sahne yazma işini bide chatgptde dene". Written by ChatGPT (chat "Animasyon Konseptleri", chatgpt.com/c/6ae9a586-6fa4-83eb-98a2-c0d28ba1dea1). The full English per-shot prompts are in that chat; summary below.

## Concept: Black Friday Lift-Off
The bottle does not grow by magic. On Black Friday night Merve and Polen fill a giant ShapeShift-shaped launch balloon on the roof of their own lab building with purple NX35 vapour, ride it over New York and come back to the roof.

| # | s | Shot | Cause → effect |
|---|---|---|---|
| 1 | 2.0 | Wide, night exterior of the lab building, founders small in the lit top floor | Sets the one building where everything happens |
| 2 | 2.0 | Close-up of the real bottle on the bench, flask feeding purple NX35 vapour into a tube going up | Shows the product and the power source |
| 3 | 2.0 | Medium: Merve connects the tube, Polen turns the valve; through the roof door the folded giant balloon | Makes the mechanism explicit |
| 4 | 2.0 | Low angle on the roof: vapour inflates the giant ShapeShift, the two climb onto a small seat near the top | Growth = inflation, not magic |
| 5 | 2.0 | One eye of Merve through clouds, chrome edge beside her | They are riding it in the sky |
| 6 | 1.5 | Empty New York skyline at night | Anticipation |
| 7 | 2.5 | Giant ShapeShift drifts into frame with both on top, heading back | Payoff |
| 8 | 3–4 | Hero: giant bottle settling over the same roof, both sitting on top; a real-size bottle on the ledge; empty top for title | Closes the loop, shows the real product |

Headline: "Lift Your Look. Black Friday." Offer line: "Black Friday Offer on ShapeShift".
ChatGPT's own logic risk: the giant bottle must read as an inflatable in shots 3–4, or "how does it fly?".
Product rule written into every prompt: purple/silver mirror chrome, white text printed on the chrome, no black band.

## v2 (2026-11-03): ChatGPT watched the reel itself
User: "saçma oldu videoyu ver bide öyle baksın". The reel was recorded in the browser (`_calisma/batch-96-bf-film-v2/refs/ysl_reel_referans.mp4`, 6.7 s, 24 fps) and uploaded to the same chat.

ChatGPT's reading of the reel: about 5 camera set-ups carrying 8 story beats. Joke = an everyday action (putting a luxury compact in the oven like food) gives an absurdly big result. Wordless cause → wait → smoke warning → shock → giant payoff, one object, one action, one surprise, one reward. Beats 4–5 share one low shot from inside the oven, beats 6–8 share one locked city shot.

New concept: **The Big Zoom**. Merve puts the bottle under a comically oversized lab magnifying lens; Polen turns the zoom wheel one click too far; the bottle really grows.
| # | s | Shot (reel equivalent) |
|---|---|---|
| 1 | 0.0–0.8 | Wide, sunlit Manhattan loft lab: Merve sets the bottle under the giant lens, Polen reaches for the wheel (oven loading) |
| 2 | 0.8–2.0 | 85mm close: Polen turns the brass wheel, bottle looks huge in the lens (oven close-up) |
| 3 | 2.0–3.2 | 50mm medium: Merve reads notes, purple smoke rises behind from the lens, Polen notices (reading) |
| 4 | 3.2–3.9 | 24mm low from under the lens: bottle physically pushes the lens up, both wide-eyed (inside oven) |
| 5 | 3.9–4.8 | same shot: smoke fills frame, one eye of Merve (eye through smoke) |
| 6 | 4.8–5.2 | locked 35mm city: the same cream lab building, empty blue sky (empty Paris) |
| 7 | 5.2–5.8 | same city shot: giant ShapeShift with both on top amid purple smoke |
| 8 | 5.8–6.7 | same: smoke clears, giant bottle on the roof, both sitting, top 25% empty sky |
Title: "SMALL BOTTLE. BIG BLACK FRIDAY." Offer: "Black Friday Savings on ShapeShift". Full per-shot prompts in the chat.
My note: ChatGPT writes frame 7 as the bottle "descending from above"; in the reel the object bursts up out of the building, and the user rejected a falling bottle. Frame 7 should rise out of the lab roof.

## v4 sonuç (2026-11-03) — `_calisma/batch-96-bf-film-v2/film/v4/kare_1..8.png`, kontak `big_zoom_kontak.jpg`
- 1, 2, 6: reel karesi (b1, b2, b6) dönüştürme, tek seferde tuttu.
- 3: b3 dönüşümü (şişe düz kapaklı çıktı) → PRODUCT FIX düzenlemesi → gümüşte siyah yazı → `whiten_col2.py` ile piksel beyazlatma.
- 4: b4 tabanı iki kez başarısız (vida ağızlı şişe, nokta göz) → kare 2'nin çıktısı taban yapıldı → yazısız çıktı → TEXT FIX + piksel beyazlatma.
- 5: kare 4 çıktısı taban (mercek çatlıyor, bulutlar, Polen'in gözü).
- 7: kare 6 çıktısı taban → eğik/yazısız → PRODUCT FIX + POSITION (dik, alt kısım çatıda) → gerdanlık silme düzenlemesi.
- 8: kare 7'nin DÜZENLEMESİ olarak yapıldı (transform kamerayı değiştirdi) → 2 düzenleme: enkaz/duman sil, şişe dik, su kulesi dik, ikisi sakin oturuyor.
- Ders: devam karelerinde transform değil EDIT (aynı kadraj korunuyor). Gümüş yarıdaki yazıyı model inatla koyu çiziyor; bir düzeltme denemesinden sonra pikselde düzelt.
