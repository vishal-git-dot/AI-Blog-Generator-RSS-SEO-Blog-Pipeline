---
title: "I Built a Procrastination Pattern Detector with 8 CBT Interventions — No AI, No ML"
slug: "i-built-a-procrastination-pattern-detector-with-8-cbt-interventions-no-ai-no-ml"
author: "CBT Tools"
source: "devto_python"
published: "Sat, 19 Sep 2026 19:08:49 +0000"
description: "You're not lazy. You're running one of 8 procrastination patterns, each with a specific CBT intervention that breaks the cycle. I built a detector that ident..."
keywords: "intervention, you, pattern, cbt, detector, not, patterns, procrastination"
generated: "2026-09-19T20:21:54.587650"
---

# I Built a Procrastination Pattern Detector with 8 CBT Interventions — No AI, No ML

## Overview

You're not lazy. You're running one of 8 procrastination patterns, each with a specific CBT intervention that breaks the cycle. I built a detector that identifies which patterns are keeping you stuck — using keyword matching, not machine learning. The 8 Procrastination Patterns Each pattern has a root cause, a behavioral signature, and an evidence-based CBT intervention: Perfectionism Block — "If I can't do it perfectly, I won't start." Intervention: valued action over quality Fear of Failure — "What if I try and fail?" Intervention: decatastrophize the failure outcome Task Overwhelm — "There's too much to do." Intervention: break into 5-minute micro-steps Waiting for Motivation — "I'll do it when I feel like it." Intervention: behavioral activation — action precedes motivation Task Avoidance — "I'll do anything except the task." Intervention: identify and remove avoidance behavior All-or-Nothing Approach — "I either do it all or none." Intervention: partial progress is still progress Guilt-Procrastination Cycle — "I procrastinated → I feel guilty → I procrastinate more." Intervention: self-compassion breaks the cycle Minimization Trap — "It's not that important." Intervention: reconnect with values and long-term cost How It Works The detector uses keyword-pattern matching — the same approach I used for my CBT Thought Analyzer : PATTERNS = [ { " id " : " perfectionism_block " , " keywords " : [ " perfect " , " flawless " , " not good enough " , " has to be right " ], " intervention " : " You ' re waiting for perfect conditions that will never come. " " CBT: valued action > quality. Start with a 5-min imperfect draft. " }, { " id " : " fear_of_failure " , " keywords " : [ " what if i fail " , " fail " , " mistake " , " embarrass " ], " intervention " : " You ' re catastrophizing failure. CBT: What ' s the realistic " " worst case? Can you survive it? What ' s the cost of NOT trying? " }, # ... 6 more patterns ] def detect_procrastination ( text ): detected = [] text_lower = text . lower () for pattern in PATTERNS : matches = [ kw for kw in pattern [ " keywords " ] if kw in text_lower ] if matches : detected . append ({ " pattern " : pattern [ " id " ], " confidence " : len ( matches ) / len ( pattern [ " keywords " ]), " evidence " : matches , " intervention " : pattern [ " intervention " ] }) return sorted ( detected , key = lambda x : x [ " confidence " ], reverse = True ) No embeddings. No fine-tuning. No API calls to OpenAI. Just keyword matching against a curated list of behavioral signatures derived from CBT research. Why Keyword Matching > ML for This Domain Determinism : Same input → same output, every time. ML models give different results on different runs. For a clinical tool, nondeterminism is a bug. Explainability : The matched keywords ARE the evidence. You can see exactly why the detector flagged "perfectionism block" — because you wrote "has to be perfect" and "not good enough." An ML model gives you a probability and a black box. Zero Cost : No GPU, no API calls, no inference latency. The detector runs in <1ms. Privacy : The text never leaves your device. No data sent to a server. Known Output Space : There are exactly 8 patterns from decades of CBT research. ML might discover a 9th, but it would be a noise cluster, not a clinically validated pattern. The API The detector is deployed as a REST API on Render: curl -X POST https://cbt-thought-analyzer.onrender.com/procrastination -H "Content-Type: application/json" -d '{"text": "I need to write my thesis but it has to be perfect and I keep waiting for the right time to start"}' Response: { "patterns_detected" : [ { "pattern" : "perfectionism_block" , "confidence" : 0.5 , "evidence" : [ "perfect" ], "intervention" : "You're waiting for perfect conditions..." }, { "pattern" : "waiting_for_motivation" , "confidence" : 0.33 , "evidence" : [ "waiting for the right time" ], "intervention" : "Behavioral activation: action precedes motivation..." } ], "total_patterns" : 2 , "dominant_pattern" : "perfectionism_block" } The Behavioral Activation Principle The core insight behind all 8 interventions: action precedes motivation, not the other way around. This is the central finding of behavioral activation research (Jacobson et al., 1996; Dimidjian et al., 2006). You don't wait until you feel like doing something — you do it, and the feeling follows. Each intervention in the detector is a specific application of this principle to the pattern's root cause: Perfectionism → start with an imperfect 5-min draft Fear of failure → test the catastrophic prediction with a small experiment Task overwhelm → identify the smallest possible first step Waiting for motivation → act for 5 minutes, then reassess Try It The API is live. The detector is also submitted to aitopia.ai as an AI agent (in review) — if approved, you'll be able to invoke it from the marketplace. import requests response = requests . post ( " https://cbt-thought-analyzer.onrender.com/procrastination " , json = { " text " : " I keep putting off my taxes because I might make a mistake " } ) print ( response . json ()) No AI. No ML. No NLP library. Just psychology.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/473185670/i-built-a-procrastination-pattern-detector-with-8-cbt-interventions-no-ai-no-ml-4pc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
