---
id: TASK-18
title: 'go 용어를 계획 승인으로 바꾸고, hooks 구현(TASK-58 ~ 63)에서 정해진 미정 항목을 설계 문서에 반영한다'
status: In Progress
assignee: []
created_date: '2026-10-21 08:57'
updated_date: '2026-10-22 05:36'
labels:
  - design
dependencies: []
references:
  - decision-1
  - decision-2
documentation:
  - 'https://github.com/coralstay/claude-code-agile-hooks/pulls'
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
유저 결정(2026-10-21): 'go'는 하는 일과 동떨어진 말이라 업계 관행(plan approval · approval gate)에 맞춰 바꾼다 — go → 계획 승인, go 판정 → 승인 게이트, Plan-Review-Go → 계획 → 리뷰 → 계획 승인, 커밋 제목 Go: <ID> → Plan-Approved: <ID>. 또 '사람이 쓴 건 사람, AI가 쓴 건 AI'를 지키도록 서명 키를 둘로 나눈다 — Claude는 AI 전용 키, 사람은 기존 키(ssh-agent에서 내려 암호 입력). 승인 게이트는 유효 서명(%G?=G)에 더해 서명자(%GS)가 humanSigners 목록에 있을 때만 통과한다. claude-code-agile-hooks decision-14(decision-13 대체)와 TASK-58 구현에 맞춘다. 대상: 2.02 · 2.03 · 3.03 · 3.04 · 3.05(ADR-022) · 용어집, 최상위 decision-1.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 design/ 전체에서 go · go 판정 · Plan-Review-Go · Go: <태스크 ID> 표기를 계획 승인 · 승인 게이트 · 계획 → 리뷰 → 계획 승인 · Plan-Approved: <태스크 ID>로 바꾼다(용어집 항목 포함)
- [ ] #2 2.02 구현 계획 형식 · 3.04 §1 · 3.05 ADR-022에 승인 게이트가 서명자(%GS)를 humanSigners 목록과 대조한다는 것과 두 키 구성(AI 전용 키 · 사람 키는 ssh-agent 밖)을 적고, ADR-022 기각한 대안에 '한 키로 유효 서명만 확인'을 추가한다
- [ ] #3 3.04 §7 프로젝트 설정 표에 humanSigners 키를 추가한다
- [ ] #4 '미정 — claude-code-agile-hooks DRAFT-N에서 확정'으로 남긴 항목을 hooks 구현 결과로 바꾼다: 계획 승인 커밋 형식(빈 서명 커밋, decision-14), 커버리지 지표 line + branch · 리포트 위치 설정 키 coverageReportDir · -s Done 게이트는 새 훅 require_coverage_on_done.py(TASK-62), 테스트 파일 헤더 '<ID>: <요약>' · 섹션 표식 '== AC/DoD ==' · '== Coverage ==' · 기존 파일 유예(TASK-61), 작업 순서 의존 출처 = 태스크 frontmatter dependencies(TASK-60), 전파 확인 = 로컬 components/* 모든 브랜치의 Refs 커밋 · 영향 없음 트레일러 Propagation-None: <컴포넌트>: <사유> · 차단 시점 최상위 -s Done(TASK-63, decision-15). 대상: 00 편집 규칙, 2.02, 2.03 RAIL-024, 3.04 §7, 3.05 ADR-022 · ADR-023 · ADR-025
- [ ] #5 작업 순서 재계산 규칙: 2.02 상태와 전이 · 전이와 커밋, 2.03 BL-016 · RAIL-023에 'draft든 To Do 태스크든 앞으로 할 일이 새로 생기거나 다시 열리거나 의존이 바뀔 때마다 의존을 정리하고 작업 순서를 다시 계산해 바로 커밋한다(작업 순서에는 draft도 포함)'를 반영한다 — claude-code-agile-hooks DRAFT-14와 맞춘다
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 grep으로 design/에 go 계열 옛 표기가 0건이다(다른 뜻의 영단어 제외)
- [ ] #2 design/ 상대 링크 검사에서 깨진 링크가 없다(기존 템플릿 예시 1건 제외)
- [ ] #3 파일 하나에 커밋 하나, push하지 않는다
- [ ] #4 grep -rn '미정 — claude-code-agile-hooks DRAFT' design 결과가 0건이다
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
### Subjective
유저가 go라는 말이 무엇인지 모르겠다며 하는 일에 맞는 용어로 바꾸라고 했고(업계 관행 확인 후 계획 승인 + Plan-Approved 선택), AI 커밋과 사람 커밋을 서명으로 가르는 방식으로 두 키 + 사람 키 agent 제외를 골랐다(2026-10-21).

### Objective
design/에서 go 계열 표기는 6개 파일 약 48곳(2.02 · 2.03 · 3.03 · 3.04 · 3.05 · 용어집). 최상위 decision-1은 제목만 있는 결정('go = 사람의 서명 커밋')이다. hooks 쪽 decision-14와 TASK-58이 새 용어와 서명자 확인을 구현 중이다.

### Assessment
용어 치환은 기계적이지만 문장마다 조사를 맞춰야 하므로 파일별로 읽으며 고친다. 서명자 확인은 ADR-022 결정 · 결과와 2.02 구현 계획 형식, 3.04 계약 · 설정 표에 넣는다. 최상위 decision-1은 CLI로 본문을 고칠 수 없으므로 새 decision으로 대체를 기록한다.

### Plan
1. hooks TASK-58 결과(설정 키 이름 · 메시지)를 확인한다.
2. 2.02 → 2.03 → 3.03 → 3.04 → 3.05 → 용어집 순서로 고치고 파일마다 커밋한다.
3. 최상위 decision-2로 decision-1 대체를 기록한다.
4. grep · 링크 검사.

추가(2026-10-22): hooks 저장소 TASK-58 ~ TASK-63이 끝나 '미정 — DRAFT-N에서 확정' 항목들이 정해졌다(PR coralstay/claude-code-agile-hooks#54 ~ #59). AC #4로 이 반영을 함께 한다. grep -rn '미정 — claude-code-agile-hooks DRAFT' design 결과가 0건이어야 한다(PRG 강제 방법처럼 hooks draft가 없는 미정은 그대로).
<!-- SECTION:PLAN:END -->
