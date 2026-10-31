"""Plantilla compartida de carruseles Plogy (piezas 027 en adelante).

Cada pieza tiene un `generar.py` que importa este módulo, define sus láminas como HTML con las
clases de abajo y llama a `build()`. El resultado es un `carrusel.html` autocontenido (CSS adentro,
logos de marca en línea) con la vista `?s=N` de una sola lámina. Exportar con `_comun/render.py`.

Temas de lámina: light (blanco), surface (crema), dark (Ink con foco naranja), orange (criterio),
photo (CTA con foto a sangre y tarjeta de vidrio).
"""
import html as _html
import pathlib
import re

COMUN = pathlib.Path(__file__).resolve().parent
LOGOS = COMUN / "logos"

BRAND = {
    "gmail": "#EA4335", "googlecalendar": "#4285F4", "googlesheets": "#34A853", "whatsapp": "#25D366",
    "notion": "#000000", "googledrive": "#4285F4", "slack": "#4A154B", "instagram": "#E4405F",
    "openai": "#000000", "anthropic": "#191919", "claude": "#D97757", "googlegemini": "#8E75B2",
    "meta": "#0467DF", "hubspot": "#FF7A59", "shopify": "#7AB55C", "canva": "#00C4CC", "zapier": "#FF4F00",
    "n8n": "#EA4B71", "make": "#6D00CC", "perplexity": "#1FB8CD", "x": "#000000", "linkedin": "#0A66C2",
    "googlemeet": "#00897B", "zoom": "#0B5CFF", "trello": "#0052CC", "airtable": "#18BFFF",
    "stripe": "#635BFF", "mercadopago": "#00B1EA", "wix": "#0C6EFC", "dropbox": "#0061FF", "zoho": "#E42527",
    "xero": "#13B5EA", "googleads": "#4285F4", "adobe": "#FF0000",
}


def logo(name, size=58, color=None):
    """Logo de marca (simple-icons 13.21.0, CC0) en línea, con su color oficial."""
    svg = (LOGOS / f"{name}.svg").read_text(encoding="utf-8")
    fill = color or BRAND.get(name, "#171310")
    svg = svg.replace("<svg ", f'<svg width="{size}" height="{size}" fill="{fill}" ', 1)
    return re.sub(r"<title>.*?</title>", "", svg)


# Íconos de trazo propios (24x24), se pintan con currentColor.
_IC = {
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    "file": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6.5 6.5 0 0 1 3.5 6"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "table": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M3 15h18M10 4v16"/>',
    "brain": '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 6 1V5a3 3 0 0 0-3-1z"/><path d="M15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-6 1"/>',
    "plug": '<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0zM12 18v4"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
    "list": '<path d="M9 6h12M9 12h12M9 18h12"/><circle cx="4" cy="6" r="1"/><circle cx="4" cy="12" r="1"/><circle cx="4" cy="18" r="1"/>',
    "send": '<path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/>',
    "alert": '<path d="M12 3 2 21h20z"/><path d="M12 10v5M12 18h.01"/>',
    "repeat": '<path d="M17 2l4 4-4 4"/><path d="M3 11V9a3 3 0 0 1 3-3h15M7 22l-4-4 4-4"/><path d="M21 13v2a3 3 0 0 1-3 3H3"/>',
    "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
    "money": '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="3"/><path d="M6 10v4M18 10v4"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "image": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="m21 17-5-5-9 8"/>',
    "code": '<path d="m8 7-5 5 5 5M16 7l5 5-5 5"/>',
    "eye": '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "cart": '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.5 12h11.5l2-8H6.2"/>',
    "phone": '<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/>',
    "pen": '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>',
    "chart": '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 6-7"/>',
    "star": '<path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.3 6.5 20.2l1-6.2L3 9.6l6.2-.9z"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
}


def ic(name, size=38, color="currentColor", sw=2.2):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{_IC[name]}</svg>')


def esc(s):
    return _html.escape(s, quote=True)


