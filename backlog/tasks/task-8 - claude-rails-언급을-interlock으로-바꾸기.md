---
id: TASK-8
title: claude-rails 언급을 claude-code-agile-hooks로 바꾸고 3.03 컴포넌트 명세 §2에 세 가지 성격 반영
status: Done
assignee: []
created_date: '2026-10-05 07:49'
updated_date: '2026-10-05 11:43'
labels:
  - rename
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
claude-rails 저장소가 interlock(coralstay/interlock)으로 이름이 바뀐다. 계획: ~/.claude/plans/typed-chasing-conway.md

수용 기준(승격 시 AC로 등록):
1. README · 아키텍처.md · 컴포넌트-현황.md · design/ 문서의 claude-rails 이름·링크·components/ 경로를 interlock으로 바꾼다
2. Claude 앱 문서(편집 원본)도 같이 바꾼다
3. RFC HTML/PDF에 이름이 있으면 빌드 스크립트로 재생성한다
4. git grep claude-rails가 기록성 문서에만 남는다
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 README · 아키텍처.md · 컴포넌트-현황.md · design/ 문서의 claude-rails 이름·링크·경로를 claude-code-agile-hooks로 바꾼다
- [x] #2 3.03 컴포넌트 명세 §2에 훅의 세 가지 성격(절차 강제 · 품질·안전 게이트 · 기록·관측)과 훅 저장소 설계 문서 링크를 담는다
- [x] #3 Claude 앱 문서도 같이 바꾼다
- [x] #4 RFC HTML/PDF에 이름이 있으면 빌드 스크립트로 재생성한다
- [x] #5 git grep claude-rails · interlock이 기록성 문서에만 남는다
<!-- AC:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
claude-rails의 최종 이름 claude-code-agile-hooks를 최상위 문서(Sigkill Foundry)에 반영했다 (커밋 58f9a9f: claude-rails→interlock, 95ab975: interlock→claude-code-agile-hooks).
- README 로드맵, design/ 0 문서 정보(대상 저장소 표·영역 설명)·1.01·2.03·3.03, RFC HTML, 다이어그램 원본 → build-diagrams.py · build-pdf.sh로 SVG·PDF 재생성.
- 3.03 컴포넌트 명세 §2에 훅의 세 가지 성격(① 절차 강제 ② 품질·안전 게이트 ③ 기록·관측)과 훅 저장소 설계 문서 링크를 담았다.
- 컴포넌트-현황.md는 2026-10-05 스냅샷이라 본문은 두고 이름 변경 안내만 추가. 요구사항 영역 코드 RAIL 유지.
- Claude 앱 문서(0, 1.01, 2.03, 3.03) 같은 수정.
- 같이 정리: PR #3(task/TASK-5)을 task/TASK-6까지 fast-forward해 #3에서 '부품'이 사라지게 했고, #6의 base를 task/TASK-5로 바꿈. #4는 gh pr close가 git-safety 훅으로 금지돼 유저가 닫아야 함.
- 검증: git grep interlock 0건, claude-rails는 컴포넌트-현황.md(스냅샷)에만.
<!-- SECTION:FINAL_SUMMARY:END -->
