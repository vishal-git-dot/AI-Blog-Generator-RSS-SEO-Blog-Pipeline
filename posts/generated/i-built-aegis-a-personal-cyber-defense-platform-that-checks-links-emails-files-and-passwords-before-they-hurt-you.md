---
title: "I built Aegis — a personal cyber defense platform that checks links, emails, files and passwords before they hurt you"
slug: "i-built-aegis-a-personal-cyber-defense-platform-that-checks-links-emails-files-and-passwords-before-they-hurt-you"
author: "Manoj Kumar Sharma"
source: "devto_python"
published: "Wed, 11 Nov 2026 13:42:35 +0000"
description: "Most people don't get hacked by nation-state attacks. They get hacked by a fake link in a text message, a convincing "verify your account" email, a malware a..."
keywords: "every, aegis, can, email, what, link, audit, platform"
generated: "2026-11-11T13:54:26.911789"
---

# I built Aegis — a personal cyber defense platform that checks links, emails, files and passwords before they hurt you

## Overview

Most people don't get hacked by nation-state attacks. They get hacked by a fake link in a text message, a convincing "verify your account" email, a malware attachment disguised as an invoice, or a password that already leaked in someone else's data breach. So I built Aegis — one place where a non-technical person can check each of those things before it hurts them, built to the same security standard it checks for. 🔗 Live demo: https://aegis-cyber-defense-platform.onrender.com (free hosting — first load after idle can take ~ a minute) 💻 Code: https://github.com/Manoj-2424150118/aegis-cyber-defense-platform What it does Smart Scan is the front door: paste anything — a link, an email, a suspicious message — and Aegis detects what it is and routes it to the right analyser automatically. Underneath are 10 tools , each answering a question a worried user actually asks: URL Analyser — "Is this link safe?" IP-instead-of-domain, look-alike domains, brand names hidden in paths, shorteners, credential bait. Email Analyser — "Is this email really from my bank?" SPF/DKIM/DMARC authentication, display-name mismatches, pressure language, and every link inside re-scored. File Scanner — "Is this attachment dangerous?" Content-vs-extension mismatches, double extensions like invoice.pdf.exe , hidden code. Files are examined in memory only — never opened, never run, never saved. Password Lab — offline guess-time estimation, common/repetitive pattern detection, secure generation. Breach Check — k-anonymity lookup: only the first five characters of the password's hash ever leave the machine. Secret Scanner — finds leaked API keys and credentials hiding in text and code. Encrypted Vault — AES-256-GCM with keys derived via Argon2id; the server stores only scrambled data, and tampering is detected automatically. Website Audit — any site graded A–F on HTTPS enforcement, security headers and cookie safety. Scam Message Checker — recognises Indian scam scripts: fake "digital arrest" threats, KYC/account-block warnings, OTP harvesting, Telegram task scams. Domain & TLS Checker — live grading of a domain's email-auth records, plus a real handshake to verify a site's certificate. The part most tools skip: the fix Every finding in every report ends with a Suggested Fix — concrete next steps written for the person holding the report. A test enforces that no finding can ship without one. A report should end the problem, not just name it. Since v2.0, a detection-engine "Signal" layer sits across the analysers, and public Trends show what people are actually checking. How it protects itself A security tool has to survive its own audit: The website-audit feature could once have been tricked into fetching internal network addresses (SSRF). It now resolves every target first, refuses private/internal addresses, and re-checks every redirect. Uploads are read in capped chunks and rejected exactly at the 10 MB limit — no memory-exhaustion via huge files. Login responses are timing-equalised with generic errors, so attackers can't enumerate real accounts. Accounts lock after repeated failures; login is rate-limited. Auth is Argon2id + JWT, and the platform ships the same strict security headers its own audit module grades other sites on. Aegis's self-audit score: 100, grade A . Testing is evidence, not decoration 186 automated tests , all passing, with CI and CodeQL green on every push. The canonical reference scores never drift between releases: the reference phishing link scores 85, the phishing email 100, the disguised program 40 — in every battery, on every version. A scripted QA battery (functional checks, attack suite, fuzzing, load) runs in a sandbox before deployment and against the live site after it. Stack FastAPI (Python) back end, React + TypeScript front end, single Docker container, Neon Postgres for storage (accounts and vault items survive redeploys — proven by test). Honest limits The demo runs on free hosting, which sleeps when idle — the first load can take about a minute. The code is identical to what a paid deployment would run. The checkers use explained heuristics, not magic. They can over- or under-flag at the margins — which is exactly why every finding shows its reasoning, so the user can judge. I'm Manoj Kumar Sharma, a cybersecurity & software professional (MCA, Manipal University Jaipur) based in Jaipur, India. I also run Scam Decoded , where I break down real Indian scams in short videos. If you try Aegis, I'd genuinely like to hear what it got right — and what it missed.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/manojthegeek/i-built-aegis-a-personal-cyber-defense-platform-that-checks-links-emails-files-and-passwords-3icm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
