---
title: "Qdrant Recall Inconsistency: It Took 300 Test Runs to Discover the Index Wasn't Refreshed"
slug: "qdrant-recall-inconsistency-it-took-300-test-runs-to-discover-the-index-wasnt-refreshed"
author: "BAOFUFAN"
source: "devto_python"
published: "Sun, 16 Aug 2026 01:05:06 +0000"
description: "At 2 AM, a user reported that the AI Agent suddenly forgot details of a project we discussed yesterday. I groggily opened Grafana and saw the memory recall r..."
keywords: "recall, client, qdrant, collection, test, index, import, points"
generated: "2026-08-16T01:41:13.468051"
---

# Qdrant Recall Inconsistency: It Took 300 Test Runs to Discover the Index Wasn't Refreshed

## Overview

At 2 AM, a user reported that the AI Agent suddenly forgot details of a project we discussed yesterday. I groggily opened Grafana and saw the memory recall rate had dropped from 98% to 60%. My first thought was the embedding model acting up again, but after digging through logs, I found a "time gap" between Qdrant writes and queries—data was upserted, yet queries intermittently returned nothing. This wasn't the first time, so I decided to automate recall consistency testing with pytest + Qdrant, and discovered the pitfalls were deeper than expected. Problem Breakdown The AI Agent's memory storage uses Qdrant to store vectors and payloads, with the core requirement of "immediately recallable after write." But in real scenarios, recall inconsistency is weird: local tests all pass, but CI occasionally fails; the same query, executed twice in a row, yields different results. The root cause is that Qdrant's write and index building are asynchronous—the upsert method returns without waiting for index refresh by default, so subsequent queries may read empty or partial results. A common workaround is manually adding time.sleep(2) in code, but that's not engineering practice, and the sleep duration is unpredictable—treating the symptom, not the cause. Worse, recall consistency also involves distance metrics and score threshold choices; a careless test assertion can mislead you. Design I chose pytest as the testing framework because its fixtures and parametrization are great for isolation and covering multiple scenarios. Qdrant's official Python client supports :memory: mode, so each test case gets a clean vector database instance fully isolated—no mocks needed; mocks can't reveal real index behavior. Why not unittest? Because fixture cleanup and parametrization are too verbose. Why not mock? Because we need to verify real Qdrant recall behavior; mocks only hide the async index problem. Architecturally, I define a qdrant_client fixture in conftest.py ; each test automatically creates an independent collection and cleans it up after. Core tests cover three scenarios: single-point recall, batch-write recall, and recall with payload filters. Core Implementation This code solves test environment isolation, ensuring each test uses an independent Qdrant instance and collection. # conftest.py import pytest from qdrant_client import QdrantClient from qdrant_client.models import VectorParams , Distance @pytest.fixture def qdrant_client (): # 内存模式：每个测试完全隔离，不落盘，速度快 client = QdrantClient ( " :memory: " ) yield client client . close () @pytest.fixture def mem_collection ( qdrant_client ): collection_name = " agent_memory_test " # 向量维度 3，余弦距离 qdrant_client . create_collection ( collection_name = collection_name , vectors_config = VectorParams ( size = 3 , distance = Distance . COSINE ) ) return qdrant_client , collection_name This code exposes the first pitfall: querying immediately after a direct upsert gives unstable recall results. # test_recall_failure.py import pytest from qdrant_client.models import PointStruct def test_immediate_recall_without_wait ( mem_collection ): client , collection = mem_collection # 写入一条向量，注意：没有 wait=True client . upsert ( collection_name = collection , points = [ PointStruct ( id = 1 , vector = [ 0.1 , 0.2 , 0.3 ], payload = { " user " : " alice " })] ) # 立即查询相同向量，期望能召回 result = client . query_points ( collection_name = collection , query = [ 0.1 , 0.2 , 0.3 ], limit = 1 ) # 这一行经常失败：result.points 为空 assert len ( result . points ) == 1 Running this test, it fails 6 out of 10 times with AssertionError: assert 0 == 1 . That's exactly the cause of online recall rate jitter. This code fixes the index refresh problem: wait=True forces the client to wait for the index to be ready before querying. # test_recall_fix.py import time from qdrant_client.models import PointStruct , VectorParams , Distance def test_immediate_recall_with_wait ( mem_collection ): client , collection = mem_collection # 关键参数：wait=True，确保写入后索引刷新完成 client . upsert ( collection_name = collection , points = [ PointStruct ( id = 1 , vector = [ 0.1 , 0.2 , 0.3 ], payload = { " user " : " alice " })], wait = True # 官方文档没明说，但这是解决异步索引的关键 ) # 现在查询稳定返回结果 result = client . query_points ( collection_name = collection , query = [ 0.1 , 0.2 , 0.3 ], limit = 1 ) assert len ( result . points ) == 1 assert result . points [ 0 ]. id == 1 # 还可以进一步验证 payload 一致性 assert result . points [ 0 ]. payload [ " user " ] == " alice " If you don't want to add wait=True to every call, you can...

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/_eb7f2a654e97a60ae9f96e/qdrant-recall-inconsistency-it-took-300-test-runs-to-discover-the-index-wasnt-refreshed-3agf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
