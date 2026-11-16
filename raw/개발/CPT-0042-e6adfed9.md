---
pkm_id: CPT-0042
pkm_type: concept
title: "멀티 에이전트 협업 패턴 4종"
job: "개발"
domain: ai-agent
keywords:
  - "멀티 에이전트"
  - multi-agent
  - "Agent as Tool"
  - Swarm
  - Graph
  - Workflow
  - "오케스트레이션"
contributor: swj
revision: e6adfed9
exported_at: 2026-11-16
---

# 멀티 에이전트 협업 패턴 4종

## Definition

멀티 에이전트 협업은 Agent as Tool, Swarm, Graph, Workflow 네 패턴으로 나뉜다. 복잡한 업무일수록 단일 모놀리식 에이전트보다 전문화된 에이전트의 협업 구조가 유리하다.

## Evidence

| 패턴 | 특징 | 적합한 경우 |
|---|---|---|
| Agent as Tool | 에이전트를 다른 에이전트의 도구로 사용 | 단순 위임 |
| Swarm | 자율 협업, 병렬 태스크 분배, 에이전트 간 직접 통신 | 탐색적·병렬적 작업 |
| Graph | 에이전트=노드, 의존성=엣지 | 여러 전문 분석 결과 연결 |
| Workflow | 명시적 순서, 이전 출력=다음 입력 | 재현 가능한 절차 업무 |

- 멀티 에이전트의 이점: 전문화, 확장성(분산·탄력 확장), 비용 효율(리소스 경량화), 유지보수성
- 실전 예: 도메인 전문가 에이전트 + 리드(오케스트레이터) 에이전트, 기획–실행–평가 에이전트 분리
