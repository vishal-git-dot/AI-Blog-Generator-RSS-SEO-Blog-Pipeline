---
title: "Tutorial Profundo: Rastreabilidade Total no Apache Airflow com OpenLineage"
slug: "tutorial-profundo-rastreabilidade-total-no-apache-airflow-com-openlineage"
author: "BIX"
source: "devto_python"
published: "Fri, 21 Aug 2026 18:36:47 +0000"
description: "No ecossistema atual de Engenharia de Dados, a observabilidade (Data Observability) é o que separa pipelines maduros de sistemas que operam na base da espera..."
keywords: "airflow, openlineage, que, dag, marquez, para, apache, dados"
generated: "2026-08-21T18:43:06.893610"
---

# Tutorial Profundo: Rastreabilidade Total no Apache Airflow com OpenLineage

## Overview

No ecossistema atual de Engenharia de Dados, a observabilidade (Data Observability) é o que separa pipelines maduros de sistemas que operam na base da esperança. Saber que uma DAG falhou no Apache Airflow é o básico; o desafio real de governança é saber instantaneamente quais tabelas no Data Warehouse , quais modelos de ML e quais dashboards de diretoria foram impactados por essa falha. Para resolver isso sem precisar escrever logs customizados em cada task, o padrão de mercado atual é o OpenLineage : um framework open-source de observabilidade de dados. Neste tutorial prático, vamos instrumentar o Apache Airflow para emitir eventos de linhagem automaticamente para o Marquez (o servidor backend de referência do OpenLineage). Entendendo a Arquitetura O OpenLineage não "lê" o seu banco de dados. Em vez disso, o Airflow atua como um emissor. Sempre que uma task começa ou termina, os Extractors nativos do Airflow analisam o código SQL executado, identificam as tabelas de origem e destino (Inputs e Outputs) e disparam um evento JSON padronizado para o servidor do Marquez. Passo 1: Subindo a infraestrutura completa (Docker-Compose) Vamos subir um ambiente local contendo o Marquez (API e UI) e o Airflow configurado via variáveis de ambiente. `version: '3.8' services: # O servidor backend que coleta e desenha a linhagem marquez: image: marquezproject/marquez:latest ports: - "5000:5000" # API do OpenLineage - "5001:5001" # Interface Web # Instância do Airflow configurada para apontar para o Marquez airflow: image: apache/airflow:2.8.0 environment: - AIRFLOW_ CORE LOAD_EXAMPLES=False - OPENLINEAGE_URL= http://marquez:5000 - OPENLINEAGE_NAMESPACE=meu_pipeline_producao - AIRFLOW OPENLINEAGE _DISABLED=False ports: - "8080:8080" command: standalone ` Passo 2: Instalando o Provider no Airflow O suporte ao OpenLineage é nativo nas versões modernas do Airflow, mas você precisa garantir que o provider está instalado no seu ambiente: pip install apache-airflow-providers-openlineage Passo 3: Criando uma DAG Rastreável A mágica do OpenLineage é que ele requer zero alterações na lógica de negócios da sua DAG. Veja este exemplo simulando um ETL simples no PostgreSQL: Validando o Resultado Assim que a DAG for executada com sucesso, abra o seu navegador em http://localhost:5001 (Marquez UI). Você não verá apenas logs de execução, mas um grafo visual (DAG de dados, não de tarefas) mostrando que o dataset stg_vendas.transacoes_brutas é upstream do dataset dm_vendas.faturamento_diario. Se a tabela de staging dropar, você sabe exatamente qual métrica de faturamento vai quebrar amanhã de manhã. Implementar o OpenLineage é um quick win massivo para a engenharia: poucas linhas de configuração de infraestrutura geram um mapa de dependências que salva horas de troubleshooting no futuro. Versão completa disponível no link . `from airflow import DAG from airflow.providers.postgres.operators.postgres import PostgresOperator from datetime import datetime default_args = { 'owner': 'data_engineering_team', 'start_date': datetime(2026, 8, 1), } with DAG( 'processamento_vendas_diarias', default_args=default_args, schedule_interval='@daily', catchup=False ) as dag: # O OpenLineage Extractor vai ler este SQL, dar parse no "INSERT INTO" e no "SELECT FROM", # e criar a linhagem automaticamente relacionando as duas tabelas. transform_data = PostgresOperator( task_id='transform_sales', postgres_conn_id='postgres_default', sql=""" INSERT INTO dm_vendas.faturamento_diario SELECT data_venda, SUM(valor) as receita_total FROM stg_vendas.transacoes_brutas WHERE status = 'pago' GROUP BY data_venda; """ ) `

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bixtecnologia/tutorial-profundo-rastreabilidade-total-no-apache-airflow-com-openlineage-19fa

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
