#!/usr/bin/env python3
"""Build the SOP library into one self-contained HTML page.

Usage:
  python3 build/build.py                 # render dist/sop-library.html
  python3 build/build.py --check         # validate front matter, headings, links, index
  python3 build/build.py --write-index   # regenerate the index block in README.md
  python3 build/build.py --write-sources # regenerate SOURCES.md
  python3 build/build.py --out PATH      # alternative output path

Requires: python-markdown, pyyaml (both present on this machine).
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import sys
from pathlib import Path

import markdown
import yaml
from markdown.extensions.toc import slugify as md_slugify

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"

SECTIONS = [
    ("00-foundations", "Foundations"),
    ("10-onboarding", "Onboarding — CCM1 to CCM4"),
    ("20-ongoing-service", "Ongoing service — CCM5 and service standards"),
    ("30-advanced-planning", "Advanced planning and the expert network"),
    ("40-family-layer", "Family layer — Mode A"),
    ("50-growth-inside-service", "Growth inside service"),
    ("60-practice-ops", "Practice operations"),
    ("70-team-building", "Team building"),
    ("templates", "Templates"),
]
SECTION_TITLE = dict(SECTIONS)

REQUIRED_KEYS = ["id", "title", "type", "section", "owner", "modes", "source", "extension", "status", "updated"]
REQUIRED_H2 = {
    "procedure": ["Purpose", "Trigger", "Roles", "Timing", "Inputs", "Prep checklist", "Procedure",
                  "Follow-up", "Outputs and records", "Do / Don't", "Metrics", "Related", "Source"],
    "spec": ["Purpose", "Contents", "Standards", "Refresh cadence", "Owner", "Related", "Source"],
    "reference": ["Purpose", "Related", "Source"],
    "template": ["Purpose", "How to use", "Related", "Source"],
}
MODE_H2 = "Mode A / Mode B"
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
H2_RE = re.compile(r"^## +(.+?)\s*$", re.M)
LINK_RE = re.compile(r"\]\(([^)\s]+?\.md)(#[^)\s]*)?\)")
PLACEHOLDER_RE = re.compile(r"\[([A-Z][A-Za-z0-9 .&'/-]{0,40})\](?![\(\[])")
INDEX_START, INDEX_END = "<!-- index:start -->", "<!-- index:end -->"
PAGE_TITLE = "The Family CFO Playbook"


class Doc:
    def __init__(self, path: Path, meta: dict, body: str):
        self.path = path
        self.meta = meta
        self.body = body

    @property
    def id(self) -> str:
        return str(self.meta.get("id", ""))

    @property
    def section(self) -> str:
        return self.path.parent.name

    @property
    def title(self) -> str:
        return str(self.meta.get("title", self.path.stem))

    @property
    def type(self) -> str:
        return str(self.meta.get("type", ""))

    @property
    def modes(self) -> list:
        m = self.meta.get("modes") or []
        return [str(x) for x in m]

    @property
    def rel(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


def load_docs() -> list[Doc]:
    docs: list[Doc] = []
    for dirname, _ in SECTIONS:
        d = ROOT / dirname
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            text = p.read_text(encoding="utf-8")
            m = FM_RE.match(text)
            if not m:
                docs.append(Doc(p, {}, text))
                continue
            try:
                meta = yaml.safe_load(m.group(1)) or {}
            except yaml.YAMLError as e:  # pragma: no cover
                meta = {"_yaml_error": str(e)}
            docs.append(Doc(p, meta, text[m.end():]))
    return docs


def resolve_link(doc: Doc, target: str) -> Path:
    return (doc.path.parent / target).resolve()


# ---------------------------------------------------------------- check

def check(docs: list[Doc]) -> list[str]:
    errors: list[str] = []
    by_path = {d.path.resolve(): d for d in docs}
    ids: dict[str, str] = {}
    for d in docs:
        where = d.rel
        if "_yaml_error" in d.meta:
            errors.append(f"{where}: front matter YAML error: {d.meta['_yaml_error']}")
            continue
        if not d.meta:
            errors.append(f"{where}: missing front matter")
            continue
        for k in REQUIRED_KEYS:
            if k not in d.meta:
                errors.append(f"{where}: front matter missing '{k}'")
        if d.id in ids:
            errors.append(f"{where}: duplicate id {d.id} (also {ids[d.id]})")
        ids[d.id] = where
        expected_prefix = "t-" if d.section == "templates" else "sop-"
        if d.id and not d.id.startswith(expected_prefix):
            errors.append(f"{where}: id '{d.id}' should start with '{expected_prefix}'")
        if d.meta.get("section") and d.meta["section"] != d.section:
            errors.append(f"{where}: front matter section '{d.meta['section']}' != folder '{d.section}'")
        if d.type not in REQUIRED_H2:
            errors.append(f"{where}: unknown type '{d.type}'")
        else:
            h2s = [h.strip() for h in H2_RE.findall(d.body)]
            for h in REQUIRED_H2[d.type]:
                if h not in h2s:
                    errors.append(f"{where}: missing required heading '## {h}'")
            if d.type in ("procedure", "spec") and {"A", "B"} <= set(d.modes) and MODE_H2 not in h2s:
                errors.append(f"{where}: modes [A, B] but no '## {MODE_H2}' section")
        if "!!! extension" in d.body and not d.meta.get("extension") and "Extension" not in d.body.split("## Source")[-1]:
            errors.append(f"{where}: uses an extension callout but front matter extension=false and Source has no 'Extension' line")
        for target, _frag in LINK_RE.findall(d.body):
            if resolve_link(d, target) not in by_path:
                errors.append(f"{where}: broken link -> {target}")
    # README index freshness
    readme = (ROOT / "README.md")
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        if INDEX_START in text and INDEX_END in text:
            current = text.split(INDEX_START)[1].split(INDEX_END)[0].strip()
            if current != index_block(docs).strip():
                errors.append("README.md: index block is stale — run build.py --write-index")
        else:
            errors.append("README.md: index markers missing")
    return errors


# ---------------------------------------------------------------- index / sources

def index_block(docs: list[Doc]) -> str:
    lines: list[str] = []
    for dirname, title in SECTIONS:
        group = [d for d in docs if d.section == dirname]
        if not group:
            continue
        lines.append(f"**{title}**\n")
        lines.append("| # | Document | Type | Modes | Owner |")
        lines.append("|---|---|---|---|---|")
        for d in group:
            num = d.id.split("-")[-1]
            modes = ", ".join(d.modes) or "—"
            ext = " · beyond Bowen" if d.meta.get("extension") else ""
            lines.append(f"| {num} | [{d.title}]({d.rel}) | {d.type}{ext} | {modes} | {d.meta.get('owner','')} |")
        lines.append("")
    return "\n".join(lines)


def write_index(docs: list[Doc]) -> None:
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    pre, rest = text.split(INDEX_START)
    _, post = rest.split(INDEX_END)
    readme.write_text(f"{pre}{INDEX_START}\n{index_block(docs)}\n{INDEX_END}{post}", encoding="utf-8")


def sources_table(docs: list[Doc]) -> str:
    def fmt(v):
        if not v:
            return "—"
        if isinstance(v, list):
            return "<br>".join(html.escape(str(x)) for x in v)
        return html.escape(str(v))
    lines = ["| # | Document | Type | Beyond Bowen | Bowen | Hughes | Other |", "|---|---|---|---|---|---|---|"]
    for d in docs:
        src = d.meta.get("source") or {}
        ext = "yes" if d.meta.get("extension") else ""
        lines.append(f"| {d.id} | [{d.title}]({d.rel}) | {d.type} | {ext} | {fmt(src.get('bowen'))} | {fmt(src.get('hughes'))} | {fmt(src.get('other'))} |")
    return "\n".join(lines)


def write_sources(docs: list[Doc]) -> None:
    head = ("# Sources — traceability\n\n"
            "Generated by `build/build.py --write-sources` from each document's front matter. "
            "Bowen = *Breaking Through* (CEG Worldwide, 2008). Hughes = *Family Wealth* (2004), *Complete Family Wealth* (2018), "
            "*Family: The Compact Among Generations* (2007), Goldstone/Hughes/Whitaker *Family Trusts* (2016). "
            "Other = Palaveev *The Ensemble Practice* (2012), Bonner & Bonner *Family Fortunes* (2012), or our own extensions. "
            "All content is paraphrased and adapted; no source text is reproduced.\n\n")
    (ROOT / "SOURCES.md").write_text(head + sources_table(docs) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- render

def make_md(doc_id: str) -> markdown.Markdown:
    def slug(value, sep):
        return f"{doc_id}-{md_slugify(value, sep)}"
    return markdown.Markdown(extensions=["tables", "toc", "fenced_code", "attr_list", "def_list", "admonition", "sane_lists"],
                             extension_configs={"toc": {"slugify": slug, "toc_depth": "2-3"}})


def render_body(doc: Doc, path_to_id: dict[Path, str], doc_id: str) -> str:
    body = PLACEHOLDER_RE.sub(r'<span class="ph">[\1]</span>', doc.body)
    body = re.sub(r"^# .*\n", "", body, count=1, flags=re.M)  # H1 is rendered from the meta
    out = make_md(doc_id).convert(body)

    def rewrite(m):
        href = m.group(1)
        target, _, frag = href.partition("#")
        if target.endswith(".md"):
            tid = path_to_id.get(resolve_link(doc, target))
            if tid:
                return f'href="#{tid}{"-" + frag if frag else ""}"'
        return m.group(0)
    return re.sub(r'href="([^"]+)"', rewrite, out)


def meta_bar(d: Doc) -> str:
    src = d.meta.get("source") or {}
    bits = []
    for key, label in (("bowen", "Bowen"), ("hughes", "Hughes"), ("other", "Other")):
        v = src.get(key)
        if v:
            bits.append(f"<b>{label}:</b> " + html.escape("; ".join(str(x) for x in v) if isinstance(v, list) else str(v)))
    ext = '<span class="badge ext">beyond Bowen</span>' if d.meta.get("extension") else ""
    modes = "".join(f'<span class="badge mode">Mode {m}</span>' for m in d.modes)
    return (f'<div class="meta"><span class="badge type {html.escape(d.type)}">{html.escape(d.type)}</span>'
            f'<span class="badge">Owner: {html.escape(str(d.meta.get("owner","")))}</span>{modes}{ext}'
            f'<span class="badge">Updated {html.escape(str(d.meta.get("updated","")))}</span>'
            f'<div class="src">{" · ".join(bits)}</div></div>')


def sidebar(docs: list[Doc]) -> str:
    out = ['<nav class="side" aria-label="Contents">', '<a class="brand" href="#overview">Overview</a>']
    for dirname, title in SECTIONS:
        group = [d for d in docs if d.section == dirname]
        if not group:
            continue
        out.append(f'<details open><summary>{html.escape(title)}</summary><ul>')
        for d in group:
            num = d.id.split("-")[-1]
            out.append(f'<li><a href="#{d.id}"><span class="num">{html.escape(num)}</span>{html.escape(d.title)}</a></li>')
        out.append("</ul></details>")
    out.append('<a class="brand" href="#sources">Sources</a></nav>')
    return "\n".join(out)


def build_page(docs: list[Doc]) -> str:
    path_to_id = {d.path.resolve(): d.id for d in docs}
    css = (BUILD / "style.css").read_text(encoding="utf-8")
    svg = (BUILD / "process-map.svg").read_text(encoding="utf-8") if (BUILD / "process-map.svg").exists() else ""
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_text = re.sub(r"<!-- ghonly:start -->.*?<!-- ghonly:end -->", "", readme_text, flags=re.S)
    readme_doc = Doc(ROOT / "README.md", {"id": "overview"}, readme_text)
    readme_html = render_body(readme_doc, path_to_id, "overview")
    parts = [f"<title>{PAGE_TITLE}</title>",
             '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Source+Sans+3:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">',
             f"<style>{css}</style>",
             '<header class="top"><div><h1>' + PAGE_TITLE + '</h1>'
             '<p class="sub">Operating procedures for a practice that serves families with $30M to several hundred million as their personal chief financial officer — the consultative process, the family layer, and the team that delivers it.</p></div>'
             f'<div class="legend"><span class="badge type procedure">procedure</span><span class="badge type spec">spec</span>'
             f'<span class="badge type reference">reference</span><span class="badge type template">template</span>'
             f'<span class="badge mode">Mode A/B</span><span class="badge ext">beyond Bowen</span>'
             f'<span class="ph">[Placeholder]</span></div></header>',
             '<div class="layout">', sidebar(docs), "<main>",
             f'<section id="overview" class="doc"><h2 class="sec">Overview</h2><figure class="map">{svg}</figure>{readme_html}</section>']
    for dirname, title in SECTIONS:
        group = [d for d in docs if d.section == dirname]
        if not group:
            continue
        parts.append(f'<section id="sec-{dirname}"><h2 class="sec">{html.escape(title)}</h2>')
        for d in group:
            num = d.id.split("-")[-1]
            parts.append(f'<article id="{d.id}" class="doc {html.escape(d.type)}"><h1><span class="num">{html.escape(num)}</span> {html.escape(d.title)}</h1>'
                         f'{meta_bar(d)}{render_body(d, path_to_id, d.id)}</article>')
        parts.append("</section>")
    sources_html = make_md("sources").convert(sources_table(docs))
    sources_html = re.sub(r'href="([^"]+\.md)"', lambda m: f'href="#{path_to_id.get((ROOT / m.group(1)).resolve(), "")}"', sources_html)
    parts.append(f'<section id="sources"><h2 class="sec">Sources — traceability</h2>{sources_html}</section>')
    parts.append(f'<footer>Built {dt.date.today().isoformat()} · {len(docs)} documents · all source material paraphrased and adapted</footer>')
    parts.append("</main></div>")
    parts.append("""<script>
