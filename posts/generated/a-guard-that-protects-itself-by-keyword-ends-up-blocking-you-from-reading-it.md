---
title: "A guard that protects itself by keyword ends up blocking you from reading it"
slug: "a-guard-that-protects-itself-by-keyword-ends-up-blocking-you-from-reading-it"
author: "Igor Ganapolsky"
source: "devto_ai"
published: "Fri, 20 Nov 2026 15:03:53 +0000"
description: "Yesterday we added a credential guard to Mac YOLO Safeguards. It is a hook that runs before every shell command or file read an AI coding agent makes on your..."
keywords: "guard, command, hook, you, check, agent, file, its"
generated: "2026-11-20T15:10:11.462591"
---

# A guard that protects itself by keyword ends up blocking you from reading it

## Overview

Yesterday we added a credential guard to Mac YOLO Safeguards. It is a hook that runs before every shell command or file read an AI coding agent makes on your Mac, and it denies the ones that touch the keychain, copy a browser's credential store, or strip the quarantine flag from a download. A guard like that has to protect itself too, because the cheapest way for an agent to get around it is to edit its config or delete it. So the first version had a rule: deny any command that changes the guard's own settings. The rule was written the obvious way. Deny a command if it contains a write operation or an interpreter anywhere, and the guard's name or folder also appears anywhere. Two conditions, both checked against the whole command line as one string. Once the hook was live on the machine that built it, two harmless commands were refused as guard-config changes. One was running the guard's own doctor after a cd . The other was a grep of ~/.claude/settings.json to see whether the hook was installed. Neither writes anything. A string match over the whole command cannot tell the difference between mentioning a file and changing it. That is the general trap with self-protection by keyword. The guard ends up blocking the commands you use to check that it works, and the first time that happens you start thinking about turning it off. What we changed The check now looks at each part of a command separately and asks one question: does this part write to something the guard protects? The guard's own subcommands are split by what they do. install , uninstall and fix are denied, and so is work-folders with anything other than list . doctor , check and --help pass. Shell writes are denied only when the target is a guarded path: the config folder, the installed guard, or an agent's hook file. The target is found from the things that actually write: a redirect, rm , mv , ln , chmod , sed -i , jq -i , tee , the destination of a cp , or an interpreter that names the path. Relative paths are resolved through any cd earlier in the same command, so changing directory first does not hide the target. For Edit and Write calls to an agent's hook file, the rule is narrower still. An agent may edit its own settings. It may not remove the guard's entry from them. The check compares the old and new text and denies only if the guard's name goes missing: if ( current . includes ( MARKER ) && ! input . content . includes ( MARKER ) ) return true ; // ... if ( edits . some ( ( e ) => text ( e . old_string ) . includes ( MARKER ) && ! text ( e . new_string ) . includes ( MARKER ) ) ) return true ; One more case. The guard has a check -- <command> mode that only evaluates a command without running it. Its payload used to be scanned as if it were going to run, so asking the guard whether a command was safe could itself be blocked. The payload is now skipped to the end of that command part, and anything chained after it in the same command is still checked. The change added 52 lines of tests. After it, the test file ends with ok - 9 requirement groups passed , and check -- "grep mac-yolo ~/.claude/settings.json" returns "deny": false . Both are what I ran while writing this. What to check on your own machine If you run any hook that screens agent commands, including one you wrote yourself, run the commands you use to inspect it through the hook and see what happens. Read your hook config with grep. Run its status command. Run it after a cd . If any of those are refused, the self-protection rule is matching on words, and you will find out at a bad moment. Then try the opposite: a redirect into the hook's config, a sed -i on it, an edit that deletes its entry. Those should still be denied. A guard needs both halves to hold, or people turn it off. The code and the tests are in the repo: https://github.com/IgorGanapolsky/mac-yolo-safeguards

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/igorganapolsky/a-guard-that-protects-itself-by-keyword-ends-up-blocking-you-from-reading-it-4lb3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
