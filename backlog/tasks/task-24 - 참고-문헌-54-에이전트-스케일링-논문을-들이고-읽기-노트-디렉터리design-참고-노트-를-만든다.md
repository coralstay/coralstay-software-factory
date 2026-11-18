---
id: TASK-24
title: 참고 문헌 [54] 에이전트 스케일링 논문을 들이고 읽기 노트 디렉터리(design/참고-노트/)를 만든다
status: To Do
assignee: []
created_date: '2026-11-18T00:17:00Z'
updated_date: '2026-11-18T00:43:00Z'
labels:
  - design
  - references
dependencies: []
documentation:
  - /Users/flynn_macpro/.claude/plans/factory-ref-54-scaling-agents.md
  - https://arxiv.org/abs/2512.08296
  - design/부록-참고-문헌.md
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
## 배경
유저(2026-11-18): MIT 김유빈님의 에이전트 스케일링 논문을 레퍼런스로 들일 때가 됐다. 레퍼런스 디렉터리를 agent-orchestrator 쪽에, 아니면 적절한 위치에.
위치 판단: design/부록-참고-문헌.md 가 이 설계의 참고 문헌 SSOT(인용 원칙 6개, [1]~[53], 관련 연구 표)이고 agent-orchestrator 부록은 그걸 이어받는 하위 문서다. 논문이 닿는 곳도 팩토리 설계(G-6 Allocation Policy, R-6 병렬 충돌, 1.01 '얼마나', 4역할 구조)라 팩토리 최상위에 둔다.
계획: ~/.claude/plans/factory-ref-54-scaling-agents.md (승인됨)

## 문헌
Towards a Science of Scaling Agent Systems — Yubin Kim 외(Google Research · Google DeepMind · MIT), arXiv 2512.08296, v1 2025-12-09 · v3 2026-04-08, cs.AI, arXiv 기본 비독점 라이선스.

## 범위
- design/참고-노트/README.md(목적·파일 이름·노트 형식·저작권 원칙), design/참고-노트/54-2512.08296.md(v3 읽기 노트)
- design/부록-참고-문헌.md: [54] 추가, 관련 연구 표 한 행, 닿는 범위 명시
- R-6 · G-6 본문에 [54] 각주(범위 포함)
- agent-orchestrator design/부록-참고-문헌.md 에 이어받음 한 줄

## 비즈니스 규칙
- B1 (AC #1) 원문 PDF·긴 인용을 저장소에 넣지 않는다. 한 문장 이내 인용만 따옴표와 출처 절
- B2 (AC #2) 수치마다 버전(v1·v2·v3)을 밝힌다
- B3 (AC #3) 인용 원칙 3·4: 재는 것(과제 성능)과 닿는 범위를 적고 G-1(판정 독립성) 근거로 쓰지 않는다
- B4 (AC #2) 번호는 [54]로 새로 붙이고 기존 번호를 바꾸지 않는다

## 하지 않는 것
다른 문헌 추가, 부록 나머지 정리, 카드에 '병렬 가능성' 속성 도입
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 design/참고-노트/README.md 가 목적·파일 이름 규칙(<번호>-<arXiv ID 또는 짧은 이름>.md)·노트 형식·저작권 원칙(원문 PDF·긴 인용 금지)을 담는다(B1)
- [ ] #2 부록 목록에 [54] 가 추가되고 노트 54-2512.08296.md 가 서지 전체·v3 기준 요약·버전별 수치를 담는다(B2·B4)
- [ ] #3 노트와 관련 연구 표 행이 재는 것(과제 성능)과 닿는 범위를 적고 G-6·R-6·1.01 '얼마나'에 연결하며 G-1 근거로 쓰지 않는다고 밝힌다(B3)
- [ ] #4 R-6·G-6 본문에 [54] 각주가 범위와 함께 붙는다
- [ ] #5 agent-orchestrator design/부록-참고-문헌.md 에 최상위 [54] 이어받음과 AO-33·SessionRegistry 연결 한 줄이 있고, 두 저장소 source-header lint --strict 가 0 이다
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 v3 원문(HTML 판)을 직접 읽고 노트의 요약 문장마다 출처 절을 표기했다
- [ ] #2 build-diagrams.py 로 다이어그램을 다시 만들어도 변경이 없다
- [ ] #3 팩토리·agent-orchestrator 각각 PR 이 있다
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
### Subjective
유저(2026-11-18)가 MIT 김유빈님의 에이전트 스케일링 논문을 레퍼런스로 들이고 레퍼런스 디렉터리를 만들자고 했다. agent-orchestrator 쪽, 아니면 적절한 위치. 계획: ~/.claude/plans/factory-ref-54-scaling-agents.md

### Objective
- 논문: Towards a Science of Scaling Agent Systems, arXiv 2512.08296(v3 2026-04-08), arXiv 기본 비독점 라이선스. v3 초록: 단일 1종·다중 4종 구조, 260 구성·6 벤치마크, +80.8%~−70.0%, 단일 기준선이 높으면 조율 이득 감소, 교차검증 R²=0.373. v2 에는 독립형 오류 증폭 17.2× 대 중앙형 4.4×.
- design/부록-참고-문헌.md 가 참고 문헌 SSOT(인용 원칙 6개, [1]~[53], 관련 연구 표). agent-orchestrator 부록은 이어받는 하위 문서.
- 연결 지점: 03-목표와-범위 G-6(Allocation Policy), 04-기대-효과와-리스크 R-6('에이전트 적용은 미검증'), 01-배경과-문제 '얼마나'.
- 인용 원칙 3·4: 재는 것이 다르면 인용하지 않고, 근거로 쓸 때는 닿는 범위를 적는다.

### Assessment
팩토리 최상위 부록에 [54] 로 들이고 읽기 노트는 design/참고-노트/ 에 둔다. 과제 성능 연구라 G-1(판정 독립성) 근거로는 쓰지 않고 에이전트 수·구조 선택(G-6·R-6·'얼마나')에만 범위를 붙여 쓴다. 원문은 저장소에 넣지 않는다.

### Plan
1. v3 HTML 원문을 읽는다.
2. design/참고-노트/README.md, 54-2512.08296.md 작성.
3. 부록에 [54]·관련 연구 행, R-6·G-6 각주.
4. agent-orchestrator 부록 한 줄(그 저장소 브랜치에서 커밋).
5. lint·다이어그램 확인, 커밋, PR 두 개.
<!-- SECTION:PLAN:END -->
