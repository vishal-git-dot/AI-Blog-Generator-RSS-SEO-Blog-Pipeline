---
title: "Move your Vapi assistants to a self-hosted server with no platform fee"
slug: "move-your-vapi-assistants-to-a-self-hosted-server-with-no-platform-fee"
author: "Alan"
source: "devto_webdev"
published: "Tue, 10 Nov 2026 01:15:34 +0000"
description: "Hosted voice-agent platforms add a per-minute fee on top of what you pay your speech-to-text, model, voice and phone providers. OpenRing is an open-source (M..."
keywords: "your, you, voice, vapi, what, openring, move, hosted"
generated: "2026-11-10T01:21:53.737932"
---

# Move your Vapi assistants to a self-hosted server with no platform fee

## Overview

Hosted voice-agent platforms add a per-minute fee on top of what you pay your speech-to-text, model, voice and phone providers. OpenRing is an open-source (MIT) alternative that runs on your own machine and speaks Vapi's API, so you can move an account in a few minutes. 1. Start it You need Node.js 18 or later. Everything else, Python included, installs itself: npx openring The dashboard opens at http://localhost:8000 . Choose a password, then connect providers on the Providers page (a speech-to-text key and a model key; Groq's free tier and Deepgram's credit for new accounts are enough to start). 2. Import your account Copy every assistant, squad, tool and Twilio number in one request (the key is used once and never stored): curl -X POST http://localhost:8000/import \ -H "Authorization: Bearer $OPENRING_API_KEY" -H "Content-Type: application/json" \ -d '{"baseUrl": "https://api.vapi.ai", "apiKey": "YOUR_PRIVATE_KEY"}' The answer lists each assistant with anything that keeps it from taking calls yet, for example a provider OpenRing doesn't support. Importing again updates what came in before. 3. Test from the browser Open an assistant and press Test . Talk into your microphone, no phone number needed. Each call records its transcript, the latency of every turn and the cost per provider. 4. Point your client at it Change your client's base URL to your server and send the same JSON. For phone numbers, set each number's voice webhook to $PUBLIC_URL/twilio/voice (you need a public https address; a tunnel works for testing). What to know before you move Only Twilio has taken real calls so far. Telnyx, Plivo, Vonage and SIP trunks are beta, tested on simulated carriers. Calls have Vapi's default limits: 10 minutes, and 30 seconds of silence. You run the server, its uptime and any compliance work. Hosted platforms take on the first two. A fully local, free stack (Whisper, Ollama, Kokoro) is possible, but a voice on a laptop CPU is slow. If you try it, tell me what breaks: https://github.com/elifalanrocha/openring/issues/16

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/elifalanrocha/move-your-vapi-assistants-to-a-self-hosted-server-with-no-platform-fee-3ho6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
