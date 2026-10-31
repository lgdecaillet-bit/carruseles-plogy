"""Pieza 040 · Claude cambia sus reglas de uso el 12 de noviembre (noticia)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, logo, cta_follow, criterio, noticia

HERE = pathlib.Path(__file__).resolve().parent
SRC = 'Fuente: Anthropic, actualización de la Política de Uso, 8 oct 2026. Rige desde el 12 de noviembre.'

CSS = """
.p4 .fade{background:linear-gradient(180deg,rgba(18,13,10,.85) 0%,rgba(18,13,10,.55) 30%,rgba(18,13,10,.88) 55%,rgba(18,13,10,.97) 100%)}
.pol{width:100%;transform:rotate(-1.5deg)}
.pol .t{font:700 40px/1.1 var(--display);letter-spacing:-.02em}
.pol .t span{display:block;margin-top:8px;font:500 24px/1 var(--body);color:var(--muted);letter-spacing:0}
.pol .sec{margin-top:20px;border-radius:20px;padding:18px 22px;background:var(--surface);font:600 27px/1.25 var(--display);display:flex;gap:14px;align-items:center}
.pol .sec.n{background:#fff3ea;border:2px solid var(--orange)}
.pol .sec em{margin-left:auto;font:700 17px/1 var(--display);font-style:normal;letter-spacing:.12em;text-transform:uppercase;background:var(--orange);border-radius:999px;padding:9px 12px}
.pol .date{position:absolute;right:-16px;top:-40px;background:var(--ink);color:#fff;border-radius:22px;padding:18px 22px;text-align:center;transform:rotate(6deg);box-shadow:0 18px 40px rgba(23,19,16,.25)}
.pol .date small{display:block;font:700 17px/1 var(--display);letter-spacing:.14em;text-transform:uppercase;color:var(--orange)}
.pol .date b{display:block;margin-top:6px;font:700 64px/1 var(--display)}
.dom{display:grid;grid-template-columns:1fr 1fr;gap:14px;width:100%}
.dom div{display:flex;align-items:center;gap:16px;border-radius:24px;background:#fff;border:2px solid var(--line);padding:22px 22px;font:700 32px/1 var(--display)}
.dom div i{width:60px;height:60px;border-radius:16px;background:var(--orange);color:var(--ink);display:flex;align-items:center;justify-content:center}
.hum{margin-top:22px;display:grid;grid-template-columns:1fr 1fr;gap:14px;width:100%}
.hum div{border-radius:26px;background:var(--ink);color:#fff;padding:24px 24px;font:600 29px/1.25 var(--display)}
.hum small{display:block;font:700 18px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--orange);margin-bottom:10px}
"""

s1 = f"""<div class="body">
    {noticia('8 oct', 'Anthropic', 'anthropic')}
    <div class="vis"><div class="card pol">
      <div class="date"><small>Rige desde</small><b>12 nov</b></div>
      <div class="hd">{logo('claude',30)}Claude · Política de uso</div>
      <div class="t">Lo que no se puede hacer con Claude<span>Versión actualizada</span></div>
      <div class="sec n">{ic('alert',30,'#b43d00')}Campañas engañosas<em>Nuevo</em></div>
      <div class="sec">{ic('user',30,'#625951')}Persona revisando en casos de alto riesgo</div>
      <div class="sec">{ic('eye',30,'#625951')}Rastrear personas sin consentimiento</div>
    </div></div>
    <h1>Claude cambia sus reglas de uso <span class="hl t">el 12 de noviembre.</span></h1>
  </div>"""

def r(icon, t, s):
    return f'<div class="row"><div class="ic">{ic(icon,34)}</div><div><b>{t}</b><span>{s}</span></div><span></span></div>'

s2 = f"""<div class="body">
    <div class="eyebrow">Nuevo</div>
    <h2>Prohibidas las campañas engañosas, <span class="hl t">también las comerciales.</span></h2>
    <div class="vis"><div class="rows" style="width:100%">
      {r('eye','Ocultar quién está detrás de un mensaje','Hacer pasar por otro lo que dice tu marca.')}
      {r('users','Cuentas o publicaciones falsas','Para inflar el alcance de un contenido.')}
      {r('code','Herramientas para campañas de influencia','Construir la infraestructura también cuenta.')}
    </div></div>
  </div>"""

def dm(icon, t):
    return f'<div><i>{ic(icon,32)}</i>{t}</div>'

s3 = f"""<div class="body">
    <h2>Si afecta a una persona, <span class="hl t">revisa una persona.</span></h2>
    <div class="gap"></div>
    <div class="dom">{dm('shield','Salud')}{dm('file','Derechos legales')}{dm('money','Finanzas')}{dm('users','Trabajo y servicios')}</div>
    <div class="hum">
      <div><small>Requisito 1</small>Una persona calificada revisa lo que propone Claude y lo puede cambiar.</div>
      <div><small>Requisito 2</small>La persona afectada sabe que se usó IA.</div>
    </div>
  </div>"""

s4 = fondo("fondo-vigilancia.jpg", "Personas marcadas con recuadros de reconocimiento junto a una reja") + f"""<div class="body end">
    <h2 class="l">Rastrear personas sin su consentimiento <span class="hl">queda prohibido.</span></h2>
    <p class="support">En tiempo real o analizando datos que ya tenías. <b>El monitoreo de fraude con consentimiento sigue permitido.</b></p>
  </div>"""

def q(t, s):
    return f'<div><i>{ic("check",32)}</i><div>{t}<span>{s}</span></div></div>'

s5 = f"""<div class="body">
    <div class="eyebrow">Nuestra lectura</div>
    <h2>Qué revisar si usas Claude <span class="hl t">en tu negocio.</span></h2>
    <div class="vis"><div class="chk">
      {q('Tu marketing','Nada de reseñas, cuentas ni testimonios falsos hechos con IA.')}
      {q('Créditos, cobranza o salud','Una persona revisa y el cliente sabe que hubo IA.')}
      {q('Seguimiento de clientes','Solo con datos que te autorizaron a usar.')}
    </div></div>
  </div>"""

s6 = criterio("Lo que no le contarías a tu cliente, <span class='w'>no lo pongas en manos de una IA.</span>",
              "Si una automatización necesita esconderse, ya tienes la respuesta.", foto="crit-oficina.jpg")

s7 = cta_follow("cta-pantalla-error.jpg", "Implementar bien también es esto", "Las reglas son parte del trabajo.",
                "Noticias de IA que sí te tocan.", top=640,
                alt="Ciudad y parque teñidos de naranja con texto de error de sistema superpuesto")

slides = [slide("light", s1, src=SRC), slide("light", s2, src=SRC), slide("surface", s3, src=SRC),
          slide("photo", s4, src=SRC), slide("light", s5), slide("orange", s6), slide("photo", s7)]

build(HERE, "Pieza 040 · Claude cambia sus reglas de uso",
      "Fuente editable. 7 láminas de 1080x1350. Noticia. Fuente: anthropic.com/news/2026-usage-policy-update (8 oct 2026). La lámina 5 es interpretación de Plogy, rotulada Nuestra lectura.",
      slides, CSS)
