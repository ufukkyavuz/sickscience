# Batch 41 — New discount scenes with type that plays with the photo (2026-10-12)

User: "sitedeki indirimler için denemeler yap" + "olan fotoğrafı çalma, yeni yap". Existing photos (batch-19–21 Sculpted/Body/Head-to-Toe/OTG) are NOT reused. Each concept gets a new 9:16 master; Story, Feed and Square are crops of it.

Offers (checked on the site 2026-10-12, products.json; not used in D1–D3 / N1–N3):
- Head-to-Toe Transformation Duo (PowerCycle + DropOff): $116 → $104
- Sculpted Duo (ShapeShift + gua sha): $88 → $79
- Body Transformation Duo (DropOff + ShapeShift): $116 → $98
- ShapeShift on the Go (pouch + ShapeShift): $76 → $69
- Free shipping over $75 on every order above.
- BOGOS free-gift offers (tote / gua sha / pouch) are on the site in `"status":"test"` → hidden from customers, NOT advertised.

Production: Higgsfield web UI, Nano Banana Pro, 9:16, 2K, Unlimited. In the prompts `{@ss-…}` means mention the element in the composer. Gua sha is always the separate `@ss-guasha` element; the set element is not used for it.

## E1 — "Measured head to toe" (Head-to-Toe Duo, {@ss-set-head-to-toe})
Figma: the price sits on the tape like a measurement. A thin tick line plus "$116" (struck through) at one mark, "$104" in PowerCycle green at a lower mark. Headline "HEAD TO TOE, FOR $104." set in the top white space.
```
A real editorial top-down still-life photograph featuring {@ss-set-head-to-toe}.

Preserve the exact identity of both products: the PowerCycle capsule with a glossy metallic green chrome cap on the upper half and a mirror-polished silver chrome lower half, rounded pill silhouette, a narrow black stripe with vertical pure white text 'SickScience' and 'PowerCycle'; the matte cobalt-blue DropOff squeeze tube with its blue screw cap and vertical white text 'SickScience' and 'DropOff'. Use the element for identity only; never redraw the products. Exactly two products, no extra product. Every word printed on the products is pure white: on the PowerCycle capsule one continuous narrow black stripe runs along the whole capsule across the green cap AND the silver half, and both 'SickScience' and 'PowerCycle' are pure white letters on that black stripe — never black letters on silver.

PRODUCT ORIENTATION
Shot from directly above. A cream tailor's measuring tape runs straight down the frame from top to bottom, slightly right of centre, with plain blank tick marks and no printed numbers. The PowerCycle capsule lies flat horizontally across the tape near the top, label facing up and legible. The DropOff tube lies flat horizontally across the tape lower down, cap to the right, label facing up and legible. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
Vertical 9:16, 50mm lens straight down on a warm white matte plaster surface. The capsule sits at 26% to 31% of the frame height; the tube at 55% to 62%. The left 45% of the frame between 14% and 55% height is clean empty plaster for type to be added later. The bottom 35% is calm plaster with only the tape continuing. Every object fits completely inside the frame.

SCALE
The PowerCycle capsule is 14 cm long and 4.5 cm wide; the DropOff tube is 20 cm long and 4 cm wide; the tape is 2 cm wide. If in doubt make the products smaller, never bigger.

LIGHT AND SHADOW
Soft daylight from the upper left, short soft shadows to the lower right, crisp highlights in the chrome; no glare over any printed word.

BACKGROUND
Only warm white plaster and the tape. No other props.

PHOTOGRAPHIC FINISH
50mm at f/11, fine plaster grain, woven tape texture, polished chrome, matte plastic tube, high-key, restrained natural colour, graphic editorial. All product text perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail.

INTEGRATION
Same light direction and softness on every object, the chrome reflects the plaster and the tape, real contact shadows, same grain everywhere, no outline, no halo.

Negative: black letters on the silver half, text printed directly on silver without the black stripe, numbers printed on the tape, text added to the scene, extra products, capsules standing upright, stubby or chubby capsule, oversized products, black or grey letters on the products, misspelled text, coloured background, props, pasted or composited look, sticker look, halo, floating product, CGI, 3D render, orange or yellow cast, watermark.
```

