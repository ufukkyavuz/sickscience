// Batch-99 (2026-11-05): Kasım indirimleri için yeni sahneler. Stil = batch-95 B (koyu/cam lab bilim kampanyası).
// Faz 1 (9–22 Kasım, setlerde %25): Black Friday küçük. Faz 2 (22–29 Kasım, %30): BLACK FRIDAY + 30% dev.
// Ürünler element DEĞİL gerçek fotoğraf referansı (elementler siyah şerit taşıyor). Composer 9:16, Nano Banana Pro, 2K, Unlimited.
// Refs sırası her sahnede `refs` dizisinde; prompt "image N" ile onlara atıf yapar.
window.__K = (() => {
const CAP = (n) => `Image 1 is a real photo of the ShapeShift capsule and shows the true construction of every capsule in this brand: a slim rounded pill, its glossy coloured chrome cap is exactly the upper half, the lower half is mirror-polished silver chrome, rounded at both ends. The brand words are printed in thin pure white letters running vertically, directly on the chrome of the cap and of the silver half. The word SickScience is printed only on the coloured cap, and the product name (ShapeShift, NetWork or PowerCycle) only on the silver half, each once. There is NO printed band, strip or label behind the letters. PROPORTIONS ARE CRITICAL: the ShapeShift and NetWork capsules are slim and tall, height 3.4 times width, never stubby. ${n}`;
const END = "Fine photographic grain. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. All product text must be perfectly legible, sharp, and accurate, no blurry or distorted letters. No text, no letters, no logos added to the scene; only the products' own printed words.";
const INT = "INTEGRATION\n\nThe products are physically in this scene: same light direction, softness and colour temperature, their chrome reflects this environment, real contact shadow, real reflection on the surface below, same sharpness and grain as the scene, no outline, no halo.";
const NEG = "black band on the capsule, black strip, dark vertical stripe behind the text, label, sticker, stubby or wide bottle, cap shorter or longer than half, black or grey letters on the product, misspelled text, 'Network' with a lowercase w, extra products, pasted or composited look, cut-out edges, halo, floating product, flat lighting, CGI, 3D render, watermark, added text";
const P = {
B1:{refs:["_calisma/batch-97-ss-normal/ref_gercek_ss.jpg","Products/site/dropoff_01.jpg"],t:`A real science campaign photograph of two products. The idea: the body duo standing on a sheet of wet black glass, lit by one cold strip of light.

${CAP("Image 2 shows the DropOff tube: a matte cobalt blue squeeze tube standing upright on its blue cap, white vertical lettering; copy its design exactly.")} Exactly two products: the DropOff tube and the violet ShapeShift capsule. No extra product.

PRODUCT ORIENTATION

The tube stands upright on its cap, slightly behind and left. The violet capsule stands upright in front of it to the right, overlapping the tube a little. Labels face the camera, text vertical. Camera low, level with the middle of the capsule.

COMPOSITION AND FRAMING

Vertical 9:16 frame, 85mm lens. Both products horizontally centred inside the middle 50% of the frame width, standing from 46% to 78% of the frame height. Behind them, softly out of focus, one tall clear graduated glass cylinder on the left and a round-bottom flask on the right, cropped by the frame edges. The band from 10% to 40% of the frame height is calm, dark and empty for a headline. The bottom 20% is the black glass surface with reflections.

SCALE

If the ShapeShift capsule is 100 tall, the DropOff tube is 165 tall. The capsule is 12 cm tall and 3.5 cm wide, the tube 20 cm tall. The graduated cylinder is 40 cm tall.

LIGHT AND SHADOW

One long horizontal white strip light from above and behind draws bright clean vertical highlights down the chrome and the tube edges. Soft frontal fill keeps every printed word readable. Thin bright rim lines on the glass.

BACKGROUND

Deep slate grey-blue falling to near black at the top. Wet black glass surface with fine water droplets and a mirror reflection of the products.

PHOTOGRAPHIC FINISH

f/5.6. Monochrome steel-blue grade: everything is silver, slate and blue-grey, the only saturated colours are the violet capsule and the cobalt tube. ${END}

${INT}

KEY COMPOSITION

COBALT TUBE AND VIOLET CAPSULE ON WET BLACK GLASS, CENTRED, DARK EMPTY SPACE ABOVE, STEEL-BLUE LAB GLASS BEHIND.

Negative: ${NEG}, warm colour cast, coloured liquid, hands, people, numbers.`},
S2:{refs:["_calisma/batch-97-ss-normal/ref_gercek_ss.jpg","Products/site/shapeshift-on-the-go_01.jpg"],t:`A real luxury product photograph. The idea: the travel kit, a violet capsule and its violet mesh pouch, presented like a precious object on a dark bench.

${CAP("Image 2 shows the ShapeShift On-the-Go kit: a semi-transparent violet mesh zipper pouch with a small white SickScience tag, and the violet ShapeShift capsule. Copy the pouch exactly; take the capsule construction from image 1.")} Exactly two items: one violet mesh pouch and one violet ShapeShift capsule. No extra product.

PRODUCT ORIENTATION

The pouch stands upright, slightly turned, behind and left. The capsule stands upright in front of it to the right, label facing the camera, text vertical. Camera slightly below the top of the capsule.

COMPOSITION AND FRAMING

Vertical 9:16 frame, 70mm lens. The pair is horizontally centred inside the middle 55% of the frame width, from 50% to 80% of the frame height. A glossy black bench surface fills the bottom 20%. The band from 10% to 42% of the frame height is clean dark gradient for a headline.

SCALE

The pouch is 21 cm wide and 16 cm tall. The capsule is 12 cm tall and 3.5 cm wide, so it is three quarters of the pouch height.

LIGHT AND SHADOW

A soft overhead box light makes a gentle pool of light on the bench, a narrow back light separates the pouch mesh from the background and shows its texture. Long clean highlights on the chrome. Every printed word lit and readable.

BACKGROUND

Smooth graphite backdrop, lighter just behind the products, falling to black at the top and corners.

PHOTOGRAPHIC FINISH

f/6.3. Fine mesh weave visible on the pouch, mirror chrome with real reflections of the bench and backdrop. Neutral silver grade, deep blacks, the only saturated colour is violet. ${END}

${INT}

KEY COMPOSITION

VIOLET MESH POUCH AND VIOLET CAPSULE ON A GLOSSY BLACK BENCH, CENTRED LOW, DARK EMPTY SPACE ABOVE.

Negative: ${NEG}, open pouch, products inside the pouch, red pouch, wrinkled crumpled pouch, hands, people.`},
N3:{refs:["_calisma/batch-97-ss-normal/ref_gercek_ss.jpg","Products/site/network-on-the-go_01.jpg"],t:`A real science campaign photograph. The idea: the red NetWork travel kit standing among cold clear lab glass, the only warm colour in a silver world.

${CAP("Image 2 shows the NetWork On-the-Go kit: a semi-transparent red mesh zipper pouch with a small white SickScience tag, and the NetWork capsule with a glossy RED chrome cap. The label reads exactly 'NetWork' with a capital N and a capital W. Copy the pouch and the red colour exactly; take the capsule construction from image 1, no band behind the letters.")} Exactly two items: one red mesh pouch and one red NetWork capsule. No extra product.

PRODUCT ORIENTATION

The pouch stands upright behind and left, the capsule stands upright in front to the right, label facing the camera, text vertical. Camera level with the capsule.

COMPOSITION AND FRAMING

Vertical 9:16 frame, 100mm lens, compressed perspective. The pair is horizontally centred inside the middle 55% of the frame width, from 50% to 80% of the frame height, sharp. Behind them, softly out of focus, a large clear conical flask on the left and a beaker on the right, overlapping the frame edges. The band from 10% to 42% of the frame height is calm pale grey gradient for a headline.

SCALE

The pouch is 21 cm wide and 16 cm tall. The capsule is 12 cm tall and 3.5 cm wide. The conical flask is 30 cm tall.

LIGHT AND SHADOW

Soft cool daylight from the left through frosted glass, bright clean highlights on the glass rims and the chrome, soft contact shadows. Every printed word lit and readable.

BACKGROUND

Pale silver-grey lab backdrop, lighter at the top. A satin steel bench with a soft reflection.

PHOTOGRAPHIC FINISH

f/4. Clear thin glass with crisp edges, fine mesh weave on the pouch, mirror chrome. Monochrome silver world where the only saturated colour is red. ${END}

${INT}

KEY COMPOSITION

RED MESH POUCH AND RED CAPSULE, SHARP, CENTRED LOW, AMONG SOFT CLEAR LAB GLASS, PALE SILVER WORLD.

Negative: ${NEG}, violet pouch, open pouch, coloured liquid in the glass, warm cast, hands, people.`},
H4:{refs:["_calisma/batch-97-ss-normal/ref_gercek_ss.jpg","Products/site/network_01.jpg","Products/site/powercycle_01.jpg","Products/site/dropoff_01.jpg"],t:`A real high-end campaign photograph of the whole range. The idea: four formulas lined up on a long black mirror bench under one cold beam, a vast dark space above them.

${CAP("Image 2 shows the NetWork capsule: glossy RED chrome cap, label 'NetWork' with a capital N and capital W. Image 3 shows the PowerCycle capsule: glossy GREEN chrome cap, larger. Image 4 shows the DropOff tube: matte cobalt blue squeeze tube on its blue cap. Take every capsule's construction from image 1: no band behind the letters, white letters directly on the chrome.")} Exactly four products: violet ShapeShift capsule, red NetWork capsule, green PowerCycle capsule, cobalt DropOff tube. No extra product.

PRODUCT ORIENTATION

All four stand upright in one slightly staggered row, from left to right: green PowerCycle capsule, violet ShapeShift capsule, cobalt DropOff tube slightly behind, red NetWork capsule. Labels face the camera, text vertical. Camera low, level with the capsule middles.

COMPOSITION AND FRAMING

Vertical 9:16 frame, 85mm lens. The row is horizontally centred inside the middle 70% of the frame width and stands from 56% to 80% of the frame height, products small and elegant. The black mirror bench fills the bottom 20% with long reflections. The whole band from 8% to 50% of the frame height is empty deep dark space for a very large headline.

SCALE

If the ShapeShift capsule is 100 tall, NetWork is 100, PowerCycle is 117 tall and 25% wider, the DropOff tube is 165. Real sizes: ShapeShift and NetWork 12 cm tall, 3.5 cm wide; PowerCycle 14 cm tall, 4.5 cm wide; DropOff 20 cm tall.

LIGHT AND SHADOW

One narrow cold white beam from straight above lights the row and fades upward into darkness. Crisp vertical highlights on every chrome cap and on the tube. Soft frontal fill keeps all printed words readable.

BACKGROUND

Pure deep charcoal-black, with a faint vertical glow of the beam behind the products. Nothing else.

PHOTOGRAPHIC FINISH

f/8. Mirror chrome, matte tube plastic, glossy black bench reflections. Neutral silver grade, deep blacks, the only saturated colours are the four product colours. ${END}

${INT}

KEY COMPOSITION

FOUR PRODUCTS IN ONE ROW LOW IN THE FRAME ON A BLACK MIRROR BENCH, ONE COLD BEAM FROM ABOVE, HUGE EMPTY DARK SPACE ABOVE.

Negative: ${NEG}, green capsule same size as violet capsule, products large in frame, products in the upper half, gradient colour wall, smoke, hands, people.`},
H5:{refs:["_calisma/batch-97-ss-normal/ref_gercek_ss.jpg","_calisma/batch-97-ss-normal/ref_gercek_ss2.jpg"],t:`A real dramatic product photograph. The idea: one ShapeShift capsule alone in a single hard shaft of white light in total darkness, like an object revealed on one night only.

${CAP("Image 2 is a second real photo of the same ShapeShift capsule.")} Exactly one product, no extra product.

PRODUCT ORIENTATION

The capsule stands upright, label facing the camera, text vertical. Camera low, level with the middle of the capsule.

COMPOSITION AND FRAMING

Vertical 9:16 frame, 100mm lens. The capsule is horizontally centred, from 54% to 80% of the frame height. A hard vertical shaft of white light falls from the top of the frame onto it, visible as a faint column in very light haze, and makes a sharp bright ellipse on the black floor around it. The whole band from 8% to 48% of the frame height is dark, only crossed by the faint light shaft, empty for a very large headline.

SCALE

The capsule is 12 cm tall and 3.5 cm wide. The light ellipse on the floor is about three times the capsule width.

LIGHT AND SHADOW

Single hard top light. Bright crisp highlight down the violet cap and the silver half, deep falloff to black at the sides. A faint frontal fill so the white printed words read clearly.

BACKGROUND

Total black. Glossy black floor with a soft mirror reflection of the capsule inside the light ellipse.

PHOTOGRAPHIC FINISH

f/8. Mirror chrome reflecting the light ellipse, very faint atmospheric haze only inside the light shaft. Neutral grade, inky blacks, the only colour is violet. ${END}

${INT}

KEY COMPOSITION

ONE VIOLET CAPSULE IN A HARD SHAFT OF WHITE LIGHT, LOW IN THE FRAME, TOTAL BLACK, HUGE EMPTY SPACE ABOVE.

Negative: ${NEG}, thick smoke, fog cloud, spotlight fixture visible, coloured light, stage, hands, people.`},
V6:{refs:["_calisma/batch-97-ss-normal/ref_gercek_ss.jpg","Products/site/powercycle_01.jpg","Products/site/dropoff_01.jpg"],t:`A real bright science campaign photograph. The idea: the three formulas of the Vault set held in a polished steel laboratory clamp stand on a white lab bench, clean and precise.

${CAP("Image 2 shows the PowerCycle capsule: glossy GREEN chrome cap, the largest capsule. Image 3 shows the DropOff tube: matte cobalt blue squeeze tube on its blue cap. Take every capsule's construction from image 1.")} Exactly three products: green PowerCycle capsule, cobalt DropOff tube, violet ShapeShift capsule. No extra product.

PRODUCT ORIENTATION

The DropOff tube stands upright in the centre, held gently at its middle by a steel clamp of a lab retort stand. The PowerCycle capsule stands on the bench to the left of the stand base, the ShapeShift capsule to the right. Labels face the camera, text vertical. Camera level with the bench, straight on.

COMPOSITION AND FRAMING

Vertical 9:16 frame, 70mm lens. The retort stand rod rises on the left edge. The group is horizontally centred inside the middle 60% of the frame width, from 48% to 80% of the frame height. A white lab bench fills the bottom 20%. The band from 10% to 40% of the frame height is clean bright white-grey space for a headline. A clear beaker and a small petri dish with a translucent gel-serum bead stand softly out of focus behind.

SCALE

If the ShapeShift capsule is 100 tall, PowerCycle is 117 tall and 25% wider, the DropOff tube is 165 tall. The beaker is 15 cm tall.

LIGHT AND SHADOW

Bright soft daylight from a large window on the left, crisp highlights on the chrome and the steel stand, soft grey contact shadows. Every printed word lit and readable.

BACKGROUND

Bright white-grey lab wall, soft and plain.

PHOTOGRAPHIC FINISH

f/5.6. Polished steel, mirror chrome, matte tube, thin clear glass, a translucent gel-serum bead (semi-transparent with a soft milky haze, neither opaque cream nor water-clear). Cool clean white grade, high-key. ${END}

${INT}

KEY COMPOSITION

STEEL LAB CLAMP STAND HOLDING THE COBALT TUBE, GREEN AND VIOLET CAPSULES ON THE WHITE BENCH, BRIGHT WHITE LAB, CLEAN SPACE ABOVE.

Negative: ${NEG}, green capsule same size as violet capsule, dark scene, coloured liquid, warm colour cast, numbers on the glass, hands, people.`}
};
return P;
})();
