---
title: "Build a three-expression robot face with HTML and JavaScript"
slug: "build-a-three-expression-robot-face-with-html-and-javascript"
author: "Daniel Postle"
source: "devto_webdev"
published: "Wed, 14 Oct 2026 21:17:30 +0000"
description: "A robot character does not need a complicated animation system to show a little personality. Start with three still expressions and let a button switch betwe..."
keywords: "face, button, expression, html, three, robot, smile, png"
generated: "2026-10-14T21:28:09.487065"
---

# Build a three-expression robot face with HTML and JavaScript

## Overview

A robot character does not need a complicated animation system to show a little personality. Start with three still expressions and let a button switch between them. This small browser prototype helps you see whether the artwork fits your project before you spend time on a larger interface or physical display. This tutorial uses the free Mint sample from Xemory Systems : Smile, Wink and Joy, supplied as three editable SVGs and three transparent 512 × 256 PNGs. The sample download also contains its README and license. 1. Put the three PNGs beside your HTML file Download and extract the free sample. Copy smile-mint.png , wink-mint.png and joy-mint.png into a folder. In the same folder, create a plain-text file named index.html . Keep the exact filenames; the example looks for those files beside the page. 2. Paste this complete example <!doctype html> <html lang= "en" > <meta charset= "utf-8" > <meta name= "viewport" content= "width=device-width, initial-scale=1" > <title> Three-expression robot face </title> <style> body { margin : 0 ; background : #111827 ; color : #fff ; font : 18px system-ui ; text-align : center ; padding : 2rem ; } img { display : block ; width : min ( 100% , 512px ); height : auto ; margin : 1rem auto ; } button { padding : .75rem 1rem ; margin : .25rem ; font : inherit ; cursor : pointer ; } button :focus-visible { outline : 3px solid #6ee7b7 ; } </style> <h1> Give your robot an expression </h1> <img id= "face" src= "smile-mint.png" width= "512" height= "256" alt= "Robot face: smile" > <div> <button type= "button" data-face= "smile" > Smile </button> <button type= "button" data-face= "wink" > Wink </button> <button type= "button" data-face= "joy" > Joy </button> </div> <p id= "status" aria-live= "polite" > Expression: smile </p> <script> const face = document . querySelector ( ' #face ' ); const status = document . querySelector ( ' #status ' ); document . querySelectorAll ( ' [data-face] ' ). forEach ( button => { button . addEventListener ( ' click ' , () => { const expression = button . dataset . face ; face . src = expression + ' -mint.png ' ; face . alt = ' Robot face: ' + expression ; status . textContent = ' Expression: ' + expression ; }); }); </script> </html> 3. Open it and try the buttons Save the file, then open index.html in a current desktop browser with JavaScript enabled. This example uses ordinary relative image paths: no API key, external JavaScript library or server request is needed for the expression switch. If an image is missing, check that the PNG is beside the HTML file and that the spelling and extension match. If the page displays the code as text, make sure the filename ends in .html , not .html.txt . What the prototype demonstrates The JavaScript changes the image filename and its descriptive text. It does not animate the artwork or control hardware. The real buttons also work with keyboard focus and Enter or Space, while the status line announces the selected expression to assistive technology. Once the layout feels right, you can connect the same expression choices to events in your own app. For a physical display, you still need the appropriate display driver, image conversion and hardware code. This browser example is a visual starting point. More expressions or a custom visual idea? The free sample can be used or modified in personal or commercial finished projects under its included license. Standalone asset resale or redistribution is not allowed. Artwork and tutorial production are AI-assisted. The optional full DIY Robot Face Pack costs US$1.99 and provides 12 expressions in three palettes, SVG/PNG artwork, monochrome PBM assets, a C header, a PDF guide and a browser motion preview. Artwork files are still images; hardware and firmware are not included. For an idea that needs different artwork, graphics, tutorial slides or presentation visuals, you can send Xemory Systems a custom creative request . Scope and deliverables are agreed before production and payment.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/xemorysystems/build-a-three-expression-robot-face-with-html-and-javascript-4e1p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
