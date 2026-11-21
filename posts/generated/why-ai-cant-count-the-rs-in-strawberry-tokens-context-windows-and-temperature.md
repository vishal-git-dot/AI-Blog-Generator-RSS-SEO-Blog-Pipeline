---
title: "Why AI Can't Count the R's in \"strawberry\": Tokens, Context Windows and Temperature"
slug: "why-ai-cant-count-the-rs-in-strawberry-tokens-context-windows-and-temperature"
author: "Muiduzzaman Lipu"
source: "devto_ai"
published: "Sat, 21 Nov 2026 18:34:41 +0000"
description: "Why can't a very capable AI reliably count the r's in "strawberry"? Why does it forget the start of a long chat? Why does the same question get different ans..."
keywords: "tokens, temperature, model, token, split, why, one, how"
generated: "2026-11-21T18:56:47.823918"
---

# Why AI Can't Count the R's in \"strawberry\": Tokens, Context Windows and Temperature

## Overview

Why can't a very capable AI reliably count the r's in "strawberry"? Why does it forget the start of a long chat? Why does the same question get different answers? It comes down to three ideas: tokens , the context window and temperature . Every tokenizer output below is real, from OpenAI's tiktoken library with the o200k_base encoding (used by GPT-4o). Video version: 1. AI doesn't read words. It reads tokens. Before a model sees your text, a tokenizer splits it into chunks called tokens, and each one becomes an ID number. Here's a tiny helper to show the chunks: import tiktoken enc = tiktoken . get_encoding ( "o200k_base" ) split = lambda s : [ enc . decode ( [ t ] ) for t in enc . encode ( s ) ] >>> split ( "Hello world" ) [ 'Hello' , ' world' ] # 2 tokens >>> split ( "unbelievable" ) [ 'un' , 'bel' , 'ievable' ] # 3 tokens >>> split ( "Refactorly" ) [ 'Ref' , 'actor' , 'ly' ] # 3 tokens Common words are a single token (notice the space is part of ' world' ). Rare or made-up words get split into pieces. 2. Why it can't count the r's in "strawberry" >>> split ( "How many r's are in strawberry?" ) [ 'How' , ' many' , ' r' , "'s" , ' are' , ' in' , ' strawberry' , '?' ] >>> enc . encode ( " strawberry" ) [ 101830 ] In this sentence, ' strawberry' is one token : number 101830. The model never sees s-t-r-a-w-b-e-r-r-y . It sees one ID, and has to remember from training how that word is spelled. Counting letters inside a token is like asking you how many strokes are in a word you only ever heard spoken. Newer models often get this specific question right, partly because it became famous and partly because they spell the word out step by step first. The underlying limitation is still there. 3. Numbers get chopped up too >>> split ( "1234567" ) [ '123' , '456' , '7' ] >>> split ( "9.11 > 9.9" ) [ '9' , '.' , '11' , ' >' , ' ' , '9' , '.' , '9' ] Long numbers become groups of three digits, and 9.11 becomes 9 , . , 11 . The model compares the chunk 11 with the chunk 9 , which is part of why models have stumbled on "is 9.11 bigger than 9.9?". For real math, let the model write code or call a calculator tool. 4. The context window is the model's working memory The context window is everything the model can see at once: the system prompt, the whole chat history, any files or documents you pasted, and the answer it's writing right now. It's measured in tokens , not words or messages. For English, a rough rule is 1 to 1.5 tokens per word: a 180-word test paragraph came out at 201 tokens. When a conversation gets longer than the window, the oldest messages get cut or summarized by the app. That's why a long chat "forgets" what you said at the start. Tip: start a new chat for a new task, and repeat key instructions instead of assuming the model still sees them. Tokens are also how API usage is billed, so a shorter prompt is a cheaper prompt. 5. Answers are written one token at a time A language model does one thing, over and over: look at all the tokens so far, predict the most likely next token, add it, and repeat. It's generating plausible text, not looking facts up in a database. That's why it can sound completely confident and still be wrong (a "hallucination"). Give it the source material in the prompt when facts matter. 6. Temperature: how random the next token is At each step the model has a probability for every possible next token. Temperature controls how it picks: 0: always the most likely token, so the same prompt gives (nearly) the same answer. Higher: less likely tokens get picked more often, so answers vary. I asked a local model (Llama 3.2 3B via Ollama) the same question several times: # "Suggest a name for a coffee shop for programmers. Reply with only the name." temperature 0 → Byte & Brew temperature 0 → Byte & Brew temperature 1.5 → Ctrl+Alt+Brew temperature 1.5 → Byte & Brew temperature 1.5 → Ctrl+Alt+Brew Use low temperature for code, extraction and anything that should be consistent; higher for brainstorming and creative writing. Recap Idea What it means What to do Tokens Text is split into chunks with IDs Expect trouble with spelling, letters and digits Context window Everything the model sees at once, in tokens New chat per task; repeat key instructions Next-token prediction It writes plausible text, one token at a time Provide sources; verify facts Temperature Randomness of the next-token choice Low for code, higher for ideas Try tiktoken on your own name and see how it splits. 👇 I post one tested coding tip every day on YouTube at Refactorly . The 30-second version of this one is here .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/refactorly/why-ai-cant-count-the-rs-in-strawberry-tokens-context-windows-and-temperature-8k9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
