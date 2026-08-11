---
title: "I Built an Anonymous Hosting Platform Powered by Monero — Now I Don't Know Whether to Sell It or Save It"
slug: "i-built-an-anonymous-hosting-platform-powered-by-monero-now-i-dont-know-whether-to-sell-it-or-save-it"
author: "Saila Mo"
source: "devto_webdev"
published: "Tue, 11 Aug 2026 13:12:01 +0000"
description: "I need to be honest with you. This is not a tutorial. This is not a success story. This is the story of something I built with genuine passion — and the dile..."
keywords: "what, built, not, something, don, privacy, you, proxy"
generated: "2026-08-11T13:17:02.098593"
---

# I Built an Anonymous Hosting Platform Powered by Monero — Now I Don't Know Whether to Sell It or Save It

## Overview

I need to be honest with you. This is not a tutorial. This is not a success story. This is the story of something I built with genuine passion — and the dilemma I now face about what to do with it. How It Started I'm a developer. I care deeply about privacy. Not in a paranoid way — in a principled way. I believe that anonymity is a right, not a feature. That people should be able to buy infrastructure without handing over their name, email, and payment history to a third party. So I built it myself. XMRHOST.CC — an anonymous VPS and Proxy hosting platform where you pay with Monero, Bitcoin, or Litecoin — directly on-chain, no middlemen, no swap services. No account. No email. No logs. Just an Order ID. Payment confirmed → server deployed in seconds. Fully automated, end to end. What I Actually Built I want to be technically honest here, because the devil is in the details. The payment system: XMR verified via xmrchain.net (viewkey-based, 4 confirmations) BTC/LTC verified via Blockcypher API (3 confirmations) Live exchange rates via CoinGecko — always accurate USD pricing 2% tolerance to protect against rate slippage during confirmation Duplicate TX protection — same hash cannot pay two orders Race condition protection — DB-level locking on confirmation The automation: Customer picks a plan, pays with crypto Payment verified on-chain automatically Server or proxy deployed via Servury Reseller API Credentials delivered instantly The owner does nothing The stack: PHP + SQLite + Vanilla JS — no framework, no npm, runs on any basic VPS Zero dependencies that can break or need maintenance Admin panel with full order overview, Telegram alerts on every paid order and deploy fail, manual override for edge cases What customers get: VPS: full management panel — start/stop/restart, noVNC browser console, root password reset, OS reinstall (Debian 12, Ubuntu 24, CentOS 10, Windows Server 2022/2025) Proxy: Datacenter IPv4 + Residential rotating — US/CA/FR/UK/NL — HTTP & SOCKS5 No account. No email. No registration. Just an Order ID. "We can't share what we don't have." No account. No email. No logs. Deploy a server or proxy in under 60 seconds. Pay with XMR, BTC, or LTC — direct on-chain, no middleman. It Went Live. And Then Something Unexpected Happened. I posted a few listings in niche privacy communities. That was the only "marketing" I did. And then orders started coming in. From where exactly? I'm not always sure. Privacy networks. .onion communities. Word of mouth in places I'll never fully trace. The point is: I didn't ask for them. They just came. The domain now ranks organically on Google for "XMR Host" and related privacy hosting searches. Zero paid ads. Ever. The platform has been running for months. It works. It earns. It requires almost no maintenance. The First Article That Changed Everything A few weeks ago I stumbled upon this article: 👉 What I Learned From Selling a Side Project Online It resonated deeply. I recognized myself in it — the builder who put everything into something, then ran out of steam. So I listed XMRHOST.CC for sale: BitcoinTalk listing XmrBazaar listing (XMR multisig escrow available) SideProjectors (pending approval) Asking price: $2,8- - 3k — domain included, Servury API account, all crypto wallets, full documentation, full handover support. Then The Second Article Hit Me Just when I thought I had made up my mind, I found this: 👉 How to Find Funding for Your Project And suddenly a different question appeared: What if I don't have to sell it? What if the community believes in this enough to help me finish it? The Roadmap I Never Had Resources To Build Here's what XMRHOST could become with proper funding and time: Tor .onion mirror — footer already prepared, just needs deployment ZEC Shielded + LTC MWEB payments — true privacy coins HD Wallet — auto address generation per order, no address reuse ISP Proxies — residential ISP-grade proxies, highest anonymity tier eSIM — anonymous mobile connectivity, pay with XMR Proxy IP whitelist management Upgrade Plan flow — VPS upgrades from dashboard Bandwidth topup for residential proxies The foundation is solid. The automation is real. The niche is wide open. The Dilemma So here I am. I built something I'm proud of. Something that runs itself. Something that serves a real need in a world that increasingly surveils everything. But I don't have the time or the money to take it where it deserves to go. Option A: Sell it. $2,6-3k. Someone else builds the dream. Option B: Find funding. Keep it. Build the perfect privacy infrastructure myself. I genuinely don't know which path is right. Why I'm Writing This Not to advertise. Not to pitch. I'm writing this because I know this community understands what it means to build something real — alone, without funding, without a team — and then face the impossible question of what to do with it. If you've been here, I'd love to hear from you. And if you're curious about the project itself — it's live at xmrhost.cc . Whatever happens next — I built this with genuine care. And that part I don't regret. Built with PHP + SQLite + Vanilla JS. Powered by Monero. No accounts. No logs. No compromise.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sailame_71c0b61b5d32/i-built-an-anonymous-hosting-platform-powered-by-monero-now-i-dont-know-whether-to-sell-it-or-438i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
