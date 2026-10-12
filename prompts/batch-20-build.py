"""Batch 20 — new creative directions from TikTok-Shop top brands + current site campaigns (2026-10-07).
Square 1:1 masters, subject in the central ~46% width (Story/Feed are crops)."""
import json, importlib.util, sys, io, copy
def load(n, f):
    spec = importlib.util.spec_from_file_location(n, f); m = importlib.util.module_from_spec(spec)
    o = sys.stdout; sys.stdout = io.StringIO(); spec.loader.exec_module(m); sys.stdout = o; return m
b18 = load('b18', 'batch-18-build.py'); b19 = load('b19', 'batch-19-build.py')
LAB, PROP, FIN, INTEG, NEG, FRAME = b18.LAB, b18.PROP, b18.FIN, b18.INTEG, b18.NEG, b18.FRAME
caps, TUBE, p = b19.caps, b19.TUBE, b19.p
GEL = ("a translucent gel-serum — semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, slightly viscous, "
       "it holds a soft rounded bead and lets light pass through its edges")
GELNEG = "opaque white cream, thick white lotion, whipped or peaked cream, body butter, water-clear liquid, fully transparent gel, coloured or gold serum"
SETNW = ("Preserve the exact identity of every item in the set: proportions, construction, colours and printed branding exactly as the element shows them. "
         "Use the element for identity only; do not redraw any part of it. The set contains NetWork (red chrome capsule bottle, 12 cm tall), ShapeShift "
         "(violet chrome capsule bottle, 12 cm tall) and a rose-quartz gua sha stone. Exactly three items, no extra product. " + PROP)
SETV = ("Preserve the exact identity of every item in the set: proportions, construction, colours and printed branding exactly as the element shows them. "
        "Use the element for identity only; do not redraw any part of it. The set contains PowerCycle (lime-green chrome capsule bottle, 14 cm tall), DropOff "
        "(matte cobalt squeeze tube about 20 cm tall, standing on its cap) and ShapeShift (violet chrome capsule bottle, 12 cm tall). Exactly three products, no extra product. " + PROP)
