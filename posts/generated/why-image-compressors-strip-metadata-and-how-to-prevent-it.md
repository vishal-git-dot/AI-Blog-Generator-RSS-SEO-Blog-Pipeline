---
title: "Why Image Compressors Strip Metadata — and How to Prevent It"
slug: "why-image-compressors-strip-metadata-and-how-to-prevent-it"
author: "GeoImageTagger"
source: "devto_webdev"
published: "Fri, 20 Nov 2026 23:29:59 +0000"
description: "If you have ever run images through a compression pipeline and discovered the EXIF data came out empty, the explanation is usually straightforward: the compr..."
keywords: "metadata, exif, compression, xmp, iptc, data, not, image"
generated: "2026-11-20T23:51:31.229195"
---

# Why Image Compressors Strip Metadata — and How to Prevent It

## Overview

If you have ever run images through a compression pipeline and discovered the EXIF data came out empty, the explanation is usually straightforward: the compressor never handled the metadata in the first place. Image compression operates on pixel data. Metadata — EXIF, IPTC, XMP, GPS coordinates — is stored in structurally separate sections of the file. Whether those sections survive compression is entirely a function of how the tool is built. How Metadata Is Stored (By Format) JPEG JPEG files use marker segments to organize data. The pixel stream starts at the SOS (Start of Scan) marker. Metadata lives in application markers: APP1 ( 0xFFE1 ) — EXIF and XMP payloads APP13 ( 0xFFED ) — IPTC-IIM data APP2 ( 0xFFE2 ) — ICC color profiles Low-level libraries like libjpeg and libjpeg-turbo process only the pixel buffer. They do not automatically parse or carry over APPn markers. To preserve metadata, the developer must explicitly intercept markers during reading (via jpeg_save_markers() ) and reinject them during writing (via jpeg_write_marker() ). Metadata behavior varies by library and configuration. Some image libraries strip metadata by default, while others can preserve it when explicitly configured. For example, Sharp removes metadata by default unless preservation options such as keepMetadata() , keepExif() , or keepXmp() are used. PNG PNG files store metadata in ancillary chunks: tEXt / zTXt / iTXt — text-based metadata (XMP often lives in iTXt ) eXIf — binary EXIF data (added to the PNG specification to match JPEG's EXIF capability) PNG compression itself is lossless — optimizers like OxiPNG reorganize the pixel data more efficiently without changing it. But whether the metadata chunks are preserved depends on the optimizer's implementation. WebP WebP uses a RIFF container with dedicated chunks: EXIF — raw EXIF payload XMP — XML-serialized XMP data (note the trailing space in the FourCC) IPTC is not part of the WebP specification. When converting from JPEG to WebP, EXIF and XMP can be carried over, but IPTC fields have no standard container in WebP. Why Some Compressors Strip Metadata Three common reasons: The compression library does not handle it — if the tool wraps libjpeg without marker handling or uses HTMLCanvasElement.toBlob() without separately preserving and reattaching source metadata, the output file will have no metadata regardless of the input. Deliberate size optimization — some tools strip metadata to save a few kilobytes per file. Format conversion side effects — converting between formats (JPEG → WebP, TIFF → JPEG) can drop metadata fields that the target format does not support. Browser-Side Compression and Metadata Canvas-based workflows operate on decoded pixel data rather than the original file container. Exporting with canvas.toBlob() or canvas.toDataURL() creates a newly encoded image and does not automatically carry over the source file's EXIF, IPTC, or XMP metadata. Applications that need metadata preservation must handle and reattach that metadata separately. Tools that use WebAssembly-based encoders (MozJPEG, libwebp, OxiPNG) can produce better compression results and can handle metadata if the implementation explicitly copies the relevant sections. The GeoImageTagger Image Compressor uses WASM encoders for compression and is designed to preserve supported metadata as a separate step, including post-compression verification. A Verification Workflow If metadata preservation matters for your pipeline, add a verification step: Before compression — inspect the original file's metadata. The Metadata Viewer shows EXIF, IPTC, XMP, and GPS fields for any supported image. After compression — re-inspect the output file. Compare key fields: GPS coordinates, copyright, creator, camera data. If fields are missing — use a metadata editor to restore them, or switch to a compressor that preserves metadata. The Metadata Editor handles writing EXIF, IPTC, and XMP fields. For programmatic workflows, exiftool can copy metadata between files: exiftool -TagsFromFile original.jpg compressed.jpg Preserve vs. Remove: Know Your Use Case Metadata preservation is not always the right choice. Personal photos shared publicly may contain GPS coordinates and device information. For privacy-sensitive images, deliberately removing metadata is the correct approach. The EXIF Remover handles selective removal without re-encoding pixels. Key Takeaways Image compression operates on pixels; metadata survival depends on the tool JPEG metadata lives in APP1 / APP13 markers — easily preserved if the tool handles them PNG metadata lives in ancillary chunks — lossless compression should not affect them, but verify WebP supports EXIF and XMP but not IPTC Canvas-based export does not automatically preserve source EXIF/IPTC/XMP metadata WASM-based compressors can preserve metadata if designed to Always verify metadata after compression for critical workflows For the full guide, see How to Compress Images Without Losing EXIF, GPS, IPTC or XMP Metadata .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/geoimagetagger/why-image-compressors-strip-metadata-and-how-to-prevent-it-34no

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
