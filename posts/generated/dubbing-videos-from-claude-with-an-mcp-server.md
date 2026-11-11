---
title: "Dubbing videos from Claude with an MCP server"
slug: "dubbing-videos-from-claude-with-an-mcp-server"
author: "Donatas Adomavičius"
source: "devto_ai"
published: "Wed, 11 Nov 2026 13:47:26 +0000"
description: "I'm building Vocnu . It translates videos into other languages with an AI voice-over and subtitles. There's a web app and a Chrome extension for YouTube and ..."
keywords: "vocnu, you, claude, mcp, voice, subtitles, npx, videos"
generated: "2026-11-11T13:54:26.914881"
---

# Dubbing videos from Claude with an MCP server

## Overview

I'm building Vocnu . It translates videos into other languages with an AI voice-over and subtitles. There's a web app and a Chrome extension for YouTube and course sites, and there's also an MCP server. This post is about that one: how to set it up and what happens when you ask Claude to dub a file. Setup You need Node 20 or newer, a Vocnu account (new accounts get 40 free credits, no card) and an API token from the app under Settings → API & MCP. The MCP server ships in the vocnu npm package, the same one as the CLI, so there's nothing extra to install. Claude Code: claude mcp add vocnu -e VOCNU_TOKEN = vocnu_... -- npx -y vocnu mcp Claude Desktop ( claude_desktop_config.json ), Cursor or any other MCP client: { "mcpServers" : { "vocnu" : { "command" : "npx" , "args" : [ "-y" , "vocnu" , "mcp" ] , "env" : { "VOCNU_TOKEN" : "vocnu_..." } } } } Using it After that you just ask something like: Dub ~/Videos/talk.mp4 into Spanish with Vocnu Claude uploads the file with vocnu_upload_media (up to 10 GB, uploading is free). It gets back the length, your balance and the price for each output and quality grade. The start tool asks it to confirm the price with you first, so nothing gets spent until you say ok or pick a cheaper grade. Then vocnu_start_job does the actual work: speech recognition, translation, a voice reading the translation where people talk, and the mix. The original audio is turned down, not removed, so music and background sounds stay. If you want it louder, quieter or off, just say so. vocnu_job_status shows progress and time left. When it's done, vocnu_download_results saves the files next to the original, or vocnu_share_job gives you a link that opens in a browser without an account. If a job fails or you cancel it ( vocnu_cancel_job ), the credits come back. A few details You can get the full video (MP4, MKV, MOV, WebM or AVI), only the voice-over audio, or only subtitles. Subtitles come with every output and can be burned in. There are SDH subtitles too, with sounds, speaker names and songs, for deaf and hard-of-hearing viewers. vocnu_voices lists the voices for a language with a short sample of each. So "use a calmer female voice" works, and Claude picks an actual voice id instead of guessing. Premium is the default. Standard and Economy are cheaper, with simpler voices and translation. For a lecture you only want to understand they're fine. If nobody talks in the video and the story is in on-screen captions, Vocnu reads the captions out instead. Without Claude npx vocnu login npx vocnu translate talk.mp4 --to es Same thing: it uploads, shows the price, asks before starting and saves the results next to the file. npx vocnu help has the rest ( --voice , --output , --burn-subtitles , --sdh and so on). Where MCP really helps is batches. "Dub the three newest videos in this folder into German and Polish and give me share links" is one message, Claude does the rest, and because of the price check it can't spend credits you didn't agree to. Docs are at vocnu.com/developers , the package is vocnu on npm . If you try it, let me know which languages or voices sound off.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/donatas_adomavicius/dubbing-videos-from-claude-with-an-mcp-server-2636

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
