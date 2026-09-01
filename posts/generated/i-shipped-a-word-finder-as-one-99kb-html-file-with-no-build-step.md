---
title: "I shipped a word finder as one 99KB HTML file with no build step"
slug: "i-shipped-a-word-finder-as-one-99kb-html-file-with-no-build-step"
author: "The 5 Letter Words"
source: "devto_webdev"
published: "Tue, 01 Sep 2026 20:37:49 +0000"
description: "I have a Next.js word finder site. It has an App Router, a Turbopack build, a VPS behind Cloudflare, and a PM2 process to babysit. It works fine. Then I want..."
keywords: "not, word, list, one, file, you, words, filter"
generated: "2026-09-01T20:51:44.953431"
---

# I shipped a word finder as one 99KB HTML file with no build step

## Overview

I have a Next.js word finder site. It has an App Router, a Turbopack build, a VPS behind Cloudflare, and a PM2 process to babysit. It works fine. Then I wanted a small version of the same tool on GitHub Pages, and I did not want any of that. What I ended up with is one index.html. 99KB. Word list, styles and logic all inside it. No build step, no bundler, no dependencies, no network calls after the page loads. You double-click the file and it works. Here is what that actually involved, including the bug that would have made the whole thing quietly useless. The word list problem A five-letter word finder needs a word list. The current Wordle word list has 14,855 entries, which is the first thing that pushes you toward a build step: fetch a JSON file, or import a module, or generate a bundle. I tried the module route first. The page did await import("./words-db.js") and scanned the exports for arrays of five-letter strings: js const db = await import("./words-db.js"); const found = []; (function scan(value, depth) { if (depth > 2 || !value) return; if (Array.isArray(value)) { const words = value.filter(w => typeof w === "string" && /^[a-zA-Z]{5}$/.test(w) ); if (words.length) found.push(words); } else if (typeof value === "object") { for (const k in value) scan(value[k], depth + 1); } })(db, 0); That is a nice trick when you want to drop in an existing module without editing it. It also has a catch that bit me immediately: browsers block module imports over file://. Opening the file directly gets you a CORS error. You need a local server just to look at your own page. So I inlined the list instead. Not as an array literal, which spends two bytes per word on quotes and commas, but as one string: js var WORD_BLOB = aahed aalii aapas aargh ... ; var LIST = WORD_BLOB.split(/\s+/).filter(w => w.length === 5); 14,855 words, six bytes each including the separator, about 89KB. The array-literal version would have been closer to 120KB for exactly the same data. The split runs once at load and takes no measurable time. The whole file is 99KB uncompressed, and GitHub Pages serves it gzipped at a fraction of that. No build step, and it works off the file system. The bug that mattered The filter itself is three conditions. Green letters must match by position, yellow letters must appear somewhere, grey letters must not appear: js return LIST.filter(function (w) { for (var i = 0; i < 5; i++) { if (pattern[i] && w[i] !== pattern[i]) return false; } for (var a = 0; a < include.length; a++) { if (w.indexOf(include[a]) === -1) return false; } for (var b = 0; b < exclude.length; b++) { if (w.indexOf(exclude[b]) !== -1) return false; } return true; }); Straightforward. And completely broken in one very common case. Think about what a user actually types. They know C is in position one, so C goes in the green boxes. Then they list the letters they have ruled out and, half asleep, include C in there too, because they typed a word with a second C that came back grey. Now the filter is being asked for words that start with C and contain no C. It returns nothing. Not an error, not a warning, just an empty result that looks like a legitimate "no words match". That is the worst kind of bug. It does not crash, it does not log, and the user concludes your tool is bad rather than that their input was contradictory. The fix is four lines before the filter runs: js // A letter that is green or yellow can never also be excluded. var keep = {}; pattern.forEach(function (c) { if (c) keep[c] = 1; }); include.forEach(function (c) { keep[c] = 1; }); exclude = exclude.filter(function (c) { return !keep[c]; }); Positive information wins. If a letter is known to be in the word, drop it from the exclusion list and carry on. This is also correct behaviour in real Wordle, not just a convenience. A grey tile does not mean "this letter is absent". It means "there are no more of this letter than you have already been shown". A word with one C will show your second C as grey. So a letter being both green and grey in the same board is normal, not user error. I still show a hint on the empty state pointing at the yellow and grey boxes, because there are other ways to type a contradiction. But the common one is now handled silently, which is where it belongs. What I would not do this way This is not an argument against build tools. The main site has one for good reasons: hundreds of pages, image optimisation, content collections, incremental builds. The single-file approach works here because the constraints are unusually kind. One page. One dataset that changes maybe twice a year. No auth, no state to persist, no server. When those hold, every layer you add is a layer that can break at 2am for reasons unrelated to your code. When they do not hold, you will rebuild all of it badly and by hand. The result One file, on GitHub Pages, no CI, no deploy pipeline. Editing it means opening it in a text editor. Deploying it means committing. The word list came from the public Wordle list mirrored at tabatkins/wordle-list. The tool is at the5letterwords.github.io , source in the same repo. If you go looking at the code, the four-line guard is the interesting part. Everything else is a filter over an array.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/the5letterwords/i-shipped-a-word-finder-as-one-99kb-html-file-with-no-build-step-4cli

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
