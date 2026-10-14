# SickScience — oturum özeti (Ekim 2026, 01–12)

Başka bir bilgisayarda devam ederken önce bunu, sonra proje klasöründeki `CLAUDE.md` dosyasını oku. Kalıcı kurallar `CLAUDE.md` ve `memory/SickScience/` içinde. Bu dosya ne yapıldığını ve neyin beğenilip neyin beğenilmediğini kısaca anlatır.

## Çalışma düzeni
- Proje klasörü: `Drive'ım/SickScience`.
  - `Teslim/<YYYY-MM Ay>/` = müşterinin gördüğü tek yer, sadece bitmiş videolar. Alt klasörler: 01 UGC · 02 Basın & Podcast · 03 Animasyon · 04 Ulta.
  - `_calisma/` = batch klasörleri, render script'leri, klipler (eski adı `output/`, 2026-10-12'de değişti).
  - `prompts/` = her batch'in prompt kayıtları. `tools/` = yardımcı araçlar.
- Statikler Figma'da: dosya `PHPZ7XLpEVMcUVVEcNTwmz`. Müşteri statikleri kendisi export ediyor, dosya olarak teslim edilmez.
- **Görseller:** sadece Higgsfield web arayüzü, Nano Banana Pro, 2K, **Unlimited**, adet 1/4.
  - Adedi 2'ye çıkarmak Unlimited'ı sessizce kapatıyor. Sayfa yenilenince de Unlimited kapanabiliyor; her gönderimden önce kontrol et.
  - MCP ile kredi harcayarak görsel üretme.
- **Sonuçları alma:** MCP `show_generations` → `rawUrl` → doğrudan Figma'ya (`upload_assets` + curl POST, `currentPageId` parametresiyle). Tarayıcıdan indirme yapma.
- **Video:** Kling 3.0, MCP üzerinden, kredili (5 sn ≈ 8.75 kredi). Videolar için önce onay alınır.
- **Prompt:** her zaman `prompts/TEMPLATE-photographic.md` bölümleriyle yazılır.

## Yeni araçlar (`tools/`)
- `label_fix.py`: Kapsül üzerinde bozuk çıkan dikey yazıyı silip beyaz Helvetica Bold ile yeniden yazar. `stripe` seçeneğiyle eksik siyah şeridi de çizer.
  - Küçük, elde tutulan kapsülde model yazıyı sık bozuyor ("StapeShift", "NotWork"). Ürün büyütülmez, bu araçla düzeltilir.
- `cutout.py`: Beyaz fondan ürün keser (grabCut).
  - Krom gümüş kısım fonla karışıyor. Tipografiyi ürünün arkasına almak için sadece renkli kapak kesilir, convex hull ile doldurulur.

## Ekim 2026 Instagram (organik), Figma sayfası "Ekim 2026 İG"
- **Yön:** beyaz, premium, fotoğrafta görsel metafor; metin grafik tasarımın parçası, fotoğrafın üstüne düz yazı değil.
- **Beğenilmeyenler:** flaşlı/koyu seri, düz beyaz podyum, dev serum damlası, V-fold, folyo.
- **İşaretleme:** her görselde farklı olmalı ("her yerde aynı yapma"). Örnekler: crosshair, asılı numune etiketi, ölçü çizgisi, dokunma noktası halkası, fiş tipografisi, numaralı rozet + lejant, müze etiketi.
- **Taş-kağıt-makas grid satırı (G1–G3):**
  - Referans: marsi.digital trendi. Her karede 4 el: üstte makas ve ürünü tutan el, altta iki açık avuç.
  - Seçenek yazısı sol üstte, ürün adı sağ üstte, ürün renginde.
  - İlk versiyonda (2 el, avuçta ürün) "taş-kağıt-makas olduğu belli değil" dendi, referansa göre yeniden yapıldı.

## Performans statikleri, Figma sayfası "Ekim 2026 · İndirim Statikleri"
- Fiyatlar 2026-10-11'de siteden alındı:
  - Vault $180→$144
  - Award-Winning Duo $128→$108
  - GLP-1 System $162→$137
  - Subscribe & Save %15
  - $75 üstü ücretsiz kargo
- **İlk set:**
  - D1: "We cut $36." (makas el fiyat etiketini kesiyor)
  - D2: fiş (TOTAL $108)
  - D3: pouch + ücretsiz kargo çubuğu
