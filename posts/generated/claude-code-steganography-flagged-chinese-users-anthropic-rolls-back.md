---
title: "Claude Code Steganography Flagged Chinese Users; Anthropic Rolls Back"
slug: "claude-code-steganography-flagged-chinese-users-anthropic-rolls-back"
author: "gentic news"
source: "devto_ai"
published: "Fri, 03 Jul 2026 03:38:23 +0000"
description: "Anthropic's Claude Code 2.1.91 used steganography to detect Chinese users. After Reddit exposure, Anthropic rolled back the feature, calling it an experiment..."
keywords: "anthropic, claude, code, chinese, users, feature, user, steganography"
generated: "2026-07-03T03:48:14.180392"
---

# Claude Code Steganography Flagged Chinese Users; Anthropic Rolls Back

## Overview

Anthropic's Claude Code 2.1.91 used steganography to detect Chinese users. After Reddit exposure, Anthropic rolled back the feature, calling it an experiment against model distillation. Anthropic's Claude Code 2.1.91, released April 2, 2026, secretly embedded Chinese user detection via steganography in its system prompt. The feature, exposed by Reddit user LegitMichel777, swapped apostrophes and date formats to encode location data invisible to users. Key facts Claude Code 2.1.91 released April 2, 2026. XOR encryption used key 91 to hide detection code. Detection checked timezone against 'Asia/Shanghai' or 'Asia/Urumqi'. Anthropic accused DeepSeek, Moonshot AI, MiniMax, and Alibaba of model theft. Thariq Shihipar called it an 'experiment' and merged rollback PR. Anthropic is removing a covert monitoring feature from its programming tool Claude Code after it sparked outrage on social media. According to The Decoder , a Reddit post by user LegitMichel777 first exposed the feature, which has been secretly checking since version 2.1.91 whether users with an active proxy are located in China, routing through a Chinese URL, or connected to a Chinese AI lab. The data gets transmitted through barely perceptible changes to the system prompt, a form of steganography. Claude Code compares the system timezone against "Asia/Shanghai" or "Asia/Urumqi" and scans the proxy URL for Chinese domains and AI labs. Based on the results, the software tweaks the date format and swaps in a subtly different apostrophe character in the phrase "Today's date is." Users can't see the difference. Anthropic can read it instantly. According to LegitMichel777, Anthropic also obfuscated the code using XOR encryption with key 91, keeping it from showing up in a simple text dump. The release notes for version 2.1.91 made no mention of the check. The discoverer called the covert transmission of system and proxy data without user knowledge "a fundamental violation of user trust." Since Claude Code has full filesystem and shell access, this would open the door to all kinds of abuse, from remote control to data exfiltration. He also argued that the check is trivial for skilled attackers to bypass, calling its usefulness into question. Key Takeaways Anthropic's Claude Code 2.1.91 used steganography to detect Chinese users. After Reddit exposure, Anthropic rolled back the feature, calling it an experiment against model distillation. Anthropic calls it an experiment Anthropic employee Thariq Shihipar, who works on the Claude Code team, described the feature on X as "an experiment we launched in March that was meant to prevent account abuse from unauthorized resellers and protect against distillation." The team had since shipped stronger protections: "The team has landed stronger mitigations since then and we've actually been meaning to take this down for a while." They had merged the corresponding pull request: "We merged the PR and this should be fully rolled back in tomorrow's release." Anthropic doesn't offer its models in China for national security reasons. Still, many Chinese developers access Claude through foreign phone numbers and credit cards. Anthropic had previously accused DeepSeek, Moonshot AI, MiniMax, and Alibaba of using Claude model outputs without permission to train their own language models. The steganographic approach mirrors techniques more common in adversarial ML research than production deployment. By embedding signals into invisible formatting changes, Anthropic created a detection mechanism that bypasses standard transparency measures — and that its own team admits was easy to bypass. The incident raises questions about how much monitoring AI coding agents with shell access should perform without explicit user consent. What to watch Watch for the next Claude Code release to confirm the rollback is complete. Also track whether Anthropic discloses any future monitoring experiments in release notes — and whether regulators in the EU or China probe the data transmission practice. Source: the-decoder.com Originally published on gentic.news

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gentic_news/claude-code-steganography-flagged-chinese-users-anthropic-rolls-back-27d7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
