---
pkm_id: CPT-0116
pkm_type: concept
title: "Redis Stream Consumer Group 과 Last Delivered ID"
job: "개발"
domain: redis
keywords:
  - "Consumer Group"
  - XREADGROUP
  - "last delivered id"
  - "부하 분산"
  - at-least-once
  - "Redis Stream"
contributor: swj
revision: df3a4edf
exported_at: 2026-11-16
---

# Redis Stream Consumer Group 과 Last Delivered ID

## Definition

Consumer Group 은 여러 컨슈머가 한 스트림의 메시지를 중복 없이 나눠 처리하게 하는 Redis Stream 기능이다. 그룹은 마지막으로 전달한 ID(Last Delivered ID)를 기억해 재시작 후에도 이어서 읽는다.

## Evidence

- 같은 그룹의 컨슈머끼리는 메시지가 한 번씩만 배분되어 수평 확장(작업 분배)이 된다.
- 그룹 단위로 읽은 위치를 Redis 가 관리하므로 컨슈머 서버가 재시작해도 읽지 않은 다음 메시지부터 안전하게 가져온다.
- 처리 완료 확인(ACK)과 함께 쓰면 최소 한 번(at-least-once) 처리 패턴을 만들 수 있다.
