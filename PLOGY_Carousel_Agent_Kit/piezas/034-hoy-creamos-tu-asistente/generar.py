"""Pieza 034 · Hoy creamos tu asistente (clase del jueves, 4 de 4; se publica el jueves en la mañana)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, cta_glass, criterio
import clase as C

HERE = pathlib.Path(__file__).resolve().parent

CSS = """
.ticket{position:relative;width:100%;display:grid;grid-template-columns:1fr 250px;border-radius:34px;overflow:hidden;transform:rotate(-3deg);box-shadow:0 40px 80px rgba(0,0,0,.45)}
.ticket .a{background:#fff;color:var(--ink);padding:38px 40px}
.ticket .a small{display:block;font:700 22px/1 var(--display);letter-spacing:.14em;text-transform:uppercase;color:var(--orangeText)}
.ticket .a b{display:block;margin-top:16px;font:700 54px/1.02 var(--display);letter-spacing:-.03em}
.ticket .a .meta{display:flex;gap:26px;margin-top:26px;font:600 30px/1 var(--display)}
.ticket .a .meta span{display:flex;align-items:center;gap:10px}
.ticket .a .meta svg{color:var(--orange)}
.ticket .b{background:var(--orange);color:var(--ink);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;border-left:4px dashed rgba(23,19,16,.35);text-align:center}
.ticket .b small{font:700 20px/1 var(--display);letter-spacing:.14em;text-transform:uppercase}
.ticket .b b{font:700 52px/1 var(--display);letter-spacing:-.03em}
.ticket::before,.ticket::after{content:"";position:absolute;right:232px;width:36px;height:36px;border-radius:50%;background:var(--ink);z-index:2}
.ticket::before{top:-18px} .ticket::after{bottom:-18px}
.notes{position:relative;width:100%;height:100%}
.p3 .polaroid img{object-position:center 40%}
.notes .sticky{position:absolute;width:410px;font-size:38px;padding:34px 34px}
.p2 .row{padding:28px 28px;grid-template-columns:84px 1fr auto}
.p2 .row .ic{width:84px;height:84px}
.p2 .row b{font-size:40px}
.p2 .row span{font-size:30px}
.p2 .rows{gap:20px}
"""

s1 = fondo("fondo-clase-noche.jpg", "Clase de noche de Plogy: personas frente a una pantalla en una sala con muro de vidrio") + f"""<div class="body">
    <div class="pill">Hoy · {C.DIA}</div>
    <div class="vis"><div class="ticket">
      <div class="a"><small>Clase de Plogy</small><b>Crea tu asistente de IA</b>
        <div class="meta"><span>{ic('cal',32)}{C.DIA}</span><span>{ic('clock',32)}{C.HORA}</span></div></div>
      <div class="b"><small>Clase</small><b>En vivo</b></div>
    </div></div>
    <h1>Hoy creamos <span class="hl">tu asistente de IA.</span></h1>
    <p class="support">Una clase para pasar del chat a un asistente que te quita trabajo.</p>
  </div>"""

def who(icon, t, s):
    return f'<div class="row"><div class="ic">{ic(icon,34)}</div><div><b>{t}</b><span>{s}</span></div><span></span></div>'

s2 = f"""<div class="body">
    <h2>Es para ti si usas la IA <span class="hl">como un chat</span> y quieres más.</h2>
    <div class="vis"><div class="rows" style="width:100%">
      {who('cart','Tienes un negocio','y respondes lo mismo todos los días.')}
      {who('users','Estás en un equipo comercial','y haces el seguimiento a mano.')}
      {who('pen','Trabajas por tu cuenta','y el correo se te come la mañana.')}
    </div></div>
  </div>"""

def note(x, y, r, text, cls=""):
    return f'<div class="sticky {cls}" style="left:{x}px;top:{y}px;transform:rotate({r}deg)">{text}</div>'

s3 = f"""<div class="body">
    <h2>Trae una tarea que <span class="hl">repites cada semana.</span></h2>
    <div class="vis"><div class="notes">
      {note(0,110,-4,'Responder cotizaciones')}
      {note(470,80,3,'Armar el reporte del lunes','o')}
      {note(30,390,2,'Agendar citas y confirmarlas','i')}
      {note(480,370,-3,'Contestar lo mismo por WhatsApp')}
    </div></div>
    <p class="support">Con una tarea tuya, la clase trabaja <b>sobre tu caso.</b></p>
  </div>"""

s4 = criterio("Un asistente se prueba con tu trabajo, <span class='w'>no con ejemplos de internet.</span>",
              "Por eso te pedimos que traigas una tarea tuya.", foto="crit-pantallas.jpg")

s5 = cta_glass("cta-multitud.jpg", f"Hoy · {C.HORA}", C.PALABRA, C.MOTIVO,
               title="Te enseñamos a crear tu asistente de IA.", top=600,
               alt="Vista desde arriba de una multitud en movimiento; una persona quieta destaca en el centro")

slides = [slide("photo", s1), slide("light", s2), slide("surface", s3), slide("orange", s4), slide("photo", s5)]

build(HERE, "Pieza 034 · Hoy creamos tu asistente de IA",
      "Fuente editable. 5 láminas de 1080x1350. Clase del jueves (4 de 4, último llamado), CTA Comenta CLASE. Sin datos.",
      slides, CSS)
