---
id: DRAFT-1
title: 구현 계획 필수 · 단계별 커밋 · 작업 순서 · 커버리지 100% · 테스트 파일 구조를 설계 문서에 반영
status: Draft
assignee: []
created_date: '2026-10-12 02:29'
updated_date: '2026-10-12 03:07'
labels:
  - design
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
유저 요청(2026-10-12)으로 claude-code-agile-hooks에 draft 5장(DRAFT-8 구현 계획 필수, DRAFT-9 단계별 커밋, DRAFT-10 커버리지 100% + 리포트, DRAFT-11 테스트 파일 구조, DRAFT-12 승격마다 작업 순서 파일)을 등록했다. 이 draft는 그 결과를 design/에 반영하는 후속 작업이다(TASK-12 · TASK-13 방식). 문구는 구현 결과에 맞춰야 하므로 DRAFT-8 ~ DRAFT-12가 끝난 뒤에 진행한다. push는 범위 밖이다(유저 결정 2026-10-12).

새 ID: BL-015 · BL-016, RAIL-020 ~ RAIL-023, NFR-017, ADR-021 · ADR-022(현재 마지막 번호: BL-014 · RAIL-019 · NFR-016 · ADR-020).
components/claude-code-agile-hooks/design/은 아직 골격뿐이라 대상에서 뺀다. 계획: ~/.claude/plans/sunny-enchanting-conway.md
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 구현 계획 필수: 2.02 태스크 카드 구성 표의 구현 계획 행(승격 전 필수)과 상태와 전이 표의 조건, 2.03 BL 표에 BL-015, RAIL 표에 RAIL-020을 넣는다
- [ ] #2 단계별 커밋: 2.02 상태와 전이 아래 새 소절 '전이와 커밋', 2.03에 RAIL-021과 RAIL-002 · RAIL-008 갱신, 3.04 §3 상태 전이 표, 3.03 §4 backlog.md 사용 규약 표에 반영한다
- [ ] #3 커버리지 100%: 2.04에 NFR-017, 2.03 RAIL-006 갱신, 3.04 §7 coverageCommand 행과 언어별 리포트 위치 표에 반영한다
- [ ] #4 테스트 파일 구조: 2.02 테스트 표식 표에 DoD 행 <카드 ID>#D<n>과 새 소절 '테스트 파일 구조', 2.03에 RAIL-022, 4.02 테스트 추적 표에 반영한다
- [ ] #5 작업 순서 파일: 2.02 상태와 전이에 승격 직후 의존 정리, 2.03에 BL-016 · RAIL-023, 3.03 §4 backlog.md 사용 규약 표에 --dep · task list --ready 행, 3.04 §3 상태 전이 표에 반영한다
- [ ] #6 공통: 3.03 §2의 구현 요구사항 칸과 세 가지 성격 표, 3.05 결정 목록에 ADR-021 · ADR-022를 추가하고, design/ 상대 링크 검사에서 깨진 링크가 없다
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. DRAFT-8 ~ DRAFT-12의 final summary와 decision을 읽고 확정된 문구 · 키 이름을 모은다.
2. 2 요구사항(2.02 → 2.03 → 2.04) → 3 아키텍처(3.03 → 3.04 → 3.05) → 4.02 순서로, 파일 하나에 커밋 하나씩 반영한다.
3. design/ 상대 링크 검사를 돌리고, 다이어그램이 바뀌면 build-diagrams.py로 다시 렌더한다.
<!-- SECTION:PLAN:END -->
