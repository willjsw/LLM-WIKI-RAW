---
pkm_id: GDE-0020
pkm_type: guide
title: "useradd 로 일반 계정과 데몬 전용 계정 만들기"
job: "인프라-운영"
domain: linux
keywords:
  - useradd
  - nologin
  - "데몬 계정"
  - "홈 디렉토리"
  - "보조 그룹"
  - "UID 지정"
contributor: swj
revision: cef68dde
exported_at: 2026-11-16
---

# useradd 로 일반 계정과 데몬 전용 계정 만들기

## Purpose

사람용 계정과 서비스 데몬용 계정을 목적에 맞는 옵션으로 만든다.

## Steps

1. 일반 사용자: `useradd -m <user>` 로 홈 디렉토리를 함께 만든다. useradd 는 기본적으로 홈을 만들지 않는다(Debian 계열 `adduser` 는 대화형으로 이를 강제하는 래퍼다).
2. 그룹 지정: `-g <주그룹>` 으로 1차 그룹, `-G docker,wheel` 처럼 쉼표로 보조 그룹을 준다.
3. 데몬 계정(Nginx, DB 등): `useradd -s /sbin/nologin <svc_user>` 로 로그인 쉘을 막아 터미널 접속을 원천 차단한다.
4. 여러 서버·NFS 공유 환경이면 `-u <UID>` 로 UID 를 모든 서버에서 같은 값으로 고정한다.
5. 결과는 `/etc/passwd`, `/etc/group` 에서 확인한다.
