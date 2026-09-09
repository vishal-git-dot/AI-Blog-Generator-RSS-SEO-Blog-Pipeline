---
title: "Como Transformei o Armazenamento do Meu Site sem Mudar uma Linha do Frontend (e ainda deixei tudo mais seguro)"
slug: "como-transformei-o-armazenamento-do-meu-site-sem-mudar-uma-linha-do-frontend-e-ainda-deixei-tudo-mais-seguro"
author: "Alex Oliveira"
source: "devto_webdev"
published: "Wed, 09 Sep 2026 20:38:24 +0000"
description: "👋 Olá! Meu nome é Alex, sou Engenheiro de Software e entusiasta de arquitetura de sistemas. Atualmente focado em resolver problemas reais com código limpo e ..."
keywords: "para, que, como, com, uma, mais, imagens, wwwroot"
generated: "2026-09-09T20:46:26.461826"
---

# Como Transformei o Armazenamento do Meu Site sem Mudar uma Linha do Frontend (e ainda deixei tudo mais seguro)

## Overview

👋 Olá! Meu nome é Alex, sou Engenheiro de Software e entusiasta de arquitetura de sistemas. Atualmente focado em resolver problemas reais com código limpo e infraestrutura inteligente. Acompanhe meus artigos para ver como transformo desafios complexos em soluções pragmáticas. Se tem uma coisa que incomoda qualquer desenvolvedor web é ver o repositório do projeto crescendo descontroladamente por causa de imagens e documentos. Foi exatamente esse o ponto de partida da minha jornada técnica mais recente. O Cenário (ou o "Caos Controlado" inicial) Até ontem, o site funcionava de um jeito clássico: tudo na wwwroot . Quando precisávamos adicionar uma foto nova ao catálogo, ela ia direto para a pasta do projeto. Isso parecia prático no início, mas rapidamente se tornou um pesadelo: o repositório do Git ficou pesado, o deploy demorava uma eternidade e clonar o repositório também. O estopim foi quando decidimos migrar para um serviço de armazenamento open-source externo . Ele era ótimo, barato e escalável, mas tinha um detalhe: exigia autenticação até para os GETs . Ou seja, para exibir uma simples imagem pública, eu precisava de um token de autorização. E aqui vinha o grande dilema: se eu colocasse o link direto do storage no HTML, o navegador bateria de frente com um 401 Unauthorized . Se eu deixasse na wwwroot , eu não usaria o storage. Como resolver isso sem reescrever o frontend inteiro? A Solução (Primeira Fase): O "Proxy de Mídia" com Interceptação Inteligente A ideia foi simples na teoria, mas deliciosa na prática: transformar o próprio Backend em um Proxy Autenticado . Criei um Middleware/Controller que intercepta todas as requisições que antes iam para a wwwroot (como /imagens/* e /documentos/* ). Em vez de o servidor procurar o arquivo no disco, ele "segura" a requisição e assume o controle total do processo. O fluxo ficou assim: O usuário acessa a URL que sempre acessou (ex: www.meusite.com/imagens/carro.jpg ). Transparência total. O Backend recebe a requisição, mas não vai na wwwroot em busca do arquivo. Ele pega o access_token que está guardado em memória (em uma variável estática/Singleton) no servidor, gerenciado com renovação automática via credenciais do .env . Com esse token, ele abre uma requisição HTTP interna (servidor-para-servidor) para o storage externo, baixa os bytes da imagem. Por fim, ele devolve esses bytes para o navegador com o Content-Type correto, como se o arquivo estivesse ali fisicamente. A Jornada é Gradual (E tudo bem!) É importante destacar que essa foi a primeira etapa da arquitetura. Resolvemos o problema da leitura e exibição (GET) do catálogo de imagens. Portanto, neste exato momento, os uploads de imagens feitos pelos usuários no site ainda continuam sendo salvos localmente na wwwroot . O próximo passo do projeto é justamente adaptar o endpoint de upload para que, em vez de escrever no disco, ele faça um POST autenticado diretamente para o storage externo. Quando essa fase estiver concluída, aí sim teremos o desacoplamento total e a wwwroot finalmente ficará livre de arquivos gerados pelos usuários — restando apenas os arquivos estáticos essenciais (CSS, JS e fontes). Os Ganhos (Mesmo na Fase Inicial) Mesmo sendo uma implementação parcial, os benefícios já são enormes: Repositório Levíssimo : Os arquivos do catálogo (que não eram gerados por upload, mas sim estáticos do projeto) já saíram do repositório. O Git clona em segundos e os deploys ficaram muito mais rápidos. Armazenamento Escalável : As imagens pesadas do catálogo agora estão em um storage dedicado. Podemos guardar gigabytes sem preocupação com o espaço finito do servidor. Segurança Total : O token de autorização do storage nunca, em hipótese alguma, chega ao navegador. Ele fica restrito à memória do servidor. Mesmo que alguém inspecione o tráfego, só verá a requisição para o meu domínio, e não para o storage original. Transparência e Migração Zero : Como a URL permaneceu idêntica ( /imagens/foto.jpg ), o frontend não precisou ser reescrito. O usuário final nem percebeu a mudança nos bastidores — exatamente como deve ser. Aprendizado Final Essa implementação me lembrou que, às vezes, a melhor solução não está em mudar a interface do usuário, mas sim em engenhar o fluxo de dados nos bastidores. E, mais do que isso, me ensinou a valorizar a entrega incremental . Resolvemos a dor mais urgente (a wwwroot gorda e o acesso autenticado para GETs) sem paralisar o projeto. O upload e outras boas práticas, como mecanismos de performance, virão nas próximas iterações. No fim das contas, engenharia de software é sobre fazer escolhas conscientes e resolver problemas na ordem certa — e hoje, o site está mais leve, mais seguro e pronto para o próximo passo. 🤖 Transparência Tecnológica: Este artigo foi desenvolvido com o suporte de Inteligência Artificial generativa (Co-Authored By AI), que atuou como meu "pair programmer" para revisar conceitos e agilizar a escrita. A curadoria final, a validação técnica de cada linha de código e a responsabilidade sobre as decisões arquiteturais são 100% minhas.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alekswheeler/como-transformei-o-armazenamento-do-meu-site-sem-mudar-uma-linha-do-frontend-e-ainda-deixei-tudo-hh4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
