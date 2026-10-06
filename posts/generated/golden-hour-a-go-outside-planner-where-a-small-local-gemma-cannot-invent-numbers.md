---
title: "golden-hour: a go-outside planner where a small local Gemma cannot invent numbers"
slug: "golden-hour-a-go-outside-planner-where-a-small-local-gemma-cannot-invent-numbers"
author: "Sanskar Kharya"
source: "devto_python"
published: "Tue, 06 Oct 2026 05:31:15 +0000"
description: "This is a submission for the Hacktoberfest Open-Source AI Challenge Week 1: Touch Grass What I Built golden-hour tells you the best hour to go outside in the..."
keywords: "hour, model, not, gemma, sentence, your, one, numbers"
generated: "2026-10-06T05:48:43.496307"
---

# golden-hour: a go-outside planner where a small local Gemma cannot invent numbers

## Overview

This is a submission for the Hacktoberfest Open-Source AI Challenge Week 1: Touch Grass What I Built golden-hour tells you the best hour to go outside in the next 24, and a small gemma running on your own machine says it in one sentence. a rules scorer picks the hour. the model never does. it only writes the sentence, and if a number in that sentence doesn't match the forecast, the sentence is thrown away and a plain template is used instead. $ python -m golden_hour --lat 12.97 --lon 77.59 --place Bengaluru --minutes 45 Go tomorrow at 08:00 in Bengaluru: 23C, dry, wind 6 km/h. [ template] score 95/100, UV 0.9, daylight True (that run was without the model, so it's the template line. with --model pointing at a gemma file, the same facts come out as a sentence like "Please go for a walk tomorrow at 07:00 in Bengaluru with a temperature of 21C and a 9% rain chance.") i built it because the easiest reason to stay in is not knowing when the weather is actually fine. a phone weather app gives you 24 numbers. i wanted one hour and one line. Why open models matter here this is the part i actually care about, so i tried to test it instead of just saying it. it runs offline once downloaded. the gemma 3 1B file (Q4_K_M) is about 806 MB. i ran it on a box with 2 cpus and about 2 GB of ram. no gpu, no api key, no account. only the forecast leaves your machine. your city goes to open-meteo (free, no key). nothing you type goes to a model provider, because the model is a file on your disk. being able to look inside is what made the validator possible. with a local model i could check every number it wrote against the facts it was given and reject it. with a hosted chat box i'd be hoping. How it works forecast from open-meteo, 48 hourly points scorer.py scores each hour out of 100: it loses points under 18C, over 24C, for rain chance, wind over 15 km/h, UV over 5, and 25 for night. the weights are in docs/scoring.md . they are my judgment, not fitted to anything the best start hour for your walk length wins gemma 3 1B gets the facts and writes one sentence the validator pulls every number out of the sentence and checks it against the facts. any mismatch means the template line is used What i measured i ran it for 20 cities (bengaluru, mumbai, delhi, reykjavik, cape town, sydney, seattle, dubai and others), once each, on the same 2-cpu box: gemma's sentence passed validation for 19 of 20 . one fell back to the template (kolkata) median time to write a sentence: 3.0 s (2.5 to 4.3 s) including generation the picked hour was in daylight for all 20. scores ran from 58 to 100, and the five lowest (reykjavik, mexico city, dubai, chennai, sao paulo) each have an obvious reason in the facts: cold, a 67% rain chance, or 29-30C i also tried gemma 3 270M because it loads in 0.6 s. it ignored the task, so i dropped it What i did not test, and what is weak i did not field test it. it was not used on a real walk by anyone yet. the challenge asks for taking it outside, and i can't claim that. the demo and the numbers above are as far as it goes the model is gemma 3 , not gemma 4 the sentences are bland. honestly, the template line is just as useful. the model adds tone, not information. what the model does give is an easy place to see that "a small local model that can't invent numbers" is checkable validation checks numbers, not tone or wording the scorer's weights are my taste. someone who likes cold rain would disagree 20 cities, one run each, is a sanity check and not a benchmark. i did not check forecast accuracy, that is open-meteo's job the web demo runs the scorer in your browser. the sentences shown on it are precomputed on my machine, not generated in your browser Demo live, no install: https://maybesomeone-arc18.github.io/golden-hour/demo/standalone.html type a city and it picks the hour from the live forecast. below it are sample sentences from the local gemma, labelled as precomputed. Code https://github.com/MaybeSomeone-arc18/golden-hour plain python, one dependency ( llama-cpp-python , only if you want the model). 13 tests, python -m pytest tests . the eval script is eval/run_eval.py and the raw results of the run above are in eval/results_gemma3-1b-q4.json . AI assistance this was built with ai assistance. the idea, scoring rules and code were written with an ai agent, and the numbers above come from runs of the code in the repo.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sansk_ya/golden-hour-a-go-outside-planner-where-a-small-local-gemma-cannot-invent-numbers-3ol5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
