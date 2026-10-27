"""Batch 70 — contextual photo scenes for the batch-69 ads (user 2026-10-21: "hep png kullanmışsın, içeriğe uygun görsel üret";
NetWork dark scene "hem foto kötü hem ürün yanlış" - the model drew no black stripe, text straight on chrome, short cap, flat bottom).
All 9:16, Nano Banana Pro 2K Unlimited, element mention first. Copy goes on in Figma (glass UI)."""
import json
CAP = ("PROPORTIONS ARE CRITICAL: a slim, tall capsule with fully rounded ends at the top AND the bottom, height 3.4 times its width; the "
       "coloured chrome cap is exactly the upper half and the mirror-silver body exactly the lower half. A narrow vertical BLACK stripe runs the "
       "full height of the bottle over both halves, and every word ('SickScience' on the cap, the product name on the silver half) is printed "
       "vertically in pure white on that black stripe - never text directly on the chrome, never black or grey letters. Never stubby, chubby, "
       "squat or flat-bottomed.")
TUBE = ("The DropOff tube is a cobalt-blue squeeze tube about 20 cm tall standing on its round cobalt screw cap with a flat crimp at the top; "
        "vertical pure white text 'SickScience' and 'DropOff'; never black or grey text.")
GEL = ("a translucent gel-serum - semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, slightly viscous")
MODEL = ("a strikingly beautiful woman in her late 20s, model-like features, realistic skin with natural pores and texture, not plastic, "
         "exactly two arms and two hands")
FIN = ("PHOTOGRAPHIC FINISH\nHigh-end beauty campaign photograph, ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, "
       "8K detail. All product text must be perfectly legible, sharp, and accurate - no blurry or distorted letters. Fine natural grain. "
       "No text, no letters, no logos added to the scene (product labels only).")
INT = ("INTEGRATION\nThe product shares the scene's light direction, softness and colour temperature; the chrome shows the real reflections of "
       "this set; a real contact shadow where it touches a surface; same sharpness and grain as the rest of the frame; no outline or halo.")
NEG = ("Negative: pasted or composited look, cut-out edges, sticker look, halo, floating product, stubby chubby wide or flat-bottomed bottle, "
       "text printed directly on chrome, missing black stripe, black letters, dark or grey text on the product, 'Network' with a lowercase w, "
       "warped label, extra products, oversized product, product close to the camera, text, headline, watermark, CGI, 3D render, cartoon, "
       "illustration, extra arms, extra fingers, plastic skin")
COMP = ("COMPOSITION AND FRAMING\nVertical 9:16 frame. {main} The top 38% of the frame is calm, uncluttered background - clean space for a "
        "headline. The bottom 30% is calm, low-detail continuation of the set.")
