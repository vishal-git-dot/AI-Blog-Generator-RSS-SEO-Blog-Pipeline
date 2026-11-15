---
title: "Signal2Speech: what a scientist would catch, and letting Claude read the brain pipeline (Update 3)"
slug: "signal2speech-what-a-scientist-would-catch-and-letting-claude-read-the-brain-pipeline-update-3"
author: "Nate Rupard"
source: "devto_python"
published: "Sun, 15 Nov 2026 05:44:50 +0000"
description: "This is our third update on Signal2Speech, our Hack the Nest 2026 project that lets someone answer questions with an EEG headset. The app suggests replies, t..."
keywords: "our, brain, one, which, what, claude, now, only"
generated: "2026-11-15T05:48:55.489291"
---

# Signal2Speech: what a scientist would catch, and letting Claude read the brain pipeline (Update 3)

## Overview

This is our third update on Signal2Speech, our Hack the Nest 2026 project that lets someone answer questions with an EEG headset. The app suggests replies, the wearer picks one with a P300 response (a brain signal that shows up about 300 milliseconds after the tile you're watching flashes), and they confirm by closing their eyes. Nothing is spoken until they confirm. In our last post, we covered losing our headset in transit and catching Claude giving the wrong answer to our demo question. This update covers about the last hour and a half, going into midnight. The Wayne problem is fixed Last time, every model we tried answered "Wayne" to "Which county's AQI rose more?", which is wrong because Washtenaw rose 186 points and Wayne rose 168. After we added grounding, we re-tested the AI demo window with real Claude Sonnet 5.5 calls. The AQI question now gets the right answer with the "Compare counties" map option, and confirming it shows the map and speaks the correct numbers. A new question got two good replies in about 2 seconds, and the confirmed one was spoken once. With the AI provider unreachable, saved phrases showed up right away, labeled as offline. Checking the science We are also entering the Beyond the Horizon prize, so we wrote a science note explaining exactly what the NASA and EPA data is and what we do and don't claim. While doing this, we found that Washtenaw's "before" AQI of 32 was set by ozone, not by smoke particles. The AQI for a day is set by whichever pollutant is worst, so the before and after numbers for Washtenaw weren't measuring the same thing. The app now shows which pollutant set each number, and the note explains why the comparison still holds and uses Wayne as the like-for-like PM2.5 (fine smoke particles) comparison. We also fixed two things that could mislead someone. The June 26 satellite image is mostly cloud, and the screen now says so, so nobody reads white cloud as clean air. We also corrected the fire distances using the NASA FIRMS data. Most of the fires were about 1,340 km away in Quebec, with a few small ones closer, and the nearest was 84 km away. We checked all of it against EPA and NASA documentation and news reports of the June 28 smoke alert. Claude can read the brain pipeline We built a Model Context Protocol (MCP) server, which is a standard way for an AI assistant to use outside tools. With it, Claude Desktop or Claude Code can ask Signal2Speech about its live signal pipeline and get real numbers back. For example, it can answer "Is the wearer's P300 visible?" from the actual averaged brain response, and it can open the evidence window. On the simulator, it picked up a clear P300 (about 4.8 µV at 276 ms) and got 3 of 3 choices right. Every answer says whether the data is Simulated or Live EEG, and only summaries are sent to the assistant, never raw brain data. EEG is personal health data, so sending only what the assistant actually needs is the same least privilege idea we have used everywhere else in the project. Working with different EEG boards Our eyes-closed confirm used to watch channels 6 to 8, which is right for the g.tec Unicorn but wrong for other boards. The program now detects the device and picks the right channels on its own. For g.tec devices, it uses the three electrodes on the back of the head (PO7, Oz, and PO8). For the PiEEG Octopus 16, which has 16 pins in one small puck, it drops pins that aren't touching the head and averages every pin that responds when the wearer closes their eyes. Live confirm only turns on after a clean check on that wearer, with no false triggers at rest and exactly one confirm per eye closure. We tested this against PiEEG's own script and with a simulated 16-pin stream that had one flat pin and one loose pin. It found both, used the other 14, and confirmed once per closure. It has not been tried on a real board or a real person yet. Smaller things New tile design: The choice tiles now have an icon, a clear title, and a one-line description of what happens. We kept the flash itself the same (plain white with black content), so the brain-signal stimulus doesn't change, and the flash timing check still passes. Faster CI for docs: Pull requests that only change docs now finish their checks in under a minute instead of about five. A quick check also catches leftover merge-conflict markers, which actually broke a few of our doc-only PRs today. Video plan: The demo video will be a screen recording only, 2:30 or less, with every brain-signal shot labeled Simulated or Keyboard. What's next Next, we are recording the demo video and submitting on Devpost. Our draft text is fact-checked against the code, and it never says the headset was used on a real wearer because it hasn't been. Repo: https://github.com/Order-of-the-Golden-Eagles/Signal2Speech

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nrupard06/signal2speech-what-a-scientist-would-catch-and-letting-claude-read-the-brain-pipeline-update-3-p89

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
