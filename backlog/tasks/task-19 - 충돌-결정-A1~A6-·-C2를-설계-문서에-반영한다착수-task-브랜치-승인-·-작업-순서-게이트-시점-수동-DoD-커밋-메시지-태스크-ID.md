---
id: TASK-19
title: >-
  충돌 결정 A1~A6 · C2를 설계 문서에 반영한다(착수 = task 브랜치, 승인 · 작업 순서 게이트 시점, (수동) DoD, 커밋
  메시지 태스크 ID)
status: In Progress
assignee: []
created_date: '2026-10-29 02:30'
updated_date: '2026-10-29 02:45'
labels:
  - design
dependencies: []
references:
  - decision-2
  - decision-3
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
유저 결정(2026-10-29): 2026-10-22 작업(hooks TASK-58~66, 최상위 TASK-14~18, AO-27/28)에서 드러난 충돌 7건을 결정했다. 설계 문서(design/)는 아직 옛 규칙(In Progress 전환 = 착수 · 승인 게이트, 사람 상태 락, 커밋 트레일러 토큰)을 적고 있다.

결정:
- A1: 계획 승인 검사(Plan-Approved + humanSigners)는 `task/<ID>` 브랜치 생성 · 전환 시점에 한다. claude-code-agile-hooks에만 두고 훅 설치 시에만 적용. `-s "In Progress"`는 계속 하지만 판단 기준이 아니라 기록이다.
- A2: 착수 = main에 병합되지 않은 `task/<ID>` 브랜치가 있다. main에 claim 커밋 없음. 알려진 제한: backlog.md 1.51.0의 task list · view · overview · search · `backlog browser`는 main에서 착수 카드를 To Do로 보인다(2026-10-29 실측, 로컬 · 원격 브랜치 모두 — branch scan은 ID 발번용).
- A3: 오케스트레이터가 직접 하는 커밋(실제치 기록)은 AI_AGENT · CLAUDE_CODE_SESSION_ID · CLAUDE_PID를 지우고 실행한다. '프로그램 커밋' 구분은 coding-agent-git-commit-tool GF-130 때 설계.
- A4: 토큰 실제치는 당분간 `session`(헤드리스 claude -p JSON usage, 오케스트레이터 ClaudeCodeRunner가 읽음 — ADR-021의 예외)만. `commits`(커밋 귀속분)는 Q-18 이후.
- A5: 작업 순서 파일 검사(RAIL-023)는 브랜치 생성 시점에 훅이 한다. 배정 조건 ORC-005 = isReady ∧ To Do ∧ `task/<ID>` 브랜치 없음. 오케스트레이터는 work-order.md를 읽지 않는다.
- A6: DoD 항목 끝이 `(수동)`이면 Done 게이트가 `<ID>#D<n>` 표식을 요구하지 않는다.
- C2: `task/<ID>` 브랜치에서 메시지에 그 ID가 없는 커밋은 훅이 거부한다(신설 RAIL-025). TASK-14 이력은 고치지 않는다.

