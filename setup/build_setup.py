#!/usr/bin/env python3
"""Assemble the v2 setup guide from setup/parts/*.html into an HTML page."""
from pathlib import Path
import argparse, re, sys

ROOT = Path(__file__).resolve().parent.parent
PARTS = ROOT / "setup" / "parts"
DEFAULT_OUT = ROOT / "dist" / "family-cfo-setup.html"
PLAYBOOK_DEFAULT = "https://claude.ai/code/artifact/2890b4bc-3b5a-4a3b-830f-eb49c8d295c7"
PRIMER_DEFAULT = "https://claude.ai/code/artifact/7eddc750-f492-4071-9490-468515db0d2e"
TITLE = "Set Up the Practice"

CSS = """
:root{
  --ground:#eef0ec;--card:#fbfbf9;--sunk:#e4e8e3;--ink:#1a1f1d;--muted:#5a635f;--faint:#88918c;
  --line:#d3d8d2;--line-soft:#e2e6e1;
  --accent:#0f6b5c;--accent-ink:#fff;--accent-soft:#dbeee8;--accent-line:#9fcfc2;
  --done:#2f7d32;--done-soft:#e2f0e2;
  --mark:#9a5a24;--mark-soft:#f7e9dc;
  --warn:#8c2f2f;--warn-soft:#f8e6e6;
  --f-body:"Newsreader","Iowan Old Style",Georgia,serif;
  --f-ui:"Archivo","Helvetica Neue",Arial,sans-serif;
  --f-mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;
  --shadow:0 1px 2px rgba(26,31,29,.05),0 8px 22px rgba(26,31,29,.05);
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#131715;--card:#1a1f1c;--sunk:#222825;--ink:#e8eae6;--muted:#a3aca7;--faint:#7b847f;
  --line:#2f3733;--line-soft:#262d29;
  --accent:#5fbfa8;--accent-ink:#08201b;--accent-soft:#16302a;--accent-line:#2c5a50;
  --done:#7dc47f;--done-soft:#172c18;
  --mark:#d99a5e;--mark-soft:#31220f;
  --warn:#e89a9a;--warn-soft:#341a1a;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 22px rgba(0,0,0,.25);
}}
:root[data-theme="dark"]{
  --ground:#131715;--card:#1a1f1c;--sunk:#222825;--ink:#e8eae6;--muted:#a3aca7;--faint:#7b847f;
  --line:#2f3733;--line-soft:#262d29;
  --accent:#5fbfa8;--accent-ink:#08201b;--accent-soft:#16302a;--accent-line:#2c5a50;
  --done:#7dc47f;--done-soft:#172c18;
  --mark:#d99a5e;--mark-soft:#31220f;
  --warn:#e89a9a;--warn-soft:#341a1a;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 22px rgba(0,0,0,.25);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:104px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
body{margin:0;background:var(--ground);color:var(--ink);font:17px/1.6 var(--f-ui);-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:4px}

/* masthead */
.mast{background:var(--card);border-bottom:1px solid var(--line);padding:clamp(30px,5vw,54px) clamp(18px,4vw,44px) 26px}
.mast-in{max-width:820px;margin:0 auto}
.eyebrow{font:600 .7rem/1 var(--f-ui);letter-spacing:.18em;text-transform:uppercase;color:var(--mark);margin:0 0 14px}
.mast h1{font:600 clamp(2rem,5vw,2.9rem)/1.05 var(--f-ui);margin:0;letter-spacing:-.02em;text-wrap:balance}
.mast .sub{font:400 clamp(1.02rem,2vw,1.16rem)/1.55 var(--f-body);color:var(--muted);margin:14px 0 0;max-width:58ch}
.mast .sub b{color:var(--ink);font-weight:600}

/* progress rail */
.rail{position:sticky;top:0;z-index:30;background:color-mix(in srgb,var(--ground) 92%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.rail-in{max-width:820px;margin:0 auto;padding:11px clamp(18px,4vw,44px);display:flex;align-items:center;gap:16px}
.bar{flex:1;height:7px;border-radius:99px;background:var(--sunk);overflow:hidden}
.bar i{display:block;height:100%;width:0;background:var(--accent);border-radius:99px;transition:width .3s ease}
.count{font:600 .8rem/1 var(--f-ui);color:var(--muted);white-space:nowrap;font-variant-numeric:tabular-nums}
.reset{appearance:none;border:0;background:none;color:var(--faint);font:500 .76rem/1 var(--f-ui);cursor:pointer;padding:6px;white-space:nowrap}
.reset:hover{color:var(--ink);text-decoration:underline}

main{max-width:820px;margin:0 auto;padding:8px clamp(18px,4vw,44px) 120px}

/* phase divider */
.phase{margin:46px 0 18px;display:flex;align-items:baseline;gap:12px}
.phase h2{font:600 .76rem/1 var(--f-ui);letter-spacing:.16em;text-transform:uppercase;color:var(--mark);margin:0}
.phase span{flex:1;height:1px;background:var(--line)}
.phase em{font:400 .84rem/1 var(--f-body);color:var(--faint);font-style:italic}

/* step card */
.step{background:var(--card);border:1px solid var(--line);border-radius:14px;margin:0 0 16px;box-shadow:var(--shadow);overflow:hidden;transition:opacity .2s ease}
.step-head{display:flex;gap:16px;align-items:flex-start;padding:22px 24px 0}
.tick{flex:none;width:34px;height:34px;border-radius:50%;border:2px solid var(--accent-line);background:var(--card);color:transparent;
  font:700 1rem/1 var(--f-ui);cursor:pointer;display:grid;place-items:center;transition:all .18s ease;margin-top:2px}
.tick:hover{border-color:var(--accent);background:var(--accent-soft)}
.step-t{flex:1;min-width:0}
.step-n{font:600 .72rem/1 var(--f-ui);letter-spacing:.13em;text-transform:uppercase;color:var(--faint);display:flex;gap:10px;align-items:center;margin:0 0 5px;flex-wrap:wrap}
.time{background:var(--sunk);color:var(--muted);border-radius:99px;padding:3px 9px;letter-spacing:.04em;text-transform:none;font-weight:500}
.step h3{font:600 1.28rem/1.3 var(--f-ui);margin:0;letter-spacing:-.012em;text-wrap:balance}
.gives{font:400 1.02rem/1.55 var(--f-body);color:var(--muted);margin:8px 0 0;max-width:62ch}
.step-body{padding:16px 24px 24px 74px}
@media (max-width:640px){.step-body{padding:14px 18px 20px}.step-head{padding:18px 18px 0}}

/* done state */
.step.done{opacity:.55}
.step.done .tick{background:var(--done);border-color:var(--done);color:#fff}
.step.done .tick::after{content:"✓"}
.step.done .step-body{display:none}
.step.done .gives{display:none}

/* blocks */
h4.blk{font:600 .72rem/1 var(--f-ui);letter-spacing:.14em;text-transform:uppercase;color:var(--faint);margin:22px 0 10px}
h4.blk:first-child{margin-top:0}
ol.do{margin:0;padding:0;list-style:none;counter-reset:d}
ol.do li{counter-increment:d;position:relative;padding:0 0 0 30px;margin:0 0 9px;max-width:62ch}
ol.do li::before{content:counter(d);position:absolute;left:0;top:2px;width:20px;height:20px;border-radius:6px;background:var(--sunk);color:var(--muted);
  font:600 .72rem/20px var(--f-ui);text-align:center}
ul.plain{margin:0;padding-left:1.1em;max-width:62ch}
ul.plain li{margin:0 0 7px}
kbd{font:500 .84em var(--f-mono);background:var(--sunk);border:1px solid var(--line);border-bottom-width:2px;border-radius:5px;padding:1px 6px;white-space:nowrap}
.path{font:500 .86em var(--f-mono);background:var(--sunk);border-radius:5px;padding:1px 7px;white-space:nowrap}

/* paste block */
.paste{border:1px solid var(--accent-line);border-radius:10px;background:var(--accent-soft);overflow:hidden;margin:0 0 14px}
.paste-top{display:flex;align-items:center;gap:10px;padding:8px 10px 8px 14px;border-bottom:1px solid var(--accent-line)}
.paste-lbl{font:600 .7rem/1 var(--f-ui);letter-spacing:.12em;text-transform:uppercase;color:var(--accent);flex:1}
.copy{appearance:none;border:1px solid var(--accent);background:var(--accent);color:var(--accent-ink);border-radius:7px;
  font:600 .74rem/1 var(--f-ui);padding:7px 13px;cursor:pointer;white-space:nowrap;transition:opacity .15s ease}
.copy:hover{opacity:.86}
.copy.ok{background:var(--done);border-color:var(--done)}
.paste pre{margin:0;padding:14px 16px;overflow-x:auto;background:var(--card);
  font:400 .93rem/1.55 var(--f-body);white-space:pre-wrap;word-wrap:break-word;color:var(--ink)}

/* check + notes */
.check{border-left:3px solid var(--done);background:var(--done-soft);border-radius:0 9px 9px 0;padding:11px 16px;margin:16px 0 0;max-width:66ch}
.check p{margin:0;font:400 .98rem/1.5 var(--f-body)}
.check .lbl{font:600 .68rem/1 var(--f-ui);letter-spacing:.13em;text-transform:uppercase;color:var(--done);display:block;margin:0 0 5px}
.note{border-left:3px solid var(--mark);background:var(--mark-soft);border-radius:0 9px 9px 0;padding:11px 16px;margin:14px 0;max-width:66ch}
.note p{margin:0;font:400 .96rem/1.5 var(--f-body)}
.note .lbl{font:600 .68rem/1 var(--f-ui);letter-spacing:.13em;text-transform:uppercase;color:var(--mark);display:block;margin:0 0 5px}
.note.stop{border-left-color:var(--warn);background:var(--warn-soft)}
.note.stop .lbl{color:var(--warn)}
.src{font:400 .8rem/1.5 var(--f-ui);color:var(--faint);margin:14px 0 0}
.src a{color:var(--muted)}
.tw{overflow-x:auto;margin:12px 0}
table{border-collapse:collapse;width:100%;font:400 .9rem/1.45 var(--f-ui)}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
th{background:var(--sunk);font-weight:600}

footer{max-width:820px;margin:0 auto;padding:34px clamp(18px,4vw,44px) 90px;border-top:1px solid var(--line);
  color:var(--faint);font:400 .87rem/1.65 var(--f-ui)}
footer a{color:var(--muted)}
@media print{.rail,.tick,.copy,.reset{display:none}.step{break-inside:avoid;box-shadow:none}.step.done{opacity:1}
  .step.done .step-body,.step.done .gives{display:block}body{background:#fff;color:#000}}
"""

