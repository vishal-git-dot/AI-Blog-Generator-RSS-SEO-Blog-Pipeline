---
title: "I Automated My Meeting Minutes, Contract Drafts, and Reports With a CLI — Here's the Whole Setup"
slug: "i-automated-my-meeting-minutes-contract-drafts-and-reports-with-a-cli-heres-the-whole-setup"
author: "张洲诚（Zack.ZHANG）"
source: "devto_ai"
published: "Tue, 04 Aug 2026 03:08:23 +0000"
description: "Every Monday I used to lose half a day to paperwork that isn't my actual job: minutes from client calls, yet another statement of work, compressing a six-pag..."
keywords: "minutes, you, model, chat, text, message, contract, transcript"
generated: "2026-08-04T03:13:25.006478"
---

# I Automated My Meeting Minutes, Contract Drafts, and Reports With a CLI — Here's the Whole Setup

## Overview

Every Monday I used to lose half a day to paperwork that isn't my actual job: minutes from client calls, yet another statement of work, compressing a six-page memo for my manager, and the delicate "we're going to be late" email. Last week I moved all of it into my terminal. This is the full setup — every command included. Why not just use a chat tab? I did, for months. The problem isn't quality, it's repetition : paste the transcript, re-explain the format, copy the result, times ten files. And the meeting bots (Otter, Fireflies, Fathom — all genuinely good) only cover meetings inside their ecosystems. My phone recordings from on-site interviews? Nobody's job. Two properties fix this, and both are terminal-native: Prompts become files — my minutes template and contract clause list live in --system strings I wrote once Files are first-class inputs — recordings, CSVs, parameter sheets go straight into commands; ten inputs is a for loop Setup (2 minutes) Node.js 18+, then: npm install -g bailian-cli bl auth login The CLI is bl , Alibaba Cloud Model Studio's command-line tool. Grab a free API key here — the free tier covered my whole week. Docs on the Model Studio CLI page . Recording → minutes, two commands Transcribe (local path works, it uploads for you — --diarization separates speakers, and you want that for multi-person calls): bl speech recognize --url workshop-0728.m4a --language en --diarization --speaker-count 4 --out transcript.json Generate, with the format pinned: bl text chat --system "You are a minutes assistant. From the transcript produce formal minutes: attendees, discussion summary by topic, decisions, and action items with owner and due date. Mark anything not present in the transcript as [TBC]. Never invent details." --message " $( cat transcript.json ) " Lesson #1: my first run skipped --diarization and the minutes attributed a decision to the wrong person. Lesson #2: "Never invent details" is load-bearing. Without it, the model helpfully fabricated a deadline nobody said out loud. With it, I got an honest [TBC] . Ten contract drafts in one loop Eighty percent of my SOW never changes. So: one parameter file per client in contracts/ , then: for f in contracts/ * .txt ; do bl text chat --max-tokens 8000 --system "You are a contract drafting assistant. From the given parameters draft a software development services agreement with these clauses in order: parties, scope of work, timeline and milestones, payment terms, acceptance criteria, intellectual property, confidentiality, maintenance, liability, dispute resolution. Formal register. Output Markdown." --message " $( cat $f ) " > "draft- $( basename $f .txt ) .md" ; done Lesson #3: the default 4096-token output cap truncated a long draft mid-liability-clause. --max-tokens 8000 fixed it. Obligatory honesty: these are drafts for legal review, not signable contracts . My lawyer adjusted wording in three clauses and shipped it. Reviewing beats writing from scratch — that's the entire win, and it's enough. The rest of the pile Same pattern everywhere — format in --system , content in --message : bl text chat --model qwen-turbo --message "Summarize this memo in under 200 words. You must preserve all deadlines and responsible departments: $( cat compliance-memo.txt ) " bl text chat --system "You are a retail data analyst. Structure: overview, monthly trends, anomalies, actionable recommendations. Every claim must cite specific figures from the data. No unsupported statements." --message "12 months of sales data follows: $( cat sales-2025.csv ) " bl text chat --message "Rewrite this email to be professional, courteous and concise while keeping the meaning. Explain each change and why: $( cat draft-email.txt ) " Lesson #4: summaries go to qwen-turbo (the cheap tier — fractions of a cent, totally sufficient); contracts and reports stay on the default model. Budget model for volume, better model for precision. Lesson #5: "every claim must cite specific figures" turned the report from fluent filler into an actual analysis — it even flagged the March return-rate spike unprompted. The week's ledger Task Before After Minutes from a 90-min recording ~1.5 h ~20 min (mostly transcription wait) Ten contract drafts Half a day Minutes + legal review Summaries / formulas / emails 10–30 min each 1–2 min each Spend check (one-time bl auth login --console needed): bl usage free --sort remaining bl usage stats --days 30 ~40 text calls, mostly inside the free tier. Coffee money at list rates. Honest scorecard Great for : recurring paperwork — SOWs, minutes, monthly reports. The prompt files compound; they're assets, not chats. Skip it if : you draft two contracts a year and live entirely inside Zoom's ecosystem. The built-in bots are your shorter path. Never its job : legal judgment, final responsibility for numbers. It converts "write from scratch" into "review and edit" — accountability stays human. Free tier is here if you want to try. Start with whichever task annoys you most — mine was Monday's minutes. What's the paperwork task you'd automate first? Curious what other people's worst offenders are. 👇

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/zackzhang/i-automated-my-meeting-minutes-contract-drafts-and-reports-with-a-cli-heres-the-whole-setup-47ec

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
