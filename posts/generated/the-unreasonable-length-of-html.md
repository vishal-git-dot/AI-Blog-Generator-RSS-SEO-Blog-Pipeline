---
title: "The Unreasonable Length of HTML"
slug: "the-unreasonable-length-of-html"
author: "Andrew Chemis"
source: "devto_webdev"
published: "Tue, 27 Oct 2026 21:36:00 +0000"
description: "Originally published on andrewchemis.dev . In May, Thariq Shihipar argued on the Claude Code blog that agents should hand people HTML instead of Markdown ( T..."
keywords: "lede, page, html, tokens, line, one, what, opus"
generated: "2026-10-27T22:00:01.243061"
---

# The Unreasonable Length of HTML

## Overview

Originally published on andrewchemis.dev . In May, Thariq Shihipar argued on the Claude Code blog that agents should hand people HTML instead of Markdown ( The unreasonable effectiveness of HTML ). He finds it "difficult to read a Markdown file of more than a hundred lines", and HTML carries the charts, diagrams and layouts Markdown can't. Then the line that sold me: "the chance of someone actually reading your spec, report, or PR writeup is much higher if it's in HTML." I agree with nearly all of it. Lede , which stands for Line-Encoded Document Engine, is what I built after reading it. What it cuts is the HTML itself; the model never writes any. His FAQ takes the obvious question head on ("Isn't it less efficient?") and grants that Markdown "often uses fewer tokens". Then it adds that "with the 1MM context window in Opus 4.7, the increased token usage is not really noticeable in the context window." About the window, he's right. Ten HTML pages come to about 51,000 tokens, which is 5% of a million. The tokens cost something everywhere else, though, and once I measured it I couldn't stop seeing it. What the extra tokens cost I had Haiku 5.5, Sonnet 5.5 and Opus 5.5 each write 60 pages twice from the same briefs, once as HTML and once as Lede, and counted output tokens with each model's own tokenizer. Mean output per page was 2,770 against 598 for Haiku, 4,501 against 625 for Sonnet, and 5,068 against 713 for Opus. Turned into what a reader of this blog would pay for: Cost: 1,000 pages from Opus 5.5 come to $101 of output tokens as HTML and $14 as Lede, at list price. On Sonnet 5.5 it's $45 against $6. That counts the page's own tokens only, not thinking or the reference the model reads first. Time: output arrives one token at a time. At an assumed 60 tokens a second, Opus takes about 84 seconds to finish an HTML page and about 12 to finish the Lede one. Context: the 51,000 tokens above against about 7,000, which is small in a million tokens but still gets re-read on every later turn of the session. Review: one benchmark page is 136 lines of HTML and 32 lines of Lede. The last one matters to me more than the bill. The HTML source of a page is mostly class names and style rules, so it runs well past the hundred lines he stops reading at, and it's the part I'd want to check before the page goes anywhere. A Lede file is content from the first line to the last, close enough to Markdown that a diff of it reads like a diff of a document. The rendered page is the same kind of page his post argues for. This is a whole one: @title Checkout, week 42 @subtitle p99 latency is back under its target after Tuesday's cache fix kpi p99 latency | 182 ms | -38% | good kpi Error rate | 0.12% | -0.4 pts | good kpi Deploys | 23 | +4 | neutral data lat = day,p99; Mon,240; Tue,296; Wed,190; Thu,184; Fri,182 chart line lat unit=ms target="200 SLO" mark="Tue cache fix" title="p99 latency by day" ! The cache now expires on write instead of on a timer, so a deploy no longer serves stale prices. That's 214 tokens. The compiler turns it into a 44 KB page with a title block, three metric tiles, a line chart with a dashed target and an event marker, a note, light and dark themes, a phone layout, and no script tag. There's a second reason I wanted the model out of the HTML. An agent that has read an email or a web page can be talked into writing a <script> tag or an image URL that leaks data, and a page is the obvious place for it. Lede has no way to say either. The compiler sanitizes its one escape hatch for raw HTML, refuses remote images unless asked, and writes a content security policy into every page. Five kinds of page, twelve examples The examples on the site come straight from his post. It sorts HTML artifacts into five kinds (specs and planning, code review, design and prototypes, reports and explainers, custom editing interfaces), and I gave Sonnet 5.5 twelve of his example prompts with nothing but the Lede reference. Each of the twelve examples on the site shows the request, the page and its full source, and says what the page couldn't do. An early release Lede is an early release, and it isn't as refined or hardened as it could be. It fails in a few areas, and where it loses on looks the site says so. On the benchmark task behind the 32-line figure, both blind judges preferred the HTML, for its projected trend line and grouped cards. Against each model's own HTML, Lede pages won or tied 60% of the time for Haiku, 22% for Opus and 10% for Sonnet. That table is on the front page under the heading "Cheaper and safer. Not yet as good as the best HTML." That is where it stands today, and there is a lot of room to improve and refine it. Using it I've been using Lede on my own projects, and it has earned its place as a way to put something in front of a person for approval: the page they read before they say yes. I'm also convinced it reduces token usage, and the benchmark above is the part of that I've measured. I'm excited to see how people use the format and to learn from it, including the uses I didn't plan for. The code is open source at github.com/lede-lang/lede . It installs two ways. From npm, @lede-lang/cli gives you the lede command. As a skill, the Claude plugin marketplace in the repository takes /plugin marketplace add lede-lang/lede and then /plugin install lede@lede . Try it The site is at ledelang.dev , the code is at github.com/lede-lang/lede , and the playground is the quickest way to try Lede. You type Lede on the left and the page appears on the right, so you can load one of the examples and change a line. If you have a page Lede can't draw, tell me. Each example lists what its page couldn't do, and that list is the roadmap.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/andrew_chemis/the-unreasonable-length-of-html-4e36

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
