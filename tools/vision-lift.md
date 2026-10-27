# Vision subject cut-out (macOS)

Cuts the foreground subject (product, skeleton, cage…) out of a photo with Apple Vision `VNGenerateForegroundInstanceMaskRequest`. Used 2026-10-25 for the "BOO." behind-the-subject layout (S_0596 skeleton, S_0214 cage).

- Binary + source: `~/sickscience-work/tools/lift` (`lift.swift`)
- Run: `~/sickscience-work/tools/lift in.jpg mask.png`, then `im.putalpha(mask)` in PIL to get the cut-out PNG.
- In Figma: Photo rect, then the text layer, then a Cutout rect on top with the cut-out PNG at the same geometry, so the text sits behind the subject.
- Build: `swiftc -O lift.swift -o lift`. Each import needs its own line.

```swift
import Vision
import AppKit
import CoreImage
let a = CommandLine.arguments
let url = URL(fileURLWithPath: a[1])
let ci = CIImage(contentsOf: url)!
let h = VNImageRequestHandler(ciImage: ci)
let r = VNGenerateForegroundInstanceMaskRequest()
try! h.perform([r])
let obs = r.results!.first!
print("instances", obs.allInstances.count)
let mask = try! obs.generateScaledMaskForImage(forInstances: obs.allInstances, from: h)
let m = CIImage(cvPixelBuffer: mask)
let ctx = CIContext()
let cg = ctx.createCGImage(m, from: m.extent)!
let rep = NSBitmapImageRep(cgImage: cg)
try! rep.representation(using: NSBitmapImageRep.FileType.png, properties: [:])!.write(to: URL(fileURLWithPath: a[2]))
```
