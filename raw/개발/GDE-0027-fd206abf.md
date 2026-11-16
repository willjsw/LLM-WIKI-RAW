---
pkm_id: GDE-0027
pkm_type: guide
title: "Maven 사설 저장소 인증 설정"
job: "개발"
domain: build-tooling
keywords:
  - Maven
  - settings.xml
  - "server id"
  - "401 Unauthorized"
  - distributionManagement
  - Nexus
contributor: swj
revision: fd206abf
exported_at: 2026-11-16
---

# Maven 사설 저장소 인증 설정

## Purpose

로그인이 필요한 사설 Maven 저장소(Nexus 등)에서 의존성을 받고 배포한다.

## Steps

1. pom.xml `<repositories>` 에 저장소 id 와 다운로드(group) url 을 선언한다. 저장소를 옮길 때는 id 는 그대로 두고 url 만 바꾼다.
2. `~/.m2/settings.xml` 의 `<servers><server>` 에 pom 의 repository id 와 같은 id 로 username/password 를 등록한다. id 가 다르거나 이 설정이 없으면 401 Unauthorized 가 난다.
3. 계정은 pom.xml 에 넣지 않는다. settings.xml 은 Git 에 커밋하지 않는다.
4. 배포가 필요한 프로젝트만 `<distributionManagement>` 의 repository·snapshotRepository 에 배포(hosted) 저장소 url 을 같은 id 로 지정한다.
5. CI 서버에서도 빌드한다면 CI 실행 계정 홈의 `~/.m2/settings.xml` 에 같은 server 설정을 둔다.
6. `mvn -U dependency:resolve` 로 확인한다.
