---
pkm_id: CPT-0074
pkm_type: concept
title: "스핀락과 Lock Holder Preemption 문제"
job: "개발"
domain: jvm
keywords:
  - "Spin Lock"
  - "Busy Waiting"
  - "Test And Set"
  - TAS
  - CAS
  - "Lock Holder Preemption"
  - "멀티프로세서"
contributor: swj
revision: d6f8a6bb
exported_at: 2026-11-16
---

# 스핀락과 Lock Holder Preemption 문제

## Definition

멀티프로세서에서는 한 CPU의 인터럽트를 꺼도 다른 CPU가 계속 동작하므로, Test-And-Set 같은 원자적 하드웨어 명령과 루프를 돌며 조건을 반복 확인하는 Busy Waiting(Spin Lock)으로 상호배제를 구현한다. 스핀락을 쥔 스레드가 CPU를 선점당하면 그 락을 기다리는 다른 CPU들이 아무 진전 없이 CPU를 태우는 Lock Holder Preemption 문제가 생긴다.

## Evidence

- 원자 연산 동안 버스를 장악해 다른 CPU의 메모리 트랜잭션을 막는다
- TAS는 메모리의 불리언 값을 읽고 1로 쓰는 작업을 원자적으로 수행한다
- 단일 CPU용 `disableInterrupt()`를 `while(TAS(lock) != 0) continue;`로 바꾸는 것이 일반적 해법이다
- Lock Holder Preemption은 vCPU가 선점되기 쉬운 가상화 환경에서 특히 심각하다
