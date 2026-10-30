---
id: TASK-20
title: coding-agent-git-commit-tool 서술을 코드에 맞춘다(AI-Agent 트레일러 · 훅 하나 · 형식 규칙)
status: In Progress
assignee: []
created_date: '2026-10-30T12:33:00Z'
updated_date: '2026-10-30T12:58:00Z'
labels:
  - design
dependencies: []
documentation:
  - /Users/flynn_macpro/.claude/plans/starry-greeting-curry.md
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
2026-10-30 드리프트 점검에서 최상위 design/의 coding-agent-git-commit-tool 서술이 코드와 어긋났다. 코드는 hooks/prepare-commit-msg 하나만 두고(commit-msg · post-commit은 GF-127 · GF-128에서 삭제), AI-Tool · AI-Tool-Version · AI-Model을 AI-Agent 한 줄로 합쳤고, Verify-Bypassed를 붙이지 않는다. 문서는 아직 옛 구성과 트레일러를 적고 있다.

코드 기준점: components/coding-agent-git-commit-tool 작업 트리(task/GF-146; 훅 구조는 main과 같다) — hooks/prepare-commit-msg, hooks/gitformat.conf, install.sh, tests/.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 트레일러 표기를 AI-Agent: <도구>/<버전> (<모델>) 한 줄로 바꾼다 — 3.04 §2 예시 · 표, 3.03 §3, 3.01, 4.01, 2.03 TRL-006, 3.05 ADR-021, 부록 용어집 (수동)
- [x] #2 트레일러 조건을 코드에 맞춘다 — Signed-off-by는 사람 커밋에만(값은 git var GIT_COMMITTER_IDENT), Co-Authored-By는 AI_AGENT 도구가 claude-code일 때, Verify-Bypassed 삭제(TRL-008 문구, ID 유지), Task-Id는 예외 브랜치(main · master · develop · release/*) · 재생 커밋 제외(TRL-003) (수동)
- [x] #3 형식 규칙을 코드에 맞춘다 — 50자는 제목 줄 전체, Revert · Reapply 제목 면제, TRL-002에 예외 브랜치 (수동)
- [x] #4 3.03 §3 구성 · 주의점을 코드에 맞춘다 — 훅은 prepare-commit-msg 하나, python3가 없으면 커밋이 막힘, commit --no-verify로 건너뛸 수 없음(탐지 못 하는 것은 push --no-verify), .gitformat-* 파일 서술 삭제, NFR-005를 구현 목록에서 뺌 (수동)
- [x] #5 3.04 §2에 AI 판정(AI_AGENT 하나), 메시지에 이미 있는 AI-Agent 줄은 그대로 두는 한계, 비 Claude AI 도구의 knownModel 게이트를 적는다 (수동)
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 바꾼 문장마다 근거 코드 위치(file:line)를 구현 노트에 적는다 (수동)
- [x] #2 옛 표현 grep 결과를 노트에 남긴다 (수동)
- [x] #3 design/ 상대 링크 깨짐 0, 요구사항 ID 재사용 · 재번호 없음 (수동)
- [x] #4 파일 하나에 커밋 하나, 각 커밋에 카드 ID, push 하지 않는다 (수동)
- [x] #5 Done 전에 장 대응표로 영향받는 컴포넌트마다 Refs 커밋 또는 Propagation-None 트레일러를 남긴다 (수동)
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
### Subjective
유저 결정(2026-10-30): 최상위 design/의 코드 ↔ 문서 불일치만 고친다. 방향은 코드 → 문서. 코드가 다르게 구현돼 있고 그것을 뒤집는 결정이 없으면 문서를 코드에 맞추고, 결정이 먼저 반영되고 코드는 카드로 예정만 된 것은 규칙 문장을 두고 '현재 미구현(카드 ID)' 단서만 단다. 코드가 원칙보다 넓게 허용하는 것은 문서를 바꾸지 않는다. 문서끼리만 어긋나는 항목은 범위 밖이다. 계획: ~/.claude/plans/starry-greeting-curry.md

### Objective
- 트레일러: prepare-commit-msg insert_trailers(:698-725), AI-Agent(:643, 주석 :501), Co-Authored-By(:716), Hooks-Commit(:651-660), Signed-off-by 사람만(:724, :673-683), Verify-Bypassed · Tokens-Used 없음(:501-502, :689), 재생 커밋 건너뜀(:141-147, :779).
- 형식: 제목 정규식(:262), 50자는 제목 줄 전체(:309-310), Revert 면제(:236, :310), 본문 72자(:328-341), 에디터 거부(:181-191), ID는 브랜치명(:405-424).
- 판정: AI_AGENT 하나(:435-436), knownModel 게이트(:441-464), 기존 AI-Agent 줄 유지(:703-705).
- 문서 위치: 3.04:36-39 · 51 · 59-64, 3.03:92-94 · 106 · 113 · 117, 3.01:11, 4.01:71, 2.03:86-93, 3.05:184, 용어집:125.

