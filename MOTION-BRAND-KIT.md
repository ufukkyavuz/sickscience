# SickScience — Motion Brand Kit (2026-11-16)

Buzzfy/Viral UGC videolarında (ugc-viral-1106, -2, -3) çalışan yazı animasyonları
artık her videoda marka kitiyle kullanılır. Kaynak motor: `_calisma/ugc-viral-3/render3.py`
(`anim()`), `_calisma/ugc-viral-2/render2.py` (`STYLE`, spin).

## 1. Sabit olan tek şey: font
- **Varsayılan yazı görünümü (kullanıcı, 2026-11-16, katalogdaki 'Clinically inspired.' karesi):** Founders Grotesk **Medium**, satır aralığı ~%100, harf aralığı 0. Punto sabit değil: referansa ve görseldeki yazı alanına göre ayarlanır. Yerine göre farklı kalınlık (Light/Regular/Semibold/Bold) kullanılabilir.
- **Font ailesi Founders Grotesk** (Light/Regular/Medium/Semibold/Bold, italikler, Text kesimi). Condensed yok, 32 px altı yok.
- Geri kalan her şey sahneye göre **serbest** (kullanıcı, 2026-11-16: "değişime ve farklı stillere açık olmalıyız… yerine göre kullanırız, farklı hava katarız"):
  - Renk: beyaz, ink, fildişi, magenta #A921C0, ürün renkleri (SS #7300C7 · NW #C81E28 · PC #1E823C · DO #193CBE), krom gümüş, harflerin içinde fotoğraf/doku. Gölge, kontur, glow, pill, highlighter sahneye göre.
  - Bir videoda istenen kadar farklı efekt karıştırılabilir; her kelime farklı efekt alabilir. Seçim içeriğe göre yapılır (şaka = slam/bounce, bilimsel cümle = mask/blur, istatistik = counter/odometer, mit = strike/glitch).
- Değişmeyen tek pratik kural: yazı telefonda okunur, kritik metin safe band içinde.

## 2. Kütüphane: `_calisma/textfx/textfx.py` (41 efekt)
Kullanım: `render(effect, text, t, ...)` → RGBA katman; `dur` + `exit` (fade, blur-out-up, scale-down-fade, slide-out-left) ile çıkış; `word_times` ile kelime girişleri konuşmaya kilitlenir. Katalog videosu: `_calisma/textfx/out/textfx-catalogue.mp4` (`demo.py`).
- **Harf harf:** soft-blur-in · per-character-rise · drop-letters · bounce-letters · stagger-from-center · stagger-from-edges · wave · flip-letters · elastic-stretch · tracking-in · typewriter (imleçli) · scramble-decode · weight-wave (Light→Bold)
- **Kelime kelime:** word-pop (spring) · short-slide-right · short-slide-down · shared-axis-y · word-crossfade · depth-parallax · kinetic-center-build (satır her kelimede yeniden ortalanır) · karaoke-pill · highlighter · underline-sweep · strike-through · word-swap (slot'ta dönen kelime) · accent-color-shift
- **Satır:** mask-reveal-up · mask-reveal-down · line-by-line-slide
- **Bütün:** focus-blur-resolve · micro-scale-fade · fade-through · shared-axis-z · slam-shake · glitch-rgb · glow-pulse · shimmer-sweep (krom ışık) · outline-to-fill · texture-fill-rise (harf içinde jel/foto) · counter-roll · odometer
- Eski UGC motorundaki pop/blur/slide/drop/spin bunların alt kümesi; yeni işlerde bu kütüphane kullanılır.
- Daha fazlası için kaynaklar: hyperframes-animation (techniques, blueprints, animate-text 24 efekt kataloğu), motion-graphics motion-vocabulary, motion-effects (masked/elastic type), kinetic-reel (dropWord, tape, odometer, glitchIn). Yeni efekt öğrenildikçe textfx'e eklenir.

## 3. Ton örnekleri (zorunlu değil, başlangıç noktası)
- **Viral UGC:** word-pop, kinetic-center-build, karaoke-pill, slam-shake, bounce, highlighter, büyük kelime başın arkasında.
- **Premium / marka:** mask-reveal, tracking-in, focus-blur, shimmer-sweep, texture-fill-rise, yavaş eğri.
- **Bilim / kanıt:** scramble-decode, typewriter, counter-roll, odometer, underline, strike-through.

## 4. High-end yönü (araştırma, 2026-11-16) — öneri, kullanıcı onayı bekliyor
Kaynaklar ajans portfolyoları ve marka analizleri; performans verisi değil.
1. **Az ama net kodlar:** Rhode/Aesop gibi tanınır 3–4 "brand code": kapsül krom silüet, beyaz lab, magenta tek vurgu, Founders. Her işte aynı kodlar, layout çeşitli.
2. **Ritüel ve doku:** özellik listesi değil; jel-serum dokusu makro, uygulama hareketi yavaş, ürün temas gölgesi.
3. **Bilim = güven (Augustinus Bader, OneSkin):** NX35/exosome'u kurucular + gerçek lab görüntüsüyle anlat; iddia az, kanıt çok.
4. **Sessizlik:** daha az yazı, tek satır, bol negatif alan, yavaş eğri; flash/shake/emoji yalnız viral UGC'de.
5. **Ses:** ucuz whoosh yerine az ve gerçek ses (cam tık, pompa, sıvı); müzik sakin, tek parça.
6. **Işık:** tek yönlü yumuşak ışık, krom yansımaları kontrollü, beyaz/fildişi zemin; aşırı doygun renk yok.
7. **İki katman:** "marka" içeriği premium tonda, "satış/viral" içeriği UGC tonunda; ikisi aynı font/renk kodlarını paylaşır.
