---
pkm_id: CPT-0145
pkm_type: concept
title: "ACD 서비스 레벨과 RONA"
job: "공통"
domain: contact-center-telephony
keywords:
  - "service level"
  - SVC_LEVEL
  - RONA
  - "queue wait time"
  - ACD
  - "콜센터 지표"
contributor: swj
revision: b7be6d1f
exported_at: 2026-11-16
---

# ACD 서비스 레벨과 RONA

## Definition

ACD 서비스 레벨은 큐에 들어온 호가 정해진 시간(예: 20초) 안에 상담원에게 배정되어야 한다는 목표치이고, RONA(Redirect On No Answer)는 배정된 상담원이 정해진 시간 안에 받지 않을 때 호를 다른 곳으로 돌리는 처리다.

## Evidence

- 큐 최대 대기 시간(queue wait time)을 넘기거나 상담원이 응답하지 않으면 RONA 로 재분배·대체 시나리오를 탄다.
- 큐 우선순위(low/mid/high)로 같은 그룹 안에서 먼저 배정할 호를 정한다. 기본은 low 인 경우가 많다.
- 큐 타입 같은 속성은 생성 명령 한 번에 다 넣지 못해 생성 후 변경 명령으로 조정하는 교환기도 있다.
