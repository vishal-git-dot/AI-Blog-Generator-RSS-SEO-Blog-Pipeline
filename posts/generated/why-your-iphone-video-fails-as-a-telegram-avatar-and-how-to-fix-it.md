---
title: "Why Your iPhone Video Fails as a Telegram Avatar (and How to Fix It)"
slug: "why-your-iphone-video-fails-as-a-telegram-avatar-and-how-to-fix-it"
author: "liveavabot"
source: "devto_python"
published: "Sat, 01 Aug 2026 03:04:46 +0000"
description: "The silent failure I tried to set a video as my Telegram profile picture. Recorded a 6-second clip on my iPhone 15, opened Telegram Desktop, hit "Set as vide..."
keywords: "video, telegram, file, msg, ffmpeg, await, pass, encode"
generated: "2026-08-01T03:28:58.769616"
---

# Why Your iPhone Video Fails as a Telegram Avatar (and How to Fix It)

## Overview

The silent failure I tried to set a video as my Telegram profile picture. Recorded a 6-second clip on my iPhone 15, opened Telegram Desktop, hit "Set as video". Progress bar filled. Nothing happened. No error, no warning, just... nothing. My profile still had the old static photo. Turned out the iPhone recorded in HEVC (H.265), and Telegram's video avatar endpoint accepts H.264 only. It doesn't tell you that. It just accepts the upload and drops it on the floor. That's the bug I wanted to fix, and it became @LiveAvaBot . What Telegram actually wants The official spec for video profile pictures isn't documented in one place. I pieced it together from the Bot API docs, the Telegram Desktop source, and trial and error: Codec : H.264, yuv420p pixel format Container : MP4 with faststart Resolution : 800x800, square, cropped from center Duration : up to 10 seconds (longer gets rejected) File size : under 2 MB (soft cap, sometimes 3 MB works) Audio : must be stripped (any audio stream causes silent rejection on some clients) Frame rate : 30 fps max (60 fps works but adds size) Miss any of these and the client silently fails. No 400 response, no toast, nothing. The ffmpeg pipeline The core transform is a two-pass ffmpeg call. First, cropdetect on a sample of the video to find where the actual content is, then a scale+crop+encode pass to produce the square 800x800 output. # Pass 1: detect crop rectangle ffmpeg -ss 0 -t 3 -i input.mov \ -vf "cropdetect=24:16:0" \ -f null - 2>&1 | grep -o "crop=[0-9:]*" | tail -1 # Pass 2: crop + scale + encode ffmpeg -y -i input.mov \ -vf "crop=1080:1080:420:540,scale=800:800,fps=30,format=yuv420p" \ -c :v libx264 -preset veryfast -crf 26 \ -movflags +faststart \ -an -t 10 \ -pix_fmt yuv420p \ output.mp4 The -an strips audio. The format=yuv420p in the filter chain and -pix_fmt yuv420p at the codec level both matter. Some clients care about the container-level pixel format flag, others read from the codec stream. Tuning -crf was the tricky part. At crf=23 (ffmpeg default), a 10-second 800x800 clip often ended up around 3.5 MB, over the Telegram limit. At crf=28 , quality got mushy in low-light scenes. crf=26 with -preset veryfast was the sweet spot for a 2 MB budget. For clips that still bust the size limit, I do a second encode pass with crf=30 and 24 fps as a fallback. That covers about 95% of uploads without going to a full two-pass ABR encode, which would double the CPU cost. Wiring it into aiogram 3 The bot logic is standard aiogram 3. Receive a video, download it, run the pipeline, send back as an input file. Here's the handler: from aiogram import Router , F from aiogram.types import Message , FSInputFile from pathlib import Path import asyncio , tempfile , subprocess router = Router () @router.message ( F . video | F . animation | F . document ) async def handle_video ( msg : Message ): file = msg . video or msg . animation or msg . document if file . file_size and file . file_size > 20 * 1024 * 1024 : await msg . reply ( " File too big. Max 20 MB. " ) return with tempfile . TemporaryDirectory () as tmp : src = Path ( tmp ) / " input " dst = Path ( tmp ) / " output.mp4 " tg_file = await msg . bot . get_file ( file . file_id ) await msg . bot . download_file ( tg_file . file_path , destination = src ) status = await msg . reply ( " Converting... " ) try : await asyncio . to_thread ( run_pipeline , src , dst ) except subprocess . CalledProcessError as e : await status . edit_text ( f " ffmpeg failed: { e . returncode } " ) return await msg . reply_video ( FSInputFile ( dst ), caption = " Ready. Long-press your profile photo, tap Edit, choose Set as Avatar. " , ) await status . delete () asyncio.to_thread is important. ffmpeg is CPU-bound and blocks. Running it in a thread keeps the event loop responsive so other users don't stall behind a single long encode. Packaging it as @liveavabot Deploy target: a small Hetzner box with systemd. Ffmpeg from apt, Python 3.11 in a venv, aiogram 3.4. No Docker, no k8s, one unit file and a token. Currently at 265 users, most from a single Reddit thread on r/Telegram. Conversion rate on video uploads sits around 80%. The 20% that fail are usually 4K HDR clips where the encode busts the size limit even at crf=30 . Still an open TODO. Try it here: https://t.me/LiveAvaBot?start=devto_article_20260801 . Send a video, get a Telegram-ready MP4 back in about 8 seconds for a typical 6-second iPhone clip. Edge cases I hit along the way HDR to SDR : iPhone 15 records in HDR HLG. Telegram doesn't render HDR, colors come out washed. Added zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p to the filter chain. Ugly, but works. Portrait vs landscape : cropdetect picks up letterboxing on portrait video shot in landscape orientation. I bypass it for aspect ratios more square than 1:1.2. GIFs from Twitter : they come in as MP4 with no audio stream already. The -an flag is a no-op there but doesn't hurt. Rotation metadata : MOVs with rotate=90 in metadata need -vf filters applied after auto-rotation. -noautorotate and then a manual transpose filter fixed a batch of clips that were coming out sideways. What's next Better fallback for oversized 4K clips, probably a two-pass ABR encode gated on file size. A /gif mode that outputs animated MP4 stickers. And figuring out why some Android clients still reject the output even though it passes every spec check I know about. Built by me, @LiveAvaBot .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/liveavabot/why-your-iphone-video-fails-as-a-telegram-avatar-and-how-to-fix-it-4lma

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
