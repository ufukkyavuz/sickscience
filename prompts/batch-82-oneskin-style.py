"""Batch 82 — OneSkin-style organic Instagram grid, 24 posts (user 2026-10-30: "aynen bu şekilde... tüm 24 paylaşımı"). White-dominant, calm, science-led.
References: ~/sickscience-work/oneskin-1030/refs/01..24.jpg. Five images have no client shot; everything else is client photos + site copy.
4:5 masters, no text in the image. G5 uses mention ss-open-shapeshift."""
FIN = ("Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos.")
GEL = ("a translucent gel-serum - semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, slightly viscous, "
       "it holds a soft rounded bead and lets light pass through its edges")
P = {
'G1_microscope': f"""A real light-microscope photomicrograph of human skin cells, seen through the eyepiece.

COMPOSITION AND FRAMING
Vertical 4:5 frame. A single large circular microscope field fills 86% of the frame width and is centred. Inside the circle: a pale grey-blue stained cell layer with clearly visible polygonal cell borders and small round dark nuclei evenly spread, and fine darker fibres near the left and right edges of the circle. The centre of the circle is calm and even, for text. Outside the circle is plain soft white.

LIGHT AND SHADOW
Even transmitted microscope light, slightly brighter at the centre with soft natural vignetting at the rim of the circle.

BACKGROUND
Outside the circular field: clean near-white, nothing else.

PHOTOGRAPHIC FINISH
True histology photomicrograph, cool pale grey-blue monochrome tones, fine optical grain, scientific and calm. {FIN}

Negative: text, scale bar, labels, arrows, purple or pink stain, bright colours, dark background, eyepiece hardware, illustration, CGI, 3D render, watermark.""",

'G2_exosomes': f"""A real macro studio photograph that looks like a cluster of exosomes: hundreds of tiny, soft, pearly translucent spheres suspended in clear gel.

COMPOSITION AND FRAMING
Vertical 4:5 frame, extreme macro. Large soft out-of-focus spheres in the foreground corners, sharper small spheres behind them, filling the whole frame edge to edge. The centre third of the frame is the calmest area with soft even tone, for text.

LIGHT AND SHADOW
Soft diffuse white daylight, gentle pearly highlights on each sphere, very low contrast.

BACKGROUND
Only the spheres and the clear gel; the overall image is white and very pale grey.

PHOTOGRAPHIC FINISH
Macro lens, shallow depth of field, white monochrome with a faint cool tint, high-key, soft and clean. {FIN}

Negative: text, marshmallows, food, bubbles in water, colourful spheres, dark background, glitter, CGI look, 3D render, plastic beads, watermark.""",

'G3_gel_swirl': f"""A real macro studio photograph of a thick swirl of {GEL}, spread across a white surface with a smooth spatula stroke.

COMPOSITION AND FRAMING
Vertical 4:5 frame, overhead macro. Broad flowing ridges of the gel-serum sweep diagonally across the entire frame, edge to edge, with soft rounded peaks and glossy grooves.

LIGHT AND SHADOW
Soft directional daylight from the upper left; glossy highlights along the ridges; light passes through the thin edges.

BACKGROUND
Only the gel-serum and the white surface beneath it.

PHOTOGRAPHIC FINISH
Macro lens, everything sharp, neutral white, high-key, clean. {FIN}

Negative: text, opaque white cream, thick white lotion, whipped or peaked cream, body butter, water-clear liquid, fully transparent gel, coloured or gold serum, beige, dark background, watermark.""",

'G4_gel_fold': f"""A real macro studio photograph of a single large soft fold of {GEL}, one slow smear with a smooth rounded edge on a white surface.

COMPOSITION AND FRAMING
Vertical 4:5 frame, low angle macro. The smear enters from the lower left and ends in a soft rounded lip at the upper right, leaving the upper left quarter calm for text.

LIGHT AND SHADOW
Soft window daylight from the right, gentle glossy highlights, light passing through the thin edge of the smear, a faint soft shadow.

BACKGROUND
A clean white surface, softly falling out of focus.

PHOTOGRAPHIC FINISH
Macro lens at f/5.6, neutral white, high-key, clean. {FIN}

Negative: text, opaque white cream, thick white lotion, whipped or peaked cream, body butter, water-clear liquid, fully transparent gel, coloured or gold serum, beige, dark background, watermark.""",

'G5_topdown': f""" A real editorial product photograph in a bright white science lab featuring this element.

Match the element reference exactly for the open ShapeShift bottle: shape, colours, chrome finish, white pump and label layout. Exactly 1 product, no extra product. Every word printed on the bottle is pure white on the black stripe; never black, grey or dark text.

PRODUCT ORIENTATION
The open bottle lies on a clear rectangular glass lab tray, seen from a 45 degree angle above, label facing the camera. Beside it on the glass, a single soft swatch of {GEL}. No fisheye.

COMPOSITION AND FRAMING
Vertical 4:5 frame, 85mm lens. The glass tray runs diagonally across the frame. The bottle is in the upper right and the swatch in the lower left. Every object fits completely inside the frame.

SCALE
The bottle is 12 cm tall and 3.5 cm wide; the swatch is 6 cm long; the tray 30 cm long. If in doubt make the product smaller, never bigger.

LIGHT AND SHADOW
Bright soft daylight from the upper left, crisp clean glass reflections, a soft contact shadow. Every printed word stays in clear light.

BACKGROUND
A plain white lab bench, nothing else.

PHOTOGRAPHIC FINISH
Thin clear glass edges, polished chrome with true reflections of this white room, fine natural grain, bright airy high-key look. All product text must be perfectly legible, sharp, and accurate - no blurry or distorted letters. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos added to the scene (product labels only).

INTEGRATION
The product shares the scene's light direction and colour temperature; the chrome shows the real reflections of this white lab; a real contact shadow and faint reflection on the glass; same sharpness and grain as the rest of the frame; no outline or halo.

Negative: pasted or composited look, cut-out edges, sticker look, halo, floating product, stubby chubby or wide bottle, black letters, dark or grey text on the product, warped label, extra products, oversized product, headline, watermark, dark background, CGI, 3D render, opaque white cream, coloured serum.""",
}
if __name__ == '__main__':
    import json
    print(json.dumps(P, ensure_ascii=False))
