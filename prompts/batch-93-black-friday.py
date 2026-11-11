# Batch-93: Black Friday, Pinterest panosu uyarlamaları (2026-11-02)
# Pano: tr.pinterest.com/ufukkyavuz51/sickscience. Fiyatlar 2026-11-02 products.json, mevcut set indirimleri.
# Her kare kendi yönünde; görsel yazısız, metin Figma'da sahneye yedirilir.
# Pin -> konsept:
# R5  cam fanus + alttan ışık  -> V1 Vault Value Set $144/$180 20% OFF
# R10 ışık halkası             -> A1 Award-Winning Duo $108/$128 SAVE $20
# R13 yukarıdan uzanan el, kutu -> S1 Sculpted Duo $79/$88 SAVE $9
# R4  cam balonlar, ürün önde  -> G1 GLP-1 Facial Recovery System $137/$162 SAVE $25

CAPSULE = ("Each capsule bottle is a slim rounded pill: the glossy metallic coloured chrome cap is exactly the upper half, "
           "the lower half is mirror-polished silver chrome, with one full-height black vertical stripe carrying vertical text. "
           "Every word printed on the products is pure white on the black stripe, on the coloured cap AND on the silver half; never black, grey or dark text. "
           "All product text must be perfectly legible, sharp, and accurate, no blurry or distorted letters.")
END = "Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos added to the scene; only the products' own printed labels."
INTEG = ("INTEGRATION\n\nThe products are photographed in this scene with the same light direction, softness and colour temperature; their chrome reflects this environment, "
         "not a generic studio; real contact shadow and reflection; same sharpness and grain as the scene; no outline, no halo.")
NEG = "stubby, chubby or wide bottle, cap shorter or longer than half, black letters, dark or grey text on the product, misspelled text, extra products, pasted or composited look, cut-out edges, sticker look, halo, floating product, CGI, 3D render, watermark, added text"

