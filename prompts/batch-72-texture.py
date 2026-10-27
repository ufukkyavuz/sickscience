"""Batch 72 — texture videos (user 2026-10-21: "ürün dokusunu gösteren videolar, doku görünce satın alma isteği artıyor").
Clean white, scientific, restrained (feedback-video-clean-scientific). First frames in Higgsfield (Nano Banana Pro 2K Unlimited, 9:16),
then Veo 3.1 Fast image-to-video in Flow (silent motion), then code overlays (Founders Grotesk) + generated packshot end card.
Gel: translucent milky gel-serum (feedback-product-texture-gel-serum). Bottles redraw badly in video → texture is the hero, bottle partial or out of frame."""
import json
GEL = ("a translucent gel-serum - semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, "
       "slightly viscous, it holds a soft rounded bead and lets light pass through its edges")
CAP = ("PROPORTIONS ARE CRITICAL: a slim, tall capsule with fully rounded ends at the top AND the bottom; the coloured chrome cap is exactly the upper half "
       "and the mirror-silver body exactly the lower half. A narrow vertical BLACK stripe runs the full height, and every word is printed vertically in pure "
       "white on that black stripe - never text directly on the chrome, never black or grey letters.")
SCI = ("BACKGROUND\nA bright, clean white laboratory bench: white matte surface, soft white seamless wall, one clear glass element (a glass slide or petri dish) "
       "as the only prop; airy, clinical, scientific, premium; nothing else.")
FIN = ("PHOTOGRAPHIC FINISH\nUltra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail, macro lens, shallow depth of field. "
       "All product text must be perfectly legible, sharp, and accurate - no blurry or distorted letters. No text, no letters, no logos added to the scene "
       "(product labels only).")
INT = ("INTEGRATION\nThe product and gel share the scene's soft daylight; real reflections in the chrome and in the gel; real contact shadows; same sharpness "
       "and grain everywhere; no outline or halo.")
NEG = ("Negative: opaque white cream, thick white lotion, whipped or peaked cream, body butter, water-clear liquid, fully transparent gel, coloured or gold "
       "serum, pasted or composited look, cut-out edges, halo, stubby chubby or flat-bottomed bottle, black or grey letters on the product, warped label, "
       "added text, watermark, CGI, 3D render, cartoon, clutter, dark background, coloured background.")
