---
title: "AI agents need their own SSL. Here's why I built it."
slug: "ai-agents-need-their-own-ssl-heres-why-i-built-it"
author: "Edison Flores"
source: "devto_ai"
published: "Fri, 17 Jul 2026 03:11:26 +0000"
description: "In 1995, Netscape released SSL. The web didn't really take off commercially until then. Before SSL, you couldn't trust a website with your credit card. After..."
keywords: "atc, trust, agent, marketnow, agents, ssl, verify, card"
generated: "2026-07-17T03:16:27.693411"
---

# AI agents need their own SSL. Here's why I built it.

## Overview

In 1995, Netscape released SSL. The web didn't really take off commercially until then. Before SSL, you couldn't trust a website with your credit card. After SSL, e-commerce exploded. AI agents are at the same inflection point in 2026. Here's why. The problem Agents are starting to call each other autonomously. Each hop is a trust decision. But agents have no way to verify each other. Today, when Agent A calls Agent B: Is Agent B who it claims to be? No way to verify Has Agent B been audited for security? No standard Has Agent B's key been compromised? No revocation mechanism This is exactly where the web was in 1994. No SSL, no trust, no commerce. The analogy Web (1995) Agents (2026) HTTP (transport) A2A + MCP (transport) No HTTPS = can't trust No ATC = can't trust SSL certificate ATC Trust Card Certificate Authority MarketNow Sentinel CA Revocation list (CRL) /api/atc?action=verify What I built ATC (Agent Trust Card) — SSL certificates for AI agents. How it works Agent registers with MarketNow CA CA signs the agent's identity with Ed25519 Agent presents its ATC to other agents Other agents verify the signature with the CA public key If compromised, the CA revokes the ATC Real cryptography (not a mock) Ed25519 signatures (RFC 8032) CA private key in Vercel env var (never exposed) CA public key committed to public GitHub repo Every ATC persisted as signed JSON in _data/atc/ Anyone can verify signatures offline using crypto.verify Sentinel integration The ATC's trust score comes from Sentinel — the 8-layer security audit pipeline: L1.5: metadata checks L1.6: Semgrep + secrets + OSV L1.7: binary/malware detection L1.8: malware family signatures (Emotet, Cobalt Strike, etc.) The positioning MarketNow is not competing with A2A or MCP. It's the trust layer that sits on top: ATC (Trust Layer) <- MarketNow A2A / MCP (Transport Layer) <- Google / Anthropic HTTP / WebSocket (Network) <- Standard Every agent with an A2A card can have an ATC Trust Card. Every MCP skill can have a Sentinel Certificate. Complementary, not competitive. Try it # Get the CA public key curl https://marketnow.site/api/atc?action = ca-key # Issue a trust card for your agent curl -X POST https://marketnow.site/api/atc \ -H "Content-Type: application/json" \ -d '{"action":"issue","agent_id":"your.agent","public_key":"your-ed25519-pubkey"}' # Verify any agent's trust card curl "https://marketnow.site/api/atc?action=verify&card_id=ATC-2026-XXXXXXX" Live demo: https://marketnow.site/atc GitHub: https://github.com/edgarfloresguerra2011-a11y/marketnow The web needed SSL to become trustworthy enough for commerce. Agents need the same thing. This is it. — Edison Flores, AliceLabs LLC — marketnow.site

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/edison_flores_6d2cd381b13/ai-agents-need-their-own-ssl-heres-why-i-built-it-1njk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
