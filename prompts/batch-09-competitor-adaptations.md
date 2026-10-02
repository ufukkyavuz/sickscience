# Batch 09 — Rakip Meta reklam uyarlamaları (2026-10-02)

Kaynak: Meta Ad Library (US, aktif, gösterime göre sıralı) — Grüns (~1.600 reklam), IM8 Health, SpoiledChild (~1.200).

## Rakiplerden çıkan kalıplar
| Rakip | Kalıp | Not |
|---|---|---|
| Grüns | "THIS ISN'T ADDERALL" — 2 satır provokatif ret + dev ürün + alt satırda ne olduğu | En çok varyasyonlu statik |
| Grüns | Bölünmüş anatomi "On a GLP-1 / On a GLP-1 + …" | GLP-1 kitlesi |
| Grüns | UGC video + TikTok altyazı ("Do not buy … anywhere ❌") | Videolar, statik değil |
| IM8 | Loş, lambalı still-life + "90 days to decide if the evidence holds up" (risk-free) | Güven reklamı |
| IM8 | "Menopause changed your gut, too." + semptom checklist + ürün | Problem-farkındalık |
| IM8 | "BIG WELCOME. ZERO KIT COST." kit yayılımı + değer | Teklif |
| SpoiledChild | Masa üstü ürün + el yazısı post-it ("try before you buy", "best upper of the year") | Native, düşük üretim hissi |
| SpoiledChild | Gerçek önce/sonra makro split + "LEAVE THE PUFFINESS IN 2025" | Yıl/dönem kancası |

## SickScience uyarlamaları (her ürün için; iddialar sitedeki metin)
1. **ThisIsnt** — SS "THIS ISN'T A FILTER." / NW "THIS ISN'T MAKEUP." / PC "THIS ISN'T A HAT DAY." / DO "THIS ISN'T LIPO." + "It's a [site description]". Dev ürün, ürün rengi zemin.
2. **ChangedToo** (IM8) — "GLP-1 CHANGED YOUR JAWLINE / SKIN / HAIR / BODY, TOO." + sitedeki Key Benefits checklist + ürün.
3. **ThirtyDays** (IM8) — loş gece masası still-life + "30 DAYS TO DECIDE." + site: "Free returns, backed by a 30-day money back guarantee".
4. **BigSet** (IM8) — set yayılımı + "BIG ROUTINE. ZERO SHIPPING." Vault $144 (reg $180) / Award Duo $108 / Body Duo $98 / GLP-1 System $137; hepsi $75 üzeri → ücretsiz kargo doğru.
5. **StickyNote** (SpoiledChild) — masa üstü ürün + boş post-it'ler; el yazısı Figma'da (düzenlenebilir).
6. **LeaveIt** (SpoiledChild) — sitedeki GERÇEK önce/sonra (`main-beforeafter_1`, `main_beforeafter`, `mainbeforeafterDO`, `powercycle-results-2`) + "LEAVE THE ___ IN 2026" + dipnot "28 & 56 Day Study · 50 Participants · Third-Party Tested" (site görselindeki ifade).

Site "Real Results" başlıkları: SS "Chisel Your Jawline in 2 Weeks." · NW "Reveal Your Glow in 2 Weeks" · PC "Stronger, Fuller-Looking Hair in 2 Weeks." · DO "A More Sculpted Body. Visible Change in 2 Weeks."

## Sonuç (2026-10-02)
- Figma: "SS · Competitor adaptations — Grüns / IM8 / SpoiledChild (batch-09)" (187:76), 6 satır × 4 ürün × 3 format = 72 frame. Metinler düzenlenebilir, Photo katmanı ayrı, kilitsiz.
- Higgsfield (Unlimited, nano_banana_2): hero ×4 (+NW yeniden), night ×4, desk ×4, set ×4 (Award Duo ilk denemede yanlış şişe → negatif "cylindrical bottles" ile düzeldi). Çıktılar `output/batch-09-competitor/`, format kırpımları `fmt/`.
- ChangedToo ve LeaveIt satırları müşteri PNG'leri + sitedeki gerçek önce/sonra fotoğraflarıyla (üretim yok).

## Öğrenilenler
- Nano Banana ürün boyu yüzdelerini (ör. "%17") büyük ölçüde yok sayıyor; ürün yine kadrajın %35–50'si çıkıyor. Formatlara oturtmak için Python kompozitör: ürünün üst kenarını hedef y'ye taşı, eksik alanı kenar piksel uzatma + ağır blur ile doldur, kenarları yumuşat (`scratchpad/compose.py` mantığı).
- Higgsfield mention seçimi: "@ss-xxx" yazdıktan sonra açılan listedeki öğeyi JS ile (span metni = element adı, parent'a mousedown/click) seç; koordinat tıklaması liste geç açılınca boşa düşüyor ve iş elementsiz gidiyor (etikete "@ss-netw" yazdı).
- Gece/lamba sahnelerinde lamba sol üstte çıkıyor → Story/Feed'de metin sağa yaslı kolon, Square'de üst scrim.
- ⚠ Meta politikası: vücut (selülit) önce/sonra görselleri reddedilebilir — LeaveIt DropOff yayın öncesi kontrol edilmeli.
