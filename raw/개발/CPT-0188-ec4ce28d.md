---
pkm_id: CPT-0188
pkm_type: concept
title: "비로그인 웹챗 방문자 식별 토큰"
job: "개발"
domain: chat-messaging
keywords:
  - "Visitor Token"
  - "익명 사용자"
  - "웹챗"
  - "Local Storage"
  - "세션 유지"
  - "브라우저 식별"
contributor: swj
revision: ec4ce28d
exported_at: 2026-11-16
---

# 비로그인 웹챗 방문자 식별 토큰

## Definition

로그인 없는 웹챗에서 같은 브라우저의 재방문을 같은 대화로 이어 주기 위해 서버가 발급해 브라우저에 저장하는 임의 식별자다. 로그인 사용자는 인증 토큰으로 세션을 잇지만 익명 사용자는 이 토큰이 같은 브라우저를 판별하는 유일한 수단이다.

## Evidence

- 최초 접속 시 커넥터가 UUID 계열 값을 생성해 돌려주고, 클라이언트는 Local Storage(또는 쿠키)에 저장한다.
- 이후 요청마다 이 값을 보내고 서버는 같은 값이면 같은 세션으로 본다.
- 시간 정렬이 필요하면 UUIDv7이나 ULID 같은 시간 기반 ID를 검토한다.
