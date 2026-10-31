"""Pieza 036 · GPT-6 arma herramientas dentro del chat, también en el plan gratis (noticia)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, logo, cta_follow, criterio, noticia

HERE = pathlib.Path(__file__).resolve().parent
ILUS = '<span class="ilus">Ilustración</span>'
SRC = 'Fuente: OpenAI, "GPT-6 para todos" (versión es-419), 7 oct 2026.'

CSS = """
.p1 .hero{width:100%;height:520px;border-radius:30px;overflow:hidden;border:2px solid var(--line);box-shadow:0 30px 70px rgba(23,19,16,.16);background:#f7f7f7}
.p1 .hero img{display:block;width:100%;height:100%;object-fit:cover;object-position:center center}
.calc .q{margin-bottom:18px}
.calc .tool{border-radius:24px;background:var(--surface);padding:26px 26px}
.calc .tool small{display:block;font:700 18px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.calc .sl{margin-top:22px}
.calc .sl b{display:flex;justify-content:space-between;font:600 26px/1 var(--display)}
.calc .sl b span{color:var(--orangeText)}
.calc .rail{position:relative;height:12px;border-radius:6px;background:var(--line);margin-top:16px}
.calc .rail i{position:absolute;left:0;top:0;bottom:0;border-radius:6px;background:var(--orange)}
.calc .rail i::after{content:"";position:absolute;right:-14px;top:-9px;width:30px;height:30px;border-radius:50%;background:#fff;border:3px solid var(--orange)}
.calc .res{margin-top:26px;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.calc .res div{border-radius:20px;background:#fff;padding:18px 20px}
.calc .res div.o{background:var(--ink);color:#fff}
.calc .res small{font-size:16px}
.calc .res strong{display:block;margin-top:10px;font:700 44px/1 var(--display);letter-spacing:-.03em}
.calc .res .o strong{color:var(--orange)}
.pl{display:grid;grid-template-columns:1fr 1fr;gap:18px;width:100%}
.pl > div{border-radius:32px;padding:32px 30px}
.pl .a{background:#fff;border:2px solid var(--line)} .pl .b{background:var(--ink);color:#fff}
.pl small{display:block;font:700 21px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.pl .b small{color:var(--orange)}
.pl b{display:block;margin-top:16px;font:700 50px/1 var(--display);letter-spacing:-.03em}
.pl p{margin-top:18px;font:500 28px/1.35 var(--body);color:var(--muted)} .pl .b p{color:var(--soft)}
.pl em{display:inline-block;margin-top:20px;font:700 20px/1 var(--display);font-style:normal;letter-spacing:.1em;text-transform:uppercase;border-radius:999px;padding:11px 15px;background:var(--surface);color:var(--muted)}
.pl .b em{background:var(--orange);color:var(--ink)}
"""

s1 = f"""<div class="body">
    {noticia('7 oct', 'OpenAI', 'openai')}
    <div class="vis"><div class="hero"><img src="assets/openai-intelligent-ui.jpg" alt="Imagen oficial de OpenAI: GPT-6 with Intelligent UI, con una bicicleta interactiva dentro del chat"></div></div>
    <h1>ChatGPT ya no solo responde con texto. <span class="hl t">Arma herramientas.</span></h1>
  </div>"""

s2 = f"""<div class="body">
    <h2>Responde con gráficas, formularios y <span class="hl t">botones que puedes tocar.</span></h2>
    <div class="vis"><div class="card calc" style="width:100%">{ILUS}<div class="hd">{logo('openai',30)}ChatGPT</div>
      <div class="chat q"><div class="msg u">¿Cuánto facturo si subo precios 10% y vendo 5% menos?</div></div>
      <div class="tool"><small>Calculadora</small>
        <div class="sl"><b>Subir precio<span>+10%</span></b><div class="rail"><i style="width:40%"></i></div></div>
        <div class="sl"><b>Bajan las ventas<span>-5%</span></b><div class="rail"><i style="width:20%"></i></div></div>
        <div class="res"><div><small>Hoy</small><strong>$8,0 M</strong></div><div class="o"><small>Con el cambio</small><strong>$8,4 M</strong></div></div>
      </div></div></div>
  </div>"""

s3 = f"""<div class="body">
    <h2>Llegó a <span class="hl t">todos los planes,</span> también al gratis.</h2>
    <div class="vis"><div class="pl">
      <div class="a"><small>Gratis y Go</small><b>GPT-6 Luna</b><p>Desde el 8 de octubre.</p><em>Incluye el plan gratis</em></div>
      <div class="b"><small>Plus, Pro, Business y Enterprise</small><b>GPT-6 Sol</b><p>Desde el 7 de octubre.</p><em>Planes de pago</em></div>
    </div></div>
    <p class="support">En Enterprise depende de lo que configure el administrador.</p>
  </div>"""

s4 = f"""<div class="body center">
    <div class="stat">44%</div>
    <h2 style="margin-top:30px">antes empieza a responder GPT-6 Instant <span class="hl">en preguntas con búsqueda web.</span></h2>
    <p class="support">Comparado con GPT-5.6 Instant, en promedio, según OpenAI.</p>
  </div>"""

s5 = f"""<div class="body">
    <h2>Lo que <span class="hl t">no cambia</span> y lo que no se publicó.</h2>
    <div class="vis"><div class="know">
      <div class="y"><small>No cambia</small><p>Los modelos de Work y de Codex siguen siendo los mismos.</p></div>
      <div class="n"><small>No se publicó</small><p>Los límites de uso de cada plan.</p><p>Qué diferencia hay entre Luna y Sol en calidad.</p></div>
    </div></div>
  </div>"""

s6 = criterio("Que te arme la herramienta en segundos no significa que esté bien hecha. <span class='w'>Revisa la fórmula antes de usar el resultado.</span>",
              "Una calculadora con un supuesto equivocado te da un número equivocado, rápido y con buen diseño.", foto="crit-monitores.jpg")

s7 = cta_follow("cta-ascii.jpg", "Lo nuevo de la IA", "Con la letra pequeña incluida.",
                "Noticias de IA leídas desde tu negocio.", top=700,
                alt="Retrato de una persona hecho con caracteres de texto naranjas sobre fondo negro")

slides = [slide("light", s1, src=SRC), slide("light", s2), slide("surface", s3.replace('class="body"','class="body center"',1).replace('<div class="vis">','<div class="gap l"></div><div>'), src=SRC),
          slide("dark", s4, src=SRC), slide("light", s5.replace('class="body"','class="body center"',1).replace('<div class="vis">','<div class="gap l"></div><div>'), src=SRC), slide("orange", s6), slide("photo", s7)]

build(HERE, "Pieza 036 · GPT-6 arma herramientas",
      "Fuente editable. 7 láminas de 1080x1350. Noticia. Fuente: openai.com/es-419/index/gpt-6-for-everyone (7 oct 2026). Imagen oficial de OpenAI recortada en la portada. Lámina 2 es ilustración.",
      slides, CSS)
