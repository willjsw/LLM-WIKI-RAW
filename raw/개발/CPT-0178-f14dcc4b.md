---
pkm_id: CPT-0178
pkm_type: concept
title: "PID 기반 프로세스 감시의 한계와 heartbeat"
job: "개발"
domain: distributed-systems
keywords:
  - "프로세스 모니터링"
  - PID
  - heartbeat
  - keepalive
  - "헬스체크"
  - OAMP
contributor: swj
revision: f14dcc4b
exported_at: 2026-11-16
---

# PID 기반 프로세스 감시의 한계와 heartbeat

## Definition

PID 존재 여부로 프로세스를 감시하면 살아 있음(up)과 죽음(down)만 알 수 있다. 프로세스가 살아 있지만 멈췄거나 서비스를 못 하는 상태는 잡지 못하므로, 서비스가 주기적으로 상태를 보고하는 heartbeat나 연결 keepalive를 함께 둔다.

## Evidence

- 운영 관리 에이전트의 기존 감시는 프로세스 실행 상태와 CPU·메모리·디스크만 확인했다.
- 서비스 고유 상태(이중화 Active/Standby, 담당 리소스 상태)는 서비스가 직접 보고하고, 컴퓨팅 리소스는 에이전트가 수집하도록 책임을 나눴다.
- 알람은 호스트 → 서비스 그룹 → 서비스 → 컴포넌트 계층으로 관리하고 해제 이력을 남긴다(정보성 알람은 제외).
