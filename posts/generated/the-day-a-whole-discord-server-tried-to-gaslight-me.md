---
title: "The Day a Whole Discord Server Tried to Gaslight Me"
slug: "the-day-a-whole-discord-server-tried-to-gaslight-me"
author: "Seif Ahmed"
source: "devto_python"
published: "Tue, 29 Sep 2026 12:13:31 +0000"
description: "We've all run into toxic spaces, but yesterday I experienced a level of tech gaslighting so unhinged that I still can't quite believe it happened. It started..."
keywords: "python, they, print, ocaml, server, built, debate, their"
generated: "2026-09-29T12:30:40.036074"
---

# The Day a Whole Discord Server Tried to Gaslight Me

## Overview

We've all run into toxic spaces, but yesterday I experienced a level of tech gaslighting so unhinged that I still can't quite believe it happened. It started in a large developer Discord server. Someone made a joke a joke that hello() is a built-in method used for printing in Python. They likely said so because of the classic print("hello world") . I pointed out a simple truth: print() is the built-in function for printing in Python. Looks simple, right? Literally the first page of any programming book. But what I followed wasn't a normal technical debate. It was madness. The "Proof" That Python is Broken To prove me wrong, one user decided to use their "high-level" engineering skills by doing this: print = None print ( " hello world " ) # TypeError: 'NoneType' object is not callable They overrode the built-in global namespace to overwrite the print function with None , ran it, watched it predictably crash, and then used that as proof that print() is invalid. That's the equivalent of cutting the brake lines on a new car and claiming the manufacturer doesn't know how to build brakes. Using OCaml as "Python 4" When I refused to back down because of facts, things got even weirder. They opened up an OCaml REPL, tried to execute Python code inside it, and when the compiler threw a syntax error, they claimed it proved my code was broken. Their justification? They argued that OCaml is actually a "Python 4 REPL". For anyone keeping track at their home: OCaml is a completely distinct language from the ML family. Python 4 doesn't even exist and the core Python dev team has repeatedly stated they've no plans for a version 4 anytime soon. Attacking Me Personally The absolute worst part wasn't just the main troll—it was the fact that the entire chat room ganged up on me for entertainment. Because of classic Discord mentality, everyone jumped into the "debate" to protect their status. They stopped using logic and started launching personal attacks to bully me into backing down. I'm not proud of this at all, but after providing every single proof that print() is the built-in method to print in Python, I lost my cool and fired back with the exact same insults they used. Even worse, I deleted all my past messages to "hide" these insults. The Lesson I Learned: Protecting My Peace Is Better Than Winning Any Debate. I realized that I wasted massive amounts of energy into a room full of people who wanted a debate just for internet attention. So I did the best thing I can ever do: I hit the "Leave Server" button. If I fire back with logic, they bend the reality. If I fire back with insults, I give them the drama and attention they're starving for. The only way to win is to starve them of fuel completely. Instead of fighting people who think OCaml is Python 4, I'm using my energy to continue building my social media app, Vlox. My code speaks louder than any toxic chat. Did you ever deal with a developer community that tried to completely gaslight you over basic programming concepts? How do you handle it when a server turns into a mob? Let's have a good talk together.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/codemaster_121482/the-day-a-whole-discord-server-tried-to-gaslight-me-280i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
