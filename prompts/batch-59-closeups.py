"""Batch 59 — concern cards as direct close-ups (user 2026-10-20: "direkt yakın çekim yapalım merceği siktir et"). Template sections, no lens, no product."""
import json
LIGHT="LIGHT AND SHADOW\nProfessional beauty-campaign studio light: a large soft white key from the upper left, white bounce fill, bright and airy, clean neutral white balance - not warm, not yellow. Soft natural shadows that model the shape."
BG="BACKGROUND\nPure bright white seamless studio backdrop, nothing else."
FIN="PHOTOGRAPHIC FINISH\n100mm macro lens at f/5.6, the subject area tack sharp. Realistic skin with natural pores, fine texture and soft peach fuzz, no plastic retouching. Subtle optical depth, fine photographic grain, restrained natural colour, bright airy high-key look. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos added to the scene."
NEG="Negative: magnifying glass, lens, glass disc, hand, fingers, products, bottles, jewellery, heavy makeup, warm yellow or beige tone, dim moody light, coloured background, distorted anatomy, plastic skin, over-smoothed skin, CGI, 3D render, watermark, text"
def P(open_, model, orient, comp, scale, neg_extra=""):
    return [open_, model, "PRODUCT ORIENTATION\nNo product appears in this image. "+orient+" No fisheye, no wide-angle distortion.",
            "COMPOSITION AND FRAMING\n"+comp, "SCALE\n"+scale, LIGHT, BG, FIN, NEG+neg_extra+"."]
X={
'jaw':P("A real editorial studio close-up photograph of a woman's jawline and neck.",
 "The model is a strikingly beautiful woman in her late 20s with model-like features and bare shoulders. Keep realistic anatomy and natural skin.",
 "Her head is in clean side profile facing right, chin gently lifted so the jawline is long and defined. Camera at jaw height, straight on.",
 "Tight vertical close-up from just below the eye to the collarbone; the crisp line of the jaw runs diagonally through the middle of the frame and the smooth neck fills the lower half. The eye is cropped out at the top. Calm white space behind the profile.",
 "The jaw from chin to earlobe spans about 70% of the frame width. Keep real human proportions."),
'glow':P("A real editorial studio close-up photograph of a woman's luminous cheek skin.",
 "The model is a strikingly beautiful woman in her late 20s with model-like features, eyes softly closed, hair pulled back. Keep realistic anatomy and natural skin.",
 "Her face is turned three-quarter to the left. Camera at cheek height, slightly to the side.",
 "Tight vertical close-up of the cheek: from the brow to the lips; the cheekbone and the smooth, dewy cheek skin fill the centre of the frame with a soft natural glow highlight on the cheekbone. Part of the nose and lips at the frame edge.",
 "The cheek fills about 60% of the frame. Keep real human proportions."),
'hair':P("A real editorial studio close-up photograph of a woman's hair parting.",
 "The model is a woman in her late 20s with thick, glossy dark-brown hair. Keep realistic hair and natural scalp.",
 "She is seen from directly above and slightly behind, head bowed, a clean straight centre parting running vertically. Camera above the head.",
 "Tight vertical close-up of the top of the head: the straight centre parting runs from top to bottom through the middle of the frame, dense glossy strands fall to both sides, each strand visible. No face in frame.",
 "The visible area is about 15 cm of the parting. Keep real proportions."),
'body':P("A real editorial studio close-up photograph of a woman's outer thigh skin.",
 "The model is a fit woman in her late 20s with a natural healthy body in simple seamless white briefs; tasteful, non-sexual, clinical-beauty look. Keep realistic anatomy and natural skin.",
 "She stands in side profile. Camera at thigh height, straight on.",
 "Tight vertical close-up from the hip to above the knee: the outer thigh fills the frame, with a very mild, realistic everyday dimpled skin texture visible on the outer thigh in soft side light; the white briefs only at the top edge.",
 "The visible area is about 30 cm of the thigh. Keep real human proportions.", ", nudity, sexualised pose, severe cellulite"),
}
if __name__=='__main__': json.dump(X,open('/private/tmp/claude-501/p59.json','w'),indent=1); print('\n\n'.join(X['jaw']))
