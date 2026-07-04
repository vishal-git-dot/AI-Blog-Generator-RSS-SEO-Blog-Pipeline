---
title: "I added Charts to FrameUI 1.0.0"
slug: "i-added-charts-to-frameui-100"
author: "Julian"
source: "devto_webdev"
published: "Sat, 04 Jul 2026 13:26:51 +0000"
description: "FrameUI now has charts. That is the main thing I wanted to add with the new release. FrameUI started as an Angular component library beta. The early goal was..."
keywords: "charts, frame, chart, month, desktop, mobile, frameui, data"
generated: "2026-07-04T13:45:59.770957"
---

# I added Charts to FrameUI 1.0.0

## Overview

FrameUI now has charts. That is the main thing I wanted to add with the new release. FrameUI started as an Angular component library beta. The early goal was simple: build reusable Angular UI primitives with clear APIs, CSS variables, and documentation that shows real usage. This release also marks the first stable 1.0.0 line, but the version number is not the main story for me. The main story is that FrameUI can now cover more of the application interfaces it was designed for. The new charts package @frame-ui-ng/charts is a standalone Angular package for FrameUI chart primitives. npm install @frame-ui-ng/foundation @frame-ui-ng/charts Import the chart styles once: @import '@frame-ui-ng/charts/styles.css' ; Import the module: import { FrChartModule } from ' @frame-ui-ng/charts ' ; Then use frame-chart : <frame-chart aria-label= "Traffic by device" type= "area" xKey= "month" [data]= "trafficData" [series]= "trafficSeries" /> The first chart release includes: area charts bar charts composed charts ...and more It also includes grouped and stacked bars, horizontal bars, multiple curve modes, composed series, legends, tooltips, value formatting, custom colors, empty states, and chart click events. Why I added charts FrameUI is focused on application UI. Those interfaces often need data visualization next to the usual primitives: tables filters cards forms navigation overlays feedback components The chart use cases I had in mind were things like: dashboard panels admin screens reports operational tools KPI cards internal applications I wanted a chart package that fits into the same visual language instead of feeling like a separate charting product embedded into the page. A simple example Data: trafficData = [ { month : ' Jan ' , desktop : 186 , mobile : 80 }, { month : ' Feb ' , desktop : 305 , mobile : 200 }, { month : ' Mar ' , desktop : 237 , mobile : 120 }, { month : ' Apr ' , desktop : 273 , mobile : 190 }, { month : ' May ' , desktop : 209 , mobile : 130 }, { month : ' Jun ' , desktop : 314 , mobile : 260 }, ]; trafficSeries = [ { key : ' desktop ' , label : ' Desktop ' }, { key : ' mobile ' , label : ' Mobile ' }, ]; Template: <frame-chart aria-label= "Traffic by device" type= "area" xKey= "month" [data]= "trafficData" [series]= "trafficSeries" /> Why charts are separate Charts are useful, but not every application needs them. I did not want the main component package to grow just because some users need data visualization. So charts live in their own package: @frame-ui-ng/foundation for shared tokens, styles, and providers @frame-ui-ng/components for UI primitives @frame-ui-ng/charts for data visualization primitives The chart package still uses the same visual direction and token system, but users can install it only when needed. Links Docs: https://frame-ui.com GitHub: https://github.com/Gamekohl/frame-ui Feedback I am still looking for practical Angular feedback. Especially: Does the chart API feel natural in Angular templates? Is the data and series model easy to understand? Are the current chart types useful? Would you expect more customization first, or more chart types first? The earlier feedback changed the direction of FrameUI quite a lot. I am hoping the 1.0.0 release can get the same kind of practical criticism.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gamekohl/i-added-charts-to-frameui-100-d92

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
