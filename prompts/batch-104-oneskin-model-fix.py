# Batch-104 (2026-11-06): re-shoot the model frames of batch-103 to match the OneSkin references 1:1.
# User: "referanslardaki yerleşimlere dikkat et modelli olanlarda hiçbiri anlatılmak istenen gibi değil şuan".
# What the refs do and batch-103 did not:
#  - menopause / "still dry" cards (ref 4.png): the woman's FACE is in frame (eyes, expression), she applies the product
#    with her fingertips, the gel dab sits on her skin; headline boxes sit over the lower face/shoulder; the stat callout's
#    dotted line ends ON the dab.
#  - carousel card 2 (Atria m2462565717483177): the product stands UPRIGHT on an open palm held up from below,
#    a small bead of texture sits on top of the cap, the dotted callout from the body text ends on that bead.
import json,sys
from importlib import util
spec=util.spec_from_file_location('b102','prompts/batch-102-bf-windows.py'); m=util.module_from_spec(spec)
src=open('prompts/batch-102-bf-windows.py').read().split('C = {}')[0]; exec(src,m.__dict__)
CAPS,SIZE,LABEL,IMPERF,INTEG=m.CAPS,m.SIZE,m.LABEL,m.IMPERF,m.INTEG
SKIN=("Real human skin with visible pores, fine natural texture, tiny peach fuzz and slight unevenness; no retouched plastic skin, no airbrushing.")
GEL=("a translucent gel-serum — semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, slightly viscous, it holds a soft rounded bead and lets light pass through its edges")
IMP=("Real-world flaws, kept subtle: real film grain and slight sensor noise in the shadows, gentle natural vignetting, a soft bloom on the brightest highlight, a few tiny stray hairs.")
NEGF=("eyes cropped out, face cut off at the nose, sad or tired expression, wrinkled elderly skin, plastic skin, airbrushed skin, CGI, 3D render, extra fingers, six fingers, deformed hand, more than two arms, "
      "text, letters, watermark, opaque white cream, thick white lotion, whipped cream, body butter, water-clear liquid, coloured or gold serum, product bottle, packaging in frame, harsh shadows, flat seamless colour backdrop")
P={}
P["H1_meno"]=["A real high-end skincare campaign portrait, in the style of a premium clinical beauty brand. A strikingly beautiful woman around 50 with model-like features, softly silver-streaked hair tucked behind her ear, a warm genuine smile, looking into the camera. With the fingertips of her right hand raised to her face she smooths a small fresh stroke of "+GEL+" along her jawline below the ear; a second soft bead of the gel-serum sits on the side of her neck.",
 "IDENTITY AND ANATOMY","Exactly one person, exactly two arms, one hand visible with exactly five fingers and natural nude nails. Her whole face is in frame: eyes, nose, mouth, jawline and neck. Real mature-but-radiant skin, smooth and healthy. "+SKIN,
 "COMPOSITION AND FRAMING","Vertical 9:16, 85mm portrait lens, a tight head-and-shoulders crop with her face turned three-quarters to the left. Her eyes sit at about 24% of the frame height, the fingertips and the gel stroke on the jaw at about 36–40%, her chin at about 44%. The face is centred in the band from 22% to 82% of the frame width. From 50% down: her neck, collarbones and a pale blue knit top in soft light, calm and uncluttered (headline area). Nothing important below 80%.",
 "LIGHT AND SHADOW","Soft daylight from a large window on the left, gentle fill from the right, a clean specular highlight on the gel-serum stroke, soft shadow under the jaw.",
 "BACKGROUND","A studio set: warm white plaster wall, softly out of focus. Bright, clean, scientific, white-dominant.",
 "PHOTOGRAPHIC FINISH","f/2.8, eyes and gel tack sharp. Natural colour. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos added to the scene.",
 "IMPERFECTIONS",IMP,"KEY COMPOSITION","SMILING WOMAN AROUND 50, WHOLE FACE IN FRAME, FINGERTIPS SMOOTHING A TRANSLUCENT GEL-SERUM ALONG HER JAWLINE.","Negative: "+NEGF+"."]
