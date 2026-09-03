---
title: "A transcript is a record. Minutes are a promise."
slug: "a-transcript-is-a-record-minutes-are-a-promise"
author: "Syed Masood Shah"
source: "devto_ai"
published: "Thu, 03 Sep 2026 20:30:36 +0000"
description: "I know the difference between a transcript and minutes, because I kept the wrong one for years. A transcript is a record of the past. Words, in order, "ums" ..."
keywords: "minutes, you, what, one, meeting, people, transcript, record"
generated: "2026-09-03T20:48:32.220383"
---

# A transcript is a record. Minutes are a promise.

## Overview

I know the difference between a transcript and minutes, because I kept the wrong one for years. A transcript is a record of the past. Words, in order, "ums" and pauses included — and nobody reads it again. It tells you what was said. It does not tell you what happens next. Minutes are a promise. Who's doing what, by when. The whole job of taking minutes isn't to document the meeting — it's to make sure next week's meeting doesn't start with everyone slowly realizing nobody did anything. That's why I run the thing I built for every meeting I'm in. It records mic and system audio (Teams, Zoom, Meet, or a room full of people), transcribes it locally with Whisper, then a small language model I run in LM Studio writes it up as Summary, Key Decisions, Action Items, Open Questions. The action items carry an owner and a due date wherever someone actually said one. Here's what that gets you. Last month a vendor promised he'd have the firewall quotes to me by Thursday. I didn't have to remember that. It's in the minutes, with his name and Thursday on it. When Thursday came and there were no quotes, I didn't say "didn't you say something about that" — I pointed at the line in the file. That's not me being petty. That's minutes doing their job. The quiet win is being able to go back. Three weeks later, someone asks whose junior was supposed to own the CMDB cleanup — I search a folder of Markdown and PDF files and the answer is a timestamped line with a name on it. No scrolling, no "I think it was her?" No. Everything runs on my own hardware. Windows 10/11, Python 3.10+, and LM Studio with any small model loaded. It works on a plain CPU — a GPU just makes transcription faster. This isn't a demo that needs a 4090. It runs on the same cheap laptop I carry to meetings. Worth being blunt about the trade-off: the model is small, so it isn't drafting Oscar-worthy prose. It's structuring what people said into something useful. That's the whole point. I don't need beautiful minutes. I need minutes that make people accountable. One honest note: recording meetings can be regulated where you work, depending on the industry and the room. Check the rules and get consent before you hit record, especially with people from outside your company. Running it locally helps with the security part, but it doesn't make consent optional. If this sounds like the same problem you have, the whole thing is Local Meeting Notes : a one-time $9 Windows app, no subscription, nothing uploaded. It writes exactly the four sections I described, and there's nothing to set up beyond LM Studio. Ten minutes later you're keeping promises instead of files.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/syed_masoodshah_1984/a-transcript-is-a-record-minutes-are-a-promise-2j3p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
