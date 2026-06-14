---
title: "Vibe coding works until you try to change something"
slug: "vibe-coding-works-until-you-try-to-change-something"
author: "Marco Gundlach"
source: "devto_webdev"
published: "Sun, 14 Jun 2026 19:16:12 +0000"
description: "The first version almost always works. That is the part nobody is ready for. You describe what you want in one sentence, wait two minutes, and a small tool i..."
keywords: "you, not, one, vibe, code, model, coding, small"
generated: "2026-06-14T19:44:48.278250"
---

# Vibe coding works until you try to change something

## Overview

The first version almost always works. That is the part nobody is ready for. You describe what you want in one sentence, wait two minutes, and a small tool is running in your browser. It feels like a trick. The second moment feels different. You want to change one small thing. The model cheerfully rewrites half the file. Now the part that worked a minute ago is broken, and you are not sure why. This is the exact spot where useful vibe coding splits off from throwaway code. I have spent the last year building small and mid sized apps mostly through natural language, usually on Next.js with Supabase behind it. Here is the short version of what I learned. The bottleneck is no longer typing code. It is how precisely you describe the thing and how carefully you read what comes back. Get that right and you end up with something you can still maintain six months later. Ignore it and you produce, in record time, the exact kind of system nobody wants to touch. A spec beats a vibe The phrase "vibe coding" is a little misleading. It suggests you just vibe and code appears. In practice the opposite is true. The clearer your first prompt, the fewer rounds you need after it. A weak start looks like this: Build me a dashboard for our sales numbers. A good start hands the model the context it would otherwise have to guess: Add a page at /dashboard in our existing Next.js App Router project. Data comes from a Supabase table called "sales" with columns date, region, amount. Show a bar chart of total amount per region, and below it a sortable table. Reuse the components in our existing ui folder. Do not add new dependencies without asking first. The difference is not about being polite to the machine. The difference is that the second version makes decisions instead of leaving them open. Every decision you skip, the model makes for you, and it makes a slightly different one on every run. That last line matters more than it looks. " Do not add new dependencies without asking " stops the model from quietly writing three extra packages into your package.json because they seemed handy at the time. Guardrails like that, written once into the prompt, save you hours later. Small steps, or pain The most common mistake is handing the model too much at once and then letting a big change run across existing code. These models love to rewrite more than you asked. Point one at a 400 line file with the task "change the date format" and you get back a 400 line file where the date format is correct and three other things are subtly broken. What helps is dull and it works anyway. Keep the units small. One function, one component, one clearly scoped task per run. And commit after every working state. Git is not a nice extra here. It is your seatbelt. When the next run breaks something, you roll it back in two seconds instead of playing detective. My loop now is almost always the same. Working state, commit, change one thing, test, commit. It sounds like more overhead. It is faster in the end, because I never land in the situation where I have to untangle a pile of mixed changes that all arrived together. You own the code, so read it The most dangerous sentence in vibe coding is "well, it runs." Whether something runs tells you nothing about whether it does the right thing or whether it is safe. Here is a real one. Ask a model to load data from Supabase and it will often write the query straight into a client component and never mention Row Level Security. In a demo with test data this never shows up. The moment real users and real data arrive, you have shipped a data leak without noticing. The model did not do anything wrong in the "the code compiles" sense. It made an assumption that happens to be false in your setup. So treat generated code as a draft, not a finished product. You do not need to be able to write every line yourself from memory. You do need to read it and follow what it does. When you hit a spot you do not understand, ask the model to explain it before you accept it. Those five minutes are the best investment in the whole process. Where it pays off and where it does not After enough projects a pattern shows up for which jobs vibe coding actually saves time. It shines on internal tools with a contained scope. Configurators. Reports. Prototypes. Small automations. Anything with a clear task and a low blast radius if it goes wrong. A two week project regularly turns into an afternoon here, and without a drop in quality if you follow the points above. It gets miserable once a system is large, tightly connected, and business critical. The more moving parts, the harder it is to keep control through language alone. That does not mean you drop AI entirely on those systems. It means you keep an experienced developer in the loop who can judge the suggestions instead of accepting them blind. Knowing that line honestly is not a weakness. It is the difference between someone who uses vibe coding productively and someone who just buys themselves a new set of problems. The actual shift If I had to reduce all of this to one thing, it is this. Vibe coding does not make programming faster. It changes who can build software at all. Someone who knows their problem cold but never learned to code can now build a working solution, as long as they pick up the handful of habits I described here. Write a clear spec. Work in small steps. Read the code you accept. Know where your own limit is. None of that is a secret and none of it is magic. It is a craft with a new tool in it. And like any tool, the result comes down to the hand holding it, not the tool.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mgundlach/vibe-coding-works-until-you-try-to-change-something-776

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
