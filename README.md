# coralstay-software-factory

> **초안 · 미검증.** 설계 문서만 있는 저장소다. 구현 코드는 한 줄도 없고, 아래 수치와 구조는
> 어느 것도 실측으로 검증되지 않았다. **"확정된 사실"이 아니라 "검증해야 할 가설 목록"** 으로
> 읽어주길 바란다. RFC 본문 역시 `DRAFT · 검증 대기` 상태다.
>
> 이 README는 RFC(2026-09-21 정리본)를 요약한 **파생 문서**다. 본문 수치와 인용의 원본은
> 항상 RFC이며, 둘이 어긋나면 RFC가 맞다. 갱신 규칙은 [이 문서를 고치는 규칙](#이-문서를-고치는-규칙) 참고.

소프트웨어 태스크를 `backlog.md` 계층(마일스톤 · 태스크 · AC)으로 분해하고, 태스크마다
역할형 에이전트(Implementer · Reviewer · Verifier · Logger)를 독립 프로세스로 스폰·회수하는
**에이전트 레일 파이프라인** 설계 저장소.

계층은 코드 단위에 고정돼 있다 — **태스크 = 파일 하나, AC = 함수 하나, 커밋 = 함수 하나,
에이전트 배정 = 파일 하나.** 파일이 격리 단위이므로 워크트리를 분리하면 두 에이전트가 같은
파일을 만질 일이 구조적으로 없고, 커밋이 함수 단위이므로 토큰 계량도 함수 단위로 붙는다.

## 왜 만드는가 — 네 개의 질문

이 저장소는 방어할 결론을 정해두고 근거를 모은 것이 아니다. 출발점은 호기심 하나였다.

> **에이전트 모델을 왜 · 언제 · 어떻게 · 얼마나 써야 하는가?**

| 질문 | 지금까지의 답 |
| --- | --- |
| **왜** | 처리량이 아니라 **판단의 독립성**. Reviewer/Verifier가 Implementer의 추론을 상속받지 않도록 컨텍스트 격리 자체를 게이트로 쓴다 |
| **언제** | 단일 에이전트가 이미 안정적으로 해내는 태스크에는 쓰지 않는다. 판단 단위는 프로젝트가 아니라 태스크이며, 경계선은 빌려오지 않고 이 저장소에서 직접 측정한다 |
| **어떻게** | 네 역할을 완전히 독립된 프로세스로 두고, JVM 오케스트레이터가 정책을 외부에서 주입해 스폰·회수한다 |
| **얼마나** | 역할 수·모델은 Allocation Policy가 결정하고, 동시성 상한은 `min(그래프 폭, 자원 실측(peak RSS·API 한도))` — 순차 그래프의 **길이(임계 경로)** 와 **폭(동시 배정 가능 태스크 수)** 을 스케줄 라운드마다 센다 |

## 튜링의 어휘로 말하면 — 규율과 자발성

1948년 NPL 보고서 [**Intelligent Machinery**][im]에서 튜링은 구조가 대체로 무작위한 기계를
*비정형 기계(unorganised machine)* 라 부른다.

> "Machines which are largely random in their construction in this way will be called
> 'Unorganised Machines'."
>
> — 이런 식으로 구조가 대체로 무작위한 기계를 '비정형 기계'라 부르기로 한다.
> (§4 Unorganised machines · *The Essential Turing* p.417)

LLM은 이 계보의 기계다. 그리고 그런 기계의 보편성은 **무조건이 아니라 조건부**다.

> "with a B-type unorganised machine with sufficient units one can find initial conditions
> which will make it into a universal machine with a given storage capacity"
>
> — 충분한 수의 유닛을 가진 B형 비정형 기계라면, 주어진 저장 용량 안에서 그것을 보편 기계로
> 만들어줄 초기 조건을 찾아낼 수 있다. (§8 Organising unorganised machinery · p.423)

같은 보고서에서 튜링은 그 조건을 **규율(discipline)** 과 **자발성(initiative)** 으로 나눈다.
이 저장소의 이름이 "레일"인 이유가 여기 있다.

> "To convert a brain or machine into a universal machine is the extremest form of discipline.
> But discipline is certainly not enough in itself to produce intelligence. That which is
> required in addition we call initiative."
>
> — 뇌나 기계를 보편 기계로 바꾸는 것은 규율의 가장 극단적인 형태다. 그러나 규율만으로
> 지능이 생기지는 않는다. 거기에 더 필요한 것을 우리는 자발성이라 부른다.
> (§12 Discipline and initiative · p.431)

**레일이 규율이고, 에이전트가 자발성이다.** 훅 · 테스트 게이트 · 워크트리 격리 · 상태 전이
규칙은 전부 규율 쪽이고, 그 안에서 무엇을 어떻게 쓸지는 에이전트에게 남긴다. 그래서 이
설계의 진짜 질문은 "얼마나 자동화할 것인가"가 아니라 **"레일을 어디까지만 깔 것인가"** 다 —
규율을 끝까지 밀면 자발성이 사라진다는 경고가 위 문장에 이미 들어 있다.

판정 쪽의 경계는 1936년 [**On Computable Numbers, with an Application to the
Entscheidungsproblem**][cn]이 그어놨다.

> "Hence the Entscheidungsproblem cannot be solved."
>
> — 따라서 결정문제는 풀릴 수 없다. (§11 Application to the Entscheidungsproblem, p.262)

임의의 명세가 충족됐는지 판정하는 **일반** 절차는 없다. 그러나 §11이 부정한 것은 일반 절차일
뿐이고, **각 프로젝트가 스스로 정한 유한한 판정기**는 만들 수 있다 — 그것이 테스트이자
AC/DoD다. 판정기를 코드로 쓸 수 있는 자리에서는 사람이 판정 루프에 앉아 있을 이유가 없다는
것이 이 설계의 좁은 주장이다. (같은 논문 §6의 보편 기계 결과는 이 설계의 배경일 뿐 근거는
아니다.)

> **인용에 대한 정직한 단서 —** 튜링의 두 논문은 이 설계에 **어휘와 문제 설정**을 줬을 뿐,
> 4-role 구조가 효과가 있다는 **증거가 아니다.** 그 효과는 아직 아무 문헌으로도 뒷받침되지
> 않았고, 이 저장소가 직접 측정해야 할 대상이다. RFC 본문의 인용 원칙 — DOI/arXiv가 붙은
> 인용만 신뢰하고 블로그발 수치는 원문 확인 후 전부 삭제 — 을 여기서도 그대로 적용한다.
> 위 인용문은 전부 B. J. Copeland 편 『The Essential Turing』(Oxford, 2004)의 수록 원문과
> 페이지 단위로 대조했다.

## 목적은 자동화가 아니다

이 파이프라인이 파는 것은 처리량도, "지시만 던지면 나오는 소프트웨어"도 아니다.
**Reviewer와 Verifier가 Implementer의 추론 경로를 물려받지 않게 만드는 것**이다.
컨텍스트 격리가 곧 게이트이고, 격리를 유지하는 비용(프로세스 분리, 조상 문서 재로딩)은
그 독립성의 값으로 지불한다.

그래서 이 구조가 잘 맞지 않는다고 말하는 출처들도 RFC 본문에 그대로 인용해 뒀다 —
"같은 컨텍스트를 공유해야 하는 도메인은 멀티에이전트에 안 맞는다", "순차 작업·동일 파일
편집에는 단일 세션이 낫다". 이 설계는 셋 다 해당한다. 그럼에도 쓰는 이유가 위의 독립성이고,
**한 태스크에 네 역할을 붙이는 선택 자체는 속도로 정당화하지 않는다.**

단, 이것은 *태스크 안*의 이야기다. 태스크 *사이*는 완전히 다른 층위이고, 거기서는 처리량을
실제로 추구한다 — 다음 절.

### 이 구조가 서는 순서

각 단계에 근거의 종류를 함께 적는다. 외부 근거인지, 스스로 선 논증인지, 아직 검증되지 않은
가정인지 구분하지 않으면 사슬이 어디서 끊기는지 보이지 않는다.

| # | 단계 | 근거 |
| --- | --- | --- |
| 1 | LLM은 확률적 기계이고, 같은 맥락 안의 자기검토는 그 맥락이 만든 오류를 구조적으로 놓친다 | 자체 논증 |
| 2 | 그러므로 판정자에게 필요한 것은 다른 *프롬프트*가 아니라 다른 **컨텍스트**다. 세션 내 단계 분리는 이력을 공유하므로 조건을 못 채운다 | 자체 논증 |
| 3 | Claude Code에서 컨텍스트 경계는 곧 프로세스 경계다. 세션 간 전달은 순수 텍스트뿐이고 이력·파일은 따라가지 않는다 | 도구 사실 (공식 문서 확인) |
| 4 | 별도 프로세스의 조상 문서 재로딩 비용은 프리픽스 캐싱으로 상쇄된다 (비용 41~80%↓, TTFT 13~31%↑) — 프리픽스가 정적이어야 성립 | 외부 근거 · 조건부 |
| 5 | "긴 세션 하나면 되지 않나" — 임상 규모 실험에서 단일 지속 에이전트는 73.1%→16.6%로 붕괴, 오케스트레이션 다중 에이전트는 90.6%→65.3% 유지(p<0.01), 토큰 최대 65배 절감 → **장수 세션 대신 태스크마다 스폰·회수** | 외부 근거 (범위: 정확도·토큰까지. 판단 독립성의 값은 8이 책임진다) |
| 6 | 판정자가 여럿이면 판정이 갈린다. 수렴 지점이 없으면 AC 루프가 끝나지 않는다 → Reviewer는 의견, **Verifier 하나가 최종 게이트** | 자체 논증 |
| 7 | 그 게이트의 기준은 일반 절차로 정할 수 없다(결정문제) → 프로젝트마다 유한한 판정기, 즉 AC·DoD·테스트. 미들웨어는 Exit Code만 본다 | 원리적 제약 |
| 8 | 남는 공백은 그 판정기의 **내용**이다 → 채점 기준을 요구하지 않는 walking skeleton부터, 사슬 전체는 아래 중단 기준으로 검사 | 미해결 · 측정 대상 |

사슬이 끊기는 지점은 둘이다. **4의 캐싱이 성립하지 않으면 3의 비용이 정당화되지 않고,
8의 실측이 이득을 보이지 않으면 1~2의 전제가 틀린 것이다.**

**반증 가능한 중단 기준.** Implementer 단독 + self-review 대비 4-role 구조가 AC 재작업률과
회귀 발생률을 유의미하게 낮추지 못하면, Reviewer/Verifier를 별도 프로세스가 아니라
Implementer 세션 내 단계로 접는다.

## 병렬은 다른 층위에 있다 — 그래프의 길이와 폭

"순차 다음 병렬"은 두 층위에서 따로 적용된다. 섞으면 앞 절의 주장과 모순돼 보이므로 분리해
적는다.

| 층위 | 순차인 것 | 병렬인 것 | 목적 |
| --- | --- | --- | --- |
| **태스크 안** | Implementer의 AC 구현 (같은 브랜치·같은 파일이라 본질적으로 순차) | 커밋 하나가 나올 때마다 Reviewer와 Verifier·DoD가 서로를 기다리지 않고 동시에 판단 | **판단의 독립성** |
| **태스크 사이** | 의존(`--dep`) 또는 파일 결합이 있는 태스크 체인 | 의존·결합이 없는 노드는 동시 배정 | **처리량** |

태스크 사이의 병렬은 감으로 정하지 않고 **센다.** 의존 간선과 결합 간선을 합친 DAG를
위상정렬한 뒤 두 수치를 뽑는다.

- **길이 — 임계 경로.** 가장 긴 순차 체인의 노드 수. 전체 소요의 하한이며 용량을 늘려도
  줄지 않는다(Amdahl). 노드별 실행시간 예측이 없으므로 시간이 아니라 노드 수로 잰다.
- **폭 — 동시 배정 가능한 태스크 수.** 위상 레벨별 노드 수의 최대값으로 근사하고, 정확한
  값이 필요하면 최대 antichain(Dilworth 정리)으로 낸다.

폭이 곧 **그 시점에 의미 있는 동시성의 상한**이다. 폭보다 큰 워커풀은 채울 일감이 없어
낭비되고, 폭보다 작으면 독립 노드를 놀려 work-conserving 제약을 스스로 어긴다. 그래서
실제 동시성은 `min(그래프 폭, 자원 상한)`으로 잡고, 두 수치와 실제 동시 가동 수를 스케줄
라운드마다 기록한다 — 사후에 "이 백로그에서 병렬화가 실제로 이득이었나"를 계산할 수 있는
유일한 자료다.

**반증 조건.** 실측된 폭이 거의 항상 1~2라면 이 백로그는 애초에 병렬 배정할 구조가 아니고,
워커풀·세마포어·결합도 분석 전체가 과설계다 — 그때는 순차 실행 하나로 접는다.

## 언제 쓰는가 — 그리고 언제 쓰지 않는가

판단 단위는 프로젝트가 아니라 **태스크**다. 같은 프로젝트 안에서도 태스크마다 다시 계산한다.

| 쓴다 | 근거 |
| --- | --- |
| 구현자의 추론을 물려받으면 안 되는 태스크 | 판단의 독립성이 곧 이 구조의 존재 이유다. 같은 맥락을 공유한 자기검토로는 잡히지 않는 오류가 대상 |
| 판정을 게이트로 닫을 수 있는 작업 | 미들웨어는 Exit Code만 심사한다. AC/DoD가 없으면 이 구조가 보장하는 것은 아무것도 없다 |
| 회귀 비용이 큰 작업 | 놓친 회귀의 비용이 검증에 드는 토큰·시간과 비대칭일 때, 게이트를 하나 더 두는 편이 싸다 |
| 감사 추적이 필요한 작업 | 모든 시도가 커밋으로 남는다. 인간용 이력을 어떻게 정리할지는 미정 |

| 쓰지 않는다 | 근거 |
| --- | --- |
| 단일 에이전트가 이미 안정적으로 해내는 태스크 (Next.js 스캐폴드, 단순 CRUD) | 조율 오버헤드가 이득을 갉아먹는다. 재작업도 회귀도 거의 없는 태스크에 게이트를 네 겹 두는 것은 비용만 남는다 |
| 서로 의존하거나 같은 파일을 건드리는 태스크 | 병렬로 돌리지 않는다. 의존성 그래프와 파일 결합도 두 신호로 순차/병렬을 가른다 |
| 채점 기준을 쓸 수 없는 작업 | Reviewer/Verifier의 pass/fail 기준이 없으면 4-role은 성립하지 않는다 (아래 "아직 정하지 않은 것") |

**경계선은 아직 없다.** "얼마나 어려워야 4-role을 쓰는가"의 임계값을 남의 벤치마크에서
빌려오지 않는다. 멀티에이전트 조율의 손익을 다룬 문헌이 있긴 하지만, 그 연구들이 재는 것은
과제 정확도이고 이 설계가 내세우는 것은 판단의 독립성이라 종속변수가 다르다. 게다가 배정
시점에는 "이 태스크의 난이도"를 아직 모른다. 그래서 경계선은 [로드맵](#로드맵)대로 이
저장소의 재작업률·회귀 발생률로 **직접 측정해서** 정한다. 그때까지 판단은 위의 반증 기준
하나뿐이다.

## 문서

| 문서 | 내용 |
| --- | --- |
| [design/](./design) | **Sigkill Foundry 블루프린트 (SDD 명세, 작성 중).** 편집 원본은 Claude 앱 문서이고 이 디렉토리는 사본이다 |
| [에이전트_레일_파이프라인.pdf](./에이전트_레일_파이프라인.pdf) | **RFC 읽기용 (26쪽).** GitHub이 바로 렌더하므로 여기부터 읽으면 된다. `build-pdf.sh`로 재생성하는 생성물이다 |
| [에이전트_레일_파이프라인.html](./에이전트_레일_파이프라인.html) | **RFC 원본.** 왜·언제·어떻게·얼마나에 대한 근거, 4-role 실행 흐름, 트레이드오프, 31건의 인용. GitHub은 저장소 안의 HTML을 렌더하지 않으므로 내려받아 브라우저로 연다 (180 KB · 자바스크립트 없음) |
| [diagrams/](./diagrams) | 다이어그램 **원본**. 8개는 Graphviz `.dot`, 태스크 시퀀스 1개는 mermaid `.mmd`다. `build-diagrams.py`가 SVG로 렌더해 HTML에 인라인한다 |
| [아키텍처.md](./아키텍처.md) | 실행 기반 설계. 단일 JVM 계층 구조와 수직확장 병목 대응. 아래 요약의 원본 |
| [Intelligent Machinery (1948)][im] · [전사본][im-tx] | 비정형 기계 · 규율과 자발성 인용 출처 (대조본: Copeland 편 『The Essential Turing』, Oxford 2004) |
| [On Computable Numbers (1936)][cn] · [전사본][cn-tx] | §6 보편 기계 · §11 결정문제 인용 출처 (같은 대조본) |

## 한눈에 보는 실행 기반

```
┌────────────────────────────────────────────────────────────────────────┐
│                     [ 단일 JVM 프로세스 (Java 25) ]                    │
│                                                                        │
│ ┌──────────────────────┐   ┌──────────────────────┐   ┌──────────────┐ │
│ │ 1. Pure Allocator    │ ─>│ 2. Embedded DB       │ ─>│ 3. UI Server │ │
│ │  (WatchService 감시) │   │  (상태/큐/캐시 관리) │   │  (Javalin)   │ │
│ └──────────┬───────────┘   └──────────────────────┘   └──────┬───────┘ │
│            │ (ProcessBuilder 격리 기동)                      │         │
│            ▼                                                 ▼         │
│ ┌──────────────────────────────────────────────────┐   ┌─────────────┐ │
│ │ 4. 외부 도구 레이어 (Claude Code CLI / Worktree) │   │ 5. 브라우저 │ │
│ │  - 독립 브랜치 및 1파일 1주제 자율 코딩 수행     │   │  (Vis.js)   │ │
│ └──────────────────────────┬───────────────────────┘   └─────────────┘ │
│                            │ (자동 영속화)                             │
│                            ▼                                           │
│ ┌────────────────────────────────────────────────────────────────────┐ │
│ │ 6. Git Repository (.git) — 진실의 원천                             │ │
│ └────────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘
```

## 실행 기반 요약 — [아키텍처.md](./아키텍처.md)

### 1. 핵심 내부 상태

`cache`(`ConcurrentHashMap`)는 내장 DB와 동기화되는 프롬프트 캐시로 중복 연산을 차단하고,
`finalPrompt`는 백로그 원문에 시스템 규칙과 행동 제약을 바인딩한 결과물이며, `taskContent` /
`agentId`는 단위 명세와 그것을 배정받는 에이전트의 식별 정보다.
→ [상세](./아키텍처.md#1-프로그램-핵심-변수-internal-states)

### 2. 사람이 제어하는 것

① 상위 기획 지시문으로 PM 모드를 깨우고 태스크 카드를 모니터링, ② *1파일 1주제* 격리 락
정책으로 충돌 범위 조율 — **사람이 태스크를 직접 `In Progress`로 옮기면 그 파일에 락이 걸려
에이전트가 배정되지 않는다**(상태 값 자체가 락이다), ③ 내장 DB·외부 연산 레이어의 동시 I/O
커넥션 상한 조정.
→ [상세](./아키텍처.md#2-사용자가-제어하는-가변-요소-user-control-points)

### 3. 시스템 계층

단일 JVM 안에서 **Pure Allocator**(`WatchService` + `ProcessBuilder`, 가상 스레드),
**Embedded DB**(SQLite/H2가 상태·큐·캐시 흡수), **CodeGraphAnalyzer**(`JavaParser` AST →
호출 관계 JSON), **Javalin + Vis.js 대시보드**가 맞물린다. 모든 변경은 Git과 내장 DB로 이중
영속화된다. → [상세](./아키텍처.md#3-시스템-계층-system-layers)

### 4. 실행 흐름

환경 구축(`install-tools.sh`) → PM 모드가 함수 단위까지 일감을 쪼개 `backlog/` 카드 생성 →
새 `todo` 감지 시 `git worktree`로 에이전트별 독립 디렉토리·브랜치 분기 → 파일 하나에 집중해
코딩·커밋 후 `done` 전환 → 정적 분석 결과를 대시보드 링크로 사람이 검증.
→ [상세](./아키텍처.md#4-시간-순서별-자율-워크플로우)

### 5. 단점과 해결책

| 단점 | 해결책 |
| --- | --- |
| 매 시도가 커밋으로 남아 인간용 로그 추적 불가 | 발자취는 Git이 전부 품고, 완료 시점에 정리 — **합칠지 남길지는 미정** (아래 "아직 정하지 않은 것") |
| 병렬 에이전트가 같은 파일·인덱스를 건드려 충돌 | **Worktree + 1태스크 1에이전트 1파일 1주제** — 물리 폴더 분리 |
| 상태·캐시를 디스크 마크다운으로 오가는 I/O 지연 | 고빈도 상태는 임베디드 DB, Git은 최종 영속화만 |

→ [상세](./아키텍처.md#5-단점과-해결책-trade-offs--solutions)

### 6. 디렉토리 구조

오케스트레이터는 별도 [구현 저장소][impl]에서 만든다. 패키지는 RFC 06절 컴포넌트명을 따르고,
`(예정)`이 없는 것만 실제로 있다. Board Watcher · Request Queue · Allocation Policy는 첫
마일스톤(단발 `run <taskId>`) 범위 밖이고, 계층 2~4(내장 DB · 정적 분석 · 대시보드)도 아직 설계로만 있다.

```text
agent-orchestrator/
├── backlog/                        # [상태 저장소] 마크다운 태스크 카드
└── src/main/java/com/coralstay/orchestrator/
    ├── Main.java · RunCommand.java # CLI 진입점 · (예정) run 흐름 배선
    ├── backlog/                    # backlog CLI 래퍼 — 태스크 판독
    ├── workspace/                  # 태스크별 git worktree · task/<id> 브랜치
    ├── spawn/                      # (예정) Agent Spawner
    ├── registry/                   # (예정) Session Registry
    └── ledger/                     # (예정) git-logbook 트레일러 판독
```

→ [상세](./아키텍처.md#6-프로젝트-디렉토리-구조)

### 7. 규칙의 소재지

규칙은 미들웨어가 아니라 **대상 프로젝트의 테스트 코드**(`ArchUnit` 레이어 검증, 컴플라이언스
게이트)에 산다. 할당자는 `gradlew test`의 Exit Code만 심사하고, 실패 시 에러 로그를 묶어
자가 치유를 명령한다. → [상세](./아키텍처.md#7-규칙의-소재지--미들웨어-vs-대상-프로젝트)

### 8. 수직확장 시 커널 병목

| 병목 | 격리 방안 |
| --- | --- |
| 수백 개 `fork/exec`의 컨텍스트 스위칭 | `taskset` / `cgroups`로 에이전트별 **CPU Affinity** 지정 |
| 동시 `gradlew test`의 디스크·저널링 락 대기 | 작업 공간을 **`tmpfs`(RAM 디스크)** 에 마운트 |
| 가상 스레드 Pinning으로 캐리어 스레드 고갈 | `jdk.virtualThreadScheduler.parallelism` / `maxPoolSize` 상한 설정 |

→ [상세](./아키텍처.md#8-수직확장scale-up-시-커널-병목과-해결책)

### 9. 수평확장 vs 수직확장

모든 작업 공간이 `tmpfs`에 있고 통신이 단일 JVM 메모리 버스 안에서 끝나면 Pod 간 gRPC/REST
오버헤드가 사라진다. 대가는 SPOF 리스크이며 베어메탈 이중화로 완화한다.
→ [상세](./아키텍처.md#9-수평확장pod-분산-vs-수직확장scale-up-평가)

## 로드맵

1. **Walking skeleton (다음 착수 지점)** — 4-role 전체가 아니라 Implementer 하나만 스폰 →
   작업 → 토큰 집계 → 회수(프로세스·자손 종료 + Registry 제거 — 헤드리스 세션은 종료가 곧
   컨텍스트 폐기라 `/clear` 단계가 없다). 아직 없는 채점 기준을 요구하지 않는 유일한 조각이면서
   Spawner·Registry·세마포어·토큰 측정을 한 번에 검증한다.
2. **실측 3종** — 헤드리스 세션 간 메시징 실동 여부, `backlog.md`의 의존성/마일스톤/상태 필드
   실제 지원 범위, `claude` 프로세스 peak RSS와 API 분당 한도. 진행 상태는
   [출처와 검증 상태](#출처와-검증-상태) 표에서만 갱신한다.
3. **경계선 측정** — walking skeleton이 태스크별 성공/실패와 재작업·회귀를 남기면, 어떤
   태스크에 4-role이 값을 하는지를 이 백로그의 실제 분포로 정할 수 있다.
4. **JVM 오케스트레이터** — Watcher / Queue / Policy / Spawner / Registry.
   이 설계에서 유일하게 처음부터 만들어야 하는 부분이다.
5. **`claude-rails` 역할 인식 확장** — 기존 훅을 role별로 분기.
6. **정적 분석 · 대시보드** — `JavaParser` 콜 그래프 → Javalin + Vis.js.

## 아직 정하지 않은 것

- **Reviewer의 pass/fail 기준과 Verifier·AC 판정 기준.** 개인 PKM 정리가 끝나기 전에는
  추측으로 채우지 않는다. 이 공백이 남아 있는 한 4-role 전체의 완료 기간은 추정 불가다.
- 조상 문서 로딩의 비대칭화(Reviewer/Logger가 요약+diff만 읽는 방안) — 열린 아이디어.
- 상태 개수와 전이 규칙의 최종 확정.
- **완료한 태스크 브랜치를 스쿼시할 것인가, 머지 커밋으로 남길 것인가.** 스쿼시는 커밋들을
  하나로 합쳐 `git log`에서 지우고, 머지 커밋은 그대로 남긴다. 계층 대응 덕에 **최소 커밋
  수는 카드의 AC 개수로 미리 세어진다**(커밋 = 함수). 남은 미지수는 **자가 치유 재시도
  배수**이고, 동시 실행 태스크 수만큼 곱해진다. 아는 제약은 하나 — 푸시해 공유된 커밋을
  스쿼시하면 해시가 바뀌어 받아간 쪽이 갈라진다는 것뿐이다. (기록 손실은 걱정하지 않는다:
  `Done` 전환 시 커밋을 읽어 태스크 카드에 기록하므로, 이력을 합쳐도 내용은 남는다.)
  [로드맵](#로드맵)의 walking skeleton이 남길 재시도 분포를 보고 정한다. ([상세](./아키텍처.md#5-단점과-해결책-trade-offs--solutions))

## 출처와 검증 상태

RFC 본문의 인용 원칙(DOI/arXiv가 붙은 것만 신뢰, 블로그발 수치는 원문 확인 후 삭제)을 이
README에도 적용한다. 검증이 진행되면 **이 표의 상태 칸만** 고친다.

| 인용 | 출처 | 상태 |
| --- | --- | --- |
| §6 보편 기계 · §11 결정문제 (1936) | [원문 스캔][cn] · [전사본][cn-tx] | ✅ 전사본 PDF 페이지 대조(§1 p.230 / §6 p.241 / §11 p.262) + Copeland 편 『The Essential Turing』(Oxford 2004) 수록 원문 재대조 |
| 비정형 기계 · 조건부 보편성 · 규율과 자발성 (1948) | [NPL 스캔][im] · [전사본][im-tx] | ✅ 『The Essential Turing』 수록 원문과 페이지 단위 대조 완료 (p.417 / p.423 / p.425 / p.431) |
| 그 외 31건의 인용 | [RFC 각주](./에이전트_레일_파이프라인.html) | RFC 10절 "인용 신뢰도에 대한 실용적 교훈" 참고 |
| 로드맵 2 실측 — `backlog.md` 의존성/마일스톤/상태 필드 지원 범위 | [RFC 04-0절 실측](./에이전트_레일_파이프라인.html) | ✅ backlog.md 1.51.0 실측(2026-10-03). `isReady`를 그대로 할당 조건으로 쓸 수 없다는 정정 포함 |
| 로드맵 2 실측 — 헤드리스 세션 간 메시징 · `claude` peak RSS · API 분당 한도 | — | ⏳ |

## 이 문서를 고치는 규칙

RFC 본문·링크·논문 검증이 계속 진행되므로 이 README도 자주 바뀐다. 매번 전체를 다시 쓰지
않도록 고치는 지점을 아래처럼 고정해둔다.

1. **원본은 하나다.** 수치·근거·인용의 원본은 RFC(`에이전트_레일_파이프라인.html`)이고,
   실행 기반 상세의 원본은 `아키텍처.md`다. README는 요약과 진입점일 뿐이며, 어긋나면 원본이
   맞다. 새 근거가 생기면 **원본을 먼저 고치고** 그다음 이 문서를 맞춘다.
2. **수치는 옮겨 적지 않는다.** README 본문에는 판단에 필요한 최소한만 남기고, 계수·p값·
   벤치마크 폭 같은 것은 RFC에 둔다. 새 수치를 README에 넣고 싶어지면 그건 RFC에 들어갈
   내용이다. **외부 문헌의 수치를 이 설계의 근거처럼 쓰지 않는다** — 종속변수가 같은지부터
   확인하고, 다르면 인용하지 않는다.
3. **링크는 문서 맨 아래 한 블록에서만 정의한다.** 본문은 `[표시][키]` 형태로만 쓴다. URL이
   바뀌면 아래 "링크" 블록 한 곳만 고치면 된다.
4. **검증 상태는 위 표에서만 관리한다.** 본문에 "확인됨/미확인"을 흩뿌리지 않는다.
   ⏳ → ✅ 전환은 그 표의 한 칸을 바꾸는 일이어야 한다.
5. **다이어그램은 `diagrams/`가 원본이다.** HTML 안의 `<svg>`를 직접 고치지 않는다.
   `.dot`(또는 시퀀스의 `.mmd`)을 고치고 `./build-diagrams.py`를 돌리면 `<!--dot:이름-->`
   마커 사이가 교체된다. 색은 소스에 센티넬 hex로 쓰고 빌드가 CSS 변수로 치환하므로,
   하나의 SVG가 문서의 라이트/다크 테마를 그대로 따른다.
   **표기 선택은 DOT 우선** — DOT으로 표현할 수 없는 것(시퀀스 등)만 mermaid로 쓴다.
   빌드 전제: `graphviz`(`dot`), 그리고 mermaid 렌더용 `npx` + 로컬 Chrome.
6. **PDF는 생성물이다.** `에이전트_레일_파이프라인.pdf`를 직접 고치지 않는다. 내용을 고친 뒤
   `./build-diagrams.py && ./build-pdf.sh`를 돌려 다시 만들고 같은 커밋에 함께 넣는다.
7. **구조 변경이 필요한 신호.** 같은 내용을 README와 원본 양쪽에서 고치고 있다면 그건 요약이
   너무 두꺼워진 것이다. 해당 절을 링크 한 줄로 접는다.

## 라이선스

[GNU AGPL-3.0](./LICENSE) — 문서와 아티팩트를 포함한 저장소 전체에 적용된다.

- **상용 라이선스 —** 저작권자가 단독이므로 듀얼 라이선스가 가능하다. AGPL 조건(네트워크
  서비스 제공 시 수정 소스 공개)이 맞지 않는 상용 사용은 별도 협의한다.
  문의: <coralstay3595@gmail.com> (또는 이 저장소의 GitHub Issue).
- **기여 —** 듀얼 라이선스 유지를 위해, 기여자는 자신의 기여를 AGPL-3.0과 상용 라이선스 양쪽으로
  배포할 권리를 저작권자에게 허여하는 데 동의한 것으로 본다.
- **이전 배포 —** 커밋 `a321868` 시점까지의 문서는 MIT로 배포되었고 그 스냅샷은 계속 MIT다.

---

## English Summary

**coralstay-software-factory** is the design repository for an *agent rail pipeline*: software
tasks decomposed into a `backlog.md` hierarchy (milestone · task · AC) and executed by role-based
agents — Implementer, Reviewer, Verifier, Logger — spawned and reclaimed as independent processes
by a JVM orchestrator. **It is an early draft: no implementation code, nothing measured yet.**

It began as one question: *why, when, how, and how much* should agent models be used? The answer
to *why* is the point of the whole design — **not throughput, but independence of judgment.**
Reviewer and Verifier must not inherit the Implementer's reasoning path, so context isolation
itself is used as a gate. Automation is not the goal, and attaching four roles to a single task is
never justified on speed.

Parallelism lives on the other layer and is measured rather than assumed. *Within* a task,
implementation is inherently sequential while judgment runs in parallel; *between* tasks, only
chains with a declared dependency or file coupling stay sequential. The dependency-plus-coupling
DAG is topologically sorted every scheduling round to yield its **length** (critical path — the
floor no added capacity removes) and its **width** (how many tasks can be admitted at once,
approximated per topological level, exactly via a maximum antichain). Width is the ceiling that
matters: real concurrency is `min(width, resource limit)`, and both numbers are logged so the
value of parallelising this backlog can be checked afterwards rather than asserted.

Turing's vocabulary fits this exactly. In [*Intelligent Machinery*][im] (1948) he called machines
"largely random in their construction" **unorganised machines** — an LLM is one — and split the
conditions for intelligence in two: "To convert a brain or machine into a universal machine is the
extremest form of discipline. But discipline is certainly not enough in itself to produce
intelligence. That which is required in addition we call initiative." The rails are the
discipline; the agent is the initiative. The real design question is therefore not *how much to
automate* but *how far to lay the rails*. On the judging side, [*On Computable Numbers*][cn]
(1936) already drew the boundary — "Hence the Entscheidungsproblem cannot be solved" (§11): there
is no *general* decision procedure, only the finite, per-project one you write yourself, which is
what a test gate is. **Turing supplies the vocabulary and the framing here, not the evidence.**

No threshold is borrowed from outside. Work on when multi-agent orchestration pays off measures
task accuracy, whereas this design claims independence of judgment — a different dependent
variable — and the difficulty of a task is not known at dispatch time anyway. So the boundary is
to be measured here, from this repository's own rework and regression rates. Until then the only
rule is the falsifiable stopping criterion: if four roles do not measurably reduce rework and
regressions against a single Implementer with self-review, the roles collapse back into one
session. What remains deliberately unfilled is the Reviewer/Verifier scoring criteria; they will
not be guessed at.

See [에이전트_레일_파이프라인.html](./에이전트_레일_파이프라인.html) for the RFC and
[아키텍처.md](./아키텍처.md) for the execution substrate (both Korean). Licensed under
[AGPL-3.0](./LICENSE); commercial licensing available on request —
<coralstay3595@gmail.com> or a GitHub issue.

---

## 링크

<!-- 본문의 모든 외부 링크는 여기서만 정의한다. URL이 바뀌면 이 블록만 고친다. -->

[cn]: https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf
[cn-tx]: http://www.cs.ox.ac.uk/activities/ieg/e-library/sources/tp2-ie.pdf
[im]: https://www.npl.co.uk/getattachment/84156b8e-1b00-45b7-9f5e-3179cfa458c5/80916595-Intelligent-Machinery.pdf?lang=en-US
[im-tx]: https://www.info2007.net/docs/intelligent-machinery-alan-turing.html
[impl]: https://github.com/coralstay/agent-orchestrator
