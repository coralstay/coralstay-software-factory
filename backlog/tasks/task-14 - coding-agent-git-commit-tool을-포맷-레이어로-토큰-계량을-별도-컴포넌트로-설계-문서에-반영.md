---
id: TASK-14
title: 'coding-agent-git-commit-tool을 포맷 레이어로, 토큰 계량을 별도 컴포넌트로 설계 문서에 반영'
status: To Do
assignee: []
created_date: '2026-10-12 09:36'
updated_date: '2026-10-12 09:43'
labels:
  - design
dependencies: []
documentation:
  - README.md
  - 'https://github.com/coralstay/coding-agent-git-commit-tool'
  - >-
    components/coding-agent-git-commit-tool/backlog/tasks/gf-146 -
    토큰·툴콜-측정을-걷어내고-커밋-포맷-전용으로-축소한다.md
priority: high
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
유저 결정(2026-10-12): coding-agent-git-commit-tool은 깃 커밋 포맷만 맞춘다. 토큰 계량을 커밋 훅에 두면 깃과 측정이 강결합되므로, 계량은 별도 컴포넌트(이름 미정)로 뺀다. 최상위 README 컴포넌트 표는 이미 고쳤다(9d6980f, 브랜치 docs/commit-tool-format-only). 설계 문서(design/)는 아직 이 도구를 '계측 레이어'이자 토큰 계량 담당으로 적고 있어 README와 어긋난다.

영향받는 곳(2026-10-12 grep):
- 3.01 시스템 구성: 컴포넌트 표의 '계측' 역할, 연결 설명
- 3.03 §3 컴포넌트 명세, 3.04 인터페이스 계약: 커밋 모양 예시, 트레일러 표의 Tokens-Used · Tool-Calls, 측정 실패 규칙
- 2.01 운영 환경('규율 · 계측'), 2.03 TRL 요구사항
- 1.01 · 1.02(P7 근거, 토큰 측정 방식 출처) · 1.03(G-4) · 1.04(R-8, G-4)
- 4.03 미결 Q-18 · Q-20
- 부록 용어집(컴포넌트 · 트레일러 · 토큰 계량 항목), diagrams/07-task-sequence.mmd

컴포넌트 쪽 대응: coding-agent-git-commit-tool DRAFT-24(측정 로직 삭제와 그 저장소 문서 정리). DRAFT-2의 전파 규칙과 같은 방향의 변경이다.

범위 밖: 새 토큰 계량 컴포넌트의 이름 · 저장소 · 측정 방식 설계. 이 draft에서는 '별도 컴포넌트(이름 미정)'로만 적는다.

## 비즈니스 규칙
- B1 (AC #1) coding-agent-git-commit-tool의 역할은 '포맷'이다. design/ 어디에도 이 도구가 토큰을 계량한다고 적지 않는다
- B2 (AC #2) 토큰 계량은 '토큰 계량 컴포넌트(이름 미정)'가 맡는다고 적고, 측정 방식은 미정으로 둔다
- B3 (AC #3) 요구사항 ID는 지우지 않는다. 옮기거나 폐기 표시만 한다
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 3.01 · 3.03 §3 · 3.04 · 2.01 · 부록 용어집에서 coding-agent-git-commit-tool의 역할을 포맷 레이어로 고치고, 트레일러 예시 · 표에서 Tokens-Used · Tool-Calls를 뺀다(B1)
- [ ] #2 3.01 컴포넌트 표와 용어집에 토큰 계량 컴포넌트(이름 미정)를 추가하고, 1.0x · 3.04 완료 기록 · 07-task-sequence.mmd의 토큰 출처를 그 컴포넌트로 바꾼다(B2)
- [ ] #3 2.03 TRL 요구사항 중 토큰 관련 항목을 폐기 또는 새 컴포넌트 소관으로 표시하고, 4.03 Q-18 · Q-20을 새 컴포넌트 기준으로 고친다(B3)
- [ ] #4 3.05에 '커밋 포맷과 토큰 계량 분리' ADR을 추가하고 강결합을 이유로 적는다
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 grep -rnE 'Tokens-Used|Tool-Calls|계측 레이어' design 결과에 coding-agent-git-commit-tool 소관으로 적힌 곳이 없다
- [ ] #2 build-diagrams.py 재렌더 · design/ 상대 링크 검사가 통과한다
- [ ] #3 coding-agent-git-commit-tool DRAFT-24와 같은 날 반영해 두 저장소 문서가 어긋난 채 남지 않는다
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
### Subjective
유저는 coding-agent-git-commit-tool이 포맷만 맞추고 토큰 측정은 별도 컴포넌트로 빼라고 했고, design 문서도 맞추라고 했다(2026-10-12).

### Objective
- README 컴포넌트 표는 고쳤다(9d6980f).
- design/ 11개 파일 18곳이 이 도구를 계측 · 토큰 계량 담당으로 적는다(위 목록).
- 컴포넌트 저장소는 DRAFT-24로 측정 로직을 걷어낸다.

### Assessment
설계 문서는 역할 정의(3.01 · 용어집)를 먼저 고치고, 그걸 근거로 인터페이스(3.04) · 요구사항(2.03) · 목표 · 리스크(1장) · 미결(4.03) 순으로 내린다. 새 컴포넌트는 이름이 없으므로 자리만 만든다.

### Plan
1. 3.05에 ADR을 추가한다. 커밋.
2. 3.01 · 용어집에서 역할을 고친다. 커밋.
3. 3.03 §3 · 3.04 트레일러를 고친다. 커밋.
4. 2.01 · 2.03을 고친다. 커밋.
5. 1장 · 4.03 · 07-task-sequence.mmd를 고치고 재렌더한다. 커밋.
6. 링크 검사를 돌린다.
<!-- SECTION:PLAN:END -->
