---
pkm_id: CPT-0174
pkm_type: concept
title: "API Key ID를 사용자 ID와 분리해 식별하는 이유"
job: "개발"
domain: api-gateway
keywords:
  - "API Key"
  - "API Key ID"
  - "키 로테이션"
  - "키 폐기"
  - "rate limit"
  - "감사 로그"
contributor: swj
revision: 9ffbfe71
exported_at: 2026-11-16
---

# API Key ID를 사용자 ID와 분리해 식별하는 이유

## Definition

API Key 인증에서 요청 주체를 사용자 ID만이 아니라 키마다 부여한 API Key ID로도 식별하는 설계다. 한 사용자가 여러 키를 가질 수 있으므로 키 단위 식별자가 있어야 폐기·로테이션·정책을 키 단위로 적용할 수 있다.

## Evidence

- 사용자:키 = 1:N. 운영용·테스트용·파트너 제공용 키 트래픽이 USER_ID만으로는 같아 보인다.
- 유출 대응: 이상 트래픽이 어느 키에서 오는지 보고 그 키만 revoke한다. 게이트웨이가 원본 키 헤더를 제거하므로 다운스트림 로그에서 키를 식별할 수단은 API_KEY_ID뿐이다.
- 로테이션: 구 키와 신 키가 공존하는 동안 구 키 트래픽이 남았는지 확인한 뒤 구 키를 지운다.
- rate limit, 쿼터, 통계는 키(연동 시스템) 단위로 건다. 파트너별로 키를 나눠 주면 키 단위가 곧 파트너 단위다.
