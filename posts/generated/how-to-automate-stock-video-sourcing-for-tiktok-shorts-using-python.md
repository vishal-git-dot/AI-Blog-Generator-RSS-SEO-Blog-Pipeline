---
title: "How to Automate Stock Video Sourcing for TikTok & Shorts Using Python"
slug: "how-to-automate-stock-video-sourcing-for-tiktok-shorts-using-python"
author: "Machine4321"
source: "devto_python"
published: "Sun, 28 Jun 2026 19:24:59 +0000"
description: "How to Automate Stock Video Sourcing for TikTok & Shorts Using Python Faceless channels on TikTok, YouTube Shorts, and Instagram Reels are booming. Many crea..."
keywords: "your, video, videos, apify, download, vertical, pexels, scraper"
generated: "2026-06-28T19:38:17.335838"
---

# How to Automate Stock Video Sourcing for TikTok & Shorts Using Python

## Overview

How to Automate Stock Video Sourcing for TikTok & Shorts Using Python Faceless channels on TikTok, YouTube Shorts, and Instagram Reels are booming. Many creators are automating their entire workflow—using AI to write scripts, generate voiceovers, and edit videos. But one major bottleneck remains: sourcing high-quality background stock videos. Manually browsing site after site, searching for relevant clips, downloading them, and organizing them into folders is incredibly tedious. In this tutorial, we will show you how to automate this process completely. You will learn how to write a Python script that bulk-downloads vertical (portrait) stock videos from Pexels based on any search keyword, ready to be fed into your video editing pipeline. 🛠️ The Solution: Apify Pexels Scraper Instead of struggling with the rate limits of the native Pexels API or parsing heavy HTML pages yourself, we will use the Pexels Video & Image Bulk Scraper on Apify . This Actor allows us to: Search for any keyword (e.g. "lofi", "meditation", "gym"). Filter results specifically by Orientation (e.g., portrait for vertical social formats). Filter by Size (e.g., HD/4K) and Locale (language). Download raw MP4 files directly to our local machine. 📥 Setup Instructions 1. Install the Apify Client SDK First, install the official Apify Client package via pip: pip install apify-client 2. Get Your API Token Sign up for a free account at apify.com and copy your API Token from your Integrations tab in the console. Set it in your terminal environment: macOS/Linux : export APIFY_TOKEN="your_token_here" Windows (PowerShell) : $env:APIFY_TOKEN="your_token_here" 🚀 The Python Implementation Create a file named download_stock_videos.py and paste the following code: import os import requests from apify_client import ApifyClient def download_file ( url , file_path ): """ Helper to download and save raw video file locally. """ print ( f " Downloading: { url } " ) response = requests . get ( url , stream = True ) if response . status_code == 200 : with open ( file_path , ' wb ' ) as f : for chunk in response . iter_content ( chunk_size = 1024 * 1024 ): if chunk : f . write ( chunk ) print ( f " ✅ Saved to: { file_path } " ) else : print ( f " ❌ Failed to download { url } " ) def main (): token = os . getenv ( " APIFY_TOKEN " ) if not token : print ( " Please set your APIFY_TOKEN environment variable. " ) return client = ApifyClient ( token ) # Scraper Input Configuration run_input = { " query " : " minimalist aesthetic " , # Search keyword " mediaType " : " videos " , # We only want video clips " orientation " : " portrait " , # Filter vertical videos for TikTok/Shorts " size " : " large " , # HD / 4K resolution " maxResults " : 5 # Number of clips to download } print ( f " Starting Pexels Scraper on Apify for query: ' { run_input [ ' query ' ] } ' ... " ) # Run the Actor and wait for completion run = client . actor ( " knobby_wallpaper/pexels-scraper " ). call ( run_input = run_input ) # Retrieve dataset items dataset_items = client . dataset ( run [ " defaultDatasetId " ]). list_items (). items print ( f " Found { len ( dataset_items ) } vertical video structures. " ) # Create folder to save videos output_dir = " stock_videos " os . makedirs ( output_dir , exist_ok = True ) # Download raw MP4 videos locally for idx , item in enumerate ( dataset_items ): video_url = item . get ( " rawUrl " ) or item . get ( " videoUrl " ) if not video_url : continue file_name = f " video_ { idx + 1 } _ { item . get ( ' id ' ) } .mp4 " file_path = os . path . join ( output_dir , file_name ) # Download the file download_file ( video_url , file_path ) if __name__ == " __main__ " : main () 📈 Going No-Code? If you prefer to download vertical stock videos directly in your web browser without writing Python scripts, you can run the scraper via the web UI: 👉 Run Pexels Scraper on Apify Store Simply enter your search keyword, select Portrait (Vertical) as the orientation, click Start , and download your vertical background clips immediately! Do you automate video generation? What's your setup? Let me know in the comments!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/machine4321/how-to-automate-stock-video-sourcing-for-tiktok-shorts-using-python-4eln

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
