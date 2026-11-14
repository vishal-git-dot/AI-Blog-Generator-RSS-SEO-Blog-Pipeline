---
title: "Your Image Compression Made the File 2.5x Bigger: 5 Numbers From One 6016px Photo"
slug: "your-image-compression-made-the-file-25x-bigger-5-numbers-from-one-6016px-photo"
author: "zhihu wu"
source: "devto_webdev"
published: "Sat, 14 Nov 2026 13:05:11 +0000"
description: "I spent an afternoon pushing one photo through a compression pipeline at every setting it has. These are file sizes from a single source image on a single ma..."
keywords: "quality, file, you, image, one, size, compression, photo"
generated: "2026-11-14T13:16:27.352445"
---

# Your Image Compression Made the File 2.5x Bigger: 5 Numbers From One 6016px Photo

## Overview

I spent an afternoon pushing one photo through a compression pipeline at every setting it has. These are file sizes from a single source image on a single machine — no benchmarks, just bytes, because "quality 80" tells you nothing until you know what it does to the file. Source: one 6,016 x 6,016 JPEG, 4.80 MB, already encoded around quality 80. Output File size quality 30 0.62 MB quality 60 1.88 MB quality 80 4.80 MB quality 90 5.46 MB quality 100 12.09 MB resized to 1200px wide 0.07 MB same image saved as PNG 30.57 MB 1. Above ~85, quality is a size knob, not a sharpness knob Quality 90 cost 14% more bytes than 80. Quality 100 cost 152% more — 12.09 MB for one image. You will not see that difference at 100% zoom on a laptop screen. You will see it in your bandwidth bill and in Largest Contentful Paint. 2. Re-compressing an already-compressed JPEG saves nothing Quality 80 in, quality 80 out: 4.798 MB versus 4.800 MB. The source had already discarded exactly what quality 80 discards, so there was nothing left to remove. If your upload pipeline re-encodes at the quality the file arrived with, it is a no-op that costs a generation of quality. 3. Raising the quality later inflates the file without bringing detail back Re-encoding the quality-60 output at quality 80 gave 2.66 MB (+41%). At quality 100 it gave 7.13 MB (+278%). Both files are still quality-60 images — blurrier than the 1.88 MB they started as, and bigger than many originals. Lossy compression is a ratchet: decide once, at the largest resolution you will ever need, and keep that file as the source. 4. Dimensions beat quality by an order of magnitude Resizing to 1200px wide produced 68.8 KB — roughly 70 times smaller than quality 80 at full size. No quality slider gets you there. Resize first, then compress; the reverse order just throws away work. 5. PNG is a format decision, not a compression setting The same photo as PNG: 30.57 MB, 6.4x the JPEG. PNG earns its size on flat colors, screenshots and transparency. For photographs it is the wrong container no matter where the slider sits. The cost that never shows up in the file size 6,016 x 6,016 x 4 bytes of RGBA is 144.8 MB just to have that image decoded in a browser tab. That is why client-side compressors stall or die on camera-original photos: decoding is the expensive step, not encoding, and looping over ten of them is how you run a mobile browser out of memory. Process one at a time, and downscale before anything else touches the pixels. I reproduce these numbers locally, but when I just need a resize-and-recompress without uploading a client's photo to a stranger's server, I use this browser-based image compressor — it runs on canvas, so the file never leaves the machine, and it strips EXIF (GPS included) on re-encode. That last part is a privacy win but also a real change: bake the orientation in before you strip the metadata, or sideways photos stay sideways.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/zhihu_wu_dea1d82af01a04d7/your-image-compression-made-the-file-25x-bigger-5-numbers-from-one-6016px-photo-1mgg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
