"""Pieza 030 · WhatsApp Business vuelve a cobrar los mensajes de servicio (noticia)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, logo, cta_follow, criterio, noticia

HERE = pathlib.Path(__file__).resolve().parent
SRC = 'Fuente: Meta, "Updates to pricing", documentación de WhatsApp Business Platform (vigente desde el 1 oct 2026).'

CSS = """
.bill{position:relative;width:100%;transform:rotate(-1.5deg)}
.bill .r{display:grid;grid-template-columns:1fr auto auto;gap:22px;align-items:center;padding:18px 0;border-top:2px solid var(--line)}
.bill .r:first-of-type{border-top:0}
.bill .r b{font:700 30px/1.15 var(--display)} .bill .r span{display:block;margin-top:4px;font:400 23px/1 var(--body);color:var(--muted)}
.bill .was{font:600 26px/1 var(--display);color:var(--muted);text-decoration:line-through}
.bill .now{font:700 22px/1 var(--display);letter-spacing:.08em;text-transform:uppercase;background:var(--orange);border-radius:999px;padding:12px 16px}
.wa{position:absolute;right:-14px;top:-46px;width:110px;height:110px;border-radius:30px;background:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 18px 40px rgba(23,19,16,.18);transform:rotate(8deg)}
.tl2{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:100%}
.tl2 > div{border-radius:30px;padding:30px 28px}
.tl2 .a{background:var(--surface);border:2px dashed var(--border)} .tl2 .b{background:var(--ink);color:#fff}
.tl2 small{display:block;font:700 21px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.tl2 .b small{color:var(--orange)}
.tl2 b{display:block;margin-top:16px;font:700 44px/1.05 var(--display);letter-spacing:-.03em}
.tl2 p{margin-top:16px;font:400 27px/1.35 var(--body);color:var(--muted)} .tl2 .b p{color:var(--soft)}
.free .num{font:700 200px/.9 var(--display);letter-spacing:-.05em;color:var(--orange)}
.free .lbl{font:700 40px/1.1 var(--display);margin-top:10px}
.free .meter{margin-top:40px}
.free .scale{display:flex;justify-content:space-between;margin-top:12px;font:600 24px/1 var(--display);color:var(--muted)}
.conv{display:grid;grid-template-columns:1fr 1fr;gap:16px;width:100%;margin-top:30px}
.conv div{border-radius:26px;background:var(--card);border:2px solid var(--cardLine);padding:24px 24px}
.conv small{display:block;font:700 19px/1.2 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--dim)}
.conv b{display:block;margin-top:12px;font:700 46px/1 var(--display);color:var(--orange)}
.conv span{display:block;margin-top:8px;font:400 23px/1.3 var(--body);color:var(--soft)}
"""

s1 = f"""<div class="body">
    {noticia('1 oct', 'Meta', 'whatsapp')}
    <div class="vis" style="position:relative">{polaroid("foto-telefono.jpg", 610, 300, 290, 268, 7, "Collage de una mano con un teléfono", 4)}<div class="card bill" style="margin-bottom:120px">
      <div class="wa">{logo('whatsapp',64)}</div>
      <div class="hd">{ic('money',30)}Tu factura de WhatsApp Business</div>
      <div class="r"><div><b>Mensajes de servicio</b><span>Respuestas a tus clientes</span></div><em class="was">Gratis</em><em class="now">Se cobran</em></div>
      <div class="r"><div><b>Mensajes de utilidad</b><span>Dentro de la conversación</span></div><em class="was">Gratis</em><em class="now">Se cobran</em></div>
      <div class="r"><div><b>Agente de IA de Meta</b><span>Respuestas automáticas</span></div><em class="was"></em><em class="now">Por tokens</em></div>
    </div></div>
    <h1>La API de WhatsApp Business volvió a cobrar <span class="hl t">los mensajes de servicio.</span></h1>
  </div>"""

s2 = f"""<div class="body">
    <h2>Qué cambió <span class="hl t">el 1 de octubre.</span></h2>
    <div class="vis"><div class="tl2">
      <div class="a"><small>Desde nov 2024</small><b>Responder era gratis</b><p>Los mensajes de servicio no se cobraban.</p></div>
      <div class="b"><small>Desde el 1 oct 2026</small><b>Se cobra por mensaje</b><p>Servicio y utilidad dentro de la conversación vuelven a costar.</p></div>
    </div></div>
    <p class="support">Aplica a la plataforma de WhatsApp Business: la API, que usan los negocios con sistemas o chatbots.</p>
  </div>"""

s3 = f"""<div class="body">
    <div class="free"><div class="num">1.000</div><div class="lbl">mensajes de servicio gratis al mes, <span class="hl t">por cada número.</span></div>
      <div class="meter"><i style="width:62%"></i></div>
      <div class="scale"><span>0</span><span>1.000 · desde aquí se cobra</span></div></div>
    <div class="vis"></div>
    <p class="support">Los que no uses <b>no se acumulan</b> para el mes siguiente.</p>
  </div>"""

s4 = f"""<div class="body">
    <h2>El agente de IA de Meta <span class="hl">se cobra por tokens.</span></h2>
    <div class="gap"></div>
    <div class="big2"><div class="stat" style="font-size:190px">4 a 5</div><h3>centavos de dólar<br>por mensaje</h3></div>
    <p class="support">US$2 por millón de tokens. Según Meta, un mensaje usa entre 20.000 y 25.000.</p>
    <div class="conv">
      <div><small>Consulta simple · 4 mensajes</small><b>16 a 20 ¢</b><span>Estimado de Meta</span></div>
      <div><small>Conversación compleja · 10 mensajes</small><b>40 a 50 ¢</b><span>Estimado de Meta</span></div>
    </div>
  </div>"""

s5 = f"""<div class="body">
    <h2>Los anuncios que abren WhatsApp dan <span class="hl t">hasta 7 días sin cobro.</span></h2>
    <div class="vis"><div class="chk">
      <div><i>{ic('check',34)}</i><div>Mensajes de marketing, utilidad y servicio<span>Gratis mientras la ventana esté abierta</span></div></div>
      <div><i style="background:var(--ink);color:#fff">{ic('x',34)}</i><div>Mensajes del agente de IA de Meta<span>Se cobran igual, con o sin anuncio</span></div></div>
    </div></div>
    <p class="support">La ventana se abre cuando alguien escribe desde un anuncio en el teléfono, no desde la web.</p>
  </div>"""

s6 = criterio("Automatizar WhatsApp con IA ya tiene <span class='w'>un costo por conversación.</span> Haz la cuenta antes de conectarlo.",
              "Conversaciones al mes, cuántas resolvería el agente y cuánto vale cada venta. Si no da, todavía no.", foto="crit-scroll.jpg")

s7 = cta_follow("cta-anden.jpg", "Antes de que llegue la factura", "Te avisamos lo que cambia en tus herramientas.",
                "IA aplicada a negocios reales.", top=640,
                alt="Una mujer de negro en el andén de una estación, junto a un tren, con un bloque de texto naranja")

slides = [slide("light", s1, src=SRC), slide("surface", s2.replace('class="body"','class="body center"',1), src=SRC), slide("light", s3.replace('<div class="vis"></div>','<div class="gap l"></div>').replace('class="body"','class="body center"',1), src=SRC),
          slide("dark", s4, src=SRC), slide("light", s5, src=SRC), slide("orange", s6), slide("photo", s7)]

build(HERE, "Pieza 030 · WhatsApp Business vuelve a cobrar",
      "Fuente editable. 7 láminas de 1080x1350. Noticia. Fuente: developers.facebook.com/docs/whatsapp/pricing/updates-to-pricing (vigente 1 oct 2026). La factura de la portada es ilustración.",
      slides, CSS)
