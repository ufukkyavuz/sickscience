# Batch 17 — ShapeShift rakip taraması + yeni kreatifler (2026-10-05)

Kaynak: Meta Ad Library (US, aktif, gösterime göre) + Instagram (kullanıcının Chrome oturumu).
Kullanıcı: "rakiplerin hepsini hem meta hem instagram… özellikle shapeshift baskın gidelim… spoiledchild'da Disney tarzı animasyon videolar… ürünü bozmadan".

## Bulgular
| Kaynak | Kalıp | ShapeShift için |
|---|---|---|
| SpoiledChild (Meta, A22 Hair Serum, 44 sn) | Pixar/Disney 3D karakterler, 1. ağızdan hikâye ("The more I spray… I found A22… changed everything… Thanks to a few sprays"), 3 farklı karakter, kalın beyaz altyazı, ürün her sahnede doğru etiketle | **Animasyon testimonial** — karakter Pixar, ürün gerçek (element) |
| "Jawline serum" kategorisi (Meta) | Pixar tarzı açıklayıcı: köşede PiP anlatıcı doktor karakteri + büyükanne karakter + gülen kolajen hücreleri (3 dk) | Hücre/ingredient sahnesi fikri (NX35 eksozom) |
| Kore cilt bakımı (Meta) | AI avatar elinde iki sönük balon "deflated balloon" metaforu | Metafor prop'u; negatif ton → kullanılmadı |
| StriVectin (Meta + IG) | Yan profil boyun yakın planı + "The #1 Neck Cream" + 4 maddelik fayda listesi; IG'de dergi kapağı ("StriVectin" masthead); UGC 50+ kadın | **Profil + fayda listesi**, **dergi kapağı** |
| Neck/jawline ads | Doktor kil büstü yontuyor (heykel metaforu); "NECK LOOKS DULL AND OLDER THAN YOUR FACE?"; Marée V-line maske profili; Perricone sepet ekranı; fiyat rozeti | **Heykeltıraş büstü** = "Chisel your jawline" (sitedeki başlık) |
| SpoiledChild IG (@spoiledchildworld, 800K) | Organik: makro ürün/tekstür, renkli kapsül ürün animasyonu, lifestyle | — |

## Konseptler (yazısız master 9:16, metin Figma'da, Founders Grotesk — CONDENSED YOK)
1. **Sculpt** — beyaz alçı büst + keski + ShapeShift. Başlık: "CHISEL YOUR JAWLINE IN 2 WEEKS." (site) · alt: "92% saw a more sculpted jawline".
2. **Profile** — yan profil çene/boyun, elde ürün. Başlık + sitedeki 3 Key Benefit listesi.
3. **Cover** — dergi kapağı: "ShapeShift" masthead + cover lines (92% / 94% / 98% / 90% site istatistikleri) + "2024 REAL SIMPLE Award Winner".
4. **Toon** — Pixar karakter 4 kare (ayna → buluş → uygulama → 2 hafta sonra), Flow/Veo ile animasyon, ElevenLabs VO + altyazı, HyperFrames kurgu; kapanış gerçek ürün fotoğrafı.

## Animasyonda ürünü bozmama yöntemi
- Karakter Pixar, ürün `@ss-shapeshift` elementi ile "NOT CARTOONISED… exact shape/label" — gerçek nesne olarak render.
- Ürün kadrajda sabit/elde, büyük hareket yok (Veo'da ürünün deforme olma riski hareketle artar).
- Etiket bozulan karelerde son karede gerçek ürün PNG/foto ile kapanış (HyperFrames).

Prompt'lar: `batch-17-build.py` → `batch-17.json`.

## Sonuç (2026-10-05)
- **Video:** `output/video-05-shapeshift-toon/ShapeShift_toon_9x16.mp4` (29 sn, telefon için `_web.mp4`). HyperFrames projesi `~/OpenMontage/projects/shapeshift-toon`. Sahneler: ayna (Veo) → yatak (still + yavaş zoom; Veo politika filtresine 2 kez takıldı) → uygulama (Veo) → selfie (Veo, yüze kırpıldı) → gerçek ürün PNG'li kapanış. VO: ElevenLabs eleven_v3, Sara.
- **Figma** "SS · ShapeShift push — competitor-driven (batch-17)" (393:225): Profile ×3, Cover ×3 (Square'ler ayrı 1:1 üretim), Countdown 15% · Toon · Story, Countdown 15% · Packshot ×3 (gerçek PNG). Sayaç kutuları düzenlenebilir metin ("Countdown (animate in Figma)").
- Heykel konsepti kullanıcı isteğiyle bırakıldı (daha önce yapılmıştı).

## Öğrenilenler
- `@ss-shapeshift` elementi oranı sık bozuyor: elde tutulan şişe tıknaz/geniş, yakın plan still-life'ta dev çıkıyor. Prompt'a "PROPORTIONS ARE CRITICAL… height 3.4× width… cap = upper half" eklemek çoğu karede düzeltti; masada duran şişe elde tutulandan daha güvenilir.
- Veo (Flow) image-to-video ürünü yeniden çiziyor → klipte şişe tıknazlaşabilir; çözüm: kırp/kadraj dışı bırak, kapanışta gerçek PNG.
- Flow: "Sessiz videolar" açık olsa da prompt'ta ses çağrıştıran eylem (sigh vb.) "Ses üretilemedi" hatası veriyor; prompt'a "SILENT video (no audio track at all)" yaz. Yatakta askılı karakter görseli politika filtresine takıldı. Başarısız işler kredi düşmüyor.
- Flow'da onay butonu "Her zaman onayla"ya alındı (2026-10-05).
