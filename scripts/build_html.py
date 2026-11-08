# Builds references_gallery.html: fixed character references, a divider, then shot cards
# (image + story + narration/dialogue + copyable video prompt) from shots.json.
# Run from the "فصل 2" folder:  py -I scripts/build_html.py
import base64, html, json, os

ROOT = os.getcwd()
REFS = [("nafiseh_ref.webp", "نفیسه"), ("madar_nafiseh_ref.webp", "مادر نفیسه"),
        ("sara_ref.webp", "سارا"), ("damad_ref.webp", "داماد"),
        ("madar_damad_ref.webp", "مادر داماد"), ("pedar_damad_ref.webp", "پدر داماد"),
        ("siahi_ref.webp", "سیاهی"), ("paziraee_ref.webp", "پذیرایی خونه نفیسه"),
        ("otagh_nafiseh_ref.webp", "اتاق نفیسه")]


def b64(path):
    ext = os.path.splitext(path)[1].lstrip(".").replace("jpg", "jpeg")
    return f"data:image/{ext};base64," + base64.b64encode(open(path, "rb").read()).decode()


e = html.escape
refs = "".join(
    f'<figure><img src="{b64(os.path.join(ROOT, "references", f))}" alt="{e(n)}"><figcaption>{e(n)}</figcaption></figure>'
    for f, n in REFS)

shots_all = json.load(open(os.path.join(ROOT, "shots.json"), encoding="utf-8"))

CSS = """body{margin:0;padding:16px;background:#111;color:#eee;font-family:Tahoma,Vazirmatn,sans-serif}
h1{font-size:20px;color:#ff3b3b;margin:0 0 14px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:12px}
figure{margin:0;background:#1c1c1c;border-radius:10px;overflow:hidden;border:1px solid #333}
figure img{width:100%;aspect-ratio:9/16;object-fit:cover;display:block}
figcaption{text-align:center;padding:7px;font-size:14px;font-weight:bold}
hr{border:0;border-top:3px solid #ff3b3b;margin:26px 0 8px}
.seq{color:#ff3b3b;font-size:18px;margin:18px 0 10px}
.shot{display:flex;gap:16px;background:#1a1a1a;border:1px solid #333;border-radius:12px;padding:12px;margin-bottom:16px;flex-wrap:wrap}
.pic{flex:0 0 220px;max-width:100%} .pic img{width:100%;border-radius:8px;display:block}
.todo{aspect-ratio:9/16;display:flex;align-items:center;justify-content:center;font-size:40px;color:#666;background:#222;border-radius:8px}
.info{flex:1 1 300px;min-width:0} h3{margin:0 0 6px;font-size:16px}
.meta{color:#aaa;font-size:13px} .story{line-height:1.8;font-size:14px}
.talk{background:#241515;border-right:4px solid #ff3b3b;padding:8px 10px;border-radius:6px;margin:8px 0}
.line{line-height:1.9;font-size:15px} .nar{color:#ffcf9e} .muted{color:#888}
.snd{color:#9ec9ff;font-size:13px;margin:8px 0}
.lbl{font-size:13px;color:#bbb;margin:6px 0}
.pbox{position:relative} pre{white-space:pre-wrap;background:#0b0b0b;border:1px solid #333;border-radius:6px;padding:34px 10px 10px;font-size:12px;line-height:1.5;text-align:left;margin:0}
button{position:absolute;top:6px;right:6px;background:#ff3b3b;color:#fff;border:0;border-radius:5px;padding:4px 12px;cursor:pointer;font-family:inherit}"""

SCRIPT = """<script>
function cp(i,b){var t=document.getElementById('p'+i).innerText;
 function ok(){b.textContent='کپی شد ✓';setTimeout(function(){b.textContent='کپی'},1500)}
 function fb(){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();
  try{document.execCommand('copy');ok()}catch(e){}document.body.removeChild(a)}
 if(navigator.clipboard){navigator.clipboard.writeText(t).then(ok,fb)}else fb();}
</script>"""


def render(shots, title, with_refs):
    cards, last_seq = [], None
    for i, s in enumerate(shots):
        if s["seq"] != last_seq:
            cards.append(f'<h2 class="seq">{e(s["seq"])}</h2>')
            last_seq = s["seq"]
        talk = ""
        if s.get("narration"):
            talk += f'<div class="line nar"><b>راوی:</b> {e(s["narration"])}</div>'
            if s.get("narration_note"):
                talk += f'<div class="line muted">{e(s["narration_note"])}</div>'
        for who, txt in s.get("dialogue", []):
            talk += f'<div class="line"><b>{e(who)}:</b> «{e(txt)}»</div>'
        if not talk:
            talk = '<div class="line muted">این شات راوی یا دیالوگ نداره.</div>'
        img = os.path.join(ROOT, s["image"])
        img_html = f'<img src="{b64(img)}" alt="">' if os.path.exists(img) else '<div class="todo">⏳</div>'
        cards.append(f'''<section class="shot">
  <div class="pic">{img_html}</div>
  <div class="info">
    <h3>{e(s["title"])}</h3>
    <div class="meta">⏱ {e(s.get("duration", ""))}</div>
    <p class="story">{e(s.get("story", ""))}</p>
    <div class="talk"><div class="lbl">🎙 راوی و دیالوگ‌ها</div>{talk}</div>
    <div class="snd">🔊 {e(s.get("sound", ""))}</div>
    <div class="lbl">🎬 پرامپت ویدیو (Gemini)</div>
    <div class="pbox"><button onclick="cp({i},this)">کپی</button><pre id="p{i}" dir="ltr">{e(s["video_prompt"])}</pre></div>
  </div>
</section>''')
    refs_html = (f'<div class="lbl">تصاویر مرجع (ثابت)</div><div class="grid">{refs}</div><hr>' if with_refs else "")
    return (f'<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title>'
            f'<style>{CSS}</style></head><body><h1>{e(title)}</h1>{refs_html}{"".join(cards)}{SCRIPT}</body></html>')


import glob, re
from collections import OrderedDict
groups = OrderedDict()
for s_ in shots_all:
    groups.setdefault(s_["id"].split("_")[0], []).append(s_)   # s1, s2, s3 ...
for old in glob.glob(os.path.join(ROOT, "html*.html")) + glob.glob(os.path.join(ROOT, "gallery_live_*.html")):
    os.remove(old)
out = []
open(os.path.join(ROOT, "html0_marajea.html"), "w", encoding="utf-8").write(
    render([], "عروسی جن‌ها | فصل ۲ | تصاویر مرجع", True)); out.append("html0_marajea.html")
for key, items in groups.items():
    num = key[1:]
    name = f"html{num}_seq{num}_{len(items)}shot.html"
    open(os.path.join(ROOT, name), "w", encoding="utf-8").write(
        render(items, f"عروسی جن‌ها | فصل ۲ | قسمت ۱ | سکانس {num}", False))
    out.append(name)
print("built:", out)

# single combined page: references + all shots, full-quality images
all_name = "episode1_full.html"
open(os.path.join(ROOT, all_name), "w", encoding="utf-8").write(
    render(shots_all, "عروسی جن‌ها | فصل ۲ | قسمت ۱ | همه‌ی شات‌ها", True))
print("combined:", all_name)
