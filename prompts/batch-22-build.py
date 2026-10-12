"""Batch 22 (2026-10-07) — fresh scenes replacing re-used archive images in batch-21 concepts 21-35 (user: 'daha önce kullandığın görselleri tekrar kullanma')."""
import json, importlib.util, sys, io, copy
def load(n, f):
    spec = importlib.util.spec_from_file_location(n, f); m = importlib.util.module_from_spec(spec)
    o = sys.stdout; sys.stdout = io.StringIO(); spec.loader.exec_module(m); sys.stdout = o; return m
b18 = load('b18', 'batch-18-build.py'); b19 = load('b19', 'batch-19-build.py'); b21 = load('b21', 'batch-21-build.py')
PROP, caps, TUBE, p = b18.PROP, b19.caps, b19.TUBE, b19.p
SMALL, FULL, ident_set, add0 = b21.SMALL, b21.FULL, b21.ident_set, b21.add
J = {}
def add(k, *a, small=True, opener='A real high-end editorial still-life photograph featuring '):
    x = p(opener, *a)
    x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + FULL + (SMALL if small else ''), 1)
    x[2] = x[2].replace('Negative: ', 'Negative: borders, letterbox bands, ' + ('giant product filling the frame, ' if small else ''))
    J[k] = x
S = caps
VAULT = ident_set('PowerCycle (lime-green chrome capsule bottle, 14 cm tall), DropOff (matte cobalt squeeze tube about 20 cm tall standing on its cap) and ShapeShift (violet chrome capsule bottle, 12 cm tall)','three products')
DUO = ident_set('ShapeShift (violet chrome capsule bottle, 12 cm tall) and PowerCycle (lime-green chrome capsule bottle, 14 cm tall)','two products')
GLP = ident_set('NetWork (red chrome capsule bottle, 12 cm tall), ShapeShift (violet chrome capsule bottle, 12 cm tall) and a rose-quartz gua sha stone','three items: two bottles and the gua sha')
add('b22_vault','ss-set-vault',VAULT,'The three products stand upright side by side, touching, inside a pulled-out brushed-steel safe-deposit-box drawer, front labels facing the camera.',
    'A wall of small brushed-steel safe-deposit lockers fills the background softly out of focus; one long drawer is pulled out towards the camera and the three products stand in it, centred.',
    'PowerCycle 14 cm, DropOff about 20 cm, ShapeShift 12 cm; the drawer is 40 cm long.','Cool clean light from above with soft violet accent light, crisp steel and chrome highlights.',
    'Out-of-focus wall of steel lockers, calm and luxurious.','85mm at f/5.6. Brushed steel, mirror chrome, matte tube. Fine grain, cool premium colour.','money, gold, numbers on lockers, text, keys')
add('b22_duo','ss-set-award-duo',DUO,'The two products stand upright about 10 cm apart on a wide round white plaster pedestal, front labels facing the camera.',
    'A wide low white pedestal with soft curved edges; a large soft arch-shaped shadow of a window falls across the pale wall behind; the two products clearly separated, centred.',
    'ShapeShift 12 cm, PowerCycle 14 cm; the pedestal is 40 cm wide and 10 cm tall.','Warm late-afternoon window light from the right casting a soft arch shadow, crisp chrome highlights.',
    'Pale warm-grey plaster wall; minimal sculptural mood.','85mm at f/8. Plaster, mirror chrome. Fine grain, warm minimal colour.','text, extra products, plants')
add('b22_glp','ss-set-glp1-v2',GLP,'The two bottles stand upright side by side on a crisp white linen bed with the gua sha stone lying flat in front, front labels facing the camera.',
    'A neatly made white bed with soft rumpled linen and a pale grey knitted throw folded at one side; calm restful recovery morning; the items centred.',
    'Each bottle is 12 cm tall; the gua sha stone is 9 cm long.','Soft cool morning window light from the left, gentle shadows on the linen.','Out-of-focus serene white bedroom.',
    '50mm at f/4. Linen, knit, mirror chrome, polished stone. Fine grain, airy calm colour.','people, text, phones, pills')
add('b22_vanity','ss-shapeshift',S('violet'),'The product stands upright on a white lacquered dressing table in front of a Hollywood vanity mirror framed by round warm bulbs, front label facing the camera.',
    'The bulb-framed mirror fills the background softly; a few makeup brushes in a glass cup to one side; backstage glamour; the product centred.',
    'The product is 12 cm tall; the bulbs are 8 cm in diameter.','Warm glowing bulb light from behind and the sides, crisp chrome highlights.','Out-of-focus backstage dressing room.',
    '50mm at f/4. Lacquer, glass, warm bulbs, mirror chrome. Fine grain, warm glam colour.','people or faces in the mirror, text, logos')
