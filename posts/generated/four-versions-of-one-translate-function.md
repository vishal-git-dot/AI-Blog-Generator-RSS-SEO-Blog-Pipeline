---
title: "Four versions of one translate() function"
slug: "four-versions-of-one-translate-function"
author: "Xiantao Cai"
source: "devto_webdev"
published: "Sun, 06 Sep 2026 14:47:54 +0000"
description: "I build Connexa, a chat product for cross-language teams: you write Chinese, your teammate reads English. I assumed translation was one function. The file no..."
keywords: "tone, translated, text, one, return, glossary, you, not"
generated: "2026-09-06T15:15:47.151459"
---

# Four versions of one translate() function

## Overview

I build Connexa, a chat product for cross-language teams: you write Chinese, your teammate reads English. I assumed translation was one function. The file now holds four versions of it, and each one exists because the previous one dropped something. v1: ten lines async translate ( text : string , targetLang : string ): Promise < string > { const slice = text . length > 12000 ? ` ${ text . slice ( 0 , 12000 )} …` : text ; return this . chat ([{ role : ' user ' , parts : [{ text : `Translate the following text into ${ targetLang } . Return only the translation, no explanations:\n\n ${ slice } ` }], }]); } The output was correct. The problem is that it translates sentences , not conversations . Example: 这个我看一下 → I'll take a look at this. Literally accurate. In Chinese that line is sometimes a polite refusal. The words arrived, the intent stayed behind. v2: make tone a field, not a hope The tempting fix is to ask for a "more natural" translation. That isn't controllable and isn't testable. Instead I made tone a schema-constrained field : generationConfig : { temperature : 0.3 , topP : 0.9 , maxOutputTokens : 2048 , responseMimeType : ' application/json ' , responseSchema : { type : ' OBJECT ' , properties : { translated : { type : ' STRING ' }, tone : { type : ' STRING ' }, }, required : [ ' translated ' ], }, } with a system instruction pinning the vocabulary: Tone should be a short lowercase label such as casual, formal, urgent, direct, friendly, sarcastic, frustrated, or neutral. Note required: ['translated'] — tone is optional on purpose. That matters in v5 below. Tone went from something I hoped the model conveyed into something I can render in the UI, store, and reason about. v3: context, and the bug it introduced A single message can't be translated without what came before it, so I appended the last 10 lines: const ctx = ( contextLines || []). filter ( Boolean ). slice ( - 10 ). join ( ' \n ' ); const parts = [ `Translate the following message into ${ targetLang } .` , glossaryText ? `Team glossary (use these terms):\n ${ glossaryText } ` : '' , ctx ? `Conversation context (tone/reference only):\n ${ ctx } ` : '' , `Message to translate:\n ${ slice } ` , ' Return ONLY the translation. ' , ]. filter ( Boolean ). join ( ' \n\n ' ); The bug: the model helpfully translates the context too. You ask for one translated line and get a translated transcript. (tone/reference only) is not a comment for human readers. It is the constraint. Remove that parenthetical and the return shape changes. v4: glossary, and the verb you use to introduce it If the same term renders as A in one message and B in the next, the conversation quietly desyncs. So: a per-team glossary, flattened line by line. const glossaryText = glossary && Object . keys ( glossary ). length ? Object . entries ( glossary ). map (([ k , v ]) => ` ${ k } → ${ v } ` ). join ( ' \n ' ) : '' ; The part worth noting is the wording change between versions: - `Team glossary (use these terms):\n${glossaryText}` + `Team glossary (must follow):\n${glossaryText}` I did not A/B this. I am not claiming a measured lift. I changed it because "use these terms" phrases a constraint as a suggestion, and I had no reason to keep it phrased that way. v5 is the fallback, and its direction matters Structured output fails sometimes. The question is what you drop when it does. try { const parsed = JSON . parse ( this . extractText ( await this . generateRaw ( body ))); return { translated : parsed ?. translated ?. trim () || fallbackText , tone : parsed ?. tone ?. trim () || null , }; } catch ( e ) { this . logger . warn ( `translateWithTone fallback: ${( e as Error ). message } ` ); return { translated : await this . chat ([{ role : ' user ' , parts : [{ text : prompt + ' \n\n Return only the translated text. ' }], }]), tone : null , }; } Drop to a plain-text request, return tone: null . In a chat product, translation is the primary path and tone is an enhancement. Degrade the enhancement, never the path. That is why tone was optional in the schema. What I'd keep Translation is not converting language A into B. It is reconstructing A's intent in B. The literal layer is the easiest part to move, which is why it gets finished first — and exactly why it is easy to believe you are done. Tone, prior context, and term consistency do not show up in the output on their own. Each one has to be added back deliberately, and each one costs you a prompt section and a failure mode. What is the last output you shipped that was correct and still wrong? Shorter versions of this appeared on LinkedIn and on my Chinese-language channels.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cxtao/four-versions-of-one-translate-function-4jea

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
