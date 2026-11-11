# Batch-103: OneSkin-style variant set (2026-11-06). User: "referansları incele bazılarında birden fazla görsel var.
# toplantıda konuşulanları da göz önünde bulundurarak bunlarla birkaç varyantlı görsel çıkartalım".
# Meeting (Fathom 'Sick Science brand book', 05.11): niche audiences menopause / postpartum / GLP-1; OneSkin learnings =
# shocking B/A hooks, menopause focus, "2 steps" routines; Ufuk: clinical data + microscopic images.
# Only 4 generated images; everything else = client real B/A + client photos. Text added in Figma.
import json,sys
sys.path.insert(0,'prompts')
SKIN=("Real human skin with visible pores, fine natural texture, tiny peach fuzz and slight unevenness; no retouched plastic skin, no airbrushing.")
GEL=("a translucent gel-serum — semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, slightly viscous, it holds a soft rounded bead and lets light pass through its edges")
IMP=("Real-world flaws, kept subtle: real film grain and slight sensor noise in the shadows, gentle natural vignetting, a soft bloom on the brightest highlight, tiny stray hairs.")
NEGP=("full face, eyes, nose, face above the upper lip, wrinkled elderly skin, plastic skin, airbrushed skin, CGI, 3D render, extra fingers, six fingers, deformed hand, jewellery logos, text, letters, watermark, "
      "opaque white cream, thick white lotion, whipped cream, body butter, water-clear liquid, coloured or gold serum, product bottle, packaging, harsh shadows, flat seamless colour backdrop")
P={}
P["G1_meno"]=["A real high-end skincare campaign photograph, extreme close crop of a woman's lower face and neck: from just below the nose to the collarbones, in exact side-three-quarter profile facing right. Two fingertips of her right hand smooth a small fresh stroke of "+GEL+" upward along the jawline, just below the ear. A second soft bead of the gel-serum sits on the side of the neck.",
 "IDENTITY AND ANATOMY","Exactly one person, exactly two visible fingertips of one hand, natural nails with a nude polish. The face is cropped at the upper lip: the eyes are never in frame. Natural skin of a woman in her forties, smooth but real. "+SKIN,
 "COMPOSITION AND FRAMING","Vertical 9:16, 100mm macro portrait lens. The jawline and fingertips sit between 34% and 62% of the frame height, inside the central band from 22% to 80% of the frame width. The lower 30% is the softly lit neck and a pale blue knit top; the upper 22% is calm soft background.",
 "LIGHT AND SHADOW","Soft daylight from a large window on the left, gentle fill from the right, a clean specular highlight on the gel-serum stroke, soft shadow under the jaw.",
 "BACKGROUND","A studio set: warm white plaster wall, softly out of focus. Bright, clean, scientific, white-dominant.",
 "PHOTOGRAPHIC FINISH","f/4, the gel and fingertips tack sharp, the far side softly falling off. Natural colour. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos added to the scene.",
 "IMPERFECTIONS",IMP,"KEY COMPOSITION","LOWER FACE AND NECK IN PROFILE, FINGERTIPS SMOOTHING A TRANSLUCENT GEL-SERUM UP THE JAWLINE.","Negative: "+NEGP+"."]
P["G2_glp1"]=["A real high-end skincare campaign photograph, close crop of a woman's cheek and lower face facing the camera at a slight angle to the left: from the cheekbone down to the chin, the mouth relaxed and closed. One fingertip of her left hand rests on the cheekbone beside a single fresh bead of "+GEL+".",
 "IDENTITY AND ANATOMY","Exactly one person, exactly one visible hand with natural nails. The crop starts just below the eyes: no eyes in frame. Natural skin of a woman in her late thirties with a slightly hollow, softer cheek. "+SKIN,
 "COMPOSITION AND FRAMING","Vertical 9:16, 100mm lens. The fingertip and the gel-serum bead sit between 36% and 56% of the frame height, inside the central band from 30% to 76% of the frame width. Upper 24% calm soft background, lower 30% soft neck and a white shirt collar.",
 "LIGHT AND SHADOW","Soft frontal daylight from the upper left, gentle fill, a crisp highlight on the gel bead showing its translucency.",
 "BACKGROUND","Studio set: pale cool-white wall, softly out of focus. Bright, clean, scientific.",
 "PHOTOGRAPHIC FINISH","f/4. Natural colour. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos added to the scene.",
 "IMPERFECTIONS",IMP,"KEY COMPOSITION","CHEEK CLOSE-UP, FINGERTIP BESIDE A TRANSLUCENT GEL-SERUM BEAD ON THE CHEEKBONE.","Negative: "+NEGP+"."]
