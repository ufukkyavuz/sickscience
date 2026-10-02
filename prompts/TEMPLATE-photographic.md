# Fotografik görsel prompt şablonu (kullanıcı standardı, 2026-10-02)

Tüm fotografik (gerçekçi sahne) Higgsfield prompt'ları bu bölümlerle ve bu sırayla yazılır. Kaynak: kullanıcının verdiği "spa day" örnek prompt'u (aşağıda).

## Bölümler

1. **Açılış satırı** — "A real editorial lifestyle photograph featuring @element." (web UI'da @ss-… mention; API kaydında `<<<id>>>` olarak görünür)
2. **Kimlik koruma paragrafı** — her ürünün oranı, yapısı, renkleri ve baskılı markası birebir korunur; element sadece kimlik için kullanılır, ürün yeniden çizilmez. Ürüne özgü ayırt edici detaylar tek tek yazılır (ör. kapak şekli, halka, pompa). Set ise: "Exactly N products from the set, no extra product."
3. **PRODUCT ORIENTATION** — her ürünün nerede ve nasıl durduğu (dik / yatık / hangi yüz kameraya, yazı yönü), olmaması gereken duruşlar ("never upright, never standing on its end"). Kamera yüksekliği ve açısı. "No fisheye, no wide-angle distortion."
4. **COMPOSITION AND FRAMING** — sahne tipi, lens (85mm full-frame), zemin/yüzey, sol ve sağ yardımcı objeler, kahraman ürünün konumu, "Every object fits completely inside the frame", metin için boş bırakılan alan (yüzde olarak).
5. **SCALE** — her ürünün ve yardımcı objenin gerçek cm ölçüsü, en küçük ürünün diğerine oranı, "if in doubt make the products smaller, never bigger."
6. **LIGHT AND SHADOW** — ışığın yönü ve karakteri, yansımalar/kostikler hiçbir baskılı yazının üstüne düşmez, tüm yazılar aydınlık ve okunur, dolgu ışığı.
7. **BACKGROUND** — arka planda sadece ne olduğu; olmayacaklar (desen, merdiven, insan, gökyüzü…).
8. **PHOTOGRAPHIC FINISH** — diyafram, malzeme dokuları tek tek (taş gözenekleri, kumaş, cam, metal, plastik), optik derinlik, ince grain, doğal renk, ton (high-key vb.), "All product text stays perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail."
9. **Negative:** — virgülle ayrılmış liste: yanlış duruşlar, fazladan/uydurma ürün, sahte marka, yanlış yazım, ekstra yazı, büyük ürün, bulanık ürün, okunmaz yazı, istenmeyen objeler, renk kayması (orange/yellow cast), CGI, 3D render, plastik doku, HDR glow, watermark, sahneye uymayan şeyler.

## SickScience uyarlaması
- Proje kuralları geçerliliğini korur: yazısız üretim (Figma'da metin), ürün dokuları, model yaşı (30'lar), geniş açı insanlı kareler, renk kodları.
- Kapsül ürünler için kimlik detayı: "top half glossy metallic [violet/red/green] chrome cap, bottom half mirror-polished silver chrome, rounded pill silhouette, vertical white printed text on a black stripe". DropOff: "glossy cobalt squeeze tube standing on its blue screw cap".
- **SCALE ölçüleri (kullanıcı, 2026-10-02):** ShapeShift ve NetWork kapsül 12 cm boy / 3.5 cm çap · PowerCycle kapsül 14 cm boy / 4.5 cm çap · DropOff tüp ~20 cm boy · makyaj çantası/pouch 21 × 16 cm · tote 30 × 40 × 10 cm. Elde tutulan sahnede: "an adult palm is about 18 cm long, so the 12 cm capsule is about two-thirds of the hand length". Her zaman "if in doubt make the products smaller, never bigger" eklenir.

## Örnek (kullanıcının verdiği, birebir)

```
A real editorial lifestyle photograph featuring <<<178eed48-62f1-4d90-9551-6ce5b58e07e6>>>.

Preserve the exact identity of every item in the set: proportions, construction, colours and printed branding - the bag keeps its own logo exactly as the element shows it. Use the element for identity only; place it as described below without redrawing any part of it. The balm keeps its own short, wide silver cap and round metal key ring exactly as the element shows it. Exactly four products from the set, no extra product.

PRODUCT ORIENTATION

The closed bag of the set stands upright on the stone pool edge, front face to the camera, logo reading horizontally. The two tubes lie on a rolled white towel at slightly different angles, the stick stands upright beside them, and the balm lies flat on the stone in front, its whole length touching the stone, never upright, never standing on its end. Camera about 25 degrees above, low and close. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING

Vertical 'spa day' scene with an 85mm full-frame lens. A pale honed limestone pool edge runs across the lower half of the frame, with calm clear pale-aqua water just behind it showing soft caustic light ripples. On the LEFT, a neatly rolled white waffle towel. On the RIGHT, a clear glass of water with a thin slice of cucumber and a pair of white terry slippers. The set sits in the lower-centre as the hero. Every object fits completely inside the frame. Keep the upper 30% of the frame as soft out-of-focus water for text to be added later.

SCALE

The bag of the set is 32cm wide and 18cm tall. The two tubes are 12cm tall. The balm is 9cm long. The stick is 4cm tall - one third of a tube, the smallest item. The glass is about 12cm tall. Keep these real proportions; if in doubt make the products smaller, never bigger.

LIGHT AND SHADOW

Bright soft daylight from the upper left, out of frame, with delicate rippling caustic reflections from the water dancing on the stone, never covering any printed word. Keep every printed word on the products and the bag in clear light and fully legible. Soft white bounce; no dark fill.

BACKGROUND

Only the calm pale water of the pool behind the stone edge, softly out of focus, no tiles pattern, no ladder, no people, no sky.

PHOTOGRAPHIC FINISH

85mm lens at f/8. Honed limestone with fine pores, waffle cotton, terry loops, thin clear glass with condensation, clear water caustics, real fabric on the bag, metal and plastic finishes on the products. Subtle optical depth, fine photographic grain, restrained natural colour, bright airy high-key look. All product text stays perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail.

Negative: upright balm, balm standing on its end, extra products, redrawn or invented products, fake brand names, misspelled text, any word printed on the bag other than its own logo, long thin or pointed balm cap, missing key ring, bag rotated onto its side, oversized products, blurred product, unreadable text, window, window frame, dark or grey scene, orange or yellow colour cast, CGI, 3D render, plastic textures, HDR glow, extra text, watermark, sea, beach, people swimming, wet or dripping products.
```
