#!/usr/bin/env python3
"""Assemble the primer from guide/parts/*.html into dist/family-cfo-primer.html."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parent.parent
PARTS = ROOT / "guide" / "parts"
OUT = ROOT / "dist" / "family-cfo-primer.html"
PLAYBOOK = "https://claude.ai/code/artifact/2890b4bc-3b5a-4a3b-830f-eb49c8d295c7"

CSS = """
:root{
  --ground:#eceae5;--s0:#f8f7f4;--s1:#f3f1ed;--s2:#e5e2db;--s3:#dbd7ce;
  --ink:#1c2120;--muted:#5e6663;--faint:#8a918d;--line:#d2cec5;--line-soft:#e0dcd4;
  --accent:#155e63;--accent-ink:#ffffff;--accent-soft:#d9e8e8;
  --mark:#9c5326;--mark-soft:#f0e3d8;
  --pip-off:#c9c4ba;
  --f-disp:"Instrument Serif","Iowan Old Style",Georgia,serif;
  --f-body:"Newsreader","Iowan Old Style",Georgia,serif;
  --f-ui:"Archivo","Helvetica Neue",Arial,sans-serif;
  --shadow:0 1px 2px rgba(28,33,32,.06),0 6px 18px rgba(28,33,32,.05);
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#14171a;--s0:#1b1f22;--s1:#202528;--s2:#282e31;--s3:#31383b;
  --ink:#e9e8e3;--muted:#a2aba7;--faint:#7d8783;--line:#333b3e;--line-soft:#2a3134;
  --accent:#74c3c7;--accent-ink:#0e1c1d;--accent-soft:#1a2f31;
  --mark:#dd9a68;--mark-soft:#33251a;
  --pip-off:#414a4d;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 6px 18px rgba(0,0,0,.22);
}}
:root[data-theme="dark"]{
  --ground:#14171a;--s0:#1b1f22;--s1:#202528;--s2:#282e31;--s3:#31383b;
  --ink:#e9e8e3;--muted:#a2aba7;--faint:#7d8783;--line:#333b3e;--line-soft:#2a3134;
  --accent:#74c3c7;--accent-ink:#0e1c1d;--accent-soft:#1a2f31;
  --mark:#dd9a68;--mark-soft:#33251a;
  --pip-off:#414a4d;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 6px 18px rgba(0,0,0,.22);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:96px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{animation:none!important;transition:none!important}}
body{margin:0;background:var(--ground);color:var(--ink);font:18px/1.62 var(--f-body);-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-underline-offset:2px}
a:focus-visible,summary:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:3px}

/* ---------- masthead ---------- */
.mast{padding:clamp(32px,6vw,72px) clamp(20px,5vw,64px) 30px;border-bottom:1px solid var(--line);background:var(--s0)}
.mast-in{max-width:1030px;margin:0 auto;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:20px 56px;align-items:end}
@media (max-width:820px){.mast-in{grid-template-columns:1fr}}
.kicker{font:500 .72rem/1 var(--f-ui);letter-spacing:.2em;text-transform:uppercase;color:var(--mark);margin:0 0 18px}
.mast h1{font:400 clamp(2.6rem,6vw,4.4rem)/.98 var(--f-disp);margin:0;letter-spacing:-.015em;text-wrap:balance}
.mast .stand{font:400 clamp(1.05rem,2vw,1.3rem)/1.5 var(--f-body);color:var(--muted);margin:18px 0 0;max-width:56ch}
.mast .stand em{color:var(--ink);font-style:italic}
.glance{border-left:1px solid var(--line);padding-left:26px}
.glance h2{font:500 .68rem/1 var(--f-ui);letter-spacing:.16em;text-transform:uppercase;color:var(--faint);margin:0 0 12px}
.glance ol{list-style:none;margin:0;padding:0;columns:2;column-gap:26px;font:400 .86rem/1.75 var(--f-ui)}
.glance li{break-inside:avoid}
.glance a{color:var(--muted);text-decoration:none;display:block}
.glance a:hover{color:var(--accent)}
.glance b{color:var(--faint);font-weight:500;font-variant-numeric:tabular-nums;margin-right:7px}
@media (max-width:820px){.glance{border-left:0;padding-left:0;border-top:1px solid var(--line);padding-top:20px}}

