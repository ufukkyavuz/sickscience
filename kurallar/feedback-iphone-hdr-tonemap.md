---
name: feedback-iphone-hdr-tonemap
description: iPhone HDR (HLG/BT.2020 + Dolby Vision 8.4) footage — keep the original colour natively (HEVC 10-bit HLG out WITH the DV RPU), never tone-map/convert; replace delivered files in place
metadata:
  type: feedback
---

User, 2026-11-05 (after two failed attempts with an avconvert SDR proxy and an Apple AVAssetReader SDR proxy): "Değiştirme renkleri. Direkt orijinal dosyada renk neyse onu kullan. Çevirim yapmaya uğraşma… olan videoyu değiştir, sürekli yeni video atıp durma."

**Why:** any HDR→SDR conversion (avconvert, AVAssetReader, plain ffmpeg decode as BT.709) visibly changes the colours against the original as the user sees it on the phone or Mac. The user judges by eye against the original, not by numbers.

**How to apply:**
- ffprobe the client's phone video for color_transfer. `arib-std-b67` (HLG) or `smpte2084` (PQ) means HDR.
- For HDR, cut straight from the original in 10-bit YUV with no RGB step: hflip/scale/setpts/trim, concat, overlay text as an RGBA pipe (`overlay=format=yuv420p10`). Encode libx265 yuv420p10le with `-tag:v hvc1`, colorprim bt2020, transfer arib-std-b67, colormatrix bt2020nc (x265-params plus ffmpeg tags). Copy the audio. Script: `~/sickscience-work/video-projects/merve-grwm-1103/render_native.py`.
- **Keep the Dolby Vision RPU** (iPhone = DV profile 8.4 on HLG). Without it macOS tone-maps the HLG punchier and more saturated, and the user sees 'patlak renkler' (2026-11-05: QuickTime capture brightness 135→142 and saturation 75.8→77.6 after only stripping DV). Add libx265 `-dolbyvision 1 -strict unofficial` plus x265 `vbv-maxrate=60000:vbv-bufsize=120000` (DV needs VBV). Check that every frame has 'Dolby Vision RPU' side data.
- Final check: open the original and the edit in QuickTime at the same moment, app_screenshot both, and compare mean RGB/saturation outside the text area.
- Verify by comparing the Y/U/V plane means with the source frame at the same moment. They should match within about 2 levels.
- Revisions overwrite the delivered file under the SAME name. No v2 or sibling files in the delivery folder.
- A graded copy ("– renk ayarlı") only when the user asks for one.

Related: [[feedback-video-studio-gates]], [[feedback-delivery-folders]], [[project-polen-personal-social]]

**2026-11-10:**
- The "yellow" Beauty Connect reel (polen-1030 `render7`) went through an RGB pipe and lost the HLG tags, so players misread the colours.
- Fixed with `render7_native.py`: segments cut from the HLG originals, the text as an RGBA overlay (Vision masks for the words behind her), x265 10-bit with HLG tags.
- WhatsApp SDR sources go through the same no-RGB path (`batch-123/render_native.py`, `overlay=format=yuv420`, bt709 tags).
- Check: the U/V plane means match the source within 0.1.
