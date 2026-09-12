---
title: "Paid DMARC and MTA-STS audit APIs for AI agents (x402, 2026-09-12)"
slug: "paid-dmarc-and-mta-sts-audit-apis-for-ai-agents-x402-2026-09-12"
author: "HAL GOBVAN"
source: "devto_python"
published: "Sat, 12 Sep 2026 19:09:20 +0000"
description: "Two new paid email-security audit APIs Built on top of the same URL-metadata x402 stack as /api/extract , /api/summarize , /api/keywords , /api/seo-audit , a..."
keywords: "api, dmarc, sts, mta, domain, agents, email, policy"
generated: "2026-09-12T20:23:47.692079"
---

# Paid DMARC and MTA-STS audit APIs for AI agents (x402, 2026-09-12)

## Overview

Two new paid email-security audit APIs Built on top of the same URL-metadata x402 stack as /api/extract , /api/summarize , /api/keywords , /api/seo-audit , and /api/wayback-diff , two new sub-cent endpoints are now live for AI agents doing email-deliverability audits and outbound-email TLS-enforcement reviews . Endpoint Purpose Price /api/dmarc DMARC policy lookup + compliance evaluator $0.0005 USDC /api/mta-sts MTA-STS policy discovery + compliance evaluator $0.0005 USDC Both reachable through the same Cloudflare-tunneled public gateway: https://epson-rpm-america-satisfy.trycloudflare.com/api/dmarc?domain=microsoft.com https://epson-rpm-america-satisfy.trycloudflare.com/api/mta-sts?domain=microsoft.com Payment is settled in USDC on Base mainnet via the open pay.openfacilitator.io facilitator. No API key, no signup, no monthly minimum — every call is $0.0005. Why DMARC for AI agents DMARC is the canonical email-impersonation defense. Knowing the policy of a domain is a prerequisite to: Outbound deliverability — Gmail, Yahoo, and Microsoft all require DMARC alignment on bulk senders. Brand protection — measuring how strict a target's policy is before mentioning them in a phishing report. ESP onboarding — agents helping customers choose between Postmark / SES / SendGrid / Mailgun need to know if their customer's existing record will silently ruin inbox placement. M&A due diligence — a buyer of an email-heavy business wants to know if the seller's DMARC posture will break after migration. The endpoint queries _dmarc.<domain> over Cloudflare DNS-over-HTTPS, parses every standard tag ( v=DMARC1 , p , sp , pct , adkim , aspf , rua , ruf , fo , ri ), and returns a weighted compliance score 0..100 plus an A-F grade and a list of findings. Why MTA-STS for AI agents MTA-STS (RFC 8461) is the SMTP-side counterpart to DMARC: it forces opportunistic TLS to be actually enforced between mail servers. The endpoint queries _mta-sts.<domain> and fetches https://mta-sts.<domain>/.well-known/mta-sts.json , then validates version / mode / mx / max_age and returns the same score + grade + findings format. Full catalog 43 paid endpoints across four pricing tiers — discovery at /.well-known/x402 , /llms.txt , /openapi.json . Listed on agent402.tools Smart Order Router and 402index.io .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hal_gobvan_16a285d49bda97/paid-dmarc-and-mta-sts-audit-apis-for-ai-agents-x402-2026-09-12-5b99

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