/* ---------- depth control ---------- */
.rail{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--ground) 88%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.rail-in{max-width:1030px;margin:0 auto;padding:10px clamp(20px,5vw,64px);display:flex;gap:18px 22px;align-items:center;justify-content:space-between}
@media (max-width:1080px){nav.chapters{display:none}}
.depth{display:flex;align-items:center;gap:10px}
.depth-lbl{font:500 .68rem/1 var(--f-ui);letter-spacing:.14em;text-transform:uppercase;color:var(--faint)}
.depth-btns{display:flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;background:var(--s0)}
.depth-btns button{appearance:none;border:0;background:none;color:var(--muted);font:500 .78rem/1 var(--f-ui);padding:8px 14px;cursor:pointer;white-space:nowrap;border-right:1px solid var(--line-soft)}
.depth-btns button:last-child{border-right:0}
.depth-btns button[aria-pressed="true"]{background:var(--accent);color:var(--accent-ink)}
.depth-btns button:hover:not([aria-pressed="true"]){background:var(--s2);color:var(--ink)}
nav.chapters{display:flex;gap:2px;overflow-x:auto;scrollbar-width:none;-ms-overflow-style:none;max-width:100%;-webkit-mask-image:linear-gradient(to right,#000 calc(100% - 28px),transparent);mask-image:linear-gradient(to right,#000 calc(100% - 28px),transparent)}
nav.chapters::-webkit-scrollbar{display:none}
nav.chapters a{font:500 .76rem/1 var(--f-ui);color:var(--muted);text-decoration:none;padding:7px 9px;border-radius:5px;white-space:nowrap}
nav.chapters a:hover{background:var(--s2);color:var(--ink)}
nav.chapters a.on{color:var(--accent);background:var(--accent-soft)}

/* ---------- layout ---------- */
main{max-width:1030px;margin:0 auto;padding:0 clamp(20px,5vw,64px) 120px}
.chapter{padding:clamp(44px,7vw,86px) 0 10px;border-top:1px solid var(--line-soft)}
.chapter:first-of-type{border-top:0}
.ch-head{display:grid;grid-template-columns:minmax(0,1fr);gap:6px;margin:0 0 34px;max-width:78ch}
.eyebrow{font:500 .7rem/1 var(--f-ui);letter-spacing:.18em;text-transform:uppercase;color:var(--mark);margin:0}
.ch-head h2{font:400 clamp(1.9rem,3.6vw,2.7rem)/1.08 var(--f-disp);margin:6px 0 0;letter-spacing:-.01em;text-wrap:balance}
.lede{font-size:1.08rem;color:var(--muted);margin:12px 0 0;max-width:62ch}
.cards{display:grid;gap:16px}

/* ---------- card = depth 1 ---------- */
.card{background:var(--s0);border:1px solid var(--line);border-radius:12px;padding:24px 26px 8px;box-shadow:var(--shadow)}
.card-t{font:600 1.16rem/1.35 var(--f-body);margin:0;letter-spacing:-.005em;text-wrap:balance;max-width:60ch}
.essence{margin:8px 0 4px;color:var(--muted);max-width:70ch;font-size:1.02rem}
.card .num{font:500 .72rem/1 var(--f-ui);color:var(--faint);letter-spacing:.1em;display:block;margin:0 0 8px}

/* ---------- layers ---------- */
details.layer{margin:12px -26px 0;border-top:1px solid var(--line-soft)}
details.layer>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:10px;padding:12px 26px;font:500 .74rem/1 var(--f-ui);letter-spacing:.1em;text-transform:uppercase;color:var(--faint)}
details.layer>summary::-webkit-details-marker{display:none}
details.layer>summary:hover{color:var(--ink)}
details.layer>summary .chev{width:9px;height:9px;border-right:1.6px solid currentColor;border-bottom:1.6px solid currentColor;transform:rotate(45deg);transition:transform .18s ease;margin-top:-4px}
details.layer[open]>summary .chev{transform:rotate(225deg);margin-top:2px}
details.layer>summary .pips{margin-left:auto;display:flex;gap:4px}
details.layer>summary .pips i{width:6px;height:6px;border-radius:50%;background:var(--pip-off);display:block}
details.layer>summary .pips i.on{background:var(--accent)}
.layer-body{padding:2px 26px 20px;font-size:1rem}
.layer-body>*:first-child{margin-top:0}
.layer-body p{max-width:70ch}
.layer-body ul,.layer-body ol{max-width:64ch;padding-left:1.15em}
.layer-body li{margin:5px 0}
details.l2{background:var(--s1)}
details.l2>.layer-body{background:var(--s1)}
details.l3{margin:14px 0 0;border:1px solid var(--line-soft);border-radius:9px;background:var(--s2);overflow:hidden}
details.l3>summary{padding:11px 18px;color:var(--mark)}
details.l3>.layer-body{padding:0 18px 16px;background:var(--s2)}
details.l3 .pips i.on{background:var(--mark)}
.card>details.layer:last-child{border-radius:0 0 12px 12px;overflow:hidden}

/* ---------- inner furniture ---------- */
.sop{margin:14px 0 0;padding-top:10px;border-top:1px dashed var(--line);font:500 .82rem/1.5 var(--f-ui)}
.sop a{text-decoration:none;border-bottom:1px solid var(--accent-soft)}
.sop::before{content:"↳ ";color:var(--faint)}
.pull{margin:16px 0;padding:14px 18px;border-left:3px solid var(--accent);background:var(--accent-soft);border-radius:0 8px 8px 0;font-size:.98rem}
.pull.warn{border-left-color:var(--mark);background:var(--mark-soft)}
.pull p{margin:0}
.pull .lbl{display:block;font:500 .68rem/1 var(--f-ui);letter-spacing:.14em;text-transform:uppercase;color:var(--mark);margin:0 0 6px}
.pull:not(.warn) .lbl{color:var(--accent)}
.tw{overflow-x:auto;margin:14px 0}
table{border-collapse:collapse;width:100%;font:400 .92rem/1.45 var(--f-ui);font-variant-numeric:tabular-nums}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
th{background:var(--s3);font-weight:600}
code{font:.88em var(--f-ui);background:var(--s3);padding:1px 5px;border-radius:4px}
.seq{list-style:none;padding:0;margin:14px 0;counter-reset:s}
.seq li{counter-increment:s;position:relative;padding:0 0 0 34px;margin:9px 0;max-width:64ch}
.seq li::before{content:counter(s);position:absolute;left:0;top:1px;width:22px;height:22px;border-radius:50%;background:var(--accent);color:var(--accent-ink);font:600 .72rem/22px var(--f-ui);text-align:center}
.kv{display:grid;grid-template-columns:auto 1fr;gap:4px 14px;margin:12px 0;font-size:.96rem}
.kv dt{font:500 .78rem/1.5 var(--f-ui);color:var(--mark);white-space:nowrap}
.kv dd{margin:0}

/* ---------- misc ---------- */
.chapter-foot{display:flex;justify-content:space-between;gap:16px;margin:28px 0 0;font:500 .8rem/1 var(--f-ui)}
.chapter-foot a{text-decoration:none;padding:9px 14px;border:1px solid var(--line);border-radius:999px;background:var(--s0)}
.chapter-foot a:hover{background:var(--s2)}
footer.end{max-width:1030px;margin:0 auto;padding:40px clamp(20px,5vw,64px) 80px;border-top:1px solid var(--line);color:var(--faint);font:400 .88rem/1.6 var(--f-ui)}
@media (max-width:720px){
  body{font-size:17px}
  .mast{padding-top:34px}
  .card{padding:20px 18px 6px;border-radius:10px}
  details.layer{margin:12px -18px 0}
  details.layer>summary{padding:12px 18px}
  .layer-body{padding:2px 18px 18px}
  details.l3{margin:12px 0 0}
  nav.chapters{display:none}
}
@media print{
  .rail,.chapter-foot{display:none}
  details.layer{border:0}
  details.layer>summary{display:none}
  .layer-body,details.l3>.layer-body{display:block!important;background:none;padding:0}
  details.l3{background:none;border:0;border-left:2px solid #999;border-radius:0;padding-left:12px}
  .card{break-inside:avoid;box-shadow:none;background:none;border:0;border-bottom:1px solid #ccc;padding:0 0 14px}
  body{background:#fff;color:#000;font-size:11pt}
}
"""

JS = """
(function(){
  var body=document.body, btns=[].slice.call(document.querySelectorAll('.depth-btns button'));
  function apply(d,persist){
    document.querySelectorAll('details.l2').forEach(function(x){x.open=d>=2;});
    document.querySelectorAll('details.l3').forEach(function(x){x.open=d>=3;});
    btns.forEach(function(b){b.setAttribute('aria-pressed', b.dataset.depth===String(d));});
    if(persist){try{localStorage.setItem('primer-depth',d);}catch(e){}}
  }
  btns.forEach(function(b){b.addEventListener('click',function(){apply(+b.dataset.depth,true);});});
  var saved=1; try{var v=localStorage.getItem('primer-depth'); if(v)saved=+v;}catch(e){}
  apply(saved,false);

  var links=[].slice.call(document.querySelectorAll('nav.chapters a')), map={};
  links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a;});
  if('IntersectionObserver' in window){
    var obs=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ links.forEach(function(a){a.classList.remove('on');}); var a=map[e.target.id]; if(a)a.classList.add('on'); } });
    },{rootMargin:'-15% 0px -75% 0px'});
    document.querySelectorAll('section.chapter').forEach(function(s){obs.observe(s);});
  }
})();
"""

def build():
    parts = sorted(PARTS.glob("*.html"))
    if not parts:
        sys.exit("no parts found in guide/parts/")
    chapters, bodies = [], []
    for p in parts:
        html = p.read_text(encoding="utf-8").replace("PLAYBOOK_URL", PLAYBOOK)
        for m in re.finditer(r'<section class="chapter" id="([^"]+)"([^>]*)>.*?<h2>(.*?)</h2>', html, re.S):
            nav = re.search(r'data-nav="([^"]*)"', m.group(2))
            chapters.append((m.group(1), nav.group(1) if nav else re.sub(r"<[^>]+>", "", m.group(3)).strip()))
        bodies.append(html)
    return chapters, bodies


def main():
    chapters, body_parts = build()
    nav = "".join(f'<a href="#{cid}">{title}</a>' for cid, title in chapters)
    def _g(cid, title):
        num, _, rest = title.partition(" · ")
        return (f'<li><a href="#{cid}"><b>{num}</b>{rest}</a></li>' if rest
                else f'<li><a href="#{cid}"><b>·</b>{title}</a></li>')
    glance = "".join(_g(cid, title) for cid, title in chapters)
    doc = [
        "<title>The Family CFO Primer</title>",
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=Archivo:wght@400;500;600&display=swap">',
        f"<style>{CSS}</style>",
        '<header class="mast"><div class="mast-in"><div>',
        '<p class="kicker">A guided walkthrough · read once, then keep the playbook</p>',
        "<h1>The Family CFO Primer</h1>",
        '<p class="stand">Everything the practice does, in ten chapters — each idea stated in one line, '
        'explained in a paragraph, and taken down to the mechanics when you want them. '
        '<em>Open only as deep as you need.</em></p>',
        f'</div><div class="glance"><h2>Inside</h2><ol>{glance}</ol></div></div></header>',
        '<div class="rail"><div class="rail-in">',
        '<div class="depth"><span class="depth-lbl">Depth</span><div class="depth-btns" role="group" aria-label="Reading depth">'
        '<button data-depth="1" aria-pressed="true">1 · The claim</button>'
        '<button data-depth="2" aria-pressed="false">2 · Why &amp; how</button>'
        '<button data-depth="3" aria-pressed="false">3 · Mechanics</button>'
        "</div></div>",
        f'<nav class="chapters" aria-label="Chapters">{nav}</nav>',
        "</div></div>",
        "<main>",
        "\n".join(body_parts),
        "</main>",
        f'<footer class="end">Companion to <a href="{PLAYBOOK}">The Family CFO Playbook</a> — '
        "the 38 procedures and 28 templates this primer walks you through. "
        "Sources: Bowen &amp; CEG Worldwide (the consultative process), James E. Hughes Jr. and co-authors "
        "(the family layer), Philip Palaveev (the team). All content is original writing informed by them.</footer>",
        f"<script>{JS}</script>",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(doc), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size//1024} KB, {len(chapters)} chapters, {len(body_parts)} parts)")

if __name__ == "__main__":
    main()
