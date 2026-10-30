<!-- work-order-hash: 46485bf07d0c5c8562974855dcc740537e58cc99646e3d96c3519ca6935fe803 -->
# 작업 순서

`work_order.py`가 backlog/tasks의 의존(`dependencies`)으로 만든 파일이다 — 직접 고치지 말고 다시 생성한다. 같은 단계의 태스크는 병렬로, 단계는 위에서 아래로 순차로 진행한다. Done 태스크와 없는 태스크에 대한 의존은 충족된 것으로 본다.

| 단계 | ID | 제목 |
|---|---|---|
| 1 | TASK-19 | 충돌 결정 A1~A6 · C2를 설계 문서에 반영한다(착수 = task 브랜치, 승인 · 작업 순서 게이트 시점, (수동) DoD, 커밋 메시지 태스크 ID) |
| 2 | TASK-20 | coding-agent-git-commit-tool 서술을 코드에 맞춘다(AI-Agent 트레일러 · 훅 하나 · 형식 규칙) |
| 3 | TASK-21 | agent-orchestrator 서술을 코드에 맞춘다(완료 기록 · 회수 · 배정 조건 · --plain 판독 · 구성 표) |
