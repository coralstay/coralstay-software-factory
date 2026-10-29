---
id: decision-3
title: >-
  decision-2의 착수 시점 대체: 착수는 미병합 task/<ID> 브랜치의 존재이고, 착수 검사(계획 승인 게이트 · 계획/AC/DoD
  형식 · 작업 순서)는 훅이 그 브랜치 생성 · 전환 때와 -s "In Progress" 때 두 번 한다(In Progress 전환은 시작 기록이자
  검사 지점). 오케스트레이터 배정 조건은 isReady ∧ To Do ∧ 브랜치 없음
date: '2026-10-29 02:34'
status: accepted
---
## Context

decision-2(2026-10-22)는 계획 승인을 사람 키로 서명한 빈 커밋 `Plan-Approved: <ID>`로 기록하고, 승인 게이트를 `backlog task edit <ID> -s "In Progress"` 때 돌렸다. 그때는 `In Progress` 상태 값이 착수이자 사람과 에이전트 사이의 락이었다.

2026-10-22 작업(claude-code-agile-hooks TASK-58 ~ TASK-66, 최상위 TASK-14 ~ TASK-18, agent-orchestrator AO-27 · AO-28)에서 이 전제가 깨졌다.

- 상태 전환 커밋은 `task/<ID>` 브랜치에 들어간다(RAIL-002). 그래서 main을 읽는 쪽(오케스트레이터 · 사람의 보드)에는 착수한 카드가 계속 `To Do`로 보여 상태 값이 락이 되지 못한다.
- 실측(backlog.md 1.51.0, 2026-10-29, 임시 저장소): task 브랜치에서 `In Progress`로 바꾸고 커밋해도 main의 `task list` · `task view` · `overview` · `search`와 `backlog browser`(웹 API)는 `To Do`를 보인다. 로컬 브랜치만 있을 때도 원격 브랜치만 있을 때도 같다. 브랜치 스캔(`check_active_branches`)은 ID 발번에만 쓰인다.
- 사람이든 에이전트든 작업을 시작하면 `task/<ID>` 브랜치를 먼저 만들고 상태는 나중에 옮긴다. `-s "In Progress"`에만 게이트를 두면 게이트 전에 착수가 생긴다.

유저 결정(2026-10-29, TASK-19):

- A1 — 계획 승인 검사(Plan-Approved + humanSigners)는 `task/<ID>` 브랜치 생성 · 전환 시점에 한다. claude-code-agile-hooks에만 두고 훅이 설치된 곳에서만 적용한다. `-s "In Progress"`는 계속 하지만 판단 기준이 아니라 기록이다.
- A2 — 착수 = main에 병합되지 않은 `task/<ID>` 브랜치가 있다. main에 claim 커밋을 만들지 않는다.
- A5 — 작업 순서 파일 검사(RAIL-023)도 브랜치 생성 시점에 훅이 한다. 오케스트레이터 배정 조건(ORC-005)은 isReady ∧ To Do ∧ `task/<ID>` 브랜치 없음이고, 오케스트레이터는 `backlog/work-order.md`를 읽지 않는다.

실행 중(TASK-19, 2026-10-29) 빈틈이 드러났다. 오케스트레이터는 `task/<ID>` 브랜치를 자기 Java 프로세스에서 `git worktree add`로 직접 만든다(agent-orchestrator `WorktreeManager`). 이 명령은 Claude Code 세션의 Bash 도구를 거치지 않으므로 훅이 보지 못한다. 브랜치 시점에만 검사하면 에이전트가 실행하는 태스크는 승인 게이트를 건너뛴다. 유저가 A1을 보완했다(2026-10-29): 착수 검사를 두 시점 모두에 둔다.

## Decision

