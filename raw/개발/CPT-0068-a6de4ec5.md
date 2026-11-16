---
pkm_id: CPT-0068
pkm_type: concept
title: "GC Root와 Reachable 객체의 출처"
job: "개발"
domain: jvm
keywords:
  - "GC Root"
  - "Root Set"
  - Reachable
  - "Garbage 판정"
  - "메모리 누수 원인"
contributor: swj
revision: a6de4ec5
exported_at: 2026-11-16
---

# GC Root와 Reachable 객체의 출처

## Definition

Garbage는 Heap과 Method Area에서 현재 사용되지 않는 객체이며, 판단 기준은 Root Set과의 참조 관계다. Root Set에서 어떤 식으로든 참조가 이어지면 Reachable 객체이고, 아니면 Garbage다.

## Evidence

- GC Root의 출처는 Runtime Data Area 구조 그대로다
  1. JVM Stack: 지역변수와 Operand Stack의 객체 참조
  2. Method Area: 로딩된 클래스의 Constant Pool 참조와 static 변수의 객체 참조
  3. Native Method Stack: 네이티브 메서드(JNI)로 넘겨진 객체 참조
- 따라서 "왜 이 객체가 GC되지 않는가"는 이 세 출처 중 어디서 참조가 이어지는지를 찾는 문제다(Heap Dump 도구의 Path to GC Roots)
- static 컬렉션이나 전역 scope 객체에 담긴 것은 항상 Reachable하므로 누수의 흔한 원인이다
