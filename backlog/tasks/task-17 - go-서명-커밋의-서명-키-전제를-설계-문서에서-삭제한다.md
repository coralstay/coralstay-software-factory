---
id: TASK-17
title: go 서명 커밋의 서명 키 전제를 설계 문서에서 삭제한다
status: In Progress
assignee: []
created_date: '2026-10-21 04:54'
updated_date: '2026-10-21 04:57'
labels:
  - design
dependencies: []
references:
  - decision-1
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
유저 지시(2026-10-21): TASK-15가 넣은 'go 서명 커밋은 사람의 서명 키가 Claude 실행 환경에 없어야 한다'는 전제를 삭제한다. 대상 3곳 — 2.02 구현 계획 형식(56행), 3.03 §2 ① 절차 강제 아래 항목(70행), 3.05 ADR-022 결과(193행). go = 사람이 직접 남기는 서명 커밋(decision-1)과 미정 항목(go 커밋 세부 형식 — claude-code-agile-hooks DRAFT-8)은 그대로 둔다.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 2.02 구현 계획 형식에서 '훅은 서명만으로 사람과 Claude를 구분하므로, 사람의 서명 키가 Claude의 실행 환경에 없어야 한다' 문장을 지운다
- [ ] #2 3.03 §2의 '훅은 서명으로만 사람과 Claude를 가르므로, 사람의 서명 키가 Claude의 실행 환경에 없어야 한다' 문장을 지운다
- [ ] #3 3.05 ADR-022 결과에서 서명만으로 구분 · 같은 서명 키면 구분 불가 · 전제 문장을 지우고, go 판단 지점 추가와 미정 항목은 남긴다
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 grep -rn '서명 키' design 결과가 0건이다
- [ ] #2 design/ 상대 링크 검사에서 깨진 링크가 없다(기존 템플릿 예시 1건 제외)
- [ ] #3 파일 하나에 커밋 하나, push하지 않는다
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
### Subjective
유저가 TASK-15에서 넣은 서명 키 전제를 삭제하라고 했다(2026-10-21).

### Objective
grep -rn '서명 키' design → 3건: 2.02 56행, 3.03 70행, 3.05 193행(ADR-022 결과). 세 곳 모두 '사람의 서명 키가 Claude 실행 환경에 없어야 한다'는 전제 문장이다.

### Assessment
전제 문장과 그 근거 문장(서명만으로 구분 · 같은 키면 구분 불가)만 지운다. go = 사람의 서명 커밋(decision-1), 세부 형식 미정(DRAFT-8) 문장은 남긴다.

### Plan
1. 2.02 → 3.03 → 3.05 순서로 문장 삭제, 파일마다 커밋.
2. grep · 링크 검사.
<!-- SECTION:PLAN:END -->