CSS = r"""
:root{
  --ink:#171310; --paper:#ffffff; --muted:#625951; --orange:#ff5b00; --orangeText:#b43d00;
  --surface:#f4f1ef; --border:#a39486; --line:#e6ddd5; --soft:#cfc6bd; --dim:#8f857c;
  --card:#211b17; --cardLine:#3a322c;
  --grad:linear-gradient(135deg,#ff5b00 0%,#f75946 22%,#ee5358 40%,#e1556a 58%,#c85981 78%,#9c5aa7 100%);
  --display:Screener,'Space Grotesk','Helvetica Neue',Arial,sans-serif;
  --body:'Helvetica Neue',Helvetica,Arial,sans-serif;
  --mono:Consolas,'Courier New',monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#d9d2cb;font-family:var(--body)}
body:not(.single){display:flex;flex-wrap:wrap;gap:32px;padding:32px}
body:not(.single) .slide{zoom:.4}
body.single{background:none}
body.single .slide:not(.on){display:none}
.slide{position:relative;width:1080px;height:1350px;overflow:hidden;color:var(--ink);flex:none}
.t-light{background:var(--paper)}
.t-surface{background:var(--surface)}
.t-dark{color:#fff;background:radial-gradient(ellipse 60% 40% at 50% 0%,rgba(255,91,0,.17),transparent 72%),radial-gradient(circle,rgba(255,255,255,.055) 1.6px,transparent 1.8px) 0 0/40px 40px,var(--ink)}
.t-orange{background:var(--orange);color:var(--ink)}
.t-photo{background:#120d0a;color:#fff}

/* marco */
.logo{position:absolute;top:80px;left:58px;width:230px;height:auto;z-index:6}
.count{position:absolute;top:96px;right:96px;font:700 30px/1 var(--display);letter-spacing:.04em;color:var(--muted);z-index:6}
.t-dark .count,.t-photo .count{color:#a99d92}
.t-orange .count{color:var(--ink);opacity:.6}
.dots{position:absolute;bottom:80px;left:96px;display:flex;gap:14px;z-index:6;color:var(--ink)}
.t-dark .dots,.t-photo .dots{color:#fff}
.dots i{width:14px;height:14px;border-radius:50%;background:currentColor;opacity:.2}
.dots i.on{opacity:1;background:var(--orange)}
.t-orange .dots i.on{background:var(--ink)}
.src{position:absolute;left:96px;right:96px;bottom:118px;z-index:4;font:400 23px/1.35 var(--body);color:var(--muted)}
.t-dark .src{color:var(--dim)}
.src b{font-weight:700}

/* cuerpo: el contenido fluye entre el logo y los puntos */
.body{position:absolute;left:96px;right:96px;top:196px;bottom:168px;display:flex;flex-direction:column;z-index:3}
.body.src-on{bottom:196px}
.body.end{justify-content:flex-end}
.body.center{justify-content:center}
.vis{flex:1;position:relative;display:flex;align-items:center;justify-content:center;min-height:0}
.gap{height:34px;flex:none} .gap.s{height:20px} .gap.l{height:56px}

h1,h2,h3{position:relative;z-index:3;font-family:var(--display);font-weight:700;letter-spacing:-.035em;line-height:1.05;text-wrap:balance}
h1{font-size:86px} h2{font-size:70px} h3{font-size:46px;letter-spacing:-.025em;line-height:1.1}
h1.xl,h2.xl{font-size:100px} h2.l{font-size:80px} h2.s{font-size:60px}
.hl{color:var(--orange)}
.t-orange .w{color:#fff}
.t-light .hl.t,.t-surface .hl.t{color:var(--orangeText)}
.grad{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.support{position:relative;z-index:3;font:400 36px/1.36 var(--body);color:var(--muted);margin-top:24px;max-width:900px;text-wrap:pretty}
.support b{color:var(--ink);font-weight:700}
.t-dark .support{color:var(--soft)} .t-dark .support b{color:#fff}
.t-orange .support{color:rgba(23,19,16,.78)} .t-orange .support b{color:var(--ink)}
.eyebrow{font:700 26px/1 var(--display);letter-spacing:.14em;text-transform:uppercase;color:var(--orangeText);margin-bottom:26px}
.t-dark .eyebrow{color:var(--orange)}
.t-orange .eyebrow{color:var(--ink);opacity:.72}
.pill{display:inline-flex;align-items:center;gap:12px;align-self:flex-start;background:var(--orange);color:var(--ink);font:700 27px/1 var(--display);letter-spacing:.08em;text-transform:uppercase;padding:17px 28px;border-radius:999px}
.pill.ink{background:var(--ink);color:#fff}
.pill.ghost{background:transparent;border:2px solid var(--border);color:var(--muted)}
.t-dark .pill.ghost{border-color:#5d524a;color:#e6dfd8}
.pills{display:flex;flex-wrap:wrap;gap:14px;align-items:center}
.kick{display:flex;align-items:center;gap:20px;margin-bottom:28px}
.kick i{width:76px;height:76px;flex:none;border-radius:22px;background:var(--orange);color:var(--ink);display:flex;align-items:center;justify-content:center;font:700 40px/1 var(--display);font-style:normal}
.kick span{font:700 26px/1 var(--display);letter-spacing:.14em;text-transform:uppercase;color:var(--orangeText)}
.t-dark .kick span{color:var(--orange)}

/* tarjetas */
.card{position:relative;background:#fff;border:2px solid var(--line);border-radius:34px;box-shadow:0 26px 60px rgba(23,19,16,.13);padding:30px 34px;color:var(--ink)}
.card.flat{box-shadow:none}
.card.ink{background:var(--card);border-color:var(--cardLine);color:#fff;box-shadow:0 30px 70px rgba(0,0,0,.35)}
.t-dark .card:not(.ink){box-shadow:0 30px 70px rgba(0,0,0,.4)}
.card .hd{display:flex;align-items:center;gap:14px;font:700 21px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:22px}
.card.ink .hd{color:#a99d92}
.card .hd .av{width:44px;height:44px;border-radius:50%;background:var(--grad);flex:none}
.ilus{position:absolute;top:24px;right:26px;font:700 16px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);border:1.5px solid var(--border);border-radius:999px;padding:7px 11px;background:rgba(255,255,255,.7)}
.card.ink .ilus,.t-dark .ilus.free{color:#a99d92;border-color:#5d524a;background:transparent}
.ilus.free{position:absolute}

/* chat */
.chat{display:flex;flex-direction:column;gap:16px}
.msg{max-width:84%;border-radius:28px;padding:20px 26px;font:400 29px/1.36 var(--body)}
.msg.u{align-self:flex-end;background:var(--ink);color:#fff;border-bottom-right-radius:8px}
.msg.a{align-self:flex-start;background:var(--surface);color:var(--ink);border-bottom-left-radius:8px}
.card.ink .msg.a{background:#2c241f;color:#f1ebe5}
.card.ink .msg.u{background:var(--orange);color:var(--ink)}
.msg small{display:block;font:700 17px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;opacity:.6;margin-bottom:9px}
.msg.dim{opacity:.45}

/* filas con ícono */
.rows{display:flex;flex-direction:column;gap:14px}
.row{display:grid;grid-template-columns:72px 1fr auto;gap:22px;align-items:center;background:#fff;border:2px solid var(--line);border-radius:26px;padding:18px 24px;color:var(--ink)}
.row .ic{width:72px;height:72px;border-radius:20px;background:var(--surface);display:flex;align-items:center;justify-content:center;color:var(--orange);font:700 36px/1 var(--display)}
.row b{display:block;font:700 33px/1.12 var(--display);letter-spacing:-.015em}
.row span{display:block;margin-top:6px;font:400 26px/1.3 var(--body);color:var(--muted)}
.row em{font:700 19px/1 var(--display);font-style:normal;letter-spacing:.1em;text-transform:uppercase;border-radius:999px;padding:11px 15px;background:var(--surface);color:var(--muted);white-space:nowrap}
.row em.o{background:var(--orange);color:var(--ink)}
.row em.i{background:var(--ink);color:#fff}
.row.on{background:var(--ink);border-color:var(--ink);color:#fff}
.row.on span{color:var(--soft)} .row.on .ic{background:var(--orange);color:var(--ink)}
.row.off{background:transparent;border-style:dashed;border-color:var(--border)}
.row.off b{color:var(--muted)} .row.off .ic{color:var(--border)}
.t-dark .row{background:var(--card);border-color:var(--cardLine);color:#fff}
.t-dark .row span{color:var(--soft)} .t-dark .row .ic{background:#2c241f}
.t-dark .row em{background:#2c241f;color:#e6dfd8}

/* logos */
.lg{width:120px;height:120px;border-radius:32px;background:#fff;box-shadow:0 14px 34px rgba(23,19,16,.14);display:flex;align-items:center;justify-content:center;flex:none}
.lg.s{width:88px;height:88px;border-radius:24px}
.lg.xs{width:64px;height:64px;border-radius:18px;box-shadow:0 8px 18px rgba(23,19,16,.12)}
.orb{border-radius:50%;background:var(--grad);box-shadow:0 0 0 14px rgba(255,91,0,.1),0 30px 70px rgba(231,85,106,.35);display:flex;align-items:center;justify-content:center;color:#fff}

/* cifras */
.stat{font:700 230px/.9 var(--display);letter-spacing:-.055em;color:var(--orange)}
.stat small{font-size:.42em;letter-spacing:-.03em}
.t-dark .stat{text-shadow:0 0 60px rgba(255,91,0,.35)}

/* foto con marco */
.polaroid{position:relative;border:14px solid #fff;border-radius:6px;box-shadow:0 26px 60px rgba(23,19,16,.28);overflow:hidden;background:#fff}
.polaroid img{display:block;width:100%;height:100%;object-fit:cover}

/* nota adhesiva */
.sticky{background:#fff7ef;border-radius:12px;padding:28px 30px;font:600 33px/1.22 var(--display);letter-spacing:-.015em;box-shadow:0 18px 40px rgba(23,19,16,.16);color:var(--ink)}
.sticky.o{background:var(--orange)}
.sticky.i{background:var(--ink);color:#fff}

/* cita de la fuente */
.quote{position:relative;border-left:8px solid var(--orange);padding:6px 0 6px 34px}
.quote p{font:500 40px/1.3 var(--display);letter-spacing:-.02em}
.quote small{display:block;margin-top:18px;font:700 21px/1.2 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.t-dark .quote small{color:var(--dim)}

/* comparación */
.vs{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.vs > div{border-radius:34px;padding:30px 30px 32px;display:flex;flex-direction:column}
.vs .no{background:var(--surface);border:2px dashed var(--border)}
.vs .yes{background:var(--orange)}
.vs .ink{background:var(--ink);color:#fff}
.vs small{font:700 22px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.vs .yes small{color:var(--ink);opacity:.7} .vs .ink small{color:#a99d92}
.vs b{display:block;margin-top:14px;font:700 42px/1.06 var(--display);letter-spacing:-.03em}
.vs ul{list-style:none;margin-top:22px;display:flex;flex-direction:column;gap:13px}
.vs li{font:500 29px/1.25 var(--body);padding-left:40px;position:relative}
.vs .no li{color:var(--muted)}
.vs li::before{position:absolute;left:0;top:-1px;font:700 30px/1 var(--display)}
.vs .no li::before{content:"×";color:var(--border)}
.vs .yes li::before,.vs .ink li::before{content:"✓"}
.vs .ink li::before{color:var(--orange)}

/* tabla */
.tbl{width:100%;border-collapse:collapse;font:400 27px/1.25 var(--body)}
.tbl th{text-align:left;font:700 19px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);padding:0 14px 14px}
.tbl td{padding:18px 14px;border-top:2px solid var(--line)}
.tbl td b{font:700 29px/1.1 var(--display)}
.tbl tr.on td{background:#fff3ea}
.tbl .o{color:var(--orangeText);font-weight:700}

/* teléfono */
.phone{position:relative;width:400px;border-radius:60px;background:var(--ink);padding:14px;box-shadow:0 40px 80px rgba(23,19,16,.32)}
.phone .scr{position:relative;border-radius:47px;overflow:hidden;background:#fff}
.phone .scr img{display:block;width:100%}
.phone .nt{position:absolute;top:24px;left:50%;width:120px;height:32px;margin-left:-60px;border-radius:999px;background:var(--ink);z-index:2}

/* criterio */
.crit-mark{display:inline-flex;align-items:center;gap:16px;font:700 26px/1 var(--display);letter-spacing:.14em;text-transform:uppercase;margin-bottom:34px}
.crit-mark i{width:58px;height:58px;border-radius:50%;background:var(--ink);color:var(--orange);display:flex;align-items:center;justify-content:center}
.t-dark .crit-mark{color:var(--orange)} .t-dark .crit-mark i{background:var(--orange);color:var(--ink)}

/* CTA vidrio + foto */
.t-photo .photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.t-photo .shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,13,10,.78) 0%,rgba(18,13,10,.2) 22%,rgba(18,13,10,.05) 40%,rgba(18,13,10,.15) 60%,rgba(18,13,10,.88) 100%)}
.glass{position:absolute;left:96px;right:96px;z-index:4;border-radius:44px;padding:48px 56px;text-align:center;
  background:rgba(30,22,17,.42);border:1.5px solid rgba(255,255,255,.3);
  -webkit-backdrop-filter:blur(26px) saturate(140%);backdrop-filter:blur(26px) saturate(140%);
  box-shadow:0 30px 80px rgba(0,0,0,.45),inset 0 1px 0 rgba(255,255,255,.25)}
.glass .sym{width:150px;height:150px;display:block;margin:-40px auto -14px}
.glass .ey{font:700 25px/1.2 var(--display);letter-spacing:.18em;text-transform:uppercase;color:#ffb48a}
.glass h2{margin-top:20px;font-size:56px;color:#fff}
.glass small{display:block;margin-top:26px;font:700 44px/1 var(--display)}
.glass strong{display:block;margin-top:6px;font:700 132px/1 var(--display);letter-spacing:-.04em;color:var(--orange);text-shadow:0 0 50px rgba(255,91,0,.5)}
.glass strong.m{font-size:104px}
.glass p{margin-top:22px;font:500 33px/1.3 var(--display);color:#fff}
.glass p span{display:block;margin-top:14px;font:400 27px/1.4 var(--body);color:#e6dfd8}
.glass .follow{display:inline-flex;align-items:center;gap:16px;margin-top:28px;background:var(--orange);color:var(--ink);border-radius:999px;padding:22px 40px;font:700 46px/1 var(--display);letter-spacing:-.02em}
.glass .handle{display:block;margin-top:16px;font:500 26px/1 var(--mono);color:#e6dfd8}
"""

