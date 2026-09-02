#!/usr/bin/env python3
"""Build the GitHub Pages site into docs/ — landing page + both documents."""
import subprocess, sys, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"

LANDING = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Family CFO Practice</title>
<meta name="description" content="Operating procedures for a wealth-management practice serving families with $30M to several hundred million — a guided primer and a 38-procedure playbook.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=Archivo:wght@400;500;600&display=swap">
<style>
:root{--ground:#eceae5;--card:#f8f7f4;--ink:#1c2120;--muted:#5e6663;--faint:#8a918d;--line:#d2cec5;
  --accent:#155e63;--accent-ink:#fff;--accent-soft:#d9e8e8;--mark:#9c5326;
  --f-disp:"Instrument Serif","Iowan Old Style",Georgia,serif;
  --f-body:"Newsreader","Iowan Old Style",Georgia,serif;
  --f-ui:"Archivo","Helvetica Neue",Arial,sans-serif;}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ground:#14171a;--card:#1b1f22;--ink:#e9e8e3;--muted:#a2aba7;--faint:#7d8783;--line:#333b3e;--accent:#74c3c7;--accent-ink:#0e1c1d;--accent-soft:#1a2f31;--mark:#dd9a68;}}
:root[data-theme="dark"]{--ground:#14171a;--card:#1b1f22;--ink:#e9e8e3;--muted:#a2aba7;--faint:#7d8783;--line:#333b3e;--accent:#74c3c7;--accent-ink:#0e1c1d;--accent-soft:#1a2f31;--mark:#dd9a68;}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font:18px/1.62 var(--f-body);-webkit-font-smoothing:antialiased;
  display:flex;flex-direction:column;min-height:100vh}
a{color:var(--accent)}
a:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:3px}
.wrap{max-width:1120px;margin:0 auto;padding:clamp(44px,8vw,96px) clamp(20px,5vw,56px) 40px;flex:1}
.kicker{font:500 .72rem/1 var(--f-ui);letter-spacing:.2em;text-transform:uppercase;color:var(--mark);margin:0 0 18px}
h1{font:400 clamp(2.5rem,6.5vw,4.2rem)/1 var(--f-disp);margin:0;letter-spacing:-.015em;text-wrap:balance}
.stand{font-size:clamp(1.05rem,2vw,1.24rem);color:var(--muted);margin:20px 0 0;max-width:60ch}
.stand em{color:var(--ink);font-style:italic}
.docs{display:grid;grid-template-columns:repeat(auto-fit,minmax(272px,1fr));gap:20px;margin:52px 0 0}
.doc{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:28px 30px 26px;display:flex;flex-direction:column;
  text-decoration:none;color:inherit;transition:transform .16s ease,border-color .16s ease}
.doc:hover{transform:translateY(-2px);border-color:var(--accent)}
.doc.primary{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent) inset}
.doc .tag{font:600 .66rem/1 var(--f-ui);letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin:0 0 8px}
.doc .icon{font-size:1.7rem;line-height:1;margin:0 0 14px}
.doc h2{font:400 1.62rem/1.15 var(--f-disp);margin:0 0 8px;letter-spacing:-.01em}
.doc p{margin:0;color:var(--muted);font-size:.99rem;flex:1}
.doc .meta{margin:18px 0 0;font:500 .74rem/1.5 var(--f-ui);letter-spacing:.08em;text-transform:uppercase;color:var(--faint);
  display:flex;align-items:baseline;gap:4px 10px;flex-wrap:wrap}
