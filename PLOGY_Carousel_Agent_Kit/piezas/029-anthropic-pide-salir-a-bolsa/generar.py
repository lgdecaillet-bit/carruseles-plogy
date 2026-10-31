"""Pieza 029 · Anthropic pide salir a bolsa (noticia del día)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, logo, cta_follow, criterio, noticia

HERE = pathlib.Path(__file__).resolve().parent
SRC = 'Fuente: Anthropic, anuncio del Form S-1 ante la SEC, 26 oct 2026. Esta pieza no es una recomendación de inversión.'

CSS = """
.tick{position:relative;width:100%;border-radius:34px;background:#fff;color:var(--ink);padding:40px 44px;box-shadow:0 40px 90px rgba(0,0,0,.5);transform:rotate(-2deg)}
.tick .top{display:flex;align-items:center;gap:18px}
.tick .top .lg{box-shadow:none;background:var(--surface)}
.tick .top b{font:700 40px/1 var(--display)}
.tick .top span{display:block;margin-top:8px;font:500 24px/1 var(--body);color:var(--muted)}
.tick .sym{margin-top:34px;display:flex;align-items:baseline;gap:22px}
.tick .sym strong{font:700 150px/.9 var(--display);letter-spacing:-.05em}
.tick .sym em{font:700 30px/1 var(--display);font-style:normal;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.tick .price{margin-top:26px;display:flex;align-items:center;gap:16px;border-radius:20px;border:2px dashed var(--border);padding:20px 24px;font:600 30px/1.2 var(--display);color:var(--muted)}
"""

s1 = fondo("fondo-mercado.jpg", "Dos siluetas de traje hablan en voz baja; una línea roja sube detrás") + f"""<div class="body">
    {noticia('Hoy, 26 oct', 'Anthropic', 'anthropic')}
    <div class="vis"><div class="tick">
      <div class="top"><div class="lg s">{logo('claude',52)}</div><div><b>Anthropic, PBC</b><span>La empresa que hace Claude</span></div></div>
      <div class="sym"><strong>ANT</strong><em>Nasdaq</em></div>
      <div class="price">{ic('clock',32)}Precio por acción: sin definir</div>
    </div></div>
    <h1>La empresa detrás de Claude <span class="hl">pidió salir a bolsa.</span></h1>
  </div>"""

def r(icon, t, s, on=False):
    return f'<div class="row{" on" if on else ""}"><div class="ic">{ic(icon,34)}</div><div><b>{t}</b><span>{s}</span></div><span></span></div>'

s2 = f"""<div class="body">
    <h2>Qué presentó: una solicitud <span class="hl t">ante el regulador de EE. UU.</span></h2>
    <div class="vis"><div class="rows" style="width:100%">
      {r('file','Formulario S-1','Es la solicitud para ofrecer acciones al público. Va a la SEC.')}
      {r('table','Acciones Clase A','Son las que se ofrecerían en la salida a bolsa.')}
      {r('chart','Nasdaq, símbolo ANT','Ahí piensa cotizar si la solicitud avanza.', True)}
    </div></div>
  </div>"""

def off(t, em="Sin definir"):
    return f'<div class="row off"><div class="ic">{ic("x",34)}</div><div><b>{t}</b></div><em>{em}</em></div>'

s3 = f"""<div class="body">
    <h2>Lo que <span class="hl t">todavía no se sabe.</span></h2>
    <div class="vis"><div class="rows" style="width:100%">
      {off('El precio de cada acción')}
      {off('Cuántas acciones va a ofrecer')}
      {off('La fecha en que empezaría a cotizar', 'No la da')}
    </div></div>
    <p class="support">La solicitud está presentada, pero <b>todavía no está vigente.</b></p>
  </div>"""

s4 = f"""<div class="body center">
    <div class="lg" style="margin-bottom:40px">{logo('claude',64)}</div>
    <h2 class="l">¿Y si usas Claude en tu negocio?</h2>
    <p class="support">El anuncio habla de acciones. <b>No menciona cambios en planes, precios ni productos.</b> Si llegan, saldrán en otro anuncio.</p>
    <div class="gap l"></div>
    <div class="pills">{''.join(f'<div class="pill ghost">{x}</div>' for x in ['Free','Pro','Max','Team','Enterprise'])}</div>
  </div>"""

s5 = criterio("La noticia es de la empresa. <span class='w'>La decisión de usar Claude sigue siendo de tu negocio,</span> y se toma con tu tarea en la mano.",
              "Si te ahorra tiempo en algo concreto, eso no lo cambia un formulario ante la SEC.", foto="crit-mesa.jpg")

s6 = cta_follow("cta-despegue.jpg", "Lo que pasa en IA, sin humo", "Leemos la noticia para que tú decidas.",
                "Noticias de IA explicadas desde el negocio.", top=330,
                alt="Un avión despega hacia un cielo morado y naranja")

slides = [slide("photo", s1, src=SRC), slide("light", s2, src=SRC), slide("surface", s3, src=SRC),
          slide("light", s4), slide("orange", s5), slide("photo", s6)]

build(HERE, "Pieza 029 · Anthropic pide salir a bolsa",
      "Fuente editable. 6 láminas de 1080x1350. Noticia del día. Fuente: anthropic.com/news/s1-sec (26 oct 2026). No es recomendación de inversión.",
      slides, CSS)
