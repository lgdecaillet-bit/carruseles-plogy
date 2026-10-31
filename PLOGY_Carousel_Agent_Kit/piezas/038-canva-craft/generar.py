"""Pieza 038 · Canva Craft, el modelo de imágenes de Canva entrenado con diseños (noticia)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, logo, cta_follow, criterio, noticia

HERE = pathlib.Path(__file__).resolve().parent
ILUS = '<span class="ilus">Ilustración</span>'
SRC = 'Fuente: Canva Newsroom, "Introducing Canva Craft", 22 oct 2026.'

CSS = """
.plan2{display:grid;grid-template-columns:1fr 60px 1fr 60px 1fr;gap:6px;align-items:center;width:100%}
.plan2 .st{border-radius:26px;padding:24px 20px;background:#fff;border:2px solid var(--line);min-height:300px}
.plan2 .st small{display:block;font:700 18px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--orangeText)}
.plan2 .st b{display:block;margin-top:12px;font:700 32px/1.05 var(--display)}
.plan2 .st p{margin-top:14px;font:400 22px/1.35 var(--body);color:var(--muted)}
.plan2 .ar{display:flex;justify-content:center;color:var(--orange)}
.plan2 .wire{margin-top:16px;display:grid;grid-template-columns:1fr 1fr;gap:6px}
.plan2 .wire i{height:34px;border-radius:6px;border:2px dashed var(--border)}
.plan2 .wire i.w{grid-column:1/3;height:22px;background:var(--line);border:0}
.plan2 .img{margin-top:16px;height:150px;border-radius:14px;background:var(--grad);position:relative;overflow:hidden}
.plan2 .img span{position:absolute;left:14px;bottom:12px;font:700 26px/1 var(--display);color:#fff}
.chips{display:flex;flex-wrap:wrap;gap:14px}
.chips span{display:flex;align-items:center;gap:12px;font:700 34px/1 var(--display);border-radius:999px;padding:20px 28px;background:#fff;border:2px solid var(--line)}
.chips span svg{color:var(--orange)}
.chips span.o{background:var(--ink);color:#fff;border-color:var(--ink)}
.trip{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;width:100%}
.trip div{border-radius:30px;background:var(--card);border:2px solid var(--cardLine);padding:32px 22px;text-align:center}
.trip b{display:block;font:700 96px/1 var(--display);letter-spacing:-.04em;color:var(--orange)}
.trip span{display:block;margin-top:16px;font:500 26px/1.3 var(--body);color:var(--soft)}
.p1 .hero{width:100%;border-radius:30px;overflow:hidden;box-shadow:0 30px 70px rgba(23,19,16,.2);transform:rotate(-1.5deg)}
.p1 .hero img{display:block;width:100%;height:480px;object-fit:cover}
.strip{width:100%;border-radius:24px;overflow:hidden;margin-top:40px;box-shadow:0 20px 50px rgba(23,19,16,.16)}
.strip img{display:block;width:100%;height:270px;object-fit:cover}
.cover{position:relative;width:100%;height:100%}
.cover .poster{position:absolute;border-radius:24px;overflow:hidden;box-shadow:0 30px 60px rgba(23,19,16,.22)}
.cover .poster .bg{position:absolute;inset:0}
.cover .poster b{position:absolute;left:24px;right:24px;bottom:24px;font:700 40px/1.02 var(--display);letter-spacing:-.03em;color:#fff}
.cover .poster small{position:absolute;left:26px;top:24px;font:700 18px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:#fff;opacity:.85}
.cover .badge{position:absolute;right:20px;top:10px;z-index:4}
"""

s1 = f"""<div class="body">
    {noticia('22 oct', 'Canva', 'canva')}
    <div class="vis"><div class="hero"><img src="assets/canva-craft-oficial.jpg" alt="Imagen oficial de Canva: collage de imágenes generadas con Craft"></div></div>
    <h1>Canva lanzó su propio modelo de imágenes, <span class="hl t">entrenado con diseños.</span></h1>
  </div>"""

s2 = f"""<div class="body">
    <h2>Primero planea la composición, <span class="hl t">después dibuja.</span></h2>
    <div class="vis"><div class="plan2">
      <div class="st"><small>1 · Pedido</small><b>«Póster de feria de café»</b><p>En el idioma que quieras.</p></div>
      <div class="ar">{ic('arrow',44)}</div>
      <div class="st"><small>2 · Plan</small><b>Qué va y dónde</b><div class="wire"><i class="w"></i><i></i><i></i><i class="w"></i></div><p>Elementos, tamaños, jerarquía y texto.</p></div>
      <div class="ar">{ic('arrow',44)}</div>
      <div class="st"><small>3 · Imagen</small><b>Hasta 2K</b><div class="img"><span>Feria</span></div></div>
    </div></div>
    <p class="support">Por eso el texto sale donde debe y se puede editar por capas.</p>
  </div>"""

def chip(icon, t, o=False):
    return f'<span class="{"o" if o else ""}">{ic(icon,30)}{t}</span>'

s3 = f"""<div class="body">
    <h2>Aprendió de plantillas hechas por personas, <span class="hl t">no solo de fotos.</span></h2>
    <div class="vis"><div class="chips">
      {chip('image','Pósters')}{chip('chat','Posts')}{chip('table','Presentaciones')}{chip('chart','Infografías')}{chip('list','Menús')}{chip('pen','Tipografía',True)}
    </div></div>
    <div class="strip"><img src="assets/canva-craft-oficial-2.jpg" alt="Imágenes de ejemplo generadas con Craft, publicadas por Canva"></div>
    <p class="support">Millones de plantillas de la biblioteca de Canva, según la empresa.</p>
  </div>"""

s4 = f"""<div class="body">
    <h2>Escribe en <span class="hl">55 idiomas</span> y genera en más de 30 proporciones.</h2>
    <div class="vis"><div class="trip">
      <div><b>55</b><span>idiomas para el texto dentro de la imagen</span></div>
      <div><b>30+</b><span>proporciones, o la que tú definas</span></div>
      <div><b>2K</b><span>de resolución máxima</span></div>
    </div></div>
  </div>"""

s5 = f"""<div class="body center">
    <h2>Ya está para <span class="hl t">todos los usuarios de Canva.</span></h2>
    <div class="gap l"></div>
    <div class="know">
      <div class="y"><small>Dónde</small><p>En Dream Lab, en el panel de la izquierda.</p><p>En la API pública de Canva.</p></div>
      <div class="n"><small>Lo que viene o no se dice</small><p>Conexión con asistentes de IA (MCP): próximamente.</p><p>Cuánto consume de cada plan: no lo dice.</p></div>
    </div>
  </div>"""

s6 = criterio("Cuando todos tienen el mismo modelo, <span class='w'>la diferencia está en el pedido.</span>",
              "Qué quieres decir, a quién y por qué. Eso no lo genera ninguna herramienta.", foto="crit-caballo.jpg")

s7 = cta_follow("cta-pintor.jpg", "IA para crear", "Con criterio para usarla.",
                "Herramientas nuevas, leídas desde tu negocio.", top=760, pos="center 20%",
                alt="Un hombre de traje pinta con pincel sobre la pantalla de un computador antiguo")

slides = [slide("light", s1, src=SRC), slide("surface", s2, src=SRC), slide("light", s3, src=SRC),
          slide("dark", s4, src=SRC), slide("light", s5, src=SRC), slide("orange", s6), slide("photo", s7)]

build(HERE, "Pieza 038 · Canva Craft",
      "Fuente editable. 7 láminas de 1080x1350. Noticia. Fuente: canva.com/newsroom/news/canva-craft (22 oct 2026), leída en el navegador. Las piezas de la portada y la lámina 2 son ilustraciones, no salidas de Craft.",
      slides, CSS)
