---
title: "Batch Text Analysis with an LLM CLI: 500 Reviews, One For Loop, a Few Cents"
slug: "batch-text-analysis-with-an-llm-cli-500-reviews-one-for-loop-a-few-cents"
author: "张洲诚（Zack.ZHANG）"
source: "devto_ai"
published: "Thu, 06 Aug 2026 03:11:21 +0000"
description: "I tried to get an AI to label 500 Etsy reviews by pasting them into a chat tab, twenty at a time. By batch three, the model had quietly invented a new catego..."
keywords: "output, reviews, batch, text, model, json, you, free"
generated: "2026-08-06T03:12:22.485897"
---

# Batch Text Analysis with an LLM CLI: 500 Reviews, One For Loop, a Few Cents

## Overview

I tried to get an AI to label 500 Etsy reviews by pasting them into a chat tab, twenty at a time. By batch three, the model had quietly invented a new category that wasn't in my labeling scheme. That's not a model problem — it's a container problem. Long conversations drift; batch work needs rules that don't. So I moved the whole job into the terminal. This post is the full walkthrough: sentiment labeling for 500 reviews, a contract risk checklist, an AI-writing check for a thesis chapter, and turning a 2-hour lecture video into Obsidian notes. Total cost for the week: under $0.50. The Tool bl is the CLI for Alibaba Cloud Model Studio. Install with Node.js: npm install -g bailian-cli Get a free API key from the Model Studio console (new accounts include a free tier), then: bl auth login Pattern: Rules as Files, Input as Files, Output as JSON The whole approach fits in one sentence: put your labeling rules in a file, feed inputs from files, write structured output to files. Every call gets identical rules — drift is gone by construction. rule.txt : You are a review analyzer. For the input review output JSON: {"sentiment": "positive/negative/neutral", "aspect": [matching items from "quality","shipping","packaging","price","service"], "intent": "praise/complaint/suggestion/question", "summary": "under 10 words"}. Output JSON only. The loop: for f in reviews/ * .txt ; do bl text chat --model qwen-turbo --system " $( cat rule.txt ) " --message " $( cat " $f " ) " --output json > "out/ $( basename " $f " .txt ) .json" ; done Three deliberate choices: --model qwen-turbo : labeling is factory work, not reasoning work. On a 50-sample side-by-side, the budget tier matched the flagship default — at an order of magnitude lower cost. The 500-review batch cost cents. --output json : results feed straight into a spreadsheet or script. (Piped output defaults to JSON anyway.) File-per-review : 3 items failed on special characters; retrying meant re-running exactly 3 files, not the batch. Sequential run: ~40 minutes. With --concurrent 4 : ~11 minutes. The aggregate: 62% of negative sentiment pointed at "shipping," and 17 product suggestions were hiding inside 5-star reviews. My friend had skimmed those reviews for three evenings and come away with vibes; the loop came back with numbers. Contract → Risk Checklist Same command, different contract (pun intended). The trick is the negative constraint: bl text chat --system "You are a contract reviewer. List ONLY clauses that are unfavorable or unusual for the contractor. For each: quote the exact wording, explain the risk, suggest a redline. Skip boilerplate." --message " $( cat agreement.txt ) " Without "skip boilerplate," the model dutifully reviews every standard clause and buries the signal. With it, my 9-page freelance agreement came back as four flagged items — including an IP-assignment clause that kicked in before final payment. Each with exact quotes I could paste into my reply. Boundary: this is triage. For real money, the checklist is what you bring to a lawyer. AI-ness Check for a Thesis Universities now run AI-content detection on submissions, and my cousin needed a self-check. Honest framing first: no tool guarantees passing any detector, and AI-detecting-AI has real false positives. What works is humbler — locate the most machine-flavored paragraphs and get sentence-level rewrite directions: bl text chat --system "Analyze the input for AI-generation markers: mechanical parallel structures, stock transitions, vague claims with no concrete detail. Rate each paragraph High/Medium/Low and give specific humanization suggestions, down to the sentence." --message " $( cat chapter3.txt ) " Two paragraphs came back High — both were AI output she'd barely edited. She rewrote them herself using the suggestions. 2-Hour Lecture → Obsidian Notes Different command, same philosophy. bl vision describe takes a local video file directly: bl vision describe --video ./lecture.mp4 --prompt "This is a course lecture. Output Markdown study notes: chapters in teaching order, each with core arguments, key examples, and any formulas or code. End with a takeaway list. Use Obsidian-compatible syntax." Minutes later: chaptered notes. I watched 25 minutes of the video instead of 120. Dedicated summarizer tools are more polished (timestamps, browser extensions) but subscription-based; at two videos a month, pay-per-call wins and the note format is whatever my prompt says. The Bill bl usage stats --days 7 at the end of the week: everything above, under $0.50, mostly inside the free tier. bl usage free shows remaining free quota before you fire off a big batch — worth a glance. When to Use This (and When Not) Use it when the work is high-volume, repetitive, and needs structured output — reviews, tickets, surveys, contract triage, lecture backlogs. Skip it if you analyze one text a month (chat tab is fine) or need zero-error output (AI is the triage layer, not the signature). If you've got a pile of unread text of your own, the free tier is enough to run everything in this post: sign up here , and the distance between "unread" and "read, with a checklist" is one for loop. What's the biggest batch-text job you've been putting off? Tell me in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/zackzhang/batch-text-analysis-with-an-llm-cli-500-reviews-one-for-loop-a-few-cents-2m45

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
