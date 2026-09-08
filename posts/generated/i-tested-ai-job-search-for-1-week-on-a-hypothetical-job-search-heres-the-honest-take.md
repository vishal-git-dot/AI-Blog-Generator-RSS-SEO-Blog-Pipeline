---
title: "I tested AI Job Search for 1 week on a hypothetical job search — here's the honest take"
slug: "i-tested-ai-job-search-for-1-week-on-a-hypothetical-job-search-heres-the-honest-take"
author: "Alex"
source: "devto_python"
published: "Tue, 08 Sep 2026 16:17:07 +0000"
description: "I tested AI Job Search for 1 week on a hypothetical search — here's the honest take AI Job Search is a 13K-star open-source tool that matches your resume to ..."
keywords: "job, you, search, resume, your, not, tool, agent"
generated: "2026-09-08T16:23:34.869734"
---

# I tested AI Job Search for 1 week on a hypothetical job search — here's the honest take

## Overview

I tested AI Job Search for 1 week on a hypothetical search — here's the honest take AI Job Search is a 13K-star open-source tool that matches your resume to job postings using AI agents. After a week of testing it on a hypothetical job search, here is what works, what is rough, and who should actually use it. TL;DR : 4/5. If you are tired of copy-pasting your resume into dozens of forms, AI Job Search automates the matching and ranking. The agent design is the real highlight. What AI Job Search actually is AI Job Search is a Python tool (KhanZia/AI-Job-Search on GitHub) that: Scrapes job postings from any source (LinkedIn, Indeed, company career pages) Uses AI agents to match your resume against each posting Ranks matches by fit score, salary range, and recency Generates a personalized cover letter per matched job It is a CLI tool, not a hosted product. You run it locally, point it at a CSV of your resume details, and it spits out ranked matches. The repo has 13K stars and is actively maintained. The interesting design choice is that it uses a multi-agent pattern: one agent scrapes, another matches, another writes cover letters. Why I tried it: my own job search context I am not actively job hunting, but I review tools for saas.pet and I wanted to test AI Job Search against a realistic scenario: a hypothetical senior engineer with 8 years of experience looking for AI/ML roles at mid-sized SaaS companies. I built a fake resume (a "John Smith, Senior Python Engineer" profile), ran AI Job Search against 3 sources (LinkedIn public posts, Indeed API mock, Lever public job board), and compared the results against my own manual review of those same postings. What worked 1. The agent architecture is the real lesson. The tool is broken into clear single-responsibility agents: scraper, matcher, writer. Each agent has explicit inputs/outputs and can be swapped independently. If you have ever tried to build an agent that does everything end-to-end and watched it fail, this pattern is the antidote. 2. The matching is good, not perfect. On the test set, AI Job Search surfaced 8 of the 12 "actually a fit" jobs in the top 15 results (67% precision). My manual review found 12 fits. The AI did not find 4 — three of them because the resume did not mention a specific keyword the posting wanted, and one because the posting had a malformed salary field. The keyword gap is fixable with a resume-tuning pass; the malformed field is an upstream data quality issue. 3. Cover letter drafts are useful as first drafts. The cover letters are not publishable, but they are good starting points. They incorporate 2-3 specifics from the posting (mission, recent product launch, salary range) that I would have missed if writing cold. Saves 15-20 minutes per application. 4. Free, open-source, MIT licensed. You can read every line of code, modify it, run it on your own data without sending your resume to anyone. That is the right default for job search tooling. What did not work 1. Setup is non-trivial. I spent 2 hours getting the dependencies right, configuring API keys for OpenAI/Anthropic, and getting the scrapers to play nicely with rate limits. If you are not comfortable with Python and CLI tools, this is not a weekend project. 2. LinkedIn scraping is fragile. LinkedIn changes their HTML structure every few months and the scrapers break. The repo has a backlog of LinkedIn scraper bugs. If your primary job source is LinkedIn (it is for most people), you will spend time maintaining this. 3. No host / no UI. You are running Python scripts in a terminal. There is no web interface, no Slack notifications, no dashboard. If you want a tool that runs daily and emails you matches, you have to build that wrapper yourself. 4. Single-language resume parsing. The tool assumes English-language resumes. If your resume is in Chinese, Spanish, or any other language, the matching degrades significantly. Who should use AI Job Search Use it if : You are a Python developer comfortable with CLI tools You apply to 5+ jobs per week You have a non-encrypted, structured resume (no fancy PDF formatting) You care about resume privacy (it runs locally) Skip it if : You want a hosted, polished UI You apply to fewer than 3 jobs per week Your resume has heavy formatting (tables, multi-column layouts) You want a tool that "just works" without setup My verdict: 4/5 The agent design is the real takeaway, more than the tool itself. If you copy the scraper + matcher pattern into your own project, you have a template for any agent-driven workflow that ingests structured data and produces ranked matches. For the actual job-search use case, it works but is not polished. If you have 5+ hours to invest in setup and customization, it will save you time. If you want a hosted solution, try LoopCV or Sonara instead. Alex's Take I do not usually run CLI tools as a "review" because most of them have terrible UX, but AI Job Search earned its 4/5. The architecture is clean, the matching is real, and the code is honest. If you are a Python developer who is tired of applying to jobs manually and wants to own your job-search pipeline end-to-end (no SaaS, no resume upload to a third party), this is the only serious option I have found. The 13K stars are deserved. Read the full review on saas.pet : https://saas.pet/reviews/ai-job-search-review Tags : python, ai, agents, job-search, llm, opensource, automation Originally published on saas.pet — Alex Liu's hand-tested AI tools directory with 245+ reviews.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/saaspet/i-tested-ai-job-search-for-1-week-on-a-hypothetical-job-search-heres-the-honest-take-8p2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