P["H2_glp1"]=["A real high-end skincare campaign portrait, in the style of a premium clinical beauty brand. A strikingly beautiful woman in her late 30s with model-like features and dark hair pulled back, a calm, slightly thoughtful expression. Her face is turned in profile-three-quarter to the right and cropped by the left edge of the frame through the far eye. With the index and middle fingertips of her right hand she dabs a single fresh bead of "+GEL+" onto her cheekbone.",
 "IDENTITY AND ANATOMY","Exactly one person, exactly two arms, one hand visible with exactly five fingers and natural nails. The near eye, the cheek, nose, mouth and jaw are in frame. Slightly softer, less full cheeks. "+SKIN,
 "COMPOSITION AND FRAMING","Vertical 9:16, 100mm lens, close crop. The near eye sits at about 22% of the frame height near 30% of the width; the gel-serum bead on the cheekbone sits at about 34% of the height and 46% of the width, with the fingertips just to its right; the mouth at about 44%. The upper-right quarter of the frame (from 55% to 92% of the width, 14% to 34% of the height) is calm soft background or smooth skin with nothing in it (stat callout area). From 52% down: her jaw, neck and a white shirt collar, calm (headline area).",
 "LIGHT AND SHADOW","Soft frontal daylight from the upper left, gentle fill, a crisp highlight on the gel bead showing its translucency.",
 "BACKGROUND","Studio set: pale cool-white wall, softly out of focus. Bright, clean, scientific.",
 "PHOTOGRAPHIC FINISH","f/2.8, the eye, fingertips and gel bead tack sharp. Natural colour. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos added to the scene.",
 "IMPERFECTIONS",IMP,"KEY COMPOSITION","CLOSE CHEEK PORTRAIT, FINGERTIPS DABBING A TRANSLUCENT GEL-SERUM BEAD ON THE CHEEKBONE, EMPTY UPPER RIGHT.","Negative: "+NEGF+"."]
NEGH=("product lying down, product held by the fingertips, product tilted more than 10 degrees, fist, closed hand, more than one hand, six fingers, deformed hand, fully coloured capsule, capsule without a silver half, stubby, chubby or wide bottle, "
      "matte or plastic cap, black letters, dark or grey text on the product, misspelled text, extra products, pasted or composited look, cut-out edges, halo, CGI-clean surfaces, plastic perfection, CGI, 3D render, watermark, added text, face, props, "
      "opaque white cream, whipped cream, water-clear liquid, coloured or gold serum")
def hand(code,col,bg):
    return [f"A real high-end product campaign photograph: one woman's open hand, palm up, rises into the frame from the lower right and holds the {col} capsule from the element reference standing UPRIGHT on her palm, fingers gently curled around its silver lower half. A single small soft bead of "+GEL+" sits on the top of the rounded cap.",
     "Preserve the exact identity of the product: match the element reference exactly, for identity only, never redrawn. "+CAPS+" Exactly one product.",
     "PRODUCT ORIENTATION","The capsule stands perfectly vertical, label facing the camera, text vertical and fully visible from top to bottom.",
     "COMPOSITION AND FRAMING","Vertical 9:16, 85mm lens, camera slightly below the hand. The capsule's top with the gel bead sits at about 40% of the frame height, its base on the palm at about 64%; the capsule is centred near 52% of the width, inside the band from 30% to 74%. The wrist leaves the frame at the lower right. The upper 36% is calm empty background for a headline and text.",
     "SCALE",SIZE[code]+"; an adult hand is about 18–19 cm long, so the capsule is about two-thirds of the hand's length and slightly wider than two fingers. Real size, never shrunk to a pill held between fingertips.",
     "LIGHT AND SHADOW","Soft large softbox from the upper left, gentle bounce from the right, true reflections of the hand and room in the chrome. "+LABEL,
     "BACKGROUND",bg,
     "PHOTOGRAPHIC FINISH","f/5.6, the capsule label, gel bead and fingers tack sharp. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. All product text must be perfectly legible, sharp, and accurate — no blurry or distorted letters. Every word is printed in thin pure white letters on the coloured cap AND on the silver half, made readable by a dark reflection behind it; never black, grey or dark text. No text, no letters, no logos added to the scene.",
     "IMPERFECTIONS",IMPERF,"INTEGRATION",INTEG,
     "KEY COMPOSITION","OPEN PALM HOLDING THE CAPSULE UPRIGHT, A SMALL GEL-SERUM BEAD ON TOP OF THE CAP, EMPTY UPPER THIRD.","Negative: "+NEGH+"."]
P["H3_ss_hand"]=hand("SS","violet ShapeShift","A seamless soft gradient from pale ice-blue at the top to light blue-grey at the bottom, like a clean clinical studio.")
P["H4_pc_hand"]=hand("PC","green PowerCycle","A seamless soft gradient from pale ice-blue at the top to light grey at the bottom, like a clean clinical studio.")
out=sys.argv[1] if len(sys.argv)>1 else '/tmp/p104.json'
json.dump({k:"\n".join(v) for k,v in P.items()},open(out,'w')); print({k:sum(len(x) for x in v) for k,v in P.items()})
