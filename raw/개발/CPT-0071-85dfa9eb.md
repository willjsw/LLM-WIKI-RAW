---
pkm_id: CPT-0071
pkm_type: concept
title: "HotSpot JIT 컴파일과 주요 최적화 기법"
job: "개발"
domain: jvm
keywords:
  - JIT
  - HotSpot
  - C1
  - C2
  - OSR
  - Deoptimization
  - "Code Cache"
  - AOT
contributor: swj
revision: 85dfa9eb
exported_at: 2026-11-16
---

# HotSpot JIT 컴파일과 주요 최적화 기법

## Definition

HotSpot JVM은 바이트코드를 인터프리터로 실행하다가 프로파일링으로 자주 실행되는 Hot Code를 감지하면 JIT 컴파일해 네이티브 코드로 바꾸는 Mixed Mode로 동작한다. 컴파일된 코드는 Native 영역의 Code Cache에 저장된다.

## Evidence

- C1(Client): 가볍고 빠른 최적화, 단순 호출 횟수 기반 / C2(Server): 공격적 최적화. `-XX:CompileThreshold` 기본값은 Client 1500, Server 10000
- C2 최적화: 공통 부분식 제거(CSE), Loop Unrolling, 배열 경계 검사 제거, Dead Code Elimination, Code Hoisting(루프 불변 코드를 밖으로)
- OSR(On Stack Replacement): 한 번 호출된 메서드 안의 긴 루프 도중에 인터프리터 코드를 컴파일 코드로 교체한다. 대신 일부 다른 최적화가 생략될 수 있다
- Deoptimization: 사용 빈도가 떨어진 컴파일 코드를 버리고 인터프리터로 되돌려 유한한 Code Cache를 회수한다
- AOT(예: GraalVM)는 처음부터 네이티브로 컴파일해 JIT warm-up을 없애므로 서버리스·컨테이너 기동에 유리하다
- 관련 옵션: `-Xint`(인터프리터 전용), `-Xcomp`, `-XX:+PrintCompilation`, `-XX:CICompilerCount`