SCRIPT = """<script>
  var m = location.search.match(/s=(\\d+)/);
  if (m) {
    document.body.classList.add('single');
    var el = document.querySelector('.slide[data-n="' + m[1] + '"]');
    if (el) el.classList.add('on');
  }
</script>"""

LOGO_FILE = {"light": "plogy-color.svg", "surface": "plogy-color.svg", "dark": "plogy-white.svg",
             "orange": "plogy-black.svg", "photo": "plogy-white.svg"}


def slide(theme, html, cls="", src=None, chrome=True):
    return {"theme": theme, "html": html, "cls": cls, "src": src, "chrome": chrome}


def build(out_dir, title, comment, slides, extra_css=""):
    out_dir = pathlib.Path(out_dir)
    n = len(slides)
    parts = []
    for i, s in enumerate(slides, 1):
        inner = s["html"]
        if s.get("src"):
            inner = inner.replace('class="body', 'class="body src-on', 1)
            inner += f'\n  <div class="src">{s["src"]}</div>'
        chrome = ""
        if s.get("chrome", True):
            band = 'class="cband"' in s["html"]
            if band:
                s = dict(s, cls=(s["cls"] + " has-band").strip())
            lf = "plogy-white.svg" if band else LOGO_FILE[s["theme"]]
            chrome = (f'\n  <img class="logo" src="../../brandkit/assets/{lf}" alt="Plogy">'
                      f'\n  <div class="count">{i:02d}/{n:02d}</div>')
        dots = '<div class="dots">' + "".join('<i class="on"></i>' if k == i else "<i></i>" for k in range(1, n + 1)) + "</div>"
        parts.append(f'<!-- {i:02d} -->\n<section class="slide t-{s["theme"]} p{i} {s["cls"]}" data-n="{i}">{chrome}\n  {inner}\n  {dots}\n</section>')
    doc = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{esc(title)}</title>
