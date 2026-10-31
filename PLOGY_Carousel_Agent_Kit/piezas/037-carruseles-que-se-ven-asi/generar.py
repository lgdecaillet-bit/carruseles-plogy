"""Pieza 037 · ¿Quieres que tus carruseles se vean así? (lead magnet, Comenta CARRUSELES)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, cta_glass, criterio

HERE = pathlib.Path(__file__).resolve().parent

CSS = """
.fan{position:relative;width:100%;height:100%}
.fan .sh{position:absolute;width:330px;height:412px;border-radius:18px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.5)}
.fan .sh img{width:100%;height:100%;object-fit:cover;display:block}
.pair{display:flex;gap:26px;justify-content:center;align-items:center;width:100%}
.pair .sh{width:400px;height:500px;border-radius:20px;overflow:hidden;box-shadow:0 26px 60px rgba(23,19,16,.22)}
.pair .sh img{width:100%;height:100%;object-fit:cover;display:block}
.pair .sh:first-child{transform:rotate(-3deg)} .pair .sh:last-child{transform:rotate(3deg) translateY(30px)}
.tagp{display:inline-flex;align-items:center;gap:10px;margin-top:26px;font:700 21px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.t-dark .tagp{color:var(--dim)}
.trio{display:flex;gap:18px;justify-content:center;width:100%}
.trio .sh{position:relative;width:280px;height:350px;border-radius:18px;overflow:hidden;box-shadow:0 26px 60px rgba(0,0,0,.45)}
.trio .sh img{width:100%;height:100%;object-fit:cover;display:block}
.trio .sh:nth-child(2){transform:translateY(-30px)}
.trio .play{position:absolute;left:50%;top:50%;width:76px;height:76px;margin:-38px 0 0 -38px;border-radius:50%;background:rgba(255,91,0,.92);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 30px rgba(0,0,0,.4)}
.trio .play::after{content:"";border-left:24px solid var(--ink);border-top:15px solid transparent;border-bottom:15px solid transparent;margin-left:6px}
"""

def sh(img, x, y, r, z=1):
    return f'<div class="sh" style="left:{x}px;top:{y}px;transform:rotate({r}deg);z-index:{z}"><img src="assets/{img}.jpg" alt=""></div>'

s1 = f"""<div class="body">
    <div class="vis"><div class="fan">
      {sh('ej-023-1',10,90,-9,1)}{sh('ej-025-1',530,70,8,2)}{sh('ej-019-1',270,30,-1,3)}
    </div></div>
    <h1>¿Quieres que tus carruseles <span class="hl">se vean así?</span></h1>
    <p class="support">Estos los hicimos en Plogy. Te contamos cómo.</p>
  </div>"""

s2 = f"""<div class="body">
    <div class="eyebrow">Noticias</div>
    <h2>Una noticia, leída <span class="hl">desde tu negocio.</span></h2>
    <div class="vis"><div class="pair">
      <div class="sh"><img src="assets/ej-023-1.jpg" alt="Portada de la pieza 023"></div>
      <div class="sh"><img src="assets/ej-023-4.jpg" alt="Lámina 4 de la pieza 023"></div>
    </div></div>
  </div>"""

s3 = f"""<div class="body">
    <div class="eyebrow">Guías</div>
    <h2>Guías para <span class="hl">guardar y volver a ellas.</span></h2>
    <div class="vis"><div class="pair">
      <div class="sh"><img src="assets/ej-025-1.jpg" alt="Portada de la pieza 025"></div>
      <div class="sh"><img src="assets/ej-018-1.jpg" alt="Portada de la pieza 018"></div>
    </div></div>
  </div>"""

s4 = f"""<div class="body">
    <div class="eyebrow">Animados</div>
    <h2>Y cuando hace falta, <span class="hl">se mueven.</span></h2>
    <div class="vis"><div class="trio">
      <div class="sh"><img src="assets/ej-026-1.jpg" alt=""><span class="play"></span></div>
      <div class="sh"><img src="assets/ej-026-5.jpg" alt=""><span class="play"></span></div>
      <div class="sh"><img src="assets/ej-026-15.jpg" alt=""><span class="play"></span></div>
    </div></div>
    <p class="support">Cada lámina es un video que se repite sin salto.</p>
  </div>"""

def flt(icon, t, s):
    return f'<div class="row"><div class="ic">{ic(icon,34)}</div><div><b>{t}</b><span>{s}</span></div><span></span></div>'

s5 = f"""<div class="body">
    <h2>Lo que no se ve: <span class="hl">cuatro filtros</span> antes de publicar.</h2>
    <div class="vis"><div class="rows" style="width:100%">
      {flt('search','Fuente verificada','Si no lo podemos comprobar, no sale.')}
      {flt('list','Una idea por lámina','Para que se lea en el teléfono, sin esfuerzo.')}
      {flt('spark','Criterio propio','Lo que pensamos nosotros, no lo que dice la fuente.')}
      {flt('eye','Revisión humana','Nada se publica sin que una persona lo apruebe.')}
    </div></div>
  </div>"""

s6 = criterio("El diseño hace que alguien se detenga. <span class='w'>La idea hace que alguien te siga.</span>",
              "Por eso en cada carrusel trabajamos las dos.", foto="crit-camara.jpg")

s7 = cta_glass("cta-nino-tv.jpg", "¿Quieres que los tuyos se vean así?", "CARRUSELES",
               "y te contamos cómo los hacemos para tu marca.", top=640, shift=120,
               alt="Un niño sentado en el piso mira una pantalla encendida en una habitación oscura")

slides = [slide("dark", s1), slide("light", s2), slide("surface", s3), slide("dark", s4),
          slide("light", s5), slide("orange", s6), slide("photo", s7)]

build(HERE, "Pieza 037 · Carruseles que se ven así",
      "Fuente editable. 7 láminas de 1080x1350. Lead magnet, CTA Comenta CARRUSELES. Muestra exportaciones reales de las piezas 018, 019, 023, 025 y 026 (assets/ej-*.jpg).",
      slides, CSS)
