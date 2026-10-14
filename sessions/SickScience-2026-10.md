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
