---
title: "AI memory가 자기 출력을 다시 입력으로 세지 않게 하는 법"
slug: "ai-memory"
author: "박준현"
source: "devto_ai"
published: "Thu, 16 Jul 2026 13:55:57 +0000"
description: "AI memory가 자기 출력을 다시 입력으로 세지 않게 하는 법 AI memory 시스템은 대화에서 기억을 만들고, 그 기억을 다시 요약해 더 높은 수준의 결론을 만들 수 있습니다. 여기서 원본에 가까운 입력과 시스템이 만든 파생 결과를 구분하지 않으면, 파생 결과가 다음 작업의..."
keywords: "explicit, pinned, pending, checkpoint, threshold, deductive, derived, memory"
generated: "2026-07-16T14:05:41.532835"
---

# AI memory가 자기 출력을 다시 입력으로 세지 않게 하는 법

## Overview

AI memory가 자기 출력을 다시 입력으로 세지 않게 하는 법 AI memory 시스템은 대화에서 기억을 만들고, 그 기억을 다시 요약해 더 높은 수준의 결론을 만들 수 있습니다. 여기서 원본에 가까운 입력과 시스템이 만든 파생 결과를 구분하지 않으면, 파생 결과가 다음 작업의 trigger를 키우는 self-reinforcing loop가 생길 수 있습니다. 이 글은 AI memory OSS Honcho의 PR #573과 pinned source를 읽으며, 이런 feedback pressure를 입력 eligibility, 성공 checkpoint, in-flight state로 나눠 해결한 방식을 추적한 기록입니다. Scenario Honcho의 dreamer는 collection(observer-observed 쌍마다 memory document가 쌓이는 묶음)에 있는 document를 바탕으로 더 높은 수준의 관찰을 만듭니다. Document에는 여러 level이 있습니다. explicit 원문에서 직접 도출된 관찰 deductive 기존 관찰에서 연역한 결과 inductive 여러 관찰에서 귀납한 결과 contradiction 서로 충돌하는 관찰을 표현한 결과 dreamer가 실행되면 deductive, inductive, contradiction 같은 새로운 document가 생길 수 있습니다. 동시에 scheduler는 collection에 document가 일정 개수 이상 추가되면 다음 dream을 예약합니다. 문제는 무엇을 "새 입력"으로 셀 것인가 입니다. 변경 전: 모든 document가 같은 trigger에 들어갔다 PR #573 직전의 check_and_schedule_dream 은 workspace와 observer/observed만으로 document 수를 계산했습니다. level 조건이 없었기 때문에 explicit input뿐 아니라 이전 dream이 만든 derived output도 threshold에 포함됐습니다. 예를 들어 threshold가 50일 때 다음 collection을 생각할 수 있습니다. explicit 30 deductive 40 inductive 10 ---------------- 전체 document 80 새로운 explicit 관찰은 30개뿐이지만 전체 count는 80이므로 scheduler 조건을 통과할 수 있습니다. 이전 dream의 출력이 다음 dream의 trigger를 키우는 구조입니다. 이것만으로 production에서 무한 실행이 발생했다고 단정할 수는 없습니다. 시간 간격 제한과 queue deduplication 같은 다른 gate도 있기 때문입니다. 여기서 source와 regression test로 확인한 것은 derived output이 trigger count를 스스로 증가시킬 수 있었던 eligibility 오류 입니다. 첫 번째 경계: source-like input만 센다 변경 후 threshold query는 Document.level == "explicit" 조건을 사용합니다. current_explicit_count - last_dream_document_count >= threshold deductive, inductive, contradiction document는 검색과 추론에는 계속 사용할 수 있지만, 다음 consolidation을 시작시키는 새 입력으로는 세지 않습니다. 저장 여부와 scheduling eligibility를 분리한 것입니다. pinned current code에서는 실행할 session을 고를 때도 최신 explicit document만 봅니다. threshold는 explicit 기준 집합으로 계산하면서 실행 context는 더 최신인 derived document의 session에서 가져오는 비대칭을 피하기 위한 조치입니다. 두 번째 경계: enqueue가 아니라 성공 뒤에 checkpoint한다 변경 전 enqueue_dream 은 queue에 작업을 넣으면서 다음 두 값을 바로 기록했습니다. last_dream_document_count last_dream_at 하지만 enqueue는 작업이 실행되거나 유효한 결과를 만들었다는 뜻이 아닙니다. 실패한 작업이 baseline을 먼저 전진시키면 같은 corpus를 다시 시도할 근거를 잃을 수 있습니다. 현재 코드는 enqueue 단계에서 dream metadata를 건드리지 않습니다. process_dream 이 non-null result를 받은 뒤에만 row lock을 잡고 현재 explicit count를 다시 계산해, count와 timestamp를 함께 기록합니다. enqueue in-flight 상태만 생성 run_dream 실패 checkpoint 유지 run_dream 성공 explicit count + 완료 시각을 함께 전진 이때 "성공"은 result is not None 이라는 현재 코드의 비교적 관대한 기준입니다. 생성된 memory의 의미적 품질이나 정확성까지 보장하는 quality gate는 아닙니다. 세 번째 경계: 실행 중 상태는 queue가 소유한다 checkpoint를 완료 뒤로 미루면 새 문제가 생깁니다. 첫 dream이 아직 실행 중일 때 baseline은 이전 값이므로 scheduler가 같은 collection을 다시 예약할 수 있습니다. Honcho는 이 in-flight window를 metadata timestamp로 흉내 내지 않고 pending QueueItem 으로 확인합니다. 같은 collection과 dream type의 작업을 식별하는 work-unit key로 pending dream을 먼저 조회해 두 번째 schedule을 막고, 동시에 insert가 경쟁하더라도 DB partial unique index가 duplicate pending row를 거부합니다. 현재 enqueue 경로는 이 충돌을 정상 skip으로 바꾸지 않고 예외를 다시 올리므로, 여기서 확인한 보장은 중복 row가 저장되지 않는다는 범위입니다. 실패해서 pending 상태가 끝났지만 checkpoint가 전진하지 않았다면 같은 corpus를 다시 시도할 수 있습니다. 따라서 세 상태의 owner가 분리됩니다. 새 입력 eligibility -> Document.level == explicit 완료된 progress -> collection dream checkpoint 현재 실행 중 -> pending QueueItem 테스트가 고정하는 계약 PR #573과 pinned test에는 다음 경계가 명시돼 있습니다. 30 explicit + 40 deductive + 10 inductive는 threshold 50을 통과하지 않습니다. 60 explicit은 threshold를 통과합니다. 100 contradiction + 10 explicit도 통과하지 않습니다. 성공한 dream은 완료 시점의 explicit count와 last_dream_at 을 함께 기록합니다. pending dream이 있으면 같은 collection의 두 번째 schedule을 막습니다. run_dream 이 None 을 반환하면 checkpoint를 전진시키지 않고 같은 corpus의 재시도를 허용합니다. 이번 로컬 환경에서는 Honcho가 요구하는 Python/pytest 조합을 실행하지 못해 테스트 코드를 정적으로 확인했습니다. 다른 pipeline에 옮길 수 있는 계약 이 사례는 AI memory에만 한정되지 않습니다. ETL 결과가 다음 ETL의 입력 후보가 되거나, feature가 다시 학습 데이터에 들어가거나, LLM 생성물이 다음 RAG corpus에 포함되는 시스템에서도 같은 질문이 필요합니다. 1. source와 derived를 저장 계층뿐 아니라 eligibility에서도 구분한다. 2. progress checkpoint는 enqueue가 아니라 성공 조건 뒤에 전진시킨다. 3. queued/running 상태를 완료 checkpoint에 섞지 않는다. 4. count, session selection, retry가 같은 input cohort를 보게 한다. 5. 파생물 저장 뒤 checkpoint가 실패하면 같은 입력이 재실행될 수 있다. 재실행을 허용한다면 파생물 write의 deduplication 또는 idempotency를 함께 설계한다. 6. checkpoint 이후에도 남은 side effect가 있다면 그 실패를 다시 처리할 별도 상태를 둔다. derived data를 영원히 입력에서 제외하라는 뜻은 아닙니다. 재귀적 개선이 필요한 시스템이라면 어떤 derived level을 언제 다시 입력으로 허용할지 별도의 명시적 정책과 종료 조건을 둬야 합니다. Limitations Honcho의 공개 코드와 변경 이력을 분석한 글이며, Honcho를 직접 구현·운영하거나 이 변경에 기여한 경험이 아닙니다. 분석 기준은 85239a69b262c944de3c35900b91c88ba9b84f1a 로 고정했습니다. production workload에서 반복 schedule, 비용 증가, 무한 loop를 재현하지 않았습니다. PR #573은 feedback eligibility뿐 아니라 time guard, metadata write, queue coherence를 함께 수정합니다. non-null DreamResult 이후 checkpoint하는 현재 기준이 memory 품질까지 검증한다고 주장하지 않습니다. last_dream_document_count 가 전체 level count에서 explicit-only count로 의미가 바뀔 때 기존 collection metadata를 어떻게 전환하는지는 이번 분석에서 확인하지 않았습니다. 테스트 파일은 확인했지만 현재 로컬 환경에서는 실행하지 못했습니다. Sources Honcho repository PR #573: threshold and time-guard semantics PR #573 merge commit Code immediately before the change Pinned explicit-only threshold and pending-queue gate Pinned success checkpoint Pinned enqueue boundary Pinned pending-dream partial unique index Pinned threshold regression tests Pinned checkpoint and in-flight coherence tests Pinned queue/retry coherence tests

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/junhyun-dev/ai-memoryga-jagi-culryeogeul-dasi-ibryeogeuro-seji-anhge-haneun-beob-2k0g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
