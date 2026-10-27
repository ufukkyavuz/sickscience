"""Batch 62 — Amazon What's inside, real products (user 2026-10-20: "üstünde takke gibi duran kapağımız var mı… düzgün olanını yap… X-ray'de görünümü").
Full-bleed 21:9 scene (3000x1286 slot): four real products on the RIGHT ~55%, calm empty space on the LEFT for Figma text.
Opening line takes 4 element mentions typed in the composer: ss-shapeshift, ss-network-v2, ss-powercycle, ss-dropoff."""
import json
OPEN=" element references exactly for the four products: silhouette, proportions, cap and label layout. Exactly four products, no extra product."
ORDER="From left to right: ShapeShift (violet), NetWork (red), PowerCycle (green), DropOff (cobalt tube)."
PROP="PROPORTIONS ARE CRITICAL: ShapeShift and NetWork are slim capsules 12 cm tall and 3.5 cm wide (height 3.4x width), the coloured cap is exactly the upper half and the silver body the lower half; PowerCycle is 14 cm tall and 4.5 cm wide with the same half-and-half split; DropOff is a flat-crimped squeeze tube about 20 cm tall standing on its round cobalt cap. Never stubby, chubby, squat or wide. The label reads exactly 'NetWork' with a capital N and a capital W."
INSIDE=("Inside each product the real raw ingredients are visible: ShapeShift - pineapple chunks and coffee beans in gel; "
        "NetWork - radish and cucumber slices and almonds in gel; PowerCycle - garlic cloves, wheat grains and a rosemary sprig in gel; "
        "DropOff - fibrous pineapple stem pieces and coffee beans in gel.")
COMP=("COMPOSITION AND FRAMING\nUltra-wide 21:9 frame, camera straight on at product mid-height, orthographic feel, no tilt. "
      "The four products stand upright in a neat row on the RIGHT 55% of the frame, evenly spaced, all on the same baseline, bottoms in the lower third. "
      "The LEFT 45% of the frame is calm, empty, uncluttered background for text - nothing there.")
SCALE="SCALE\nCapsules 12 cm and 14 cm tall, the DropOff tube about 20 cm tall; real relative sizes between the four products. If in doubt make the products smaller, never bigger."
NEG_C="extra products, fifth bottle, glass vessel with a separate cap, clear glass bottle, stubby chubby or wide bottle, warped label, misspelled label, 'Network' with lowercase w, text, headline, logos added to the scene, watermark, CGI, cartoon, illustration"
X={
'xray_dark':[
 "Match the",  # + 4 mentions + OPEN
 "A premium medical-grade X-ray radiograph of the four SickScience products, scientific and beautiful.",
 "PRODUCT ORIENTATION\n"+ORDER+" "+PROP+" The products are shown as an X-ray image: glowing pale cyan-white translucent silhouettes on deep black, the outer shell faint and glassy, the cap and base outlines crisp, the vertical label stripe faintly visible. "+INSIDE+" The ingredients read as brighter, denser X-ray shapes inside each product - recognisable pineapple chunks, coffee beans, garlic cloves, almonds, radish slices - like a real radiograph of the contents.",
 COMP,
 SCALE,
 "LIGHT AND SHADOW\nPure X-ray look: no external light, no reflections; luminous cool cyan-white density on black, soft glow at the dense areas, faint fine film grain.",
 "BACKGROUND\nDeep matte black X-ray film background with a very subtle cool blue vignette; nothing else.",
 "PHOTOGRAPHIC FINISH\nUltra photorealistic, hyperrealistic real radiograph film scan, indistinguishable from a real X-ray, 8K detail, crisp edges, fine grain. No text, no letters, no logos added to the scene.",
 "INTEGRATION\nAll four products share the same X-ray exposure and density scale; same sharpness; same baseline.",
 "Negative: "+NEG_C+", colour photo, chrome reflections, skeleton, bones, hands, people, medical scanner machine, rainbow colours."],
'xray_light':[
 "Match the",
 "A premium inverted X-ray radiograph of the four SickScience products on light film, scientific, clean and elegant.",
 "PRODUCT ORIENTATION\n"+ORDER+" "+PROP+" The products are shown as an inverted X-ray: deep navy and slate-blue density shapes on pale film, the shell outline crisp, the cap halves slightly darker, each cap keeps a faint hint of its colour (violet, red, green, cobalt). "+INSIDE+" The ingredients read as darker, denser X-ray shapes inside - recognisable pineapple chunks, coffee beans, garlic cloves, almonds, radish slices.",
 COMP,
 SCALE,
 "LIGHT AND SHADOW\nEven backlit lightbox look, no external reflections, soft density gradients, fine film grain.",
 "BACKGROUND\nPale cool-white X-ray film on a lightbox, very soft gradient, subtle film texture; nothing else.",
 "PHOTOGRAPHIC FINISH\nUltra photorealistic, hyperrealistic real radiograph film, indistinguishable from a real X-ray, 8K detail, crisp edges, fine grain. No text, no letters, no logos added to the scene.",
 "INTEGRATION\nAll four products share the same exposure and density scale; same sharpness; same baseline.",
 "Negative: "+NEG_C+", colour photo, chrome reflections, skeleton, bones, hands, people, dark background."],
'seethrough':[
 "Match the",
 "A premium scientific studio photograph of the four real SickScience products rendered see-through, like a formula made visible.",
 "PRODUCT ORIENTATION\n"+ORDER+" "+PROP+" Each product keeps its exact real shape and label, but its body is made of clear glass: the cap half is translucent glass tinted in its colour (violet, ruby red, emerald green), the lower half is clear glass, the black vertical label stripe with pure white text stays on the glass. The DropOff tube is clear glass tinted cobalt at its cap. "+INSIDE+" The gel is a translucent gel-serum with a soft milky haze.",
 COMP,
 SCALE,
 "LIGHT AND SHADOW\nBright high-key studio light: large soft key from the upper left, white bounce fill, crisp clean glass refractions and caustics, soft contact shadows and faint reflections on the surface.",
 "BACKGROUND\nSeamless very pale lilac-white studio backdrop on a glossy white surface; nothing else.",
 "PHOTOGRAPHIC FINISH\n100mm lens at f/8, everything tack sharp. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. All product text must be perfectly legible, sharp, and accurate - no blurry or distorted letters. Every word printed on the products is pure white on the black stripe. No text, no letters, no logos added to the scene (product labels only).",
 "INTEGRATION\nAll four products share one light direction and colour temperature; real refraction; real contact shadows; no outline, halo or pasted look.",
 "Negative: "+NEG_C+", chrome, opaque bottle, black letters, dark or grey text on the product, dark background, people, hands."],
}
if __name__=='__main__':
    for k,v in X.items(): json.dump(v,open(f'/private/tmp/claude-501/p62_{k}.json','w'))
    print('\n\n'.join(X['xray_dark'][1:]))
