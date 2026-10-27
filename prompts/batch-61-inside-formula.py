"""Batch 61 — Amazon What's inside as 'formula' visuals (user 2026-10-20: "formül gibi bilimsel göster… her şeyi anlatmadığın şekilde").
Clear glass vessel in the product silhouette, layered with the real raw ingredients named on the site. Labels added in Figma. 3:4."""
import json
LIGHT="LIGHT AND SHADOW\nBright high-key laboratory studio light: a large soft key from the upper left, white bounce fill, crisp clean refractions in the glass, a soft contact shadow and faint reflection on the bench. Neutral white balance."
BG="BACKGROUND\nSeamless very pale cool-white studio backdrop with a soft gradient; the vessel stands on a glossy white lab bench; nothing else in the scene."
FIN="PHOTOGRAPHIC FINISH\n100mm lens at f/8, everything inside the glass tack sharp, real glass refraction and caustics. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. Fine photographic grain. No text, no letters, no logos, no labels anywhere."
INT="INTEGRATION\nThe vessel and its contents share one light direction and colour temperature; real refraction bends the layers at the curved glass edges; real contact shadow; no outline, halo or cut-out look."
NEG="Negative: text, letters, labels, logos, extra vessels, beakers, flasks, hands, people, messy spill, dark background, coloured background, warm yellow tone, CGI, 3D render, illustration, cartoon, plastic look, stubby or wide vessel"
def P(shape, cap, layers, scale):
    return ["A real premium scientific product photograph of a single clear glass vessel filled with layered raw ingredients, like a formula made visible.",
            "No person appears; this is a clean editorial laboratory still life.",
            "PRODUCT ORIENTATION\n"+shape+" "+cap+" Standing perfectly upright, camera straight on at mid-height, orthographic feel, no tilt.",
            "COMPOSITION AND FRAMING\nVertical 3:4 frame. The vessel is centred and fills about 70% of the frame height, with clean empty space left and right for labels. Inside the glass, distinct horizontal layers stacked from bottom to top with crisp boundaries: "+layers,
            "SCALE\n"+scale, LIGHT, BG, FIN, INT, NEG+"."]
CAP="Sealed at the top by a rounded cap in glossy metallic chrome of colour {c}; the rest of the vessel is completely clear glass."
CAPS="A slim, tall, clear glass capsule with rounded pill ends, height 3.4 times its width."
X={
'ss':P(CAPS, CAP.format(c="violet purple"),
 "bottom - a layer of fresh golden pineapple chunks; then a layer of whole roasted coffee beans; then a layer of pale ivory shea butter; then a layer of fine white crystalline powder; at the top a layer of translucent gel-serum with a soft milky haze and tiny suspended bubbles.",
 "The vessel is 24 cm tall and 7 cm wide; coffee beans about 1 cm; pineapple chunks about 2 cm."),
'nw':P(CAPS, CAP.format(c="ruby red"),
 "bottom - a layer of thin fresh radish and cucumber slices stacked on edge; then a layer of whole sweet almonds; then a layer of whole roasted coffee beans; then a clear pale golden oil layer; at the top a layer of translucent gel-serum with a very subtle pearly shimmer and tiny suspended bubbles.",
 "The vessel is 24 cm tall and 7 cm wide; almonds about 2 cm; radish slices about 3 cm."),
'pc':P(CAPS, CAP.format(c="bright green"),
 "bottom - a layer of whole peeled garlic cloves; then a layer of golden wheat grains; then a layer of fresh green rosemary sprigs; then a layer of whole roasted coffee beans; at the top a layer of translucent gel-serum with a soft milky haze and tiny suspended bubbles.",
 "The vessel is 26 cm tall and 8 cm wide; garlic cloves about 2.5 cm; wheat grains about 6 mm."),
'do':P("A slim, tall, clear glass squeeze-tube shape: flat crimped seam at the top end, round shoulder and flat round base, height 4 times its width.",
 "The tube is sealed at the base by a round screw cap in matte cobalt blue; the rest is completely clear glass. The tube stands on its cap.",
 "bottom - a layer of whole roasted coffee beans; then a layer of fibrous pale-yellow pineapple stem pieces; then a layer of fine white crystalline powder; at the top a thick layer of translucent gel-serum with a soft milky haze and tiny suspended bubbles.",
 "The tube is 28 cm tall and 7 cm wide; coffee beans about 1 cm."),
}
if __name__=='__main__':
    for k,v in X.items():
        json.dump(v,open(f'/private/tmp/claude-501/p61_{k}.json','w'))
    print('\n\n'.join(X['ss']))
