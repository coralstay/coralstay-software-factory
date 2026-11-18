---
id: DRAFT-1
title: 참고 문헌 [54] 에이전트 스케일링 논문을 들이고 읽기 노트 디렉터리(design/참고-노트/)를 만든다
status: Draft
assignee: []
created_date: '2026-11-18T00:17:00Z'
labels:
  - design
  - references
dependencies: []
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
