---
title: "Four of our twelve guide pages have an h1 their title tag could not afford"
slug: "four-of-our-twelve-guide-pages-have-an-h1-their-title-tag-could-not-afford"
author: "Daniel Pertu"
source: "devto_webdev"
published: "Sun, 18 Oct 2026 10:40:41 +0000"
description: "CogniPrep has two guide clusters built on one metadata type: the interview guides under /interview/<slug> and the assessment centre guides under /assessment-..."
keywords: "title, exercise, assessment, string, page, characters, which, you"
generated: "2026-10-18T10:43:33.397574"
---

# Four of our twelve guide pages have an h1 their title tag could not afford

## Overview

CogniPrep has two guide clusters built on one metadata type: the interview guides under /interview/<slug> and the assessment centre guides under /assessment-centre-practice/<slug> . Twelve pages, one GuideMeta , and four of its fields are names for the same page. export interface GuideMeta { slug : string ; /** Short label for breadcrumbs and sibling pills. */ label : string ; /** Page <h1>, also used as the hub card title. */ h1 : string ; /** * The <title>, before the root layout appends ' | CogniPrep' (12 characters). * Keep this at 48 characters or fewer so the rendered title stays under 60. */ metaTitle : string ; /** Under 160 characters. */ metaDescription : string ; /** Shorter variant for Open Graph and Twitter, which truncate harder. */ ogTitle : string ; keywords : string []; /** Blurb on the parent hub's guide card. */ cardBlurb : string ; } Four name fields looks like over-provisioning. It is not, and the interesting part is which pages prove it. The 12 character tax The root layout sets a title template, so every page's metaTitle is rendered twelve characters longer than it is written: title : { template : ' %s | CogniPrep ' } Google truncates a title in the results at somewhere around 60 characters depending on pixel width. Twelve of those are spent before the page gets a say, which is why the comment on the field names 48 rather than 60. A writer tidying up a title has no reason to know that, so the budget is written where the string is. Eight of the twelve reuse their h1 verbatim Open a guide page and run this in the console: console . log ({ title : document . title , h1 : document . querySelector ( ' h1 ' ). textContent . trim (), og : document . querySelector ( ' meta[property="og:title"] ' ). content , }); You get the same sentence three times: title : " Common Interview Questions and Answers | CogniPrep" h1 : " Common Interview Questions and Answers" og : " Common Interview Questions and Answers" That is the deliberate default. Somebody searches the phrase, the result says it, and the first line on the page is the same sentence, so nothing about the click needs re-justifying. Eight of the twelve guides are like this, and for all eight the h1 happens to fit inside 48 characters, so reuse costs nothing. The four that could not The other four are the assessment centre exercise guides, and in every one the h1 is the longest field in the entry: page h1 title og h1 text presentation-exercise 49 55 35 Presentation Exercise Tips for Assessment Centres written-exercise 44 52 39 Written Exercise Tips for Assessment Centres role-play-exercise 43 51 32 Role Play Exercise Tips for Assessment Days group-exercise 42 50 37 Group Exercise Tips for Assessment Centres The title column already includes the twelve character suffix. Reusing the 49 character h1 on the presentation guide as its title would have rendered 61 characters, which is exactly the length that gets cut off mid-word in a search result. So the entry carries two headlines: { slug : ' presentation-exercise ' , label : ' Presentation Exercise ' , h1 : ' Presentation Exercise Tips for Assessment Centres ' , metaTitle : ' Presentation Exercise at Assessment Centres ' , ogTitle : ' Assessment Centre Presentation Tips ' , ... } Three strings, and the differences are not arbitrary. The h1 is written for somebody already on the page, so it reads as a promise about the content. The metaTitle drops "Tips for" and uses "at", buying six characters without losing the keyword or its position near the front. The ogTitle is shorter again and reordered, because a link preview in a chat app or a social card truncates harder and earlier than a search result does, and what survives there needs the category first. Compare this with our can-you-cheat cluster , which has 56 pages and only one title field, because every h1 in it is short enough to serve as both. The lesson from putting the two side by side is not "always split your titles" or "always reuse them". It is that the field count follows the length of the longest headline in your data, and until you have measured that you are guessing. The cheap way to find out which group you are in Four lines over the registry, no browser needed: for ( const g of [... INTERVIEW_GUIDES , ... AC_GUIDES ]) { const rendered = g . metaTitle . length + ' | CogniPrep ' . length ; if ( rendered > 60 || g . h1 !== g . metaTitle ) console . log ( g . slug , g . h1 . length , rendered ); } The first condition is the one that must never print anything. The second is informational: it tells you which pages are carrying a second headline, which is the set you should actually be reviewing when you change the template string. Ours is four pages, and a fifth would have to be a deliberate decision rather than something nobody noticed.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/daniel_pertu/four-of-our-twelve-guide-pages-have-an-h1-their-title-tag-could-not-afford-53l7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
