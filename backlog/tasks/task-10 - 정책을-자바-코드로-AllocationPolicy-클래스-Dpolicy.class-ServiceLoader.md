---
id: TASK-10
title: '정책을 자바 코드로: AllocationPolicy 클래스 + -Dpolicy.class + ServiceLoader'
status: Done
assignee: []
created_date: '2026-10-10 22:29'
updated_date: '2026-10-10 22:31'
labels:
  - design
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
유저 결정(2026-10-11): 정책은 설정 파일(YAML·key=value)이 아니라 자바 코드로 쓴다 — ① 오케스트레이터에 넣은 AllocationPolicy 구현 클래스를 기본으로, -Dpolicy.class로 교체 ② 별도 jar의 구현을 java.util.ServiceLoader로 찾아 꽂기. 외부 의존성 없음(NFR-010)과 맞고, 조건 판단·타입 검사가 가능하다. 런타임 컴파일(javax.tools)은 보안 경계 때문에 택하지 않는다.

수용 기준(승격 시 AC로 등록):
1. ORC-010을 ①·② 방식으로 고친다(YAML 기본 구현 요구 제거)
2. 3.03 §1 · 3.04 정책 계약 · 3.05 ADR-003을 같은 내용으로 고치고, ADR-003 기각한 대안에 YAML(외부 의존성) · key=value(조건 판단 불가) · 런타임 컴파일(보안 경계)을 적는다
3. Claude 앱 문서(2.03 · 3.03 · 3.04 · 3.05)도 같이 고친다
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 ORC-010을 ①·② 방식으로 고친다(YAML 기본 구현 요구 제거)
- [x] #2 3.03 §1 · 3.04 정책 계약 · 3.05 ADR-003을 같은 내용으로 고치고, ADR-003 기각한 대안에 YAML · key=value · 런타임 컴파일을 적는다
- [x] #3 Claude 앱 문서(2.03 · 3.03 · 3.04 · 3.05)도 같이 고친다
<!-- AC:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
정책을 설정 파일이 아니라 자바 코드로 쓰도록 최상위 문서를 고쳤다(유저 결정: 자바 코드 ①·② 방식).
- ORC-010: AllocationPolicy 구현 자바 클래스, 내장 기본 구현 + ① -Dpolicy.class ② ServiceLoader(별도 jar) 순 교체, 외부 라이브러리 없음(NFR-010).
- 3.04 정책 계약: 기본 구현 DefaultAllocationPolicy, 선택 순서(-D → ServiceLoader 하나 → 둘 이상이면 시작 거부 → 없으면 기본), 배포(META-INF/services).
- 3.03 §1, 3.05 ADR-003 결정·근거·기각한 대안(YAML: 외부 의존성·암묵적 타입·CVE-2022-1471 / key=value: 계층·조건 표현 불가 / 런타임 컴파일: 보안 경계·JDK 필요).
- Claude 앱 문서 2.03 · 3.03 · 3.04 · 3.05 같은 수정.
- 남은 일: agent-orchestrator 쪽(decision-10 대체, ModelPolicy → AllocationPolicy 설계, 4.01)은 그 저장소 태스크로 진행.
커밋: ace234b
<!-- SECTION:FINAL_SUMMARY:END -->
