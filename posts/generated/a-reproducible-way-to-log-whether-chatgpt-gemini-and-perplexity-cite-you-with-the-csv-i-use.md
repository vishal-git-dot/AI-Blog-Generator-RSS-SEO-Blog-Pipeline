---
title: "A reproducible way to log whether ChatGPT, Gemini and Perplexity cite you (with the CSV I use)"
slug: "a-reproducible-way-to-log-whether-chatgpt-gemini-and-perplexity-cite-you-with-the-csv-i-use"
author: "Robin"
source: "devto_ai"
published: "Sat, 24 Oct 2026 20:25:57 +0000"
description: "Small detail that made me write this: when I asked Perplexity "How do I check if ChatGPT recommends my product?" on 24 Oct 2026, 2 of its 10 sources were dev..."
keywords: "you, week, perplexity, answers, answer, chatgpt, use, not"
generated: "2026-10-24T20:31:17.912211"
---

# A reproducible way to log whether ChatGPT, Gemini and Perplexity cite you (with the CSV I use)

## Overview

Small detail that made me write this: when I asked Perplexity "How do I check if ChatGPT recommends my product?" on 24 Oct 2026, 2 of its 10 sources were dev.to posts. Not mine, other authors. So if you write about this topic here, you are on a platform that actually gets pulled into answers. Here is the method I use to check that week over week, without a paid tool. It is boring on purpose. Boring is reproducible. Why bother logging at all I ran 8 fixed buyer questions on ChatGPT, Gemini and Perplexity on 17 Oct and 24 Oct. Two things stood out in the data: The engines barely share sources. In week 1, ChatGPT and Gemini overlapped on only 3 domains. Gemini's source list mostly turned over in one week. Only a handful of URLs repeated. If the answers move that much, a single check tells you very little. You need the same questions, asked the same way, logged the same way, repeatedly. (And yes, for transparency: my own stuff appeared in 0 of 40 answers across both weeks. The method works fine for measuring zero.) Step 1: freeze your questions Write 8 to 20 questions a buyer would type, without your brand name in them. All three engines recommended testing somewhere between 10 and 50 prompts, so pick a number you will actually keep up. Then freeze them. Put them in a file, give each an ID, and never reword. Mine look like this: Q1 | How do I check if ChatGPT recommends my product? Q3 | What tools can I use to see if AI assistants cite my site? Q8 | What are cheap or free tools to monitor my brand's visibility in AI answers? If you change the wording in week 3, you cannot compare week 3 to week 1. That is the whole game. Step 2: control the session Record the session state as data, because it changes the answer: ChatGPT: I use it logged out, web search at default. Gemini: signed in to the same account every week (signed-in answers may be personalised, so note it). Perplexity: logged-out use was blocked for me on all 8 questions in week 1 ("Sign up and repeat your request."), so I now use a free account. Perplexity's own answer to Q1 recommended running each prompt 3 times in a clean session, on different days. Gemini said 3 to 5 runs in a temporary chat the week before. I currently do one run per question per engine, which is the weak point of my setup. If you have the time, do 3 and record the run number. Step 3: log with a fixed schema This is the header of my log.csv , plus a run column I recommend adding: date,engine,question_id,run,web_search_or_sources_shown,cited_urls,brands_tools_named,our_presence,note A few rules that saved me later: One row per answer. 3 engines x 8 questions = 24 rows per week. Copy cited URLs exactly. Answer text can be summarized, but URLs are your real dataset. They are what lets you spot that dev.to showed up, or that 10 different small sites made up one source list. Log the engine config in the row ("logged out, web search default on"). Log blocked runs as rows. My week 1 Perplexity rows say blocked . Missing data you documented is still data. Separate "named" from "cited". A brand can be mentioned without a link, or linked without being recommended. Perplexity's Q1 answer suggested tracking whether you are named, your position, accuracy, competitors and cited URLs. Keep the raw answer for each row in its own text file ( raw/2026-10-24/perplexity-Q1.txt ). The CSV is for counting, the raw file is for rereading. Step 4: compute two simple numbers You do not need a dashboard. Two numbers per week are enough: Presence rate: answers that name or cite you / total answers. Source overlap: domains that appear in this week's list and last week's list, per engine. The second one is underrated. It tells you how stable the "slot" you are trying to win actually is. Step 5 (optional): the GA4 side Logging answers tells you if you are cited. It does not tell you if anyone clicks. On the two GA4 questions, all three engines gave essentially the same answer both weeks: use GA4's AI Assistant channel, check session source/medium, and build a custom channel group above Referral with a regex. Perplexity's version of the filter: chatgpt\.com|chat\.openai\.com|openai\.com|perplexity\.ai Two caveats the engines themselves gave: some AI visits land as Direct, and Perplexity traffic can still show up under Referral even with the AI Assistant channel. I do not have my own GA4 numbers to share here, so treat this as the consensus answer, not my results. What the engines will not tell you Every engine now recommends a manual spreadsheet, alongside tools like Otterly, Peec, Profound and the HubSpot AI Search Grader. The method is not a secret. What the free advice skips is discipline: frozen wording, controlled sessions, exact URLs, week-over-week comparison. I am on week 2 of doing this in public. If you run the same kind of log, I would genuinely like to compare overlap numbers in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/robin_geo/a-reproducible-way-to-log-whether-chatgpt-gemini-and-perplexity-cite-you-with-the-csv-i-use-2do8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
