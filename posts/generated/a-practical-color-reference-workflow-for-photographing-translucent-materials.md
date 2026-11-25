---
title: "A Practical Color-Reference Workflow for Photographing Translucent Materials"
slug: "a-practical-color-reference-workflow-for-photographing-translucent-materials"
author: "Ryan Harvey"
source: "devto_python"
published: "Wed, 25 Nov 2026 21:20:56 +0000"
description: "Photographing translucent materials is a calibration problem before it is a photography problem. Two shots of the same stone, taken ten minutes apart under t..."
keywords: "not, same, two, step, img, material, card, float"
generated: "2026-11-25T21:26:57.088749"
---

# A Practical Color-Reference Workflow for Photographing Translucent Materials

## Overview

Photographing translucent materials is a calibration problem before it is a photography problem. Two shots of the same stone, taken ten minutes apart under the same lamp, can look like two different materials once the camera decides on a white balance. I ran into this while helping document jadeite pieces for a small trading archive, and the fix turned out to be mostly code, not gear. The problem A camera's auto white balance optimises for a pleasant average, not for consistency. With a strongly coloured subject filling the frame, the camera compensates for the colour it sees and neutralises exactly the signal you want to measure. Dark green material on a light background pulls the exposure one way; the same material on dark velvet pulls it the other. Step 1: fix the light, then stop trusting the camera I settled on a single diffused source at a fixed distance, a matte grey card in the corner of every frame, and manual exposure. The grey card is not decoration: it is the anchor the script uses to normalise every image to the same reference point. Step 2: sample the card, not the subject from PIL import Image import numpy as np def grey_reference ( path , box ) : img = Image . open ( path ) . convert ( "RGB" ) patch = np . asarray ( img . crop ( box ) ) . reshape ( - 1 , 3 ) . astype ( float ) # median is robust against dust and specular highlights return np . median ( patch , axis = 0 ) The crop box is fixed once and reused for the whole series, so every frame gets the same treatment. Median instead of mean matters: a stray highlight on the card will drag a mean badly and leave a colour cast that no later step can undo. Step 3: apply a per-channel gain def balance ( img , ref , target = ( 200 , 200 , 200 ) ) : arr = np . asarray ( img ) . astype ( float ) gain = np . array ( target , dtype = float ) / np . maximum ( ref , 1.0 ) out = np . clip ( arr * gain , 0 , 255 ) . astype ( np . uint8 ) return Image . fromarray ( out ) Two lines and the whole series lands on a common neutral. I keep the gain values in a CSV next to the images; when a new lamp or a new diffuser shows up, the drift is visible as a step change in that column instead of being buried in the pictures. Step 4: describe the material in numbers, not adjectives Once the frames are comparable, a short feature extractor makes the archive searchable. For translucent material the useful features are narrow: mean hue in the subject mask, saturation spread, and a crude translucency proxy built from the ratio of edge brightness to centre brightness. def translucency_proxy ( img , mask ) : arr = np . asarray ( img . convert ( "L" ) ) . astype ( float ) edge = arr [ mask & ~ erode ( mask ) ] core = arr [ erode ( erode ( mask ) ) ] return float ( np . mean ( edge ) / max ( np . mean ( core ) , 1.0 ) ) This is not a grading system and it does not pretend to be one. It is a way to sort two hundred photographs into groups that a human can then look at side by side, which is the only part of the job that actually needs eyes. What I would do differently Put the grey card in the frame before the first shot, not after the fortieth. Store the raw gain values in the filename. EXIF rewriting is a rabbit hole. Resist the urge to make the numbers look nice. A feature that separates your groups but has no physical meaning will not survive a change of lighting. If you only take one thing from this: the difference between two photos of the same piece is usually a measurement error, and measurement errors are cheaper to fix in code than in a studio. The reference archive this workflow was built for lives at https://www.jjjadeite.com , and a shorter buyer-facing write-up of the same ideas is at https://sites.google.com/view/jadeite-buyer-guide — both were useful to me as examples of how the same material is described for two very different audiences.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jadeitenotes/a-practical-color-reference-workflow-for-photographing-translucent-materials-1n31

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