PROMPTS = {
"V1": [("Mentions", "ss-powercycle ss-dropoff ss-shapeshift"), ("Body", f"""A real high-end science campaign photograph featuring [M1], [M2] and [M3]. The idea: the formulas are sealed like a precious specimen, and tonight the vault is opening. Capture the exact moment the tall glass bell jar has just lifted a few centimetres off its base and a thin cold vapour spills out over the floor.

Preserve the exact identity of every product: proportions, construction, colours and printed branding. The elements are the absolute source of truth for the products; use them for identity only, never redraw them. {CAPSULE} The green capsule is visibly the biggest capsule, 17% taller and 25% wider than the violet capsule. The cobalt matte tube stands on its blue screw cap with white vertical text. Exactly three products, no extra product.

PRODUCT ORIENTATION

The three products stand upright side by side inside the glass jar on a round polished steel plinth: green capsule on the left, cobalt tube in the middle, violet capsule on the right. Labels face the camera, text vertical. Camera low, at the height of the middle of the products, level and straight on.

COMPOSITION AND FRAMING

Dark science laboratory, 50mm lens. The glass bell jar is the hero, horizontally centred, occupying the band from 30% to 72% of the frame height and the middle 58% of the frame width. Out-of-focus glass laboratory columns stand far behind on both sides. The top 28% of the frame is calm dark space for a headline.

SCALE

Violet capsule 12 cm tall and 3.5 cm wide. Green capsule 14 cm tall and 4.5 cm wide. Cobalt tube 20 cm tall. The jar is 34 cm tall and 22 cm wide, so the tube is a little over half of the jar height.

LIGHT AND SHADOW

A cold white light ring hidden in the plinth lights the products from below and the jar glass catches long clean vertical highlights. A soft frontal fill keeps every printed word bright and readable. Everything outside the jar falls to deep blue-black.

BACKGROUND

Only deep blue-black space with soft blurred glass columns. No windows, no people, no pattern.

PHOTOGRAPHIC FINISH

f/8. Thick clear borosilicate glass with real refraction at the rim, brushed steel plinth, vapour that is thin and real and stays below the labels, reflections slightly softer than the objects. Fine photographic grain. {END}

{INTEG}

KEY COMPOSITION

ONE LIFTED GLASS BELL JAR, THREE UPRIGHT PRODUCTS WITH READABLE WHITE LABELS, COLD LIGHT FROM BELOW, DARK LAB.

Negative: {NEG}, green capsule same size as violet capsule, fog covering labels, warm colour cast, hands, people.""")],

"A1": [("Mentions", "ss-shapeshift ss-powercycle"), ("Body", f"""A real editorial product campaign photograph featuring [M1] and [M2]. The idea: two award winners stand inside a blazing ring of light, like a portal switched on for one night only.

Preserve the exact identity of both products: proportions, construction, colours and printed branding. The elements are the absolute source of truth; use them for identity only, never redraw them. {CAPSULE} The green capsule is visibly bigger, 17% taller and 25% wider than the violet capsule. Exactly two products, no extra product.

PRODUCT ORIENTATION

Both capsules stand upright on a black mirror floor, close together and very slightly turned toward each other, labels readable, text vertical. Camera low near floor level looking slightly up.

COMPOSITION AND FRAMING

28mm lens for monumental presence, product closest to the camera. A perfect circle made of many separate bright white LED points stands behind the products, horizontally centred, its diameter 78% of the frame width, its centre at 50% of the frame height. The capsules stand in the centre of the ring, from 34% to 72% of the frame height. The space inside the ring stays dark around the products.

SCALE

Violet capsule 12 cm tall and 3.5 cm wide, green capsule 14 cm tall and 4.5 cm wide. The light ring is 40 cm across, so the green capsule reaches about one third of the ring diameter in real life and looks larger because it is close to the lens.

LIGHT AND SHADOW

The ring is the main light and draws two clean vertical highlights along each chrome capsule. A soft low front fill keeps every printed word bright. The ring and capsules reflect sharply in the black floor with soft falloff.

BACKGROUND

Pure black studio with a faint silver haze around the ring. Nothing else.

PHOTOGRAPHIC FINISH

f/11, gentle bloom only on the LED points, polished black acrylic floor with very fine dust, mirror chrome with true ring reflections. Fine photographic grain. {END}

{INTEG}

KEY COMPOSITION

ONE WHITE LED RING, ONE VIOLET AND ONE LARGER GREEN CAPSULE INSIDE IT ON BLACK MIRROR.

Negative: {NEG}, broken ring, oval ring, coloured light, neon tube, green capsule same size as violet capsule, people, hands.""")],

"S1": [("Mentions", "ss-shapeshift ss-guasha"), ("Body", f"""A real luxury campaign photograph featuring [M1] and [M2]. The idea: an elegant silhouetted hand reaches in from above and lifts the last one out of its black box. Capture the exact moment the capsule clears the box.

Preserve the exact identity of both products. The elements are the absolute source of truth; use them for identity only, never redraw them. {CAPSULE} The gua sha is a flat SOLID polished stainless-steel tool. Exactly two products, no extra product.

PRODUCT ORIENTATION

A woman's single hand comes straight down from the top of the frame and pinches the violet capsule by its rounded cap between thumb and two fingers, label facing the camera, text vertical. The capsule hangs vertically just above an open matte black box whose lid flaps fold outward. The steel gua sha rests flat against the front of the box. Camera low and level with the capsule.

COMPOSITION AND FRAMING

35mm lens, close to the box so it feels monumental. The box sits on a seamless floor, horizontally centred, from 58% to 84% of the frame height. The capsule hangs from 36% to 58%. The dark forearm enters from the top edge. The band from 12% to 32% stays clean on both sides of the arm for a headline.

SCALE

The capsule is 12 cm tall and 3.5 cm wide, about two-thirds of the adult hand length. The gua sha is 9 cm long. The box is 16 cm wide and 16 cm tall.

LIGHT AND SHADOW

The arm and hand are rimmed by a thin cold light and read almost as a black silhouette. A soft gradient of pale steel blue behind the box glows brighter near the floor. A soft front light keeps every printed word on the capsule bright.

BACKGROUND

Smooth gradient from deep slate blue at the top to pale cold grey-blue at the horizon. A soft horizon, no wall edges, no props.

PHOTOGRAPHIC FINISH

f/8. Matte box board with fine paper grain, mirror chrome, brushed steel, natural hand with short clean nails. Fine photographic grain. {END}

{INTEG}

KEY COMPOSITION

ONE SILHOUETTED HAND FROM ABOVE LIFTS ONE VIOLET CAPSULE OUT OF AN OPEN BLACK BOX, STEEL GUA SHA AGAINST THE BOX.

Negative: {NEG}, second hand, extra fingers, malformed hand, pink gua sha, rose quartz, jade, stone, translucent, melted shape, table edge.""")],

"G1": [("Mentions", "ss-network-v2 ss-shapeshift ss-guasha"), ("Body", f"""A real science editorial photograph featuring [M1], [M2] and [M3]. The idea: the protocol assembled on the lab bench, three steps standing among clean glass. Monochrome silver world where the only colours are red and violet.

Preserve the exact identity of every product. The elements are the absolute source of truth; use them for identity only, never redraw them. {CAPSULE} The label reads exactly 'NetWork' with a capital N and a capital W. The gua sha is a flat SOLID polished stainless-steel tool. Exactly three products, no extra product.

PRODUCT ORIENTATION

The red capsule and the violet capsule stand upright side by side in the foreground, labels facing the camera, text vertical. The steel gua sha leans against the base of the red capsule. Camera at product height, straight on.

COMPOSITION AND FRAMING

100mm lens, compressed perspective. Two large clear glass flasks stand behind the products, softly out of focus: a round-bottom flask on the left and a conical flask on the right, both overlapping the frame edges. The products are horizontally centred, from 42% to 76% of the frame height, sharp. The top 34% of the frame is calm soft grey gradient for a headline.

SCALE

Both capsules are 12 cm tall and 3.5 cm wide. The gua sha is 9 cm long. The flasks are about 25 cm tall.

LIGHT AND SHADOW

Soft top-left window-like key with a dark gradient toward the lower edge, as in fine silver photography. Clean vertical highlights on the chrome. Every printed word stays in clear light.

BACKGROUND

Cold neutral grey gradient, glass only. No other equipment, no people.

PHOTOGRAPHIC FINISH

f/5.6, the glass melting softly into the background with thin bright edges, glossy black bench with a subtle reflection under each product. Fine photographic grain, restrained colour. {END}

{INTEG}

KEY COMPOSITION

RED AND VIOLET CAPSULE WITH STEEL GUA SHA, SHARP IN FRONT OF SOFT CLEAR FLASKS, SILVER MONOCHROME WORLD.

Negative: {NEG}, 'Network' with a lowercase w, pink gua sha, rose quartz, jade, stone, translucent, melted shape, liquid inside flasks, coloured liquid, warm colour cast.""")],
}

