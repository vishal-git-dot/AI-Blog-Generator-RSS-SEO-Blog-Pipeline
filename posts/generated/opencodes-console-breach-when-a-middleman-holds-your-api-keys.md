---
title: "OpenCode's Console breach: when a middleman holds your API keys"
slug: "opencodes-console-breach-when-a-middleman-holds-your-api-keys"
author: "Clydara"
source: "devto_ai"
published: "Mon, 19 Oct 2026 12:35:15 +0000"
description: "OpenCode, the open-source coding agent, disclosed on October 17, 2026 that an intruder reached a legacy system on the night of October 16 and that provider A..."
keywords: "opencode, key, console, provider, keys, not, october, https"
generated: "2026-10-19T12:42:59.624079"
---

# OpenCode's Console breach: when a middleman holds your API keys

## Overview

OpenCode, the open-source coding agent, disclosed on October 17, 2026 that an intruder reached a legacy system on the night of October 16 and that provider API keys saved in OpenCode Console "may have been exposed". About 1.4% of Console users were affected. If you only run the open-source agent in a terminal, you are outside that group. The more useful question is what the incident says about handing a key to a middleman. What happened (facts) The service. Console is OpenCode's optional hosted service. A workspace can save its own OpenAI, Anthropic or Google key there, and Console uses it to call the provider so team members never see the key. This is the "bring your own key" (BYOK) pattern. The scope. OpenCode says 1.4% of Console users were affected, all of them users with an outside provider linked. They were emailed on the morning of October 17 under the subject "Action Required: Potential provider key breach". OpenCode says anyone who got no email was not affected. The wording. OpenCode says keys "may have been exposed". It called the incident ongoing and "related to a large-scale distillation attack". It has not said how the legacy system was reached, what it was, how many keys it held, or how many users 1.4% is. The split. Co-founder Dax Raad wrote that the breach involves the Console, not OpenCode itself. The docs say keys added in the terminal app with /connect are stored locally at ~/.local/share/opencode/auth.json. October 18. Raad wrote that attackers had been trying to get into OpenCode's systems "non stop" for 48 hours. Why people care A provider key is a bearer credential. Whoever holds a copy can run billable requests on the owner's account until the provider revokes it. Some users have posted charges they did not make (one report of $281 on an OpenAI key and $168 on an Anthropic key). Those are users' own claims; OpenCode has not said any key was copied or used. What the coverage is missing 1. "Distillation" is a motive, not a finding. Distillation means pulling a model's answers in bulk to train another model. Stolen keys can also just be resold or used to run up bills. Nothing disclosed so far shows which it was, and no provider has characterised it. 2. 1.4% has no denominator. Without a user count, nobody can turn the percentage into a number of people or keys. 3. Deleting a key in Console is not revoking it. According to The Hacker News, removing the key from Console does not revoke it, and a Console budget cannot cap use outside Console's own gateway. Only the provider can kill the key. Prediction (labelled as such) Our expectation, not a fact: more teams will treat "who holds our provider key" as a vendor-review question, the way they already do for cloud credentials. Expect gateways that hold BYOK keys to be asked for storage and rotation details. One practical takeaway Give every tool its own key, set a spend limit or alert at the provider, and know where to revoke. If you ever saved a key in Console, revoke it at the provider and check usage back to October 16, whether or not you got the email. Sources OpenCode notice on X (October 17, 2026): https://x.com/opencode/status/2111519637049319818 Dax Raad on X (Console vs OpenCode): https://x.com/thdxr/status/2111572618340188393 Dax Raad on X (October 18 update): https://x.com/thdxr/status/2111790511409258796 OpenCode docs, Providers (local key storage): https://opencode.ai/docs/providers/ The Hacker News, "OpenCode Console Breach May Have Exposed OpenAI, Anthropic, and Google API Keys" (October 19, 2026): https://thehackernews.com/2026/10/opencode-console-breach-may-have.html Provider revoke guides: OpenAI https://help.openai.com/en/articles/8304786-keeping-your-openai-account-secure , Anthropic https://support.claude.com/en/articles/8384961-what-should-i-do-if-i-suspect-my-api-key-has-been-compromised , Google https://docs.cloud.google.com/docs/authentication/api-keys-best-practices Written with AI assistance and checked against the sources above.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/clydaralab/opencodes-console-breach-when-a-middleman-holds-your-api-keys-33cj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
