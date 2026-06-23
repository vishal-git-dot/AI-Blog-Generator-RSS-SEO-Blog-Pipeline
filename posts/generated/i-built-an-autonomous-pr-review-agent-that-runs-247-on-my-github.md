---
title: "I Built an Autonomous PR Review Agent That Runs 24/7 on My GitHub"
slug: "i-built-an-autonomous-pr-review-agent-that-runs-247-on-my-github"
author: "Hong Phuc"
source: "devto_python"
published: "Tue, 23 Jun 2026 09:27:06 +0000"
description: "A deep dive into setting up Hermes Agent with a GitHub App to auto-review every pull request across 22 repos — as a bot, not as me. The Problem I have 22 act..."
keywords: "review, agent, github, hermes, token, app, reviews, prs"
generated: "2026-06-23T09:53:37.256262"
---

# I Built an Autonomous PR Review Agent That Runs 24/7 on My GitHub

## Overview

A deep dive into setting up Hermes Agent with a GitHub App to auto-review every pull request across 22 repos — as a bot, not as me. The Problem I have 22 active repositories on GitHub. Pull requests pile up — dependabot bumps, feature branches, hotfixes. I'd either forget to review them, review them too late, or spend time on trivial lockfile changes that just need a quick approval. I wanted something that: Scans all my repos automatically Reviews PRs for real issues (security, performance, code quality) Posts comments under its own identity — not mine Notifies me via Telegram with a summary Lets me make the final merge decision The Architecture ┌─────────────────────────────────────────────┐ │ Cron: every 15 minutes │ └──────────────────┬──────────────────────────┘ │ ▼ ┌─────────────────────────────────────────────┐ │ scan-prs.py (GraphQL batch query) │ │ → Fetches all open PRs in 1 API call │ │ → Filters by head SHA (skip reviewed) │ │ → Parallel diff fetch (5 workers) │ └──────────────────┬──────────────────────────┘ │ ▼ ┌─────────────────────────────────────────────┐ │ Hermes Agent (LLM review) │ │ → Reads diff for security, quality, tests │ │ → Writes review to temp file │ │ → Posts via GitHub API as hermes-agent[bot] │ │ → Marks reviewed in state.json │ └──────────────────┬──────────────────────────┘ │ ▼ ┌─────────────────────────────────────────────┐ │ Telegram notification │ │ → Summary of all reviews │ │ → Verdict per PR (approve/changes/comment) │ │ → Silent if nothing new │ └─────────────────────────────────────────────┘ Why a GitHub App, Not a Bot Account I initially considered creating a separate GitHub account for the agent. But the community consensus — and my own research — pointed to GitHub Apps as the right choice: Bot Account GitHub App Identity Looks like a random user Proper [bot] suffix with verified badge Auth PAT (broad access, long-lived) Installation token (scoped, auto-expires in 1 hour) Rate limits Shares your personal limit Has its own 5000/hr per installation Security PAT until manually revoked Fresh token each run, minimal permissions Scalability One account, one identity Install on unlimited repos/orgs The GitHub App only requests pull_requests: write and contents: read . If compromised, the blast radius is minimal. The Token Flow The auth dance happens automatically every run: JWT signing — Python's PyJWT signs a JWT with the app's private key (RS256), valid for 10 minutes Installation token — Exchange JWT for a short-lived installation token via GitHub's API Token caching — Cached in .token-cache.json with 5-minute buffer before expiry API call — Use the token to POST a review via GitHub's REST API No long-lived secrets on disk. The private key is the only persistent credential, stored at ~/.hermes/credentials/hermes-app.pem with chmod 600 . What It Reviews The agent checks every diff for: Security — hardcoded secrets, SQL injection, shell=True with user input, auth bypass Performance — N+1 queries, unbounded loops, memory leaks Code quality — naming, duplication, error handling, missing types Tests — missing test coverage for new behavior File permissions — accidental 644→755 mode changes on non-scripts Dependabot lockfile bumps get a quick approval. Real code changes get a thorough review. Real Output Here are actual reviews posted by the agent: VideoMakerBot #1 — user: root in docker-compose: 🤖 Hermes Agent Review Verdict: REQUEST CHANGES user: root in docker-compose is a security risk. Document why it is needed or remove it. 29 files changed from 644 to 755. Most are .py/.json files that don't need +x. skills #7 — new agent spec: 🤖 Hermes Agent Review Verdict: COMMENT (Approve) Adds a new landing-page-updater agent to the release-manager skill. Purely additive — new file only. astro-js-starter-template #14 — dependabot bump: 🤖 Hermes Agent Review Verdict: COMMENT (Approve) Patch bump: diff 5.2.0 → 5.2.2. Minimal lockfile change. Safe to merge. The Stack Component Tool Purpose Scheduler Hermes cron (every 15m) Triggers the scan Scanner Python + GitHub GraphQL Batch-fetches all open PRs Auth PyJWT + GitHub App API Fresh installation tokens Reviewer LLM via Hermes Agent Reads diffs, writes reviews Poster GitHub REST API Posts as hermes-agent[bot] Notifier Telegram Delivers summary to me State state.json Tracks reviewed PRs by SHA Total cost: ~$0.01-0.05 per review cycle (depending on diff size and model). At 15-minute intervals, that's roughly $1-5/month. Human-in-the-Loop The agent reviews and comments, but I merge . The Telegram notification gives me the verdict so I can decide what to act on. No auto-merge, no silent failures. This is the pattern I've found works best for AI agents in development workflows: let them handle the tedious analysis, keep humans in the decision seat. Files Everything lives in ~/.hermes/scripts/pr-review/ : pr-review/ ├── scan-prs.py # GraphQL scanner + diff fetcher ├── post-review.py # GitHub App auth + review poster ├── gh-app-auth.py # JWT signing + token management ├── state.json # Reviewed PR tracking └── .token-cache.json # Cached installation token The skill is documented at ~/.hermes/skills/github/pr-auto-review/SKILL.md . What's Next Webhook mode — for real-time reviews (needs public endpoint on my VM) Auto-merge — for approved dependabot PRs (with user confirmation) Multi-agent review — Hermes reviews → Codex suggests fixes → I approve This post was written and published by Hermes Agent — the same system that reviews my PRs. The irony is not lost on me.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hongphuc5497/i-built-an-autonomous-pr-review-agent-that-runs-247-on-my-github-38l9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
