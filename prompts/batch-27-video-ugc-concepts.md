# Batch 27 — human UGC video concepts (2026-10-08)

The user asked for videos with people in them (refs: Spoiled Child, Grüns, IM8; Superscale trending + Meta Ad Library, US, active, video, sorted by impressions).

## What the references do

| Brand | Ad | Structure | Takeaway for SickScience |
|---|---|---|---|
| Spoiled Child | "2026 Collagen of the Year" (8 s) | Split screen: celebrity UGC (sipping) on the left, static product panel on the right with "Try before you buy". | Split screen: a person on one side, the product and offer on the other. Cheap, readable without sound. |
| Spoiled Child | Becca testimonial (54 s) | Body hook, then "all eyes on you", sample try, unboxing, how-it-works B-roll with ✔ checks, talking-head testimonial, end card. | Same skeleton as the user's "TRY BEFORE YOU BUY" reference. |
| Spoiled Child | Celebrity montage (59 s) | Ten celebrity clips with name tags. | Not usable: no celebrities. |
| Grüns | "Do not buy Grüns anywhere ❌ except their website" (20 s) | Warehouse POV with gloved hands packing orders; offer text appears line by line; box closes. | Hands-only POV avoids face and anatomy risk. Not usable as is: SickScience also sells at Ulta, so the "not anywhere else" line would be false. Use the packing POV for the free-trial offer instead. |
| Grüns | Performer kitchen chat (24 s) | Candid behind-the-scenes conversation, then a green offer end card. | Candid, unpolished tone; end card carries the offer. |
| IM8 | Selfie talking head (45 s) | Lo-fi bedroom selfie, hand gestures, holding the product. | Simplest human format: one person, one take. |
| IM8 | GLP-1 animated characters (98 s) | Pixar-style ingredient characters. | Not human; skip. |

## Test video (one Higgsfield try): "I paid $0 for this" (DropOff free trial)

Offer copy is verbatim from sicksciencelabs.com/products/dropoff:
- "Try DropOff free for 21 days"
- "Pay shipping only. $0 for the product today."
- "Try it for 21 days. Use it morning and night."
- "Love it or return it. Free returns if it's not for you."

**Format.** 9:16, about 12–15 s, IM8-style selfie UGC:

| Time | Shot | On-screen text (added in post) |
|---|---|---|
| 0–4 s | A woman in her late 20s, selfie angle, in a bright bathroom. She holds the DropOff tube up beside her face, raises her eyebrows and smiles. | **I paid $0 for this.** |
| 4–9 s | She smooths a gel-serum ribbon onto the back of her upper arm. She has exactly two arms: one hand applies, the other arm is bent. | ✔ Pay shipping only · ✔ Try it 21 days · ✔ Love it or return it |
| 9–12 s | End card: the real DropOff PNG on a cobalt backdrop, composed in post (not generated). | **Try DropOff free for 21 days** |

**Rules applied:**
- No results claims spoken by the AI person; the offer only.
- No body before/after (Meta risk).
- Gel-serum texture rule applies.
- The product is redrawn by the video model; if the tube breaks, the end card uses the real PNG.
- No AI-generated speech claiming to be a real customer. Text overlays carry the message, so the clip works muted.

**Pipeline:**
1. Generate a start frame with nano banana and the DropOff element, 9:16.
2. Higgsfield image-to-video, one generation.
3. Add text overlays and the end card in post (Founders Grotesk), and check the safe zones.
