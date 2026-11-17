---
title: "An embedded form or survey builder still ships skip logic and scoring in the browser"
slug: "an-embedded-form-or-survey-builder-still-ships-skip-logic-and-scoring-in-the-browser"
author: "VEILVM"
source: "devto_webdev"
published: "Tue, 17 Nov 2026 01:43:14 +0000"
description: "Form and survey builders often embed a runtime in the customer’s page: a script tag, a webpack chunk, or a Web Component. The pitch is instant skip logic, li..."
keywords: "form, definition, you, not, answers, embed, engine, score"
generated: "2026-11-17T01:46:24.813674"
---

# An embedded form or survey builder still ships skip logic and scoring in the browser

## Overview

Form and survey builders often embed a runtime in the customer’s page: a script tag, a webpack chunk, or a Web Component. The pitch is instant skip logic, live validation, calculated scores, and no round-trip between questions. That runtime is JavaScript, and it usually includes the definition of the form itself. If the value of your product is the engine — branching, scoring, price quotes, qualification — then that engine is in the browser. This article is about what an embedded form runtime actually exposes, what must be re-checked on the server, and how to protect the engine you still have to ship. The definition and the engine travel together A typical embed looks like this: export function mountSurvey ( el , definition ) { let answers = { } ; function next ( ) { const q = pickNext ( definition , answers ) ; // your interesting part if ( ! q ) return finish ( score ( definition , answers ) ) ; renderQuestion ( el , q ) ; } el . addEventListener ( "submit" , ( e ) => { answers [ e . qId ] = e . value ; next ( ) ; } ) ; next ( ) ; } function pickNext ( definition , answers ) { // skip logic, AB branches, "disqualify if …", paid-tier questions return definition . rules . find ( ( rule ) => match ( rule , answers ) ) ; } function score ( definition , answers ) { return definition . weights . reduce ( ( n , w ) => n + w . points * !! answers [ w . id ] , 0 ) ; } A visitor who loads the embed can: Read the runtime chunk and the form definition from the Network panel. Recover skip rules, hidden questions, disqualification thresholds, and scoring weights. Call score or pickNext from the console with crafted answers. Lift the engine into another product, or fill the official form with a script that already knows the winning path. Minifying the runtime will rename pickNext . It will not hide "disqualify", a distinctive weight, or a question you thought was secret because the UI had not reached it yet. grep -R -nE "disqualify|weights|pickNext" dist/embed | head Hidden questions are not confidential This is the part teams regret after a launch. A hiring screen, a pricing quiz, a medical-style symptom tree, or a lead-qualification form sometimes puts the "real" criteria in client-side skip logic: reject if salary is below a number, skip the expensive plan if the company size is small, show a deluxe upsell only when the score is high. Assume anyone can read those criteria. If they must stay unpublished — interview answer keys, fraud signals, medical cutoffs, unpublished prices — do not put them in the embed. Fetch the next question from the server, or at least re-evaluate the result on the server before it means anything. Submitted answers should also go to your server in raw form. A client-computed score: 97 is a suggestion. What the embed should still do A snappy runtime is still the right UX for most marketing forms. Validation, animations, save-and-resume, and non-sensitive branching can stay in the browser. For the proprietary engine: Re-check qualification, prices, and pass/fail on the server before you create a lead, a charge, or a "you passed" state. Minify the embed as usual. Extract pickNext / score (or the compiler that turns a form JSON into those functions) and apply a real protection pass — identifier renaming and string tables as a floor, VM-style protection if wholesale reuse of the engine is the risk you care about. Keep unpublished answer keys and fraud signals off the client. Keep production source maps off the public CDN. A JS VM obfuscator compiles that function to a custom bytecode and ships a small interpreter. Pretty-printing the chunk no longer reconstructs the original scoring routine; you get bytecode and a dispatcher. That is slower than a thin JSON walker, which is why you protect the engine, not the entire form UI. VEILVM is a browser-based JSVMP workspace you can point at one extracted function before you wire protection into CI. Protection raises the cost of casual inspection and wholesale reuse. It does not make a public form definition a secret, and it does not replace a server-side score. Checklist [ ] Qualification, prices, and pass/fail are re-evaluated on the server. A client-computed score cannot grant the result by itself. [ ] Unpublished keys, fraud signals, and confidential cutoffs are not in the embed. [ ] The open UI kit is left alone; only your skip or scoring engine is a candidate for protection. [ ] Distinctive rule strings and weights in the public chunk are ones you accept being public, or they live behind a stronger pass. [ ] Production source maps are not downloadable from the CDN. [ ] End-to-end tests submit a fixture form against the minified (and, if applicable, protected) production embed, including a path the UI would not show. If you want to try VM protection on a single extracted function, VEILVM runs in the browser with no sign-up: 3 free runs a day, up to 5 KB per file (resets at 00:00 UTC). A free account raises the input limit to 30 KB. Pro is $9/month or $79/year and adds an API so the protection step can run in CI. Standard requests are processed in memory and are not written to logs. Start at https://vm.ldvmp.com .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/veilvm/an-embedded-form-or-survey-builder-still-ships-skip-logic-and-scoring-in-the-browser-889

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
