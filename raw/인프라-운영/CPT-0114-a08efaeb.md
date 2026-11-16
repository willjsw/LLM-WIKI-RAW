---
pkm_id: CPT-0114
pkm_type: concept
title: "Nginx와 keepalived VIP 기반 L4 프록시 이중화"
job: "인프라-운영"
domain: infra
keywords:
  - "L4 스위치"
  - "Nginx stream"
  - keepalived
  - VIP
  - GSLB
  - "로드밸런서 이중화"
contributor: swj
revision: a08efaeb
exported_at: 2026-11-16
---

# Nginx와 keepalived VIP 기반 L4 프록시 이중화

## Definition

전용 L4 스위치 대신 Nginx 두 대를 L4(TCP) 프록시로 두고 keepalived 로 가상 IP(VIP)를 넘겨받게 하면 소프트웨어만으로 로드밸런서 이중화를 구성할 수 있다. 외부에는 VIP 하나만 노출한다.

## Evidence

- L4 스위치: 장비 자체가 이중화를 지원하고 네트워크 구간을 가로질러 도메인별 분기가 가능하지만 고가이고 쓸 수 있는 포트 수에 제약이 있다.
- Nginx L4 프록시: Nginx 2대 + keepalived. 장애 시 keepalived 가 VIP 를 대기 노드로 옮긴다. 리눅스 서버(예: Rocky Linux)만 있으면 된다.
- 사이트 간 이중화는 그 위에 GSLB(DNS 기반 전역 분산)를 얹는다.
- 비용과 장비 조달이 제약일 때 Nginx 방식이 대안이 되고, 처리량·운영 편의가 우선이면 전용 장비가 유리하다.
