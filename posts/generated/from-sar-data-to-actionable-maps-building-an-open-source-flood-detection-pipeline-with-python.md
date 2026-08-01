---
title: "🌊 From SAR Data to Actionable Maps: Building an Open-Source Flood Detection Pipeline with Python"
slug: "from-sar-data-to-actionable-maps-building-an-open-source-flood-detection-pipeline-with-python"
author: "Aditya Singh"
source: "devto_python"
published: "Sat, 01 Aug 2026 07:20:38 +0000"
description: "Optical satellites are useless during floods because, well, it’s cloudy. Sentinel-1 SAR sees through rain and night, but its data is noisy, complex, and full..."
keywords: "qgis, data, water, sar, flood, permanent, transparent, maps"
generated: "2026-08-01T08:27:56.503122"
---

# 🌊 From SAR Data to Actionable Maps: Building an Open-Source Flood Detection Pipeline with Python

## Overview

Optical satellites are useless during floods because, well, it’s cloudy. Sentinel-1 SAR sees through rain and night, but its data is noisy, complex, and full of "permanent water" that isn't actually flooding. I built an end-to-end pipeline to turn raw SNAP GeoTIFFs into clean, actionable flood maps. Here’s how I solved the three biggest headaches in SAR processing. 1. The "Padding" Trap SNAP exports often include zero-value borders. If you don’t crop these, your histogram gets skewed by millions of 0 s, breaking automatic thresholding. The Fix: Treat 0.0 as NaN , convert to dB, and crop strictly to the valid data footprint before any analysis. # Crop to valid data only rows = np . where ( ~ np . all ( np . isnan ( dB_full ), axis = 1 ))[ 0 ] cols = np . where ( ~ np . all ( np . isnan ( dB_full ), axis = 0 ))[ 0 ] dB = dB_full [ rows . min (): rows . max () + 1 , cols . min (): cols . max () + 1 ] 2. Isolating New Floodwater A simple -17 dB threshold detects all water. To find actual flood damage, you must subtract permanent rivers and lakes. The Fix: I used OSMnx to fetch permanent water bodies from OpenStreetMap, rasterized them to match the SAR grid, and subtracted them from the detected mask. # Fetch permanent water from OSM osm_water = ox . features_from_bbox ( bbox = bbox , tags = { " natural " : " water " }) # Subtract from detected mask flood_only = mask_clean & ( ~ binary_dilation ( permanent_water , iterations = 2 )) 3. The QGIS "Black Background" Bug Exporting transparent GeoTIFFs is a nightmare. QGIS often renders "transparent" pixels as solid black if you rely on standard Alpha channels. The Fix: Instead of RGBA, I use a single-band raster with a dedicated NoData value (255). QGIS treats NoData as transparent automatically. # 1 = flooded, 255 = NoData (Transparent in QGIS) overlay = np . where ( final_flood_raster == 1 , 1 , 255 ). astype ( np . uint8 ) The Result The pipeline outputs: Vector Data: GeoJSON/Shapefiles with accurate area calculations (in km²). Interactive Maps: A Folium HTML map with Satellite/Street toggles. QGIS-Ready Rasters: Clean overlays that work immediately upon import. 🚀 Try It Out The full notebook is open-source. It handles everything from speckle cleanup to final visualization. 🔗 [ https://github.com/Adityas221b/QGIS-Flood ] Python #GeoAI #RemoteSensing #OpenSource #ClimateTech

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/adityahunt/from-sar-data-to-actionable-maps-building-an-open-source-flood-detection-pipeline-with-python-2idf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
