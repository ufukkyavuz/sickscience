"""Batch 63 — X-ray v2 (user 2026-10-20: dark X-ray "daha mantıklı ama daha casual olsun, yazılar olmasın, tam xray gibi göster").
Real radiograph look, no labels/text/dimension lines, casual arrangement, uniform seamless black. 21:9, 4 element mentions."""
import json
OPEN=" element references for the silhouettes and proportions of the four products only. Exactly four products, no extra product."
BASE_ORIENT=("Silhouettes: ShapeShift and NetWork are slim capsule bottles, height 3.4 times their width, split at the middle into cap and body; "
 "PowerCycle is the same capsule shape, slightly larger; DropOff is a flat-crimped squeeze tube with a round screw cap. Never stubby or wide. "
 "Rendered as a real X-ray: monochrome cool blue-white density only, no colour, the plastic and metal shells faint and translucent, the seam between cap and body a thin brighter line. "
 "NO printed words, NO labels, NO logos visible on the products - X-rays do not show print. "
 "Inside, the contents show as denser X-ray shapes: ShapeShift - pineapple chunks and coffee beans; NetWork - radish and cucumber slices and almonds; "
 "PowerCycle - garlic cloves, wheat grains and a rosemary sprig; DropOff - fibrous pineapple stem pieces and coffee beans.")
FIN=("PHOTOGRAPHIC FINISH\nA real medical X-ray radiograph film, indistinguishable from a real X-ray scan: monochrome, soft density gradients, slight edge glow, "
     "fine film grain and subtle scan noise, 8K detail. Absolutely no text, no letters, no numbers, no measurements, no dimension lines, no rulers, no labels anywhere.")
NEG=("Negative: text, letters, numbers, measurement lines, dimension arrows, rulers, cm, labels, logos, brand names, colour, coloured caps, glossy render, "
     "CGI, 3D render, illustration, two-tone background, visible seam, panel edge, black rectangle, frame border, skeleton, bones, hands, people, extra products, "
     "stubby or wide bottles, separate glass vessel with a cap.")
X={
'scatter':[OPEN,
 "A casual, real X-ray radiograph of four SickScience products lying on the X-ray table, as if casually dropped there.",
 "PRODUCT ORIENTATION\n"+BASE_ORIENT+" The products lie flat at different relaxed angles - one diagonal, one almost horizontal, one slightly overlapping another - a natural, unposed arrangement.",
 "COMPOSITION AND FRAMING\nUltra-wide 21:9 frame, straight top-down X-ray view. The loose group of four products sits in the right 55% of the frame; the left 45% is the same empty black film - calm, no objects.",
 "SCALE\nReal relative sizes: the two small capsules equal, PowerCycle slightly larger, the DropOff tube about 1.6 times the small capsule length.",
 "LIGHT AND SHADOW\nPure X-ray exposure: no external light, no reflections, no cast shadows; brightness only from material density.",
 "BACKGROUND\nOne continuous, seamless deep black-to-midnight-blue X-ray film across the ENTIRE frame, uniform from edge to edge, with a very soft vignette.",
 FIN, "INTEGRATION\nAll four products share one exposure and density scale and the same grain.", NEG],
'lean':[OPEN,
 "A casual, real X-ray radiograph of four SickScience products standing loosely together, a little playful.",
 "PRODUCT ORIENTATION\n"+BASE_ORIENT+" The products stand in a loose casual cluster: one leaning against another at a slight angle, one a little in front, the tube leaning on the back - unposed, relaxed, not a neat line-up.",
 "COMPOSITION AND FRAMING\nUltra-wide 21:9 frame, straight-on side X-ray view. The cluster sits in the right 55% of the frame; the left 45% is the same empty black film - calm, no objects.",
 "SCALE\nReal relative sizes: the two small capsules equal, PowerCycle slightly larger, the DropOff tube about 1.6 times the small capsule length.",
 "LIGHT AND SHADOW\nPure X-ray exposure: no external light, no reflections, no cast shadows; brightness only from material density.",
 "BACKGROUND\nOne continuous, seamless deep black-to-midnight-blue X-ray film across the ENTIRE frame, uniform from edge to edge, with a very soft vignette.",
 FIN, "INTEGRATION\nAll four products share one exposure and density scale and the same grain.", NEG],
}
if __name__=='__main__':
    open('/private/tmp/claude-501/p63.js','w').write('window.__p62='+json.dumps(X)+';"ok"')
    print('\n\n'.join(X['scatter']))
