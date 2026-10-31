"""Pieza 028 · Tu asistente de IA no es un chat (clase del jueves, 1 de 4)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, logo, cta_glass, criterio
import clase as C

HERE = pathlib.Path(__file__).resolve().parent

CSS = """
.p1 .duo{position:relative;width:100%;height:100%}
.p1 .polaroid img{object-position:center 40%}
.p1 .c1{position:absolute;left:150px;top:290px;width:380px;transform:rotate(-4deg);z-index:2}
.p1 .c2{position:absolute;right:0;top:90px;width:560px;transform:rotate(3deg);z-index:3}
.p1 .c1 .msg{font-size:26px;max-width:100%}
.done{display:flex;flex-direction:column;gap:14px}
.done div{display:grid;grid-template-columns:40px 1fr;gap:14px;align-items:start;font:500 27px/1.3 var(--body);color:#f1ebe5}
.done i{width:40px;height:40px;border-radius:12px;background:var(--orange);color:var(--ink);display:flex;align-items:center;justify-content:center}
.p2 .card{width:100%}
.doc .ln{font:500 30px/1.4 var(--mono);color:var(--ink);padding:14px 0;border-top:2px dashed var(--line)}
.doc .ln:first-of-type{border-top:0}
.doc .ln u{text-decoration:none;color:var(--orangeText);font-weight:700}
.files{position:relative;width:100%;height:100%}
.files .f{position:absolute;display:flex;align-items:center;gap:18px;background:#fff;border:2px solid var(--line);border-radius:24px;padding:20px 26px;box-shadow:0 18px 40px rgba(23,19,16,.12);font:700 29px/1 var(--display)}
.files .f span{display:block;margin-top:6px;font:400 22px/1 var(--body);color:var(--muted)}
.files .f .ic{width:58px;height:58px;border-radius:16px;background:var(--surface);display:flex;align-items:center;justify-content:center;color:var(--orange)}
.files .orb{position:absolute;left:50%;top:50%;width:200px;height:200px;margin:-100px 0 0 -100px}
.files svg.ln{position:absolute;inset:0;width:100%;height:100%}
.hub{position:relative;width:820px;height:600px}
.hub .orb{position:absolute;left:310px;top:200px;width:200px;height:200px}
.hub .lg{position:absolute}
.hub svg.ln{position:absolute;inset:0}
.lim{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:100%}
.lim > div{border-radius:30px;padding:26px 28px}
.lim .a{background:var(--surface)} .lim .b{background:var(--ink);color:#fff}
.lim small{display:block;font:700 21px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:18px}
.lim .b small{color:var(--orange)}
.lim p{display:flex;align-items:center;gap:14px;font:600 32px/1.2 var(--display);padding:10px 0}
.lim p i{color:var(--orange);display:flex}
.appr{margin-top:20px;width:100%}
.appr .btns{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:18px}
.appr .btns span{text-align:center;border-radius:999px;padding:18px;font:700 28px/1 var(--display)}
.appr .btns .n{border:2px solid var(--border);color:var(--muted)} .appr .btns .y{background:var(--orange);color:var(--ink)}
.appr p{font:500 30px/1.3 var(--body)}
"""

ILUS = '<span class="ilus">Ilustración</span>'

s1 = f"""<div class="body">
    <div class="pill">Clase · {C.DIA}</div>
    <div class="vis"><div class="duo">
      {polaroid("foto-clase-dia.jpg", 0, 0, 360, 440, -5, "Clase de Plogy con estudiantes frente a la pantalla")}
      <div class="card ink c2">{ILUS}<div class="hd"><span class="av"></span>Tu asistente</div>
        <div class="done"><div><i>{ic('check',24)}</i>Leí los 14 correos que entraron hoy.</div>
        <div><i>{ic('check',24)}</i>Tres piden cotización: te dejé los borradores.</div>
        <div><i>{ic('check',24)}</i>Mañana tienes reunión con Laura. Aquí va lo que compró.</div></div></div>
    </div></div>
    <h1>Tu asistente de IA no es <span class="hl">un chat con otro nombre.</span></h1>
    <p class="support">Son cuatro piezas. Sin ellas, sigues hablando con un chat.</p>
  </div>"""

s2 = f"""<div class="body">
    <h2>Un chat empieza <span class="hl">de cero</span> cada vez.</h2>
    <div class="vis"><div class="card">{ILUS}<div class="hd">{ic('chat',30)}Conversación nueva</div>
      <div class="chat">
        <div class="msg u dim">Te cuento otra vez: tengo una tienda de café, vendemos por Instagram…</div>
        <div class="msg u">…los precios están en un PDF, te lo pego. Y respondemos de tú, corto.</div>
        <div class="msg a">¡Perfecto! ¿En qué te ayudo hoy?</div>
      </div></div></div>
    <p class="support">Le vuelves a explicar tu negocio en cada conversación. Y lo que te responde <b>no sale de la pantalla.</b></p>
  </div>"""

s3 = f"""<div class="body">
    <div class="kick"><i>1</i><span>Instrucciones</span></div>
    <h2>Le dices quién es, para quién trabaja y <span class="hl">cómo responde.</span></h2>
    <div class="vis"><div class="card doc" style="width:100%">{ILUS}<div class="hd">{ic('file',30)}Instrucciones del asistente</div>
      <div class="ln">Eres el asistente de <u>Café Monte</u>.</div>
      <div class="ln">Respondes en español, de tú y en pocas líneas.</div>
      <div class="ln">Si no sabes un precio, <u>no lo inventes</u>: pregúntame.</div>
    </div></div>
  </div>"""

def f(x, y, name, sub, icon):
    return f'<div class="f" style="left:{x}px;top:{y}px"><div class="ic">{ic(icon,32)}</div><div>{name}<span>{sub}</span></div></div>'

s4 = f"""<div class="body">
    <div class="kick"><i>2</i><span>Contexto</span></div>
    <h2>Lo que sabe de tu negocio <span class="hl">sin que se lo repitas.</span></h2>
    <div class="vis"><div class="files">
      <svg class="ln" viewBox="0 0 888 560"><g stroke="#ff5b00" stroke-width="3" stroke-dasharray="2 12" stroke-linecap="round" fill="none" opacity=".7">
        <path d="M200 90 L444 280"/><path d="M690 120 L444 280"/><path d="M190 470 L444 280"/><path d="M700 450 L444 280"/></g></svg>
      <div class="orb">{ic('brain',90,'#fff',1.6)}</div>
      {f(0,40,'precios-2026.pdf','Lista de precios','money')}
      {f(500,70,'clientes.xlsx','Quién compró qué','table')}
      {f(0,420,'preguntas.doc','Lo que siempre te preguntan','chat')}
      {f(500,400,'tono.doc','Cómo hablas tú','pen')}
    </div></div>
    <p class="support">Tus archivos, tus precios, tus clientes. Los cargas una vez.</p>
  </div>"""

# hub de herramientas
pos = [(30, 40, 'gmail'), (350, 0, 'googlecalendar'), (670, 40, 'googlesheets'), (30, 440, 'googledrive'), (350, 480, 'whatsapp'), (670, 440, 'notion')]
lines = "".join(f'<path d="M{x+60} {y+60} L410 300"/>' for x, y, _ in pos)
lgs = "".join(f'<div class="lg" style="left:{x}px;top:{y}px">{logo(n, 60)}</div>' for x, y, n in pos)
s5 = f"""<div class="body">
    <div class="kick"><i>3</i><span>Herramientas</span></div>
    <h2>Conectado a tu correo, tu agenda y tus hojas.</h2>
    <div class="vis"><div class="hub">
      <svg class="ln" viewBox="0 0 820 600" width="820" height="600"><g stroke="#ff5b00" stroke-width="3" stroke-dasharray="2 12" stroke-linecap="round" fill="none" opacity=".8">{lines}</g></svg>
      <div class="orb">{ic('bolt',84,'#fff',1.8)}</div>{lgs}
    </div></div>
    <p class="support">Ahí deja de responder y <b>empieza a hacer.</b></p>
  </div>"""

s6 = f"""<div class="body">
    <div class="kick"><i>4</i><span>Límites</span></div>
    <h2>Qué hace solo y qué <span class="hl">te pregunta antes.</span></h2>
    <div class="vis" style="flex-direction:column">
      <div class="lim">
        <div class="a"><small>Hace solo</small><p><i>{ic('check',30)}</i>Leer</p><p><i>{ic('check',30)}</i>Resumir</p><p><i>{ic('check',30)}</i>Preparar</p></div>
        <div class="b"><small>Te pregunta antes</small><p><i>{ic('lock',30)}</i>Enviar</p><p><i>{ic('lock',30)}</i>Pagar</p><p><i>{ic('lock',30)}</i>Borrar</p></div>
      </div>
      <div class="card appr">{ILUS}<div class="hd"><span class="av"></span>Tu asistente</div>
        <p>¿Envío esta cotización a Laura?</p>
        <div class="btns"><span class="n">Revisar</span><span class="y">Enviar</span></div></div>
    </div>
  </div>"""

s7 = criterio("La confianza en un asistente se da por permisos: <span class='w'>primero lee, después prepara y al final envía.</span>",
              "Cada permiso nuevo se gana con semanas de trabajo bien revisado.", foto="crit-manos.jpg")

s8 = cta_glass("cta-escalera.jpg", f"{C.DIA} · {C.HORA}", C.PALABRA, C.MOTIVO,
               title="Te enseñamos a crear tu asistente de IA.", top=560, shift=300,
               alt="Una persona sube una escalera iluminada hacia una abertura de luz")

slides = [
    slide("light", s1), slide("surface", s2), slide("light", s3), slide("light", s4),
    slide("dark", s5), slide("light", s6), slide("orange", s7), slide("photo", s8),
]

build(HERE, "Pieza 028 · Tu asistente de IA no es un chat",
      "Fuente editable. 8 láminas de 1080x1350. Clase del jueves (1 de 4), CTA Comenta CLASE. Todas las maquetas son ilustraciones rotuladas; no hay datos.",
      slides, CSS)
