---
title: "Como impedir que um agente de programação faça mudanças destrutivas sem aprovação humana"
slug: "como-impedir-que-um-agente-de-programao-faa-mudanas-destrutivas-sem-aprovao-humana"
author: "Kusaki Werison"
source: "devto_ai"
published: "Sat, 19 Sep 2026 15:36:58 +0000"
description: "Agentes de programação reduzem drasticamente o tempo entre uma intenção e uma alteração real no projeto. Esse ganho também muda o tipo de risco. Quando um ag..."
keywords: "uma, como, com, rollback, que, agente, risco, quando"
generated: "2026-09-19T15:42:01.046390"
---

# Como impedir que um agente de programação faça mudanças destrutivas sem aprovação humana

## Overview

Agentes de programação reduzem drasticamente o tempo entre uma intenção e uma alteração real no projeto. Esse ganho também muda o tipo de risco. Quando um agente consegue editar dezenas de arquivos, executar comandos, instalar dependências ou alterar configuração em poucos segundos, a pergunta deixa de ser apenas: “Ele consegue fazer?” e passa a ser: “Ele tinha autoridade para fazer isso?” Uma estrutura mínima de governança pode reduzir essa ambiguidade sem transformar cada alteração em burocracia. 1. Autoridade deve ser explícita Uma regra útil é: Ausência de proibição não significa autorização. Separe as ações em três grupos: Autônomas Ações reversíveis e de baixo impacto, como: ler código; analisar erros; elaborar planos; executar testes existentes; propor patches. Com aprovação humana Ações como: excluir arquivos; alterar dependências; modificar produção; fazer deploy; publicar conteúdo; alterar permissões; executar operações destrutivas. Fora de escopo Quando a autoridade não está definida: STATUS: BLOCKED REASON: AUTHORITY_UNDEFINED NEXT: REQUEST_HUMAN_APPROVAL 2. Ações destrutivas precisam de um gate Antes de uma ação difícil de reverter, o agente deve demonstrar quatro coisas: qual é o impacto; qual é o caminho de rollback; por que a ação é necessária; que recebeu aprovação humana explícita. Sem esses quatro elementos, a execução para. Isso é diferente de simplesmente pedir “tenha cuidado”. O gate transforma cuidado em uma condição verificável. 3. Rollback vem antes da mudança Uma mudança segura não começa pelo patch. Ela começa respondendo: “Como voltamos ao estado anterior se isso der errado?” Dependendo do projeto, rollback pode significar: branch; commit; snapshot; backup; arquivo de configuração anterior; migration reversível; feature flag. Se não existe rollback e o impacto é relevante, o risco precisa subir de nível antes da execução. 4. “Concluído” exige evidência Um dos erros mais comuns em fluxos com agentes é transformar ausência de erro visível em sucesso. Uma regra simples: UNKNOWN != PASS O agente só deve declarar uma alteração como concluída quando houver evidência observável. Por exemplo: CLAIM: bug corrigido EVIDENCE: teste X passou + reprodução original não ocorre RESULT: PASS LIMITATIONS: não validado em produção Isso força a separação entre: implementação; validação; declaração de sucesso. 5. Use um ciclo previsível Um fluxo pequeno já ajuda bastante: PLAN → IMPLEMENT → VALIDATE → RELEASE PLAN define escopo, autoridade e risco. IMPLEMENT executa apenas o que foi autorizado. VALIDATE procura evidência e regressões. RELEASE só ocorre quando os gates relevantes foram satisfeitos. Starter gratuito Preparei um starter PT-BR com quatro arquivos pequenos: AGENT_AUTHORITY_POLICY.md HUMAN_APPROVAL_GATES.md PRE_CHANGE_CHECKLIST.md EVIDENCE_BEFORE_CLAIMS_MINI.md Repositório gratuito: https://github.com/werisonkusanagi-collab/safe-ai-coding-governance-starter-ptbr Kit completo Para quem precisa de uma estrutura reutilizável mais ampla, o Kit de Codificação Segura com IA — Governança de Agentes inclui: manual completo; guia rápido; policies; templates; workflows; checklists; exemplos; AGENTS.md ; CLAUDE.md ; rollback; regression validation; multi-agent review. Página do produto: https://kit-codificacao-segura-ia-governanca.lovable.app Preço atual: R$ 39,90 — pagamento único. Este material é uma camada de governança operacional. Ele não substitui permissões, sandboxing, backups, branch protection, gestão de credenciais, testes ou revisão técnica adequados ao risco do ambiente.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/werison-kusaki/como-impedir-que-um-agente-de-programacao-faca-mudancas-destrutivas-sem-aprovacao-humana-4hk6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
