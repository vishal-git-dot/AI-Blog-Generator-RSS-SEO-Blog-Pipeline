---
title: "DNS 설정을 상태 머신처럼 보면 카페24 메일 연결이 덜 꼬인다"
slug: "dns-24"
author: "오피셜메일"
source: "devto_webdev"
published: "Mon, 17 Aug 2026 01:09:10 +0000"
description: "카페24에서 도메인 메일을 연결하다가 막히면 대부분 값을 더 많이 넣으려고 합니다. 하지만 DNS 문제는 값의 개수보다 상태의 순서 로 보는 편이 디버깅하기 쉽습니다. 제가 추천하는 순서는 다음 네 상태입니다. 권한 있는 DNS를 찾는다. MX로 수신 경로를 바꾼다. SPF와 DK..."
keywords: "dns, txt, spf, state, dkim, nslookup, type, example"
generated: "2026-08-17T01:39:21.438413"
---

# DNS 설정을 상태 머신처럼 보면 카페24 메일 연결이 덜 꼬인다

## Overview

카페24에서 도메인 메일을 연결하다가 막히면 대부분 값을 더 많이 넣으려고 합니다. 하지만 DNS 문제는 값의 개수보다 상태의 순서 로 보는 편이 디버깅하기 쉽습니다. 제가 추천하는 순서는 다음 네 상태입니다. 권한 있는 DNS를 찾는다. MX로 수신 경로를 바꾼다. SPF와 DKIM으로 발신자를 인증한다. 외부 송수신으로 실제 결과를 확인한다. 한 상태가 통과하지 않았는데 다음 값을 수정하면 원인과 결과가 섞입니다. State 1: authoritative DNS를 먼저 확정한다 도메인을 카페24에서 구매했다는 사실만으로 카페24가 현재 DNS 운영처라는 뜻은 아닙니다. 네임서버가 다른 업체를 가리키면 카페24 관리자에 입력한 값은 실제 조회에 반영되지 않습니다. 먼저 외부에서 NS를 확인합니다. nslookup -type=NS example.com 카페24 네임서버를 쓰고 있다면 카페24 DNS 화면에서 계속합니다. 타사 네임서버라면 그 업체의 DNS 관리자에서 같은 작업을 해야 합니다. 쇼핑몰 관리자: 쇼핑몰 설정 → 기본 설정 → 쇼핑몰 정보 → 도메인 설정 → 도메인 관리 → DNS 설정 호스팅센터: 나의 서비스 관리 → 도메인 관리 → 도메인 부가서비스 → DNS 관리 State 2: MX는 하나의 수신 시스템으로 수렴시킨다 MX는 새 메일이 도착할 서버를 고릅니다. 예전 서비스 MX와 새 서비스 MX가 섞이면 일부 메일이 이전 메일함으로 갈 수 있습니다. 이전 메일함 백업 새 서비스가 제공한 MX 주소와 우선순위 기존 MX 제거 시점 MX 변경은 과거 메일을 옮기지 않습니다. 앞으로 들어올 메일의 경로만 바꿉니다. 웹사이트용 A·CNAME은 메일 설정과 분리하세요. MX를 바꾸면서 A·CNAME까지 삭제하면 쇼핑몰 접속이 끊길 수 있습니다. State 3: SPF는 append가 아니라 merge다 SPF는 루트 도메인의 TXT 정책입니다. 이미 v=spf1로 시작하는 레코드가 있는데 새 SPF를 하나 더 만들면 PermError가 발생할 수 있습니다. nslookup -type=TXT example.com 기존 발송 도구와 새 회사 메일을 함께 써야 한다면 두 조건을 하나의 SPF 정책 으로 합쳐야 합니다. include 문법을 추측하지 말고 발송 서비스가 안내한 통합 값을 기준으로 작업합니다. State 4: DKIM은 selector와 public key를 한 쌍으로 본다 DKIM은 보통 selector._domainkey 형태의 호스트명과 긴 TXT 값으로 구성됩니다. DNS 화면이 기본 도메인을 자동으로 붙이는데 전체 호스트명을 다시 입력함 긴 TXT 값이 제한에 걸려 일부가 잘리거나 임의로 수정됨 TXT 길이 제한을 만났다면 글자를 삭제하지 마세요. 제공 업체가 안내한 분할 방식이나 지원 가능한 키 길이를 확인하고, 최종 조회 결과가 원본과 같은지 비교합니다. Done 상태는 저장 버튼이 아니라 송수신 테스트다 카페24 안내상 MX 변경은 보통 30분에서 1시간 정도 걸릴 수 있습니다. 그동안 같은 값을 계속 바꾸기보다 아래 체크를 순서대로 통과시키세요. 외부 조회에서 새 MX가 보인다. SPF가 하나의 정책으로 반환된다. DKIM 선택자 조회가 정상이다. 개인 메일에서 회사 주소로 보낸 메일이 도착한다. 회사 주소에서 외부로 보낸 메일의 SPF·DKIM 결과가 PASS다. 문제를 증상으로 분기하면 더 빠릅니다. 조회값이 안 바뀜 → 네임서버 메일이 예전 메일함으로 감 → 남은 MX SPF PermError → SPF 정책 중복 DKIM만 실패 → 선택자 또는 TXT 잘림 쇼핑몰까지 끊김 → A·CNAME 변경 여부 운영에서 남길 로그 DNS를 바꿀 때는 변경 전 값, 변경 시각, 새 값, 첫 정상 조회 시각을 기록해 두세요. 다음 장애에서 이 네 줄이 가장 빠른 디버깅 로그가 됩니다. 카페24 MX·SPF·DKIM 전체 설정 순서와 FAQ 보기 값을 많이 입력하는 것보다, 각 상태의 통과 조건을 확인한 뒤 다음 단계로 넘어가는 것이 안전한 연결 방법입니다.``

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/officialmailkr/dns-seoljeongeul-sangtae-meosinceoreom-bomyeon-kape24-meil-yeongyeoli-deol-ggoinda-43k5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
