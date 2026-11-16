---
pkm_id: CPT-0133
pkm_type: concept
title: "SIP Via 헤더와 Contact 헤더의 차이"
job: "개발"
domain: sip
keywords:
  - "Via header"
  - "Contact header"
  - rport
  - "NAT traversal"
  - "SIP 프록시"
  - "사설 IP"
contributor: swj
revision: efd5ca45
exported_at: 2026-11-16
---

# SIP Via 헤더와 Contact 헤더의 차이

## Definition

Via 헤더는 지금 트랜잭션의 응답을 어디로 돌려보낼지 나타내고, Contact 헤더는 이후 상대가 나에게 새 요청을 보낼 주소를 나타낸다.

## Evidence

- NAT·방화벽 뒤 사설 IP 단말은 헤더에 사설 주소를 적는다. 서버는 수신 패킷의 실제 출발 IP·포트를 볼 수 있으므로 `rport` 로 실제 주소를 기록하고, 헤더 주소와 실제 패킷 주소가 다르면 실제 패킷 정보를 우선한다.
- SIP 프록시는 Via 경로를 따라 응답을 되돌리고 등록 정보를 이용해 요청 경로를 찾는다.
- 방화벽이 UDP 를 막는 환경이면 SIP 시그널링 포트만 예외로 열어야 통신된다.
- 프록시 IP 는 Via 헤더에 남아 인증 절차 확인에도 쓰인다.
