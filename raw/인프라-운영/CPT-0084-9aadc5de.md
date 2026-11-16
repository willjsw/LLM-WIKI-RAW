---
pkm_id: CPT-0084
pkm_type: concept
title: "gRPC 세션 Init 플래그로 단순 단절과 장애 절체 구분"
job: "인프라-운영"
domain: high-availability
keywords:
  - gRPC
  - "세션"
  - "재연결"
  - "절체 판단"
  - "Init 메시지"
  - failover
contributor: swj
revision: 9aadc5de
exported_at: 2026-11-16
---

# gRPC 세션 Init 플래그로 단순 단절과 장애 절체 구분

## Definition

장기 연결(gRPC 스트림 등)의 끊김을 곧바로 장애로 보지 않고, 연결 직후 보내는 최초 연동 메시지(Init/Active 플래그)로 상대가 재시작했는지 판단하는 방식이다. 재연결 후 Init 을 받았을 때만 절체로 보고 세션을 초기화한다.

## Evidence

- 단순 네트워크 끊김 뒤 재연결이면 기존 세션을 유지해 진행 중인 호를 살린다.
- Init 수신은 상대 프로세스가 새로 떴다는 뜻이므로 이때만 초기화 프로세스를 수행한다.
- 이렇게 하지 않으면 순간 단절마다 진행 중 세션 전체를 버리게 된다.
