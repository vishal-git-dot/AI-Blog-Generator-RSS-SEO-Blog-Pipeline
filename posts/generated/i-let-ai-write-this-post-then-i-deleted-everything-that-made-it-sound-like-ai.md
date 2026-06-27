---
title: "I let AI write this post. Then I deleted everything that made it sound like AI."
slug: "i-let-ai-write-this-post-then-i-deleted-everything-that-made-it-sound-like-ai"
author: "fernforge"
source: "devto_webdev"
published: "Sat, 27 Jun 2026 13:38:02 +0000"
description: "A language model wrote this post. I directed it, but I didn't rewrite a single sentence by hand. Then I ran the draft through a small ruleset called Alchemy...."
keywords: "alchemy, you, your, post, like, writing, words, one"
generated: "2026-06-27T13:54:40.041963"
---

# I let AI write this post. Then I deleted everything that made it sound like AI.

## Overview

A language model wrote this post. I directed it, but I didn't rewrite a single sentence by hand. Then I ran the draft through a small ruleset called Alchemy. If the writing below doesn't trip your "this is AI" alarm, that's the entire point, and I'll show you the machinery. Start with the alarm itself. You've felt it. A README opens with "In today's fast-paced digital landscape." A reply leans on the em-dash three times in two sentences. Something delves into something else. The words are grammatical and the facts might even be right, but a part of your brain has already filed it under generated and dialed down how much it trusts you. That reaction is real and it's getting sharper. So the question for anyone shipping AI-written text is no longer "is it correct," it's "does it read like a person bothered to write it." What the draft looked like first Here's a paragraph describing this tool, the way a model writes it with no guardrails: In today's fast-paced digital landscape, writing has never been more important. Alchemy is a robust, powerful, and seamless solution that empowers developers to elevate their content and unlock the full potential of AI. By leveraging cutting-edge techniques, it delves into the intricacies of language to deliver a truly transformative experience — a game-changer for anyone looking to take their writing to the next level. Forty-eight words and it tells you nothing. Now the same point after Alchemy: Alchemy is a list of rules you hand your AI. It deletes the patterns that give generated text away: the em-dashes, the "not just X, but Y," the words like delve and robust that nobody says out loud. What's left reads like a person wrote it. The second one isn't smarter. It just stops performing. The rules aren't vibes The easy version of this post would list words I find annoying. Instead the ruleset is built on what people have actually measured. Wikipedia's editors maintain a page called "Signs of AI writing," a long catalogue of tells they use to clean up machine-generated articles. A 2025 study by Kobak and colleagues went through millions of biomedical papers and found specific words whose frequency jumped after ChatGPT shipped: delve showed up at roughly 28 times its old rate, underscore and showcase close behind. Pangram Labs did the same for phrases and found "in the ever-evolving landscape" running about eleven thousand times more often than humans ever wrote it. So Alchemy bans the heavy hitters outright, puts a second tier on rations, and flags the constructions: the rule-of-three flourish, the recap conclusion that repeats the intro, the helpful-assistant outro. One rule matters more than the lists, though. No single word proves anything. Real writers use em-dashes, delve is a fine word, and a humanizer that strips every flagged term leaves prose worse than it found it. The tell is density — a dozen of these tics stacked together over flat, evenly-weighted text. The rules weigh co-occurrence over any one hit, which is also why this post can use an em-dash without flinching. This is the second one. It's fine. Using it The whole product is one Markdown file your agent reads before it writes. Drop it in: npx @fernforge/alchemy init That writes ALCHEMY.md into your project and links it from your CLAUDE.md , AGENTS.md , or .cursorrules . From then on the rules ride along whenever the agent writes a doc, a commit message, or a reply. You can also just read the file: it's MIT-licensed and lives at github.com/fernforge/alchemy . It won't make a model say anything true or interesting. That part is still on you. What it does is stop the writing from announcing where it came from, so the ideas get read on their own terms. Which, given how this post was made, is a claim you're in a good position to judge.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fernforge/i-let-ai-write-this-post-then-i-deleted-everything-that-made-it-sound-like-ai-28aj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
