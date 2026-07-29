---
title: "The Security Check That Couldn't Fail"
slug: "the-security-check-that-couldnt-fail"
author: "Jeriah Keith"
source: "devto_ai"
published: "Wed, 29 Jul 2026 02:59:46 +0000"
description: "My script printed a green [OK] . The setting it was checking was correct. Both of those things were true, and neither of them mattered, because the check tha..."
keywords: "check, one, because, you, same, not, security, had"
generated: "2026-07-29T03:14:29.813330"
---

# The Security Check That Couldn't Fail

## Overview

My script printed a green [OK] . The setting it was checking was correct. Both of those things were true, and neither of them mattered, because the check that printed [OK] was incapable of printing anything else. I want to walk through how that happened, because I wrote it, and because I think it is the most common way security tools fail. What I was building I am a cybersecurity student, and I was setting up a lab to study an AI agent framework that NVIDIA released this month. The framework can execute code written by a language model. Their own documentation is blunt about what that means: generated code might delete files, send private data somewhere it shouldn't go, or modify the environment it runs in. They tell you to run it inside a virtual machine, isolated from your real files. So I built one. A virtual machine with no shared folders, no clipboard sharing between the VM and my computer, no drag and drop. Every channel between the sandbox and my actual hard drive, switched off. Then I did the part I was proud of. Instead of trusting that I had ticked all the right boxes, I wrote a script that read the machine's settings back and confirmed each one. Set the control, then verify the control took effect. Those are two different things, and skipping the second is how people end up protected on paper only. That was the right instinct. My implementation of it was broken. The bug The check asked whether the clipboard was disabled. It used the wrong name for the setting, so it got no answer back. And it treated no answer as a yes. That is the whole thing. Nothing more sophisticated than that. The tool I was querying reports the clipboard setting under one name. The command I used to configure it in the first place used a different name for the same thing. I assumed they matched. They didn't. So my check searched for a setting that, as far as it could tell, did not exist, found nothing, and concluded everything was fine. If I had left the clipboard wide open, the check would have printed exactly the same green [OK] . How I found it Not by testing the security check. I want to be honest about that, because the real answer is more instructive than a clean story would be. The same script printed a summary of the machine's configuration at the end, purely for me to read. I noticed the summary was short. A few settings I expected to see weren't listed. It looked like a formatting glitch, the kind of thing you would normally shrug at. I chased it anyway, and it turned out those settings were missing from the summary for the same reason the security check was broken: I had the names wrong. The cosmetic bug and the security bug had one shared cause. The harmless one was visible. The dangerous one was invisible by design, because a check that cannot fail looks exactly like a check that passed. I got lucky. I would rather say I found it through rigor, but I found it because something unrelated looked slightly off and I didn't ignore it. The fix, and the part that mattered more Fixing the names was easy. Fixing the shape of the logic was the real work. Now, if the script can't find the setting it's looking for, it says so and fails. "I could not verify this" and "this is fine" are no longer the same outcome. Then I did something I had not done the first time. I deliberately broke the isolation. I connected a shared folder pointing straight at the drive with all my work on it, and I turned the clipboard back on. Then I ran the check. It failed. It named both problems and refused to give the all clear. That took about ninety seconds and it is the only reason I believe the check works. Watching a security control report success proves nothing about the control. It only proves the control can produce that output. You learn whether it works by breaking the thing it's supposed to be watching and confirming that it notices. The part I did not expect A few hours later I was reading the source code of the framework I had built all this to study. Deep in the sandbox module, I found a specific error they raise when the computer can't enforce one of their security guarantees. The comment next to it says failing closed there is deliberate, because the alternative is running untrusted code with a guard silently missing. That is the same principle. Same reasoning, opposite direction. My check could not verify something and resolved that to success. Their sandbox cannot enforce something and resolves that to refusing to start at all. I had written my fix hours before I read their code. Finding a team at NVIDIA arriving at the same conclusion, and treating it as important enough to explain in a comment, was the moment it stopped feeling like a personal lesson and started feeling like a rule. What I actually took from it A control that cannot fail is not a control. It is a message that says what you want to hear, and it will keep saying it long after the thing it was watching has stopped working. Systems are full of these. A monitoring rule watching a field that got renamed. A scanner pointed at a folder that moved. A test that stopped running months ago and still shows green. None of them announce themselves. They all look precisely like everything is fine, which is the point, and which is why the ordinary failure mode of a broken safety check is silence. "I don't know" and "you're safe" are different states. Any system that collapses them into one output will eventually tell you that you're safe when you are not. I know that now because I built one that did.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/yeriahz/the-security-check-that-couldnt-fail-2d4h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
