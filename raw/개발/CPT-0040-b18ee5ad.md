---
pkm_id: CPT-0040
pkm_type: concept
title: "ReAct 루프와 Agent 메모리 계층"
job: "개발"
domain: ai-agent
keywords:
  - ReAct
  - "Agent Memory"
  - "단기 메모리"
  - "장기 메모리"
  - Compaction
  - "에이전트 루프"
contributor: swj
revision: b18ee5ad
exported_at: 2026-11-16
---

# ReAct 루프와 Agent 메모리 계층

## Definition

ReAct는 LLM이 추론(Reasoning)으로 다음 행동을 정하고 행동(Acting)으로 도구를 호출한 뒤 결과를 관찰하는 루프를 반복하는 에이전트의 기본 동작 패턴이다. 메모리는 ReAct 자체에 속하지 않는 별도 구성요소로, 단기 메모리와 장기 메모리로 계층화된다.

## Evidence

- 추론: LLM 호출로 요청 이해, 실행 계획 수립, 다음 행동 결정
- 행동: 도구(DB, API 등) 호출 후 결과 저장
- 단기 메모리: Agent 상태, 메시지 순서, 실행 계획, 루프 간 공유 스크래치패드
- 장기 메모리: 벡터 스토어 기반 시맨틱 검색
- Context Window 한계에 닿으면 대화·기록을 압축(Compaction)하며, 대부분 프레임워크가 이를 처리한다
