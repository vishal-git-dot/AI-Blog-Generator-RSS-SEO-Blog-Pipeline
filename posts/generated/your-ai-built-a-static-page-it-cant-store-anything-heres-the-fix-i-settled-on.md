---
title: "Your AI built a static page. It can't store anything. Here's the fix I settled on."
slug: "your-ai-built-a-static-page-it-cant-store-anything-heres-the-fix-i-settled-on"
author: "Alex"
source: "devto_webdev"
published: "Fri, 10 Jul 2026 14:26:23 +0000"
description: "An AI can build you a full page in one prompt now. A leaderboard, an RSVP form, a little internal dashboard, a guestbook. It looks done. Then someone types t..."
keywords: "page, you, can, one, step, record, your, there"
generated: "2026-07-10T14:40:05.900484"
---

# Your AI built a static page. It can't store anything. Here's the fix I settled on.

## Overview

An AI can build you a full page in one prompt now. A leaderboard, an RSVP form, a little internal dashboard, a guestbook. It looks done. Then someone types their name into the form, hits submit, and nothing happens, because there is no server on the other end. It's just HTML sitting in a bucket. I kept hitting this. The generated page was 90% there and the last 10% was "wire up a database," which quietly means: stand up a backend, get API keys, handle auth, deploy it, keep it running. For a page you built in four minutes to share with a few people, that is a wildly lopsided amount of work. So most of these pages just stay read-only forever, or die in a folder. I build a hosting product for AI-generated sites (Thryvate, it's mine, disclosing up front), and this was the most common dead end people hit. So I spent a while on the storage half specifically. This post is about what I landed on and the tradeoffs, not a pitch. If you're wiring your own AI-built pages to Supabase or Firebase, some of this might save you a step. The constraint that shapes everything The page is static. The person who "wrote" it was an AI, prompted by someone who may not code. There is no build step they control, no env file, no place to safely put a secret. So the usual answer, "just add Supabase," breaks on step one: a public static page can't hold a service key, and asking a non-dev to set up row-level security is a non-starter. That pushes you to one design: the data layer has to be ambient. Present on every page with zero setup, no keys in the HTML, and the trust boundary enforced by the host, not by code the page ships. What I ended up with A single global the page can assume is there: // save a record; the collection is created on first write await window . THRYVATE . append ( ' rsvp ' , { name : ' Sam ' , coming : true }) // read it back const { records } = await window . THRYVATE . query ( ' rsvp ' , { order : ' desc ' , limit : 50 }) records . forEach ( r => console . log ( r . value . name , r . value . coming )) No fetch , no endpoint, no key. Each record comes back as { id, value, created, actor } and you read your own fields off record.value . The AI generating the page only has to know this one object exists, which turns out to be easy to teach it, because it's a tiny surface. A few decisions inside that were less obvious than they looked: Collections are created on first write. No migration, no schema step. The person prompting the AI never says "create a table." The first append to a new name makes it. This matters more than it sounds: every explicit setup step is a place a non-dev abandons. Identity is resolved by the host, and the page can't lie about it. There's a viewer() call that returns who is looking at the page, but only when the site is actually behind auth: const me = await window . THRYVATE . viewer () // private site, signed-in viewer -> { id: 'sam@work.com', kind: 'viewer' } // public or password-only -> { kind: 'anonymous' } The rule I enforce: if you want to show WHO did something (a high score, a clock-in, a comment), you call viewer() and write that identity into the record yourself. You cannot read back the actor on someone else's record to display it, that field is redacted in-page down to just a kind . Otherwise any guestbook becomes an email scraper. It took a couple of rewrites to get that boundary in the right place: useful enough to build a real leaderboard, locked down enough that a public page can't harvest who visited. "Current state" vs "full history" is one flag. Append-only logs are honest but annoying when you actually want the latest value per key (a settings row, the current status). So query takes latest: true and folds to the newest record per key field. You get an event log for free and a state view when you want it, without two different storage models. Where this is the wrong tool Being honest about the ceiling, because dev.to will (correctly) push back otherwise: It's records-in, records-out with equality filters and ordering. No joins, no server-side aggregation, no transactions. If you're building something with real relational needs, you want an actual backend and the setup cost that comes with it. The whole point is the page can't hold a secret, so anything requiring server-side trust (charging a card, calling a paid API with your key) is out of scope by design. That belongs on a server. It's tied to the page being hosted somewhere that provides the runtime. A raw file on S3 won't grow a window.THRYVATE on its own. The takeaway that isn't about my product If you're the one gluing AI-generated pages to a database, the thing worth stealing is the constraint, not the implementation: assume the page can hold no secrets and the person shipping it won't configure anything. Design the data layer so identity and access are enforced by the host and the page just calls a verb. Once you accept that, a lot of the "which BaaS" debate collapses, because most of them assume a setup step your actual user will never do. Curious how others are handling the storage half for vibe-coded pages. Are you defaulting people to Supabase and eating the setup, or avoiding stateful pages entirely?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/thryvate/your-ai-built-a-static-page-it-cant-store-anything-heres-the-fix-i-settled-on-3jlf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