대상: 1.03 · 1.04 · 2.01 · 2.02 · 2.03 · 2.04 · 3.02 · 3.03 · 3.04 · 3.05 · 4.01 · 4.02 · 4.03 · 부록 용어집, 최상위 decision-3(decision-2의 착수 시점 부분 대체). 컴포넌트 전파: agent-orchestrator AO-29 · AO-30, claude-code-agile-hooks(TASK-65 범위 확대 + 새 카드), coding-agent-git-commit-tool(GF-130 연기 한 줄 또는 Propagation-None).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 A1: 2.02 · 2.03(RAIL-020 · BL-017) · 3.03 · 3.04(착수 · humanSigners) · 3.05 ADR-022 · 용어집에서 승인 게이트 시점을 `-s "In Progress"`에서 `task/<ID>` 브랜치 생성 · 전환으로 옮기고, 2.02 전이와 커밋 표에 브랜치 생성(게이트) 단계를 넣고 In Progress 전환은 기록 단계로 적는다
- [x] #2 A2: 1.03 G-5 · 1.04 R-6 · 2.01 · 2.02 · 2.03(ORC-005 · RAIL-002) · 3.02 · 3.03 · 3.04 · 3.05 ADR-014 · 4.01 M1 · 4.02 · 4.03 Q-3 · Q-13 · 용어집에서 사람 상태 락 · 선점 · claim을 '착수 = 미병합 task/<ID> 브랜치'로 바꾸고, backlog.md 1.51.0 화면 제한을 3.03 §4 주의점과 4.02 실측 사실에 적는다
- [x] #3 A3 · A4: 3.03 §1 · 3.04에 오케스트레이터 커밋이 지우는 환경변수 3개를 적고, 2.03 ORC-021 · 3.04 · 3.05 ADR-021 · 4.03 Q-18 · Q-20에 토큰 출처를 '당분간 session(ClaudeCodeRunner), commits는 Q-18 이후'로 적는다. 커밋 단위 측정 서술(G-4 · P7 · NFR-004 등)에 같은 단서를 단다
- [x] #4 A5: 2.02 · 2.03 RAIL-023 · 3.03 · 3.04 · 3.05 ADR-023 · 용어집에서 작업 순서 파일 검사 시점을 브랜치 생성으로 옮기고, ORC-005 배정 조건을 isReady ∧ To Do ∧ task/<ID> 브랜치 없음(work-order.md는 읽지 않음)으로 적는다
- [x] #5 A6: 2.02 · 2.03 RAIL-022 · 3.04 · 3.05 ADR-023 · 4.02 · 용어집에 DoD 항목 끝 `(수동)` 표시는 #D 표식 요구에서 빠진다는 예외를 적는다
- [x] #6 C2: 2.03에 RAIL-025(task/<ID> 브랜치에서 메시지에 그 ID가 단어 경계로 없는 커밋 거부)를 신설하고 3.03 · 3.04 · 3.05 ADR-023 · 4.02 수용 기준에 반영한다
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 옛 표현 grep 0건(In Progress 시점 승인 게이트, 사람 선점, 상태 값 자체가 락, claim) (수동)
- [x] #2 design/ 상대 링크 깨짐 0건 (수동)
- [x] #3 파일 하나에 커밋 하나, 각 커밋에 TASK ID, push하지 않는다 (수동)
- [x] #4 요구사항 ID 재사용 · 재번호 없음, 폐기 · 소관 이전은 표시로만 (수동)
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
### Subjective
유저는 2026-10-29에 충돌 A1~A6 · C2를 결정했고(A1은 A2 결과로 재결정), 요약을 확인한 뒤 반영 계획을 승인했다. 결정은 설계 문서에 먼저 반영하고(00 편집 규칙: 명세 먼저) 컴포넌트에 전파한다.

### Objective
- 2026-10-29 조사: 승인 게이트를 `-s "In Progress"`에 두는 서술이 2.02 · 2.03 · 3.03 · 3.04 · 3.05 · 용어집에, 사람 상태 락 · claim 서술이 1.03 · 1.04 · 2.01 · 2.02 · 2.03 · 3.02 · 3.03 · 3.04 · 3.05 · 4.01 · 4.02 · 4.03 · 용어집에 있다.
- 실측(backlog 1.51.0, 임시 저장소): task 브랜치에서 In Progress로 바꾸고 커밋해도 main의 list · view · overview · search · browser API는 To Do를 보인다. 원격 브랜치만 있어도 같다.
- 오케스트레이터 커밋 환경 제거 목록(BacklogCardSource.STRIPPED_ENV)은 AI_AGENT · CLAUDE_CODE_SESSION_ID 둘이고, GF-130은 판정을 SESSION_ID · CLAUDE_PID로 바꾼다.
- RAIL은 024까지 있다(다음 번호 RAIL-025).

### Assessment
승인 게이트와 착수 판단이 같은 시점(브랜치)이어야 '승인 없이 브랜치만 만든 착수'가 생기지 않는다. 오케스트레이터는 훅을 모른다는 원칙(A1)을 지키려면 배정 조건에 훅 산출물(work-order.md)을 넣지 않는다. 토큰은 Q-18이 미정이라 확정 가능한 session만 먼저 쓴다. 테스트 불가 DoD는 가짜 테스트 대신 카드에 드러나는 `(수동)` 예외로 리뷰 대상에 둔다.

