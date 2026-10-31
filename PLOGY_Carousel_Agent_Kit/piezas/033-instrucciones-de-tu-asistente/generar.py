"""Pieza 033 · Las instrucciones de tu asistente (clase del jueves, 3 de 4)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, cta_glass, criterio
import clase as C

HERE = pathlib.Path(__file__).resolve().parent
ILUS = '<span class="ilus">Ilustración</span>'

CSS = """
.outline{position:relative;z-index:2;width:640px;margin-right:auto;transform:rotate(-1.5deg)}
.p1 .vis{position:relative}
.outline .sec{display:grid;grid-template-columns:54px 1fr;gap:18px;align-items:start;padding:14px 0;border-top:2px solid var(--line)}
.outline .sec:first-of-type{border-top:0}
.outline .sec i{width:54px;height:54px;border-radius:16px;background:var(--surface);color:var(--orange);display:flex;align-items:center;justify-content:center;font:700 28px/1 var(--display);font-style:normal}
.outline .sec b{display:block;font:700 30px/1.1 var(--display);margin-top:4px}
.outline .bars{margin-top:10px;display:flex;flex-direction:column;gap:7px}
.outline .bars u{display:block;height:9px;border-radius:5px;background:var(--line)}
.one{width:100%;text-align:center;padding:60px 40px}
.one code{font:500 52px/1.2 var(--mono);color:var(--ink)}
.one .verdict{margin-top:34px;display:inline-flex;gap:12px;align-items:center;font:700 22px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);border:2px dashed var(--border);border-radius:999px;padding:14px 20px}
.fields{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-bottom:36px}
.fields span{height:10px;border-radius:5px;background:rgba(23,19,16,.12)}
.fields span.on{background:var(--orange)} .fields span.d{background:rgba(255,91,0,.35)}
.t-dark .fields span{background:rgba(255,255,255,.14)} .t-dark .fields span.d{background:rgba(255,91,0,.45)} .t-dark .fields span.on{background:var(--orange)}
.ej{width:100%}
.ej .hd{margin-bottom:16px}
.ej .tx{font:500 35px/1.5 var(--mono);color:var(--ink)}
.bign{position:absolute;right:-30px;top:-120px;font:700 520px/1 var(--display);letter-spacing:-.06em;color:rgba(255,91,0,.09);z-index:0;pointer-events:none}
.t-dark .bign{color:rgba(255,91,0,.14)}
.ej{z-index:2}
.ej .tx u{text-decoration:none;color:var(--orangeText);font-weight:700}
.ej .tx p{padding:6px 0}
.card.ink.ej .tx{color:#f1ebe5} .card.ink.ej .tx u{color:var(--orange)}
"""

def bars(*w):
    return '<div class="bars">' + "".join(f'<u style="width:{x}%"></u>' for x in w) + "</div>"

FIELDS = ["Quién es", "Qué sabe", "Qué hace", "Qué no hace", "Cómo entrega"]

s1 = f"""<div class="body">
    <div class="pill">Clase · {C.DIA}</div>
    <div class="vis">{polaroid("foto-ensenando.jpg", 560, 20, 330, 420, 5, "Una persona enseña frente a una pantalla en una clase de Plogy")}<div class="card outline">{ILUS}<div class="hd">{ic('file',30)}instrucciones-del-asistente</div>
      <div class="sec"><i>1</i><div><b>Quién es y para quién trabaja</b>{bars(90,60)}</div></div>
      <div class="sec"><i>2</i><div><b>Qué sabe de tu negocio</b>{bars(80,95,40)}</div></div>
      <div class="sec"><i>3</i><div><b>Qué hace y en qué orden</b>{bars(70,85)}</div></div>
      <div class="sec"><i>4</i><div><b>Qué nunca hace sin preguntarte</b>{bars(75)}</div></div>
      <div class="sec"><i>5</i><div><b>Cómo te entrega</b>{bars(65,50)}</div></div>
    </div></div>
    <h1>Tu asistente es tan bueno como <span class="hl">sus instrucciones.</span></h1>
  </div>"""

s2 = f"""<div class="body">
    <h2>Muchos le escriben <span class="hl">una sola línea.</span></h2>
    <div class="vis"><div class="card one">{ILUS}<code>"Eres un asistente útil."</code><br>
      <span class="verdict">{ic('x',24)}No sabe nada de ti</span></div></div>
    <p class="support">Con eso responde como cualquier chat: correcto, genérico y <b>sin saber nada de tu negocio.</b></p>
  </div>"""

def campo(n, title, lines, theme_ink=False):
    segs = "".join(f'<span class="{"on" if k == n else ("d" if k < n else "")}"></span>' for k in range(1, 6))
    tx = "".join(f"<p>{l}</p>" for l in lines)
    card = "card ink ej" if theme_ink else "card ej"
    return f"""<div class="body">
    <div class="fields">{segs}</div>
    <div class="kick"><i>{n}</i><span>{FIELDS[n-1]}</span></div>
    <h2>{title}</h2>
    <div class="vis"><div class="bign">{n}</div><div class="{card}">{ILUS}<div class="hd">{ic('pen',28)}Ejemplo</div><div class="tx">{tx}</div></div></div>
  </div>"""

s3 = campo(1, 'Quién es y <span class="hl">para quién trabaja.</span>', [
    'Eres el asistente de <u>Café Monte</u>, una tienda de café de origen en Medellín.',
    'Trabajas para <u>Ana</u>, la dueña, y para su equipo de ventas.'])
s4 = campo(2, 'Qué sabe de <span class="hl">tu negocio.</span>', [
    'Precios: los del archivo <u>precios-2026.pdf</u>.',
    'Envíos: a todo el país, de 2 a 5 días hábiles.',
    'Atención: de lunes a sábado, de 8 a 6.'])
s5 = campo(3, 'Qué hace y <span class="hl">en qué orden.</span>', [
    '1. Lee los mensajes nuevos.',
    '2. Responde precios y envíos.',
    '3. Si piden más de 20 bolsas, prepara una cotización <u>y me la pasa.</u>'], theme_ink=True)
s6 = campo(4, 'Qué nunca hace <span class="hl">sin preguntarte.</span>', [
    'No confirma descuentos.',
    'No promete fechas de entrega.',
    'No le escribe a un cliente nuevo <u>sin que yo lo vea.</u>'])
s7 = campo(5, 'Cómo <span class="hl">te entrega.</span>', [
    'Respuestas de máximo tres líneas, de tú.',
    'Cotizaciones en tabla.',
    'Si no sabe algo, <u>lo dice.</u>'])

s8 = criterio("Si no se lo sabes explicar a alguien nuevo en tu equipo, <span class='w'>tampoco a tu asistente.</span>",
              "Escribir las instrucciones te obliga a ordenar cómo trabajas. Ese orden sirve aunque nunca uses la IA.", foto="crit-equipo.jpg")

s9 = cta_glass("cta-cursor-libro.jpg", f"{C.DIA} · {C.HORA}", C.PALABRA, C.MOTIVO,
               title="Escribimos juntos las instrucciones de tu asistente.", top=575, shift=250,
               alt="Un cursor de computador en forma de mano sale de un libro naranja abierto")

slides = [slide("light", s1), slide("surface", s2), slide("light", s3), slide("light", s4),
          slide("dark", s5), slide("light", s6), slide("surface", s7), slide("orange", s8), slide("photo", s9)]

build(HERE, "Pieza 033 · Las instrucciones de tu asistente",
      "Fuente editable. 9 láminas de 1080x1350. Clase del jueves (3 de 4), CTA Comenta CLASE. Café Monte y Ana son un ejemplo inventado, rotulado Ilustración.",
      slides, CSS)
