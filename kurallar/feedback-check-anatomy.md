---
name: feedback-check-anatomy
description: "Before delivering any model image, count arms/hands/fingers — AI images with hand-applied product often add a third arm"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-08T13:51:42.779Z
---

Every model image gets an explicit anatomy check before it goes into Figma: count arms, hands and fingers, and trace each hand back to a shoulder. Poses where one hand applies product to the other arm while also holding a product are the main risk; prompts must state "exactly TWO arms and TWO hands" and describe which hand does what.

**Why:** User 2026-10-08 (angry): "kadının 3 kolu var kontrol ettiğin hali bu mu?" — DropOff model image (one hand rubbing the arm + another hand holding the tube) shipped with three arms.

**How to apply:** Add the anatomy sentence + negatives ("three arms, extra hand") to every model prompt; reject on any extra limb. Related: [[feedback-models-in-30s]], [[feedback-vary-product-placement]]

**Hand orientation too (user 2026-10-08: "kızın eli ters duruyo"):** counting arms is not enough. For each hand check that the forearm comes from its own shoulder side (not out of the chest), the wrist is not twisted, and the thumb is on the correct side for a left/right hand that is palm-up or palm-down. Zoom into each hand at full resolution before delivery. Safest pose: one visible hand, palm up beside the cheek, arm rising from the same side, other arm out of frame (u26_ss2). Avoid "one hand on head + palm-up hand", which produced a reversed hand (u26_pc5).
