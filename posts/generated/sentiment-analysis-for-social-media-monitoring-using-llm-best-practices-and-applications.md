---
title: "Sentiment Analysis for Social Media Monitoring using LLM: Best Practices and Applications"
slug: "sentiment-analysis-for-social-media-monitoring-using-llm-best-practices-and-applications"
author: "shashank ms"
source: "devto_ai"
published: "Thu, 18 Jun 2026 15:36:06 +0000"
description: "We are building a real-time sentiment analysis pipeline that ingests raw social media posts, classifies each by sentiment, extracts mentioned entities, and f..."
keywords: "sentiment, oxlo, confidence, posts, negative, entities, post, escalate"
generated: "2026-06-18T15:38:46.164551"
---

# Sentiment Analysis for Social Media Monitoring using LLM: Best Practices and Applications

## Overview

We are building a real-time sentiment analysis pipeline that ingests raw social media posts, classifies each by sentiment, extracts mentioned entities, and flags posts that need immediate attention. It helps community managers and brand teams catch negative spikes without reading every comment manually. What you'll need You need Python 3.10 or newer, the OpenAI SDK, and an Oxlo.ai API key from https://portal.oxlo.ai . Install the SDK with pip. pip install openai Step 1: Set up the Oxlo.ai client We initialize the OpenAI-compatible client pointing to Oxlo.ai. I use Llama 3.3 70B because it handles classification reliably, and Oxlo.ai's flat per-request pricing keeps costs predictable even when we pass in long posts or full comment threads. from openai import OpenAI client = OpenAI(base_url="https://api.oxlo.ai/v1", api_key="YOUR_OXLO_API_KEY") Step 2: Define the system prompt The system prompt forces structured JSON output. We want a sentiment label, confidence score, mentioned entities, and an escalation flag. Keeping this in the system prompt reduces token overhead in the user message. SYSTEM_PROMPT = """You are a social media sentiment analyzer. Analyze the user-provided post and respond with a single JSON object containing exactly these keys: - sentiment: one of "positive", "neutral", or "negative" - confidence: an integer from 1 to 10 - entities: an array of brand or product names mentioned, or an empty array - escalate: boolean, true only if the post is strongly negative and mentions a specific product flaw or safety issue Respond with only the JSON object, no markdown fences, no commentary.""" Step 3: Build the analyzer function This function sends a raw post to Oxlo.ai and returns a parsed dict. Because Oxlo.ai charges per request rather than per token, we can include the full text of long posts without watching input costs scale. import json def analyze_post(post_text: str) -> dict: response = client.chat.completions.create( model="llama-3.3-70b", messages=[ {"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": post_text}, ], ) raw = response.choices[0].message.content.strip() return json.loads(raw) Step 4: Process a batch of posts Monitoring means handling volume. Here we define a list of incoming posts, analyze each one, and collect the results. In production this list would come from a social media API webhook. posts = [ "Just got the new Aurora Phone and the battery life is incredible. Best purchase this year!", "Seriously disappointed with the Aurora Phone. It overheats after 10 minutes of video calls and the screen flickers.", "Anyone know if the Nova Laptop works well with Linux? Thinking about buying one.", "The Nova Laptop charger sparked and smelled like burning plastic. This is a safety hazard.", ] results = [] for post in posts: try: result = analyze_post(post) result["original"] = post results.append(result) except Exception as e: print(f"Failed to analyze post: {e}") print(json.dumps(results, indent=2)) Step 5: Add alerting logic Raw scores are useless without action. We add a simple rule: if sentiment is negative and confidence is 8 or higher, or if escalate is true, we print an alert. This turns the LLM output into a signal a human can act on. def check_alerts(results: list[dict]): for r in results: if r.get("escalate"): print(f"ESCALATION ALERT: {r['original'][:80]}...") continue if r.get("sentiment") == "negative" and r.get("confidence", 0) >= 8: print(f"HIGH CONFIDENCE NEGATIVE: {r['original'][:80]}...") check_alerts(results) Run it Save the script as sentiment_monitor.py , replace YOUR_OXLO_API_KEY with your key from the Oxlo.ai portal , and run it. python sentiment_monitor.py Expected output looks like this: [ { "sentiment": "positive", "confidence": 9, "entities": ["Aurora Phone"], "escalate": false, "original": "Just got the new Aurora Phone and the battery life is incredible. Best purchase this year!" }, { "sentiment": "negative", "confidence": 9, "entities": ["Aurora Phone"], "escalate": false, "original": "Seriously disappointed with the Aurora Phone. It overheats after 10 minutes of video calls and the screen flickers." }, { "sentiment": "neutral", "confidence": 5, "entities": ["Nova Laptop"], "escalate": false, "original": "Anyone know if the Nova Laptop works well with Linux? Thinking about buying one." }, { "sentiment": "negative", "confidence": 10, "entities": ["Nova Laptop"], "escalate": true, "original": "The Nova Laptop charger sparked and smelled like burning plastic. This is a safety hazard." } ] ESCALATION ALERT: The Nova Laptop charger sparked and smelled like burning plastic. This is... HIGH CONFIDENCE NEGATIVE: Seriously disappointed with the Aurora Phone. It overheats after... Wrap-up This pipeline gives you a working foundation. Two concrete next steps: wire the posts list to a real-time social media API feed so you analyze live data, and swap in qwen-3-32b if you need to monitor multilingual conversations across regions. Oxlo.ai's flat per-request pricing makes both long-context thread analysis and high-volume streaming affordable, since cost does not scale with prompt length.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shashank_ms_6a35baa4be138/sentiment-analysis-for-social-media-monitoring-using-llm-best-practices-and-applications-3j06

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
