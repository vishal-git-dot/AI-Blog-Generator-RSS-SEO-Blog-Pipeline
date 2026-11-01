---
title: "I Built a 170-Year Caribbean Hurricane Observatory, Alone, in Python"
slug: "i-built-a-170-year-caribbean-hurricane-observatory-alone-in-python"
author: "Dim's Build"
source: "devto_python"
published: "Sun, 01 Nov 2026 05:04:58 +0000"
description: "TL;DR CaribScope is an open-source climate risk observatory for the Caribbean: 170 years of Atlantic hurricane tracks (NOAA HURDAT2, 1851–2022), live USGS ea..."
keywords: "storm, hurricane, what, caribbean, data, live, category, more"
generated: "2026-11-01T05:26:23.412973"
---

# I Built a 170-Year Caribbean Hurricane Observatory, Alone, in Python

## Overview

TL;DR CaribScope is an open-source climate risk observatory for the Caribbean: 170 years of Atlantic hurricane tracks (NOAA HURDAT2, 1851–2022), live USGS earthquake data, sea surface temperature trends, and a Random Forest model that predicts a storm's Saffir-Simpson category. It's a 16-page Streamlit app, built solo, running on a single VPS. It's also, by my own admission, more finished as a product than as a project anyone has heard of — which is the part of this post that isn't a victory lap. The gap During hurricane season, the National Hurricane Center and NOAA publish everything you'd want: forecasts, historical tracks, advisories. All of it in English, built for a US audience. French-speaking Caribbean media, creators, and residents get none of that tailored to them — no French-language dashboard, no historical context localized to Guadeloupe, Martinique, or Haiti, nothing that says "here's what a storm like this one has historically done in your part of the Caribbean." That gap is what CaribScope tries to close. 170 years is a lot of inconsistent data HURDAT2 is NOAA's official Atlantic hurricane database, going back to 1851. The format is a flat text file, not a clean CSV: header lines mixed with position/wind/pressure records, missing pressure values before the satellite era (pre-1979 mostly relies on ship and land station reports), and storm identifiers that changed convention more than once across 170 years. There's no off-the-shelf pandas reader for this — parsing it means writing a state machine that tracks whether the current line is a storm header or a data row, and being honest with yourself about which columns are trustworthy back to 1851 and which only become reliable once aircraft reconnaissance and satellites show up mid-20th century. The payoff for going back that far isn't just the feat itself. It's context: when a Category 3 approaches, "the last comparable storm hit this island in 1928" is a more useful sentence than "here's a live radar loop," especially for an audience that already has access to the radar loop. What's actually in it Trajectories & stats — every HURDAT2 storm, filterable by island, category, decade Seismic map — live USGS feed, magnitude ≥ 2.5, Caribbean plate boundary Climate trends — temperature and sea surface temperature (SST) over time ML prediction — a Random Forest classifier (scikit-learn) trained on the HURDAT2 history, predicting Saffir-Simpson category from a storm's current attributes Hurricane of the Day — a daily-format page pulling from the historical archive, built to be the shareable/embeddable unit for media and social 16 Streamlit pages in total, each independently a small app. Streamlit's multi-page routing (a pages/ folder, each file a page) made that structure nearly free — the cost shows up later, in navigation and information architecture, not in the initial build. The stack Python 3.10+, Streamlit for the app itself, Plotly for every chart and map, pandas / numpy / pyarrow for the data layer, scikit-learn for the Random Forest, pytest for tests. Shipped as a Docker image ( python:3.12-slim ) behind Coolify on a personal VPS, with GitHub Actions running CI and Renovate keeping dependencies current — the same self-hosted infrastructure I already run Listmonk on, so adding one more container was marginal cost, not a new operational surface. The Random Forest, and its actual limits The prediction model takes a storm's current attributes and outputs a predicted Saffir-Simpson category, trained on the historical HURDAT2 record. I want to be specific about what that is and isn't: it's a classifier trained on a few thousand historical storm-observations, not a physics-based forecast model, and it will never compete with NOAA's own operational forecasts, which fold in atmospheric modeling this project has no access to. What it's useful for is pattern-matching against history — showing, from data, what tends to happen next to storms that looked like this one before. That's a narrower and more honest claim than "hurricane prediction," and it's the one I'm making. What doesn't work yet The product is ahead of its distribution, not the other way around, and I'd rather say that upfront than have someone else point it out. Sixteen pages, a working ML pipeline, live earthquake and climate data — and until recently, no analytics installed, no email capture, no one outside a small circle who knew it existed. Building the thing was the easy part. The next phase is entirely about getting it in front of the people it's actually for: French-speaking Caribbean media and creators during the exact six months a year they'd want it. Try it Live app: caribscope.fwicss.fr Source: github.com/FWICSS/caribscope It's open source. If you've got a dataset that would sharpen the risk picture for a specific island, or you've dealt with HURDAT2's pre-satellite-era gaps before and have opinions, I'd like to hear them.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dimsbuild/i-built-a-170-year-caribbean-hurricane-observatory-alone-in-python-1gkh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
