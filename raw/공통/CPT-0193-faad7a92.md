---
pkm_id: CPT-0193
pkm_type: concept
title: "도메인 지식을 실행 가능한 규칙과 테스트로 바꾸기"
job: "공통"
domain: ai-assisted-development
keywords:
  - "도메인 지식"
  - invariant
  - "실행 가능한 명세"
  - "테스트"
  - "AI 에이전트"
  - "규칙화"
contributor: swj
revision: faad7a92
exported_at: 2026-11-16
---

# 도메인 지식을 실행 가능한 규칙과 테스트로 바꾸기

## Definition

조직의 도메인 지식을 '반드시 성립해야 하는 것'과 '절대 일어나면 안 되는 것' 같은 규칙(Invariant)으로 적고, 그 규칙을 자동 테스트로 실행할 수 있게 만드는 작업이다. AI 에이전트가 이 규칙을 맥락과 검증 기준으로 쓰게 된다.

## Evidence

- 단계: Domain Knowledge(프로토콜 규칙, 이중화·절체 규칙, 보안·개인정보, 업무 처리 규칙) → Rule/Invariant(상태 전이 조건, 아키텍처 경계) → Executable(테스트로 실행 가능).
- 예: 패킷 덤프를 분석해 규칙 위반 여부를 리포트하는 테스트.
- 코드 작성 능력보다 도메인 지식이 AI 활용 수준을 정한다는 관점에서 나온 방향이다.
- 사내 사례에서는 과거 장애 목록과 서비스 특성(Active-Active 등)을 리뷰 스킬과 CLAUDE.md, REVIEW.md에 녹였다.
