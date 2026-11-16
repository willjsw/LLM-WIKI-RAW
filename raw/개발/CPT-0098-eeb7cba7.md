---
pkm_id: CPT-0098
pkm_type: concept
title: "공유 DB 에서 마이그레이션 도구를 쓸 때의 공통 원칙"
job: "개발"
domain: postgresql
keywords:
  - "마이그레이션"
  - spring.liquibase.enabled
  - logicalFilePath
  - runOnChange
  - "소유자 계정"
  - "롤 기반 권한"
contributor: swj
revision: eeb7cba7
exported_at: 2026-11-16
---

# 공유 DB 에서 마이그레이션 도구를 쓸 때의 공통 원칙

## Definition

여러 애플리케이션이 하나의 DB 를 함께 쓰면, 마이그레이션은 앱 기동과 분리해 객체 소유 계정으로 한 곳에서 실행하고, 앱은 롤로 받은 데이터 권한만 갖게 한다.

## Evidence

- 앱 기동 시 자동 마이그레이션을 끈다(`spring.liquibase.enabled=false`, `spring.flyway.enabled=false`). 여러 앱이 기동 순서대로 같은 DB 를 바꾸면 서로 다른 버전이 충돌하고 잠금 대기가 생긴다.
- 실행 계정은 객체 소유 계정으로 한다. 객체 소유자는 설치 계정 하나, 스키마마다 CRUD 롤과 조회 롤을 두고 앱 계정은 그 롤을 부여받아 쓰는 구조에서는 앱 계정에 DDL 권한이 없다.
- 모든 changelog 에 `logicalFilePath` 를 고정해 디렉토리 정리·레포 이동 시 이미 적용된 변경이 재실행되지 않게 한다.
- 이력 테이블 위치를 명시(`liquibase-schema-name`)하면 객체 비교·검증에서 제외하기 쉽다.
- 뷰·함수는 `runOnChange` 로 정본 파일 하나를 계속 고친다. 테이블·시드는 일반 changeset 으로 두고 적용 뒤에는 고치지 않는다(체크섬 오류).
- 운영 중인 DB 에 처음 도입할 때는 현재 형상을 기준선 changeset 으로 두고 기존 DB 에는 '적용됨'으로만 기록한다.
- 사이트 구분은 contexts, 모듈 구분은 labels 로 한다.
