---
title: "Show HN Post — ComplianceLayer"
slug: "show-hn-post-compliancelayer"
author: "ComplianceLayer"
source: "devto_python"
published: "Tue, 30 Jun 2026 14:00:01 +0000"
description: "Show HN Post — ComplianceLayer Target: news.ycombinator.com Timing: Tuesday-Thursday, 9-11 AM EST (peak HN traffic) Goal: Early adopters, API developers, sec..."
keywords: "scanning, compliancelayer, security, api, scan, port, grade, domain"
generated: "2026-06-30T14:30:32.340206"
---

# Show HN Post — ComplianceLayer

## Overview

Show HN Post — ComplianceLayer Target: news.ycombinator.com Timing: Tuesday-Thursday, 9-11 AM EST (peak HN traffic) Goal: Early adopters, API developers, security-minded engineers who will try it and share it Post Title: Show HN: ComplianceLayer – External security scoring API for any domain (DNS, SSL, ports, headers) Hey HN, I built ComplianceLayer after getting frustrated with two things: Enterprise security scoring tools (SecurityScorecard, BitSight) that cost $20K+/year and are built for procurement teams, not engineers Security audits that live in PDFs nobody reads ComplianceLayer is an API that scans any domain and returns a structured security score across four categories: DNS/Email — SPF, DMARC, DKIM, CAA, DNSSEC SSL/TLS — cert validity, chain issues, expiry, protocol versions Open ports — TCP scan for exposed services (RDP, SSH, SMB, common web ports) HTTP headers — HSTS, CSP, X-Frame-Options, CORS, referrer policy Each check returns a score (0-100), grade (A-F), and specific findings with remediation steps. Use cases so far: MSPs running automated security checks across their client base SaaS companies checking vendor/supplier posture before onboarding Security consultants generating client-facing reports programmatically Developers building security dashboards Quick example: curl -H "Authorization: Bearer sk_..." \ https://api.compliancelayer.net/v1/scan \ -d '{"domain": "example.com"}' Returns: { "domain" : "example.com" , "overall_score" : 74 , "grade" : "C" , "categories" : { "dns_email" : { "score" : 65 , "grade" : "D" , "issues" : [ "No DMARC policy" , "No DKIM" ]}, "ssl_tls" : { "score" : 98 , "grade" : "A" , "issues" : []}, "open_ports" : { "score" : 80 , "grade" : "B" , "issues" : [ "Port 22 open" ]}, "http_headers" : { "score" : 55 , "grade" : "F" , "issues" : [ "No HSTS" , "No CSP" , "No X-Frame-Options" ]} } } What I found scanning 200 random SMB domains: 59% have no DMARC policy (fully spoofable) 29% serve HTTP without redirect 18% have SSH exposed directly to internet 7% have RDP exposed to internet (the scariest one) Only 23% have HSTS enabled Pricing: Free tier (10 scans/day), then $99/mo for 250 scans. API key in 30 seconds, no sales call. Happy to answer questions about the tech stack, scanning methodology, or how I handle rate limiting / false positives on the port scanning side. compliancelayer.net Anticipated HN Questions & Answers "How do you handle false positives on port scanning?" TCP SYN scan with 3-attempt verification before flagging. We also check against common CDN/proxy IP ranges and flag those differently. Still imperfect — external port scanning has inherent limitations. We're clear about that in the docs. "What's the legal situation with scanning domains you don't own?" We scan only publicly accessible services — same as what any internet-connected system can observe. No exploitation, no intrusion. We follow responsible disclosure norms and have a clear AUP. Scanning a domain you don't own for malicious purposes violates our ToS. "How does this compare to Shodan?" Shodan is a search engine for internet-connected devices — it indexes what it finds. ComplianceLayer is a scoring/reporting layer that combines multiple data sources (DNS lookups, SSL checks, port scans, header analysis) and gives you a structured grade optimized for reporting and monitoring, not raw discovery. "What's the tech stack?" Python/FastAPI backend, PostgreSQL, Redis for rate limiting and caching. Port scanning via asyncio with custom TCP implementation (not nmap — too heavy for API use). Hosted on Hetzner. "Can I self-host this?" Not currently. It's SaaS. The port scanning infrastructure in particular is complex to self-host correctly (IP reputation, rate limiting, legal compliance per jurisdiction). "What's the scan speed?" Full scan (all 4 categories) typically completes in 8-15 seconds. DNS/SSL/Headers are fast; port scanning is the bottleneck. We scan ~100 common ports. Launch Day Plan Post at 9 AM Tuesday (best HN traffic window) Monitor comments — respond to everything within 30 min for first 2 hours Don't be defensive about criticism — thank them, take notes Have the API actually working flawlessly before posting (non-negotiable) Free tier must be no-friction (email + instant key, no credit card) Success Metrics Good: 50 points, 20 comments, top 30 of the day Great: 100+ points, 50+ comments, front page Home run: Front page + feature in "Best of HN" digest Last updated: 2026-03-07 Built by ComplianceLayer — scan any domain for security compliance in seconds. Get your free API key .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/compliancelayer/show-hn-post-compliancelayer-2d9k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
