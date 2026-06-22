---
title: "Add Security Scanning to Any GitHub Repo in 3 Lines of YAML"
slug: "add-security-scanning-to-any-github-repo-in-3-lines-of-yaml"
author: "Moon sehwan"
source: "devto_webdev"
published: "Mon, 22 Jun 2026 04:38:44 +0000"
description: "AI writes code fast. It also writes the same security bugs, over and over. We scanned 10 popular vibe-coded repos (10k–100k ⭐) last week. Every single one ha..."
keywords: "patterns, github, return, scan, api, key, add, security"
generated: "2026-06-22T05:02:45.250987"
---

# Add Security Scanning to Any GitHub Repo in 3 Lines of YAML

## Overview

AI writes code fast. It also writes the same security bugs, over and over. We scanned 10 popular vibe-coded repos (10k–100k ⭐) last week. Every single one had at least one critical issue that passed code review undetected. The most common pattern: # AI generates this constantly def save_user ( data ): return { " status " : " saved " } # No actual DB write. Ever. async def fetch_profile ( user_id ): return profile # async keyword, zero await calls These aren't typos. They're structural patterns that emerge when LLMs write code — and standard linters miss all of them. We built a scanner that catches them AINAScan / VibeGuard — AST-based, deterministic, no LLM involved. 48 patterns across 9 languages. And now it's a GitHub Action. Add it to your repo in 3 lines # .github/workflows/vibeguard.yml name : Security Scan on : [ pull_request ] jobs : scan : runs-on : ubuntu-latest steps : - uses : actions/checkout@v4 - uses : Moonsehwan/aina-vibeguard-action@v1 with : api-key : ${{ secrets.VIBEGUARD_KEY }} Add VIBEGUARD_KEY → Settings → Secrets → Actions → New secret Use vg_free_test as the value (free promo key, valid until June 24). That's it. Every PR now gets scanned. Critical issues fail the check automatically. What it actually catches Security patterns (33) SQL injection via f-strings Path traversal from unvalidated input Command injection in subprocess calls Hardcoded API keys and passwords SSRF, XSS, eval/exec risks Vibe-coding patterns (15) — unique to AINAScan Pattern What it means MISSING_WRITE save_user() with no INSERT/UPDATE anywhere FAKE_ASYNC async def with zero await calls STUB_SKELETON Function body is just return {} DEAD_CALL_RESULT Calls 3 modules, ignores all return values INPUT_OUTPUT_DISCONNECTED Parameters don't affect the return value These patterns are in no other scanner. They exist because AI coding assistants repeat them constantly. Real finding from last week Scanned serena (25k ⭐) — a popular AI coding assistant: [ BLOCK ] COMMAND_INJECTION agent . py : 1222 subprocess . Popen ( cmd , shell = True ) → any config value can execute arbitrary shell commands Found in 3 seconds. Missed by the maintainers. Use the output in your agent workflow The API returns structured JSON, so AI agents can auto-fix: result = requests . post ( " https://pleasing-transformation-production-90c2.up.railway.app/v1/scan " , headers = { " X-API-Key " : " vg_free_test " }, files = { " file " : open ( " app.py " , " rb " )} ). json () # Pass to Claude/GPT for auto-fix if not result [ " passed " ]: prompt = f " Fix these issues: { result [ ' issues ' ] } " fixed = agent . generate ( prompt ) Try it now Free key (until June 24): vg_free_test curl -X POST https://pleasing-transformation-production-90c2.up.railway.app/v1/scan \ -H "X-API-Key: vg_free_test" \ -F "file=@your_file.py" GitHub Action: Moonsehwan/aina-vibeguard-action Full docs: github.com/Moonsehwan/aina-scan Would love to hear what patterns you're seeing in your AI-generated code. Drop them in the comments — if it's a real pattern we're not catching, we'll add it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/_55c9ae90dd2b13bd715f5/add-security-scanning-to-any-github-repo-in-3-lines-of-yaml-1l81

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
