"""Batch 64 — X-ray of a bag with SickScience inside (user 2026-10-20 reference: AKANOMA handbag X-ray — inverted blue
monochrome radiograph on white, casual everyday items). 21:9 full-bleed, bag on the right, empty white left for Figma text.
Mentions typed in composer: tote = ss-tote (or ss-pouch-purple), + ss-shapeshift, ss-network-v2, ss-powercycle, ss-dropoff."""
import json
OPEN=" element references for the silhouettes and proportions only. Exactly one bag and exactly four SickScience products inside it, no extra SickScience product."
PRODUCTS=("The four products: ShapeShift and NetWork slim capsule bottles (height 3.4 times width, split at the middle into cap and body), "
 "PowerCycle the same capsule shape slightly larger, DropOff a flat-crimped squeeze tube with a round screw cap. Never stubby or wide. "
 "Inside each product its contents show as denser X-ray shapes: ShapeShift - pineapple chunks and coffee beans; NetWork - radish and cucumber slices and almonds; "
 "PowerCycle - garlic cloves, wheat grains and a rosemary sprig; DropOff - fibrous pineapple stem pieces and coffee beans.")
XR=("Everything is rendered as one real inverted X-ray: monochrome steel-blue and navy density on white, translucent overlapping layers, "
    "dense parts darker, thin parts pale, crisp fine edges like the classic designer-bag X-ray photograph. No colour except the blue X-ray tone.")
LIGHT="LIGHT AND SHADOW\nPure X-ray exposure: no external light, no reflections, no cast shadows; tone comes only from material density."
BG="BACKGROUND\nPure clean white across the entire frame, seamless edge to edge; nothing else."
FIN=("PHOTOGRAPHIC FINISH\nA real high-resolution X-ray radiograph, indistinguishable from a genuine X-ray photograph, 8K detail, crisp, fine grain. "
     "No text, no letters, no numbers, no brand names, no labels, no measurement lines anywhere in the image.")
INT="INTEGRATION\nThe bag and every object inside share one exposure and density scale; overlaps show real X-ray transparency."
NEG=("Negative: text, letters, numbers, labels, logos, brand names, dimension lines, colour photo, glossy render, CGI, 3D render, illustration, cartoon, "
     "grey or dark background, seam, frame border, skeleton, bones, hands, people, extra SickScience products, stubby or wide bottles, separate glass vessel with a cap.")
def P(bag_line, bag_scale, layout):
    return [OPEN,
     "A casual, stylish X-ray photograph of "+bag_line+" with its everyday contents spilling naturally inside, featuring four SickScience products.",
     "PRODUCT ORIENTATION\n"+PRODUCTS+" "+XR+" "+layout,
     "COMPOSITION AND FRAMING\nUltra-wide 21:9 frame, straight-on flat X-ray view. The bag and its contents sit in the right 50% of the frame, fully visible with margin, not cropped. The left 50% is empty clean white for text - nothing there.",
     "SCALE\n"+bag_scale+" Capsules 12 cm and 14 cm tall, the DropOff tube 20 cm. Everyday objects at real size. If in doubt make the products smaller, never bigger.",
     LIGHT, BG, FIN, INT, NEG]
X={
'tote':P("an open tote bag",
 "The tote is 30 cm wide and 40 cm tall with two shoulder handles rising above it.",
 "Inside and around the tote, casually arranged and slightly overlapping like a real bag: the four SickScience products at relaxed angles, a pair of sunglasses, a bunch of keys, a smartphone, a few coins, wired earbuds, and a flat solid stainless-steel heart-shaped gua sha tool about 9 cm."),
'pouch':P("an open zip makeup pouch",
 "The pouch is 21 cm wide and 16 cm tall, lying flat; the products are partly inside it and partly spilling out of its open zip onto the film.",
 "The four SickScience products lie at relaxed casual angles, two inside the pouch and two spilled beside it, with a lipstick, a small round compact mirror, hair clips, a few coins and a flat solid stainless-steel heart-shaped gua sha tool about 9 cm."),
}
if __name__=='__main__':
    open('/private/tmp/claude-501/p64.js','w').write('window.__p62='+json.dumps(X)+';"ok"')
    print('\n\n'.join(X['tote']))
