"""Pieza 027 · ChatGPT Ads llega a Colombia (noticia)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, logo, cta_follow, criterio, noticia

HERE = pathlib.Path(__file__).resolve().parent
ILUS = '<span class="ilus">Ilustración</span>'
SRC = 'Fuente: OpenAI, "ChatGPT Ads expands to 26 new countries", 21 oct 2026.'

CSS = """
.p1 .hero{position:relative;width:100%;border-radius:30px;overflow:hidden;box-shadow:0 40px 90px rgba(0,0,0,.5);transform:rotate(-2deg)}
.p1 .hero img{display:block;width:100%;height:440px;object-fit:cover}
.p1 .flag{position:absolute;right:10px;bottom:-30px;z-index:3;background:var(--orange);color:var(--ink);border-radius:999px;padding:16px 26px;font:700 30px/1 var(--display);box-shadow:0 18px 40px rgba(0,0,0,.35);transform:rotate(3deg);display:flex;align-items:center;gap:12px}
.plans{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;width:100%}
.plans div{border-radius:26px;padding:26px 10px;text-align:center;border:2px solid var(--line);background:#fff}
.plans div.ad{background:var(--orange);border-color:var(--orange)}
.plans b{display:block;font:700 31px/1 var(--display)}
.plans span{display:flex;justify-content:center;margin-top:20px}
.plans small{display:block;margin-top:14px;font:700 17px/1.2 var(--display);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.plans .ad small{color:var(--ink)}
.countries{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.countries span{font:700 30px/1 var(--display);border-radius:999px;padding:16px 24px;background:#fff;border:2px solid var(--line)}
.countries span.o{background:var(--orange);border-color:var(--orange)}
.countries span.g{background:transparent;border-style:dashed;color:var(--muted)}
.chatad .ans{font:400 28px/1.4 var(--body);color:var(--ink);padding:6px 4px 18px}
.chatad .spons{border-radius:22px;border:2px solid var(--line);padding:18px 20px;display:grid;grid-template-columns:76px 1fr;gap:18px;align-items:center;background:var(--surface)}
.chatad .spons .th{width:76px;height:76px;border-radius:16px;background:var(--grad)}
.chatad .spons small{display:block;font:700 17px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.chatad .spons b{display:block;margin-top:6px;font:700 28px/1.15 var(--display)}
.chatad .spons span{display:block;margin-top:4px;font:400 23px/1.25 var(--body);color:var(--muted)}
"""

s1 = f"""<div class="body">
    {noticia('21 oct', 'OpenAI', 'openai')}
    <div class="vis"><div style="position:relative;width:100%"><div class="hero"><img src="assets/openai-ads.jpg" alt="Imagen oficial de OpenAI: ChatGPT Ads expands to 26 new countries">
      </div><div class="flag">{ic('globe',30,'#171310')}Colombia incluida</div></div></div>
    <h1>ChatGPT ya puede mostrar anuncios <span class="hl">en Colombia.</span></h1>
  </div>"""

def plan(n, ad):
    if ad:
        return f'<div class="ad"><b>{n}</b><span>{ic("check",40,"#171310",3)}</span><small>Con anuncios</small></div>'
    return f'<div><b>{n}</b><span>{ic("x",40,"#a39486",3)}</span><small>Sin anuncios</small></div>'

s2 = f"""<div class="body">
    <h2>Los anuncios salen solo en los planes <span class="hl t">Gratis y Go.</span></h2>
    <div class="vis"><div class="plans">{plan('Gratis',1)}{plan('Go',1)}{plan('Plus',0)}{plan('Pro',0)}{plan('Enterprise',0)}</div></div>
    <p class="support">Quien paga Plus, Pro o Enterprise sigue sin ver publicidad.</p>
  </div>"""

s3 = f"""<div class="body">
    <div class="big2"><div class="stat">89</div><h3>países con anuncios<br>en ChatGPT</h3></div>
    <div class="gap"></div>
    <h2 class="s">Después de México y Brasil, llega a <span class="hl t">14 países más</span> de Latinoamérica.</h2>
    <div class="countries"><span class="g">México</span><span class="g">Brasil</span><span>Argentina</span><span>Chile</span><span class="o">Colombia</span><span>Perú</span><span class="g">y 10 que OpenAI no nombra</span></div>
  </div>"""

s4 = f"""<div class="body">
    <h2>Para un negocio, es <span class="hl">un canal nuevo</span> de anuncios.</h2>
    <div class="vis"><div class="card chatad" style="width:100%">{ILUS}<div class="hd">{logo('openai',30)}ChatGPT</div>
      <div class="chat"><div class="msg u">¿Dónde compro café de origen para regalar?</div></div>
      <div class="ans">Puedes buscar tostadores locales que vendan por internet y envíen a tu ciudad…</div>
      <div class="spons"><div class="th"></div><div><small>Patrocinado</small><b>Café Monte · Cajas de regalo</b><span>Envío a todo el país</span></div></div>
    </div></div>
    <p class="support">Se compra en el Ads Manager de OpenAI o a través de sus socios.</p>
  </div>"""

s5 = f"""<div class="body">
    <h2>Lo que dice OpenAI y <span class="hl t">lo que todavía no.</span></h2>
    <div class="vis"><div class="know">
      <div class="y"><small>Lo que dice</small><p>Más de 100.000 anunciantes ya hicieron campañas.</p><p>No comparte las conversaciones con los anunciantes.</p><p>No vende datos de los usuarios.</p></div>
      <div class="n"><small>Lo que no dice</small><p>Cuánto cuesta un clic o una impresión.</p><p>Si hay un presupuesto mínimo.</p><p>Qué formatos hay en cada país.</p></div>
    </div></div>
  </div>"""

s6 = criterio("Antes de pagar por aparecer en ChatGPT, <span class='w'>pregúntale qué recomienda cuando alguien busca lo que vendes.</span>",
              "Ese es tu punto de partida. Y mirarlo no cuesta nada.", foto="crit-ojo-monitor.jpg")

s7 = cta_follow("cta-ojos.jpg", "Noticias de IA para tu negocio", "Te contamos qué cambia y qué no.",
                "Aquí la IA se implementa, no se promete.", top=700,
                alt="Unos ojos gigantes en una valla miran a una persona sola en el andén de una estación")

slides = [slide("dark", s1, src=SRC), slide("surface", s2, src=SRC), slide("light", s3.replace('class="body"','class="body center"',1), src=SRC),
          slide("light", s4), slide("light", s5.replace('class="body"','class="body center"',1).replace('<div class="vis">','<div class="gap l"></div><div>'), src=SRC), slide("orange", s6), slide("photo", s7)]

build(HERE, "Pieza 027 · ChatGPT Ads llega a Colombia",
      "Fuente editable. 7 láminas de 1080x1350. Noticia. Fuente: openai.com/index/chatgpt-ads-expands-26-new-countries (21 oct 2026). Imagen oficial de OpenAI en la portada. Lámina 4 es ilustración.",
      slides, CSS)