# Sonuç (2026-11-02). Görseller _calisma/batch-93-black-friday/, Figma Kasım 2026 section 1524:49 (BF1-BF8, referans + Feed + Story).
# İlk dört prompt yukarıda. Diğerleri aynı şablonla, Higgsfield geçmişinde tam metin:
# BF5 Head-to-Toe Duo = H1 374771d0 (R1, 85mm buz mavi cam lab, cam disk) $104/$116
# BF6 DropOff On-the-Go = D1 dd72ba9e (R12, 40mm siyah tezgâh, sert ışık hüzmesi) $57/$64
# BF7 PowerCycle On-the-Go = P1 fb7986db (R9, 24mm çok yakın, beyaz/siyah diyagonal) $69/$76
# BF8 Teaser = T1 d1ddda97 (R7, 100mm makro, cam üstünde jel-serum, arkada bulanık kapsül)
# Yazı efektleri: BF1/BF2 sahne ışığına uygun glow; BF7 diyagonalde, BF8 kapsül içinde ters renk (mask + TEXT, düzenlenebilir).
# Açık: BF1 Feed Figma Expand bekliyor (ekran kilitliydi). Kaynak 1527:81, sayfada x=20000. Şu an jar kırpılıyor.
# Panoda işlenmeyen pinler: R2 R3 R6 R8 R11 R14 R15 R16 R17 R18.
