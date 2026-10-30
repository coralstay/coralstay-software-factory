---
id: TASK-20
title: coding-agent-git-commit-tool 서술을 코드에 맞춘다(AI-Agent 트레일러 · 훅 하나 · 형식 규칙)
status: In Progress
assignee: []
created_date: '2026-10-30T12:33:00Z'
updated_date: '2026-10-30T12:52:00Z'
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
- [ ] #1 트레일러 표기를 AI-Agent: <도구>/<버전> (<모델>) 한 줄로 바꾼다 — 3.04 §2 예시 · 표, 3.03 §3, 3.01, 4.01, 2.03 TRL-006, 3.05 ADR-021, 부록 용어집 (수동)
- [ ] #2 트레일러 조건을 코드에 맞춘다 — Signed-off-by는 사람 커밋에만(값은 git var GIT_COMMITTER_IDENT), Co-Authored-By는 AI_AGENT 도구가 claude-code일 때, Verify-Bypassed 삭제(TRL-008 문구, ID 유지), Task-Id는 예외 브랜치(main · master · develop · release/*) · 재생 커밋 제외(TRL-003) (수동)
- [ ] #3 형식 규칙을 코드에 맞춘다 — 50자는 제목 줄 전체, Revert · Reapply 제목 면제, TRL-002에 예외 브랜치 (수동)
- [ ] #4 3.03 §3 구성 · 주의점을 코드에 맞춘다 — 훅은 prepare-commit-msg 하나, python3가 없으면 커밋이 막힘, commit --no-verify로 건너뛸 수 없음(탐지 못 하는 것은 push --no-verify), .gitformat-* 파일 서술 삭제, NFR-005를 구현 목록에서 뺌 (수동)
- [ ] #5 3.04 §2에 AI 판정(AI_AGENT 하나), 메시지에 이미 있는 AI-Agent 줄은 그대로 두는 한계, 비 Claude AI 도구의 knownModel 게이트를 적는다 (수동)
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 바꾼 문장마다 근거 코드 위치(file:line)를 구현 노트에 적는다 (수동)
- [ ] #2 옛 표현 grep 결과를 노트에 남긴다 (수동)
- [ ] #3 design/ 상대 링크 깨짐 0, 요구사항 ID 재사용 · 재번호 없음 (수동)
- [ ] #4 파일 하나에 커밋 하나, 각 커밋에 카드 ID, push 하지 않는다 (수동)
- [ ] #5 Done 전에 장 대응표로 영향받는 컴포넌트마다 Refs 커밋 또는 Propagation-None 트레일러를 남긴다 (수동)
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
