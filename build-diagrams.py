#!/usr/bin/env python3
"""diagrams/*.dot → SVG 렌더 후 HTML에 인라인 주입.

원본은 diagrams/ 안의 .dot(그리고 시퀀스 하나는 .mmd)이고, HTML 속 SVG는 생성물이다.
다이어그램을 고치려면 .dot을 고치고 이 스크립트를 다시 돌린다.

색은 .dot에 센티넬 hex로 적고 여기서 CSS 변수로 치환한다 — 그래야 하나의 SVG가
문서의 라이트/다크 테마를 그대로 따라간다.
"""
import io, os, re, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).parent
HTML = ROOT / "에이전트_레일_파이프라인.html"
DIA = ROOT / "diagrams"

TOKENS = {
    "#f00001": "var(--diagram-ink)",     "#f00002": "var(--diagram-muted)",
    "#f00003": "var(--diagram-line)",    "#f00004": "var(--diagram-surface)",
    "#f00005": "var(--diagram-surface-2)", "#f00006": "var(--diagram-accent)",
    "#f00007": "var(--diagram-accent-bg)", "#f00008": "var(--diagram-accent-ink)",
    "#f00009": "var(--diagram-impl)",    "#f0000a": "var(--diagram-impl-bg)",
    "#f0000b": "var(--diagram-review)",  "#f0000c": "var(--diagram-review-bg)",
    "#f0000d": "var(--diagram-verify)",  "#f0000e": "var(--diagram-verify-bg)",
    "#f0000f": "var(--diagram-logger)",  "#f00010": "var(--diagram-logger-bg)",
}
# mermaid가 렌더해 둔 SVG(시퀀스)는 자기 팔레트를 하드코딩한다 — 같은 방식으로 토큰화한다.
MERMAID_TOKENS = {
    "#262b34": "var(--diagram-ink)",      "#000000": "var(--diagram-ink)",
    "#f2f3f5": "var(--diagram-surface)",  "#eaeaea": "var(--diagram-surface-2)",
    "#9aa4b8": "var(--diagram-line)",     "#a8adb8": "var(--diagram-muted)",
    "#edf2ae": "var(--diagram-accent-bg)", "#fff5ad": "var(--diagram-accent-bg)",
    "#575247": "var(--diagram-muted)",
}
FONT = '"IBM Plex Sans", ui-sans-serif, system-ui, sans-serif'


def clean_svg(svg: str, name: str, mermaid: bool = False) -> str:
    svg = re.sub(r"<\?xml[^>]*\?>\s*", "", svg)
    svg = re.sub(r"<!DOCTYPE[^>]*>\s*", "", svg, flags=re.S)
    svg = re.sub(r"<!--.*?-->\s*", "", svg, flags=re.S)
    # 루트 svg: 고정 width/height 제거 → 컨테이너 폭에 맞춰 축소
    def fix_root(m):
        tag = m.group(0)
        tag = re.sub(r'\s(width|height)="[^"]*"', "", tag)
        tag = tag.replace("<svg", f'<svg class="dot-diagram" role="img" '
                                  f'aria-label="{name}" style="max-width:100%;height:auto"', 1)
        return tag
    svg = re.sub(r"<svg\b[^>]*>", fix_root, svg, count=1)
    # Graphviz가 깔아두는 배경 폴리곤 제거(투명 배경이라 white가 남는 경우 대비)
    svg = re.sub(r'<polygon fill="white"[^/]*/>\s*', "", svg)
    # 센티넬을 먼저 치환하고, mermaid 기본 팔레트가 남아 있으면 그것도 토큰으로 바꾼다.
    for table in (TOKENS, MERMAID_TOKENS):
        for sentinel, var in table.items():
            svg = svg.replace(sentinel, var).replace(sentinel.upper(), var)
    if not mermaid:
        svg = re.sub(r'font-family="[^"]*"', f"font-family='{FONT}'", svg)
    return svg.strip()


def render_mmd(path: pathlib.Path) -> str:
    """mermaid 소스를 mermaid-cli로 렌더한다.

    색은 diagrams/mermaid-theme.json이 .dot과 같은 센티넬 hex로 지정하므로,
    렌더 결과에 같은 TOKENS 치환이 그대로 먹는다.
    """
    svg_out = path.with_suffix(".svg")
    cmd = [
        "npx", "-y", "@mermaid-js/mermaid-cli@11",
        "-i", str(path), "-o", str(svg_out),
        "-c", str(DIA / "mermaid-theme.json"), "-b", "transparent",
    ]
    env = dict(os.environ)
    env.setdefault("PUPPETEER_EXECUTABLE_PATH",
                   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    print(f"  {path.stem}: mermaid-cli 렌더 중…")
    r = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if r.returncode:
        if svg_out.exists():
            print(f"    ! mermaid-cli 실패 — 기존 {svg_out.name}을 그대로 쓴다\n"
                  f"      {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else ''}")
            return clean_svg(io.open(svg_out, encoding="utf-8").read(), path.stem)
        sys.exit(f"mermaid-cli 실패, 대체할 SVG도 없다: {path}\n{r.stderr}")
    return clean_svg(io.open(svg_out, encoding="utf-8").read(), path.stem)


def render_dot(path: pathlib.Path) -> str:
    out = subprocess.run(["dot", "-Tsvg", str(path)], capture_output=True, text=True)
    if out.returncode:
        sys.exit(f"dot 실패: {path}\n{out.stderr}")
    return clean_svg(out.stdout, path.stem)


def main() -> None:
    html = io.open(HTML, encoding="utf-8").read()
    injected = 0
    for marker in sorted(set(re.findall(r"<!--dot:([a-z0-9-]+)-->", html))):
        dot_path, mmd_path = DIA / f"{marker}.dot", DIA / f"{marker}.mmd"
        if dot_path.exists():
            svg = render_dot(dot_path)
        elif mmd_path.exists():  # DOT에 대응물이 없는 것(시퀀스 등)만 mermaid
            svg = render_mmd(mmd_path)
        else:
            sys.exit(f"소스 없음: {dot_path} 도 {mmd_path} 도 없다")
        block = re.compile(
            rf"(<!--dot:{re.escape(marker)}-->).*?(<!--/dot:{re.escape(marker)}-->)", re.S
        )
        html, n = block.subn(lambda m: f"{m.group(1)}\n{svg}\n{m.group(2)}", html)
        injected += n
        print(f"  {marker}: {n}곳 주입 ({len(svg):,} bytes)")
    io.open(HTML, "w", encoding="utf-8").write(html)
    print(f"완료 — 다이어그램 {injected}개, HTML {len(html):,} bytes")


if __name__ == "__main__":
    main()