<!-- {comment}
     Vista previa: abrir sin parámetros. Una lámina sola: carrusel.html?s=1 ... ?s={n}
     Generado por generar.py con la plantilla _comun/plogy.py. Editar generar.py y volver a correrlo.
     Exportar: python _comun/render.py <carpeta de la pieza>
     Tipografía: Screener solo tiene licencia DEMO, por eso el display usa Space Grotesk (respaldo del brand kit). -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<style>{CSS}
/* propio de la pieza */
{extra_css}
</style>
</head>
<body>

{chr(10).join(parts)}

{SCRIPT}
</body>
</html>
"""
    (out_dir / "carrusel.html").write_text(doc, encoding="utf-8")
    print("ok", out_dir.name, n, "láminas")


# ---------- bloques reutilizables ----------

def _photo(photo, pos, shift, alt):
    st = f"object-position:{pos}"
    if shift:
        st += f";top:{-shift}px;-webkit-mask-image:linear-gradient(#000 78%,transparent);mask-image:linear-gradient(#000 78%,transparent)"
    return f'<img class="photo" src="assets/{photo}" alt="{esc(alt)}" style="{st}">' + '\n  <div class="shade"></div>\n'


def cta_glass(photo, eyebrow, word, motive, detail="", title=None, top=560, pos="center", alt="", shift=0):
    """CTA de palabra clave: tarjeta de vidrio sobre foto de la biblioteca."""
    t = f"<h2>{title}</h2>" if title else ""
    d = f"<span>{detail}</span>" if detail else ""
    size = ' class="m"' if len(word) > 8 else ""
    return (_photo(photo, pos, shift, alt) +
            f'  <div class="glass" style="top:{top}px">\n    <img class="sym" src="../../brandkit/assets/plogy-symbol.svg" alt="">\n'
            f'    <div class="ey">{eyebrow}</div>{t}\n    <small>Comenta</small>\n    <strong{size}>{word}</strong>\n'
            f'    <p>{motive}{d}</p>\n  </div>')


def cta_follow(photo, eyebrow, title, motive, top=600, pos="center", alt="", shift=0):
    """CTA de seguimiento: tarjeta de vidrio con Sigue a Plogy."""
    return (_photo(photo, pos, shift, alt) +
            f'  <div class="glass" style="top:{top}px">\n    <img class="sym" src="../../brandkit/assets/plogy-symbol.svg" alt="">\n'
            f'    <div class="ey">{eyebrow}</div>\n    <h2>{title}</h2>\n'
            f'    <div class="follow">Sigue a Plogy</div>\n    <p>{motive}</p>\n  </div>')


def criterio(title, support="", foto=None):
    s = f'<p class="support">{support}</p>' if support else ""
    band = f'<div class="cband"><img src="assets/{foto}" alt=""></div>\n  ' if foto else ""
    cls = "body cp" if foto else "body center"
    return (f'{band}<div class="{cls}">\n    <div class="crit-mark"><i>{ic("spark", 32)}</i>Criterio Plogy</div>\n'
            f'    <h2 class="l">{title}</h2>\n    {s}\n  </div>')


def fondo(img, alt=""):
    """Foto a sangre detrás del contenido (tema photo)."""
    return f'<img class="bgimg" src="assets/{img}" alt="{esc(alt)}">\n  <div class="fade"></div>\n  '


def polaroid(img, x, y, w, h, r=0, alt="", z=1):
    return (f'<div class="polaroid" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
            f'transform:rotate({r}deg);z-index:{z}"><img src="assets/{img}" alt="{esc(alt)}"></div>')


def noticia(fecha, fuente, marca=None):
    """Cabecera de noticia: fecha del anuncio y quién lo anunció."""
    lg = logo(marca, 30) if marca else ""
    return (f'<div class="pills"><div class="pill">Noticia · {fecha}</div>'
            f'<div class="pill ghost src-pill">{lg}{fuente}</div></div>')


CSS += """
.src-pill{gap:12px;text-transform:none;letter-spacing:0;font-size:27px;padding:13px 24px}
.t-dark .src-pill svg{filter:invert(1)}
.big2{display:flex;align-items:baseline;gap:22px}
.meter{width:100%;height:56px;border-radius:28px;background:var(--surface);overflow:hidden;position:relative}
.meter i{position:absolute;left:0;top:0;bottom:0;border-radius:28px;background:var(--orange)}
.chk{display:flex;flex-direction:column;gap:16px;width:100%}
.chk > div{display:grid;grid-template-columns:64px 1fr;gap:22px;align-items:center;border-radius:26px;padding:20px 24px;background:#fff;border:2px solid var(--line);font:600 33px/1.2 var(--display);color:var(--ink)}
.chk i{width:64px;height:64px;border-radius:18px;background:var(--orange);color:var(--ink);display:flex;align-items:center;justify-content:center;font:700 32px/1 var(--display);font-style:normal}
.chk span{display:block;margin-top:6px;font:400 25px/1.3 var(--body);color:var(--muted)}
.t-dark .chk > div{background:var(--card);border-color:var(--cardLine);color:#fff}
.t-dark .chk span{color:var(--soft)}
.know{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:100%}
.know > div{border-radius:30px;padding:28px 26px}
.know .y{background:#fff;border:2px solid var(--line)} .know .n{background:transparent;border:2px dashed var(--border)}
.know small{display:block;font:700 21px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;margin-bottom:16px}
.know .y small{color:var(--orangeText)} .know .n small{color:var(--muted)}
.know p{font:500 32px/1.3 var(--body);padding:16px 0;border-top:2px solid var(--line)}
.know p:first-of-type{border-top:0}
.know .n p{color:var(--muted);border-top-style:dashed}
"""

CSS += """
/* criterio con banda de foto arriba */
.cband{position:absolute;left:0;right:0;top:0;height:560px;z-index:1;overflow:hidden}
.cband img{width:100%;height:100%;object-fit:cover;display:block}
.cband::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(23,19,16,.6) 0%,rgba(23,19,16,0) 32%,rgba(255,91,0,0) 62%,#ff5b00 100%)}
.body.cp{top:560px;justify-content:center}
.body.cp h2.l{font-size:72px}
.body.cp .crit-mark{margin-bottom:24px}
.has-band .count{color:#fff;opacity:.85}
/* foto a sangre detrás del contenido */
.t-photo .bgimg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0}
.t-photo .fade{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(18,13,10,.8) 0%,rgba(18,13,10,.25) 28%,rgba(18,13,10,.35) 52%,rgba(18,13,10,.95) 100%)}
.t-photo h1,.t-photo h2{color:#fff}
.t-photo .support{color:#e6dfd8} .t-photo .support b{color:#fff}
.t-photo .src{color:#cfc6bd}
.t-photo .pill.ghost{border-color:rgba(255,255,255,.45);color:#fff}
.t-photo .src-pill svg{filter:invert(1)}
.t-photo .eyebrow{color:#ffb48a}
"""
