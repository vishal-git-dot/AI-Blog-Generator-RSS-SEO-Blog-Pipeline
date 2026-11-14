---
title: "Do your tests really catch bugs? / Seus testes pegam erro de verdade?"
slug: "do-your-tests-really-catch-bugs-seus-testes-pegam-erro-de-verdade"
author: "Arthur Figueiredo"
source: "devto_python"
published: "Sat, 14 Nov 2026 21:54:34 +0000"
description: "I measured this together with Claude, ran research and tests, and built a garden about whether tests really catch bugs. The idea is simple: a test can pass a..."
keywords: "com, garden, que, tests, testes, step, digital, passo"
generated: "2026-11-14T22:10:54.921131"
---

# Do your tests really catch bugs? / Seus testes pegam erro de verdade?

## Overview

I measured this together with Claude, ran research and tests, and built a garden about whether tests really catch bugs. The idea is simple: a test can pass and still be weak. To find out how weak, I broke the code on purpose and counted how many bugs the tests let through. Then I did the same for each step of my AI workflow, from the spec (the text that describes what the code should do) to the commit. In the garden, each step has its own number, and the ideas that didn't pay off are there too. There is one note just for what I still don't know, because the study is small, comes from a few projects, and nobody outside has checked it. And there is a step-by-step to repeat the measurement on your own project. "A digital garden is a site of linked notes that the author keeps tending over time. It accepts unfinished notes and shows it, with a badge for how well each one is proven." If you want to take a look: Digital-Garden 🇧🇷 Eu medi isso junto com o Claude, fiz pesquisas e testes, e criei um jardim sobre se os testes pegam erro de verdade. A ideia é simples: um teste pode passar e ainda assim ser fraco. Para saber o quanto, estraguei o código de propósito e contei quantos erros os testes deixaram passar. Depois fiz o mesmo com cada passo do meu fluxo de trabalho com IA, da spec (o texto que descreve o que o código deve fazer) até o commit. No jardim, cada passo tem o seu número, e as ideias que não compensaram também estão lá. Tem uma nota só com o que eu ainda não sei, porque o estudo é pequeno, vem de poucos projetos e ninguém de fora conferiu. E tem um passo a passo para repetir a medida no seu projeto. "Jardim digital é um site de notas ligadas entre si, que o autor continua cuidando com o tempo. Ele aceita nota inacabada e mostra isso, com um selo de quanto cada uma está provada." Se quiser olhar: Digital-Garden

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/arthur2122/do-your-tests-really-catch-bugs-seus-testes-pegam-erro-de-verdade-4560

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
