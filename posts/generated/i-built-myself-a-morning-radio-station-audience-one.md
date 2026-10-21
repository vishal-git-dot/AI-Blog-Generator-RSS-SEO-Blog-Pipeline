---
title: "I built myself a morning radio station (audience: one)"
slug: "i-built-myself-a-morning-radio-station-audience-one"
author: "AMiN"
source: "devto_python"
published: "Wed, 21 Oct 2026 04:02:40 +0000"
description: "At 7am, my phone buzzes. There’s a tall dashboard image in WhatsApp, followed by a voice note. The image shows my top tasks, job pipeline and project status...."
keywords: "voice, chucka, morning, day, one, script, dashboard, whatsapp"
generated: "2026-10-21T04:08:31.252813"
---

# I built myself a morning radio station (audience: one)

## Overview

At 7am, my phone buzzes. There’s a tall dashboard image in WhatsApp, followed by a voice note. The image shows my top tasks, job pipeline and project status. The voice talks me through the same board, starting with a fresh “G’day”. It’s a tiny radio station that broadcasts to an audience of one. I built it for myself, in spare hours, and on 17 October 2026 I open-sourced it as Chucka, also known as MorningDashboard. Why Chucka? In Australia, Chucka is a name shared by several distinct, well-known cockatoos. I liked the distinctly Aussie connection and the cheeky personality it brings to the project. Cockatoos certainly know how to make themselves heard, and my little automation does something similar: it pipes up every morning with a fresh greeting and a rundown of the day ahead. It describes what it does; Chucka gives it a noisy character of its own. You want to see the real one? The idea was simple: I already had the information I needed in Obsidian. I didn’t need another app to check. I wanted that information to find me. A picture and a voice note Every morning at 07:00 AM, Chucka sends two things to my own WhatsApp. First is a dashboard image. Python and Pillow render it directly from the live files in my Obsidian vault. It brings together the day’s top must-dos, my job pipeline and the current state of my projects. Second is a WhatsApp voice-note bubble, roughly 170 words and about 60–70 seconds long. It summarises the same board, with a new greeting each day. The script is written fresh by an LLM each morning; a text-to-speech model turns it into audio that sound natural. The flow is deliberately straightforward. Chucka reads the vault, builds the dashboard and passes the dashboard data into a prompt. The script generator also receives Melbourne weather from wttr.in. The opencode CLI runs the LLM and writes the spoken summary. Audio is rendered, converted to Ogg/Opus with ffmpeg, then sent through a local OpenWA gateway to WhatsApp. A macOS launchd job starts the whole run at 7am. From start to send, a full run takes about two minutes. The voice part The first version had no voice at all. later, I added a spoken summary. The first voice came from macOS say . It did the job, though “morning radio” was perhaps a generous description of the sound. Then came the voice hunt. I set up local voice cloning with VoiceStudio , created voice profiles, auditioned three energy samples and picked a voice profile I named Pepper. I sped it up to about 1.08×, ran a full rehearsal and adjusted the prompt so the script could include inline emotion tags as well. Finding a voice with morning energy was the hardest part. Chucka uses a three-tier voice chain. The primary option is VoiceStudio / OmniVoice running locally on my Mac. If that app is unavailable, it falls back to Gemini TTS in the cloud. If that also fails, macOS say is the last resort. The final option is robotic, but dependable. The boring 80% is reliability Getting audio out of a model is only one part of sending a useful message every morning. The rest is making sure it arrives. Chucka sends through a local OpenWA gateway. I learned that a status of sent means the message has been queued, not necessarily delivered. After catching a silent drop, I changed the runner to wait for a delivered or read confirmation before shutting anything down. “Sent” and “delivered” are not synonyms when you’re relying on a message to start your day. From personal script to open source Open-sourcing it was also a forcing function. A script that only works on my machine can get away with mysterious assumptions. A repository for other people needs clearer setup steps and a cleaner boundary between the code and my own configuration. Making it public pushed me to tidy the edges. Chucka isn’t a product launch or a claim that I’ve solved personal productivity. It’s one person automating information that already exists, and adding a voice and a face to it. The source of truth remains Obsidian; the briefing is just a more convenient way to meet the day. For now, I’ll keep using Chucka daily and refining the voice and its energy. The point was never to build the biggest system. It was to make something small enough to finish, useful enough to keep, and tidy enough to share. Chucka is open source under the MIT licence: https://github.com/aminkh17/Chucka

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aminkh17/i-built-myself-a-morning-radio-station-audience-one-2hij

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