1. 착수는 main에 병합되지 않은 `task/<ID>` 브랜치(로컬 · 원격 어느 쪽이든)가 있는 상태다. 병합 여부는 `git cherry` 기준으로 판정한다(`git branch --no-merged`는 패치가 이미 들어간 브랜치도 잡는다). main에 착수 기록 커밋을 만들지 않는다. 브랜치가 병합되거나 지워지면 착수가 풀린다.
2. 착수 검사는 세 가지다 — 작성된 구현 계획(SOAP) · AC · DoD 형식(RAIL-020), 계획 승인 게이트(유효한 서명 `%G?` = `G`이고 서명자 `%GS`가 `humanSigners`에 있는 `Plan-Approved: <ID>`, RAIL-020 · BL-017), 최신 작업 순서 파일(RAIL-023).
3. 훅은 착수 검사를 두 시점에 같은 내용으로 한다.
   - ① `task/<ID>` 브랜치를 만들거나 그 브랜치로 전환할 때(`git switch -c` · `checkout -b` · `switch` · `checkout` · `worktree add`, 사람이나 Claude 세션이 실행한 명령).
   - ② `backlog task edit <ID> -s "In Progress"` 때. 오케스트레이터가 만든 브랜치에서는 그 워크트리 안의 에이전트 세션이 이 전환을 하므로, 여기가 에이전트 태스크의 검사 지점이다.
4. `-s "In Progress"`는 착수 판단이 아니라 실제 시작 시각을 카드에 남기는 기록이고, 동시에 검사 지점이다.
5. 착수 검사는 claude-code-agile-hooks에만 둔다. 훅이 설치된 곳에서만 적용되고, 사람이 훅 없이 터미널에서 만든 브랜치는 검사하지 않는다.
6. 오케스트레이터는 훅을 모른다. 배정 조건(ORC-005)은 `isReady` ∧ `status = To Do` ∧ 미병합 `task/<ID>` 브랜치 없음이고, `backlog/work-order.md`는 읽지 않는다(의존 순서는 `isReady`가 보장한다). 에이전트 세션의 `In Progress` 전환이 거부되면 오케스트레이터는 사유를 해석하지 않고 일반 '착수 안 됨' 실패로 거둔다.
7. 알려진 제한: backlog.md 1.51.0의 화면(`task list` · `view` · `overview` · `search` · `backlog browser`)은 main에서 착수한 카드를 `To Do`로 보인다. 사람은 `git branch -a --list '*task/*'`와 병합 여부로 착수를 확인한다.

## Consequences

- 사람과 에이전트의 충돌은 브랜치 존재로 막힌다. 별도 락 파일 · claim 커밋 · 사람 담당 표시가 필요 없고, main에 오케스트레이터 커밋이 생기지 않아 병합 방식(merge commit) 제약이 사라진다(agent-orchestrator decision-14). 단 병합 뒤 `task/<ID>` 브랜치를 지우는 것이 규칙이다(유저 결정 2026-10-29, 3.03 §1 주의점).
- squash 병합은 패치 ID가 달라 `git cherry`가 미병합으로 본다. 판정은 `git cherry`로 두므로, squash 병합하고 지우지 않은 브랜치는 지울 때까지 착수로 보여 배정을 막는다.
- 사람과 Claude 세션의 착수는 브랜치 시점에서 걸러지고, 오케스트레이터 태스크는 `In Progress` 전환에서 걸러진다. 어느 경로든 훅이 있으면 승인 없이 작업이 시작되지 않는다.
- 오케스트레이터 태스크는 브랜치가 먼저 생기고 검사가 뒤에 오므로, 거부된 경우 승인 없는 미병합 브랜치가 남아 착수로 보인다. 그 카드는 브랜치가 남아 있는 동안 다시 배정되지 않고 사람이 판단한다.
- 같은 검사를 두 시점에서 하므로 훅 구현이 검사 로직을 공유해야 한다. 현재 구현(claude-code-agile-hooks TASK-58 · TASK-60)은 `-s "In Progress"`에서만 검사하고, 브랜치 생성 · 전환 시점 검사는 아직 구현 전이다.
- 훅 없이 만든 브랜치와 훅 없이 한 상태 전환은 검사되지 않는다. 이는 훅이 opt-in인 한 남는 한계다.
- main의 backlog.md 보드는 착수를 보이지 않는다. 보드 대신 브랜치 목록을 확인해야 하고, 이 불편은 backlog.md가 브랜치의 상태를 보이게 될 때까지 남는다.
- decision-2의 승인 기록 형식(서명 빈 커밋 · `humanSigners` · 두 키 구성)은 그대로이고, 게이트 시점만 이 결정이 대체한다. 설계 문서 반영: 2.02 · 2.03(RAIL-020 · RAIL-023 · BL-017 · ORC-005) · 3.03 · 3.04 · 3.05 ADR-014 · ADR-022 · ADR-023 · 부록 용어집.
