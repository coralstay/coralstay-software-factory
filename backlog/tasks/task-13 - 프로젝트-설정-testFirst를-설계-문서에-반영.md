---
id: TASK-13
title: 프로젝트 설정 testFirst를 설계 문서에 반영
status: Done
assignee: []
created_date: '2026-10-11 08:49'
updated_date: '2026-10-11 08:49'
labels:
  - docs
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
claude-code-agile-hooks에 require_test_first 훅(TASK-56)이 생기면서 프로젝트 설정 .claude-code-agile-hooks.json에 testFirst(sourceGlobs · testGlobs) 블록이 추가됐다. 최상위 3.04 §7 프로젝트 설정과 3.03 §2 프로젝트 설정 칸은 아직 testCommand · coverageCommand만 적고 있다.

수용 기준(승격 시 AC로 등록):
1. 3.04 §7과 3.03 §2에 testFirst 블록(필드 · 의미 · opt-in · 예시)을 적는다
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 3.04 §7과 3.03 §2에 testFirst 블록(필드 · 의미 · opt-in · 예시)을 적는다
<!-- AC:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
3.04 §7 프로젝트 설정에 testFirst(sourceGlobs · testGlobs) 예시 · 동작 · 실패 시 행동(RAIL-019 · ADR-020)과 'opt-in' 원칙을, 3.03 §2 프로젝트 설정 칸에 testFirst를 추가했다. claude-code-agile-hooks TASK-56(require_test_first 훅)에 맞춘 후속.
<!-- SECTION:FINAL_SUMMARY:END -->
