---
pkm_id: CPT-0186
pkm_type: concept
title: "Blind Transfer와 Attended Transfer"
job: "개발"
domain: telephony
keywords:
  - "호전환"
  - "Blind Transfer"
  - "Attended Transfer"
  - "Consult Transfer"
  - "교환기 부가기능"
  - "과금"
contributor: swj
revision: fd56bc6d
exported_at: 2026-11-16
---

# Blind Transfer와 Attended Transfer

## Definition

Blind Transfer는 전환하는 쪽(A)이 받을 쪽(B)과 통화하지 않고 바로 호를 넘기고 빠지는 방식이다. Attended Transfer는 A가 상대를 보류한 채 B와 먼저 통화한 뒤 연결하고 빠지는 방식이다.

## Evidence

- Blind: 고객–A 통화 → A 보류(고객에게 보류음) → 기능 코드 + B 번호 → A 즉시 종료 → B 단말이 울리고 B–고객 통화.
- Attended: 고객–A 통화 → A 돌려주기(고객 보류음) → A–B 통화 → A 종료 → 고객–B 통화.
- 단말 제조사마다 Transfer를 켜는 방법이 다르다(교환기 Config 변경 vs 단말 설정).
- 과금: A → B 통화는 A가, B가 C로 호전환하면 전환 구간은 B가 과금 주체가 된다. 통화 내역 기반 과금 기록을 CDR이라 한다.
- 유사 기능: Call Park(호를 끊지 않고 잠시 옮겼다가 다시 받음), Conference(보류 후 제3자 초대), MeetMe(미리 만든 방에 예정 시각에 참여), Observer(관리자 감청).
