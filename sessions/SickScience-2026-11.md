# SickScience — oturum özeti (Kasım 2026)

Başka bilgisayarda devam ederken önce bunu, sonra `CLAUDE.md` ve `kurallar/` (memory kopyası) oku.

## 2026-11-11 · Viral UGC 3 (Polen'in ham çekimleri)
Teslim: `Video/2026-11 Kasım/01 UGC/Viral UGC 3/` — motor `_calisma/ugc-viral-3/render3.py` + `specs.py` (B, M, L, A).
- **Myth or fact – Plant exosomes and human cells:** açılış lab'da pipetle çalıştığı sahne (telefonla oynadığı ya da boş beklediği kare değil). İfade + "Myth or fact?" Polen'in gerçek sesinden klonla okunuyor; MYTH / or / FACT kelime anında sağ-orta-sol. Büyük MYTH kafanın arkasında (Vision person mask, `person_cut`), harflerin çoğu okunacak yükseklikte. İsim etiketi OneSkin referansı gibi beyaz kutu, metin kutuda ortalı. Lab verisi + makale kartları ince konturlu, kenardan boşluklu, üst üste binmez.
- **ShapeShift – That was my before:** "that was my before" derken parmağıyla gösterdiği sağ üstte Polen'in before fotoğrafı (sadece çene/jawline kırpımı, göz yok). AFTER yüzün üstünde değil, altta.
- **ShapeShift – How to apply in the lab** (Ayşim, kinetik tipografi) ve **Lab – POV you work at SickScience** (gülüşle biten) teslim edildi.
- **Bekleyen:** Puffy face (NetWork/gua sha ham çekimleri gelmedi).

## Ses klonu
- Higgsfield element "Polen real voice (DropOff sample)" `2cb98bff-9efc-4922-a078-a2f6433c4ef7`, kaynak `_calisma/batch-123-polen-dropoff/polen_real_vo_raw.mpeg` (kullanıcı onaylı). Eski "Polen IG clean" Rus aksanlı → kullanma. Klondan önce kaynak kaydı kullanıcıya gönderip teyit al.

## Öğrenilenler
- Referans videoyu baştan sona kare kare incele (OneSkin reel: tek sakin plan, beyaz kutulu isim etiketi, küçük altyazı, efekt yok).
- Kinetik başlıkta kelime/satır arası sıkı olmalı; büyük kelimeler yüzü/kanıtı kapatmaz.
- Eklenen kart/fotoğraflar: ince beyaz kontur, kenardan ≥100 px boşluk, hafif yukarıda.
- B/A fotoğrafı ürün alanına kırpılır (ShapeShift = çene/boyun).

## 2026-11-13 · BF set kreatifleri, Cuma 13, UGC kart/ürün PNG düzeltmeleri
- **Viral UGC 2 (10 video):** beyaz ürün adı kartı HER videoda vardı → kaldırıldı ("ai slop"); sol üstte ürün adının soluna gerçek ürün PNG'si denendi (kullanıcı isteği, KALICI KURAL DEĞİL). Kart kodu pipeline'dan silindi.
- **BF set görselleri** (`Products/sets-bf/`): Drive'ım/ad ss referanslarından her sete ayrı referans (yerleşim %'leri `prompts/batch-128-bf-set-layouts.md`), sahne referansa benzer ama beyaz ağırlıklı. DropOff HER ZAMAN kapaklı (açık/damlayan uç çizilmişti). Set PNG'lerinde tüp/SS 1.30 çıktı, kural 19/14/12 cm = 1.58 → elementler düzeltildi (`sets-fixed`).
- **Fiyat:** taban = normal (üstü çizili/compare_at) fiyat, 2026-11-16 netleşti (mailler doğru); sitede setler Early BF'de zaten %25.
- **Cuma 13:** Drive "Mail Alternatifleri (13 Kasım)" PDF'inden 4 konsept (`prompts/batch-130-friday13.md`), öncelik 1; 4 Story + Feed/Square üretildi.
- **Figma bağlayıcısı** 500 verdi; Higgsfield MCP Claude Code'da Unlimited kapalı, Chrome profili kullanıcı hesabına bağlı değildi (Muse hesabı).