X = {
 'K_sorry_ss': ["Match the ELEMENT reference exactly for the ShapeShift bottle: shape, colours, chrome finish and label layout.",
   f"The person is {MODEL}, sleek low bun, small gold earrings, bare shoulders; confident, playful half-smile.",
   "PRODUCT ORIENTATION\nShe is in a three-quarter profile turned to the right, chin slightly lifted so her clean, defined jawline and smooth neck are the hero; "
   "she holds the closed ShapeShift bottle upright between her fingertips just under her jaw, label facing the camera, at the same distance from the camera as her face. " + CAP,
   COMP.format(main="35mm lens, chest-up; her face, jaw and the bottle sit between 42% and 68% of the frame height, centred."),
   "SCALE\nThe bottle is 12 cm tall and 3.5 cm wide - about two thirds of the length of her hand, never as tall as her face. If in doubt make it smaller.",
   "LIGHT AND SHADOW\nSoft sculpting key light from the front left that carves the jawline, gentle rim light on the neck, clean lilac fill.",
   "BACKGROUND\nA studio-built set: a smooth curved lilac plaster wall with a soft gradient, one sculptural white plinth edge out of focus; premium and minimal.",
   FIN, INT, NEG + "."],
 'L_salon_pc': ["Match the ELEMENT reference exactly for the PowerCycle bottle: shape, colours, chrome finish and label layout.",
   f"The person is {MODEL}, with long, thick, glossy, voluminous dark brown hair, sitting in a chair, smiling at her reflection. Behind her a hair stylist's two hands lift and fan out a section of her hair to show its thickness; the stylist's face is out of frame.",
   "PRODUCT ORIENTATION\nThe closed PowerCycle bottle stands upright on the white marble salon counter in the foreground right, label facing the camera, sharp. " + CAP,
   COMP.format(main="35mm lens; the woman's head and hair sit between 40% and 70% of the frame height; the bottle stands on the counter at the right, between 58% and 70% of the frame height."),
   "SCALE\nThe bottle is 14 cm tall and 4.5 cm wide, far smaller than the woman's head. If in doubt make it smaller.",
   "LIGHT AND SHADOW\nBright, airy salon daylight from large windows, soft highlights shining through the hair strands.",
   "BACKGROUND\nAn upscale, minimal hair salon: warm white walls, a large round mirror, pale oak, a few green plants, softly out of focus.",
   FIN, INT, NEG + ", bald patches, wig look."],
 'M_body_do': ["Match the ELEMENT reference exactly for the DropOff tube: shape, colour, cap and label layout.",
   f"The person is {MODEL}, toned, wearing a matching soft periwinkle-blue ribbed sports bra and high-waisted leggings, hair in a sleek ponytail; glowing, confident.",
   "PRODUCT ORIENTATION\nShe stands in a relaxed three-quarter pose, one hand on her waist, the other hand holding the DropOff tube upright at waist height, label facing the camera. " + TUBE,
   COMP.format(main="35mm lens, from the head to mid-thigh; her body and the tube are centred between 38% and 95% of the frame height, the tube at about 60%."),
   "SCALE\nThe tube is 20 cm tall - about the length of her forearm from wrist to mid-forearm. Real proportions.",
   "LIGHT AND SHADOW\nSoft, bright studio light from the front left, gentle contour shadows, healthy skin sheen.",
   "BACKGROUND\nA studio-built set: a seamless pale periwinkle-to-white curved wall with a soft round shadow; minimal.",
   FIN, INT, NEG + ", nudity, lingerie, exaggerated muscles."],
 'N_brush_pc': ["Match the ELEMENT reference exactly for the PowerCycle bottle: shape, colours, chrome finish and label layout.",
   "No person appears; a calm, premium bathroom still life that tells a story.",
   "PRODUCT ORIENTATION\nOn a pale travertine vanity: a wooden paddle hairbrush lying at an angle with a few loose long dark hair strands caught in its bristles, and beside it the closed PowerCycle bottle standing upright, label facing the camera, sharp; a single glossy bead of " + GEL + " on the stone in front of the bottle. " + CAP,
   COMP.format(main="Camera at counter height, slightly above; the brush and the bottle sit between 50% and 70% of the frame height, the bottle right of centre."),
   "SCALE\nThe bottle is 14 cm tall and 4.5 cm wide; the hairbrush about 24 cm long. Real relative sizes.",
   "LIGHT AND SHADOW\nSoft morning window light from the left, long gentle shadows, fresh and clean.",
   "BACKGROUND\nA soft sage-green plaster wall and pale travertine; nothing else.",
   FIN, INT, NEG + ", people, hands, clumps of hair, messy."],
 'O_ulta_line': ["Match the ELEMENT references exactly for the four products: shapes, colours, chrome finish and label layouts. Exactly four products, no extra product.",
   "No person appears; a bright retail-launch still life.",
   "PRODUCT ORIENTATION\nA plain, glossy, completely blank bright-orange paper shopping bag with twisted handles stands slightly behind; in front of it the four products stand on a white glossy plinth in a dynamic staggered row: DropOff tube, PowerCycle (green), ShapeShift (violet), NetWork (red), labels facing the camera. The bag has a completely plain front panel - no text, no logo. " + CAP + " " + TUBE,
   COMP.format(main="Camera straight on at product height; the bag and products sit between 45% and 72% of the frame height, centred."),
   "SCALE\nShapeShift and NetWork 12 cm tall, PowerCycle 14 cm, DropOff 20 cm; the bag 30 cm wide and 40 cm tall. Real relative sizes; never larger.",
   "LIGHT AND SHADOW\nBright, clean studio light, soft shadows, glossy chrome highlights with warm orange reflections from the bag.",
   "BACKGROUND\nA soft peach-to-white seamless studio backdrop; nothing else.",
   FIN, INT, NEG + ", text or logo on the bag, Ulta text."],
 'P_vault_set': ["Match the ELEMENT reference exactly for the three products of the set: shapes, colours, chrome finish and label layouts. Exactly three products, no extra product.",
   "No person appears; a dynamic, premium campaign still life.",
   "PRODUCT ORIENTATION\nThree travertine stone plinths of different heights stand in a staggered row; on each one product stands upright, label facing the camera: the DropOff tube on the left (lowest plinth), PowerCycle (green) in the middle on the tallest plinth, ShapeShift (violet) on the right; one soft glossy bead of " + GEL + " on each plinth top. " + CAP + " " + TUBE,
   COMP.format(main="Camera slightly below product height, straight on; plinths and products sit between 42% and 75% of the frame height, centred."),
   "SCALE\nShapeShift 12 cm tall, PowerCycle 14 cm, DropOff 20 cm; plinths 15-30 cm tall. Real relative sizes.",
   "LIGHT AND SHADOW\nBright directional sunlight from the right with crisp, graphic shadows of the plinths on the wall; glossy chrome highlights.",
   "BACKGROUND\nA soft lilac plaster wall and floor; nothing else.",
   FIN, INT, NEG + "."],
 'J2_nw_dark': ["Match the ELEMENT reference exactly for the NetWork bottle: shape, colours, chrome finish and label layout.",
   f"The person is {MODEL}, dark glossy waves, deep burgundy velvet dress, luminous dewy glowing skin; she sits behind a small dark marble table, chin resting lightly on her hand, looking at the camera.",
   "PRODUCT ORIENTATION\nThe closed NetWork bottle stands upright ON THE TABLE in front of her, label facing the camera, sharp, with candlelight reflections on the chrome. The label reads exactly 'NetWork' with a capital N and a capital W. " + CAP,
   COMP.format(main="35mm lens; her face sits at 45-55% of the frame height, the bottle on the table at 58-70%, centred."),
   "SCALE\nThe bottle is 12 cm tall and 3.5 cm wide - clearly smaller than her face. If in doubt make it smaller.",
   "LIGHT AND SHADOW\nWarm candlelight key from the left, glowing highlights on her cheekbones, rich deep shadows, a soft warm rim light.",
   "BACKGROUND\nA dark, luxurious candlelit room: tall candles, a few deep red roses, burgundy velvet, soft bokeh.",
   FIN, INT, NEG + ", vampire fangs, blood, horror, bottle in her hand."],
}
if __name__ == '__main__':
    open('/private/tmp/claude-501/p70.json', 'w').write(json.dumps(X))
    print(list(X))
