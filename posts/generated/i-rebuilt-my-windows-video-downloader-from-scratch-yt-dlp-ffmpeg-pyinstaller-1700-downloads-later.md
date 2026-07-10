---
title: "I rebuilt my Windows video downloader from scratch — yt-dlp + FFmpeg + PyInstaller, 1,700 downloads later"
slug: "i-rebuilt-my-windows-video-downloader-from-scratch-yt-dlp-ffmpeg-pyinstaller-1700-downloads-later"
author: "Rebell Yell"
source: "devto_python"
published: "Fri, 10 Jul 2026 19:01:14 +0000"
description: "Three months ago I posted here about Grabbit, a desktop video downloader I built for Windows. The app has grown a lot since then — new engine, local file con..."
keywords: "dlp, ffmpeg, pyinstaller, video, grabbit, new, what, you"
generated: "2026-07-10T19:40:31.689245"
---

# I rebuilt my Windows video downloader from scratch — yt-dlp + FFmpeg + PyInstaller, 1,700 downloads later

## Overview

Three months ago I posted here about Grabbit, a desktop video downloader I built for Windows. The app has grown a lot since then — new engine, local file converter, batch mode, transcript extraction — so I wanted to write a proper update with the actual technical details. What Grabbit does (2026 edition) Grabbit is a Windows 10/11 desktop app that downloads videos from 8+ platforms — YouTube, TikTok, Instagram, Facebook, Twitter/X, Pinterest, Twitch, SoundCloud — up to 4K quality. Everything runs locally. No cloud, no account required, no file upload anywhere. It also ships with a local FFmpeg converter (Pro) that converts between video and image formats entirely on your machine. Supported downloads: YouTube to MP3 , TikTok , Instagram Reels , Pinterest , YouTube Shorts , SoundCloud , and more. Supported conversions: Video → MP3 , WebM → MP4 , HEIC → JPG , WebP → JPG , Video → ProRes HQ , Video → DNxHR HQ . The stack (unchanged from v1, for a reason) Backend: Python + Flask + yt-dlp + FFmpeg Frontend: Vanilla JS (no framework) Auth/DB: Supabase (PostgreSQL + Edge Functions) Payments: Stripe → Supabase Edge Function → Resend Installer: PyInstaller + Inno Setup Distribution: GitHub Releases (auto-update via version check) I kept the same stack because it works. The temptation to rewrite in Electron or Tauri was real but I resisted it. Adding complexity wouldn't have shipped any of the features below. What's new: the FFmpeg Converter The biggest addition since April is the local Converter. Users can drop a local file (MP4, MKV, AVI, MOV, WebM, HEIC, WebP) and convert it to another format — entirely on their machine. No upload, no size limit. The trickiest part: bundling FFmpeg and pillow-heif with PyInstaller . For FFmpeg I use imageio-ffmpeg which ships its own binary: import imageio_ffmpeg ffmpeg_path = imageio_ffmpeg . get_ffmpeg_exe () This gives you a reliable path whether you're running from source or from a frozen PyInstaller bundle. No which ffmpeg nonsense, no PATH issues on Windows. For HEIC support ( pillow-heif ), PyInstaller doesn't collect the native DLLs automatically. You need to force it in the .spec file: # grabbit.spec from PyInstaller.utils.hooks import collect_all datas_heif , binaries_heif , hiddenimports_heif = collect_all ( ' pillow_heif ' ) Without that, HEIC conversion silently fails at runtime on the packaged exe — no error, just nothing happens. Took an embarrassing amount of time to debug. What's new: Batch mode Pro users can paste up to 50 URLs at once — one per line — and Grabbit queues them all. The implementation is straightforward but the UX took iteration: users need to know which URLs failed and why, without it feeling like a wall of errors. I ended up with a per-URL status row that shows queued → downloading → done/error in real time. The progress streaming still holds — polling every 600ms against a lightweight endpoint works well enough that I haven't needed WebSockets. What's new: Transcript mode Grabbit can extract transcripts from YouTube videos — useful for summarizing, repurposing content, or accessibility. It uses yt-dlp's subtitle extraction under the hood: ydl_opts = { ' writesubtitles ' : True , ' writeautomaticsub ' : True , ' subtitleslangs ' : [ ' en ' ], ' skip_download ' : True , } Auto-generated captions aren't perfect but for most YouTube content they're good enough for summarization use cases. What's new: self-updating yt-dlp yt-dlp breaks constantly as platforms change their APIs. Rather than shipping a new app version every time, Grabbit updates yt-dlp silently in the background on launch: import subprocess , sys def update_ytdlp (): subprocess . run ( [ sys . executable , ' -m ' , ' pip ' , ' install ' , ' --upgrade ' , ' yt-dlp ' ], capture_output = True ) When frozen with PyInstaller, sys.executable points to the bundled Python — so pip updates the bundled yt-dlp, not a system one. This means users always have a working downloader even when a platform changes something overnight. Numbers after 3 months 1,700+ installs via GitHub Releases Top countries: Mexico, US, Peru, Spain, Argentina, Colombia Top traffic sources: Direct, Google Organic, ChatGPT referral Free plan: 10 single downloads, 1 batch (up to 10 links), 2 transcripts Pro: $8.99/month or $59.99/year — unlimited downloads, batch up to 50, all converter formats The LATAM tilt was unexpected but makes sense in hindsight — there's a real gap for a clean Spanish-language download tool. I shipped 19 new SEO landing pages in Spanish last week targeting that. What I'd do differently Ship the Chrome Extension earlier. The extension puts a one-click Grab button directly on video pages while you're watching. It's one of the highest-retention features and I waited too long to build it. Don't fight PyInstaller — embrace the spec file. I spent weeks trying to make things work without touching the .spec . The right answer is always: open the spec, add what you need, move on. Ignore the "just use Electron" advice. Flask + Vanilla JS served from localhost is genuinely fine for a tool like this. The bundle is smaller, startup is faster, and I understand every line of it. If you're building something similar — local desktop tool, Python backend, freemium model — happy to answer questions in the comments. If you want to try it: appgrabbit.com — Windows only, free plan available, no account required.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/indignity/i-rebuilt-my-windows-video-downloader-from-scratch-yt-dlp-ffmpeg-pyinstaller-1700-downloads-1f0l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
