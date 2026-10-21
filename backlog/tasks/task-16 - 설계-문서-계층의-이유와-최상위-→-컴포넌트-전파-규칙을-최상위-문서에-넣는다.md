---
id: TASK-16
title: 설계 문서 계층의 이유와 최상위 → 컴포넌트 전파 규칙을 최상위 문서에 넣는다
status: To Do
assignee: []
created_date: '2026-10-12 06:15'
updated_date: '2026-10-21 04:05'
labels:
  - design
dependencies:
  - TASK-15
documentation:
  - >-
    components/claude-code-agile-hooks/backlog/drafts/draft-13 -
    최상위-설계-문서를-고치면-컴포넌트-설계-문서-전파를-훅으로-강제한다.md
  - design/00-문서-정보.md
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
유저 질문(2026-10-12): 설계 문서(design/)가 왜 최상위 한 곳과 컴포넌트 세 곳(agent-orchestrator · claude-code-agile-hooks · coding-agent-git-commit-tool)에 나뉘어 있는가? 최상위 문서를 고치면 하위 컴포넌트 문서도 반드시 고치게 강제하고, 그 규칙을 최상위 문서에 넣으라고 했다.

지금 구성의 이유는 문서 곳곳에 흩어져 있고, 설계 결정(ADR)으로 적힌 적은 없다.
- 컴포넌트는 각자 독립된 git 저장소다. 루트 .gitignore 주석("컴포넌트 저장소는 각자 독립된 git 저장소다 (components/<name>)")과 design/00-문서-정보.md의 "대상 저장소" 표에 적혀 있다.
- SDD는 저장소마다 적용된다. 각 00-문서-정보.md의 "명세와 코드가 어긋나면 명세를 먼저 고친 뒤 코드를 맞춘다" 때문에, 명세가 코드와 같은 저장소에 있어야 같은 PR에서 함께 바뀐다.
- 역할이 나뉜다. 최상위는 목표 · 원칙 · 요구사항 ID를 소유한다(components/claude-code-agile-hooks/design/00-문서-정보.md: "요구사항 ID는 최상위 2.03 · 2.04에서만 부여한다"). 컴포넌트는 그것을 같은 ID로 이어받아 패키지 · 클래스로 내린다(components/agent-orchestrator/design/00-문서-정보.md 상위 문서 표).
- 에이전트가 읽는다. design/00-문서-정보.md 편집 규칙에 따라 오케스트레이터가 띄우는 에이전트는 design/ 파일을 조상 문서로 읽으므로(ORC-019), 명세가 그 저장소 안에 있어야 한다.

빠진 것: 상속 규칙("어겨야 하면 최상위 결정을 먼저 고친다")은 있지만, 최상위를 고치면 하위도 맞춘다는 전파 의무는 없다. 10-11 사전 점검에서 나온 최상위 ↔ 컴포넌트 불일치 29건의 원인이다.

저장소 구조(2026-10-12 확인): 루트 .gitignore 2행이 components/를 제외하고, git check-ignore로 컴포넌트 3개와 agent-orchestrator-wt가 모두 무시되며, 최상위가 추적하는 components/ 파일은 0개다. .gitmodules는 없다 — 컴포넌트는 서브모듈이 아닌 독립 저장소다. 따라서 최상위 git · backlog는 그대로 둔다.

