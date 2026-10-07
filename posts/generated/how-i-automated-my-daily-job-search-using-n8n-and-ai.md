---
title: "How I Automated My Daily Job Search Using n8n and AI 🤖💼"
slug: "how-i-automated-my-daily-job-search-using-n8n-and-ai"
author: "srivalli jalla"
source: "devto_ai"
published: "Wed, 07 Oct 2026 05:13:18 +0000"
description: "Searching for jobs manually every single day can quickly become repetitive and inefficient. You scroll through multiple job boards, read dense job descriptio..."
keywords: "rss, job, workflow, gmail, daily, key, node, python"
generated: "2026-10-07T05:20:33.235833"
---

# How I Automated My Daily Job Search Using n8n and AI 🤖💼

## Overview

Searching for jobs manually every single day can quickly become repetitive and inefficient. You scroll through multiple job boards, read dense job descriptions, filter out irrelevant postings, and track links manually. To streamline this process, I built a zero-cost, automated workflow using n8n and AI that automatically aggregates job postings from Wellfound, extracts key details using an LLM, and delivers structured daily updates straight to my Gmail inbox. Here is a breakdown of how the automation works and how you can replicate it. 🛠️ The Architecture & Workflow The entire automation is powered by an n8n workflow composed of six core nodes: [ Schedule Trigger ] ──► [ RSS Read ] ──► [ Limit ] ──► [ AI Model ] ──► [ If Condition ] ──► [ Gmail Node ] Schedule Trigger ⏰ Set to run automatically on a daily schedule (e.g., every morning at 9:00 AM) so job updates are ready before starting the workday. RSS Read 📡 Connects directly to Wellfound’s RSS feed to fetch real-time listing updates for specific roles (e.g., Python Developer, Cloud AI Engineer). Limit Node 🚦 Restricts the maximum number of items processed per run to keep daily alerts focused on the newest listings. Message a Model (AI Node) 🧠 Passes raw feed content into an LLM (such as OpenAI GPT or Google Gemini) with a tailored prompt to extract structured metadata: 📌 Role Title 🏢 Company / Source 📍 Work Mode / Location 💰 Stipend / Salary 🛠️ Key Tech Stack 📝 Brief Summary 🔗 Direct Apply URL If Condition 🔀 Evaluates whether valid job listings were processed before proceeding, preventing empty or corrupted emails from being sent. Send a Message (Gmail) 📧 Uses n8n’s Gmail node to dispatch clean, emoji-formatted summaries directly to my inbox. 📬 What the Output Looks Like Instead of raw RSS data or unstructured links, the output arrives as a clean, easy-to-read summary directly in Gmail: 🎯 New Role: Python Developer (Cloud AI Platform) at NGRS 📌 Role: Python Developer (Cloud AI Platform) 🏢 Company: NGRS (via Wellfound) 📍 Work Mode: New York City 🛠️ Key Tech Stack: Python, Cloud, AI 📝 Brief Summary: NGRS is hiring a Python Developer to contribute to their Cloud AI Platform based in New York City. 🔗 Link to Apply: [Click Here to Apply] 🚀 How to Set Up Your Own Version If you want to run this workflow yourself: Clone the Repository: Download the open-source workflow file from my GitHub repository: 👉 GitHub Repository[cite: 6] Import into n8n: Open your n8n instance, navigate to Workflows, and select Import from File. Configure Credentials: Link your Gmail OAuth2 credentials. Add an API key for your preferred AI provider in the Message a Model node. Customize the RSS Feed: Replace the RSS URL with your custom Wellfound query feed. Activate: Switch the workflow toggle to Active. 💡 Key Takeaways Time Saved: Eliminates 15–20 minutes of daily manual searching and reading. Structured Data: Raw RSS feeds are transformed into scannable summaries. Low Code / No Code: Built completely using n8n visual workflows without needing complex server infrastructure. Have you built similar job search or RSS automation workflows? Let's connect in the comments! 👇

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/srivalli_jalla_70b9119ecd/how-i-automated-my-daily-job-search-using-n8n-and-ai-479p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
