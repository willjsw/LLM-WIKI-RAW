---
pkm_id: CPT-0018
pkm_type: concept
title: "CSTA 콜 이벤트 기본 시퀀스"
job: "공통"
domain: contact-center
keywords:
  - CSTA
  - "콜 이벤트"
  - Delivered
  - Established
  - Cleared
  - Originated
  - CTI
contributor: swj
revision: ae3fed68
exported_at: 2026-11-16
---

# CSTA 콜 이벤트 기본 시퀀스

## Definition

CSTA는 CTI에서 콜 제어 기능과 이벤트를 정의한 표준이다. 콜 상태 변화는 정해진 이벤트 시퀀스로 통지되며, 통계는 이 시퀀스로 인입·응대·종료를 판정한다.

## Evidence

- 인바운드: Offered → Delivered → Established → (Cleared).
- 아웃바운드: Originated → Offered → Delivered → Established → (Cleared).
- 종료 계열은 참여자 하나가 빠지는 이벤트(Connection/Transfer/Consult Cleared)와 콜 전체가 끝나는 이벤트(Call Cleared, Abandon Cleared)를 구분해야 한다. 앞의 것을 콜 종료로 보면 호전환 콜이 중간에 끊긴 것으로 집계된다.
- 보류는 Held → Retrieved 이벤트 쌍으로 온다. Held를 통화 연결 상태로 기록하면 보류 시간을 구분할 수 없게 된다.
- Party는 Call + Connection + Device의 조합으로, 한 콜에 파티가 계속 바뀌고 추가된다.
