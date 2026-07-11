---
title: "My Abandoned Cricket Kit Confronted Me. So I Built It a Voice"
slug: "my-abandoned-cricket-kit-confronted-me-so-i-built-it-a-voice"
author: "Himanshu Kumar"
source: "devto_ai"
published: "Sat, 11 Jul 2026 03:10:15 +0000"
description: "This is a submission for the DEV Weekend Challenge: Passion Edition . What I Built Everyone will tell you about the passions they have. Nobody talks about th..."
keywords: "you, what, passion, every, voice, persona, snowflake, abandoned"
generated: "2026-07-11T03:17:17.852857"
---

# My Abandoned Cricket Kit Confronted Me. So I Built It a Voice

## Overview

This is a submission for the DEV Weekend Challenge: Passion Edition . What I Built Everyone will tell you about the passions they have. Nobody talks about the ones they quit. I played cricket every evening from age 11 to 17. I told everyone I'd play Ranji Trophy one day. Then the entrance exam years came, the bat went behind the cupboard, and I never went back. Eight years now. EMBER gives that abandoned passion a voice. You confess what you quit. AI forges its persona: the dusty object, the game itself, or the younger you. Then it talks back , out loud, in a voice matched to its temperament. It asks the question only it can ask: why did you really stop? Then it offers two doors: 🔥 Rekindle it. It negotiates the smallest possible first step ("Pick up your old bat and feel its weight. Sunday evening.") and you seal the pledge on-chain , where you can't quietly delete it. 🕯️ Lay it to rest. It says goodbye properly: a personal eulogy, spoken aloud, and a permanent on-chain stone. Closure is a feature, not a failure state. Every anonymized session joins the Atlas of Abandoned Passions , a live map of what humanity gives up, at what age, and what killed it. When I ran my own confession through it, the app decided my passion should speak as " Your old cricket kit bag ." Its first words: "It's been a while since you hoisted me up here, hasn't it? I still remember the thrill of a good cover drive, too." I built a thing and it emotionally wrecked me on the first test run. Working as intended. Demo 🔗 Live app: https://ember-himanshus-projects-acd54afd.vercel.app Try it in two clicks: tap an example confession (cricket at 17, the closet guitar, the novel at chapter three), headphones on. The voice is the point. A real pledge, sealed on Solana devnet: view the transaction . Code 🔗 Repo: https://github.com/himanshu748/ember How I Built It The loop is confess, converse, decide, commit, belong. Each stage is one sponsor technology doing what it is uniquely good at. Google AI (Gemini): the persona compiler Gemini doesn't chat with you. It reads your confession and forges the character that will. Structured extraction of your story ( years_dormant , abandonment_reason , emotional_tone ), then an embodiment decision : should the object speak (the kit bag), the passion itself (cricket, personified), or the younger you ? It writes the persona's system prompt, its opening line, every conversational reply, and finally the eulogy or the negotiated revival pact. Strict persona rules: it misses you, it never guilt-trips, wry beats weepy. ElevenLabs: the voice The persona's temperament maps to a curated voice (wistful is Sarah, wry is George, bitter is Callum). Every line the passion speaks arrives as real audio. Hearing your abandoned passion say things out loud is the difference between a chatbot and a séance. Snowflake: the Atlas Every session lands in a Snowflake sessions table, and the Atlas page is pure live SQL: most abandoned passions, what killed them, dormancy years, rekindle rate. Snowflake is also the system of record for session state. The app runs serverless, so persona and conversation context are reconstructed from Snowflake on every request. Solana: the commitment device A pledge you can edit is a wish. Rekindle pledges and eulogy stones are attested on Solana devnet via the Memo program: {kind, passion, commitment, confessionHash, ts} . Timestamped, unforgeable, permanent. No wallet needed: a server-side vault signs, so you can go from confession to on-chain proof in one sitting. Stack Next.js 16 · @google/genai · ElevenLabs TTS · snowflake-sdk · @solana/web3.js · Tailwind v4 Prize Categories Best Use of Google AI, Best Use of ElevenLabs, Best Use of Snowflake, Best Use of Solana. The four aren't features bolted onto an app. Each one is a load-bearing stage of a single emotional pipeline. There is a closet like yours in every house on earth. What's in yours? The Atlas is waiting. 🔥

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/himanshu_748/my-abandoned-cricket-kit-confronted-me-so-i-built-it-a-voice-ph1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
