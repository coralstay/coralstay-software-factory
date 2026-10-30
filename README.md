# coralstay-software-factory

Sigkill Foundry — Claude Code 세션을 찍어내고 `kill -9`로 끊어내는 소프트웨어 공장의 설계 저장소다.
소프트웨어 태스크를 `backlog.md` 계층(마일스톤 · 태스크 · AC)으로 분해하고, 태스크마다 역할형
에이전트(Implementer · Reviewer · Verifier · Logger)를 독립 프로세스로 스폰 · 회수한다. 목적은 처리량이
아니라 판단의 독립성이다 — Reviewer와 Verifier가 Implementer의 추론을 물려받지 않도록 컨텍스트 격리
자체를 게이트로 쓴다. 이 저장소에는 설계 문서만 있고, 구현은 아래 컴포넌트 저장소에 있다.

## 설계 문서

- [design/README.md](./design/README.md) — Sigkill Foundry 설계 문서(SDD) 목차. 제안서 · 요구사항 명세서 ·
  아키텍처 설계서 · 구현 계획서 · 구현 결과 보고서의 다섯 문서로 이어진다.

## 컴포넌트 저장소

| 컴포넌트 | 역할 | 저장소 |
| --- | --- | --- |
| agent-orchestrator | JVM 오케스트레이터 — 역할 에이전트 스폰 · 회수 | [coralstay/agent-orchestrator][ao] |
| claude-code-agile-hooks | 규율 레이어 — 훅 · 테스트 게이트 · 상태 전이 | [coralstay/claude-code-agile-hooks][hooks] |
| coding-agent-git-commit-tool | 포맷 레이어 — 커밋 메시지 형식만 맞춘다. 토큰 계량은 하지 않는다 | [coralstay/coding-agent-git-commit-tool][commit] |
| 토큰 계량 컴포넌트 (이름 미정) | 계측 레이어 — 토큰 계량. coding-agent-git-commit-tool에서 분리 예정 | 미정 |
| backlog.md | 태스크 계층 · 상태 저장소 (외부 오픈소스 CLI) | [MrLesk/Backlog.md][backlog] |

## 라이선스

[GNU AGPL-3.0](./LICENSE) — 문서와 아티팩트를 포함한 저장소 전체에 적용된다(전문: [`LICENSE`](./LICENSE), [GNU AGPL-3.0 원문][agpl]).

- 상용 라이선스 — 저작권자가 단독이므로 듀얼 라이선스가 가능하다. AGPL 조건(네트워크
  서비스 제공 시 수정 소스 공개)이 맞지 않는 상용 사용은 별도 협의한다.
  문의: <coralstay3595@gmail.com> (또는 이 저장소의 GitHub Issue).
- 기여 — 듀얼 라이선스 유지를 위해, 기여자는 자신의 기여를 AGPL-3.0과 상용 라이선스 양쪽으로
  배포할 권리를 저작권자에게 허여하는 데 동의한 것으로 본다.
- 이전 배포 — 커밋 `a321868` 시점까지의 문서는 MIT로 배포되었고 그 스냅샷은 계속 MIT다.

---

## English Summary

coralstay-software-factory holds the design of Sigkill Foundry, a software factory that spawns
Claude Code sessions and kills them when their work is done. Software tasks are decomposed into a
`backlog.md` hierarchy (milestone · task · AC) and executed by role-based agents — Implementer,
Reviewer, Verifier, Logger — spawned and reclaimed as independent processes by a JVM orchestrator.
The point is independence of judgment, not throughput: Reviewer and Verifier must not inherit the
Implementer's reasoning, so context isolation itself is used as a gate. This repository contains only
the design documents (Korean, under [`design/`](./design/README.md)); the implementation lives in the component repositories above. Licensed under
[AGPL-3.0](./LICENSE) ([original text][agpl]); commercial licensing available on request — <coralstay3595@gmail.com> or a
GitHub issue.

---

## 링크

<!-- 본문의 모든 외부 링크는 여기서만 정의한다. URL이 바뀌면 이 블록만 고친다. -->

[ao]: https://github.com/coralstay/agent-orchestrator
[hooks]: https://github.com/coralstay/claude-code-agile-hooks
[commit]: https://github.com/coralstay/coding-agent-git-commit-tool
[backlog]: https://github.com/MrLesk/Backlog.md
[agpl]: https://www.gnu.org/licenses/agpl-3.0.html