JS = """
(function(){
  var KEY='cfo-setup-v2';
  var steps=[].slice.call(document.querySelectorAll('.step'));
  var bar=document.querySelector('.bar i'), count=document.querySelector('.count');
  function load(){try{return JSON.parse(localStorage.getItem(KEY))||{};}catch(e){return {};}}
  function save(s){try{localStorage.setItem(KEY,JSON.stringify(s));}catch(e){}}
  var state=load();
  function paint(){
    var n=0;
    steps.forEach(function(el){
      var on=!!state[el.id];
      el.classList.toggle('done',on);
      var t=el.querySelector('.tick');
      if(t){t.setAttribute('aria-pressed',on);t.setAttribute('aria-label',(on?'Mark step incomplete: ':'Mark step complete: ')+(el.dataset.title||''));}
      if(on)n++;
    });
    if(bar)bar.style.width=(steps.length?(n/steps.length*100):0)+'%';
    if(count)count.textContent=n+' of '+steps.length+' done';
  }
  steps.forEach(function(el){
    var t=el.querySelector('.tick');
    if(!t)return;
    t.addEventListener('click',function(){
      state[el.id]=!state[el.id];
      if(!state[el.id])delete state[el.id];
      save(state);paint();
      if(state[el.id]){var nx=el.nextElementSibling;while(nx&&!nx.classList.contains('step'))nx=nx.nextElementSibling;
        if(nx)nx.scrollIntoView({block:'start'});}
    });
  });
  var rs=document.querySelector('.reset');
  if(rs)rs.addEventListener('click',function(){state={};save(state);paint();window.scrollTo({top:0});});
  paint();

  document.querySelectorAll('.copy').forEach(function(b){
    b.addEventListener('click',function(){
      var pre=b.closest('.paste').querySelector('pre');
      var txt=pre.innerText;
      var done=function(){var o=b.textContent;b.textContent='Copied';b.classList.add('ok');
        setTimeout(function(){b.textContent=o;b.classList.remove('ok');},1600);};
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(done,function(){fallback(txt,done);});}
      else fallback(txt,done);
    });
  });
  function fallback(txt,cb){
    var ta=document.createElement('textarea');ta.value=txt;ta.style.position='fixed';ta.style.opacity='0';
    document.body.appendChild(ta);ta.select();
    try{document.execCommand('copy');cb();}catch(e){}
    document.body.removeChild(ta);
  }
})();
"""