## E2 — "The curve" (Sculpted Duo, {@ss-shapeshift} + {@ss-guasha})
Figma: "SCULPTED FOR $79" runs along the gua sha's curved edge as text on a path. "was $88" is struck through below it. TextPath is new in Figma.
```
A real fine-art editorial top-down still-life photograph featuring {@ss-shapeshift} and {@ss-guasha}.

Preserve the exact identity of both items: the ShapeShift capsule with a glossy metallic violet chrome cap on the upper half and a mirror-polished silver lower half, slim (height 3.4 times its width, cap exactly the upper half), a narrow black stripe with vertical pure white text 'SickScience' and 'ShapeShift'; the flat SOLID polished stainless-steel gua sha, silver metal, single-notch heart / wing shape with 'SickScience' engraved. Use the elements for identity only; never redraw them. Exactly two items, no extra product. Every word printed on the capsule is pure white.

PRODUCT ORIENTATION
Shot from directly above. The gua sha lies flat in the centre of the frame, its long smooth outer curve facing the upper left. The capsule lies flat diagonally in the lower right, cap pointing to the upper right, label facing up and legible. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
Vertical 9:16, 50mm lens straight down on smooth pale stone with a soft fold of ivory silk along the bottom edge. The gua sha sits at 38% to 52% of the frame height, horizontally centred; the capsule at 52% to 64%. Leave a clean band of plain stone about 6% of the frame wide around the gua sha's outer curve and keep 14% to 36% of the frame height empty for type to be added later. Every object fits completely inside the frame.

SCALE
The gua sha is only 9 cm long and 6 cm wide; the capsule is 12 cm long and 3.5 cm wide. The capsule is clearly LONGER than the gua sha: the gua sha's length is three quarters of the capsule's length, never bigger than the capsule. If in doubt make the items smaller, never bigger.

LIGHT AND SHADOW
Soft window light from the upper left, a crisp bright highlight running along the polished curve of the gua sha, soft contact shadows; no glare over any printed word.

BACKGROUND
Only pale stone and the silk fold. No other props.

PHOTOGRAPHIC FINISH
50mm at f/11, honed stone pores, silk sheen, mirror-polished steel, chrome, soft warm neutral palette, premium editorial. All product text perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail.

INTEGRATION
Same light on both items, the steel and chrome reflect the stone, real contact shadows, same grain, no outline, no halo.

Negative: gua sha bigger than the capsule, oversized gua sha, pink gua sha, rose quartz, jade, stone gua sha, translucent gua sha, melted shape, stubby, chubby or wide bottle, extra products, text added to the scene, black or grey letters on the product, oversized products, coloured background, props, pasted look, halo, floating product, CGI, 3D render, watermark.
```

## E3 — "Written in the steam" (Body Duo, {@ss-set-body-duo})
Figma: "$98" written in Permanent Marker (handwriting allowed by the concept) on the fogged mirror, with lowered opacity and the Texture effect so it reads as a finger drawing. Next to it "$116" is crossed out the same way. Headline in Founders below the price: "BODY DUO. SAVE $18."
```
A real editorial interior photograph featuring {@ss-set-body-duo}.

Preserve the exact identity of both products: the matte cobalt-blue DropOff squeeze tube with its blue screw cap and vertical white text 'SickScience' and 'DropOff'; the ShapeShift capsule with a glossy metallic violet chrome cap on the upper half and a mirror-polished silver lower half, PROPORTIONS ARE CRITICAL: slim and tall, height 3.4 times its width, cap exactly the upper half, never stubby, chubby or squat; vertical pure white text 'SickScience' and 'ShapeShift'. Use the element for identity only; never redraw the products. Exactly two products, no extra product. Every word printed on the products is pure white.

PRODUCT ORIENTATION
The tube stands upright on its cap and the capsule stands upright beside it on a white marble vanity ledge in the lower part of the frame, labels facing the camera. Camera at ledge height, straight on. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
Vertical 9:16, 50mm lens. A large frameless bathroom mirror fills the frame behind the ledge from the top down to about 60% of the frame height; its surface is evenly fogged with soft white steam condensation, a few fine droplets near the edges, completely blank, no writing, no reflection details readable. The ledge with the products sits at 58% to 75% of the frame height, products centred. The fogged mirror between 16% and 55% is clean and even for text to be added later. Every object fits completely inside the frame.

SCALE
The DropOff tube is 20 cm tall; the capsule is 12 cm tall and 3.5 cm wide. If in doubt make the products smaller, never bigger.

LIGHT AND SHADOW
Soft diffuse warm-white bathroom light from above left, gentle glow through the steam, soft contact shadows on the marble, crisp highlights in the chrome; no glare over any printed word.

BACKGROUND
Only the fogged mirror and the marble ledge, a set-built studio bathroom, premium and clean. No people, no faucet in front of the products.

PHOTOGRAPHIC FINISH
50mm at f/5.6, fine condensation texture, veined white marble, matte tube, polished chrome, airy high-key palette, campaign look. All product text perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail.

INTEGRATION
Same light on both products, the chrome reflects the fog and marble, real contact shadows, same grain, no outline, no halo.

Negative: stubby, chubby or wide capsule, writing or drawings on the mirror, letters in the fog, people, hands, reflections of a person, extra products, stubby capsule, oversized products, black or grey letters on the products, text added to the scene, dark scene, coloured background, pasted look, halo, floating product, CGI, 3D render, orange or yellow cast, watermark.
```

