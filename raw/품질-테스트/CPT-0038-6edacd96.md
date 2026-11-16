---
pkm_id: CPT-0038
pkm_type: concept
title: "k6와 SIPp로 상담사와 고객을 나눠 시뮬레이션하는 콜 회귀 테스트"
job: "품질-테스트"
domain: call-testing
keywords:
  - k6
  - SIPp
  - "콜 테스트"
  - CTI
  - STOMP
  - SIP
  - "회귀 테스트"
contributor: swj
revision: 6edacd96
exported_at: 2026-11-16
---

# k6와 SIPp로 상담사와 고객을 나눠 시뮬레이션하는 콜 회귀 테스트

## Definition

콜센터 CTI 회귀 테스트에서 상담사는 k6(STOMP over WebSocket 클라이언트)로, 고객은 SIPp(SIP·RTP)로 흉내 내고, 오케스트레이터가 케이스별로 두 도구의 기동 순서를 맞춘다. 판정은 k6 가 받은 상담사 이벤트 시퀀스와 DB 적재 결과로 하며, SIPp 는 교환기에 진짜 콜을 흘려 넣는 장치다. 기대값을 아는 콜 1통을 만드는 회귀 도구이며 부하 테스트가 아니다.

## Evidence

- 고객 측은 교환기 대표번호로 INVITE 를 보내고 in-band DTMF 로 IVR 을 통과하거나, 상담사 발신을 받는다.
- 상담사 측은 로그인 → Ready → 이벤트(DeliveredIn, EstablishedIn, CallCleared, ACW 등)를 보고 응답·호전환·협의 요청을 보낸다.
- 케이스 role 에 따라 기동 순서를 다르게 한다: 내선간(k6만), 인바운드(k6 먼저 Ready → SIPp 발신), 지연 기동, SIPp 단독, 아웃바운드(SIPp 착신 대기 → k6 발신).
- 개선 방향: 케이스 정의를 파일 한 장으로 모아 새 시나리오를 파일 하나로 추가한다. 자격증명은 gitignore 된 env 파일 한 곳에 두고 없으면 시작을 거부한다. 스크립트는 `k6 run -` 처럼 표준입력으로 넘겨 공유 디렉터리 동기화를 없앤다. preflight 로 IP·파일·정의 중복을 검사한다.
