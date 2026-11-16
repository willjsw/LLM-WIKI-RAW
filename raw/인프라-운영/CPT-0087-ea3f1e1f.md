---
pkm_id: CPT-0087
pkm_type: concept
title: "Redis Sentinel 은 3대 이상 분산하고 같은 네트워크에 둔다"
job: "인프라-운영"
domain: high-availability
keywords:
  - "Redis Sentinel"
  - failover
  - "마스터 선출"
  - quorum
  - "Redis 이중화"
contributor: swj
revision: ea3f1e1f
exported_at: 2026-11-16
---

# Redis Sentinel 은 3대 이상 분산하고 같은 네트워크에 둔다

## Definition

Redis master 장애 시 새 master 를 선출하는 Sentinel 은 과반 합의가 가능하도록 서로 다른 서버 3대 이상에 분산해 둔다.

## Evidence

- 2대 구성에서 Master Shutdown 시 이벤트 지연이 관찰돼, 통계 서버에 Sentinel 을 추가해 3대로 분산했다.
- 운영 환경에서는 VM 으로 분리해 Sentinel 을 분산하고, 1대는 DB 서버에 둔다. Sentinel 용 RAM 은 1~2GB 정도로 잡았다.
- Sentinel 들은 같은 네트워크에 있어야 한다.
