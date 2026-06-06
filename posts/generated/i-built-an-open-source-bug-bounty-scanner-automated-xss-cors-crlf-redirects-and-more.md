---
title: "I built an open-source Bug Bounty scanner — automated XSS, CORS, CRLF, redirects and more"
slug: "i-built-an-open-source-bug-bounty-scanner-automated-xss-cors-crlf-redirects-and-more"
author: "N0wzy8"
source: "devto_python"
published: "Sat, 06 Jun 2026 19:01:22 +0000"
description: "Been using this privately for a while and finally decided to open-source it. It crawls your target, fuzzes parameters for XSS/CRLF/Open Redirect, checks CORS..."
keywords: "open, bug, bounty, scanner, xss, cors, crlf, redirect"
generated: "2026-06-06T19:40:03.724780"
---

# I built an open-source Bug Bounty scanner — automated XSS, CORS, CRLF, redirects and more

## Overview

Been using this privately for a while and finally decided to open-source it. It crawls your target, fuzzes parameters for XSS/CRLF/Open Redirect, checks CORS misconfigurations, missing security headers, sensitive file exposure, subdomain enumeration, and more — all multi-threaded. Drops a clean .txt report when it's done. Built in Python, one-liner install. Would love feedback from the community — still a lot I want to add. 🙏 n0wzy8 / N0wzy8-BugBountyScanner Fast multi-threaded bug bounty scanner featuring XSS, Open Redirect, CRLF, CORS, Clickjacking, Recon and Sensitive File Discovery. ⚡ N0wzy8 Bug Bounty Scanner Fast, multi-threaded reconnaissance and vulnerability scanner engineered for efficient bug bounty hunting. Screenshot 🚀 Features 🔍 Reconnaissance & Intelligence Module Description Subdomain Enumeration Discovers hidden assets and expands attack surface Technology Fingerprinting Identifies backend stacks, CMS, and server software Sensitive File Discovery Scans for backups, .env files, and exposed configs Directory Listing Detection Flags misconfigured directories leaking server structure Information Leak Detection Extracts emails, internal IPs, and risky HTML comments 🛡️ Vulnerability Assessment Module Description Reflected XSS Scans parameters for cross-site scripting vulnerabilities Open Redirect Validates unsafe parameter-based redirections CRLF Injection Checks for HTTP response splitting potential CORS Misconfiguration Detects overly permissive cross-origin policies Clickjacking & Headers Analyzes missing security headers ( X-Frame-Options , CSP , etc.) Cookie Security Flags missing HttpOnly , Secure , and SameSite attributes Dangerous HTTP Methods Tests for active PUT , DELETE , or TRACE methods Rate Limiting Evaluates server … View on GitHub

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/n0wzy8/i-built-an-open-source-bug-bounty-scanner-automated-xss-cors-crlf-redirects-and-more-2dd7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