- **Yazının görselle oynadığı set** ("dümdüz olmasın"):
  - N1: ürünler "%" işaretini oluşturuyor, yanında dev "20"
  - N2: "Read the fine print", büyüteç altında "save 15%" büyüyor
  - N3: dev "$137" ürün kapaklarının arkasından geçiyor
- **Düzeltmeler:**
  - N3'te gua sha yanlıştı. Set elementleri gua sha'yı yanlış çiziyor; gua sha her zaman `@ss-guasha` ile ayrı verilir.
  - N2'de maske kötüydü; mercek ölçülerek oturtuldu, halka, sap ve kapsül yazının üstüne kesildi.
- Buzzfy'da statik reklam kütüphanesi yok, sadece reel. Playbook'tan alınan kurallar: üstte iddia/sayı satırı, paylaşılabilirlik, numaralı faydalı içerik.

## Videolar
- **Teslim edilenler (Teslim/2026-10 Ekim):**
  - UGC: ShapeShift Try-before-you-buy hook 1–4; buzzfy b1–b4; kısa UGC'ler p1/d1/n1
  - Gloss Angeles podcast kesitleri g1–g4
  - TODAY Show ×4 (9x16 / 4x5 / 1x1)
  - Animasyonlar
  - Ulta Holiday UGC 1–2
- **UI-hook videoları (batch-40):** soru kutusu yakma, bildirim yakalama, yorum buruşturma. Kullanıcı beğenmedi, Teslim'den sildi. Bu konsept tekrar önerilmez.
  - Ders: referanstaki "Comment X" CTA'sı bizde kullanılmaz (o reel prompt dağıtmak için yapmış). Kapanış önceki videolar gibi stat + logo + SickScienceLabs.com olur.
- Video kuralları: ≤20 sn; ürün videoda bozulursa kadraj dışı bırakılır, kapanışta gerçek PNG yapıştırılmaz.

## Sıradaki olası işler
- BCRF fişi statiği (NetWork, Ekim boyunca).
- "92%" ShapeShift statiği.
- Kasım için `Teslim/2026-11 Kasım/` klasörü, BFCM "The Vault Is Open".

## 2026-10-13 — Founder toon series (batch-43) + client feedback
- Founder character sheets (Merve, Polen) from the site photos → Higgsfield elements `ss-founder-merve`, `ss-founder-polen`; Polen re-done with jet-black hair after her feedback → `ss-founder-polen-v2`.
- Ep1–3 delivered (`Video/2026-10 Ekim/03 Animasyon/ShapeShift – Kurucular Bölüm 1/2/3`). Talking shots via Veo 3.1 (Higgsfield + Google Flow); Kling mispronounced "exosomes" → ElevenLabs/Wan tested, Veo native voice adopted.
- New tools: `_calisma/batch-43-founder-toon/capsule_patch.py` (track + smooth + sub-pixel composite of a sharp product label), `render43.py`, `render43_ep.py` (per-episode end cards from brand films, URL without plate).
- Client feedback (Polen, 2026-10-13): product film showed foam → new gel-serum pump clip ready; VO too sultry → 3 ElevenLabs voice samples sent, waiting for choice; Polen's hair should be jet black → sheet updated, existing episodes pending (a: regenerate ~100 Flow cr / b: recolour).
- Observations 0035 (hinted ASR is not a pronunciation check), 0036 (tracked composites need temporal smoothing + consecutive-frame QA).

### Linkler — 2026-10-13 oturumu
**Çalışma alanları**
- Higgsfield proje: https://higgsfield.ai/generate/@residential_walrus_super/sickscience
- Google Flow proje (Veo klipleri): https://flow.google.com/project/9d3b1d8b-d9b1-4f4b-8f43-8677fb4f0f44
- ElevenLabs Flow (ses denemeleri; Merve sesi + ürün filmi ses adayları): https://elevenlabs.io/app/flows/tudaHws9lSPT9jRuq7ou
- Figma: https://www.figma.com/design/PHPZ7XLpEVMcUVVEcNTwmz/SickScience
- GitHub repo: https://github.com/ufukkyavuz/sickscience (branch `claude/agency-rules-and-knowledge`)
- Müşteri UGC Dropbox ("All UGC"): https://www.dropbox.com/scl/fo/6usaz92h135sgv7bm627k/AKlzvKIFmCkExsvI60PQjJ8?rlkey=siowdmdufxmei0t3aj664y815&dl=0
- Kurucu fotoğrafları (kaynak): https://sicksciencelabs.com/pages/sickscience-labs
- Ürün sayfası (copy kaynağı): https://sicksciencelabs.com/products/shapeshift

