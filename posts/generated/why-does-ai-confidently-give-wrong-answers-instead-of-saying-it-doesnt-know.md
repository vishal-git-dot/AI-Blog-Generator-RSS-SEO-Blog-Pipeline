---
title: "Why does AI confidently give wrong answers instead of saying it doesn't know?"
slug: "why-does-ai-confidently-give-wrong-answers-instead-of-saying-it-doesnt-know"
author: "M rstmi"
source: "devto_ai"
published: "Sun, 20 Sep 2026 10:58:37 +0000"
description: "OpenAI's own September 2025 research paper answers this directly, and the analogy they use is exactly what you'd expect from a room full of AI researchers: a..."
keywords: "answers, wrong, guessing, how, confidently, saying, know, research"
generated: "2026-09-20T11:02:02.640186"
---

# Why does AI confidently give wrong answers instead of saying it doesn't know?

## Overview

OpenAI's own September 2025 research paper answers this directly, and the analogy they use is exactly what you'd expect from a room full of AI researchers: an exam. The paper argues hallucinations aren't a mysterious glitch but a predictable result of how models are trained and evaluated. Most benchmarks grade purely on accuracy, the percentage of exactly correct answers. Under that system, saying "I don't know" scores zero, and guessing wrong also scores zero. There's no additional penalty for confidently guessing versus admitting uncertainty, so models learn that guessing is never worse and often better, just like a multiple-choice test with no penalty for wrong answers. This isn't purely academic either. In a widely reported 2023 case, a New York lawyer used ChatGPT for legal research and submitted a court filing citing six completely fabricated court cases, complete with fake judge names and quotes. The lawyer was sanctioned once the fabrication was discovered. The proposed fix: change how benchmarks are scored, explicitly penalizing confident wrong answers more than calibrated uncertainty, similar to how many exams already penalize guessing to discourage it. I wrote a longer breakdown here:[ My Article ]

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/m_rstmi_5744443054d86d511/why-does-ai-confidently-give-wrong-answers-instead-of-saying-it-doesnt-know-2da

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
