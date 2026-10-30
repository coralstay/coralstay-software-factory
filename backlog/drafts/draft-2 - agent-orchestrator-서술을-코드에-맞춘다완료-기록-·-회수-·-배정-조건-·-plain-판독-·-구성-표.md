---
id: DRAFT-2
title: agent-orchestrator 서술을 코드에 맞춘다(완료 기록 · 회수 · 배정 조건 · --plain 판독 · 구성 표)
status: Draft
assignee: []
created_date: '2026-10-30T12:33:00Z'
updated_date: '2026-10-30T12:33:00Z'
labels:
  - design
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
2026-10-30 드리프트 점검에서 최상위 design/의 agent-orchestrator 서술이 코드와 어긋났다. 완료 기록은 CommitLedger · Logger가 아니라 TaskCardSource/BacklogCardSource가 Token Budget 소절에 쓰고, 회수에 /clear가 없으며, 배정은 isReady가 아닌 자체 계산, 판독은 --plain이다.

코드 기준점: components/agent-orchestrator 작업 트리 task/AO-30(main 미병합 AO-28~30 포함). 동작 코드는 BacklogClient · WorktreeManager · AgentSpawner · SessionRegistry이고, TaskCardSource · BacklogCardSource · ClaudeCodeRunner · ModelPolicy는 스텁 + pending 테스트 계약이다. AllocationPolicy(AO-25)는 결정됐지만 코드는 옛 ModelPolicy 스텁이므로 문서를 되돌리지 않고 단서만 단다.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 완료 기록 서술을 코드에 맞춘다 — 쓰는 쪽은 TaskCardSource/BacklogCardSource, 내용은 Description ### Token Budget 소절의 estimated · attempt n · actual 줄(recap · 커밋 판독 없음), 실패 시도도 기록, 태스크 워크트리에서 커밋 — 3.02 §4, 3.04 §1, diagrams/07-task-sequence.mmd (수동)
- [ ] #2 회수 서술을 코드에 맞춘다 — /clear 단계 삭제(07 mmd), destroy → 500ms → destroyForcibly, 유예 TBD(Q-16) 옆에 현재 구현값 500ms (3.02 §6, 3.03 §1) (수동)
- [ ] #3 3.01 의존 방향을 '--plain으로 읽고 상태는 바꾸지 않으며 Token Budget만 기록'으로, 3.03 §1 · 3.04의 기계 판독 --json을 --plain으로 고친다 (수동)
- [ ] #4 배정 조건 서술(3.03 §1, 3.04 §3, 4.02)을 'isReady를 쓰지 않고 To Do ∧ 직접 의존 전부 Done ∧ 미병합 task/<ID> 브랜치 없음(git cherry, 로컬 · 원격)'으로 고친다 (수동)
- [ ] #5 3.03 §1 구성 표와 3.04 스폰 인자를 코드에 맞춘다 — CommitLedger · RunCommand를 현재 클래스에서 빼고 card/TaskCardSource · BacklogCardSource 추가, usage 판독은 ClaudeCodeRunner, SessionRegistry 기본 용량 1, 스폰 인자 -p · --permission-mode auto · --permission-prompts none (수동)
- [ ] #6 미구현 단서를 단다 — AllocationPolicy(AO-25 예정, 코드는 ModelPolicy 스텁), run 미배선, runs.jsonl · install-tools.sh · In Progress 전환 프롬프트 · '착수 안 됨' 경로 (수동)
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
- 완료 기록: TaskCardSource.java:13-18 · 21-22 · 36-40, BacklogCardSource.java:16-17 · 20-21 · 33 · 52. CommitLedger는 작업 트리에 없음(AO-6 Q-18 보류).
- 회수: AgentSpawner.java:199 · 211-218, SessionRegistry.java:38 · 138-139.
- 판독 · 배정: BacklogClient.java:77 · 124-125 · 131-140 · 153-167.
- 스폰 인자: AgentSpawner.java:124-131, AgentRunner.java:62-67 · 108 · 123-136.
- 미구현: Main.java:50-53(run), runs.jsonl은 ModelPolicy.java:26 주석뿐, install-tools.sh 없음, -s In Progress 호출 없음.
- 문서 위치: 3.01:19, 3.02:77 · 108 · 142-145, 3.03:13 · 23-33 · 25 · 29 · 37 · 44 · 48, 3.04:23 · 76 · 84 · 105-107 · 119 · 148, 4.02:57-60, 2.01:46, 3.02:9, 07 mmd:40 · 42.

### Assessment
스텁의 시그니처와 pending 테스트도 코드 계약으로 본다. 단, AllocationPolicy처럼 결정이 코드보다 앞선 것은 문서를 되돌리지 않는다. Q-16은 닫지 않고 현재 구현값만 병기한다.

### Plan
1. 3.03 §1 → 3.04 → 3.02 → 3.01 → 4.02 → 2.01 → diagrams/07-task-sequence.mmd(+ build-diagrams.py로 SVG) 순서로 파일마다 커밋한다.
2. grep '/clear' · 'CommitLedger' · '--json' · 'isReady ∧' 결과를 노트에 남긴다.
3. 상대 링크 검사, 장 대응표로 전파 대상 확인(agent-orchestrator design/이 코드와 맞으면 Propagation-None, 아니면 멈추고 보고).
<!-- SECTION:PLAN:END -->