## Öğrenilenler (2026-11-13)
- Arşivli oturumlar aramada çıkmaz; ~/.claude/projects jsonl'lerini grep'le, gerekirse unarchive_session.
- Referanstan sahne + yerleşim kopyalanır; palet beyaz ağırlıklı.
- Giriş/onay/sözleşme sayfalarını kullanıcı verir; kendi başına hesap değiştirme.

## 2026-11-16 · Yazı animasyon kütüphanesi, high-end yön, Figma düzen sistemi, tasarım videosu
- **textfx (41 efekt):** `_calisma/textfx/textfx.py` + `demo.py`, katalog `_calisma/textfx/out/textfx-catalogue.mp4`. Kaynak: hyperframes-animation (animate-text 24 efekt adları, techniques), motion-graphics motion-vocabulary, motion-effects, kinetic-reel. Harf/kelime/satır/bütün efektleri, exit'ler, `word_times` ile konuşmaya kilit. Varsayılan ağırlık Medium.
- **Kural düzeltmesi:** "beyaz yazı + tek vurgu rengi", "videoda tek ana stil" gibi kısıtlar kaldırıldı ("değişime ve farklı stillere açık olmalıyız"); sadece Founders Grotesk + okunurluk sabit. `MOTION-BRAND-KIT.md`.
- **High-end araştırma:** az ama net marka kodları, ritüel/doku, bilim = güven, sessizlik, gerçek sesler, marka vs satış iki katman (MOTION-BRAND-KIT §4).
- **Figma düzen sistemi:** renk değişkenleri (accent/magenta, neutral/ivory eklendi), text style'lar `SS / Display Light(+Italic)`, `SS / Body`, `SS / Label`, `SS / Headline Medium`; konsept başına copy component (`HE / Copy / A–C`, Headline/Sub + `Show sub`), Story/Feed/Square instance; sayfa "High-end · Kasım 2026" (2022:14), A lab sehpası S_1143, B petri S_0883, C kurucular S_1729.
- **Başlık stili:** kullanıcı katalogdaki "Clinically inspired." karesini seçti → Founders Medium, sıkı satır aralığı; punto SABİT DEĞİL.
- **Kullanıcının Figma videosu** (Masaüstü "Ekran Kaydı 2026-11-16 11.42.11.mov", sesli; faster-whisper medium ile döküldü): fotoğraf kenarı zeminde görünmez (büyüt), başlık boş alana göre göz kararı (tek satır olabilir, alt satır ~45), logo zorunlu değil, Feed/Square = 9:16 master yazının arkasında + Expand, free shipping mührü eşikte + hafif mor, NX35™ özellik rozeti (™ küçük, arkada molekül).
- **Esnetilen kurallar:** yazı zemine göre siyah/beyaz; partner (Ulta) kimliği alttan yedirilir (kalem alt çizgi, fosforlu iz, glow), direkt turuncu başlık yok; yaratıcı rozetler, hediye rozeti çok işe yarar (teyitle); farklılaştıran bileşenler şık bilimsel görsellerle; reklam metni yaratıcı olabilir (iddia/istatistik/fiyat siteden).
- **Referans:** X @TheXEffect_ 20 poster (marka öğesi + tanıdık fikir + tek zekice cümle). SickScience için 8 konsept önerildi (PowerCycle ⏻, NetWork sinyal çubukları, eksozom kurye, ShapeShift açıölçer, tech-neck ekran süresi, ananas, ilaç esprisi (Meta riski), kurucular). Kullanıcı seçimi bekleniyor, üretim onaysız başlamaz.

## Öğrenilenler (2026-11-16)
- Ses dinleme = whisper dökümü + kare kare inceleme; faster-whisper'da av.open hatası → wav'ı numpy olarak ver.
- X çoklu görsel: sayfada JS ile grid overlay kurup tek ekranda incele (URL'ler sorgu engelli).
- Figma'da açık observation 91: izinsiz harf/satır aralığı ayarı yok (kullanıcı videodaki gibi isterse olur).