add('b22_green','ss-powercycle',S('lime-green'),'The product stands upright on a round dark-green marble pedestal, front label facing the camera.',
    'A single spotlight pool on the pedestal in an otherwise moody deep-green room with a fluted green wall panel behind; the product centred.',
    'The product is 14 cm tall and 4.5 cm in diameter; the pedestal is 25 cm wide.','Dramatic single top spotlight, crisp chrome highlights, deep soft falloff.','Deep forest-green fluted wall, moody luxury.',
    '85mm at f/5.6. Green marble, mirror chrome. Fine grain, rich deep colour.','text, trophies, people')
add('b22_mags','ss-dropoff',TUBE,'The tube stands upright on its cap on top of a neat stack of five matte magazines lying flat on a light oak café table, front label facing the camera.',
    'The magazines are stacked squarely with their spines facing the camera, each spine a plain solid colour (white, pale pink, lilac, white, cobalt) with absolutely no printed text; a cappuccino cup to one side; the stack centred.',
    'The tube is about 20 cm tall; each magazine is 1 cm thick and 28 cm wide.','Soft bright window light from the left, gentle shadows.','Out-of-focus bright café interior.',
    '70mm at f/5.6. Matte paper, oak, ceramic, matte tube. Fine grain, bright airy colour.','text on spines, magazine titles, readable covers')
add('b22_cloche','ss-network',S('red'),'The product stands upright under a clear glass bell-jar cloche on a white marble pedestal, front label facing the camera.',
    'A tall clear glass cloche covers the product like a precious exhibit; the pedestal stands in a calm gallery with a pale stone wall; the product centred.',
    'The product is 12 cm tall; the cloche is 30 cm tall.','Soft museum spotlight from above, faint reflections on the glass.','Calm pale gallery wall, out of focus.',
    '85mm at f/8. Clear glass, marble, mirror chrome. Fine grain, quiet premium colour.','text, placards, people, artworks')
add('b22_car','ss-shapeshift',S('violet'),'The product stands upright on the cream leather back seat of a luxury car, front label facing the camera.',
    'Night city lights glow as soft bokeh through the car window behind; a camera flash burst gives a paparazzi feel; the product centred.',
    'The product is 12 cm tall.','A bright direct on-camera flash from the front with crisp highlights, warm city bokeh behind.','Out-of-focus night city through the car window.',
    '35mm at f/2.8, flash photography look. Leather, mirror chrome. Fine grain, punchy colour.','people, faces, logos, text')
add('b22_cake','ss-set-vault',VAULT,'The three products stand upright side by side on the top tier of a white ceramic cake stand, front labels facing the camera.',
    'A white tiered cake stand on a pale pink table with a few scattered sugared-almond sweets and one candle-free tiny white cake on the lower tier; festive celebration; centred.',
    'PowerCycle 14 cm, DropOff about 20 cm, ShapeShift 12 cm; the cake stand is 30 cm wide.','Bright soft party light, gentle shadows, crisp chrome highlights.','Seamless pale pink backdrop.',
    '85mm at f/8. Ceramic, sugar, mirror chrome, matte tube. Fine grain, joyful pastel colour.','candles, text, numbers, balloons, confetti')
add('b22_glass','ss-shapeshift',S('violet'),'The product stands upright on a thick floating glass shelf, front label facing the camera.',
    'The shelf is lit from behind by a soft lilac glowing wall panel so the glass edge glows; minimal and futuristic; the product centred.',
    'The product is 12 cm tall; the shelf is 50 cm long and 2 cm thick.','Soft lilac backlight, crisp frontal key light on the chrome.','Glowing pale lilac wall panel.',
    '85mm at f/8. Glass, mirror chrome. Fine grain, cool lilac colour.','text, extra objects')
add('b22_dropper','ss-open-powercycle',"Preserve the exact identity of the product: an open PowerCycle bottle with its lime-green chrome dropper exactly as the element shows it. Use the element for identity only. "+PROP,
    'The open bottle stands upright on a pale stone counter with its dropper resting across the top, front label facing the camera.',
    'A single translucent gel-serum droplet hangs from the dropper tip; a soft sage-green wall behind; calm bathroom morning; the bottle in the LEFT third of the frame, the right half calm empty wall.',
    'The bottle is 14 cm tall.','Soft morning light from the left, the droplet glowing.','Plain soft sage-green wall.',
    '100mm at f/5.6. Stone, glass dropper, mirror chrome. Fine grain, fresh calm colour.','hands, people, text, gold serum, coloured liquid', small=True)
