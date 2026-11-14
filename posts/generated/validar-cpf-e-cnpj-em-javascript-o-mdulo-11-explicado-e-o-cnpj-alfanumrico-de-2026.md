---
title: "Validar CPF e CNPJ em JavaScript: o módulo 11 explicado (e o CNPJ alfanumérico de 2026)"
slug: "validar-cpf-e-cnpj-em-javascript-o-mdulo-11-explicado-e-o-cnpj-alfanumrico-de-2026"
author: "Doit Follow"
source: "devto_webdev"
published: "Sat, 14 Nov 2026 21:59:17 +0000"
description: "Se você já montou um formulário de cadastro no Brasil, já precisou validar CPF e CNPJ no front-end antes de enviar os dados. A boa notícia: a regra é pública..."
keywords: "cnpj, cpf, resto, que, regra, base, pesos, com"
generated: "2026-11-14T22:10:54.922836"
---

# Validar CPF e CNPJ em JavaScript: o módulo 11 explicado (e o CNPJ alfanumérico de 2026)

## Overview

Se você já montou um formulário de cadastro no Brasil, já precisou validar CPF e CNPJ no front-end antes de enviar os dados. A boa notícia: a regra é pública, determinística e cabe em poucas linhas de JavaScript — os dois documentos usam o módulo 11 para gerar os dígitos verificadores. Neste artigo eu explico a conta passo a passo, mostro a implementação e ainda cubro a mudança que chega em 2026: o CNPJ alfanumérico . CPF: 9 dígitos + 2 verificadores Um CPF tem 11 dígitos. Os 9 primeiros são a base; os 2 últimos são calculados assim: Primeiro verificador: multiplique os 9 dígitos pelos pesos 10, 9, 8 … 2 , some tudo e divida por 11. Se o resto for 0 ou 1, o dígito é 0 ; senão, é 11 − resto . Segundo verificador: repita com os 10 primeiros dígitos (incluindo o verificador que você acabou de calcular) e os pesos 11, 10, 9 … 2 , com a mesma regra. Exemplo real, com o CPF fictício 111.444.777-35 : 1×10 + 1×9 + 1×8 + 4×7 + 4×6 + 4×5 + 7×4 + 7×3 + 7×2 = 162 → 162 ÷ 11 tem resto 8 → dígito = 11 − 8 = 3 ✓ 1×11 + 1×10 + 1×9 + 4×8 + 4×7 + 4×6 + 7×5 + 7×4 + 7×3 + 3×2 = 204 → resto 6 → dígito = 11 − 6 = 5 ✓ Os dois dígitos conferem: o CPF é válido pela regra matemática . function validarCPF ( cpf ) { const d = cpf . replace ( / \ D / g , "" ) ; if ( d . length !== 11 || /^ ( \ d ) \ 1 { 10 } $ / . test ( d ) ) return false ; const digito = ( base , pesoInicial ) => { let soma = 0 ; for ( let i = 0 ; i < base . length ; i ++ ) soma += Number ( base [ i ] ) * ( pesoInicial - i ) ; const resto = ( soma * 10 ) % 11 ; return resto === 10 || resto === 11 ? 0 : resto ; } ; return digito ( d . slice ( 0 , 9 ) , 10 ) === Number ( d [ 9 ] ) && digito ( d . slice ( 0 , 10 ) , 11 ) === Number ( d [ 10 ] ) ; } validarCPF ( "111.444.777-35" ) ; // true validarCPF ( "111.444.777-34" ) ; // false — trocou um dígito, quebrou a conta validarCPF ( "111.111.111-11" ) ; // false — sequência repetida (ver abaixo) A pegadinha: dígitos repetidos "passam" na conta Sequências como 111.111.111-11 e 000.000.000-00 satisfazem o módulo 11, mas nenhum CPF real é assim — por isso a validação precisa rejeitá-las explicitamente (é o regex /^(\d)\1{10}$/ no código acima). Esquecer esse passo é o erro mais comum que vejo em implementações por aí. CNPJ: os pesos "andam" de 2 a 9 O CNPJ tem 14 dígitos (12 de base + 2 verificadores). A lógica é a mesma, mas os pesos não descem de 13 e 12: eles ciclam de 2 a 9 , da direita para a esquerda. Para o primeiro verificador, os pesos sobre os 12 dígitos são 5 4 3 2 9 8 7 6 5 4 3 2 ; para o segundo, sobre 13 dígitos, 6 5 4 3 2 9 8 7 6 5 4 3 2 . A regra do resto muda um pouco: se soma % 11 < 2 , o dígito é 0; senão, é 11 − (soma % 11) . 2026: o CNPJ alfanumérico A partir de julho de 2026 , novos CNPJs poderão ter letras nas 12 primeiras posições (os 2 verificadores continuam numéricos). A validação quase não muda: cada caractere vira um valor numérico pelo código ASCII menos 48 — dígitos valem o próprio valor ( 0 – 9 ) e letras valem de 17 em diante ( A = 65 − 48 = 17, B = 18, …). Depois disso, é o mesmo módulo 11 com os mesmos pesos. Exemplo calculado com essa regra: a base 12.ABC.345/01DE vira os valores 1, 2, 17, 18, 19, 3, 4, 5, 0, 1, 20, 21 , e os verificadores resultantes são 3 e 5 — ou seja, o CNPJ completo 12.ABC.345/01DE-35 é válido pela nova regra. Se o seu sistema valida CNPJ, vale adaptar o código agora: basta trocar o Number(d[i]) por d.charCodeAt(i) - 48 e parar de rejeitar letras na máscara. Validar não é consultar Um último cuidado, que confunde muita gente: passar no módulo 11 só prova que o número respeita a regra matemática . Não prova que o documento existe, pertence a alguém ou está regular na Receita Federal — isso só a consulta oficial confirma. Validação client-side serve para pegar erro de digitação cedo e melhorar a experiência do formulário; situação cadastral é outra camada. Quer testar sem escrever código? No JeitoBR — um site de ferramentas gratuitas que eu mantenho — o validador de CPF e o validador e consulta de CNPJ rodam 100% no navegador, com a mesma lógica deste artigo (o de CNPJ já consulta a situação na Receita). Se você encontrar algum caso em que a sua implementação discorda da minha, me conta nos comentários — adoro um edge case novo.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jeitobr/validar-cpf-e-cnpj-em-javascript-o-modulo-11-explicado-e-o-cnpj-alfanumerico-de-2026-5282

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
