---
title: "When I tell Cursor "just make it work", this rule stops the shortcut from rotting"
slug: "when-i-tell-cursor-just-make-it-work-this-rule-stops-the-shortcut-from-rotting"
author: "ShipStack"
source: "devto_webdev"
published: "Mon, 16 Nov 2026 15:12:13 +0000"
description: "Cursor is very obedient about the word "quick." If I say "just make it work," it will often make something work by skipping the parts that are annoying: the ..."
keywords: "not, debt, when, say, cursor, rule, cut, what"
generated: "2026-11-16T15:22:11.708073"
---

# When I tell Cursor "just make it work", this rule stops the shortcut from rotting

## Overview

Cursor is very obedient about the word "quick." If I say "just make it work," it will often make something work by skipping the parts that are annoying: the ownership check, the empty state, the test, the rollback. The feature looks done. A week later I cannot remember which of those shortcuts is load-bearing, and one of them is in a path real users hit. I got tired of cleaning that up, so I stopped treating "MVP" as a quality setting. I treat it as a scope setting. The rule lives in .cursor/rules/ and I pull it in when I hear myself say "hack this in," "just for now," or "we'll tidy it later." Cut scope, not quality The useful question is not "how do we write this faster?" It is "what can we not build yet?" I tell the agent to cut these first: A settings screen. A named constant at the top of the file is enough for one flag. An admin panel. A script or a SQL snippet in /scripts will do. Teams and roles. Stay on a single user, but keep userId on every record so you can add teams later without a rewrite. A custom design system. Use the component library already in the repo. Edge-case polish. A clear error message is enough. I also tell it what it is not allowed to cut, even in a hurry: Auth and ownership checks. Input validation at API boundaries. Idempotency for payments and webhooks. Error logging. A console.error with context is better than a silent catch . Types on function signatures that cross a module boundary. That split is the whole point. "Quick" means the settings UI can wait. It does not mean the webhook can be processed twice. Shortcuts have to be greppable Some debt is still worth taking. When I take it, I want to find it again on a Monday morning, not rediscover it in production. I use one comment format: // DEBT(solo): <what's missing> — <when it'll hurt> — <how to fix> // DEBT(solo): no pagination — breaks past ~1k items — add a cursor param to /api/items Three rules around it: The marker has to say what is missing, when it will hurt, and how to fix it. "TODO later" is not a plan. At most three new DEBT(solo) markers in one change. If I need a fourth, the slice is too big and the agent should say so, not keep going. grep -R "DEBT(solo)" is the backlog. If it is not greppable, it does not count. This is boring on purpose. The alternative is a vague "we'll refactor this" that nobody can search for. Prototype and production are different folders If I say "prototype" or "throwaway," I want it in /sandbox or on a separate branch, and I want the agent to say out loud that it is not production-safe. If a real user can reach it, it is production. The "never cut" list applies. Putting a prototype in the same routes as checkout, "just to see," is how a labelled shortcut becomes an unlabelled incident. A compact rule you can paste Save this as .cursor/rules/60-mvp-not-sloppy.mdc . It is not always-on. It should attach when the task is a prototype, a spike, or a deliberately small first version. --- description: "Use when the user says quick, MVP, hack, or just make it work." alwaysApply: false --- # Fast but not sloppy "Quick" means fewer features, not worse code. Cut scope, keep quality. ## Cut these first - Settings/config UI → a named constant at the top of the file. - Admin panels → a script or SQL snippet in /scripts. - Multi-tenant/team support → single user, but keep userId on every record. - A custom design system → the component library already installed. - Edge-case UX polish → a clear error message is enough. ## Never cut these - Auth and ownership checks. - Input validation at API boundaries. - Idempotency for payments and webhooks. - Error logging (a console.error with context beats silence). - Types on function signatures that cross module boundaries. ## Debt you take on must be labelled ```ts // DEBT(solo): <what's missing> — <when it'll hurt> — <how to fix> ``` Max 3 new DEBT markers per change. If you need more, the scope is too big; say so. ## Prototype vs production - If the user says "prototype / throwaway", put it in /sandbox or a separate branch and say it is not production-safe. - Anything reachable by real users is production. Apply all of the above. After that I still ask for a short done-summary: what changed, how to verify, and which DEBT(solo) items were added. If the summary has no debt list and the diff quietly skipped a test, the rule did not run. What this does not replace This is not a substitute for a small-diff rule, a bug-fix playbook, or a real review. It only answers one failure mode: the agent heard "hurry" and lowered the quality bar instead of the feature bar. If you want the rest of the set I use (core working agreement, feature slicing, root-cause bug fixes, PR review, landing copy), I bundled them as a one-time Cursor pack: shipstack.sognia.workers.dev/cursor-pack . The rule above is usable on its own. Free sample rule: https://shipstack.sognia.workers.dev/sample

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ship_stack/when-i-tell-cursor-just-make-it-work-this-rule-stops-the-shortcut-from-rotting-2b7k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
