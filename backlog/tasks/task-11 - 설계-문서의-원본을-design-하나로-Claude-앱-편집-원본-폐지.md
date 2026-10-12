---
id: TASK-11
title: 설계 문서의 원본을 design/ 하나로 (Claude 앱 편집 원본 폐지)
status: Done
assignee: []
created_date: '2026-10-10 22:35'
updated_date: '2026-10-11 08:08'
labels:
  - docs
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
유저 결정(2026-10-11): 설계 문서의 원본은 저장소 design/*.md 하나다. Claude 앱 문서는 편집 원본이 아니다. 근거: 오케스트레이터가 띄우는 에이전트는 작업 폴더에서 조상 문서를 파일로 읽는다(ORC-019), git 이력·PR 리뷰. 편집은 Claude Code(웹 포함)나 GitHub 편집기로 하고 커밋·PR로 남긴다.

수용 기준(승격 시 AC로 등록):
1. 0 문서 정보 편집 규칙, design/README.md, 루트 README에서 'Claude 앱이 편집 원본' 문구와 Claude 앱 링크 칸을 없애고 원본은 design/라고 적는다
2. 단방향 동기화 draft(DRAFT-1)를 보관(archive)한다 — 더 이상 필요 없다
3. Claude 앱의 기존 문서 처리(갱신 중단 표시 또는 삭제)는 유저 결정을 받아 따로 한다
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 0 문서 정보 편집 규칙, design/README.md, 루트 README에서 'Claude 앱이 편집 원본' 문구와 Claude 앱 링크 칸을 없애고 원본은 design/라고 적는다
- [x] #2 단방향 동기화 draft(DRAFT-1)를 보관한다
- [x] #3 Claude 앱의 기존 문서 처리는 유저 결정을 받아 따로 한다
<!-- AC:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
설계 문서의 원본을 저장소 design/ 하나로 정했다(유저 결정 2026-10-11).
- 0 문서 정보 편집 규칙: 원본은 design/**/*.md, 다른 곳에 사본 · 편집 원본을 두지 않음, 고치면 커밋 · PR, 에이전트도 이 파일을 조상 문서로 읽음(ORC-019).
- design/README.md: Claude 앱 링크 칸 제거, 상태를 실제 파일 기준으로(5.01~5.04만 작성 전). 루트 README의 Claude 앱 목차 링크 제거. build-diagrams.py 주석 정리.
- 단방향 동기화 draft(DRAFT-1) 보관.
- Claude 앱 문서 정리(유저 결정: 모두 삭제): Sigkill Foundry 24개 + 컴포넌트 저장소에서 중간까지 만들어진 35개, 모두 삭제 — 남은 아티팩트 0개 확인.
- 컴포넌트 저장소 3곳도 같은 규칙으로 고침(TASK-55 · AO-24 · GF-145).
커밋: 9097580
<!-- SECTION:FINAL_SUMMARY:END -->