(function(){var links=[].slice.call(document.querySelectorAll('nav.side a[href^="#"]'));var map={};links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a;});
if(!('IntersectionObserver' in window))return;var obs=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){links.forEach(function(a){a.classList.remove('active')});var a=map[e.target.id];if(a){a.classList.add('active');}}});},{rootMargin:'-10% 0px -80% 0px'});
document.querySelectorAll('article.doc, section#overview, section#sources').forEach(function(el){obs.observe(el);});})();
</script>""")
    return "\n".join(parts)


# ---------------------------------------------------------------- main

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write-index", action="store_true")
    ap.add_argument("--write-sources", action="store_true")
    ap.add_argument("--out", default=str(ROOT / "dist" / "sop-library.html"))
    args = ap.parse_args(argv)
    docs = load_docs()
    if args.write_index:
        write_index(docs)
        print("README.md index block regenerated")
    if args.write_sources:
        write_sources(docs)
        print("SOURCES.md regenerated")
    if args.check:
        errs = check(docs)
        for e in errs:
            print("ERROR", e)
        print(f"{len(docs)} documents checked, {len(errs)} error(s)")
        return 1 if errs else 0
    if not (args.write_index or args.write_sources) or args.out != ap.get_default("out"):
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build_page(docs), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out} ({out.stat().st_size // 1024} KB, {len(docs)} documents)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
