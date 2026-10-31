"""Pieza 039 · Las Gems de Gemini se retiran: fechas y qué hacer (noticia)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, logo, cta_follow, criterio, noticia

HERE = pathlib.Path(__file__).resolve().parent
SRC = 'Fuente: Centro de ayuda de Gemini (Google), "Gems are transitioning to skills", consultado el 26 oct 2026.'

CSS = """
.p5 h2 .hl{color:#ffd2b5}
.p5 h2{text-shadow:0 2px 24px rgba(0,0,0,.6)}
.p5 .fade{background:linear-gradient(180deg,rgba(18,13,10,.7) 0%,rgba(18,13,10,.1) 32%,rgba(18,13,10,.45) 62%,rgba(18,13,10,.92) 100%)}
.calx{display:grid;grid-template-columns:1fr 1fr;gap:20px;width:100%}
.calx > div{border-radius:30px;overflow:hidden;background:#fff;border:2px solid var(--line);box-shadow:0 24px 50px rgba(23,19,16,.12)}
.calx .m{background:var(--orange);color:var(--ink);font:700 26px/1 var(--display);letter-spacing:.14em;text-transform:uppercase;padding:18px 24px}
.calx > div.k .m{background:var(--ink);color:#fff}
.calx .d{font:700 150px/1 var(--display);letter-spacing:-.05em;padding:20px 24px 0}
.calx p{padding:6px 24px 26px;font:600 30px/1.2 var(--display)}
.calx p span{display:block;margin-top:6px;font:400 23px/1.3 var(--body);color:var(--muted)}
.swap{display:grid;grid-template-columns:1fr 80px 1fr;align-items:center;gap:10px;width:100%}
.swap .c{border-radius:30px;padding:30px 26px;min-height:300px}
.swap .g{background:var(--surface);border:2px dashed var(--border);color:var(--muted)}
.swap .s{background:var(--ink);color:#fff}
.swap small{display:block;font:700 21px/1 var(--display);letter-spacing:.12em;text-transform:uppercase}
.swap .s small{color:var(--orange)}
.swap b{display:block;margin-top:16px;font:700 48px/1 var(--display);letter-spacing:-.03em}
.swap p{margin-top:16px;font:400 26px/1.35 var(--body)} .swap .s p{color:var(--soft)}
.swap .ar{display:flex;justify-content:center;color:var(--orange)}
.line{position:relative;width:100%;padding-left:60px}
.line::before{content:"";position:absolute;left:21px;top:20px;bottom:20px;width:4px;border-radius:2px;background:var(--line)}
.line .e{position:relative;padding:18px 0}
.line .e::before{content:"";position:absolute;left:-52px;top:26px;width:30px;height:30px;border-radius:50%;background:#fff;border:4px solid var(--border)}
.line .e.o::before{background:var(--orange);border-color:var(--orange)}
.line .e small{font:700 22px/1 var(--display);letter-spacing:.1em;text-transform:uppercase;color:var(--orangeText)}
.line .e b{display:block;margin-top:8px;font:700 36px/1.1 var(--display)}
.line .e span{display:block;margin-top:6px;font:400 25px/1.3 var(--body);color:var(--muted)}
"""

s1 = f"""<div class="body">
    <div class="pills"><div class="pill">Aviso de servicio</div><div class="pill ghost src-pill">{logo('googlegemini',30)}Gemini</div></div>
    <div class="vis"><div class="calx">
      <div><div class="m">Noviembre</div><div class="d">17</div><p>Solo lectura<span>Se abren, pero no se usan ni editan</span></p></div>
      <div class="k"><div class="m">Diciembre</div><div class="d">17</div><p>Se eliminan<span>Con sus archivos</span></p></div>
    </div></div>
    <h1>Tus Gems de Gemini <span class="hl t">tienen fecha de retiro.</span></h1>
  </div>"""

s2 = f"""<div class="body">
    <h2>Las reemplazan <span class="hl t">las skills.</span></h2>
    <div class="vis"><div class="swap">
      <div class="c g"><small>Antes</small><b>Gem</b><p>Un asistente aparte, con sus instrucciones.</p></div>
      <div class="ar">{ic('arrow',54)}</div>
      <div class="c s"><small>Ahora</small><b>Skill</b><p>Instrucciones que reutilizas en cualquier chat, y que Gemini aplica cuando vienen al caso.</p></div>
    </div></div>
  </div>"""

def e(d, t, s, o=False):
    return f'<div class="e{" o" if o else ""}"><small>{d}</small><b>{t}</b><span>{s}</span></div>'

s3 = f"""<div class="body">
    <h2>Las fechas, <span class="hl t">según tu cuenta.</span></h2>
    <div class="vis"><div class="line">
      {e('17 nov 2026','Cuentas personales: solo lectura','Mayores de 18 años.',True)}
      {e('17 dic 2026','Cuentas personales: se eliminan','Descarga tus archivos antes.',True)}
      {e('Marzo 2027','Workspace para empresas','Business, Enterprise y sin ánimo de lucro.')}
      {e('Junio 2027','Workspace para educación','Colegios y universidades.')}
    </div></div>
  </div>"""

def x(t):
    return f'<div class="row off"><div class="ic">{ic("x",32)}</div><div><b>{t}</b></div><span></span></div>'

s4 = f"""<div class="body">
    <h2>Se convierten solas, pero <span class="hl t">no todo pasa.</span></h2>
    <div class="vis"><div class="rows" style="width:100%">
      <div class="row on"><div class="ic">{ic('file',32)}</div><div><b>Máximo 100 MB por skill</b><span>Si te pasas, se quitan primero los archivos más grandes.</span></div><span></span></div>
      {x('Audio y video')}
      {x('.doc, .xls y .ppt antiguos')}
      {x('Archivos comprimidos y de GitHub')}
    </div></div>
  </div>"""

s5 = fondo("foto-carpeta.jpg", "Un haz de luz verde baja desde un objeto en el cielo, en tonos naranja") + f"""<div class="body">
    <h2>Qué hacer <span class="hl">esta semana.</span></h2>
    <div class="vis"><div class="chk">
      <div><i>1</i><div>Haz la lista de tus Gems<span>Las que de verdad usas</span></div></div>
      <div><i>2</i><div>Descarga los archivos que no pasan<span>Audio, video, formatos antiguos</span></div></div>
      <div><i>3</i><div>Copia las instrucciones en un documento tuyo<span>Fuera de Gemini</span></div></div>
    </div></div>
  </div>"""

s6 = criterio("Tus instrucciones son tuyas, no de la herramienta. <span class='w'>Guárdalas fuera de ella.</span>",
              "Así, cuando una plataforma cambia, mudarte es copiar y pegar, no empezar de cero.", foto="crit-destello.jpg")

s7 = cta_follow("cta-radiografia.jpg", "Las fechas que importan", "Te avisamos antes de que te tomen por sorpresa.",
                "IA aplicada a negocios reales.", top=700,
                alt="Radiografía naranja de una persona encorvada mirando su teléfono")

slides = [slide("light", s1, src=SRC), slide("light", s2, src=SRC), slide("surface", s3, src=SRC),
          slide("light", s4, src=SRC), slide("photo", s5), slide("orange", s6), slide("photo", s7)]

build(HERE, "Pieza 039 · Las Gems de Gemini se retiran",
      "Fuente editable. 7 láminas de 1080x1350. Noticia de servicio. Fuente: support.google.com/gemini/answer/18560919. Fechas para cuentas personales mayores de 18 años.",
      slides, CSS)
