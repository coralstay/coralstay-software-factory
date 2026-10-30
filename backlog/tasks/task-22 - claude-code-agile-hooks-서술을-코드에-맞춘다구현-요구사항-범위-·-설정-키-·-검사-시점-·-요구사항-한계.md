---
id: TASK-22
title: claude-code-agile-hooks 서술을 코드에 맞춘다(구현 요구사항 범위 · 설정 키 · 검사 시점 · 요구사항 한계)
status: To Do
assignee: []
created_date: '2026-10-30T12:33:00Z'
updated_date: '2026-10-30T12:49:00Z'
labels:
  - design
dependencies:
  - TASK-21
documentation:
  - /Users/flynn_macpro/.claude/plans/starry-greeting-curry.md
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
2026-10-30 드리프트 점검에서 최상위 design/의 claude-code-agile-hooks 서술이 코드와 어긋났다. RAIL-015~018은 이미 구현됐는데 구현 목록에 없고, humanSigners는 필수인데 opt-in으로 적혀 있으며, 여러 RAIL 요구사항이 코드보다 넓게 적혀 있다. 브랜치 시점 착수 검사 · (수동) 예외 · RAIL-025는 결정은 반영됐지만 코드는 TASK-68 · 69 · 70(To Do)이라 단서만 단다.

코드 기준점: components/claude-code-agile-hooks 저장소 HEAD(설치본과 바이트 동일) — hooks/*.py, settings.hooks.json. 코드가 원칙보다 넓게 허용하는 것(permission_auto_allow의 find · git branch · git remote, pre_push_coverage_check의 push allow)은 이 카드에서 문서를 바꾸지 않고 그 저장소의 버그 draft로 넘긴다.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 3.03 §2 구현 요구사항을 코드에 맞춘다 — RAIL-015 ~ 018 포함(session_start · instructions_audit · reserved_tag_guard · permission_auto_allow), RAIL-010은 미구현으로 표시 (수동)
- [ ] #2 설정 키를 코드에 맞춘다 — 3.03 §2 · 3.04 §7에 humanSigners(-s "In Progress"에서 필수) · coverageReportDir, require_test_layout은 testFirst 없이도 기본 패턴으로 검사, testFirst Done은 #D<n>도 요구 (수동)
- [ ] #3 2.03 RAIL 문구를 코드 동작에 맞춘다 — RAIL-002 · 003 · 005 · 006 · 007 · 008 · 016 · 023의 조건 · 한계 (수동)
- [ ] #4 RAIL-024 커밋 선택을 브랜치 범위로 적는다(2.03 RAIL-025 문장, 메시지 ID 방식은 TASK-66 예정), 3.05 ADR-025의 '원격 브랜치는 보지 않고'를 git log --all 기준으로 고친다 (수동)
- [ ] #5 3.02 §2 Phase B에 promote 때 SOAP · AC · DoD가 없으면 훅이 거부하고, 작업 순서 갱신은 다음 단계 명령에서 강제한다(생성 직후 강제는 TASK-64)는 것을 적는다 (수동)
- [ ] #6 미구현 단서를 단다 — 브랜치 생성 · 전환 시점 착수 검사와 브랜치 기반 편집 차단(TASK-68), (수동) 예외(TASK-69), RAIL-025(TASK-70) (수동)
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 바꾼 문장마다 근거 코드 위치(file:line)를 구현 노트에 적는다 (수동)
- [ ] #2 옛 표현 grep 결과를 노트에 남긴다 (수동)
- [ ] #3 design/ 상대 링크 깨짐 0, 요구사항 ID 재사용 · 재번호 없음 (수동)
- [ ] #4 파일 하나에 커밋 하나, 각 커밋에 카드 ID, push 하지 않는다 (수동)
- [ ] #5 Done 전에 장 대응표로 영향받는 컴포넌트마다 Refs 커밋 또는 Propagation-None 트레일러를 남긴다 (수동)
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
### Subjective
유저 결정(2026-10-30): 최상위 design/의 코드 ↔ 문서 불일치만 고친다. 방향은 코드 → 문서. 코드가 다르게 구현돼 있고 그것을 뒤집는 결정이 없으면 문서를 코드에 맞추고, 결정이 먼저 반영되고 코드는 카드로 예정만 된 것은 규칙 문장을 두고 '현재 미구현(카드 ID)' 단서만 단다. 코드가 원칙보다 넓게 허용하는 것은 문서를 바꾸지 않는다. 문서끼리만 어긋나는 항목은 범위 밖이다. 계획: ~/.claude/plans/starry-greeting-curry.md

### Objective
- 구현: session_start.py:45-54, instructions_audit.py:2-17, reserved_tag_guard.py:2-5, permission_auto_allow.py:24-28. 역할 인식 훅 없음(RAIL-010).
- 착수 검사: require_implementation_plan.py:5 · 10 · 238-241 · 446-455 · 466, require_work_order.py:7 · 13-15 · 24-27. git switch · checkout · worktree add 처리 훅 없음.
- 설정: pre_commit_check.py:189 · 216-226, pre_push_coverage_check.py:190 · 409 · 427, require_coverage_on_done.py:28-31 · 85, require_implementation_plan.py:136, require_test_first.py:177 · 504-516, require_test_layout.py:9-17 · 175.
- 그 밖: require_active_task.py:76-88, block_stop_if_dirty.py:2-4, pre_push_check.py:206-207, require_stage_committed.py:9-13 · 50, require_design_propagation.py:30-36 · 355-391 · 516. (수동)은 grep 0건.
- 카드: TASK-64 · 66 · 68 · 69 · 70 모두 To Do.

### Assessment
코드가 동작을 정한 것은 문서를 맞추고, A1 · A6 · C2처럼 결정이 앞선 것은 규칙 문장을 남기고 '현재 미구현(카드)'만 단다. 원칙보다 넓은 허용은 버그로 보고 문서에 적지 않는다.

### Plan
1. 2.03 → 3.03 §2 → 3.04 → 3.05 → 3.02 → 2.02 → 4.01 · 4.02 순서로 파일마다 커밋한다.
2. 단서 문구는 '현재 미구현(claude-code-agile-hooks TASK-n)' 하나로 통일하고 grep으로 개수를 노트에 남긴다.
3. 상대 링크 검사, 장 대응표로 전파 대상 확인(claude-code-agile-hooks design/은 TASK-65 대기 중 — 영향 사유를 Propagation-None으로 남길지 유저에게 묻는다).
<!-- SECTION:PLAN:END -->