## E4 — "Departures" (ShapeShift on the Go, {@ss-otg-shapeshift})
Figma: the blank split-flap tiles are filled tile by tile with white Founders letters: "SHAPESHIFT ON THE GO" / "$76 → $69". Optional: a flap-flip animation with Motion and `export_video`.
```
A real editorial travel photograph featuring {@ss-otg-shapeshift}.

Preserve the exact identity of every item: the violet mesh zipper pouch with its small white 'SickScience' label, and the ShapeShift capsule with a glossy metallic violet chrome cap on the upper half and a mirror-polished silver lower half, slim (height 3.4 times its width), vertical pure white text 'SickScience' and 'ShapeShift'. Use the element for identity only; never redraw them. Exactly one pouch and one capsule, no extra product. Every word printed on the capsule is pure white.

PRODUCT ORIENTATION
The pouch lies flat on top of a closed pale-grey hard-shell carry-on suitcase that lies on its side on a polished terrazzo airport floor; the capsule stands upright on the suitcase next to the pouch, label facing the camera. Camera slightly above, straight on. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
Vertical 9:16, 50mm lens. Behind, softly out of focus, a classic black split-flap departure board fills the upper part of the frame from 14% to 46% height: rows of blank black flaps with no letters, numbers or symbols at all, no header, no 'Departures' title, no icons. The suitcase with the pouch and capsule sits at 52% to 72% of the frame height, centred. Every object fits completely inside the frame.

SCALE
The pouch is 21 cm wide and 16 cm tall; the capsule is 12 cm tall and 3.5 cm wide, so the capsule is SHORTER than the pouch (three quarters of the pouch height) and very slim; the carry-on is 55 × 40 cm, so the pouch covers less than half of the suitcase top. If in doubt make the products smaller, never bigger.

LIGHT AND SHADOW
Bright, soft daylight from tall windows on the left, gentle reflections on the terrazzo, crisp highlights on the chrome; no glare over any printed word.

BACKGROUND
Only the blank split-flap board and a bright, calm, modern terminal wall, softly out of focus. No people, no signs, no logos.

PHOTOGRAPHIC FINISH
50mm at f/4, mesh fabric texture, polished chrome, hard-shell texture, terrazzo, clean cool-neutral palette, premium editorial travel look. All product text perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail.

INTEGRATION
Same light on all items, the chrome reflects the terminal, real contact shadows on the suitcase, same grain and depth of field as the scene, no outline, no halo.

Negative: capsule taller than the pouch, oversized capsule, 'Departures' title, header text, plane icon, letters, numbers or symbols on the departure board, signs, airline logos, people, extra products, oversized capsule, stubby capsule, pouch in a different colour, black or grey letters on the products, text added to the scene, dark scene, pasted look, halo, floating product, CGI, 3D render, orange or yellow cast, watermark.
```
