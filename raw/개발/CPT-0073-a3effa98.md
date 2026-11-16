---
pkm_id: CPT-0073
pkm_type: concept
title: "세마포어, 뮤텍스, 모니터의 차이"
job: "개발"
domain: jvm
keywords:
  - Semaphore
  - Mutex
  - Monitor
  - "condition variable"
  - "P V 연산"
  - "동기화 기법"
contributor: swj
revision: a3effa98
exported_at: 2026-11-16
---

# 세마포어, 뮤텍스, 모니터의 차이

## Definition

세마포어는 P/V 연산으로 상호배제와 스케줄링을 모두 할 수 있는 저수준 도구이고, 뮤텍스는 lock한 주체만 unlock할 수 있게 소유권을 강제한 Sleeping Lock이며, 모니터는 공유 데이터·연산·동기화를 하나로 묶어 상호배제를 암묵적으로 제공하는 고수준 추상화다.

## Evidence

- 발전 순서: Interrupt Disable(단일 CPU, 시스템 전체를 멈춰 지나치게 강력) → Semaphore → Mutex → Monitor
- 세마포어의 약점: 비구조적이라 P/V가 코드 곳곳에 흩어지고 짝이 맞는지 컴파일러가 검증할 수 없다. 서로 다른 세마포어로 lock해도 문법상 문제가 없다
- 뮤텍스는 lock/unlock 주체 불일치를 규약 위반으로 드러내 레이스를 찾기 쉽게 한다
- 모니터의 condition variable: `wait`는 락을 놓고 잠들었다 깨면 재획득, `signal`은 대기자 하나를 깨운다. 대기자가 없으면 signal은 사라진다(No history). 세마포어의 V는 값이 누적되어 나중의 P가 통과한다는 점이 결정적 차이다
- Java의 `synchronized`, `wait()`, `notify()`는 모니터의 직접 구현이다
