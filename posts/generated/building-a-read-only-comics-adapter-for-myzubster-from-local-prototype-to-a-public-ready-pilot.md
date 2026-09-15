---
title: "Building a Read-Only Comics Adapter for MyZubster: From Local Prototype to a Public-Ready Pilot"
slug: "building-a-read-only-comics-adapter-for-myzubster-from-local-prototype-to-a-public-ready-pilot"
author: "Nicola Lorenzini"
source: "devto_python"
published: "Tue, 15 Sep 2026 15:30:33 +0000"
description: "Building a Read-Only Comics Adapter for MyZubster: From Local Prototype to a Public-Ready Pilot Over the last few days, I’ve been working on a small but conc..."
keywords: "api, comic, adapter, public, pilot, candidate, only, comics"
generated: "2026-09-15T16:40:33.688074"
---

# Building a Read-Only Comics Adapter for MyZubster: From Local Prototype to a Public-Ready Pilot

## Overview

Building a Read-Only Comics Adapter for MyZubster: From Local Prototype to a Public-Ready Pilot Over the last few days, I’ve been working on a small but concrete experiment inside the MyZubster ecosystem : turning my N4K48 × MyZubster comic series into a structured catalog that can be queried by Zorgax . The goal wasn't to jump directly into minting NFTs. Instead, I wanted to build and verify the pieces that should come before that: catalog data, API access, rights status, an explicit NFT candidate, and a clean boundary between what is already working and what still needs validation. The pilot The project currently contains three comic panels: Dall’idea software al metaverso Il software prende forma Verso Neon Plaza They are exposed through a read-only catalog adapter. The first panel is currently marked as: NFT_CANDIDATE PROPOSED_FOR_REVIEW rights_status: TO_VERIFY This distinction matters. NFT_CANDIDATE does not mean that an NFT has been minted. At this stage there is no contract address, token ID or transaction hash associated with the comic. Those fields remain empty until an actual on-chain operation can be performed and independently verified. A small API for Zorgax The pilot exposes a few deliberately simple endpoints: GET /api/comics GET /api/comics/{comic_id} POST /api/zorgax/ask The Zorgax adapter supports four explicit actions: gallery detail candidate next_steps For example: { "question" : "Quale candidata NFT?" , "action" : "candidate" } returns the proposed candidate from the catalog. The important architectural decision here is that the adapter is read-only . It cannot mint NFTs, modify the catalog, access wallets or execute payments. It simply provides a controlled interface between the catalog and the assistant layer. Testing the complete local flow I rebuilt the environment using Docker Compose and tested the API from PowerShell. The API container reached: healthy 0.0.0.0:5000->5000 Then I manually verified the main flow. Gallery gallery returned all three N4K48 comic panels. Detail detail correctly returned the complete record for: n4k48-comic-001 NFT candidate candidate returned only: n4k48-comic-001 Dall’idea software al metaverso with: nft_status: NFT_CANDIDATE selection_status: PROPOSED_FOR_REVIEW rights_status: TO_VERIFY transaction_hash: null Next steps The adapter also correctly reports that provenance/authorizations and the public Zorgax connection still need verification, and that the service itself does not execute minting. So the local happy path is now working: request ↓ gallery ↓ detail ↓ comic asset ↓ candidate ↓ rights / on-chain status Preparing the adapter for a public environment The next problem was important. The API worked on: http://localhost:5000 but we don't want a public Zorgax service to depend on — or expose — my personal PC. So I changed the adapter to accept its public base URL through an environment variable: NICOLA_COMICS_BASE_URL Without that variable, the API returns relative URLs: /api/comics/n4k48-comic-001 With a configured public base URL, it can instead return: https://pilot.example.org/api/comics/n4k48-comic-001 No production URL is hardcoded into the application. No authentication tokens or secrets are stored in the repository. An interesting Docker issue During the test I set: $ env : NICOLA_COMICS_BASE_URL = "https://pilot.example.org" but the API continued returning: "api_base_url" : null The Python code was working correctly. The problem was Docker Compose: the environment variable from the host wasn't being forwarded to the API container. The fix was to explicitly pass it: environment : NICOLA_COMICS_BASE_URL : " ${NICOLA_COMICS_BASE_URL:-}" After rebuilding the containers, the same API request returned: "api_base_url" : "https://pilot.example.org" and: "detail_url" : "https://pilot.example.org/api/comics/n4k48-comic-001" That gave us a useful intermediate verification: the adapter is still running locally, but its URL-generation behavior is ready to be configured for a separate public hosting environment. What is verified — and what isn't At this point we have verified: ✓ Docker deployment locally ✓ comic catalog ✓ gallery ✓ comic detail ✓ NFT candidate selection ✓ next-step reporting ✓ configurable API base URL ✓ Docker environment propagation ✓ read-only integration boundary Still pending: ○ real public HTTPS deployment ○ public Zorgax → pilot connection ○ hosting authentication/authorization ○ rights verification ○ on-chain transaction ○ NFT mint verification Keeping those two lists separate is one of the most important parts of the experiment. A prototype shouldn't claim capabilities simply because they're part of the roadmap. The next milestone The next test will move the same adapter from the local environment to a reachable HTTPS endpoint. Then the goal is to verify the complete public flow: User request ↓ Public Zorgax ↓ Nicola Comics adapter ↓ Gallery ↓ Comic detail/card ↓ Published image ↓ NFT candidate ↓ Rights / verified on-chain status The adapter remains read-only during this phase. Only after rights and the blockchain step have actually been completed and verified should the project move from NFT candidate to a real minted asset. For me, that's the interesting part of this pilot: not simply putting a comic “on Web3”, but building a small, reproducible path where every transition has an explicit and verifiable state. Nicola / N4K48 opensource #python #docker #api #web3 #ai #buildinpublic

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/n4k48/building-a-read-only-comics-adapter-for-myzubster-from-local-prototype-to-a-public-ready-pilot-2jif

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
