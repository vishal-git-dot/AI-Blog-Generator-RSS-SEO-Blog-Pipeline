---
title: "What an LLM Actually Does: Predicting the Next Word, Explained"
slug: "what-an-llm-actually-does-predicting-the-next-word-explained"
author: "Devanshu Biswas"
source: "devto_ai"
published: "Wed, 17 Jun 2026 15:42:15 +0000"
description: ""How does ChatGPT think ?" It doesn't. The entire mechanism behind every chatbot is almost anticlimactic: it predicts one next word , adds it, and repeats. I..."
keywords: "word, next, one, model, temperature, how, every, you"
generated: "2026-06-17T15:50:36.575329"
---

# What an LLM Actually Does: Predicting the Next Word, Explained

## Overview

"How does ChatGPT think ?" It doesn't. The entire mechanism behind every chatbot is almost anticlimactic: it predicts one next word , adds it, and repeats. I built a tiny interactive predictor so you can be the model — and it explains both the magic and the flaws. 🔮 Be the model: https://dev48v.infy.uk/ai/days/day6-next-token.html This is Day 6 of AIFromZero — AI literacy, one concept a day, no code to follow. 1. It only predicts the NEXT word Given everything so far, the model outputs a probability for every possible next word, picks one, appends it, and runs again with the longer text. Paragraphs, code, poems — all of it is this one step on repeat. "the cat sat on the ___" → P(mat) high, P(bird) low 2. It's a probability over the WHOLE vocabulary The output isn't one word — it's a number for every word it knows (100,000+ for a real model). Most are near zero; a handful are plausible. The bars in the demo are that distribution, over a tiny vocabulary. 3. Autoregression: feed the output back in After picking a word, it becomes part of the input for the next prediction. Predict → append → predict again. Because each new word conditions on all the previous ones, short local choices add up to coherent long text. 4. Temperature = the creativity dial Once you have probabilities, how do you choose? Temperature reshapes them before sampling: Near 0: the top word always wins — safe, repetitive. High: the odds flatten, so rarer words get a real chance — creative, error-prone. p = p ** ( 1 / temperature ); // then renormalise and sample Drag the slider in the demo and watch the bars sharpen or even out. That one knob is what an API calls "creativity." 5. Where do the probabilities come from? In my toy, from counting which word followed which in a few sentences (a "bigram" with 1-word memory). A real LLM replaces the counting with a giant neural network trained on much of the internet, and its memory spans thousands of words. The mechanism is identical — only the quality of the guess changes. 6. Why this explains so much "Just predicting the next word" explains the fluency (it has seen how language flows) AND the hallucinations: a plausible-sounding next word isn't always a true one. It optimises for likely , not correct . That gap is where made-up facts live — and it's tomorrow's topic. The takeaway Predict next word → append → repeat; temperature tunes the daring. Understand this loop and "the AI thinks…" stops being mysterious and starts being mechanical. Try being the model — click words and watch a sentence build.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/what-an-llm-actually-does-predicting-the-next-word-explained-iag

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
