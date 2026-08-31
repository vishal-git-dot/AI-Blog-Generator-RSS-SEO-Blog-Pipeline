---
title: "Don't trust my "client-side only" claim. Open DevTools and check."
slug: "dont-trust-my-client-side-only-claim-open-devtools-and-check"
author: "Format stack"
source: "devto_webdev"
published: "Mon, 31 Aug 2026 04:39:00 +0000"
description: "Carhartt just had 12.9 million customer accounts show up on Have I Been Pwned. Names, emails, phone numbers, physical addresses — all pulled by an extortion ..."
keywords: "your, you, data, tool, not, don, open, pasted"
generated: "2026-08-31T04:52:56.231404"
---

# Don't trust my "client-side only" claim. Open DevTools and check.

## Overview

Carhartt just had 12.9 million customer accounts show up on Have I Been Pwned. Names, emails, phone numbers, physical addresses — all pulled by an extortion group that says it grabbed the data back in August. Manchester Airports Group had a similar week: Wi-Fi signup data across three UK airports, gone. Neither of those companies got breached because a user pasted something into a sketchy tool. They got breached because they stored data server-side, and storage is a standing liability — it sits there waiting to be exfiltrated. But those headlines are exactly why "we don't store your data" claims from random web tools are worth being skeptical of, not trusting. Every JSON formatter, regex tester, and Base64 decoder on the internet says some version of "your data never leaves your browser." Most of them are telling the truth. Some aren't. You have no way to know which, unless you check. So here's the actual check, using FormatStack as the example, since it's the one I can show you the source for. The claim FormatStack's tools — JSON formatter , regex tester , UUID generator , Base64 encoder/decoder , cron parser — run entirely in-browser. No framework, no build step shipping your input to a server, no API call carrying your pasted content anywhere. The proof, not the promise Anyone can write "processed locally" in a footer. Here's how to verify it takes about 30 seconds and works on any tool claiming client-side processing, not just this one: Open the tool in your browser. Open DevTools (F12 or Cmd+Option+I), go to the Network tab. Clear the log, then paste in something identifiable — a fake API key, a made-up email, whatever you'll recognize. Run the formatter/parser/whatever the tool does. Watch the Network tab. If your pasted content is client-side only, you'll see zero new requests carrying that payload. Analytics pings may fire (page views, button clicks) — that's expected and disclosed — but none of them will contain your input. If instead you see a POST request firing off to some API right after you paste, with your input sitting in the request body — that tool is not doing what its marketing copy says, regardless of what the footer claims. Why I'm not hiding the parts that do send data FormatStack runs Google Analytics and AdSense. Both of those make outbound requests. I'm not going to pretend otherwise — that would be the same category of lie as a tool that silently uploads your JSON. The distinction that actually matters, and the only one I'm claiming, is narrow: analytics tracks that you used the tool; nothing tracks what you put into it. Open the Network tab and you'll see the difference — GA calls carry event names and page paths, never your pasted payload. That's a smaller claim than "we don't track anything," and it's also the only one that survives someone actually checking. The takeaway Breach news cycles every few weeks because storage is a liability regardless of intent — good security practices reduce risk, they don't eliminate the fact that stored data can eventually leak. The tools that can't leak your pasted content are the ones that never had it to lose. But don't take my word for that either. Open the tab. Check.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/formatstack_2688dca3303f2/dont-trust-my-client-side-only-claim-open-devtools-and-check-51fe

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
