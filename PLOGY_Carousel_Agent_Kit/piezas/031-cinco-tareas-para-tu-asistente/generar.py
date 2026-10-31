"""Pieza 031 · Cinco tareas para tu asistente de IA (clase del jueves, 2 de 4)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, logo, cta_glass, criterio
import clase as C

HERE = pathlib.Path(__file__).resolve().parent
ILUS = '<span class="ilus">Ilustración</span>'

CSS = """
.p1 .stack{position:relative;z-index:2;width:640px;margin-right:auto;transform:rotate(-2deg)}
.p1 .vis{position:relative}
.p1 .row{padding:10px 20px;grid-template-columns:56px 1fr auto}
.p1 .row .ic{width:56px;height:56px}
.p1 .row b{font-size:30px}
.p1 h1{font-size:80px}
.p1 .rows{gap:10px}
.mail .r{display:grid;grid-template-columns:1fr auto;gap:16px;align-items:center;padding:16px 0;border-top:2px solid var(--line)}
.mail .r:first-of-type{border-top:0}
.mail .r b{display:block;font:700 28px/1.1 var(--display)}
.mail .r span{display:block;margin-top:5px;font:400 24px/1.2 var(--body);color:var(--muted)}
.mail em{font:700 18px/1 var(--display);font-style:normal;letter-spacing:.1em;text-transform:uppercase;border-radius:999px;padding:10px 13px;background:var(--surface);color:var(--muted);white-space:nowrap}
.mail em.o{background:var(--orange);color:var(--ink)} .mail em.i{background:var(--ink);color:#fff}
.draft{margin-top:14px;border-radius:22px;background:var(--ink);color:#fff;padding:20px 24px;font:400 26px/1.35 var(--body)}
.draft small{display:block;font:700 17px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--orange);margin-bottom:8px}
.meet{width:100%;display:flex;flex-direction:column;gap:16px}
.ev{display:flex;align-items:center;gap:20px;background:var(--ink);color:#fff;border-radius:26px;padding:22px 26px}
.ev .t{font:700 40px/1 var(--display);color:var(--orange)}
.ev b{font:700 30px/1.15 var(--display)} .ev span{display:block;margin-top:4px;font:400 23px/1 var(--body);color:var(--soft)}
.brief .r{display:grid;grid-template-columns:150px 1fr;gap:18px;padding:16px 0;border-top:2px solid var(--line);font:400 28px/1.3 var(--body)}
.brief .r:first-of-type{border-top:0}
.brief .r small{font:700 19px/1.4 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--orangeText)}
.p5 .card{width:100%}
.p6 .card{width:100%;padding:26px 24px 10px}
"""

def task(i, icon, t, s, em="", on=False):
    e = f'<em class="o">{em}</em>' if em else "<span></span>"
    return f'<div class="row{" on" if on else ""}"><div class="ic">{ic(icon,32)}</div><div><b>{t}</b></div>{e}</div>'

s1 = f"""<div class="body">
    <div class="pill">Clase · {C.DIA}</div>
    <div class="vis">{polaroid("foto-estudiantes.jpg", 560, 30, 330, 410, 5, "Dos estudiantes en una clase de Plogy")}<div class="rows stack">
      {task(1,'mail','Ordenar tu correo','')}
      {task(2,'cal','Preparar tus reuniones','')}
      {task(3,'users','Hacer seguimiento','','',True)}
      {task(4,'chat','Responder lo de siempre','')}
      {task(5,'search','Investigar antes de decidir','')}
    </div></div>
    <h1>5 tareas para tu asistente de IA <span class="hl">esta semana.</span></h1>
  </div>"""

s2 = f"""<div class="body">
    <div class="kick"><i>1</i><span>Tu correo</span></div>
    <h2>Te resume lo que entró y deja <span class="hl">los borradores listos.</span></h2>
    <div class="vis"><div class="card mail" style="width:100%">{ILUS}<div class="hd">{ic('mail',30)}Hoy · 14 correos</div>
      <div class="r"><div><b>Proveedor de empaques</b><span>Se retrasa la entrega del jueves</span></div><em class="o">Urgente</em></div>
      <div class="r"><div><b>Laura Gómez</b><span>Cotización para 200 unidades</span></div><em class="i">Responder hoy</em></div>
      <div class="r"><div><b>Banco</b><span>Extracto de octubre</span></div><em>Leer luego</em></div>
      <div class="draft"><small>Borrador listo</small>Hola Laura, te comparto la cotización para 200 unidades…</div>
    </div></div>
    <p class="support">Tú revisas y envías.</p>
  </div>"""

s3 = f"""<div class="body">
    <div class="kick"><i>2</i><span>Tus reuniones</span></div>
    <h2>Antes de cada llamada, <span class="hl">un resumen del cliente.</span></h2>
    <div class="vis"><div class="meet">
      <div class="ev"><div class="t">10:00</div><div><b>Llamada con Distribuidora Andina</b><span>En 30 minutos</span></div></div>
      <div class="card brief">{ILUS}<div class="hd"><span class="av"></span>Tu asistente</div>
        <div class="r"><small>Compró</small><div>Tres pedidos este año, el último en agosto.</div></div>
        <div class="r"><small>Pidió</small><div>Descuento por volumen en la última llamada.</div></div>
        <div class="r"><small>Pendiente</small><div>Enviarle el catálogo nuevo.</div></div>
      </div>
    </div></div>
  </div>"""

def fu(name, what, days, hot=False):
    return f'<div class="row"><div class="ic">{ic("user",32)}</div><div><b>{name}</b><span>{what}</span></div><em class="{"o" if hot else ""}">{days}</em></div>'

s4 = f"""<div class="body">
    <div class="kick"><i>3</i><span>Seguimiento</span></div>
    <h2>Te avisa a quién <span class="hl">no le has respondido.</span></h2>
    <div class="vis" style="flex-direction:column;align-items:stretch;justify-content:center;gap:0">
      <div class="card flat" style="padding:24px 24px 26px">{ILUS}<div class="hd">{ic('clock',30)}Sin respuesta</div>
      <div class="rows">
        {fu('Andrés Rojas','Pidió precio el lunes pasado','8 días',True)}
        {fu('Hotel Sierra','Quedó en confirmar el pedido','5 días',True)}
        {fu('Laura Gómez','Te mandó una pregunta','3 días')}
      </div></div>
    </div>
    <p class="support">El cliente que se enfría casi nunca avisa.</p>
  </div>"""

s5 = f"""<div class="body">
    <div class="kick"><i>4</i><span>Preguntas frecuentes</span></div>
    <h2>Responde lo de siempre, con tus precios y <span class="hl">en tu tono.</span></h2>
    <div class="vis"><div class="card ink">{ILUS}<div class="hd"><span class="av"></span>Café Monte · Asistente</div>
      <div class="chat">
        <div class="msg a" style="align-self:flex-end;background:#3a322c">¿Hacen envíos a Cali?</div>
        <div class="msg u" style="align-self:flex-start">Sí, a todo el país. A Cali llega en 2 o 3 días hábiles.</div>
        <div class="msg a" style="align-self:flex-end;background:#3a322c">¿Y si pido tres bolsas?</div>
        <div class="msg u" style="align-self:flex-start">Desde tres, el envío no tiene costo.</div>
      </div></div></div>
    <p class="support">Y lo que no sabe, <b>te lo pasa a ti.</b></p>
  </div>"""

s6 = f"""<div class="body">
    <div class="kick"><i>5</i><span>Investigar</span></div>
    <h2>Compara opciones y te entrega <span class="hl">una tabla.</span></h2>
    <div class="vis"><div class="card">{ILUS}<div class="hd">{ic('table',30)}Proveedores de empaque</div>
      <table class="tbl">
        <tr><th>Proveedor</th><th>Por unidad</th><th>Entrega</th><th>Mínimo</th></tr>
        <tr><td><b>Empaques A</b></td><td>$1.200</td><td>5 días</td><td>500</td></tr>
        <tr class="on"><td><b>Empaques B</b></td><td class="o">$980</td><td>8 días</td><td>1.000</td></tr>
        <tr><td><b>Empaques C</b></td><td>$1.150</td><td class="o">2 días</td><td>200</td></tr>
      </table></div></div>
    <p class="support">La decisión <b>sigue siendo tuya.</b></p>
  </div>"""

s7 = criterio("Delega lo que <span class='w'>sabrías hacer tú.</span>",
              "Así puedes revisar lo que te entrega. Lo que todavía no sabes revisar, todavía no se delega.", foto="crit-campo.jpg")

s8 = cta_glass("cta-morado.jpg", f"{C.DIA} · {C.HORA}", C.PALABRA, C.MOTIVO,
               title="Te enseñamos a crear tu asistente de IA.", top=640, shift=230,
               alt="Ilustración de un hombre recostado frente a su computador, con los pies sobre el escritorio")

slides = [slide("light", s1), slide("light", s2), slide("surface", s3), slide("light", s4),
          slide("dark", s5), slide("light", s6), slide("orange", s7), slide("photo", s8)]

build(HERE, "Pieza 031 · Cinco tareas para tu asistente de IA",
      "Fuente editable. 8 láminas de 1080x1350. Clase del jueves (2 de 4), CTA Comenta CLASE. Correos, clientes, precios y proveedores son ejemplos rotulados Ilustración.",
      slides, CSS)
