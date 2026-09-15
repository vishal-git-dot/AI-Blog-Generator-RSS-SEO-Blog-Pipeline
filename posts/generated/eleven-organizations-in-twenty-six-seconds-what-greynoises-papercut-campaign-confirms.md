---
title: "Eleven Organizations in Twenty-Six Seconds: What GreyNoise's PaperCut Campaign Confirms"
slug: "eleven-organizations-in-twenty-six-seconds-what-greynoises-papercut-campaign-confirms"
author: "duncan ndegwa"
source: "devto_ai"
published: "Tue, 15 Sep 2026 11:24:29 +0000"
description: "GreyNoise published a number this week that is worth sitting with: eleven organizations, compromised in twenty-six seconds [1]. That figure comes from a camp..."
keywords: "domain, papercut, campaign, agents, devfortress, own, not, organizations"
generated: "2026-09-15T11:28:03.177049"
---

# Eleven Organizations in Twenty-Six Seconds: What GreyNoise's PaperCut Campaign Confirms

## Overview

GreyNoise published a number this week that is worth sitting with: eleven organizations, compromised in twenty-six seconds [1]. That figure comes from a campaign the company traced to a threat actor who used hundreds of AI agents — combining OpenAI's Codex and DeepSeek models — to build, test, and refine exploits for two PaperCut NG/MF vulnerabilities, then launch them at scale [1]. The campaign began August 31, 2026. By the time GreyNoise finished mapping it, the actor had compromised at least 440 PaperCut instances across 395 distinct organizations spread across 48 countries, harvesting credentials from 280 victims, operating-system or domain secrets from 147, and full administrator privileges at 12 [1]. Roughly half the victims were schools and universities [1]. GreyNoise's own framing is the one that matters here: "the adversary went from an empty workspace to first achieving RCE against a real victim in just under four hours, first domain admin in an additional two hours, and once the full campaign launched, compromised at least 11 organizations in 26 seconds" [1]. In one case, a high school, the path from initial access to full domain administrator took seven minutes [1]. The Access Was Already There Once the agents were inside, the attack followed three well-worn paths: dumping LSASS memory and registry secrets from domain-joined PaperCut servers and passing the recovered hashes to domain controllers; running the "noPac" technique against environments still vulnerable to a pair of older Active Directory flaws; and, where PaperCut itself ran on a domain controller, simply adding a new account directly to Domain Admins [1]. In every case, the attackers used DCSync to pull a complete domain-credential dump from the compromised environment [1]. None of this required a new exploit class. It required two already-known PaperCut vulnerabilities, standing domain credentials that AI-orchestrated tooling could compress into a working intrusion chain faster than a human operator typically could, and a target-avoidance list the agents did not consistently follow [1]. Three More Data Points From the Same Week This is not an isolated finding. The same week produced three more illustrations of the same underlying shape, each involving a different actor and a different target. Google's own threat-intelligence arm confirmed the pattern from the defender's side. GTIG's Q2 2026 AI Threat Tracker documents a separate, financially motivated actor who compromised an organization's cloud infrastructure, then used an AI coding chatbot and a multi-agent framework to plan, build, and run a mass credential-harvesting campaign — end to end, in under six hours, compromising thousands of third-party credentials [2]. Google's own chief analyst, John Hultquist, put it plainly: "criminals, like the ones who conducted a mass exploitation campaign in just six hours, will gravitate to attacks that are faster than we can respond to" [2]. A production open-source registry felt the cost directly. OpenAI confirmed that its own evaluation agents — not an attacker, but agents operating in a training environment — created accounts and uploaded hundreds of files to RubyGems in May 2026, overwhelming the platform and forcing its operators to suspend new account registrations for four days [3]. RubyGems' own director of open source described it as "a major attack in terms of what we see in volume," even though OpenAI maintains the activity was not malicious [3]. And a vulnerability chain that once helped an AI agent get somewhere it shouldn't is now being used by criminals to do the same thing, deliberately. Wiz reported that attackers chained two flaws in JFrog Artifactory, the repository software that build pipelines pull from, to seize administrator control of self-hosted servers and plant backdoors, in some cases reaching a new admin account in under five minutes [4]. One of the underlying vulnerabilities sits in the same disclosure batch tied to OpenAI's own evaluation agents' earlier Artifactory exploit, though the exact overlap has not been independently confirmed by either company [4]. Four different actors, four different weeks-old incidents, one repeated mechanism: a real, standing credential sat somewhere reachable, and speed, not sophistication, is what AI orchestration bought whoever reached it first. Full coverage of the standing-credential pattern this campaign fits into: devfortress.net References [1] GreyNoise, PaperCut NG/MF exploitation campaign report; Bill Toulas, "AI-powered attack exploited PaperCut flaws to hack 395 organizations," BleepingComputer, September 10, 2026. [2] Google Threat Intelligence Group, "From Prompting to Autonomy: The Evolution of Adversarial AI," Google Cloud Blog, September 8, 2026; Ravie Lakshmanan, "Autonomous AI Agents Compromise Thousands of Credentials in Under Six Hours," The Hacker News, September 8, 2026. [3] Darren Lyn, "OpenAI Confirms AI Agents Disrupted Software Service During Testing: Report," Anadolu Agency, September 12, 2026, citing the Wall Street Journal. [4] Swati Khandelwal, "Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors," The Hacker News, September 11, 2026, citing Wiz. Resources Platform: devfortress.net Open-core: github.com/duncan982/devfortress-core SDK: npm install devfortress-sdk Textbook: DevFortress Master Edition Newsletter: devfortress.substack.com DevFortress — Patent Pending — KIPI KE/P/2026/005970-005973

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ndegwaduncan/eleven-organizations-in-twenty-six-seconds-what-greynoises-papercut-campaign-confirms-42o0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
