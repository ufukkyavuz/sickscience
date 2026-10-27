"""Batch 60 — Amazon Store featured ShapeShift image (user 2026-10-20: "burda aynı fotoyu kullanmışsın bunu değiştir").
Must differ from the lab still life used in the product tile. Square 1:1 (slot 1500x1500). Template sections.
Element mention typed in the composer where ELEMENT appears (ss-shapeshift)."""
import json
LABEL="Every word printed on the product is pure white on the black stripe - on the coloured cap AND on the silver half; never black, grey or dark text. The labels read exactly 'SickScience' and 'ShapeShift'."
PROP="PROPORTIONS ARE CRITICAL: slim and tall capsule, height 3.4x its width, the purple chrome cap is exactly the upper half, the mirror-chrome silver base the lower half, rounded pill ends; never stubby, chubby, squat or wide."
TEX="Gel texture: a translucent gel-serum - semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, slightly viscous, it holds a soft rounded bead and lets light pass through its edges."
FIN="PHOTOGRAPHIC FINISH\nUltra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. All product text must be perfectly legible, sharp, and accurate - no blurry or distorted letters. Realistic skin with natural pores and fine texture, no plastic retouching, fine photographic grain. No text, no letters, no logos added to the scene (product labels only)."
INT="INTEGRATION\nThe product shares the scene's light direction, softness and colour temperature; the chrome shows the real reflections of this set, not a studio softbox; a real contact shadow and a faint reflection on the surface it stands on; same sharpness and grain as the rest of the frame; no outline or halo."
NEG_COMMON="pasted or composited look, cut-out edges, sticker look, halo, product lit differently, floating product, stubby chubby or wide bottle, black letters, dark or grey text on the product, extra products, warped label, distorted anatomy, extra fingers, more than two arms, CGI, 3D render, watermark, headline text"
X={
'A_model':[
 "Match the ELEMENT reference exactly for the product: shape, colours, chrome finish and label layout.",
 "The model is a strikingly beautiful woman in her late 20s with model-like features, bare shoulders, hair sleekly pulled back. Realistic skin with natural pores. Exactly two arms.",
 "PRODUCT ORIENTATION\nThe ShapeShift capsule stands upright, cap on top, label facing the camera, on a sculptural white stone plinth beside her shoulder. "+PROP+" "+LABEL,
 "COMPOSITION AND FRAMING\nSquare frame, 50mm, chest-up. She is in three-quarter profile facing left, chin lifted, fingertips of one hand sweeping upward along her jawline as if smoothing in a serum; a soft glossy sheen of gel-serum on the jaw. The capsule on its plinth sits at the lower right, at the same distance from the camera as the model, its top at the height of her chin. Calm negative space at the upper left. "+TEX,
 "SCALE\nThe capsule is 12 cm tall and 3.5 cm wide - about two thirds of the length of her hand; her face is far larger than the bottle. If in doubt make the product smaller, never bigger.",
 "LIGHT AND SHADOW\nBright campaign studio light: a large soft key from the upper left, white bounce fill, clean neutral white balance, soft natural shadow under the jaw.",
 "BACKGROUND\nA built studio set: warm-white plaster wall with a soft gradient of light, a curved white stone plinth; nothing else.",
 FIN, INT,
 "Negative: "+NEG_COMMON+", product in hand, product close to the camera, giant bottle, heavy makeup, warm yellow tone, dim moody light."],
'B_still':[
 "Match the ELEMENT reference exactly for the product: shape, colours, chrome finish and label layout.",
 "No person appears in this image; this is a premium editorial product still life.",
 "PRODUCT ORIENTATION\nThe ShapeShift capsule leans at a gentle 15 degree angle against a smooth block of white travertine, cap on top, label facing the camera. "+PROP+" "+LABEL,
 "COMPOSITION AND FRAMING\nSquare frame, 85mm, camera at product height. The capsule is in the centre-right third; in front of it on the stone a single glossy bead and a short swipe of gel-serum. Behind, a soft blurred shadow of a palm leaf falls across the wall. Calm negative space at the upper left. "+TEX,
 "SCALE\nThe capsule is 12 cm tall and 3.5 cm wide; the travertine block is about 20 cm tall; the gel bead about 1.5 cm.",
 "LIGHT AND SHADOW\nCrisp directional daylight from the upper right through a window, casting a long soft leaf shadow and a clean shadow of the bottle on the stone; bright, airy, neutral white.",
 "BACKGROUND\nPale lilac-white plaster wall, softly textured, out of focus; nothing else.",
 FIN, INT,
 "Negative: "+NEG_COMMON+", laboratory glassware, beakers, flasks, pineapple, people, hands, opaque white cream, water-clear liquid, coloured or gold serum, dark background."],
}
if __name__=='__main__': json.dump(X,open('/private/tmp/claude-501/p60.json','w'),indent=1); print('\n\n'.join(X['A_model']))
