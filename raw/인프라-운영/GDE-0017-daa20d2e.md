---
pkm_id: GDE-0017
pkm_type: guide
title: "엔트리포인트에서 실행 UID 로 passwd 와 group 을 맞추는 방법"
job: "인프라-운영"
domain: docker
keywords:
  - docker-entrypoint
  - UID
  - GID
  - "/etc/passwd"
  - sudo
  - "컨테이너 권한"
contributor: swj
revision: daa20d2e
exported_at: 2026-11-16
---

# 엔트리포인트에서 실행 UID 로 passwd 와 group 을 맞추는 방법

## Purpose

컨테이너를 호스트 사용자 UID/GID 로 실행(`user:` 또는 `-u`)했을 때, 컨테이너 안에 그 UID 의 계정이 없어 sudo·cron·logrotate 가 동작하지 않는 문제를 엔트리포인트에서 보정한다.

## Steps

1. 빌드 시 대상 사용자를 만들고 `/etc/passwd`, `/etc/group` 을 일시적으로 쓰기 가능하게 둔다.
2. 엔트리포인트에서 `id -u`, `id -g` 로 현재 UID/GID 를 읽는다.
3. 기존 대상 사용자 줄과 현재 UID 를 가진 줄을 제외한 passwd 를 임시 파일로 만들고, 대상 사용자 이름에 현재 UID/GID 를 붙인 줄을 추가해 덮어쓴다. group 도 같은 방식으로 고친다.
4. 이제 현재 UID 가 대상 사용자로 인식되므로 sudo 로 앱 디렉토리 소유권을 현재 UID/GID 로 바꾸고, logrotate 설정의 사용자 항목을 치환한다.
5. crond 등 보조 데몬을 띄운다.
6. 마지막에 sudoers 의 전체 허용 줄을 대상 사용자로 줄이고, passwd/group 은 644, shadow 는 000 으로 되돌린다.
7. `exec "$@"` 로 본 프로세스를 PID 1 로 실행한다.

주의: 빌드 시점에 passwd 쓰기 권한과 NOPASSWD sudo 를 열어 두는 구조라, root·sudo 사용을 금지하는 현장에서는 반려될 수 있다. 쓰기 전에 보안 정책을 확인한다.