def build(playbook, primer):
    parts = sorted(PARTS.glob("*.html"))
    if not parts:
        sys.exit("no parts in setup/parts/")
    return [p.read_text(encoding="utf-8").replace("PLAYBOOK_URL", playbook).replace("PRIMER_URL", primer)
            for p in parts]


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build the v2 setup guide.")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--playbook-url", default=PLAYBOOK_DEFAULT)
    ap.add_argument("--primer-url", default=PRIMER_DEFAULT)
    a = ap.parse_args(argv)
    bodies = build(a.playbook_url, a.primer_url)
    n_steps = sum(b.count('class="step"') for b in bodies)
    doc = [
        f"<title>{TITLE}</title>",
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=IBM+Plex+Mono:wght@400;500&display=swap">',
        f"<style>{CSS}</style>",
        '<header class="mast"><div class="mast-in">',
        '<p class="eyebrow">Version 2 · with Hazel</p>',
        f"<h1>{TITLE}</h1>",
        '<p class="sub">Do these steps in order and the practice runs itself. Each one is a few minutes of clicking and pasting. '
        '<b>You do not need to read anything else first.</b></p>',
        "</div></header>",
        '<div class="rail"><div class="rail-in">',
        '<div class="bar"><i></i></div><span class="count"></span><button class="reset" type="button">Reset</button>',
        "</div></div>",
        "<main>", "\n".join(bodies), "</main>",
        f'<footer>Steps: {n_steps}. Progress is saved in this browser only. '
        f'The reasoning behind every step is in <a href="{a.primer_url}">the Primer</a>; '
        f'the full written procedures are in <a href="{a.playbook_url}">the Playbook</a>. '
        "Hazel is Altruist's AI platform — see <a href=\"https://docs.hazel.ai\">docs.hazel.ai</a>. "
        "Verify Hazel's current screens and pricing against their documentation before relying on any step here.</footer>",
        f"<script>{JS}</script>",
    ]
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(doc), encoding="utf-8")
    rel = out.relative_to(ROOT) if out.is_relative_to(ROOT) else out
    print(f"wrote {rel} ({out.stat().st_size//1024} KB, {n_steps} steps, {len(bodies)} parts)")


if __name__ == "__main__":
    main()
