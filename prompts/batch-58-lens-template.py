"""Batch 58 — concern cards, rimless lens (reference: DUMAIN glasses through a lens), written in the mandatory sectioned template
(INO CLAUDE.md 'PROMPT KALIBI' + prompts/TEMPLATE-photographic.md). No aspect/resolution line in the prompt. No product in frame."""
import json
def build(subject_open, model, area, lens_place, scale_body, neg_extra=""):
    return [
f"A real editorial studio photograph of {subject_open}, shot through a large round piece of clear optical glass.",
f"{model} Keep realistic anatomy and natural skin; do not retouch into plastic.",
"PRODUCT ORIENTATION\nNo product appears in this image. The only prop is a completely rimless round disc of clear polished optical glass - no frame, no metal ring, no handle; its edge shows only as a thin bright refraction line where the glass ends. The disc stands square to the camera, perfectly centred. No hand, no stand. No fisheye, no wide-angle distortion.",
f"COMPOSITION AND FRAMING\nThe glass disc sits in the foreground very close to the camera, perfectly centred, filling about 75% of the frame width. Through the glass the camera focuses sharply on {area}, magnified about 1.5 times with crisp detail. {lens_place} Everything outside the glass circle is softly out of focus with a creamy shallow depth of field; the same body continues outside the edge, blurred. The whole glass circle fits inside the frame.",
f"SCALE\nThe glass disc is about 22 cm across. {scale_body} Keep real human proportions.",
"LIGHT AND SHADOW\nProfessional beauty-campaign studio light: a large soft white key from the upper left, white bounce fill, bright and airy, clean neutral white balance - not warm, not yellow. A crisp bright highlight runs along the glass edge.",
"BACKGROUND\nPure bright white seamless studio backdrop, out of focus, nothing else.",
"PHOTOGRAPHIC FINISH\n100mm macro lens at f/2.8. Realistic skin with natural pores and fine texture, clear polished glass with true refraction. Subtle optical depth, fine photographic grain, restrained natural colour, bright airy high-key look. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos added to the scene.",
f"Negative: metal rim, black ring, frame around the glass, magnifying-glass handle, hand, fingers, stand, warm yellow or beige tone, dim moody light, everything sharp, glass off-centre, two discs, products, bottles, text, watermark, coloured background, distorted anatomy, extra limbs, warped glass, cartoon, CGI, 3D render, plastic skin{neg_extra}."]
P={
'jaw': build("a woman's jawline and neck","The model is a strikingly beautiful woman in her late 20s with model-like features, shown in three-quarter profile with her chin slightly lifted and bare shoulders.","the jawline, the angle of the jaw and the smooth line under the chin","The jaw and neck fill the glass.","The visible area through the glass runs from the earlobe to the chin."),
'glow': build("a woman's cheek skin glow","The model is a strikingly beautiful woman in her late 20s with model-like features, face turned three-quarter, eyes softly closed, hair pulled back.","her cheekbone and cheek skin, smooth and luminous with fine natural pores","The cheek fills the glass.","The visible area through the glass covers the cheek from the cheekbone to the corner of the mouth."),
'hair': build("a woman's hair parting","The model is a woman in her late 20s with long glossy dark-brown hair, seen from above and behind, head gently bowed.","the centre hair parting and the dense glossy strands beside it","The parting runs vertically through the middle of the glass.","The visible area through the glass covers about 10 cm of the parting.",", bald patches"),
'body': build("a woman's outer thigh","The model is a fit woman in her late 20s with a natural healthy body in simple seamless white briefs, seen from the side at thigh level; tasteful, non-sexual, clinical-beauty look.","the outer thigh with a very mild, realistic everyday dimpled skin texture","The outer thigh fills the glass.","The visible area through the glass covers about 15 cm of the outer thigh.",", nudity, sexualised pose, severe cellulite"),
}
if __name__=='__main__':
    json.dump(P,open('/private/tmp/claude-501/p58.json','w'),indent=1); print('\n\n'.join(P['jaw']))

# v5 (user: "bunlar büyüteçle bakılıyo gibi durmuyo") — strong visible magnification inside the glass
MAG = ("COMPOSITION AND FRAMING\nThe glass disc sits in the foreground very close to the camera, perfectly centred, filling about 70% of the frame width. "
       "It works as a STRONG MAGNIFYING LENS: everything seen through the glass is shown about 2.5 times larger than the same body outside the glass - {inside} "
       "At the edge of the glass the image visibly jumps in scale: {jump} Inside the glass the image is crisp and sharp; outside the glass the body is smaller and softly out of focus with a creamy shallow depth of field. The whole glass circle fits inside the frame.")
def v5(key, inside, jump):
    p = list(P[key]); p[3] = MAG.format(inside=inside, jump=jump); return p
P5 = {
 'jaw':  v5('jaw', "the jawline and the skin under the chin look big and close, with clearly visible pores and fine skin texture.", "the line of the jaw inside the glass is much larger and does not line up with the smaller, blurred jaw and neck continuing outside the glass."),
 'glow': v5('glow', "the cheek skin looks big and close, with clearly visible pores, fine peach fuzz and a luminous glow.", "the cheek inside the glass is much larger than the small, blurred face around it, so the contour breaks at the rim."),
 'hair': v5('hair', "the parting and the individual hair strands look big and close, each strand clearly visible.", "the parting inside the glass is much wider and larger than the small, blurred head of hair around it, so the line breaks at the rim."),
 'body': v5('body', "the skin of the outer thigh looks big and close, with the mild dimpled texture clearly visible.", "the thigh contour inside the glass is much larger and does not line up with the smaller, blurred leg outside the glass."),
}
if __name__=='__main__':
    json.dump(P5,open('/private/tmp/claude-501/p58v5.json','w'),indent=1); print(P5['jaw'][3])
