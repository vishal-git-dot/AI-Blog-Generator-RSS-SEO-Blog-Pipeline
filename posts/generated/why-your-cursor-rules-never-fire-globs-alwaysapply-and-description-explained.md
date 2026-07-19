---
title: "Why your Cursor rules never fire: globs, alwaysApply, and description explained"
slug: "why-your-cursor-rules-never-fire-globs-alwaysapply-and-description-explained"
author: "Rulestack"
source: "devto_ai"
published: "Sun, 19 Jul 2026 13:23:52 +0000"
description: "You wrote a .cursor/rules file. It has good rules. And the agent keeps ignoring them. Nine times out of ten this isn't the model being dumb — it's that the r..."
keywords: "rule, rules, agent, description, globs, you, cursor, never"
generated: "2026-07-19T13:36:01.819814"
---

# Why your Cursor rules never fire: globs, alwaysApply, and description explained

## Overview

You wrote a .cursor/rules file. It has good rules. And the agent keeps ignoring them. Nine times out of ten this isn't the model being dumb — it's that the rule never got attached to the context in the first place. Cursor has four ways a rule can enter a chat, and each one is gated by a different frontmatter field. Get the frontmatter wrong and the rule just sits on disk doing nothing. Here's the whole model, and the three mistakes that silently switch a rule off. The four rule types A rule in .cursor/rules/*.mdc becomes one of four types depending on its frontmatter: Type Fires when Frontmatter Always Every chat, no matter what alwaysApply: true Auto Attached An edited or referenced file matches a glob globs: set, alwaysApply: false Agent Requested The agent reads the description and decides it's relevant description: set, no globs, alwaysApply: false Manual Only when you @ -mention the rule none of the above set Read that last row again: a rule with no alwaysApply , no globs , and no description is Manual. It will never fire on its own. That is the number-one reason a rule "does nothing" — it quietly defaulted to manual and you never @-mentioned it. Mistake 1: writing globs as a YAML array This is the big one. globs is a bare, comma-separated string — not a YAML list, and not quoted: --- globs: src/**/*.ts, src/**/*.tsx alwaysApply: false --- What people write instead, and what quietly fails to attach: --- globs: - "src/**/*.ts" # array form — does not match --- --- globs: "src/**/*.ts" # quoted — does not match --- The glob syntax itself is standard: * matches one path segment, ** matches any number of directories. src/**/*.tsx , **/*.ts , and tailwind.config.* are all valid. Multiple patterns go on one line separated by commas: docs/**/*.md, docs/**/*.mdx . Mistake 2: .md instead of .mdc Rules must use the .mdc extension. A plain .md file dropped into .cursor/rules/ is ignored — no error, no warning, it simply isn't a rule. If you pasted a rule out of a README or a gist, check the extension before you check anything else. Mistake 3: an Agent-Requested rule with no description "Apply Intelligently" rules are the nicest type — the agent pulls them in when they're relevant instead of on a rigid glob. But that decision is made entirely from the description field. No description means the agent has nothing to match against, so an otherwise Agent-Requested rule collapses back to Manual and never surfaces. Write the description as a trigger, not a title: --- description: Conventions for writing and naming Vitest unit tests alwaysApply: false --- "Testing rules" is a title. "Conventions for writing and naming Vitest unit tests" is something the agent can actually match an incoming request against. How to check a rule actually attached Don't guess — look. When you send a message, Cursor surfaces the rules it pulled into that turn as part of the chat's context. If your rule isn't in that list, it didn't fire, and now you know which of the three mistakes to go check. This "did it attach?" loop is the fastest way to debug rules, and it's the exact step most people skip while blaming the model. Which type should a rule be? Project-wide and non-negotiable (never use any , always keyword arguments): Always . Stack- or folder-specific (React component conventions, migration file format): Auto Attached with a glob. Situational and judgment-heavy (how to write tests, how to structure an ADR): Agent Requested with a sharp description. Rare, on-demand scaffolding : Manual , and @-mention it when you want it. A healthy rules directory is mostly Auto Attached and Agent Requested, with a small handful of Always rules on top. If everything is Always, you're just bloating every prompt; if everything is Manual, nothing ever fires. The one-line takeaway A Cursor rule that "doesn't work" is almost always a rule that never attached. Check the extension ( .mdc ), check that globs is a bare comma-separated string, and give Agent-Requested rules a real description — then watch the context list to confirm it fired before you touch the rule's actual content. Maintaining a full .cursor/rules set — plus the Claude Code and Codex equivalents — by hand is a lot. That's what I build at Rulestack : production-ready rule packs for Cursor, Claude Code, and Codex. I also post short AI-coding-agent tips on Bluesky — follow along at @ai-shop.bsky.social .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rulestack/why-your-cursor-rules-never-fire-globs-alwaysapply-and-description-explained-b33

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