from importlib import util
spec=util.spec_from_file_location('b102','prompts/batch-102-bf-windows.py'); m=util.module_from_spec(spec)
src=open('prompts/batch-102-bf-windows.py').read().split('C = {}')[0]; exec(src,m.__dict__)
CAPS,SIZE,NAME,LABEL,IMPERF,INTEG=m.CAPS,m.SIZE,m.NAME,m.LABEL,m.IMPERF,m.INTEG
NEG2=("products filling the frame, product in the upper half of the frame, fully coloured capsule, capsule without a silver half, large bold lettering, stubby, chubby or wide bottle, matte or plastic cap, black letters, dark or grey text on the product, misspelled text, extra products, "
      "pasted or composited look, cut-out edges, sticker look, halo, floating product, CGI-clean surfaces, plastic perfection, CGI, 3D render, watermark, added text, people, hands, props, stripe or band on the DropOff tube, pink gua sha, rose quartz, jade, stone gua sha")
def still(prods,idea,arr,light,bg,comp):
    names=" and ".join(NAME[p] for p in prods)
    return [f"A real high-end product campaign photograph featuring {names} from the element references. {idea}",
      "Preserve the exact identity of every product: match each element reference exactly, for identity only, never redrawn. "+CAPS+f" Exactly {len(prods)} products, no extra product.",
      "PRODUCT ORIENTATION",arr+" Labels face the camera, text vertical.","COMPOSITION AND FRAMING","Vertical 9:16, 85mm lens. "+comp,
      "SCALE","; ".join(SIZE[p] for p in prods)+".","LIGHT AND SHADOW",light+" "+LABEL,"BACKGROUND",bg,
      "PHOTOGRAPHIC FINISH","f/8, mirror chrome with true reflections, brushed stainless steel, matte cobalt tube. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos, no numbers added; only the products' own printed labels.",
      "IMPERFECTIONS",IMPERF,"INTEGRATION",INTEG,"KEY COMPOSITION",idea.upper(),"Negative: "+NEG2+"."]
P["G3_sculpt2"]=still(["SS","GS"],"Two steps, side by side: the ShapeShift capsule standing and its stainless-steel gua sha resting upright against it, like a calm minimal packshot.",
 "The violet capsule stands upright slightly left of centre; the flat stainless-steel gua sha stands on its edge leaning against the right side of the capsule.",
 "Soft large top-left softbox, a gentle blue-grey bounce, soft contact shadows on the surface.","A seamless soft gradient from pale ice-blue at the top to light grey at the bottom, with a faint reflective surface under the products.",
 "PRODUCTS ARE SMALL AND LOW: the capsule is about 30% of the frame height and sits between 52% and 84% of the frame height, inside the central band from 30% to 72% of the width. The upper half is calm empty gradient for a headline.")
P["G4_h2t_dark"]=still(["PC","DO"],"Hair and body in two steps: the PowerCycle capsule and the DropOff tube standing close together, lit like a premium dark packshot.",
 "The green capsule stands left, the cobalt tube stands right slightly behind it, both upright on a dark reflective surface.",
 "A soft cool key light from the upper right, gentle rim on the chrome, deep soft shadows.","A seamless gradient from deep slate teal at the top to charcoal at the bottom, softly misty.",
 "PRODUCTS ARE SMALL AND LOW: the tallest product is about 34% of the frame height; the group sits between 52% and 86% of the frame height, inside the central band from 34% to 74% of the width. The upper half is calm dark gradient for a headline.")
out=sys.argv[1] if len(sys.argv)>1 else '/tmp/p103.json'
json.dump(P,open(out,'w')); print({k:sum(len(x) for x in v) for k,v in P.items()})
