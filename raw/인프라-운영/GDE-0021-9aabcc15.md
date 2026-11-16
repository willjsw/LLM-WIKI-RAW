---
pkm_id: GDE-0021
pkm_type: guide
title: "Dockerfile 레이어 최적화"
job: "인프라-운영"
domain: docker
keywords:
  - "Dockerfile 최적화"
  - "레이어 캐시"
  - "build cache"
  - "이미지 크기"
  - "RUN 묶기"
contributor: swj
revision: 9aabcc15
exported_at: 2026-11-16
---

# Dockerfile 레이어 최적화

## Purpose

이미지 크기를 줄이고 빌드 캐시 적중률을 높인다.

## Steps

1. 받고·쓰고·지우는 작업은 한 RUN 안에서 `&&` 로 묶는다. 예: `RUN wget ... && tar -xf ... && rm ...`.
2. 변경 빈도가 낮은 명령을 위에, 높은 명령을 아래에 둔다. 예: `COPY package.json .` → `RUN npm install` → `COPY . .`.
3. 소스 전체 COPY 를 의존성 설치 위에 두지 않는다. 소스 한 줄만 바뀌어도 아래 레이어 캐시가 모두 깨져 의존성 설치가 매번 다시 돈다.
4. 결과를 `docker history` 로 확인한다.
5. 환경이 꼬였거나 의존성을 확실히 새로 받아야 하면 `docker build --no-cache` 로 캐시를 무시한다.