### Plan
1. 승격 직후 decision-3(decision-2의 착수 시점 부분 대체: A1 · A2 · A5) 작성 · 연결.
2. AC #1~#6을 장 단위로: 2.02 → 2.03 → 3.05 → 3.03 → 3.04 → 1.x · 2.01 · 3.02 → 4.0x → 용어집, 파일마다 커밋.
3. grep · 링크 검사.
4. 컴포넌트 전파(AO-29 · AO-30, hooks 카드)의 Refs 커밋 또는 Propagation-None을 확인한 뒤 Done.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
AC 반영 커밋(task/task-19, push 없음, 파일당 1커밋): 2bca0d8 2.02 · 1067ad1 2.03 · dcee67d 3.05 · 82c7da7 3.03 · a03383e 3.04 · ddc1793 1.02 · e9ce059 1.03 · c399ba5 1.04 · 359925d 2.01 · 77d95e8 2.04 · 8cb93e1 3.02 · fddbd91 4.01 · e8de9da 4.02 · 909ede1 4.03 · d24a625 부록 용어집.
- AC #1(A1): 2.02 승인 게이트 · 전이와 커밋 표 5단계(브랜치 생성 = 착수, 게이트) · 6단계(-s In Progress = 시작 기록), 2.03 RAIL-020 · BL-017, 3.03 §2 · §4, 3.04 §1 · §3 · §7 humanSigners, 3.05 ADR-022(decision-3 언급), 용어집 승인 게이트.
- AC #2(A2): 1.03 G-5 · L24 · L62, 1.04 R-6, 2.01, 2.02 착수 정의 · 파생 속성, 2.03 ORC-005 · RAIL-002 · 원천, 3.02 §3, 3.03 §1 주의점 · §4 주의점(backlog 1.51.0 화면 제한), 3.04 §1 · §3 착수 판정, 3.05 ADR-014(변경 기록), 4.01 M1 조건 2, 4.02 실측 사실, 4.03 Q-3 · Q-13, 용어집 착수 · 착수 태스크 배정 제외.
- AC #3(A3 · A4): 3.03 §1 주의점(AI_AGENT · CLAUDE_CODE_SESSION_ID · CLAUDE_PID) · §3 L112(GF-130), 3.04 §1 완료 기록 · §2 · §6, 2.03 ORC-021, 3.05 ADR-021 예외 · ADR-012, 4.03 Q-18 · Q-20 정해진 부분, 4.01 GF-130, 단서: 1.02 P7 · 1.03 G-4 · 1.04 · 2.02 L107 · 2.04 NFR-004 · 3.02 §7 · 4.02 토큰 실측.
- AC #4(A5): 2.02 · 2.03 RAIL-023 · ORC-005 · 3.03 §1 · §4 · 3.04 §3 · 3.05 ADR-023 결과 · 3.02 · 용어집 작업 순서 파일.
- AC #5(A6): 2.02 테스트 표식 · 테스트 파일 구조, 2.03 RAIL-022, 3.04 §1 DoD · §3 완료, 3.05 ADR-023, 4.02 테스트 추적, 용어집 (수동) DoD.
- AC #6(C2): 2.03 RAIL-025 신설(RAIL-024 다음), 3.03 §2 요구사항 범위 RAIL-019 ~ RAIL-025, 3.04 §2 · §3, 3.05 ADR-023(목록 관련 · 결정 · 결과), 4.02 테스트 추적 '커밋 → 카드' 행, 2.02 전이와 커밋.
DoD 증거:
- #1 grep(선점 · 상태 값 자체가 락 · claim · 상태 락 · 파일 락 · In Progress 때 승인 게이트) design/ · README: 남은 것은 변경 이력 서술 2건뿐(3.05 ADR-014 '변경', 2.02 원천 '상태 값 락은 decision-3이 대체').
- #2 design/ 상대 링크 34개 검사, 깨짐 0(00 편집 규칙의 '../diagrams/<이름>.svg' 표기 예시 1건은 기존 자리표시자).
- #3 파일 하나에 커밋 하나, 모든 커밋 제목에 TASK-19, push 없음.
- #4 2.03 ID 중복 0, 새 ID는 RAIL-025뿐, 재번호 없음.
<!-- SECTION:NOTES:END -->
