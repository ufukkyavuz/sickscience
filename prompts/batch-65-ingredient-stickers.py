"""Batch 65 — ingredient sticker photos for ShapeShift VO v3 (user 2026-10-20: "niacinamide, pineapple falan diye sayarken görsellerini getir").
Single ingredient on pure white, 1:1, to be cut out (Vision lift) and popped in as stickers. Template sections, no product."""
import json
FIN = ("PHOTOGRAPHIC FINISH\n100mm macro lens at f/8, everything sharp. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, "
       "8K detail. No text, no letters, no logos added to the scene.")
NEG = "Negative: text, labels, logos, packaging, bottles, hands, people, props, busy background, coloured background, harsh shadow, CGI, 3D render, illustration, cartoon"
def P(subject, orient, comp, scale, extra_neg=""):
    return [f"A premium clean studio product-style photograph of {subject}, isolated as a single hero ingredient.",
            "No person appears; this is an ingredient still life for a skincare brand.",
            "PRODUCT ORIENTATION\n" + orient,
            "COMPOSITION AND FRAMING\nSquare 1:1 frame, the subject centred and filling about 65% of the frame, generous empty white margin on every side so it can be cut out cleanly. " + comp,
            "SCALE\n" + scale,
            "LIGHT AND SHADOW\nBright soft high-key studio light from the upper left, white bounce fill, a very soft small contact shadow directly below the subject.",
            "BACKGROUND\nPure seamless white background, nothing else.",
            FIN, NEG + extra_neg + "."]
X = {
 'caffeine': P("a small heap of whole roasted coffee beans", "A loose, natural little mound of glossy dark-brown roasted coffee beans, seen from a slight high angle.", "Crisp individual beans with their centre crease visible.", "About 8 cm across; each bean about 1 cm."),
 'niacinamide': P("a small clear glass lab dish holding fine white crystalline powder", "A shallow round clear glass petri dish with a small soft heap of bright white fine crystalline powder (niacinamide), a few loose crystals sparkling, seen from a slight high angle.", "Clean scientific look, crisp glass edge highlights.", "Dish about 9 cm across."),
 'pineapple': P("a fresh pineapple slice", "One thick fresh golden pineapple ring slice with its green-brown rind and juicy fibrous flesh glistening, standing slightly tilted, plus one small pineapple chunk beside it.", "Juicy, vivid, appetising, natural colour.", "Slice about 9 cm across."),
 'gel': P("a single glossy bead of translucent gel-serum", "One rounded glossy bead and a short soft swipe of a translucent gel-serum - semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, slightly viscous - resting on a small clear glass slide.", "Light passes through the gel edges, crisp specular highlights.", "Bead about 2 cm across, slide 7 cm.", ", opaque white cream, water-clear liquid, coloured or gold serum"),
}
if __name__ == '__main__':
    open('/private/tmp/claude-501/p65.js', 'w').write('window.__p65=' + json.dumps(X) + ';"ok"')
    print('\n\n'.join(X['gel']))
