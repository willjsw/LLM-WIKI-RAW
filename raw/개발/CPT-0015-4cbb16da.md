---
pkm_id: CPT-0015
pkm_type: concept
title: "템플릿 메서드 기반 배치 INSERT 전략 구조"
job: "개발"
domain: batch-processing
keywords:
  - "템플릿 메서드"
  - "template method"
  - "strategy pattern"
  - "batch insert"
  - COPY
  - "multi-row insert"
  - JdbcTemplate
contributor: swj
revision: 4cbb16da
exported_at: 2026-11-16
---

# 템플릿 메서드 기반 배치 INSERT 전략 구조

## Definition

이벤트 유형별 적재 전략이 공통 인터페이스(batchInsert)를 구현하고, 추상 클래스가 배치 분할·필터·실행 방식을 고정한 채 SQL과 파라미터 매핑만 하위 클래스에 맡기는 구조다.

## Evidence

- 인터페이스: `batchInsert(List<T> events)`.
- 추상 클래스 훅: `beforeInsertFilter(dto)`(적재 제외 여부), `mapToParams(dto)`(파라미터 배열), `getInsertSql()`, `afterInsertHook(insertedDtos)`, `buildMultiRowInsertSql(sql, rowCount)`.
- 실행: 이벤트마다 필터와 매핑을 거친 뒤 batchSize 단위로 나눠, 모드가 `copy`면 CSV로 만들어 PostgreSQL COPY를, `jdbc`면 multi-row INSERT 한 문장을 실행한 후 후처리 훅을 호출한다.
- 장점: 새 이벤트 유형은 SQL과 매핑만 추가하면 되고, 대량 적재 방식(COPY vs multi-row)을 설정으로 바꿀 수 있다.
