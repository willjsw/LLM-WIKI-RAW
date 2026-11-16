---
pkm_id: GDE-0003
pkm_type: guide
title: "SR 접수에서 CR 전환까지 확인할 항목"
job: "기획-PM"
domain: software-process
keywords:
  - SR
  - CR
  - "서비스 요청"
  - "변경 요청"
  - Feature
  - Requirement
  - "형상관리 프로세스"
contributor: swj
revision: f94edd2b
exported_at: 2026-11-16
---

# SR 접수에서 CR 전환까지 확인할 항목

## Purpose

고객·현업의 서비스 요청(SR)을 개발 변경 요청(CR)과 요구사항으로 옮길 때 빠뜨리기 쉬운 항목과 판단 지점을 정리한다.

## Steps

1. SR 을 받으면 대상 서비스, 문제 발생 지점, 담당자를 확인한다.
2. 요청 유형을 나눈다. 장애 대응이면 발생/대상 환경을 필수로 받고, 단순 기능 추가면 생략할 수 있다.
3. 희망 완료 시점은 요청자마다 긴급으로 표시하기 쉬우므로, 처리 일자는 등록자와 개발팀이 협의해 정한다.
4. 검토 후 CR 로 전환할지 판단한다. 전환은 기계적으로 하지 않고 사람이 검토한다.
5. 전환된 건은 Feature(고객 요구사항)로 정리하고, Requirement 까지 PL 이 작성한다.
