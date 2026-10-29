---
title: "Script em Python pra validar margem antes de abrir sua loja online"
slug: "script-em-python-pra-validar-margem-antes-de-abrir-sua-loja-online"
author: "Nuvem Dev"
source: "devto_python"
published: "Thu, 29 Oct 2026 12:06:33 +0000"
description: "Antes de pagar qualquer plataforma de loja (Shopify, Nuvemshop, tanto faz), eu faria uma conta: sobra quanto por venda? Segue um script curto que eu rodei aq..."
keywords: "preco, margem, custo, shopify, frete, com, link, script"
generated: "2026-10-29T12:39:59.114830"
---

# Script em Python pra validar margem antes de abrir sua loja online

## Overview

Antes de pagar qualquer plataforma de loja (Shopify, Nuvemshop, tanto faz), eu faria uma conta: sobra quanto por venda? Segue um script curto que eu rodei aqui. O script def margem ( preco , custo , frete , taxa_pct = 0.0499 , taxa_fixa = 0.60 , imposto_pct = 0.06 ): taxas = preco * taxa_pct + taxa_fixa imposto = preco * imposto_pct lucro = preco - custo - frete - taxas - imposto return round ( lucro , 2 ), round ( lucro / preco * 100 , 1 ) if __name__ == " __main__ " : for preco in ( 79.9 , 99.9 , 129.9 ): print ( preco , margem ( preco , custo = 35 , frete = 18 )) Saída real 79.9 (17.52, 21.9) 99.9 (35.32, 35.4) 129.9 (62.02, 47.7) Com custo de R$ 35 e frete de R$ 18, vender a R$ 79,90 deixa só 21,9% de margem. A R$ 99,90 já vai pra 35%. As taxas (4,99% + R$ 0,60) e o imposto (6%) são valores de exemplo: troque pelos do seu gateway e do seu regime. Próximo passo Se a margem fechou, aí sim vale testar uma plataforma. A Shopify tem teste de 3 dias grátis e depois US$ 1/mês por 3 meses (confira na página oficial, promoção muda), e o Shopify Magic, que escreve descrição de produto, é gratuito segundo a central de ajuda deles. Link do teste: https://go.nowto.link/shopify Contei a versão em newsletter, com vídeo curto, aqui: https://nuvemdev.substack.com . E sobre IA e privacidade, escrevi sobre VPN: https://nuvemdev.substack.com/p/vpn-protege-o-que-voce-digita-na Aviso: este post contém link de afiliado. Se você assinar pelo link, a Nuvem Dev pode receber uma comissão, sem custo extra pra você.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nuvemdev/script-em-python-pra-validar-margem-antes-de-abrir-sua-loja-online-4cc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
