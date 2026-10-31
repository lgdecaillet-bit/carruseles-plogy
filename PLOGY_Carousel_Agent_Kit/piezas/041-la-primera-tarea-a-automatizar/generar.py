"""Pieza 041 · ¿Qué tarea automatizar primero? (lead magnet, Comenta TAREAS)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, cta_glass, criterio

HERE = pathlib.Path(__file__).resolve().parent
ILUS = '<span class="ilus">Ilustración</span>'

CSS = """
.score{width:100%}
.score .r{display:grid;grid-template-columns:1fr 260px 70px;gap:20px;align-items:center;padding:16px 0;border-top:2px solid var(--line)}
.score .r:first-of-type{border-top:0}
.score .r b{font:700 30px/1.15 var(--display)}
.score .bar{height:18px;border-radius:9px;background:var(--surface);overflow:hidden}
.score .bar i{display:block;height:100%;border-radius:9px;background:var(--border)}
.score .r.on .bar i{background:var(--orange)}
.score .r strong{font:700 34px/1 var(--display);text-align:right;color:var(--muted)}
.score .r.on strong{color:var(--orangeText)}
.tally .r{display:grid;grid-template-columns:1fr auto;gap:20px;align-items:center;padding:16px 0;border-top:2px dashed var(--line);font:600 32px/1.2 var(--display)}
.tally .r:first-of-type{border-top:0}
.tally .r span{font:500 30px/1 var(--mono);color:var(--orangeText);letter-spacing:.06em}
.notes3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;width:100%}
.notes3 > div{border-radius:30px;background:#fff;border:2px solid var(--line);padding:28px 24px;text-align:center}
.notes3 i{width:84px;height:84px;margin:0 auto;border-radius:24px;background:var(--surface);color:var(--orange);display:flex;align-items:center;justify-content:center}
.notes3 b{display:block;margin-top:22px;font:700 38px/1.1 var(--display)}
.notes3 span{display:block;margin-top:12px;font:400 29px/1.3 var(--body);color:var(--muted)}
.notes3 em{display:block;margin-top:22px;font:700 30px/1 var(--display);font-style:normal;color:var(--orangeText)}
.notes3 > div{padding:40px 22px}
.p5 .tbl td{font-size:28px}
.p5 .tbl td:last-child{text-align:right;font:700 34px/1 var(--display)}
.p5 .tbl th:last-child{text-align:right}
.p5 .tbl tr.on td{background:rgba(255,91,0,.14)}
.p5 .tbl tr.on td:last-child{color:var(--orange)}
.p5 .tbl td{border-top-color:#3a322c;color:#f1ebe5}
"""

def sc(t, v, on=False):
    return f'<div class="r{" on" if on else ""}"><b>{t}</b><div class="bar"><i style="width:{v/15*100:.0f}%"></i></div><strong>{v}</strong></div>'

s1 = f"""<div class="body">
    <div class="vis"><div class="card score">{ILUS}<div class="hd">{ic('list',30)}Puntaje de cada tarea (máximo 15)</div>
      {sc('Responder precios por WhatsApp',12,True)}
      {sc('Pasar pedidos a Excel',11)}
      {sc('Confirmar citas',10)}
      {sc('Reporte de ventas del mes',7)}
    </div></div>
    <h1>¿Qué tarea de tu negocio <span class="hl">deberías automatizar primero?</span></h1>
  </div>"""

s2 = f"""<div class="body">
    <h2>Casi todos empiezan por la que <span class="hl">más les molesta.</span></h2>
    <div class="vis"><div class="vs" style="width:100%">
      <div class="no"><small>La que molesta</small><b>Reporte de ventas del mes</b><ul><li>Una vez al mes</li><li>Cada mes cambia</li><li>Nadie sabe el paso a paso</li></ul></div>
      <div class="yes"><small>La que conviene</small><b>Responder precios</b><ul><li>34 veces en la semana</li><li>Siempre igual</li><li>Las respuestas ya existen</li></ul></div>
    </div></div>
    <p class="support">Para saber cuál te devuelve más tiempo, <b>hay que contar.</b> <span style="font-size:24px">(Ilustración)</span></p>
  </div>"""

s3 = f"""<div class="body">
    <div class="kick"><i>1</i><span>Anota</span></div>
    <h2>Durante una semana, anota <span class="hl">todo lo que se repite.</span></h2>
    <div class="vis"><div class="card tally" style="width:100%">{ILUS}<div class="hd">{ic('pen',28)}Lunes a viernes</div>
      <div class="r">Responder precios<span>34 veces</span></div>
      <div class="r">Confirmar citas<span>9 veces</span></div>
      <div class="r">Pasar pedidos a Excel<span>4 veces</span></div>
      <div class="r">Reporte de ventas del mes<span>1 al mes</span></div>
    </div></div>
  </div>"""

s4 = f"""<div class="body">
    <div class="kick"><i>2</i><span>Califica</span></div>
    <h2>Ponle tres notas de 1 a 5 <span class="hl">a cada una.</span></h2>
    <div class="vis"><div class="notes3">
      <div><i>{ic('repeat',44)}</i><b>Cuántas veces</b><span>¿Se repite a diario o una vez al mes?</span><em>1 a 5</em></div>
      <div><i>{ic('clock',44)}</i><b>Cuánto tiempo</b><span>¿Minutos u horas cada vez?</span><em>1 a 5</em></div>
      <div><i>{ic('list',44)}</i><b>Qué tan claro</b><span>¿Podrías escribir el paso a paso?</span><em>1 a 5</em></div>
    </div></div>
  </div>"""

s5 = f"""<div class="body">
    <div class="kick"><i>3</i><span>Suma</span></div>
    <h2>La que más suma es <span class="hl">tu primera.</span></h2>
    <div class="vis"><div class="card ink" style="width:100%">{ILUS}<div class="hd">{ic('table',30)}Resultado</div>
      <table class="tbl">
        <tr><th>Tarea</th><th>Veces</th><th>Tiempo</th><th>Claro</th><th>Total</th></tr>
        <tr class="on"><td><b>Responder precios</b></td><td>5</td><td>2</td><td>5</td><td>12</td></tr>
        <tr><td><b>Pedidos a Excel</b></td><td>4</td><td>4</td><td>3</td><td>11</td></tr>
        <tr><td><b>Confirmar citas</b></td><td>4</td><td>2</td><td>4</td><td>10</td></tr>
        <tr><td><b>Reporte del mes</b></td><td>1</td><td>5</td><td>1</td><td>7</td></tr>
      </table></div></div>
  </div>"""

s6 = criterio("La primera tarea no se elige por ambición. <span class='w'>Se elige porque la puedes medir el lunes siguiente.</span>",
              "Si a la semana no sabes cuánto tiempo te ahorró, todavía no era esa.", foto="crit-mesa-decision.jpg")

s7 = cta_glass("cta-teclado.jpg", "Una semana anotando, 15 minutos para elegir", "TAREAS",
               "y te mandamos la plantilla para calificar las tareas de tu negocio.", top=600,
               alt="Una mano presiona una tecla iluminada de un teclado gigante")

slides = [slide("light", s1), slide("surface", s2), slide("light", s3), slide("light", s4),
          slide("dark", s5), slide("orange", s6), slide("photo", s7)]

build(HERE, "Pieza 041 · La primera tarea a automatizar",
      "Fuente editable. 7 láminas de 1080x1350. Lead magnet, CTA Comenta TAREAS (plantilla de diagnóstico). Tareas y notas son ejemplos rotulados Ilustración.",
      slides, CSS)