add('b22_ribbon','ss-network',S('red'),'The product stands upright on white marble, front label facing the camera.',
    'Beside it lies a soft pink silk ribbon folded into the classic awareness-ribbon loop; a small vase with a single pale pink peony behind; gentle and hopeful; the product centred.',
    'The product is 12 cm tall; the ribbon loop is 10 cm tall.','Soft warm morning light from the left, gentle shadows.','Out-of-focus bright white bathroom.',
    '85mm at f/5.6. Marble, silk, petals, mirror chrome. Fine grain, soft warm colour.','text, logos, people')
add('b22_pack','ss-shapeshift',S('violet'),'The product stands upright and perfectly centred, front label facing the camera, as a clean studio packshot.',
    'Nothing else in the frame; a soft natural contact shadow on a seamless white floor.','The product is 12 cm tall and fills about 62% of the frame height.',
    'Large soft studio light from the front-left, clean specular highlights on the chrome.','Seamless pure white studio background.',
    '100mm at f/11. Mirror chrome. Crisp clean colour.','props, text, coloured background', small=False)
HUMAN = ("ultra photorealistic, a strikingly beautiful woman in her late 20s with model-like features and realistic skin texture with visible pores, natural minimal makeup, "
         "hair pulled back, wearing a lilac strapless top; shot on a 35mm lens from waist up in a carefully built studio set; ")
x = p('A real high-end beauty campaign photograph featuring ', 'ss-shapeshift', S('violet'),
      'The woman holds the product loosely in one hand near her collarbone with the front label facing the camera, the bottle at its real small size (12 cm), the same distance from the camera as she is.',
      HUMAN + 'With the fingertips of her other hand she gently strokes upward along the side of her neck towards the jawline, eyes softly closed; studio set of a white plaster wall with a soft lilac light wash; she stands in the central 55% of the frame, her head and the product in the band 30%–65% of the frame height; the upper area calm empty wall.',
      'The bottle is 12 cm tall, smaller than her hand.','Soft large beauty key light from the front-left, gentle fill, subtle rim light.','White plaster studio wall washed with soft lilac light.',
      '35mm at f/5.6. Skin, cotton, mirror chrome. Fine grain, natural premium colour.','oversized bottle, bottle close to the camera, plastic skin, heavy retouching, older woman, wrinkles')
J['b22_model_up'] = x
x = p('A real high-end beauty campaign photograph featuring ', 'ss-shapeshift', S('violet'),
      'The product stands upright on a small white plinth beside the woman at the same distance from the camera, front label facing the camera.',
      HUMAN + 'She sits on a white stool looking down at a smartphone in her hand, head tilted forward in a typical tech-neck posture, seen in side profile; studio set with a pale grey-lilac seamless wall; she is placed in the right half of the frame, the left 40% calm empty wall for text.',
      'The bottle is 12 cm tall, about the length of her hand.','Soft large beauty key light from the left, gentle fill.','Pale grey-lilac seamless studio wall.',
      '35mm at f/5.6. Skin, fabric, mirror chrome, phone. Fine grain, calm premium colour.','oversized bottle, text on phone screen, plastic skin, older woman, wrinkles')
