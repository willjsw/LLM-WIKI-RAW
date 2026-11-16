---
pkm_id: CPT-0172
pkm_type: concept
title: "인증 필터 fail-close 원칙과 단일 401 응답"
job: "개발"
domain: api-gateway
keywords:
  - fail-close
  - fail-open
  - onErrorResume
  - "인증 우회"
  - "401"
  - "보안 설계"
contributor: swj
revision: be574ecf
exported_at: 2026-11-16
---

# 인증 필터 fail-close 원칙과 단일 401 응답

## Definition

fail-close는 인증 처리 중 예상하지 못한 예외가 나면 요청을 통과시키지 않고 거부하는 원칙이다. 실패 사유(만료, 위조, 부재)도 응답에서 구분하지 않고 단일 401 코드로 돌려준다.

## Evidence

- 리액티브 구현: `Mono.defer(() -> doAuthenticate(...)).onErrorResume(e -> unauthorized(exchange))`로 필터 전체를 감싸 예외가 인증 우회로 이어지지 않게 한다. 예외 상세는 서버 로그에만 남긴다.
- 반례: 기존 서블릿 필터는 `doFilterInternal` 전체를 try/catch로 감싸고 catch 뒤에 `chain.doFilter`를 무조건 호출했다. 필터 내부에서 예외가 나면 인증 없이 통과하는 fail-open 구조였다.
- 401 단일 코드 응답은 공격자에게 토큰 상태를 알려 주지 않는다.
