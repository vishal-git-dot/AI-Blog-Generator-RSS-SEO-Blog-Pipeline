---
title: "I spent a day breaking my own eval tool's scoring rule, and it was the best use of the day"
slug: "i-spent-a-day-breaking-my-own-eval-tools-scoring-rule-and-it-was-the-best-use-of-the-day"
author: "AI Stack Lab"
source: "devto_python"
published: "Sun, 22 Nov 2026 05:40:21 +0000"
description: "This is the developer-facing version of a post I published on AI Stack Lab: Your Eval Suite Is Theater Until a Non-Zero Exit Code Stops the Merge . Same meas..."
keywords: "not, you, one, your, expected, rule, suite, exit"
generated: "2026-11-22T06:01:01.628847"
---

# I spent a day breaking my own eval tool's scoring rule, and it was the best use of the day

## Overview

This is the developer-facing version of a post I published on AI Stack Lab: Your Eval Suite Is Theater Until a Non-Zero Exit Code Stops the Merge . Same measurements, different angle — this one is about the scoring rule itself. I spent a day breaking my own eval tool's scoring rule, and it was the best use of the day Last week I shipped a $1 CLI called AIEval that does exactly one thing: read a JSONL of recorded model answers, compare each one to an expected string, and exit non-zero if accuracy falls under a threshold you wrote in a config file. Offline, stdlib only, 275 lines of Python. The part I want to write about is not the tool. It is the twenty minutes I spent trying to make its own metric lie to me. The rule, unedited def _score_answer ( response , expected ) : if not expected : return True r = " " . join ( str ( response ) . split ( ) ) . lower ( ) e = " " . join ( str ( expected ) . split ( ) ) . lower ( ) return e in r Lowercase both. Collapse every whitespace run to one space. Substring test. That is the whole grader. I chose that on purpose, because when you are gating a merge, a rule you can read in six lines is worth more than a rule you have to trust. But "readable" and "correct" are different claims, so I built a four-prompt suite with a 0.80 gate and fed it answers that should not pass. What actually happened expected response verdict why yes Yesterday it was. PASS yes sits inside yesterday not found 404 means Not\nFound PASS whitespace normalisation `` (empty) tabs, obviously PASS empty expected = auto pass, by design paris Lyon. FAIL correctly rejected Result: 75.00% (3/4 passed) , Gate min_accuracy=0.80: FAIL , exit code 1. Three of four verdicts came from substring behaviour, not from the model being right or wrong. That is the whole trap in miniature: if your expected strings are short tokens, your accuracy number is partly a coincidence. yes , no , 15 , ok — every one of them is a substring of something a wrong answer would plausibly contain. You are not measuring your model; you are measuring your vocabulary. The fix is boring and it is the actual skill Choose expected strings that a wrong answer cannot accidentally contain. Not yes but the sky is blue . Not 15 but the sum of the first five natural numbers is 15 . Not paris but the capital of france is paris . It reads badly in a diff and it saves you a quarter of argument in a review. Two more things I only found by running it rather than reading the README: A missing response is a failure, not a skip. I recorded one answer for three prompts on purpose: 0/3 , Missing responses: 2 (counted as failures) , exit 1. The safe direction — a crashed recorder should collapse the score, not silently score the rows that survived — but it looks exactly like a model regression until you read the missing-count line. Put that line in your alert. max_avg_latency_ms is inert. It is accepted from config.json and printed as NOT ENFORCED with an explanation, because the harness never times a call. It says so out loud instead of ignoring the key, which I appreciate more than I expected to. Where this fits, and where it does not If your eval story is "we have a dashboard", the missing piece is probably not a better dashboard. It is one non-zero exit code in a CI step: ` yaml name: Record answers run: python3 scripts/record_answers.py --suite evals/my-suite --out answers.jsonl name: Gate on accuracy run: python3 eval-harness.py run evals/my-suite --responses answers.jsonl ` The recorder is yours — whatever talks to your provider, in whatever language. AIEval never calls a model, holds no API key, and has zero network code in it (I grepped for requests , urllib , socket , http : zero hits in the whole 10,127-byte file). Secrets stay in your recorder, scoring stays in a separate process, and the only thing crossing between them is {"id","response"} lines. Disclosure: AIEval CLI is my own product, sold on Gumroad for $1.00 USD (read from the live listing at write time: product:price:amount=1.0 and a JSON-LD offer at 1.0 USD ). I earn the sale if you buy through this link: https://nandminc.gumroad.com/l/vmocdo . It is a scaffold + scorer + exit code — not a runtime, not an LLM judge, not a tracing platform. If you need semantic grading or latency percentiles, this is the wrong tool and I would rather say so here than have you find out after paying a dollar. Honesty block, unsoftened: example figures in this post are illustrative planning inputs — not market rates and not earnings. No legal, tax, insurance, licensing, veterinary, automotive-repair, or financial advice. No CRM, map, API or invoicing integrations are claimed or shipped; the bundle is one Python file, one bash wrapper, one MIT licence and an example suite. No ratings, testimonials, customer counts or revenue figures appear anywhere above, because I have none to cite. MIT licensed, offline, Python 3.8+. If a run contradicts anything in this post, the support address in the README is a real inbox and I answer it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/the_movie_9b1357e8c99cfaa/i-spent-a-day-breaking-my-own-eval-tools-scoring-rule-and-it-was-the-best-use-of-the-day-eak

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
