---
title: "Four open-source tools for AI in e-commerce, and what building them taught me"
slug: "four-open-source-tools-for-ai-in-e-commerce-and-what-building-them-taught-me"
author: "Naser Sadrmanesh"
source: "devto_ai"
published: "Fri, 30 Oct 2026 22:01:31 +0000"
description: "I'm Naser Sadrmanesh, an AI product engineer and founder working on online stores. Over the last months I turned the tools I kept rebuilding for clients into..."
keywords: "every, can, one, you, search, store, mcp, agent"
generated: "2026-10-30T22:07:19.231278"
---

# Four open-source tools for AI in e-commerce, and what building them taught me

## Overview

I'm Naser Sadrmanesh, an AI product engineer and founder working on online stores. Over the last months I turned the tools I kept rebuilding for clients into four open-source projects. They are small, MIT licensed, and each one exists because a real project needed it. This post explains what each does and the design decision behind it. 1. llm-search-eval: is the new search actually better? Every store eventually changes its search: keyword to vectors, a new reranker, query rewriting, synonyms. The usual offline check is to run 50 queries, compare nDCG, and ship if the number went up. That check fails in predictable ways. Labels go stale. Gold labels were written for the old system. A new retriever surfaces products nobody labeled, so they count as misses and the new system looks worse than it is. Small deltas are noise. +2% on 50 queries is often chance. One LLM judge is one opinion. If you fill gaps with a model, someone has to check it against people. llm-search-eval builds one label pool per run: your gold labels first, LLM judgments only for the gaps, and every system scored on the same pool. You can run a panel of judges and see Cohen's kappa, Fleiss' kappa and Krippendorff's alpha between them, plus how each judge agrees with your human labels. Every comparison gets a paired randomization test and bootstrap confidence intervals. Pairwise A/B judging runs in both orders to cancel position bias. The part teams like most is boring: an estimate command predicts the number of judge calls, tokens and cost before you run anything, and budgets stop a run before it overspends. A GitHub Action posts the result as a pull request comment and fails the check when ranking regresses. pip install llm-search-eval It has no runtime dependencies and works with any OpenAI-compatible endpoint, including local models. There is a sample report and a live demo on Hugging Face that runs in the browser with no API keys. 2. woocommerce-mcp: let an agent touch the store, carefully The Model Context Protocol makes it easy to give an AI agent tools. For a live store, the hard question is not "can it call the API" but "what happens when it is wrong". woocommerce-mcp answers that with a few rules: Stores are read-only until you allow writes. Every write tool first returns a preview of the exact REST request. It is applied only when the tool is called again with confirm: true . Every write attempt, applied or refused, goes to an audit log . Customer data can be redacted , and tools can be allowed or denied by pattern, for example hiding delete_* . Within those rules it covers 47 tools: catalog search, orders and fulfillment with tracking, refunds, bulk price and stock changes, coupons and scheduled sales, customer segments, shipping and tax, webhooks, and sales analytics. It runs over stdio or streamable HTTP with bearer tokens or OAuth 2.0, and it is on npm, GHCR, Docker Hub and the official MCP Registry. You can browse every tool and its schema in the tool explorer . npx -y @sadrmanesh/woocommerce-mcp The lesson: the preview and confirm loop costs one extra call, and it is the single feature store owners ask about first. 3. commerce-agent-skills: teach agents the domain, not just the syntax Coding agents write plausible checkout code that misses things an experienced e-commerce engineer would never miss: idempotent webhooks, refunds that do not match the original currency unit, stock that oversells across warehouses, inaccessible product pages. commerce-agent-skills is a library of 29 skills written in plain Markdown, each with rules, reference notes, gotchas, a verification checklist and evaluation fixtures. Topics include Stripe and Iranian payment gateways, returns and refunds, inventory across warehouses, B2B pricing, catalog migration, WCAG 2.2 accessibility, Core Web Vitals, WooCommerce and Shopify development, and MCP store tooling. A small scorer checks answers against the fixtures, so a skill change can be measured instead of guessed. npx @sadrmanesh/commerce-agent-skills init The skills are tool neutral: they are just files in .agents/skills/ that any agent can read. They are also published as a Hugging Face dataset . 4. persian-rag: retrieval that respects the language Persian breaks naive pipelines quietly. Arabic and Persian Yeh and Kaf look identical but are different code points. Half-spaces come and go. Three digit systems appear in one document. PDFs often store Persian in reversed order. Common words have several accepted spellings. persian-rag handles those first, then provides a normal RAG toolkit: loaders, chunking, BM25 plus dense retrieval with rank fusion, a spelling-variant query rewriter, reranking, answers with citations resolved to source spans, chat memory, evaluation, a FastAPI server and a Docker image. The core install is pure Python with no dependencies. On its small bundled benchmark, the rewriter raises BM25 Hit@1 on misspelled queries from 0.58 to 0.83. That set is tiny, so I treat it as a regression test rather than a claim. You can try it in the live demo , and the benchmark is on Hugging Face . pip install persian-rag What ties them together All four follow the same habits: docs sites for every project, CI on every change, tagged releases that publish to PyPI, npm, GHCR, Docker Hub or the MCP Registry automatically, a GitLab mirror, and honest limits written in the README. None of them is finished. If one of them solves a problem you have, I'd be glad to hear about it, and issues and pull requests are welcome. Site: https://sadrmanesh.github.io/ GitHub: https://github.com/sadrmanesh

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sadrmanesh/four-open-source-tools-for-ai-in-e-commerce-and-what-building-them-taught-me-5abl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