### Assessment
트레일러 · 형식은 코드가 판정한다. 요구사항 행(TRL-002 · 003 · 006 · 008)은 ID를 유지한 채 문구만 코드에 맞춘다. NFR-005의 소관 정리는 문서끼리의 문제라 이 카드에서는 이 도구의 구현 목록에서 빼는 데까지만 한다.

### Plan
1. 3.04 §2 → 3.03 §3 → 2.03 TRL → 3.01 → 4.01 → 3.05 ADR-021 → 용어집 순서로 파일마다 커밋한다.
2. grep AI-Tool · AI-Model · Verify-Bypassed · commit-msg · post-commit · .gitformat- 결과를 노트에 남긴다.
3. 상대 링크 검사, 장 대응표로 전파 대상 확인(coding-agent-git-commit-tool design/이 코드와 맞으면 Propagation-None).
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
코드 기준점: components/coding-agent-git-commit-tool(task/GF-146, 19695df). 아래 file:line의 PCM = hooks/prepare-commit-msg.

AC #1 AI-Agent 한 줄 표기
- 3.04 §2 예시 블록(:35-39) · 트레일러 표(:59-60) · 오케스트레이터 커밋 문장(:69), 3.03 §3 역할(:92), 3.01 컴포넌트 지도(:11), 4.01(:71), 2.03 TRL-006(:91), 3.05 ADR-021(:185), 용어집 트레일러(:125)
- 근거: PCM:643(<도구>/<버전> (<모델>), version-unavailable · model-unavailable), :496 · :501(AI-Tool · AI-Tool-Version · AI-Model을 합침), :627(버전 = AI_AGENT 둘째 필드, - → .), :630-641(모델 출처), :712-713(AI 커밋에만), hooks/gitformat.conf trailer.aiAgent

AC #2 트레일러 조건
- 3.04 §2 표: Signed-off-by 사람 커밋만 · git var GIT_COMMITTER_IDENT(:62), Co-Authored-By claude-code만(:60), Hooks-Commit 생략 조건(:61), Verify-Bypassed 행 삭제, Task-Id 예외(:58), 면제 행(:52)
- 2.03 TRL-003(:88) 예외 브랜치 · detached HEAD · 재생 커밋 제외, TRL-008(:93) Verify-Bypassed 부분 폐기(2026-10-30) 표시, ID 유지
- 근거: PCM:724-725 · :673-683(Signed-off-by), :716-720(Co-Authored-By), :651-660 · :722(Hooks-Commit), :501-502(Verify-Bypassed 없음), :544-549(Task-Id는 패턴 있을 때만), :141-147 · :779-780(재생 · 병합 커밋 면제), tests/test_verify_bypass_detection.py

