---
name: feedback-product-integration-not-pasted
description: "Products must look photographed in the scene, not pasted in; every Higgsfield prompt carries an INTEGRATION section + composite-look negatives"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-11-01T11:04:56.235Z
---

User, 2026-10-04: "ürün çok photoshopla koyulmuş gibi duruyo çoğu karede bunu da düzeltelim". Products in generated scenes looked composited: studio-clean chrome, different light than the room, no contact shadow, sharper than surroundings.

**Why:** a pasted-looking product kills realism and reads as a cheap ad.

**How to apply:**
- Every photographic prompt gets an INTEGRATION paragraph after PHOTOGRAPHIC FINISH:
  - same light direction, softness and colour temperature as the scene;
  - chrome reflects the real surroundings, not studio reflections;
  - real contact shadow and a faint surface reflection;
  - same focus, grain and noise as the rest of the photo; no outline or halo.
- Add the matching negatives: pasted/composited look, cut-out edges, sticker look, halo, product lit differently, floating product.
- Avoid pixel-pasting the clean element PNG into scenes, except to fix tiny unreadable labels.
- Template: prompts/batch-13-build.py.

**Placement and floor (user, 2026-11-01, batch-85e: "ürün sağda kalmış ve sonradan eklenmiş gibi" · "zeminin kesildiğini görmeyelim, zemin bize doğru devam etsin, premium hissiyatı arttırıyor"):**
- Never park the product alone at the side of the frame or in front of the subject. Put it in the action: held by the figure, between the split object, under the hand that touches the surface.
- Never write "the product alone gets a frontal fill". That line made it look pasted. It stands in the same light as the subject.
- Surfaces are a seamless sweep running out of the bottom of the frame toward the camera: no table edge, corner, leg, plinth or horizontal line. Contact shadow falls toward the camera, with a faint reflection. Or use no surface at all when the figure holds the product.
- In the same batch the user deleted a fully front-lit version of the silhouettes, so backlit figures stay dark with only a weak fill.
- A hand-held capsule goes soft and grey: rebuild the real white letters on the chrome; never paste a band (there is no stripe, see [[feedback-no-black-stripe-on-capsule]]).

Related: [[feedback-photographic-prompt-format]], [[feedback-product-text-white-and-network-spelling]].

**2026-11-10 (user, angry, "kaç kere söyledim"):** NO cut pedestals / plinths / blocks and NO floors that end inside the frame — the ground must continue seamlessly to the frame edges. Also: an award visual must SAY "we won" in the image itself (e.g. the product with a real award object/plaque, celebration), not just a pretty product shot with a seal pasted on top ("ödül almışız, ne bu fotoğrafın amacı?").
