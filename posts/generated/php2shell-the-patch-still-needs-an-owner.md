---
title: "PHP2Shell: the patch still needs an owner"
slug: "php2shell-the-patch-still-needs-an-owner"
author: "Alex"
source: "devto_ai"
published: "Fri, 23 Oct 2026 04:00:23 +0000"
description: "PHP operators: Apply the current PHP security update , restart or replace affected processes as required, and verify the runtime serving requests. Fixed upst..."
keywords: "php, not, can, whether, would, still, needs, security"
generated: "2026-10-23T04:12:22.350653"
---

# PHP2Shell: the patch still needs an owner

## Overview

PHP operators: Apply the current PHP security update , restart or replace affected processes as required, and verify the runtime serving requests. Fixed upstream releases are listed below. A patch does not establish whether an earlier compromise occurred. In 2024, a PHP developer found the first signs of an out-of-memory problem. A possible exploit was theorized, but there was no concrete attack path. The PHP Foundation's account describes competing fixes: compatibility breaks, denial-of-service risks and changes across third-party extensions. Specialists had other responsibilities, and the consensus process struggled to settle on an approach. Work stalled and restarted. The Foundation calls the delay a structural failure involving both decisions and resources. Calif's report of an unconditional remote-code-execution path on 11 August 2026 made repair the Foundation security team's top priority. According to OpenAI's account , Calif used GPT-5.6 Sol for its discovery, and Wiz independently reported both flaws. The Foundation also records an independent report of the same root cause from OpenAI and describes using AI to validate and group reports, with people responsible for decisions and patches. The weakness was known. Fixing it without breaking something else was still a problem. The patch was not the starting gun On 21 October, PHP released the fixes. But AWS subsequently identified an exploitation attempt in its MadPot honeypot telemetry dating to 17 October , four days earlier. AWS says it is unclear how the actor obtained the information or whether these attempts would have succeeded on real-world systems. An investigation into possible compromise needs to look before the public disclosure date. The PHP reports and Sean Heelan's o3-assisted Linux finding in May 2025, CVE-2025-37899 in ksmbd , show what AI-assisted research can find. They do not tell us whether discovery is globally outpacing repair. The part I recognize from client work I've worked with medium-sized businesses and larger enterprises. One thing I have repeatedly noticed is how uneven technical competence can be, especially around system administration. I don't take an IT department or a hosting contract as proof that someone understands the running system. I would ask the same question of an internal team and a provider: can you follow this advisory through to the PHP process serving a customer's request? Even for a single rented server, I want to know which parts the provider maintains and which parts the customer has to handle. In a 2026 government study , 57% of UK businesses lacked confidence in at least one of nine basic cybersecurity tasks . This was a self-report measure, not a practical assessment. Tasks handled by external providers were not counted as skills gaps. The expertise did not have to be on the company's payroll. What I would expect from that partner For an incident like PHP2Shell, I would want clear answers to four questions: Which services and runtimes are affected? Who has the access, authority and time to deploy the fix? How will we verify that services and workers use the fixed build? Who will assess whether earlier exposure needs investigation? Laravel Forge's advisory explains that its automatic security updates do not patch PHP: those packages come from a separate repository outside the automatic update scope. That maintenance process can be working as configured while PHP remains vulnerable. Updating the PHP packages restarts PHP-FPM, but long-running CLI workers still need restarting to use the fixed runtime. The company still needs to agree the scope and authorize the work. A partner can take responsibility for a repair without being able to guarantee the security of the whole system. I also would not put every failure on an administrator. A capable engineer can be blocked by insufficient staffing, an unsupported dependency or management that will not approve downtime. Competence needs resources and the authority to make decisions. Can the repair work keep up? By 21 October, researchers had documented the flaws and maintainers had released fixes. Whether a particular business was protected from these flaws still depended on what happened in its own deployment. I would judge progress in AI-assisted security by whether more affected systems actually get repaired. That requires following the work beyond the research report, through the release and into the services people use. What happens if our ability to find vulnerabilities grows faster than our ability to understand and fix them? PHP update reference The 21 October 2026 releases address CVE-2026-109618 and CVE-2026-109619 : PHP branch Fixed upstream release 8.2 8.2.35 8.3 8.3.36 8.4 8.4.27 8.5 8.5.12 Follow your supplier's current guidance for distribution backports and older branches. Customer-built container images may need rebuilding and redeployment , in addition to replacing or restarting affected processes. Sources checked on 23 October 2026. The technical findings and telemetry are the cited researchers' and providers' reports; I have not reproduced the exploits myself.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ake2l/php2shell-the-patch-still-needs-an-owner-19fl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
