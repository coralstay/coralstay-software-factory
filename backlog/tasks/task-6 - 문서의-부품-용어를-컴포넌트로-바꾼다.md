---
id: TASK-6
title: 문서의 '부품' 용어를 '컴포넌트'로 바꾼다
status: Done
assignee: []
created_date: '2026-10-05 07:16'
updated_date: '2026-10-05 07:18'
labels:
  - docs
dependencies: []
ordinal: 5000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
소프트웨어 공학 표준 용어로 통일한다. 유저가 후보(컴포넌트·모듈·서브시스템) 중 컴포넌트를 승인함.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 저장소 문서의 '부품'을 모두 '컴포넌트'로 바꾸고 조사를 맞춘다
- [x] #2 부품-현황.md와 3.03 장 파일을 git mv로 이름 변경하고 참조를 고친다
- [x] #3 Claude 앱 문서의 제목·본문도 같이 바꾼다
- [x] #4 git grep 부품 결과 0건, design/README.md 상대 링크 전부 유효
<!-- AC:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
문서의 '부품'을 '컴포넌트'로 통일했다 (유저 승인 용어).
- 저장소: design/ 9개 파일, .gitignore 주석, 부품-현황.md → 컴포넌트-현황.md, 03-부품-명세.md → 03-컴포넌트-명세.md (git mv). 조사도 맞춤(부품과→컴포넌트와, 부품이→컴포넌트가, 부품으로→컴포넌트로).
- Claude 앱 문서: 24개 전부 검색해 0. 문서 정보, 2.01, 2.03, 3.01, 3.03(제목 포함), 3.04, 4.01, 5.01을 고침.
- 검증: git grep 부품 0건(components/ 제외), design/README.md 상대 링크 전부 유효.
커밋: 2abcb6c
<!-- SECTION:FINAL_SUMMARY:END -->
