---
title: "Add "Export as image" to any dashboard"
slug: "add-export-as-image-to-any-dashboard"
author: "Accreditly"
source: "devto_webdev"
published: "Thu, 23 Jul 2026 14:00:00 +0000"
description: "First published on the Accreditly blog . "Export as image" is one of those features users expect and developers keep putting off. Someone wants to drop a cha..."
keywords: "panel, export, image, api, render, const, await, url"
generated: "2026-07-23T14:15:19.714391"
---

# Add "Export as image" to any dashboard

## Overview

First published on the Accreditly blog . "Export as image" is one of those features users expect and developers keep putting off. Someone wants to drop a chart into a slide deck or paste a KPI panel into Slack, and right now they screenshot it themselves and crop it badly. Adding a proper export button is less work than it looks, as long as you do not try to rasterise the DOM in the browser. The reliable approach is to render the panel server-side through an image API and hand back a clean PNG. This article adds an export button to a dashboard and wires up the backend that produces the image. Why not just screenshot the DOM in the browser Client-side approaches like html2canvas re-implement a browser's rendering inside the browser, and they break on the things dashboards are made of: web fonts, cross-origin images, SVG charts, CSS you did not write yourself. The output rarely matches what is on screen. Rendering server-side in a real browser engine sidesteps all of it. You send the markup or a URL, a genuine Chromium renders it, and you get a pixel-accurate PNG. Here we use the HTML to Image API from a small Node backend. There are two ways in. If the panel can be rebuilt from data, render a standalone HTML version of it on the server. If the dashboard page is reachable by the API, point it at the URL and capture just the panel with a CSS selector. We will do the first, then show the second. Step 1: The export button On the front end, an export button calls your backend, receives the image bytes, and triggers a download. No canvas, no rendering library. async function exportPanel ( panelId ) { const res = await fetch ( `/api/export/ ${ panelId } ` , { method : ' POST ' }); if ( ! res . ok ) { alert ( ' Export failed ' ); return ; } const blob = await res . blob (); const link = document . createElement ( ' a ' ); link . href = URL . createObjectURL ( blob ); link . download = ` ${ panelId } .png` ; link . click (); URL . revokeObjectURL ( link . href ); } document . querySelectorAll ( ' [data-export] ' ). forEach (( button ) => { button . addEventListener ( ' click ' , () => exportPanel ( button . dataset . export )); }); Any element with data-export="revenue" becomes an export trigger. The browser's only job is to ask for the file and save it. Step 2: Render the panel on the server The backend rebuilds the panel as a self-contained HTML document from the same data the dashboard uses, posts it to the render endpoint, and streams the PNG back. Inlining the styles keeps the render independent of your app's CSS bundle. import express from ' express ' ; const app = express (); function panelHtml ( panel ) { return ` <div style="width:1000px;padding:48px;font-family:Arial,sans-serif;background:#fff;"> <h2 style="margin:0 0 8px;font-size:28px;"> ${ panel . title } </h2> <p style="margin:0 0 24px;color:#6b7280;"> ${ panel . subtitle } </p> <div style="font-size:72px;font-weight:bold;color:#4f46e5;"> ${ panel . value } </div> </div>` ; } app . post ( ' /api/export/:id ' , async ( req , res ) => { const panel = await loadPanel ( req . params . id ); // your data layer const render = await fetch ( ' https://app.html2img.com/api/html ' , { method : ' POST ' , headers : { ' Content-Type ' : ' application/json ' , ' X-API-Key ' : process . env . HTML2IMG_API_KEY , }, body : JSON . stringify ({ html : panelHtml ( panel ), width : 1000 , height : 600 }), }); const { url } = await render . json (); const image = Buffer . from ( await ( await fetch ( url )). arrayBuffer ()); res . set ( ' Content-Type ' , ' image/png ' ); res . send ( image ); }); Because the server holds the data, the export is deterministic. The same panel produces the same image whether the user is on a phone or a 4K monitor, which is not true of a browser screenshot. Step 3: Capturing a live panel by selector If your dashboard is reachable by the API, for example a public status board or a page behind a signed URL, you can skip rebuilding the HTML and capture the real element instead. Point the screenshot endpoint at the page and pass a CSS selector for the panel you want. The API waits for that element, then crops the image to its bounds. app . post ( ' /api/export-live/:id ' , async ( req , res ) => { const render = await fetch ( ' https://app.html2img.com/api/screenshot ' , { method : ' POST ' , headers : { ' Content-Type ' : ' application/json ' , ' X-API-Key ' : process . env . HTML2IMG_API_KEY , }, body : JSON . stringify ({ url : `https://dashboard.example.com/board?token= ${ process . env . BOARD_TOKEN } ` , selector : `#panel- ${ req . params . id } ` , }), }); const { url } = await render . json (); const image = Buffer . from ( await ( await fetch ( url )). arrayBuffer ()); res . set ( ' Content-Type ' , ' image/png ' ). send ( image ); }); The selector approach is the quickest when the rendered panel already looks right and you just need it as a file. The rebuild approach gives you more control, since the export can differ from the on-screen version, add a title block, or strip interactive chrome that makes no sense in a static image. Polishing it A couple of touches make this feel finished. Show a brief loading state on the button while the request is in flight, because a render takes a second or two. And cache the generated image keyed by the panel and its last-updated time, so exporting the same unchanged panel twice does not render twice. That is a complete export feature: a button on the front end, a backend route that renders the panel in a real browser, and a clean PNG that matches what the user sees. Your users stop cropping screenshots, and "export this" becomes a one-click answer instead of a backlog item.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/accreditly/add-export-as-image-to-any-dashboard-g1a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
