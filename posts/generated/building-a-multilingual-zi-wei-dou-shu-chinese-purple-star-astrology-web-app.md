---
title: "Building a multilingual Zi Wei Dou Shu (Chinese Purple Star Astrology) web app"
slug: "building-a-multilingual-zi-wei-dou-shu-chinese-purple-star-astrology-web-app"
author: "Xian XX"
source: "devto_webdev"
published: "Sat, 12 Sep 2026 10:04:32 +0000"
description: "A few months ago I started building a small web app around Zi Wei Dou Shu (紫微斗数), a traditional Chinese astrology system. It ended up being a fun full-stack ..."
keywords: "chart, time, chinese, app, not, multilingual, wei, dou"
generated: "2026-09-12T10:25:42.908765"
---

# Building a multilingual Zi Wei Dou Shu (Chinese Purple Star Astrology) web app

## Overview

A few months ago I started building a small web app around Zi Wei Dou Shu (紫微斗数), a traditional Chinese astrology system. It ended up being a fun full-stack project, so here's a build log with the decisions that mattered. What the app does You enter a birth date, time and place. The app renders a natal chart with the 12 Palaces (life areas like career, wealth, spouse) and the 14 Major Stars , then generates a short AI-written reading explaining the chart in plain language. Free chart, optional paid readings. Interesting technical bits 1. True solar time is not optional. Chinese chart calculation depends on the actual solar time at the birth location, not the administrative timezone. China alone spans five theoretical time zones while officially using UTC+8, so two people born at the same clock time in different cities can have different charts. We do city-level longitude correction, with a fallback to the timezone mean when data is missing. 2. Multilingual output is harder than multilingual UI. Translating the interface into English / Simplified & Traditional Chinese / Japanese / Korean / Vietnamese was the easy part (standard i18n catalogs). The hard part is star and palace terminology: many terms have no accepted translation in some languages, so we keep pinyin with a localized gloss on first use. Calendars are another trap — the lunar-to-solar conversion tables differ between schools. 3. Charts are SVG, not canvas. The palace grid has to resize from mobile to desktop and remain readable for 14 stars plus dozens of minor stars. SVG with CSS variables for the theming system (light/dark, two skin families) worked better than canvas, and keeps the chart accessible. 4. AI readings need structure. Free-form prompts produced generic horoscope-speak. The reading quality improved a lot when we generated a structured chart summary first and let the model explain that, instead of asking it to interpret raw inputs. 5. Cloudflare Workers for the edge. The whole thing runs on Workers with an i18n-aware routing layer; the map is mostly static which keeps TTFB low across regions. Try it If you're curious what your chart looks like: https://zi-wei-dou-shu.com/en — free chart with a short AI introduction, six languages. Feedback welcome, especially from anyone who has dealt with lunar calendar edge cases. Standard caveat: this is a cultural/entertainment product, not fortune telling with guarantees.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/xxxian886/building-a-multilingual-zi-wei-dou-shu-chinese-purple-star-astrology-web-app-28n8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
