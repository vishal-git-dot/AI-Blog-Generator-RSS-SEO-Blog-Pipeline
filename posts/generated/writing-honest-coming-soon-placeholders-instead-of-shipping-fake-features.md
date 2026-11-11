---
title: "Writing honest 'coming soon' placeholders instead of shipping fake features"
slug: "writing-honest-coming-soon-placeholders-instead-of-shipping-fake-features"
author: "Mobeen Ahmed"
source: "devto_webdev"
published: "Wed, 11 Nov 2026 13:49:53 +0000"
description: "Every tool site eventually has a feature that is not ready yet. On ramrom.io, that feature is Douyin. The download provider I looked at returns playlists, no..."
keywords: "not, douyin, visitor, does, fake, site, button, page"
generated: "2026-11-11T13:54:26.914647"
---

# Writing honest 'coming soon' placeholders instead of shipping fake features

## Overview

Every tool site eventually has a feature that is not ready yet. On ramrom.io, that feature is Douyin. The download provider I looked at returns playlists, not files, so there is no honest way to offer a Douyin download today. I had three options: hide the platform entirely, ship a button that pretends to work, or put up a plain "coming soon" note. I chose the third, and I think it is the only one that respects the visitor. Why a fake button is the worst option A button that does nothing useful is not a placeholder, it is a lie. The visitor pastes their link, taps download, and waits. Then one of two things happens: either an error appears and the visitor assumes the whole site is broken, or the page pretends to work and the visitor waits for a file that will never arrive. Both outcomes cost trust, and trust is the only thing a free tool site really owns. I would rather a visitor left thinking "this site does not do Douyin yet" than "this site does not work". There is a second cost that is easier to miss. A dead button teaches me nothing. If the button is honest, I can watch how many people look for Douyin and decide whether it is worth buying a proper API. If the button is fake, the clicks it gets are meaningless, because some of them were people who would have bounced anyway once they found out it was fake. What an honest placeholder actually says My rule is simple: a placeholder must answer three questions in plain words. What is this? When will it be ready? What can you do instead? If it cannot answer the first one honestly, it does not go on the page. For Douyin, that looks like this: the card says Douyin, it says "coming soon", and it says the download is not available yet because no provider I have found returns real files for it. It links to nothing and it has no download button. There is no spinner, no fake progress bar, and no "try again later" message that implies the feature exists and is just having a bad day. A visitor who reads it knows exactly where they stand in about three seconds. The wording matters more than the design. "Coming soon" on its own is vague, so I add the reason in one short line. I do not write "we are working hard on it" when I am not actively working on it. The honest sentence is "not available yet" — boring, but true. The same rule applies to the code behind it An honest placeholder is also easier to maintain. The Douyin card is a static block of HTML with no JavaScript wired to it and no API call behind it. There is no disabled button pretending to be a feature, no endpoint that returns a fake error, and no half-built form waiting for someone to finish it. When the day comes that a real Douyin provider exists, I add the real tool. Until then, the page contains nothing I would have to rip out or apologise for. This is the same instinct behind the rest of the site. If a provider is down, the page says so instead of spinning forever. If a video is private or deleted, the message says that instead of blaming the visitor's link. The placeholder is just the same habit applied before a feature exists rather than after it breaks. The temptation to ship the fake version I understand why people ship fake buttons. A full-looking homepage feels more complete, and a grid with one greyed-out card feels unfinished. But the grid is not the product. The product is the download that actually works, and a visitor who uses the TikTok downloader successfully does not care that Douyin is greyed out. A visitor who taps a fake Douyin button and gets nothing will not come back to try the TikTok one. There is also a search engine angle, though it was not my main reason. A page that promises a feature and delivers an error is thin content. A page that says plainly what it does and does not do is a page I can stand behind when a reviewer reads it. My AdSense application was already rejected once for low value content, so I have learned to prefer honest, finished pages over pages that look bigger than they are. The checklist I use now Before any new platform or feature goes on the site, I ask four questions: Can I deliver the real result today, with a provider I have tested? If not, does the placeholder say so in plain words, with the reason? Is there a working alternative on the same page the visitor can use instead? Is there anything on the page that looks clickable but does nothing? If the answer to the fourth question is yes, the placeholder is not ready. A link that goes nowhere is worse than no link at all. Shipping less, honestly, has been one of the better decisions I made on this site. Visitors get a tool that does what it says, and I get a site I do not have to explain away. When Douyin becomes possible, I will build it properly and the placeholder will disappear. Until then, it stays honest.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mobeenahmedgondal/writing-honest-coming-soon-placeholders-instead-of-shipping-fake-features-4kk1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
