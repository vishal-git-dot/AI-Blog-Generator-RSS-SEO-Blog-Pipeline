---
title: "Design a File Uploader That Survives a Dead Connection"
slug: "design-a-file-uploader-that-survives-a-dead-connection"
author: "Nadeem Ur-Rehman"
source: "devto_webdev"
published: "Sun, 08 Nov 2026 12:42:32 +0000"
description: "The interviewer says "design a file uploader" and every candidate draws the same thing. A box, a button, a progress bar. Four minutes in, the whiteboard look..."
keywords: "you, file, not, state, user, chunk, client, uploader"
generated: "2026-11-08T13:02:50.719745"
---

# Design a File Uploader That Survives a Dead Connection

## Overview

The interviewer says "design a file uploader" and every candidate draws the same thing. A box, a button, a progress bar. Four minutes in, the whiteboard looks finished, and the candidate sits back, proud. The interviewer is still waiting for the interview to start. Here is the thing nobody tells you. A file uploader is not a component. It is a state machine with a network that actively hates you. The happy path, pick a file, watch the bar fill, see a green tick, is the smallest part of the design and the least interesting part to score. Anyone can draw that. The interview is scored on everything that happens after the happy path breaks. Start with the question that flips the round. What does your uploader do at 87 percent when the Wi-Fi dies? If your answer is "show an error and start over," you just failed a user who spent nine minutes uploading a 2GB video on hotel Wi-Fi. The senior answer starts somewhere else entirely: chunk the file on the client, upload the chunks in parallel, and ask the server which chunks it already has before you send anything. A dead connection then costs you the chunk in flight, not the whole file. Resume is not a feature you bolt on at the end. Resume is the architecture. That leads to the non-obvious part, the thing most candidates never say out loud. Progress bars lie, and your users know it. A bar that hits 100 percent and then hangs for six seconds while the server validates, scans, and transcodes the file has just taught the user that 100 percent does not mean done. It means "we stopped telling you the truth." Design the states the user actually lives in, not the ones that look good in a demo. Queued. Validating. Uploading. Uploaded but unconfirmed, which is the state that eats people alive. Processing. Done. Failed, with a reason a human can act on. Each state gets its own screen, its own copy, and its own next step. If a state has no next step, you have not designed it, you have decorated it. The sharpest version of this is the unknown state, the one my checkout article lived in. Your client sent the final chunk. The server stored it. The confirmation never arrived. Did the upload succeed? You do not know, and guessing wrong means either a duplicate file or a lost one. The fix is boring and that is why it scores: an idempotency key per file, generated on the client before the first byte moves, sent with every chunk, so a retry is always safe and a duplicate is impossible by construction. Say that sentence in the round and watch the interviewer's pen move. Here is the artifact to carry into the room. The uploader state card. Five lines, one per state that matters, and you fill it in before you draw a single box. Uploading: user sees real progress plus speed and time left. Client holds the chunk list and the retry count. Server knows which chunks arrived. Stalled: user sees "connection lost, retrying in 5 seconds" with a manual retry button. Client holds the last confirmed chunk. Server knows nothing new. Uploaded, unconfirmed: user sees "finishing up, do not close this tab." Client holds the idempotency key. Server either has the file or it does not, and the client asks before it assumes. Processing: user sees what is actually happening, scanning, converting, thumbnailing, with a real step name, not a spinner. Failed: user sees the exact reason and the exact fix. "File too large, limit is 100MB" beats "something went wrong" every single time, in interviews and in production. Five lines. If you can walk an interviewer through those five lines and name the chunk size, the retry policy, and the idempotency key, you have answered the question. The box and the button were never the question. I turned the full 60-question drill set into The Frontend System Design Interview Playbook ($19): https://bittalk.gumroad.com/l/frontend-interview-playbook . The uploader question is in there with the state card and the follow-up probes interviewers use to test whether you have actually shipped one.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nurrehman/design-a-file-uploader-that-survives-a-dead-connection-518h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
