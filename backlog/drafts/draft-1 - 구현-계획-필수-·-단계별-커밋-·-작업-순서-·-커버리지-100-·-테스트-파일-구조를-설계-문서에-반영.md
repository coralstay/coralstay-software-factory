---
id: DRAFT-1
title: 구현 계획 필수 · 단계별 커밋 · 작업 순서 · 커버리지 100% · 테스트 파일 구조를 설계 문서에 반영
status: Draft
assignee: []
created_date: '2026-10-12 02:29'
updated_date: '2026-10-12 05:45'
labels:
  - design
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
유저 요청(2026-10-12)으로 claude-code-agile-hooks에 draft 5장(DRAFT-8 구현 계획 필수, DRAFT-9 단계별 커밋, DRAFT-10 커버리지 100% + 리포트, DRAFT-11 테스트 파일 구조, DRAFT-12 승격마다 작업 순서 파일)을 등록했다. 이 draft는 그 결과를 design/에 반영하는 후속 작업이다(TASK-12 · TASK-13 방식). 문구는 구현 결과에 맞춰야 하므로 DRAFT-8 ~ DRAFT-12가 끝난 뒤에 진행한다. push는 범위 밖이다(유저 결정 2026-10-12).

유저 결정(2026-10-12):
- Plan-Review-Go: 태스크가 In Progress로 가기 전에 구현 계획이 작성되고, 사람이 리뷰하고, 승인(go)해야 한다. 그 뒤에만 In Progress로 옮길 수 있다.
- 구현 계획은 SOAP + AC + DoD 형식을 쓴다. 계획에는 S(Subjective: 요청 · 배경), O(Objective: 확인한 사실 · 코드 · 측정), A(Assessment: 판단 · 선택한 접근), P(Plan: 구현 순서) 절이 있고, 카드에는 AC와 DoD가 있어야 한다.
- RGR: 모든 태스크는 AC마다 Red → Green → Refactor로 구현한다.
- PRG: API 예외 처리는 항상 Post/Redirect/Get 패턴을 쓴다. 강제 방법은 미정이다.

DRAFT-8은 이 결정에 따라 범위가 넓어졌다. 계획 존재 여부만이 아니라 SOAP 절 · AC · DoD가 있는지, Plan-Review-Go 승인(go)이 기록됐는지도 훅으로 검사한다(go 기록 방식은 DRAFT-8 착수 시 결정).

새 ID: BL-015 ~ BL-017, RAIL-020 ~ RAIL-023, NFR-017 · NFR-018, ADR-021 ~ ADR-023(현재 마지막 번호: BL-014 · RAIL-019 · NFR-016 · ADR-020).
components/claude-code-agile-hooks/design/은 아직 골격뿐이라 대상에서 뺀다. 계획: ~/.claude/plans/sunny-enchanting-conway.md
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 구현 계획 필수: 2.02 태스크 카드 구성 표의 구현 계획 행(승격 전 필수)과 상태와 전이 표의 조건, 2.03 BL 표에 BL-015, RAIL 표에 RAIL-020을 넣는다
- [ ] #2 단계별 커밋: 2.02 상태와 전이 아래 새 소절 '전이와 커밋', 2.03에 RAIL-021과 RAIL-002 · RAIL-008 갱신, 3.04 §3 상태 전이 표, 3.03 §4 backlog.md 사용 규약 표에 반영한다
- [ ] #3 커버리지 100%: 2.04에 NFR-017, 2.03 RAIL-006 갱신, 3.04 §7 coverageCommand 행과 언어별 리포트 위치 표에 반영한다
- [ ] #4 테스트 파일 구조: 2.02 테스트 표식 표에 DoD 행 <카드 ID>#D<n>과 새 소절 '테스트 파일 구조', 2.03에 RAIL-022, 4.02 테스트 추적 표에 반영한다
- [ ] #5 작업 순서 파일: 2.02 상태와 전이에 승격 직후 의존 정리, 2.03에 BL-016 · RAIL-023, 3.03 §4 backlog.md 사용 규약 표에 --dep · task list --ready 행, 3.04 §3 상태 전이 표에 반영한다
- [ ] #6 Plan-Review-Go + SOAP: 2.02 태스크 카드 구성 표의 구현 계획 행(SOAP 노트 형식 + AC + DoD, 승격 전 작성, 착수 전 사람 리뷰 · go)과 새 소절 '구현 계획 형식' — 예약 제목 ### Subjective · ### Objective · ### Assessment · ### Plan(키워드처럼 고정, 이 순서, 철자 그대로)과 '작성됨' 판정 규칙(제목 있음 · 순서 · 중복 없음 · 본문 비어 있지 않음), 상태와 전이 표의 To Do → In Progress 조건, 2.03 BL 표에 BL-017(Plan-Review-Go)과 SOAP 예약 제목 규칙, 3.04 §1 태스크 카드 계약 · §3 상태 전이 표의 착수 행, 부록 용어집에 SOAP를 반영한다
- [ ] #7 RGR: 3.05 ADR-020의 결정 문구를 Red → Green → Refactor로 명시하고, 2.03 RAIL-011과 4.02 테스트 추적에 반영한다
- [ ] #8 PRG: API 예외 처리는 항상 Post/Redirect/Get 패턴을 쓴다는 규칙을 3.04 인터페이스 계약의 새 절(대상 프로젝트의 API 예외 처리 규약), 2.04 NFR 표에 NFR-018, 3.05에 새 ADR-023으로 넣는다(강제 방법은 미정으로 적는다)
- [ ] #9 공통: 3.03 §2의 구현 요구사항 칸과 세 가지 성격 표, 3.05 결정 목록에 ADR-021 ~ ADR-023을 추가하고, design/ 상대 링크 검사에서 깨진 링크가 없다
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. DRAFT-8 ~ DRAFT-12의 final summary와 decision을 읽고 확정된 문구 · 키 이름(SOAP 헤딩 이름, go 기록 방식 포함)을 모은다.
2. 2 요구사항(2.02 → 2.03 → 2.04) → 3 아키텍처(3.03 → 3.04 → 3.05) → 4.02 순서로, 파일 하나에 커밋 하나씩 반영한다.
   - 2.02: 구현 계획 행(SOAP + AC + DoD, Plan-Review-Go), 상태와 전이 조건, 전이와 커밋 · 테스트 파일 구조 소절
   - 2.03: BL-015 ~ BL-017, RAIL-020 ~ RAIL-023, RAIL-002 · RAIL-006 · RAIL-008 · RAIL-011 갱신
   - 2.04: NFR-017(커버리지 100%), NFR-018(PRG)
   - 3.03: §2 구현 요구사항 칸 · 세 가지 성격 표, §4 backlog.md 사용 규약 표
   - 3.04: §3 상태 전이 표(착수 행 포함), §7 coverageCommand, 새 절 대상 프로젝트의 API 예외 처리 규약(PRG)
   - 3.05: ADR-020 문구를 RGR로 명시, ADR-021 ~ ADR-023 추가
   - 4.02: 테스트 추적 표(DoD 표식, RGR)
3. design/ 상대 링크 검사를 돌리고, 다이어그램이 바뀌면 build-diagrams.py로 다시 렌더한다.
<!-- SECTION:PLAN:END -->
