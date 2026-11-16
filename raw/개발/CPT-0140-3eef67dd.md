---
pkm_id: CPT-0140
pkm_type: concept
title: "fork 기반 서버에서 자식이 물려받는 자원"
job: "개발"
domain: c-systems-programming
keywords:
  - fork
  - "multi-process server"
  - "listen socket"
  - "file descriptor 상속"
  - "worker process"
contributor: swj
revision: 3eef67dd
exported_at: 2026-11-16
---

# fork 기반 서버에서 자식이 물려받는 자원

## Definition

fork 로 만든 자식 프로세스는 부모의 메모리와 열린 FD 를 모두 물려받는다. 그래서 연결 관리는 부모가, 요청 처리는 자식이 맡는 서버에서는 자식이 필요 없는 리스닝 소켓을 바로 닫아야 한다.

## Evidence

- 자식은 HTTP 서버 소켓 같은 부모의 리스닝 FD 를 close 하고, 자기가 맡은 클라이언트 FD 만 select mask 에 넣어 이벤트를 처리한다.
- worker 와 client 를 1:1 로 매핑하면 한 요청의 오류가 다른 연결로 번지지 않는다.
- 부모는 자식 생성 수 제한 등 자원 한도를 관리해야 하고, 자식 종료는 SIGCHLD 로 감지한다.
