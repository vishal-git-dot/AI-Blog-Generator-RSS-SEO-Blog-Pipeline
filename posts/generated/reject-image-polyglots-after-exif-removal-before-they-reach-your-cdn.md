---
title: "Reject Image Polyglots After EXIF Removal, Before They Reach Your CDN"
slug: "reject-image-polyglots-after-exif-removal-before-they-reach-your-cdn"
author: "jaryn"
source: "devto_webdev"
published: "Mon, 20 Jul 2026 03:18:35 +0000"
description: "Removing EXIF GPS protects one privacy boundary. It does not prove that an uploaded JPEG contains only a JPEG. A useful hostile fixture is a valid image foll..."
keywords: "jpeg, jpg, exif, bytes, decoded, assert, image, only"
generated: "2026-07-20T03:39:19.784287"
---

# Reject Image Polyglots After EXIF Removal, Before They Reach Your CDN

## Overview

Removing EXIF GPS protects one privacy boundary. It does not prove that an uploaded JPEG contains only a JPEG. A useful hostile fixture is a valid image followed by bytes for another format. Many decoders stop at JPEG’s end marker and display the picture successfully, while downstream scanners, content sniffers, or accidental downloads may interpret the trailing payload differently. Build a fixture set rather than trusting extensions: clean.jpg valid JPEG exif-gps.jpg valid JPEG with location jpeg-plus-zip.jpg JPEG followed by ZIP bytes jpeg-plus-html.jpg JPEG followed by HTML truncated.jpg missing end marker oversized-dimensions.jpg small file, dangerous decode cost My upload gate has independent layers: Store the original in a non-public quarantine location. Enforce byte-size and decoded-dimension limits. Decode with a maintained image library. Re-encode pixels into a new file, discarding metadata and trailing bytes. Verify the output’s signature, dimensions, and complete parse. Publish only the derived object under a server-generated name. A boundary check can detect bytes after the end marker, but re-encoding is the stronger transformation because it creates a new representation from decoded pixels. Keep the original inaccessible and delete it according to a tested lifecycle. assert ( outputSize <= limit ); assert ( decoded . width * decoded . height <= pixelBudget ); assert ( parseConsumesEntireFile ( output )); assert ( noLocationMetadata ( output )); The OWASP File Upload Cheat Sheet recommends defense in depth: allowlisted types, generated filenames, size limits, storage separation, and content validation. No single MIME header or metadata scrubber replaces that chain. The important privacy lesson is broader than EXIF: inspect every representation that survives the upload pipeline, and publish only a constrained derivative.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jaryn_123/reject-image-polyglots-after-exif-removal-before-they-reach-your-cdn-4hi4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
