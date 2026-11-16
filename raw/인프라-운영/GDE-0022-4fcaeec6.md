---
pkm_id: GDE-0022
pkm_type: guide
title: "Docker 디스크 정리와 캐시 관리"
job: "인프라-운영"
domain: docker
keywords:
  - "docker prune"
  - "dangling image"
  - "builder prune"
  - "디스크 정리"
  - "docker system prune"
contributor: swj
revision: 4fcaeec6
exported_at: 2026-11-16
---

# Docker 디스크 정리와 캐시 관리

## Purpose

쌓인 이미지·컨테이너·빌드 캐시·볼륨을 범위를 골라 정리한다.

## Steps

1. 빌드 캐시만: `docker builder prune`.
2. 기본 정리: `docker system prune` — 정지된 컨테이너와 태그가 없는 dangling 이미지(`<none>:<none>`)를 지운다.
3. 미사용 이미지 전부: `docker system prune -a` — 어떤 컨테이너도 쓰지 않는 정상 이미지까지 지운다.
4. 볼륨까지: `--volumes` 를 붙이면 연결되지 않은 managed volume 도 지운다. 데이터 손실 위험이 있으니 마지막에만 쓴다.
5. dangling 이미지가 다시 생기지 않도록 빌드할 때 항상 `-t 이름:버전` 으로 태그를 붙인다.