HAND = ("The hand belongs to a woman in her late 20s: slim fingers, natural short nude manicure, smooth realistic skin with natural texture. Exactly one hand.")
X = {
 'T1_ss_pump': ["Match the ELEMENT reference exactly for the ShapeShift bottle: shape, purple chrome cap, silver body and label layout.", HAND,
   "PRODUCT ORIENTATION\nThe ShapeShift bottle is OPEN: the purple cap is off and lies beside it; a white pump head sits on the silver body. "
   "A single fingertip rests just under the pump nozzle, and one soft rounded bead of " + GEL + " sits on the fingertip, catching the light. " + CAP,
   "COMPOSITION AND FRAMING\nVertical 9:16 macro, camera at fingertip height. The fingertip with the gel bead is the hero at the centre of the frame (45-60% height); "
   "the bottle body and pump are on the right, partly cropped by the frame edge; the top 35% is clean white wall.",
   "SCALE\nThe bottle is 3.5 cm wide; the gel bead about 8 mm across.", "LIGHT AND SHADOW\nSoft bright window daylight from the left, a crisp specular highlight on the gel bead, light passing through its edge.",
   SCI, FIN, INT, NEG],
 'T2_ss_swipe': ["No product appears; a scientific macro texture photograph.", HAND,
   "PRODUCT ORIENTATION\nOn a clear glass slide lying on the white bench, a fingertip has just drawn a smooth, glossy swipe of " + GEL + "; "
   "the swipe is a short comet-shaped stroke with a thicker rounded head, its thin tail showing the white bench through the gel.",
   "COMPOSITION AND FRAMING\nVertical 9:16 macro, camera 30 degrees above the slide. The gel swipe sits in the centre (45-65% height); the fingertip "
   "is lifting away at the end of the stroke; the top 35% is soft out-of-focus white.",
   "SCALE\nThe swipe is about 4 cm long.", "LIGHT AND SHADOW\nSoft daylight from behind-left so the gel glows at its edges and shows its translucency; a subtle caustic on the glass.",
   SCI, FIN, INT, NEG],
 'T3_nw_stretch': ["Match the ELEMENT reference exactly for the NetWork bottle: shape, red chrome cap, silver body and label layout. The label reads exactly 'NetWork' with a capital N and a capital W.", HAND,
   "PRODUCT ORIENTATION\nThe thumb and index finger are slowly pulling apart a small amount of " + GEL + " with a very subtle pearly shimmer, "
   "forming a glossy translucent strand between them; the closed NetWork bottle stands behind on the bench, softly out of focus, label facing the camera. " + CAP,
   "COMPOSITION AND FRAMING\nVertical 9:16 macro. The fingers and the gel strand are the hero in the centre (40-60% height); the bottle stands lower right "
   "in soft focus; the top 35% is clean white.",
   "SCALE\nThe bottle is 12 cm tall and 3.5 cm wide, small behind the hand; the strand about 2 cm long.",
   "LIGHT AND SHADOW\nBright soft daylight from the right, backlighting the strand so its pearly translucency glows.", SCI, FIN, INT, NEG],
 'T4_pc_drop': ["Match the ELEMENT reference exactly for the open PowerCycle bottle with its dropper: green chrome cap removed, silver body, white dropper bulb.",
   "No person's face appears; only a hand holds the dropper. " + HAND,
   "PRODUCT ORIENTATION\nThe PowerCycle glass dropper is held vertically above a clear glass petri dish on the white bench; one rounded drop of " + GEL +
   " hangs from the pipette tip, about to fall; in the dish a small round puddle of the same gel already rests, its edge glowing.",
   "COMPOSITION AND FRAMING\nVertical 9:16 macro. The pipette tip with the hanging drop is at the centre (40-50% height), the dish below it at 60-70%; "
   "the open silver bottle body stands at the lower right edge, partly cropped; the top 30% is clean white.",
   "SCALE\nThe drop about 6 mm; the petri dish 9 cm across.", "LIGHT AND SHADOW\nSoft daylight from behind so the drop is backlit and translucent.", SCI, FIN, INT, NEG],
 'T5_do_ribbon': ["Match the ELEMENT reference exactly for the DropOff tube: cobalt-blue matte squeeze tube, white vertical text 'SickScience' and 'DropOff'.", HAND,
   "PRODUCT ORIENTATION\nThe hand gently squeezes the DropOff tube held at a low angle; a smooth glossy ribbon of " + GEL +
   " flows from the tube tip and coils softly onto a clear glass plate on the white bench.",
   "COMPOSITION AND FRAMING\nVertical 9:16 macro. The coil of gel on the glass is the hero at the centre (50-65% height); the tube tip and the hand enter "
   "from the upper right, the tube's text readable; the top 25% is clean white.",
   "SCALE\nThe tube is 4 cm wide; the gel coil about 3 cm across.", "LIGHT AND SHADOW\nSoft daylight from the left, the ribbon glossy with a long specular highlight and translucent edges.",
   SCI, FIN, INT, NEG],
}
# Veo 3.1 Fast (Flow) motion prompts, image-to-video, 8 s, 9:16, silent (no dialogue)
VEO = {
 'T1_ss_pump': "Macro. The fingertip slowly lifts the gel bead toward the camera; the bead wobbles slightly and stays a soft rounded bead; the bottle and pump stay perfectly still. Locked camera with a very slow push-in. No speech, no music.",
 'T2_ss_swipe': "Macro. The fingertip slowly drags through the gel and pulls it into a longer glossy swipe across the glass; the gel smooths out and glows translucent at the edges. Slow camera slide left to right. No speech, no music.",
 'T3_nw_stretch': "Macro. The thumb and index finger slowly pull apart and the glossy pearly gel strand stretches thinner, then they press back together and rub gently. The bottle in the background stays still and unchanged. No speech, no music.",
 'T4_pc_drop': "Macro, slow motion. The single drop slowly grows, detaches from the pipette tip, falls and lands in the gel in the petri dish with a small soft ripple. Locked camera. No speech, no music.",
 'T5_do_ribbon': "Macro, slow motion. The gel ribbon keeps flowing smoothly from the tube tip and coils onto the glass, glossy and translucent; the tube text stays readable and unchanged. Very slow push-in. No speech, no music.",
}
if __name__ == '__main__':
    open('/private/tmp/claude-501/p72.js', 'w').write('window.__p72=' + json.dumps(X) + ';window.__v72=' + json.dumps(VEO) + ';"ok"')
    print(list(X))
