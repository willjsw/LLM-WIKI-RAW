---
pkm_id: CPT-0198
pkm_type: concept
title: "Docker Swarm 서비스 템플릿 변수와 노드 라벨 배치 제약"
job: "인프라-운영"
domain: linux-infra
keywords:
  - "Docker Swarm"
  - "placement constraints"
  - node.labels
  - "서비스 템플릿"
  - Task.Slot
  - compose
contributor: swj
revision: 5edf95ab
exported_at: 2026-11-16
---

# Docker Swarm 서비스 템플릿 변수와 노드 라벨 배치 제약

## Definition

Docker Swarm 스택 파일에서는 `{{.Service.Name}}`, `{{.Task.Slot}}`, `{{.Node.Hostname}}` 같은 Go 템플릿 변수로 컨테이너 hostname과 환경변수를 태스크마다 다르게 채울 수 있고, `deploy.placement.constraints`에 노드 라벨 조건을 걸어 서비스를 특정 노드에만 배치할 수 있다.

## Evidence

- `hostname: '{{.Service.Name}}_{{.Task.Slot}}'`로 레플리카마다 구분되는 호스트명을 만든다.
- `SYSTEM_HOSTNAME: '{{.Node.Hostname}}'`로 컨테이너가 자신이 뜬 노드 이름을 안다(로그·모니터링 식별용).
- `placement.constraints: [node.labels.<키> == <값>]` + `replicas: 1`로 이중화 노드 중 지정 노드에 한 개만 띄운다. 노드에는 `docker node update --label-add <키>=<값>`으로 라벨을 붙인다(일반 사용법).
- `user: '${DOCKER_UID}:${DOCKER_GID}'`로 호스트 사용자 권한으로 실행해 bind mount한 로그·설정 디렉터리 권한 문제를 피한다.
- 외부 `host` 네트워크를 지정하면 포트 매핑 없이 호스트 네트워크를 쓴다.
