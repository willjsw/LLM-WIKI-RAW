---
pkm_id: CPT-0001
pkm_type: concept
title: "스킬 다이어트 - 리뷰 범위로 토큰 비용 제한"
job: "기획-PM"
domain: software-process
keywords:
  - "스킬 다이어트"
  - "토큰 비용"
  - "리뷰 범위"
  - "token budget"
  - "AI 리뷰 비용"
contributor: swj
revision: 70babfb2
exported_at: 2026-11-16
---

# 스킬 다이어트 - 리뷰 범위로 토큰 비용 제한

## Definition

AI 리뷰 스킬에 검토 범위를 명시적으로 제한해 토큰 소모를 관리하는 운용 방식이다. 리뷰 범위가 넓을수록 토큰 소모가 급격히 늘기 때문이다.

## Evidence

MR 하나를 전체 범위로 리뷰하다 하루치 토큰을 다 쓰는 상황이 생겼다. 스킬에 "여기까지만 봐라"를 지정해 범위를 조정하며, 리뷰 범위 설계를 처음부터 토큰 예산 관점에서 고려해야 한다.
