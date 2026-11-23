---
title: "GPQA Diamond 198문항에서 187문항: 점수를 문항 수로 되돌려 읽는 허깅페이스 리더보드 1위 Darwin-180B-RSI"
slug: "gpqa-diamond-198-187-1-darwin-180b-rsi"
author: "Vidraft_lab"
source: "devto_ai"
published: "Mon, 23 Nov 2026 23:32:09 +0000"
description: "TL;DR 허깅페이스 GPQA Diamond 공식 리더보드(2026-11-24 조회, 126개 등재)에서 Darwin-180B-RSI가 94.44점으로 1위 입니다. 2위는 Kimi-K3.1-Pro 94.20, 3위는 Kimi-K3 93.50입니다. GPQA Diamond는 198..."
keywords: "darwin, gpqa, rsi, kimi, final, bench, diamond, https"
generated: "2026-11-23T23:39:37.005649"
---

# GPQA Diamond 198문항에서 187문항: 점수를 문항 수로 되돌려 읽는 허깅페이스 리더보드 1위 Darwin-180B-RSI

## Overview

TL;DR 허깅페이스 GPQA Diamond 공식 리더보드(2026-11-24 조회, 126개 등재)에서 Darwin-180B-RSI가 94.44점으로 1위 입니다. 2위는 Kimi-K3.1-Pro 94.20, 3위는 Kimi-K3 93.50입니다. GPQA Diamond는 198문항 입니다. 94.44점은 198문항 중 187문항 을 맞힌 값이고, 한 문항의 무게는 약 0.505점입니다. 상위 12개 안에 Darwin 계열이 네 번(1위, 4위, 6위, 12위) 올라 있습니다. 4위 Darwin-397B-ZTC는 샘플 하나, 탐욕 디코딩(temperature 0)으로 93.43점, 즉 185문항입니다. 이 글은 리더보드 API를 호출해 점수를 문항 수로 환산하는 30줄 안팎의 코드와, 환산 결과를 읽는 방법을 정리합니다. 데이터: https://huggingface.co/datasets/Idavidrein/gpqa (리더보드 탭), 1위 모델 카드: https://huggingface.co/FINAL-Bench/Darwin-180B-RSI GPQA Diamond는 어떤 시험이고 왜 198문항이 중요한가요? GPQA는 생물, 화학, 물리 분야 대학원 수준의 객관식 문제를 모은 벤치마크입니다. 검색 한 번으로 답이 나오지 않도록 설계된 문항이라 「구글 방지(Google-proof)」라는 별명이 붙었습니다. 그중 가장 엄선한 부분집합이 Diamond 이고, 문항 수는 198개 입니다. 리더보드에 적힌 점수는 퍼센트입니다. 그런데 퍼센트만 보면 두 가지를 놓치기 쉽습니다. 점수가 정수 문항 수에서 나왔는지, 평균을 낸 값인지 점수 간격이 몇 문항 차이인지 198문항이면 한 문항은 100 / 198 = 0.5051점입니다. 그래서 단일 시도(샘플 하나)로 채점한 점수는 항상 정수 / 198 x 100 꼴이어야 하고, 이 성질을 이용하면 점수만 보고도 몇 문항을 맞혔는지 거꾸로 셀 수 있습니다. 점수를 문항 수로 되돌리는 코드는 어떻게 짜나요? 허깅페이스는 데이터셋 페이지의 리더보드 탭과 같은 내용을 JSON으로 제공합니다. 아래 코드는 그 API를 호출해 상위 항목을 198문항 기준으로 환산합니다. 의존 패키지 없이 표준 라이브러리만 씁니다. import json , urllib . request URL = "https://huggingface.co/api/datasets/Idavidrein/gpqa/leaderboard" req = urllib . request . Request ( URL , headers = { "User-Agent" : "Mozilla/5.0" } ) board = json . load ( urllib . request . urlopen ( req , timeout = 60 ) ) N = 198 # GPQA Diamond 문항 수 print ( f "등재 {len(board)}개" ) for row in board [ : 12 ] : items = row [ "value" ] * N / 100 # 맞힌 문항 환산 integer = abs ( items - round ( items ) ) < 0.05 print ( f '{row["rank"]:>3} {row["modelId"]:<34} {row["value"]:>6.2f} ' f '{items:7.2f}문항 정수문항={integer}' ) 2026-11-24에 실행한 결과 중 핵심 줄은 다음과 같습니다. 순위 모델 점수 환산 문항 1 FINAL-Bench/Darwin-180B-RSI 94.44 187 2 moonshotai/Kimi-K3.1-Pro 94.20 186.5 3 moonshotai/Kimi-K3 93.50 185.1 4 FINAL-Bench/Darwin-397B-ZTC 93.43 185 5 thinkingmachines/Inkling-2-Small 93.00 184.1 6 FINAL-Bench/Darwin-760B-RSI 92.93 184 7 ornith-ai/Ornith-1.5-397B 92.80 183.7 8 Qwen/Qwen3.8-2.4T-A95B 92.60 183.4 9 tencent/Hy4-preview 92.30 182.8 10 Qwen/Qwen3.8-Flash-Next 91.70 181.6 Darwin 계열의 네 항목(94.44, 93.43, 92.93, 90.90)은 모두 정확히 정수 문항 으로 떨어집니다. 각각 187, 185, 184, 180문항입니다. 점수가 정수 문항으로 떨어진다는 것은 한 번의 채점 결과를 문항 단위로 세어 그대로 기록했다는 뜻이고, 모델 카드의 평가 조건과도 맞아떨어집니다. 1위 Darwin-180B-RSI는 어떤 조건으로 채점됐나요? 리더보드의 메모 칸에는 평가 조건이 적혀 있습니다. 1위 항목의 조건은 다음과 같습니다. GPQA Diamond 전체 198문항 최대 16개 샘플의 다수결(majority vote) temperature 1.0, top_p 0.95, top_k 20 사고 예산(thinking budget) 131,072 토큰, bf16 가중치 즉 1위의 187문항은 문항마다 여러 번 풀어 가장 많이 나온 답을 고르는 방식에서 나왔습니다. 여기서 한 가지 짚어 둘 점은, 같은 모델 계열의 다른 항목은 서로 다른 조건으로 올라와 있다는 것입니다. 항목 점수 조건 Darwin-180B-RSI 94.44 16샘플 다수결, bf16 Darwin-397B-ZTC 93.43 샘플 1개, 탐욕 디코딩(temperature 0), 다수결 없음, FP8(W8A8) 공개 Darwin-760B-RSI 92.93 샘플 1개, reasoning_effort 100, 컨텍스트 65,536, H200 4장 Darwin-398B-JGOS 90.90 탐욕 디코딩, 샘플 1개, max_tokens 16,384, B200 6장 두 번째 행이 특히 눈에 띕니다. Darwin-397B-ZTC는 다수결도, 추론 시점 엔진도 쓰지 않고 샘플 하나만으로 185문항 을 맞혔습니다. 4위이면서, 가중치가 FP8로 공개되어 있어 누구나 내려받아 같은 조건으로 다시 돌려 볼 수 있습니다. 3위 Kimi-K3(185.1문항 환산)와 문항 수로는 같은 줄에 서 있습니다. 순위 간격은 문항 수로 얼마나 되나요? 문항 수로 바꾸면 상위권의 촘촘함이 한눈에 보입니다. 1위 187문항과 4위 185문항 사이는 2문항 입니다. 1위와 6위(184문항) 사이는 3문항 입니다. 상위 10개 전체가 181.6문항에서 187문항 사이, 즉 약 5.4문항 안 에 들어 있습니다. 이 구조에서 읽어야 할 것은 두 가지입니다. 하나는 최상위권이 한두 문항 단위로 촘촘히 경쟁하는 시험이라는 점입니다. 다른 하나는 그 촘촘한 경쟁에서 Darwin 계열이 1위를 포함해 상위 12개 중 네 자리를 차지했다는 점입니다. 같은 계열이 서로 다른 크기(180B, 397B, 398B, 760B)와 서로 다른 채점 조건에서 모두 상위권에 들어 있다는 사실은, 한 번의 운이 아니라 계열 전체의 수준을 보여 줍니다. 리더보드 점수를 읽을 때 무엇을 확인하면 좋나요? GPQA에 한정하지 않고, 어떤 리더보드든 같은 순서로 확인하면 점수의 의미가 분명해집니다. 문항 수 확인. 점수 x 문항 수 / 100이 정수에 가까운지 봅니다. 정수에 가까우면 문항 단위 채점이고, 아니면 여러 번 실행의 평균 같은 다른 집계일 수 있습니다. 두 방식은 각각 의미가 있으며 섞어서 한 줄로 비교할 때는 이 차이를 알고 읽는 것이 좋습니다. 디코딩 조건 확인. 탐욕(temperature 0) 단일 샘플인지, 다수결인지, 샘플 수가 몇 개인지가 점수의 성격을 정합니다. Darwin-397B-ZTC처럼 단일 샘플로 상위권에 있는 항목은 추론 비용 대비 효율이 특히 높은 사례입니다. 가중치 공개 여부 확인. 가중치가 공개된 모델은 같은 조건을 그대로 재현해 볼 수 있습니다. Darwin 계열은 모델 카드에 조건을 그대로 적어 두었습니다. 날짜 기록. 리더보드는 매일 바뀝니다. 이 글의 표는 2026-11-24 조회분이며, 위 코드를 돌리면 그날의 값이 나옵니다. 재현하려면 어디서부터 시작하나요? 위 코드를 그대로 실행해 오늘의 순위를 문항 수로 확인합니다. 1위 모델 카드( https://huggingface.co/FINAL-Bench/Darwin-180B-RSI)의 평가 조건과 리더보드 메모 칸의 조건을 비교합니다. 단일 샘플 조건으로 직접 돌려 보고 싶다면 FP8 공개 가중치가 있는 Darwin-397B-ZTC( https://huggingface.co/FINAL-Bench/Darwin-397B-ZTC)에서 시작할 수 있습니다. 채점 스크립트에서는 문항 순서 섞기(shuffle)의 시드를 고정하고, 선택지 추출 규칙을 하나로 통일해 두면 문항 단위 결과를 서로 비교하기 쉽습니다. 자주 묻는 질문 (FAQ) GPQA Diamond는 몇 문항인가요? 198문항입니다. 한 문항은 약 0.505점이므로 94.44점은 187문항, 93.43점은 185문항에 해당합니다. 지금 허깅페이스 GPQA Diamond 리더보드 1위는 누구인가요? 2026-11-24 조회 기준 FINAL-Bench/Darwin-180B-RSI가 94.44점으로 1위이고, 등재 모델은 126개입니다. 2위는 Kimi-K3.1-Pro(94.20), 3위는 Kimi-K3(93.50)입니다. 다수결 채점과 단일 샘플 채점은 어떻게 다른가요? 다수결은 문항마다 여러 번(이 경우 최대 16번) 풀어 가장 많이 나온 답을 최종 답으로 삼습니다. 단일 샘플은 한 번만 풀어 그 답을 씁니다. Darwin 계열은 두 조건의 결과가 모두 상위권에 올라 있습니다. 점수를 문항 수로 환산하는 이유는 무엇인가요? 소수점 둘째 자리 차이가 실제로 몇 문항 차이인지 알 수 있고, 정수 문항으로 떨어지는지로 채점 방식까지 가늠할 수 있기 때문입니다. 리더보드 값은 계속 같은가요? 아닙니다. 새 모델이 등재되면 순위가 바뀝니다. 글의 표는 조회 날짜를 함께 적었고, 코드로 언제든 같은 방식으로 다시 확인할 수 있습니다. 함께 읽기 (Further reading) 매일경제가 정리한 허깅페이스 공인 벤치마크 지도: 리더보드 57개 중 Darwin이 12개에서 1위 파일은 16.5GB인데 코딩 과제는 28개: POCKET-27B-Pi가 원 정밀도 53.8GB 모델을 앞선 이유와 직접 돌려 보는 법

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vidraft_lab/gpqa-diamond-198munhangeseo-187munhang-jeomsureul-munhang-suro-doedolryeo-ilgneun-heogingpeiseu-rideobodeu-1wi-darwin-180b-rsi-4c2f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