J['b22_model_neck'] = x
json.dump(J, open('batch-22.json','w'), ensure_ascii=True)
print(len(J), list(J))
x = copy.deepcopy(J['b22_glp'])
x[2] = x[2].replace('PRODUCT ORIENTATION\n', 'PRODUCT ORIENTATION\nLABELS: on each bottle the black stripe and its white text run VERTICALLY along the bottle exactly as the element shows (words read bottom-to-top), never a horizontal band; the ShapeShift cap is deep saturated violet chrome, the NetWork cap deep red chrome. ', 1)
x[2] = x[2].replace('Negative: ', 'Negative: horizontal label band, horizontal text, pale lavender cap, ')
J['b22_glp_b'] = x
json.dump(J, open('batch-22.json','w'), ensure_ascii=True); print('glp_b')
x = copy.deepcopy(J['b22_car'])
x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\nThe product is photographed from about 1.5 metres away and is only 22% of the frame height; the whole width of the back seat is visible. ', 1)
J['b22_car_b'] = x
json.dump(J, open('batch-22.json','w'), ensure_ascii=True); print('car_b')
x = copy.deepcopy(J['b22_glp_b'])
x[2] = x[2].replace('PRODUCT ORIENTATION\n', 'PRODUCT ORIENTATION\nThe gua sha is a SOLID, opaque, polished rose-quartz stone with crisp edges lying flat on the linen in front of the bottles — never liquid, never a puddle, never translucent jelly. ', 1)
x[2] = x[2].replace('Negative: ', 'Negative: liquid puddle, melted gua sha, translucent gua sha, ')
J['b22_glp_c'] = x
json.dump(J, open('batch-22.json','w'), ensure_ascii=True); print('glp_c')
x = copy.deepcopy(J['b22_model_neck'])
x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\nONE continuous seamless background across the whole frame, no panels, no split, no vertical bands, no wall edges. ', 1)
x[2] = x[2].replace('Negative: ', 'Negative: vertical panels, split background, wall corner, pillarbox, ')
J['b22_model_neck_b'] = x
json.dump(J, open('batch-22.json','w'), ensure_ascii=True); print('neck_b')
x = copy.deepcopy(J['b22_car'])
x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\nWIDE SHOT: the camera is outside the open rear car door, about 2 metres away, showing the entire rear bench seat from door to door; the 12 cm bottle is tiny on the seat, only about 12% of the frame height, a fraction of the height of the seat back. ', 1)
x[2] = x[2].replace('Negative: ', 'Negative: close-up, bottle taller than the armrest, oversized bottle, ')
J['b22_car_c'] = x
x = copy.deepcopy(J['b22_model_neck'])
x[2] = x[2].replace('The product stands upright on a small white plinth beside the woman at the same distance from the camera, front label facing the camera.', 'She holds the 12 cm bottle loosely in her free hand resting on her knee, the bottle smaller than her hand, front label facing the camera; there is no plinth.')
x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\nONE continuous seamless background across the whole frame, no panels or bands. ', 1)
x[2] = x[2].replace('Negative: ', 'Negative: plinth, bottle on a stand, bottle larger than her hand, vertical panels, ')
J['b22_model_neck_c'] = x
json.dump(J, open('batch-22.json','w'), ensure_ascii=True); print('ok')
x = copy.deepcopy(J['b22_model_neck_c'])
x[2] = x[2].replace('wearing a lilac strapless top', 'wearing a soft lilac fine-knit sweater').replace('strapless','')
J['b22_model_neck_d'] = x
x = copy.deepcopy(J['b22_car_c'])
x[2] = x[2].replace('Night city lights glow as soft bokeh through the car window behind; a camera flash burst gives a paparazzi feel', 'Soft daylight city street visible through the car window behind').replace('A bright direct on-camera flash from the front with crisp highlights, warm city bokeh behind.','Soft bright daylight through the windows, crisp chrome highlights.')
J['b22_car_d'] = x
json.dump(J, open('batch-22.json','w'), ensure_ascii=True); print('ok')
x = copy.deepcopy(J['b22_model_neck_d'])
x[2] = x[2].replace('wearing a soft lilac fine-knit sweater', 'wearing a soft lilac fine-knit sweater and matching lilac wide-leg trousers, fully dressed')
x[2] = x[2].replace('She holds the 12 cm bottle loosely in her free hand resting on her knee', 'She holds the slim 12 cm bottle (3.4 times taller than wide) loosely in her free hand at chest height')
x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\nWAIST-UP framing: the image shows her from the waist up only; legs are not visible. ', 1)
x[2] = x[2].replace('Negative: ', 'Negative: bare legs, legs visible, underwear, stubby bottle, ')
J['b22_model_neck_e'] = x
json.dump(J, open('batch-22.json','w'), ensure_ascii=True); print('ok')
add('b22_pc_sage','ss-powercycle',S('lime-green'),'The product stands upright and perfectly vertical on a pale travertine stone ledge, front label facing the camera.',
    'A calm soft sage-green wall behind; one small sprig of rosemary lies on the stone beside the bottle; the bottle stands in the LEFT third of the frame, the right half is calm empty sage wall.',
    'The product is 14 cm tall and 4.5 cm in diameter.','Soft morning window light from the left, gentle shadow, crisp chrome highlights.','Plain soft sage-green wall.',
    '85mm at f/5.6. Travertine, mirror chrome. Fine grain, fresh calm colour.','hands, people, text, droppers, open bottle')
json.dump(J, open('batch-22.json','w'), ensure_ascii=True); print('ok')
x = copy.deepcopy(J['b22_model_neck_e'])
x[2] = x[2].replace('She holds the slim 12 cm bottle (3.4 times taller than wide) loosely in her free hand at chest height', 'Her free hand rests on her knee; the slim 12 cm bottle (3.4 times taller than wide) stands on a small round white side table right next to her, at the same distance from the camera as she is, its top below her elbow height')
x[2] = x[2].replace('WAIST-UP framing: the image shows her from the waist up only; legs are not visible. ', 'Framing from mid-thigh up, she is fully dressed in sweater and trousers. ')
J['b22_model_neck_f'] = x
json.dump(J, open('batch-22.json','w'), ensure_ascii=True); print('ok')
