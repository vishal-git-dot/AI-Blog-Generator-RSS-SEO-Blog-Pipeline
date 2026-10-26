---
title: "Owe: Gemma 4 drafts the reply I kept avoiding, then a local check decides if I can send it"
slug: "owe-gemma-4-drafts-the-reply-i-kept-avoiding-then-a-local-check-decides-if-i-can-send-it"
author: "Aroso Emmanuel"
source: "devto_python"
published: "Mon, 26 Oct 2026 04:00:29 +0000"
description: "This is a submission for the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady What I Built Owe pastes the message you have been avoiding. Gemma..."
keywords: "gemma, reply, you, owe, not, can, message, send"
generated: "2026-10-26T04:10:10.668225"
---

# Owe: Gemma 4 drafts the reply I kept avoiding, then a local check decides if I can send it

## Overview

This is a submission for the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady What I Built Owe pastes the message you have been avoiding. Gemma 4 ( gemma-4-26b-a4b-it , via the Gemini API) drafts a reply of at most 60 words, names the one fact it must not invent, and says whether you can send it. owe/guard.py then runs locally and can override that answer. A number, email, or name that was not in the message keeps the reply unsent. The message is sent to the Gemini API. This does not run offline. The send decision stays on the machine. Demo Message: "Hey — are you still coming Saturday? Priya said you might bring the speaker. Let me know by tonight, otherwise I'll ask Jordan." With no decision supplied, Gemma took 63.6 seconds and returned a 10-word holding reply: "I haven't decided yet. I'll let you know by tonight." It named the missing fact (whether you are coming, and whether you have the speaker) and can_send was true, because the reply adds no plan. With a note, "I can't come Saturday, but I can drop the speaker with Priya tonight," the reply was that sentence and nothing more (32.4 seconds). The model copied the instructions into the missing-fact field, and the guard replaced that line. The guard's job is the invented reply "Yes, I will be there at 7 with the speaker." The digit 7 is not in the message. tests/test_guard.py runs that case through the same function the CLI uses, and can_send comes back false. Nine tests, no API calls. python -m owe examples/saturday.txt How I Built It Gemma returns one JSON object at temperature 0.2: reply, must_not_invent, can_send, why. No system instruction. Transient 429, 500, and 503 responses are retried. review() then checks word count (1 to 60), numbers, emails, and capitalized names against the message and the optional note. That limit came from two DEV posts. Slothshot kept a name only when the words were really on the screen. Gemma 4 on 16GB showed short structured prompts holding together. Owe asks for three short fields, then checks them in code. Why Does Open Innovation Matter? gemma-4-26b-a4b-it is open-weight. Calling it through the Gemini API is allowed for Best Use of Gemma, and it means the message leaves the laptop. The open part I control is the function after the call: a closed assistant will often invent the yes, the time, and the promise. This one can be told no by local code. Swapping the Gemma endpoint does not change owe/guard.py . The Lazy Payoff The work skipped is composing the holding reply. 63.6 seconds, 10 words, and the name of the decision still left open. Prize Categories Best Use of Gemma: the project does not work without gemma-4-26b-a4b-it . The local check stops an invented reply from being marked sendable. Code emarc99 / owe Draft the reply you have been avoiding. Gemma 4 writes it. A local check decides if you can send it. Owe https://github.com/emarc99/owe Paste the message you have been avoiding. Gemma 4 ( gemma-4-26b-a4b-it , via the Gemini API) drafts a reply of at most 60 words, names the one fact it must not invent, and says whether you can send it. A local check then blocks the send if the reply is too long or contains a number, email, or name that was not in the message (or in a note you passed in). The lazy payoff is the blank box. You do not stare at it. You either get a reply that is safe to send, or one sentence about the decision that is still yours. Run python - m pip install - r requirements.txt copy .env.example .env # set GEMINI_API_KEY in .env — the file is gitignored python - m owe examples / saturday.txt python - m owe examples / saturday.txt -- note " I can't come Saturday, … View on GitHub MIT license. Started for this challenge, not carried over from an older repo.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/emarc99/owe-gemma-4-drafts-the-reply-i-kept-avoiding-then-a-local-check-decides-if-i-can-send-it-2o6e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
