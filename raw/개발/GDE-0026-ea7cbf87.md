---
pkm_id: GDE-0026
pkm_type: guide
title: "WebSocket 서비스 운영 시 점검 항목"
job: "개발"
domain: websocket
keywords:
  - "WebSocket 운영"
  - "Nginx proxy"
  - proxy_read_timeout
  - CSWSH
  - "Origin 검사"
  - "스케일아웃"
contributor: swj
revision: ea7cbf87
exported_at: 2026-11-16
---

# WebSocket 서비스 운영 시 점검 항목

## Purpose

프록시·보안·다중 인스턴스 환경에서 WebSocket 연결이 끊기거나 탈취되지 않게 한다.

## Steps

1. 리버스 프록시(Nginx 등)에서 `Upgrade`, `Connection` 헤더를 백엔드로 넘기도록 설정한다. 빠지면 업그레이드가 되지 않는다.
2. 프록시 유휴 타임아웃(Nginx `proxy_read_timeout` 기본 60초)보다 짧은 간격으로 하트비트를 보낸다.
3. 서버에서 허용 Origin 을 검사한다. 하지 않으면 다른 사이트가 사용자 브라우저로 연결을 여는 CSWSH(Cross-Site WebSocket Hijacking)에 노출된다.
4. 운영은 `wss://` 만 쓴다.
5. 서버가 여러 대면 연결은 그중 한 대에만 있다. 다른 인스턴스가 만든 메시지를 해당 연결로 보내는 방법(외부 브로커 중계, 전 인스턴스 브로드캐스트 후 필터 등)을 설계한다.
