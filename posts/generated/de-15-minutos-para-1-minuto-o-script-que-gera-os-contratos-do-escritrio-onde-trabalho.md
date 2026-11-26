---
title: "De 15 minutos para 1 minuto: o script que gera os contratos do escritório onde trabalho"
slug: "de-15-minutos-para-1-minuto-o-script-que-gera-os-contratos-do-escritrio-onde-trabalho"
author: "Gabriel Victor"
source: "devto_python"
published: "Thu, 26 Nov 2026 20:54:48 +0000"
description: "Trabalho num escritório de advocacia previdenciária desde janeiro e estou no 2º semestre de Engenharia de Software. Todo cliente novo precisa de um contrato,..."
keywords: "que, para, contrato, script, por, com, cliente, modelo"
generated: "2026-11-26T21:14:22.325271"
---

# De 15 minutos para 1 minuto: o script que gera os contratos do escritório onde trabalho

## Overview

Trabalho num escritório de advocacia previdenciária desde janeiro e estou no 2º semestre de Engenharia de Software. Todo cliente novo precisa de um contrato, e quase todos passam pela minha mão: são de 10 a 15 por semana. Fazer um contrato à mão levava uns 15 minutos. Abrir o modelo no Word, trocar nome, CPF, endereço e benefício, conferir tudo e mandar imprimir. Parece pouco, mas são de duas horas e meia a quase quatro horas por semana fazendo a mesma coisa, e cada digitação é uma chance de errar um número de CPF. Hoje o mesmo contrato sai em cerca de 1 minuto. Vou contar como cheguei nisso, incluindo o que deu errado no caminho. A primeira tentativa: deixar a IA fazer tudo Minha primeira ideia foi pedir para a IA editar os documentos direto. Funcionou mais ou menos: chegou a levar 20 minutos para 3 documentos, mandou para a impressora errada e uma vez gerou um contrato com um dado faltando. Para um documento que o cliente vai assinar, "mais ou menos" não serve. O que eu aprendi ali: para uma tarefa que se repete sempre igual, um script é melhor do que a IA. O script faz a mesma coisa toda vez. A IA, não. A descoberta que simplificou tudo Quando fui organizar os modelos, achei que eram 11 contratos diferentes, um para cada benefício. Olhando com calma, era um contrato só : o que mudava era o nome do benefício. E os outros documentos do kit (procuração, declarações) usavam o mesmo bloco com os dados do cliente. Isso virou a base do projeto: um modelo, com marcadores no lugar dos dados ( {{NOME}} , {{CPF}} , {{ENDERECO}} , {{BENEFICIO}} ...), e um script que troca cada marcador pelo dado certo. Como montei Eu não escrevi o código sozinho, e não escondo isso. O que fiz foi: Escrever o passo a passo em português, antes de qualquer código: PARA cada contrato novo: ler os dados da ficha do cliente SE faltar um campo obrigatório: avisar o que falta e parar abrir o modelo aprovado pelos advogados trocar cada marcador pelo dado salvar na pasta do cliente mandar para a impressora certa Usar o Claude Code para transformar esse passo a passo num script em Python. Testar com casos reais, conferindo campo por campo. Achar os erros e pedir as correções até o resultado sair igual todas as vezes. A IA continua no processo, mas só numa parte: ela me ajuda a reunir os dados da ficha. O texto do contrato vem sempre do modelo que os advogados aprovaram, nunca da IA. Os detalhes que deram trabalho Masculino e feminino. O contrato diz "inscrito" ou "inscrita", "domiciliado" ou "domiciliada". O script descobre pelo estado civil informado na ficha (viúvo ou viúva, casado ou casada). Campo faltando. Antes de gerar, o script confere se todos os campos obrigatórios estão preenchidos. Se falta algum, ele para e avisa, em vez de gerar um contrato pela metade. Outro computador. Levei o sistema para outra máquina sem padronizar nada antes, e lá o resultado saiu diferente. Hoje eu padronizo tudo primeiro. E todo contrato ainda passa por uma pessoa antes de ser assinado. O resultado Antes Depois Tempo por contrato ~15 minutos ~1 minuto Contratos por semana 10 a 15 10 a 15 Tempo por semana 2h30 a 3h45 10 a 15 minutos Quer ver funcionando? O código e os modelos do escritório não podem ser públicos, porque envolvem dados de clientes. Então fiz uma demonstração com um modelo e um cliente fictícios, que roda direto no navegador e segue o mesmo caminho: ler a ficha, conferir os campos, abrir o modelo, trocar os marcadores e entregar o contrato. 👉 Testar a demonstração O que eu levo disso Antes de pensar em ferramenta, vale olhar para o problema com calma. A descoberta de que eram um contrato só, e não onze, poupou mais trabalho do que qualquer linha de código. E usar IA para programar não tira a responsabilidade de quem publica: sou eu que testo, acho os erros e respondo pelo resultado. Se você também trabalha num lugar cheio de tarefas repetitivas, comece anotando quanto tempo cada uma leva. É ali que estão os primeiros projetos.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gabrielvictorcruz/de-15-minutos-para-1-minuto-o-script-que-gera-os-contratos-do-escritorio-onde-trabalho-1hb6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
