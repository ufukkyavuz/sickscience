"""Batch 67 — extra competitor formats not in the user's 5 refs (2026-10-20).
H_bagcheck: Grüns "Game day bag check ✅" -> top-down tote flat lay, checkmarks added in Figma (mention ss-tote + 4 products).
I_ss_swirl: SpoiledChild "2 Biotin Gummies = Best Hair & Nails Ever" creamy splash composition -> ShapeShift in gel-serum swirl with pineapple (mention ss-shapeshift).
"Of the Year" blue card = Figma only (real PNG + official Esquire badge), no generation. Shrek-style licensed idea skipped (needs IP licence)."""
import json
WHITE = ("Every word printed on the products is pure white on the black stripe - on the coloured cap AND on the silver half; never black, grey or dark text. "
         "The label reads exactly 'NetWork' with a capital N and a capital W.")
GEL = ("a translucent gel-serum - semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, slightly viscous, "
       "it holds a soft rounded bead and lets light pass through its edges")
FIN = ("PHOTOGRAPHIC FINISH\nUltra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. All product text must be perfectly legible, "
       "sharp, and accurate - no blurry or distorted letters. Fine natural grain. No text, no letters, no logos added to the scene (product labels only).")
INT = ("INTEGRATION\nThe products share the scene's light direction, softness and colour temperature; the chrome shows the real reflections of this set; "
       "a real contact shadow where each touches a surface; same sharpness and grain as the rest of the frame; no outline or halo.")
NEG = ("Negative: pasted or composited look, cut-out edges, sticker look, halo, floating product, stubby chubby or wide bottle, black letters, dark or grey "
       "text on the product, warped label, misspelled label, extra SickScience products, text, headline, watermark, CGI, 3D render, cartoon")
X = {
 'H_bagcheck': [
   "Match the ELEMENT references exactly for the tote bag and the four products: shape, colours, chrome finish and label layout. Exactly one tote and exactly four SickScience products, no extra product.",
   "No person appears; a styled top-down flat lay of what's inside a stylish woman's tote bag.",
   "PRODUCT ORIENTATION\nThe holographic tote lies open at the top of the frame, slightly angled. Spread neatly below it on the surface, each with clear space around it: the ShapeShift (violet) and NetWork (red) capsule bottles lying flat, the PowerCycle (green) capsule lying flat, the DropOff cobalt tube lying flat, plus sunglasses, a phone face-down, keys, wired earbuds and a lip balm. PROPORTIONS ARE CRITICAL: ShapeShift and NetWork are slim capsules, height 3.4 times width, coloured cap exactly the upper half. Labels face up. " + WHITE,
   "COMPOSITION AND FRAMING\nVertical 9:16 frame, perfectly top-down. The tote fills the top 30% of the frame; the items are laid out in a loose grid across the middle 15-75% of the frame with generous gaps between them (room for small checkmarks next to each); the bottom 25% is the same calm empty surface.",
   "SCALE\nTote 30 x 40 cm. Capsules 12 cm and 14 cm long, DropOff tube 20 cm, sunglasses 14 cm, phone 15 cm. Real relative sizes; if in doubt make the products smaller, never bigger.",
   "LIGHT AND SHADOW\nBright soft daylight from the upper left, soft natural contact shadows, crisp chrome highlights.",
   "BACKGROUND\nA pale lilac linen surface, smooth and even; nothing else.",
   FIN, INT, NEG + ", clutter, overlapping items, people, hands."],
 'I_ss_swirl': [
   "Match the ELEMENT reference exactly for the ShapeShift bottle: shape, colours, chrome finish and label layout.",
   "No person appears; a juicy, energetic beauty hero still life.",
   "PRODUCT ORIENTATION\nThe closed ShapeShift bottle stands upright in the lower middle, label facing the camera, rising out of a soft sculpted swirl of " + GEL + ", which curls in a glossy wave around its base. Around it: two fresh golden pineapple chunks and a few glistening droplets of the same gel-serum. PROPORTIONS ARE CRITICAL: slim and tall, height 3.4 times width, the violet cap is exactly the upper half; never stubby, chubby or squat. " + WHITE.split(' The label')[0],
   "COMPOSITION AND FRAMING\nVertical 9:16 frame, camera straight on at bottle height. The bottle and swirl sit between 45% and 72% of the frame height, centred; the top 40% is clean soft lilac background for a headline; the bottom 25% calm.",
   "SCALE\nThe bottle is 12 cm tall and 3.5 cm wide; the pineapple chunks about 3 cm. If in doubt make the product smaller, never bigger.",
   "LIGHT AND SHADOW\nBright soft studio key from the upper left, glossy highlights on the gel and chrome, soft shadow.",
   "BACKGROUND\nSeamless soft lilac-to-white gradient studio backdrop; nothing else.",
   FIN, INT, NEG + ", opaque white cream, whipped cream, body butter, water-clear liquid, coloured or gold serum, milk splash."],
}
if __name__ == '__main__':
    open('/private/tmp/claude-501/p67.js', 'w').write('window.__p66=Object.assign(window.__p66||{},' + json.dumps(X) + ');"ok"')
    print(list(X))

# H2 (2026-10-20): H v1 capsules came out stubby (length/width ~2.8, must be 3.4) and sunglasses cut at the frame edge.
# H2_bag replaces the PROPORTIONS sentence with: "ShapeShift and NetWork are SLIM, LONG capsules exactly 12 cm long and 3.5 cm wide
# (length 3.4 times width - like a long slim pill, never stubby or chubby) ... PowerCycle 14 x 4.5 cm; DropOff tube 20 cm long.
# All items fully inside the frame with margin, nothing cut off at the edges."
