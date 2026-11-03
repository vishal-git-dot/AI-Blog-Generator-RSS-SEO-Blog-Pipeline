---
title: "111, 133, 172: The Same 192 Characters in Three Tokenizers"
slug: "111-133-172-the-same-192-characters-in-three-tokenizers"
author: "WGG"
source: "devto_python"
published: "Tue, 03 Nov 2026 22:54:49 +0000"
description: "I keep a bad habit: when a prompt looks short, I assume it is cheap. Then I pasted one Chinese code-review request into three tokenizers. Same 192 characters..."
keywords: "tokens, text, token, character, request, per, not, deepseek"
generated: "2026-11-03T23:03:46.605548"
---

# 111, 133, 172: The Same 192 Characters in Three Tokenizers

## Overview

I keep a bad habit: when a prompt looks short, I assume it is cheap. Then I pasted one Chinese code-review request into three tokenizers. Same 192 characters: 111 tokens in DeepSeek V4, 133 in o200k_base , 172 in cl100k_base . A 55% spread. The rule I had been using, four characters per token, predicts 48. The text asks for two failure modes of a Redis read-through cache in front of a Postgres analytics database, whether a 60-second TTL suits a financial reporting dashboard, and one metric to add before merging. The author expects p99 to fall from 1200 ms to under 50 ms at 12k requests per minute. 你是一名资深后端工程师，正在评审一个合并请求：在 PostgreSQL 分析库前面加一层 Redis 读穿缓存。 所有聚合查询的缓存时间都是 60 秒。作者预计看板接口的 p99 延迟会从 1200 毫秒降到 50 毫秒以下，高峰期每分钟 1.2 万次请求。 请列出两个风险最高的故障场景，判断 60 秒是否适合财务报表看板，并给出合并前应加的一项监控指标。每条不超过 80 字。 Where the count comes from Byte-level BPE does two things. A regular expression pre-splits the text into chunks: words with their leading space, runs of digits, punctuation, runs of whitespace. Each chunk then starts as individual bytes, and the tokenizer merges the highest-ranked adjacent pair until no listed pair remains. The merge list is learned, so frequent pairs rank high. That pre-tokenization step sets a hard boundary: merges never cross a chunk border, even when the vocabulary holds the pieces on both sides. Vocabulary size matters too. cl100k_base has 100,277 entries, o200k_base 200,019, DeepSeek V4 129,280, special tokens included. Text Characters o200k_base cl100k_base DeepSeek V4 What is a token in AI? 22 7 7 7 你好，世界！ 6 4 7 4 東京の天気は晴れ 8 7 10 7 什么是 AI 里的 token？ 16 7 10 6 Code-review sample 192 133 172 111 English barely moves: 7 tokens in all three for the 22-character question. Chinese and Japanese do. In cl100k_base the character 世 is not a token, so 你好，世界！ spends two byte tokens on it. 🦜 is 4 bytes in UTF-8 and 3 tokens in o200k_base — F0 9F , A6 , 9C — and none of those pieces is a character on its own. The full measured table, with the other samples, is in the tokenizer guide . Code is not prose either The four-character rule was calibrated on English prose, and code breaks it in a different direction. Punctuation, indentation and repeated short keys all cost tokens. Pretty-printed JSON carries spaces and newlines that minified JSON does not, and the minified text is what the API receives if you send it as a string. A 10,000-character file can need more tokens than the character estimate suggests. Claude and Gemini: estimates by design Claude and Gemini do not publish tokenizers for local use, so any local count for them is an estimate. Anthropic's count_tokens endpoint takes the same body as a message request, and its documentation calls the result an estimate. The docs also say Claude 4.7 and later produce about 30% more tokens for the same text than earlier Claude models. Google's models.countTokens does the same job for Gemini. GPT-6 is in the same position for a different reason: tiktoken 0.14.0 has no entry for it, and OpenAI has not published its tokenizer. A local tokenizer also measures one string. A request adds role markers, separators, a system prompt, tool definitions, images and files. OpenAI's /v1/responses/input_tokens counts a complete request for that reason. Estimate first, then measure With only a character count, English prose runs about 4 characters per token; Chinese is roughly 0.5 to 1.0 token per character, Japanese 0.6 to 1.0, Korean 0.5 to 1.0. For this sample the Chinese band is 111 to 172 tokens. Use the low end for a sanity check, the high end for a limit you must not cross. For o200k_base , cl100k_base and DeepSeek V4 the vocabularies are downloadable, and this counter reproduces the reference ids: import tiktoken enc = tiktoken . get_encoding ( " o200k_base " ) ids = enc . encode_ordinary ( " What is a token in AI? " ) print ( len ( ids ), ids ) # 7 [4827, 382, 261, 6602, 306, 20837, 30] Use encode_ordinary() for user text: plain encode() raises ValueError when the text contains <|endoftext|> . For DeepSeek, load the official tokenizer.json from the offline package with the tokenizers library. In the guide's test, the package's own demo used transformers , but 5.18.0 returned an empty list for Chinese text while 4.57.6 and tokenizers 0.23.2 returned the expected ids. Reading limits and prices A context window is a maximum; the input limit is the number to divide by. gpt-4o is 128,000 tokens, gpt-5.5 is 1,050,000, claude-opus-5-5 is 1,000,000, gemini-3.1-pro-preview is 1,048,576, and text-embedding-3-small is 8,192 per input. Text that fills the window leaves no room for the answer, and the request adds instructions and formatting on top. Prices are per million tokens, input and output separately: cost = input_tokens × input_price / 1,000,000 + output_tokens × output_price / 1,000,000 The 192-character sample plus 1,000 output tokens costs $0.030665 on gpt-5.5 at $5 input and $30 output per million, and $0.0012333 on deepseek-flash at peak rates of $0.30 and $1.20. Output dominates both. Above 272,000 input tokens, gpt-5.5 and GPT-6 price the whole request at 2× input and 1.5× output; Gemini moves above 200,000. The whole request moves, not just the excess. DeepSeek charges half its peak rate outside peak hours. What I changed Four characters per token remains fine for English sanity checks. For CJK text, code, JSON or tables, I count with the tokenizer that will run the request, add the system prompt and tool schemas, then leave room for the answer. The 48-token estimate was not off by a rounding error; it was less than half of every real count on this text.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kassol/111-133-172-the-same-192-characters-in-three-tokenizers-lp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
