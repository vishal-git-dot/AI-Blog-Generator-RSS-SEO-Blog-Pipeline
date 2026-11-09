---
title: "I checked every quote Claude's deep research cited. One wasn't what the source said."
slug: "i-checked-every-quote-claudes-deep-research-cited-one-wasnt-what-the-source-said"
author: "Andri Darnius"
source: "devto_python"
published: "Mon, 09 Nov 2026 05:15:37 +0000"
description: "AI research tools are good at sounding sourced. Every paragraph ends with a link, every key point sits in quotation marks. I wanted to know how often those q..."
keywords: "research, page, quote, quotes, every, one, agent, model"
generated: "2026-11-09T05:39:49.712034"
---

# I checked every quote Claude's deep research cited. One wasn't what the source said.

## Overview

AI research tools are good at sounding sourced. Every paragraph ends with a link, every key point sits in quotation marks. I wanted to know how often those quotes are actually on the page they link to, so I checked them with code instead of trusting the model. The setup I asked Claude's deep-research skill a technical question: "SQLite WAL vs rollback journal for concurrent writes." It came back with a solid report: four parallel researchers, 30 sources, and 21 direct quotes. Then I pulled out every quote and the link that followed it, fetched each page, and checked whether the quoted words were really there. Matching ignored case, punctuation, line breaks and PDF formatting, but never the words themselves. The result 20 of 21 quotes were exact. One wasn't. The report quotes the SQLite forum as saying: "a VM has its own memory space" The thread never says that. The closest sentence is: "QEMU provides a private virtual memory space for its VM" The meaning is close. The quotation marks are wrong. It's a paraphrase presented as a quote, and nothing in the research process checks for that. To be fair to deep research: its report was excellent and broader than mine (more on that below). One soft misquote in 21 isn't a scandal. But it's the kind of error that survives review, because it sounds right. It's not just one tool I hit the same problem in my own research agent. In one run on HTTP/3 performance, the agent quoted two research papers: It wrote "advantageous **for * users that move."* The paper says "advantageous **in case of * users that move."* It wrote "QUIC's removal of HOL blocking…" The paper says "QUIC's removal of HOL * (head-of-line)** blocking…"* Both are close enough that a reader, or the model re-reading its own notes, would accept them. Why this happens The cause I found most surprising: when an agent "reads" a page, it often doesn't see the page. Many agent web-fetch tools pass the page through a smaller model and return a summary or an answer to a prompt. The agent then quotes from that summary. Quotes drift. PDFs are worse: many fetch tools can't extract them at all, so the agent quotes from memory or from a secondary source. Asking the model to double-check doesn't fix this. It checks against the same summary. What worked Two changes, both boring: Quote from the exact page text. Before quoting, fetch the raw page (or extract the PDF's text) and copy from that, not from a summary. Check every quote with code. After research, fetch each cited page once and match each quote word for word, as whole words, in order. A quote is either on the page or it isn't. When a quote isn't on the cited page, check the other pages in the same research. Often the quote is real but pinned to the wrong source. In one run the checker found a real SQLite quote attributed to wal.html that actually lives on pragma.html , and corrected the link instead of dropping it. Does the checker itself work? I stress-tested it: 40 real verified quotes, 30 of them deliberately damaged (two words swapped, a "not" removed, a number changed, the wrong page cited) plus 5 invented quotes and 10 left intact. It classified 45 of 45 correctly. PDFs needed their own fixes. Footnote numbers glue onto words ("users1 ."), words split across lines ("trans-\nactions"), and ligatures replace letter pairs. Each one caused a false "not found" until handled. What it costs On the same SQLite question, my pipeline's research phase used 78,517 tokens on Claude Haiku . Deep research's four researchers used 278,826 on the main model . That's about 28% of the tokens, on a cheaper model. The trade-off is real: deep research found things mine didn't, including a SQLite WAL corruption bug fixed in 3.51.3 (March 2026) and corruption across Docker Desktop VM boundaries. Broader search costs more. Checking quotes costs almost nothing, since it's a script, not a model. Try it I packaged this as an agent skill called Quoteproof : a 5-angle research pipeline that quotes from exact page text and checks every quote before writing the report. The report ends with an audit line: quotes checked, verified, corrected, dropped. Free, MIT: Quoteproof Community checks quotes from web pages: git clone https://github.com/andre-arc/Quoteproof-Community.git ~/.claude/skills/quoteproof-community Pro: adds PDFs and research papers, exact-text quoting, and wrong-page detection: Agensi . All the data behind this post, including the deep research report and every quote checked: github.com/andre-arc/Quoteproof Tested with Claude Code. One limit to know: it proves a quote exists on the page, not that the page is right . I'm looking for reviewers So far every test is mine. I'd like researchers and programmers to try it on their own questions and tell me what happened, especially when it fails. Install the free edition (one git clone , above). Ask your agent to research something you know well, so you can judge the answer. Share the result in the comments here, or through the review form : what you researched, the audit line at the end of the report, anything it caught, and anything it got wrong. I'll read every response and publish a follow-up with what reviewers found, good and bad. With your permission, I'll quote you. Disclosure: I built Quoteproof and earn from sales of the Pro edition. The Agensi link is my referral link.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/andre-arc/i-checked-every-quote-claudes-deep-research-cited-one-wasnt-what-the-source-said-5ae7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