.doc .go{margin-left:auto;color:var(--accent);letter-spacing:0;text-transform:none;font-size:.82rem;white-space:nowrap}
.order{margin:44px 0 0;padding:22px 26px;border-left:3px solid var(--accent);background:var(--accent-soft);border-radius:0 10px 10px 0;max-width:72ch}
.order p{margin:0;font-size:1rem}
.order b{font-weight:600}
.note{margin:40px 0 0;max-width:72ch;color:var(--muted);font-size:.95rem}
footer{border-top:1px solid var(--line);color:var(--faint);font:400 .84rem/1.65 var(--f-ui)}
footer .wrap{padding-top:26px;padding-bottom:36px;max-width:1120px}
footer a{color:var(--muted)}
@media (prefers-reduced-motion:reduce){.doc{transition:none}.doc:hover{transform:none}}
</style>
</head>
<body>
<div class="wrap">
  <p class="kicker">Wealth management · $30M to several hundred million</p>
  <h1>The Family CFO Practice</h1>
  <p class="stand">A written operating system for a practice that serves families as their personal chief financial officer — the consultative process, the family layer, and the team that delivers it. <em>Three documents: one to install it, one to understand it, one to work from.</em></p>

  <div class="docs">
    <a class="doc primary" href="setup.html">
      <p class="icon">🔧</p>
      <p class="tag">Start here</p>
      <h2>Set Up the Practice</h2>
      <p>Twenty steps that install the whole method into Hazel, your AI assistant. Click, paste, tick it off. No reading required first.</p>
      <p class="meta">20 steps · about 2.5 hours <span class="go">Begin →</span></p>
    </a>
    <a class="doc" href="primer.html">
      <p class="icon">🧭</p>
      <h2>The Primer</h2>
      <p>The whole practice in ten chapters. Every idea stated in one line, explained in a paragraph, and opened down to the mechanics when you want them.</p>
      <p class="meta">57 ideas · 3 depths <span class="go">Read →</span></p>
    </a>
    <a class="doc" href="playbook.html">
      <p class="icon">🏛️</p>
      <h2>The Playbook</h2>
      <p>The procedures themselves: triggers, owners, step-by-step sequences, scripts, and the fill-in templates each one consumes or produces.</p>
      <p class="meta">38 procedures · 28 templates <span class="go">Open →</span></p>
    </a>
  </div>

  <div class="order"><p><b>If you are implementing this, start with Set Up the Practice</b> and work down the steps in order — you do not need to read anything else first. <b>If you want to understand it,</b> read the Primer at depth 1, front to back: about ten minutes for the shape of the whole thing. The Playbook is the reference you open when you are about to do something.</p></div>

  <p class="note">The setup guide configures <a href="https://docs.hazel.ai">Hazel</a>, the AI platform from Altruist, and is honest about what it will and will not do. Every procedure names its trigger, its owner, its inputs and outputs, and what changes when the practice serves a whole family rather than one member of a larger one. All of it is original writing, informed by the consultative-process literature (Bowen and CEG Worldwide), the family-wealth literature (James E. Hughes Jr. and co-authors), and the practice-management literature (Philip Palaveev); nothing is reproduced from those sources.</p>
</div>
<footer><div class="wrap">Built from the markdown library in this repository — <code>build/build.py</code> renders the playbook, <code>guide/build_guide.py</code> renders the primer, <code>build_site.py</code> assembles this site.</div></footer>
</body>
</html>
"""

def main():
    DOCS.mkdir(exist_ok=True)
    py = sys.executable
    subprocess.run([py, "build/build.py", "--check"], cwd=ROOT, check=True)
    subprocess.run([py, "build/build.py", "--out", str(DOCS / "playbook.html")], cwd=ROOT, check=True)
    subprocess.run([py, "guide/build_guide.py", "--out", str(DOCS / "primer.html"),
                    "--playbook-url", "playbook.html"], cwd=ROOT, check=True)
    subprocess.run([py, "setup/build_setup.py", "--out", str(DOCS / "setup.html"),
                    "--playbook-url", "playbook.html", "--primer-url", "primer.html"], cwd=ROOT, check=True)
    (DOCS / "index.html").write_text(LANDING, encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    for f in sorted(DOCS.iterdir()):
        if f.is_file():
            print(f"  docs/{f.name:22s} {f.stat().st_size//1024:>4d} KB")

if __name__ == "__main__":
    main()