out = {
 'ss20_tray': p('A real high-end editorial still-life photograph featuring ', 'ss-shapeshift', caps('violet'),
    'The product stands upright and perfectly vertical in the centre of a polished stainless-steel medical instrument tray, front label facing the camera.',
    'A clean rectangular stainless-steel instrument tray with softly rounded corners lies on a white surface, seen from a slightly high three-quarter angle; inside the tray, beside the product, lie two neatly folded white cotton gauze squares and a pair of polished steel tweezers. No syringes, no needles. The tray is centred.',
    'The product is 12 cm tall and 3.5 cm in diameter; the tray is 30 cm long and 20 cm wide; the tweezers are 12 cm long.',
    'Cool clean clinical key light from above-left, crisp specular highlights on the steel tray and the chrome, soft shadow.',
    'A bright white clinical surface and a soft pale grey-white wall; calm, airy, premium medical-aesthetic mood.',
    '85mm at f/8. Brushed and polished steel, mirror chrome, soft cotton texture. Fine grain, crisp clean colour with violet accent from the cap.',
    'syringes, needles, blood, pills, medical text, labels on the tray'),
 'ss20_receipt': p('A real high-end luxury still-life photograph featuring ', 'ss-set-vault', SETV,
    'The three products stand upright side by side, touching, on a white marble plinth, front labels facing the camera.',
    'TIGHT CLUSTER: the group is only about 26% of the frame width, centred, in the upper-middle of the frame. The lower 35% of the frame in front of the plinth is a clean, empty, smooth white marble surface (space for a graphic added later).',
    'PowerCycle 14 cm, DropOff about 20 cm (the tallest), ShapeShift 12 cm; the plinth is 6 cm tall and 30 cm wide.',
    'Bright soft daylight from the left, gentle shadow to the right, crisp chrome highlights.',
    'A seamless warm white backdrop and white marble; nothing else.',
    '85mm at f/8. Polished marble, mirror chrome, matte tube. Fine grain, bright clean premium colour.',
    'paper, receipts, text, price tags'),
 'ss20_tag': p('A real high-end studio product photograph featuring ', 'ss-dropoff', TUBE,
    'The tube stands upright on its cap on a pale stone ledge, front label facing the camera.',
    'Tied around the tube with a thin natural cotton string hangs one blank rectangular kraft-paper price tag with a small round reinforced hole; the tag hangs in front of the lower part of the tube, perfectly flat and facing the camera straight on, completely blank (no text, no numbers). The tube is centred.',
    'The tube is about 20 cm tall; the tag is 7 cm by 4 cm.',
    'Soft warm window light from the left, gentle shadow, the kraft tag evenly lit.',
    'A warm off-white plaster wall and pale travertine ledge; calm and minimal.',
    '85mm at f/8. Matte tube, fibrous kraft paper, cotton string, stone. Fine grain, soft warm premium colour.',
    'text on the tag, numbers on the tag, barcode, multiple tags'),
 'ss20_refill': p('A real high-end studio product photograph featuring ', 'ss-shapeshift', caps('violet'),
    'Five identical copies of the product stand upright in a single straight row receding diagonally from the front-right towards the back-left, each about 4 cm apart, all front labels facing the camera.',
    'The row of identical bottles recedes in perspective on a glossy pale-lilac surface, the nearest bottle sharp and centred, the farther ones gradually softer in shallow focus, like a calm production line. Exactly five bottles, all the same product.',
    'Each bottle is 12 cm tall and 3.5 cm in diameter; the nearest bottle occupies only about 24% of the frame height.',
    'Soft directional key light from the front-left, clean reflections on the glossy surface, crisp chrome highlights on the nearest bottle.',
    'A seamless gradient backdrop from white at the top to pale lilac at the floor; nothing else.',
    '100mm at f/4, focus on the nearest bottle. Mirror chrome, glossy floor. Fine grain, clean premium colour.',
    'different products in the row, more than five bottles, conveyor belt machinery, boxes'),
 'ss20_spoon': p('A real high-end food-styling-inspired still-life photograph featuring ', 'ss-shapeshift', caps('violet'),
    'The product stands upright and perfectly vertical slightly behind and to the right of a polished silver dessert spoon, front label facing the camera.',
    f'In the foreground a polished silver dessert spoon rests on a small round white porcelain dessert plate; in the bowl of the spoon sits one glossy bead of {GEL}. A second tiny bead sits on the plate beside the spoon. The plate and product are centred.',
    'The product is 12 cm tall and 3.5 cm in diameter; the dessert spoon is 15 cm long; the plate is 16 cm in diameter.',
    'Soft bright key light from the back-left creating a glowing rim on the gel bead and crisp highlights on the silver spoon and the chrome.',
    'A seamless pale blush-lilac backdrop and matching surface, airy pastel patisserie mood; nothing else.',
    '100mm macro-portrait look at f/5.6, the gel bead tack sharp. Polished silver, porcelain, mirror chrome. Fine grain, soft pastel premium colour.',
    GELNEG + ', food, dessert, cake, fruit, cutlery other than one spoon'),
 'ss20_kit': p('A real high-end luxury still-life photograph featuring ', 'ss-set-glp1-v2', SETNW,
    'The three items lie nested in precisely cut foam cutouts inside an open hard-shell case seen from a high three-quarter angle, front labels facing up towards the camera.',
    'A sleek open white hard-shell case (like a premium recovery kit or instrument case) with a smooth matte white lid standing open behind; inside, soft pale-grey foam with exact cutouts holds the two bottles lying side by side and the gua sha stone beside them. TIGHT: the open case is about 46% of the frame width, centred.',
    'Each bottle is 12 cm long; the gua sha stone is 9 cm; the case is 32 cm wide.',
    'Bright soft overhead key light, gentle shadows inside the foam cutouts, crisp chrome highlights.',
    'A seamless pale grey-white backdrop and surface; clean clinical-luxury mood; nothing else.',
    '70mm at f/8. Matte case, soft foam, mirror chrome, polished stone. Fine grain, clean premium colour.',
    'text on the case, logos on the case, medical crosses, pills, syringes'),
}
# proportion of bottles lying down is risky: kit gets a stronger PROP reminder
out['ss20_kit'][2] = out['ss20_kit'][2].replace('Negative: ', 'Negative: bottles shorter or fatter than normal, ')
json.dump(out, open('batch-20.json', 'w'), ensure_ascii=True)
for k, v in out.items(): print(k, v[1], len(v[0] + v[2]))

# v2 fixes after first pass: spoon got a geode backdrop + giant product; tag hung sideways and product too big
SMALL = ("SIZE IS CRITICAL: photographed from further back; the product is SMALL in the frame — only about 26% of the frame height — "
         "with lots of calm empty background around it. ")
