# Founders timeline: photos for the brand-story video (2026-11-06)

User: "o videoda toplantıda bahsettikleri bir timeline var ondan fotolar da olsun istiyorlardı".

## Source
- Meeting (Fathom "Sick Science brand book", 05.11, ~1:44–2:12): Merve shares her screen and shows a Canva doc,
  "SickScience NetWork Launch Event – Timeline…", 6 pages, one year per page, each with a photo and a caption.
  Fathom link: https://fathom.video/share/6usoma7F1sKjaYHpDUH5svGbj_FJx-Sg
- The same timeline was printed as a wall panel at the NetWork launch event:
  Brand Assets/Event video & images/Photographer NetWork Launch Event - Photos 2/IMG_9340.jpg (2024 + 2025)
  and IMG_9904.jpg (2009, 2013, 2018, 2020; shot at an angle, partly blocked by a guest).
- The Canva doc is NOT shared with us (Canva search, shared tab: not there). Action item from the meeting:
  "Add team to Canva; share assets w/ Zeynep & Ufuk" (Merve, @0:54), still open.

## The 6 beats (captions verbatim from their Canva and the wall panel)
| Year | Photo | Caption |
|---|---|---|
| 2009 | Merve and Polen in lab coats, first biology class | "Where it all began — two scientists, one lab, and a shared obsession with cellular science." |
| 2013 | the two of them at graduation, in caps | "Graduation wasn't the finish line — it was the start of turning science into impact." (read from a blurry frame, confirm) |
| 2018 | the two of them in a lab corridor, lab coats | "The first exosome breakthroughs — cancer research, obesity science, and the foundation of what was coming." |
| 2020 | selfie in masks (COVID) | "Instead of hiding during COVID, we were busy exploring exosome inhalation as a new frontier for lung therapy." |
| 2024 | both with their babies; second photo holding a paper | "Still in the lab — balancing motherhood, science, and building something bigger than ourselves." |
| 2025 | SickScience studio photo + the 4 products | "From lab benches to the global stage — SickScience grows into a biotech beauty brand ready to bring science-backed skin and hair care to the masses." |

Claim check: "lung therapy" in 2020 is the founders' own research history, not a product claim. Fine in the organic founder video; leave it out of the ≤20 s ad cut.

## Quality problem
- In the meeting recording the whole Canva window is ~420 px wide, so each photo is about 90 × 120 px. That is unusable on a 1080 frame.
- The wall-panel photos are better, but shot at an angle, with glare and a guest in front.
- **Needed: the 6 original photos (or the Canva doc shared with Ufuk's account).** Then they go into the notebook as taped prints, "FIG. 2009", "FIG. 2013"…
- Exception: the 2025 photo = the client's studio shoot, already in "Images/Founders Images (Merve & Polen)" at full resolution.

## Where it goes in the film (script-v2-notebook.md)
- Beat 02 ("We met in a chemistry class in 2009…"): taped print FIG. 2009 + caption in handwriting.
- Beat 03 (patents, papers): FIG. 2013 graduation + FIG. 2018 lab.
- New beat after 03, ~3 s: FIG. 2020 masks, handwritten "exosome inhalation, 2020".
- Beat 04 (mom, the quiet beat): no photo; keep it quiet.
- New beat after 05, ~3 s: FIG. 2024 with the babies, handwritten "still in the lab".
- Close: FIG. 2025 + the four real products on the bench.
- Organic length rises to ~55 s. The ad cut takes only 2009 + 2025 (≤20 s rule).

## Message for Merve/Polen (to forward)
Merhaba Merve, toplantıda gösterdiğin "NetWork Launch Event – Timeline" Canva'sındaki 6 fotoğrafın (2009, 2013, 2018, 2020, 2024, 2025) orijinallerini paylaşabilir misin? Ya da Canva'yı ekip olarak bize açabilirsin. Kuruluş hikâyesi videosunda bu fotoğrafları defterde yapıştırılmış baskılar olarak kullanacağız. Toplantı kaydındaki ekran paylaşımı çok küçük kaldığı için oradan kullanamıyoruz. Bir de sesler için ElevenLabs onayı gerekiyor; ses kaydını kendi sesinizle yapacağız.

## Still blocked
1. The original photos (above).
2. VO: the Merve/Polen voice clones are waiting for consent in ElevenLabs. Without it the film can only be captions + music.
3. "fourteen years" vs 2009 → 2026 (17 years); confirm with the founders.

## Production v1 (2026-11-06)
- User: "ses klonlamadan normal sesle devam edebiliriz şimdilik". VO = ElevenLabs stock voices: Polen = Cecilia O'Connor (DIS307HFaAvJZzq496qM), Merve = Tawny (Rv3wiuHHQq0rSS4QVaQ8); flow QZMVeY9AwXZ3FJlL4BK7. Swap to clones later = re-run the 11 lines, timeline rebuilds from words.json.
- Work folder: ~/sickscience-work/brandfilm (render.py = notebook film, audio.py = bed + SFX + ducked VO, words.json = whisper word times).
- Plate: Higgsfield blank grid notebook (nb_b). Prints: founders S_0944 (Brand Assets/Founders Images), petri crops from amazon gen56/nx1. End card: client studio photo All Products - New Image/S_0723 (real 4 products).
- Timeline on page 1 is a drawn year line (2009 · 2013 · 2018 · 2020 · 2024 · 2025); the real year photos go above it when Merve sends them.
- v2 delivered 2026-11-06: Video/2026-11 Kasım/03 Animasyon/ — "Founders – Defter hikâyesi (geçici ses)" 66 s, -14.4 LUFS; "…20 sn reklam" 19.9 s, -14.8 LUFS (adcut.py: lines 01, 02a, 06, 07a, 08a, 10 end, 11 end; 09 dropped for length).
- Camera: cy = focus+60 clamped 880–1100 (page px). End card = S_0723 full-height crop, tagline 3 lines top-left (x78, y226–382).
- When clones/photos arrive: re-run vo lines → words.py → render.py --info → audio.py → render.py → mux → adcut.py; overwrite the two files (no v2 siblings).

## Real v2 (2026-11-07)
- The user asked for the founders' past photos. The only sources available are the event wall panel shots, IMG_9340 and IMG_9904; the brand-assets event folders hold no other panel views, and Instagram needs a login.
  - Usable (sharp): IMG_9340 → the pair with the DNA booklet, and the microscope shot. Saved as ~/sickscience-work/brandfilm/v4/prints/pair_t.png and scope_t.png.
  - Unusable (too blurry): IMG_9904 → 2009, 2013, 2018 and 2020.
- Film: on "fourteen years", the camera pans to the blank right page, where two taped prints drop in. The camera holds there for 1.6 s into the next beat. At the 1:04 R01 beat the prints slide off the page. Code: `add_prints`, `PR_*` in animatic_real.py.
- When the originals arrive, add the 2009 and 2013 prints to the PRINTS list in the same way.
