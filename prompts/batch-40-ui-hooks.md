# Batch 40 — "Interacting with the UI" hook videos (2026-10-11)

Reference: katrina_pahomova reel DeR13pfRvtx (14 s; 25.5K likes, 33.7K comments).
- She physically plays with on-screen Instagram UI: burns a question sticker with a lighter, pulls a notification down and grabs it, crumples a card and throws it.
- The reference ended with a comment CTA. That is NOT used here (user, 2026-10-11): the end points to the product like earlier videos — stat slam, logo, SickScienceLabs.com.

Production:
- Start stills: Higgsfield web UI, Nano Banana Pro, 9:16, 2K, Unlimited.
- Motion: Kling 3.0 (credits), one clip per video.
- UI cards and the burn/crumple effects are added in our own render (render40.py), never drawn by the model, so the text is exact.
- Each video is ≤15 s. Copy is verbatim from the PDPs.

| Video | Product | UI hook | Proof (PDP) |
|---|---|---|---|
| v1 | ShapeShift | Question sticker "Is jawline serum a scam?" burned with a lighter | 92% saw a more sculpted jawline |
| v2 | NetWork | Notification "Your NetWork order has shipped" pulled down and grabbed | October: 20% of NetWork sales on SickScienceLabs.com go to BCRF |
| v3 | PowerCycle | Comment card "my ponytail used to be twice this thick" crumpled and thrown | +29% average increase in hair thickness |

## Shared still prompt (sections), product block swapped per video
```
A real editorial campaign photograph featuring {EL}. — Preserve the exact identity of the product exactly as the element shows it: {ID} Use the element for identity only; never redraw it. Exactly one product, closed. Every word printed on the product is pure white on the black stripe; never black or grey text. — PRODUCT ORIENTATION — A strikingly beautiful woman in her late 20s with model-like features and realistic skin with natural texture stands at waist height behind a sculptural white stone basin in a studio-built bathroom set. {POSE} Exactly two arms and two hands. The product is at the same distance from the camera as the model. — COMPOSITION AND FRAMING — Vertical 9:16, 35mm lens, waist up, wide. Her head and the product sit together in the band from 40% to 65% of the frame height; she is in the central 55% of the width; the top 38% of the frame is calm white plaster wall (space for a UI card later). — SCALE — {SIZE} An adult hand is about 18 cm long. If in doubt make the product smaller, never bigger. — LIGHT AND SHADOW — Large soft campaign key light from the front-left, gentle fill, soft natural shadows. — BACKGROUND — A studio bathroom set: smooth white limewash plaster wall, sculptural white stone basin, two or three curated objects (a folded linen towel, a small ceramic vase), clearly a built set. — PHOTOGRAPHIC FINISH — 35mm f/4, real skin pores, soft knit top in off-white, polished chrome, high-key premium campaign. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. All product text perfectly legible, sharp and accurate. — INTEGRATION — The product is lit like her hand, with real reflections of the room in the chrome and real finger contact; no outline or halo. — Negative: extra arms, extra fingers, product bigger than her hand, product close to the camera, stubby capsule, black letters on the product, open bottle, text, logos, ordinary home, flat seamless backdrop, plastic skin, heavy retouch, CGI, watermark.
```

## Poses
- **v1:** "In her left hand she holds the ShapeShift capsule upright beside her jaw at face depth, label to camera. Her right hand is raised to shoulder height, holding a slim matte black lighter upright, thumb on the wheel, unlit; she looks up toward the empty wall above it with a playful, sceptical half-smile."
- **v2:** "In her left hand she holds the NetWork capsule upright at chest height, label to camera. Her right arm is raised high, the hand open and reaching up toward the top edge of the frame, as if about to grab something above her; she looks up at it, amused."
- **v3:** "Her long, very thick, glossy dark-brown hair is in a full high ponytail brought forward over her right shoulder. In her left hand she holds the PowerCycle capsule upright at chest height, label to camera. In her right hand she holds a small plain white card (about 9 × 6 cm) in front of her chest, reading it with a sceptical raised eyebrow."

## Kling motion (≈5 s each, from the still)
- **v1:** "She flicks the lighter; a small real flame appears and she raises it slowly up toward the empty wall above her hand, holding it there for a moment, then lowers the lighter, looks into the camera with a confident smile and lifts the capsule slightly. The capsule stays still and unchanged in her left hand. Static camera."
- **v2:** "She closes her raised hand in the air above her head as if catching something, pulls the closed fist down quickly to her chest next to the capsule, opens it, looks at her palm, then smiles at the camera. The capsule stays still and unchanged in her left hand. Static camera."
- **v3:** "She crumples the white card into a small ball in her right hand and tosses it out of the frame to the right, then runs that hand slowly down her thick ponytail, looking into the camera with a satisfied smile. The capsule stays still and unchanged in her left hand. Static camera."

## Sonuç (2026-10-12)
Kullanıcı üç videoyu da beğenmedi ve Teslim klasöründen sildi. Bu UI-hook konsepti (soru kutusu yakma / bildirim yakalama / yorum buruşturma) tekrar önerilmez.