x = copy.deepcopy(out['ss20_spoon'])
x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + SMALL, 1)
x[2] = x[2].replace('BACKGROUND\n', 'BACKGROUND\nABSOLUTELY PLAIN: ', 1)
x[2] = x[2].replace('Negative: ', 'Negative: crystals, geode, amethyst, gemstones, rocks, stones, minerals, giant product filling the frame, ')
out['ss20_spoon_b'] = x
x = copy.deepcopy(out['ss20_tag'])
x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + SMALL + 'The tag hangs straight down at the centre front of the tube, parallel to the camera, never turned sideways. ', 1)
x[2] = x[2].replace('Negative: ', 'Negative: tag turned sideways, tag hanging off to the side, giant product filling the frame, ')
out['ss20_tag_b'] = x
json.dump(out, open('batch-20.json', 'w'), ensure_ascii=True)
print('v2 added')

# v3: refill stubby/huge, kit bottles short, spoon_b silver half rendered as clear glass
CHROME = "The lower half of every bottle is OPAQUE mirror-polished silver chrome metal — never clear glass, never transparent. "
x = copy.deepcopy(out['ss20_refill'])
x[2] = x[2].replace('Five identical copies', 'Three identical copies').replace('Exactly five bottles', 'Exactly three bottles').replace('more than five bottles', 'more than three bottles')
x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + SMALL + 'Each bottle is slim and tall like a lipstick-shaped capsule, 3.4 times taller than wide. The whole row fits inside the central 46% of the frame width. ', 1)
x[2] = x[2].replace('the nearest bottle occupies only about 24% of the frame height', 'the nearest bottle occupies only about 22% of the frame height')
x[2] = x[2].replace('Negative: ', 'Negative: short fat bottles, bottles wider than one third of their height, row filling the frame width, ')
out['ss20_refill_c'] = x
x = copy.deepcopy(out['ss20_kit'])
x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\nPROPORTIONS WHILE LYING DOWN: each bottle lying in the foam is LONG AND SLIM — its length is 3.4 times its diameter, exactly like a slim lipstick-shaped capsule; the foam cutouts are long narrow slots. ' + CHROME, 1)
out['ss20_kit_c'] = x
x = copy.deepcopy(out['ss20_spoon_b'])
x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + CHROME + 'The product stands on the table surface beside the plate, not on the plate. ', 1)
x[2] = x[2].replace('Negative: ', 'Negative: clear glass bottle, transparent lower half, product standing on the plate, ')
out['ss20_spoon_c'] = x
json.dump(out, open('batch-20.json', 'w'), ensure_ascii=True)
print('v3 added')

# receipt layouts: tall master (products low, receipt graphic hangs from the top) and square master (products left, receipt right)
x = copy.deepcopy(out['ss20_receipt'])
x[2] = x[2].replace(FRAME, "TALL 9:16 VERTICAL frame. CRITICAL LAYOUT: the upper 52% of the frame is calm, empty, softly lit warm white wall (space for a graphic added later); the products and plinth sit in the band between 55% and 78% of the frame height, centred horizontally and only about 36% of the frame width; the lower part is calm marble.")
x[2] = x[2].replace('TIGHT CLUSTER: the group is only about 26% of the frame width, centred, in the upper-middle of the frame. The lower 35% of the frame in front of the plinth is a clean, empty, smooth white marble surface (space for a graphic added later).', 'The three products stand touching as one compact group.')
out['ss20_receipt_s'] = x
x = copy.deepcopy(out['ss20_receipt'])
x[2] = x[2].replace(FRAME, "SQUARE 1:1 frame. CRITICAL LAYOUT: the products and plinth stand in the LEFT part of the frame, the group centred at about 30% of the frame width and occupying only about 30% of the frame width; the RIGHT 50% of the frame is calm, empty marble and wall (space for a graphic added later). The upper 30% of the frame is calm empty wall.")
x[2] = x[2].replace('TIGHT CLUSTER: the group is only about 26% of the frame width, centred, in the upper-middle of the frame. The lower 35% of the frame in front of the plinth is a clean, empty, smooth white marble surface (space for a graphic added later).', 'The three products stand touching as one compact group on the left.')
out['ss20_receipt_q'] = x
json.dump(out, open('batch-20.json', 'w'), ensure_ascii=True)
print('receipt layouts added', 'TALL' in out['ss20_receipt_s'][2], 'RIGHT 50%' in out['ss20_receipt_q'][2])
x = copy.deepcopy(out['ss20_spoon_c'])
x[2] = x[2].replace(FRAME, "TALL 9:16 VERTICAL frame. CRITICAL LAYOUT: the upper 50% of the frame is calm, empty, plain pastel backdrop (space for text added later); the plate, spoon and product sit in the band between 52% and 80% of the frame height, centred horizontally; the lower part is calm plain surface.")
out['ss20_spoon_s'] = x
json.dump(out, open('batch-20.json', 'w'), ensure_ascii=True)
print('spoon_s', 'TALL' in x[2])
