---
title: "Don’t Use console.log for Logging: What Vercel’s Founder Warned About"
slug: "dont-use-consolelog-for-logging-what-vercels-founder-warned-about"
author: "Pratik sharma"
source: "devto_ai"
published: "Sat, 18 Jul 2026 13:22:36 +0000"
description: "I used AI for formatting and grammar. Recently came across this x thread by Pooya Parsa(@_pi0_). He is an open source developer of multiple libraries eg. nit..."
keywords: "request, logging, one, write, log, logger, logs, console"
generated: "2026-07-18T13:26:53.516880"
---

# Don’t Use console.log for Logging: What Vercel’s Founder Warned About

## Overview

I used AI for formatting and grammar. Recently came across this x thread by Pooya Parsa(@_pi0_). He is an open source developer of multiple libraries eg. nitrojsdev, unjs. He trying to solve the bottleneck problems that javascript web dev ecosystem faces. A lot of frameworks are dependent on this open source developers to build this high utility libraries to develop on them. // Detect dark theme var iframe = document.getElementById('tweet-2078164967367295257-77'); if (document.body.className.includes('dark-theme')) { iframe.src = "https://platform.twitter.com/embed/Tweet.html?id=2078164967367295257&theme=dark" } Your API is fast. The database is tuned, responses are cached, and each request finishes in milliseconds. Then you add one harmless line: console . log ( ` ${ req . method } ${ req . url } ` ); How bad could it be? The old request logger in srvx reduced throughput by around 21% when logs were written to /dev/null . That result matters because /dev/null discards everything. There’s no slow disk, remote logging service, or colourful terminal output involved. The application was losing performance simply while creating timestamps, building strings, and calling the output stream. When logging directly to a terminal, the performance loss reached 34%. The timestamp was doing too much work The old logger generated a formatted timestamp for every request using locale-aware date formatting. That seems trivial until your server handles thousands of requests each second. Most of those requests share the same displayed second, yet the timestamp gets recalculated again and again. The new logger caches the formatted time for one second. Instead of asking JavaScript’s Intl machinery to rebuild the same value thousands of times, it calculates it once and reuses it. Small change. Large recovery. One write is cheaper than twenty The logger also batches lines before writing them. Instead of this: Request → write Request → write Request → write Request → write It works more like this: Request ─┐ Request ─┤ Request ─┼── buffer ── one write Request ─┘ The delay is only around one event-loop turn, but it greatly reduces calls to the output stream. Together, timestamp caching and batched writes cut logging overhead by roughly 60–85%, depending on where the logs were sent. Faster logging has an awkward cost Guillermo Rauch : what happens if the process crashes while logs are still waiting in memory? During a normal shutdown, the logger can flush its buffer. During SIGKILL or an OOM kill, JavaScript gets no cleanup window. The last few logs may disappear—and, annoyingly, those may be the exact logs needed to explain the crash. That’s the trade-off: immediate writes are safer but slower; buffered writes are faster but may lose the final event-loop tick. console.log() is fine for local debugging and small scripts. Production logging is different. It needs structured fields, log levels, redaction, backpressure handling, buffering, and clear failure guarantees. The real lesson isn’t that console.log() is universally bad. It’s that code inside a hot path must be judged by how often it runs. One cheap line repeated 20,000 times per second is no longer cheap.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/biomathcode/dont-use-consolelog-for-logging-what-vercels-founder-warned-about-1n46

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