DRAFT-1(구현 계획 · 단계별 커밋 등 설계 문서 반영)과 범위가 겹치지 않도록 별도 draft로 둔다. 전파 의무를 훅으로 강제하는 일은 claude-code-agile-hooks DRAFT-13에서 하고, 이 draft의 장 대응표를 그 훅이 읽는다. 영향 없음 사유의 기록 형식도 그 draft에서 확정한다. 계획: ~/.claude/plans/sunny-enchanting-conway.md
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 00 문서 정보: '대상 저장소' 표 아래 새 절 '문서 계층'을 두고, 컴포넌트는 components/<이름>에 두는 독립 저장소이며 최상위 .gitignore가 제외한다는 것(서브모듈 아님), 최상위는 ID · 원칙 · 목표를 소유하고 컴포넌트 design/이 그것을 이어받는다는 것, 장 대응표(최상위 장 → 컴포넌트 장)를 적는다
- [ ] #2 00 편집 규칙: 최상위 문서를 고친 변경은 영향받는 컴포넌트 design/을 반드시 같이 고치고, 영향이 없으면 사유를 남긴다는 규칙을 넣는다(사유 기록 형식은 claude-code-agile-hooks DRAFT-13에서 확정한 것을 따른다)
- [ ] #3 2.03: 전파 의무와 그 훅 강제를 새 요구사항으로 넣는다. 번호는 반영 시점의 다음 번호를 쓴다
- [ ] #4 3.05: 문서 계층을 저장소마다 두는 이유와 전파 규칙을 새 ADR로 넣고, 기각한 대안(최상위 하나만 · 컴포넌트에 사본 · 서브모듈)과 기각 이유를 적는다
- [ ] #5 컴포넌트 3곳(agent-orchestrator · claude-code-agile-hooks · coding-agent-git-commit-tool)의 design/00-문서-정보.md에 '최상위 00 문서 계층' 참조 한 줄을 둔다
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 design/ 상대 링크 검사에서 깨진 링크가 없다
- [ ] #2 컴포넌트 3곳의 00 문서 정보 변경은 각 컴포넌트 저장소에 같은 태스크 ID로 커밋한다
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
### Subjective
유저는 설계 문서가 왜 최상위와 컴포넌트 세 곳에 나뉘어 있는지 묻고, 최상위 문서를 고치면 컴포넌트 문서도 반드시 고치도록 강제하며 그 규칙을 최상위 문서에 넣으라고 했다(2026-10-12).

### Objective
- 루트 .gitignore 2행 components/, 위 주석에 "컴포넌트 저장소는 각자 독립된 git 저장소다". git check-ignore로 컴포넌트 3개 + agent-orchestrator-wt 무시, 최상위 추적 파일 0개, .gitmodules 없음.
- design/00-문서-정보.md에 '대상 저장소' 표(컴포넌트 → 3.03 §1 ~ §4)와 편집 규칙(ORC-019 조상 문서)이 있지만 '문서 계층' 절과 전파 의무는 없다.
- 컴포넌트 3곳의 00-문서-정보.md는 최상위를 상위 문서로 두고 ID · 원칙을 이어받는다. 상속 규칙은 있으나 역방향 전파 규칙은 없다.
- 10-11 사전 점검에서 최상위 ↔ 컴포넌트 불일치 29건.

### Assessment
문제는 하향 전파 의무가 없어서 최상위 변경이 컴포넌트에 반영되지 않고 쌓인다는 것이다. 이유와 규칙을 00 문서 정보(문서 계층 절 · 편집 규칙)와 3.05 ADR에 적고, 2.03 요구사항으로 훅 강제와 이어 둔다. 장 대응표는 훅이 읽을 입력이므로 기계가 읽을 수 있는 표 형식으로 둔다. 사유 기록 형식은 훅 draft의 결정을 기다린다.

### Plan
1. claude-code-agile-hooks 쪽 전파 강제 훅 draft에서 정한 사유 형식(트레일러 이름)과 대응표 형식을 확인한다.
2. design/00-문서-정보.md에 '문서 계층' 절(장 대응표 포함)과 편집 규칙 한 항목을 넣는다.
3. 2.03에 새 요구사항, 3.05에 새 ADR(기각 대안 포함)과 결정 목록 행을 넣는다. 파일 하나에 커밋 하나.
4. 컴포넌트 3곳의 design/00-문서-정보.md에 참조 한 줄을 각 저장소에서 커밋한다.
5. design/ 상대 링크 검사를 돌린다.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
승격 시 조정(2026-10-21): 전파 영향 없음 사유의 기록 형식은 claude-code-agile-hooks DRAFT-13이 아직 draft이므로 문서에 '미정 — claude-code-agile-hooks DRAFT-13에서 확정'으로 적는다. 요구사항 · ADR 번호는 TASK-15가 쓴 다음 번호를 쓴다.
<!-- SECTION:NOTES:END -->
