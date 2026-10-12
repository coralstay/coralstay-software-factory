---
id: TASK-5
title: 설계서를 제안서·요구사항 명세서·아키텍처 설계서·구현 계획서·구현 결과 보고서 5문서 체계로 재편
status: Done
assignee: []
created_date: '2026-10-05 06:59'
updated_date: '2026-10-05 07:09'
labels:
  - docs
dependencies: []
documentation:
  - design/README.md
  - /Users/flynn_macpro/.claude/plans/typed-chasing-conway.md
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
design/의 SDD 블루프린트(0~13장+용어집)를 프로젝트 서류 흐름(제안 → 요구사항 → 아키텍처 → 구현 계획 → 구현 결과)으로 재편한다.
계획 원문: ~/.claude/plans/typed-chasing-conway.md

수용 기준(승격 시 AC로 등록):
1. 기존 장 파일을 git mv로 1-제안서/ 2-요구사항-명세서/ 3-아키텍처-설계서/ 4-구현-계획서/ 하위로 옮기고 제목·번호·교차참조를 새 체계에 맞춘다
2. 신규 골격 9개(기대 효과와 리스크, 이해관계자와 운영 환경, 기능 요구사항, 마일스톤과 작업 분해, 5-구현-결과-보고서/ 4개 장)를 기존 골격 형식으로 작성한다
3. 00-문서-정보에 추적 체인 G-n → 요구사항 ID → 부품·인터페이스 → 수용 기준·task → 판정 결과를 명시한다
4. design/README.md를 5문서 목차로, 루트 README의 design/ 설명을 새 체계로 고친다
5. Claude 앱 문서(편집 원본) 제목 변경·신규 문서 생성·목차 문서 갱신 후 링크를 README에 기록한다
6. grep -rn 블루프린트 design README.md 결과 0건, README 상대 링크 전부 유효
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 기존 장 파일을 git mv로 1-제안서/ 2-요구사항-명세서/ 3-아키텍처-설계서/ 4-구현-계획서/ 하위로 옮기고 제목·번호·교차참조를 새 체계에 맞춘다
- [x] #2 신규 골격 9개(기대 효과와 리스크, 이해관계자와 운영 환경, 기능 요구사항, 마일스톤과 작업 분해, 5-구현-결과-보고서/ 4개 장)를 기존 골격 형식으로 작성한다
- [x] #3 00-문서-정보에 추적 체인 G-n → 요구사항 ID → 부품·인터페이스 → 수용 기준·task → 판정 결과를 명시한다
- [x] #4 design/README.md를 5문서 목차로, 루트 README의 design/ 설명을 새 체계로 고친다
- [x] #5 Claude 앱 문서(편집 원본) 제목 변경·신규 문서 생성·목차 문서 갱신 후 링크를 README에 기록한다
- [x] #6 grep -rn 블루프린트 design README.md 결과 0건, README 상대 링크 전부 유효
<!-- AC:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
design/의 단일 SDD 블루프린트를 5문서 체계(1 제안서 · 2 요구사항 명세서 · 3 아키텍처 설계서 · 4 구현 계획서 · 5 구현 결과 보고서)로 재편했다.
- 기존 14개 장을 git mv로 새 디렉토리에 옮기고 제목을 '문서번호.장번호'로, 교차참조(N장 · 7.n)를 새 번호와 § 표기로 바꿨다.
- 신규 골격 8개 작성: 1.04, 2.01, 2.03, 4.01, 5.01~5.04 (draft의 '9개'는 계산 착오로 실제 대상은 8개).
- 00-문서-정보에 문서 구성 표와 추적 사슬 G-n → 요구사항 ID → 부품·인터페이스 → 수용 기준·task → 판정(5.02)을 명시했다.
- Claude 앱 문서: 기존 15개 제목·본문 교차참조 갱신, 신규 8개 생성, 목차 문서를 5문서 표로 재작성. design/README.md에 링크 기록.
- 검증: grep 블루프린트 design README.md 0건, design/README.md 상대 링크 24개 모두 유효, '(링크 예정)' 0건.
커밋: 2ac7a73, c762d82, 47d0f65, 95a695b
<!-- SECTION:FINAL_SUMMARY:END -->