AC #3 형식 규칙
- 3.04 §2 제목 · 본문 표: 50자는 제목 줄 전체(:48), Revert · Reapply 면제(:49), 등록 트레일러 줄 72자 예외(:50)
- 2.03 TRL-001(:86) 제목 줄 전체 50자 · Revert/Reapply 면제, TRL-002(:87) 예외 브랜치(main · master · develop · release/*, gitformat.branchExempt) · detached HEAD 면제
- 근거: PCM:262(제목 정규식), :308-310(len(subject_line) 전체, revert 면제), :236(REVERT_SUBJECT_RE), :328-341(본문 72자, 트레일러 예외), :405-424(브랜치 강제 · 예외), gitformat.conf branchExempt · subjectMaxLength

AC #4 3.03 §3 구성 · 주의점
- 구성(:94) 훅 하나 + commit-msg · post-commit 삭제 이력, 구현 요구사항(:93) NFR-005 제외, 이력 불변(:106) push --no-verify, 주의점 python3 부재 시 커밋 막힘(:113), commit --no-verify로 건너뛸 수 없음(:114), AI 판정 문구(:117), .gitformat-* 삭제(:118)
- 근거: PCM:5-8(commit-msg · post-commit 삭제), :14-16 · :467-469(--no-verify로 못 건너뜀), :757-784(실행 순서), tests/test_python3_missing.py(커밋 객체 안 생김), install.sh:134-136(push --no-verify 탐지 불가), PCM:503-506 · :760(.gitformat-* 파일 코드 삭제), :643(사유 없는 *-unavailable만 → NFR-005 미구현)

AC #5 3.04 §2 판정 · 한계 · 게이트
- 3.04 §2 표 아래 목록(:65-67)
- 근거: PCM:435-436(AI_AGENT 첫 _ 앞부분), :441-464(비 claude-code 도구는 gitformat.aiModel 필수 + knownModel 목록), :531-533 · :703-705(키 단위 중복 판정, 대소문자 무시, 값 안 봄), :347-364(Fixes 검증만)

grep(design/, svg 제외: AI-Tool · AI-Model · AI-Tool-Version · Verify-Bypassed · commit-msg · post-commit · .gitformat-)
- 3.03:94 commit-msg · post-commit — 삭제 이력 서술(정당)
- 3.03:114 · :115 — prepare-commit-msg 부분 문자열(정당)
- 2.03:93 TRL-008 Verify-Bypassed — 폐기 이력 서술(정당)
- 2.02:128 '커밋 트레일러 … Task-Id · AI-Model 등' — AC #1 목록 밖이라 고치지 않음, 유저 확인 필요

상대 링크 검사: design/**/*.md 깨진 링크 0. 검출 1건(00-문서-정보.md의 ../diagrams/<이름>.svg)은 자리표시 예시라 실제 링크가 아님(이 카드와 무관, 기존).

다이어그램: 07-task-sequence.mmd 라벨('훅이 커밋 형식 검사 · 트레일러 부착')은 코드와 어긋나지 않아 손대지 않음.

범위 밖 발견(고치지 않음): 3.03 §1 주의점(:47)의 '(transcript-not-found)' 사유 표기 — 코드는 사유 없이 model-unavailable만 남긴다(PCM:643). 4.01:71 남은 작업 '토큰 측정 로직 제거(GF-146)'는 그 저장소에서 GF-146 완료(19695df).

검증(메인 세션, 2026-10-30): 3.04 §2 · 2.03 TRL 변경을 prepare-commit-msg와 다시 대조(:236 REVERT_SUBJECT_RE, :309-310 제목 줄 전체 길이, :414 branchExempt, :435-436 ai_tool_id, :630-645 trailer_ai_agent) — 일치. 2.02:128 '커밋 트레일러' 행의 AI-Model도 같은 사실이라 AI-Agent로 고침(64abc03). grep AI-Tool · AI-Model · Verify-Bypassed · post-commit · .gitformat-: 남은 것은 3.03:94(삭제 이력) · 2.03 TRL-008(폐기 이력) 2건뿐. 전파: 세 컴포넌트 design/에 옛 서술 없음 → Propagation-None 3줄. 브랜치의 3f7ed86 '[chore][workspace] align layout and tags'(.claude-code-agile-hooks.json humanSigners 추가)는 출처 미상, 내용은 유저가 만든 설정과 같아 이력을 고치지 않음.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
최상위 design/의 coding-agent-git-commit-tool 서술을 코드(prepare-commit-msg · gitformat.conf · install.sh · tests/, task/GF-146)에 맞췄다.

- 트레일러: AI-Tool · AI-Tool-Version · AI-Model을 AI-Agent 한 줄로(3.04 §2 · 3.03 §3 · 3.01 · 4.01 · 2.02 · 2.03 TRL-006 · ADR-021 · 용어집), Signed-off-by는 사람 커밋에만(GIT_COMMITTER_IDENT), Co-Authored-By는 claude-code일 때, Verify-Bypassed는 TRL-008에서 폐기 표시(ID 유지), Task-Id 예외 브랜치 · 재생 커밋.
- 형식: 50자는 제목 줄 전체, Revert · Reapply 면제, TRL-001 · TRL-002 문구.
- 구성: 훅은 prepare-commit-msg 하나, python3 없으면 커밋 차단, commit --no-verify로 못 건너뜀, .gitformat-* 서술 삭제, NFR-005를 이 도구 구현 목록에서 뺌, AI 판정 · knownModel 게이트 · 기존 AI-Agent 줄 유지 한계.
- 검증: 서브에이전트 구현 후 메인 세션이 코드 줄과 재대조, 옛 표현 grep은 이력 서술 2건만, 상대 링크 깨짐 0, 요구사항 ID 재번호 없음. 전파는 세 컴포넌트 모두 Propagation-None.
- 범위 밖 발견(노트): 3.03 §1의 '(transcript-not-found)' 표기(TASK-21 관련), 4.01의 GF-146 남은 작업 표기.
<!-- SECTION:FINAL_SUMMARY:END -->
