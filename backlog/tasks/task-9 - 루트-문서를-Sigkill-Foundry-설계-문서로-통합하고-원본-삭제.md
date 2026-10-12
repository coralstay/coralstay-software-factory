---
id: TASK-9
title: 루트 문서를 Sigkill Foundry 설계 문서로 통합하고 원본 삭제
status: Done
assignee: []
created_date: '2026-10-05 11:47'
updated_date: '2026-10-10 22:26'
labels:
  - docs
dependencies: []
documentation:
  - /Users/flynn_macpro/.claude/plans/typed-chasing-conway.md
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
루트의 RFC(에이전트_레일_파이프라인.html·pdf)·아키텍처.md·컴포넌트-현황.md·README 본문을 design/(Sigkill Foundry, Claude 앱 문서가 편집 원본) 장으로 옮기고 원본 파일은 삭제한다. 원본을 design/ 하나로 만든다. 계획(매핑표 포함): ~/.claude/plans/typed-chasing-conway.md

수용 기준(승격 시 AC로 등록):
1. 매핑표의 원천 절이 모두 대상 장(1.01~4.03, 부록)에 옮겨진다 — 진척·경위 서술 없이, 장 형식·요구사항 ID·추적 규칙 준수
2. diagrams/를 design/diagrams/로 옮기고 build-diagrams.py가 장에서 쓸 독립 SVG(라이트/다크 대응)를 만든다
3. RFC HTML·PDF, 아키텍처.md, 컴포넌트-현황.md, build-pdf.sh를 삭제한다
4. README는 소개 + design/ 진입점 + 컴포넌트 저장소 표 + 라이선스 + English Summary로 줄이고, 편집 규칙은 0 문서 정보로 옮긴다
5. Claude 앱 문서(편집 원본)를 먼저 반영하고 저장소 사본과 일치시킨다, 목차 상태 갱신
6. 삭제 파일을 가리키는 링크 0건(다른 컴포넌트 저장소 포함), design/ 상대 링크·이미지 전부 유효
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 매핑표의 원천 절이 모두 대상 장(1.01~4.03, 부록)에 옮겨진다 — 진척·경위 서술 없이, 장 형식·요구사항 ID·추적 규칙 준수
- [x] #2 diagrams/를 design/diagrams/로 옮기고 build-diagrams.py가 장에서 쓸 독립 SVG(라이트/다크 대응)를 만든다
- [x] #3 RFC HTML·PDF, 아키텍처.md, 컴포넌트-현황.md, build-pdf.sh를 삭제한다
- [x] #4 README는 소개 + design/ 진입점 + 컴포넌트 저장소 표 + 라이선스 + English Summary로 줄이고, 편집 규칙은 0 문서 정보로 옮긴다
- [x] #5 Claude 앱 문서(편집 원본)를 먼저 반영하고 저장소 사본과 일치시킨다, 목차 상태 갱신
- [x] #6 삭제 파일을 가리키는 링크 0건(다른 컴포넌트 저장소 포함), design/ 상대 링크·이미지 전부 유효
<!-- AC:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
루트의 설계 문서(RFC 에이전트_레일_파이프라인.html·pdf, 아키텍처.md, 컴포넌트-현황.md, README 본문)를 Sigkill Foundry 장(design/)으로 옮기고 원본을 삭제했다. 원본은 design/(편집 원본은 Claude 앱 문서) 하나다.
- 1.01~1.04 · 2.01~2.04 · 3.01~3.05 · 4.01~4.03 · 부록 2개를 매핑표대로 채웠다(서브에이전트 3개 분담 후 번호 정리: 목표 G-1~G-7, 요구사항 ORC/RAIL/TRL/BL/NFR 전부에 G 연결, 미결 Q-1~Q-20으로 통합, ADR-001~019).
- langtoolchain은 범위 밖으로 통일(3.02 부트스트랩 6단계와 다이어그램 노드 삭제, 근거 68b7ee1).
- 다이어그램을 design/diagrams/로 옮기고 design/build-diagrams.py가 라이트/다크 대응 독립 SVG 9개를 만든다. build-pdf.sh와 PDF는 삭제.
- README는 소개 + design/ 진입점 + 컴포넌트 저장소 표 + 라이선스(AGPL 원문 링크 포함) + English Summary로 줄였고, 편집 규칙은 0 문서 정보로 옮겼다.
- 2.03에 RAIL-015~018 추가(claude-code-agile-hooks 분류에서 드러난 요구사항, 최상위 번호 체계).
- Claude 앱 문서 19개를 저장소 사본과 일치시키고(다이어그램 9개 업로드), 목차 상태를 초안으로 갱신.
- 검증: design/·README 상대 링크 깨짐 0건. 삭제 파일을 가리키는 곳은 다른 저장소의 backlog 기록·테스트 픽스처·draft에만 남음(과거 기록이라 유지).
- 진행 중 사고: 작업 도중 HEAD가 task/TASK-9 → main으로 바뀌는 일이 있었고(원인 미확인, 서브에이전트들은 부인), 백업 후 복구해 손실 없음.
커밋: fd15f32..b0bd456
<!-- SECTION:FINAL_SUMMARY:END -->