**Higgsfield elementleri** (ID'ler `tools/hf_elements.json`)
- `ss-founder-merve` 111e2c5b-aabb-4b64-800d-a0f8326a2b58
- `ss-founder-polen` 3dae89b6-d0b3-4859-a10b-e5f49787c67e (eski, kahve saç)
- `ss-founder-polen-v2` 1ae00a81-3075-4899-a806-f4037823788b (simsiyah saç — bundan sonra bu)

**Karakter sheet'leri (Higgsfield çıktıları)**
- Merve: https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_072514_142bba89-6655-4c13-9532-21f88994c180.png
- Polen v1: https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_072620_659c8263-80fc-4cc5-a15d-d056fe4e7804.png
- Polen v2 (siyah saç): https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_201200_fe8b17aa-9e81-4406-85bc-22c8891ecddc.png

**Bölüm sahne görselleri (Higgsfield, Unlimited)**
- Ep1 S1 iki kurucu: https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_073942_2f00d188-9f6a-4aad-b69f-8c98b2a481ae.png
- Ep1 S2 Polen+kapsül: https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_074030_65083992-30e7-43da-a316-0e40badb36e6.png
- Ep1 S3 ürün (beyaz tezgâh): https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_081915_64b7b236-4c49-4e6b-bb24-d2065876179f.png
- Ep1 S4 kapanış (etiket düzeltilmiş kopya Drive'da `stills/e1_s4.png`): https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_115736_8c6d68cc-c5ad-41ac-9200-2fd046b2d149.png
- Ep2 S1 Polen hook: https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_121539_84c2c074-3d62-4b7b-ac6a-a3ee6719830f.png
- Ep2 S2 Merve + kapsül tezgâhta: https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_130007_08618b6a-acdb-4268-96a5-cea881cd873a.png
- Ep2 S3 jel damlası (kapaksız): https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_125908_080f4046-6dc3-4214-b1c0-8db3efbac5c3.png
- Ep3 S1 Merve uygulama: https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_122622_3d710887-80de-4df0-882d-c8b85b466e6b.png
- Ep3 S2 Polen gua sha: https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_121655_75105b15-b8fb-4fbe-9624-e84d96c96a42.png
- Ep3 S3 ShapeShift + gua sha: https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_122653_3b1ef6d6-dca0-4888-b674-1cb61d65c315.png
- Ürün filmi yeni pompa (jel): https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_201050_f14585fc-ce97-4552-91fe-397bba457347.png

**Kullanılan video klipleri** (yerel kopyalar `_calisma/batch-43-founder-toon/clips/`)
- Ep1 Merve (Veo, Higgsfield): https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_111121_c1ebc54a-dd03-473b-8cc2-05f0f781227a.mp4
- Ep1 Polen (Kling): https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_085841_c079e66f-cac5-496f-83c9-5a60451c2437.mp4
- Ep1 ürün b-roll (Kling): https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_085843_fd50109f-8dae-4401-91d1-d8220315da23.mp4
- Ep1 kapanış (Veo, Higgsfield): https://d8j0ntlcm91z4.cloudfront.net/user_32K9oJjn9hyqBmrRFwyN6jQbIPy/hf_20261013_120609_c28564c1-d376-4a6e-86b0-999d44965a49.mp4
- Ep2/Ep3 Veo klipleri + ürün filmi pompa klibi: Google Flow projesinde (yukarıdaki link) — "Woman talking about exosomes", "Woman speaks about gel serum", "Woman applying serum on neck", "Woman demonstrating gua sha tech…", "Dispensing gel serum from bottle"

**Teslim edilen videolar** (Drive: `Video/2026-10 Ekim/03 Animasyon/`)
- ShapeShift – Kurucular Bölüm 1 – 9x16.mp4 (17,5 sn)
- ShapeShift – Kurucular Bölüm 2 – 9x16.mp4 (16,4 sn)
- ShapeShift – Kurucular Bölüm 3 – 9x16.mp4 (14,1 sn)
- Ürün filmi revizyonu bekliyor: proje `~/OpenMontage/projects/shapeshift-v2` (yeni `assets/dispense.mp4` jel; eski köpük `dispense_OLD_foam.mp4`, eski ses `vo_OLD_sultry.mp3`); ses adayları `_calisma/video-03-shapeshift/vo_v2/`
