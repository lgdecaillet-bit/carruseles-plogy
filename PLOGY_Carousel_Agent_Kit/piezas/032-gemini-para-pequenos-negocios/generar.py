"""Pieza 032 · Gemini para dueños de pequeños negocios (noticia)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, logo, cta_follow, criterio, noticia

HERE = pathlib.Path(__file__).resolve().parent
ILUS = '<span class="ilus">Ilustración</span>'
SRC = 'Fuente: Google, "New tools in the Gemini app for small business owners", 20 oct 2026.'
SRC5 = 'Fuente: Google Workspace Updates, "An easier way to customize how Gemini works for you", 21 oct 2026.'

CSS = """
.p1 .hero{width:100%;border-radius:30px;overflow:hidden;box-shadow:0 30px 70px rgba(23,19,16,.2);border:2px solid var(--line)}
.p1 .hero img{display:block;width:100%;height:470px;object-fit:cover;object-position:center 72%}
.kit{display:grid;grid-template-columns:1fr 70px 1fr;gap:10px;align-items:center;width:100%}
.kit .k b{display:block;font:700 22px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:16px}
.kit .sw{display:flex;gap:10px}
.kit .sw i{width:62px;height:62px;border-radius:16px}
.kit .ty{margin-top:18px;font:700 64px/1 var(--display);letter-spacing:-.03em}
.kit .ty span{display:block;margin-top:6px;font:400 22px/1 var(--body);color:var(--muted);letter-spacing:0}
.kit .arr{display:flex;justify-content:center;color:var(--orange)}
.kit .post{border-radius:24px;overflow:hidden;background:#2b1e3a;color:#fff;padding:28px 26px;min-height:330px;display:flex;flex-direction:column;justify-content:flex-end;background:linear-gradient(160deg,#7b3fe4,#e1556a)}
.kit .post small{font:700 18px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;opacity:.8}
.kit .post b{display:block;margin-top:10px;font:700 44px/1.02 var(--display);letter-spacing:-.03em}
.mess{display:grid;grid-template-columns:1fr 70px 1fr;gap:10px;align-items:center;width:100%}
.mess .raw{font:500 22px/1.5 var(--mono);color:var(--muted);transform:rotate(-2deg)}
.mess .raw p{border-bottom:1.5px dashed var(--line);white-space:nowrap;overflow:hidden}
.mess .bars{display:flex;align-items:flex-end;gap:14px;height:260px;padding-top:20px}
.mess .bars i{flex:1;border-radius:10px 10px 4px 4px;background:var(--line)}
.mess .bars i.o{background:var(--orange)}
.mess .arr{display:flex;justify-content:center;color:var(--orange)}
.grid6{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;width:100%}
.grid6 .lg{width:100%;height:150px}
.grid6 .lg small{display:none}
.lab{display:flex;flex-direction:column;align-items:center;gap:12px;font:700 22px/1 var(--display);color:var(--muted)}
"""

s1 = f"""<div class="body">
    {noticia('20 oct', 'Google', 'googlegemini')}
    <div class="vis"><div class="hero"><img src="assets/google-gemini-pymes.jpg" alt="Imagen oficial de Google: Your brand, your tools, all in one place"></div></div>
    <h1>Google armó en Gemini una página <span class="hl t">para dueños de pequeños negocios.</span></h1>
  </div>"""

s2 = f"""<div class="body">
    <div class="kick"><i>{ic('image',36,'#171310')}</i><span>Tu estilo de marca</span></div>
    <h2>Le subes tu web o tu kit de marca y <span class="hl t">mantiene ese estilo.</span></h2>
    <div class="vis"><div class="card" style="width:100%">{ILUS}<div class="kit">
      <div class="k"><b>Tu marca</b><div class="sw"><i style="background:#7b3fe4"></i><i style="background:#e1556a"></i><i style="background:#f4f1ef;border:2px solid var(--line)"></i><i style="background:#171310"></i></div>
        <div class="ty">Aa<span>Tu tipografía</span></div></div>
      <div class="arr">{ic('arrow',54)}</div>
      <div class="post"><small>Nueva pieza</small><b>Abrimos el sábado</b></div>
    </div></div></div>
  </div>"""

s3 = f"""<div class="body">
    <div class="kick"><i>{ic('chart',36,'#171310')}</i><span>Tus números</span></div>
    <h2>Convierte hojas desordenadas y recibos <span class="hl t">en gráficos claros.</span></h2>
    <div class="vis"><div class="card" style="width:100%">{ILUS}<div class="mess">
      <div class="raw"><p>12/10 caja 2 · 340.000</p><p>recibo prov ?? 85.000</p><p>ventas sab 1.200.000</p><p>nomina oct 2.100.000</p><p>pedido 44 · 410.000</p></div>
      <div class="arr">{ic('arrow',54)}</div>
      <div class="bars"><i style="height:40%"></i><i style="height:62%"></i><i style="height:48%"></i><i class="o" style="height:92%"></i><i style="height:70%"></i></div>
    </div></div></div>
  </div>"""

def lab(n, name):
    return f'<div class="lab"><div class="lg">{logo(n,64)}</div>{name}</div>'

s4 = f"""<div class="body">
    <div class="kick"><i>{ic('plug',36,'#171310')}</i><span>Tus apps</span></div>
    <h2>Se conecta con <span class="hl t">apps que ya usas.</span></h2>
    <div class="vis"><div class="grid6">
      {lab('canva','Canva')}{lab('shopify','Shopify')}{lab('wix','Wix')}{lab('dropbox','Dropbox')}
      {lab('adobe','Adobe')}{lab('zoho','Zoho')}{lab('xero','Xero')}{lab('googleads','Google Ads')}
    </div></div>
    <p class="support">Además de Perfil de Negocio, Google Ads y Workspace. Para todos los usuarios de la app de Gemini.</p>
  </div>"""

s5 = f"""<div class="body center">
    <div class="eyebrow">La letra pequeña</div>
    <h2 class="l">Google avisa que la mayoría de las apps conectadas de Gemini, por ahora, <span class="hl">funcionan en inglés y en EE. UU.</span></h2>
    <p class="support">Lo dice en su nota del 21 de octubre sobre el menú Personalizar. <b>La página para negocios se despliega en todo el mundo.</b></p>
  </div>"""

s6 = criterio("Una IA puede copiar tus colores y tu letra. <span class='w'>Lo que dices y a quién se lo dices sigue siendo tuyo.</span>",
              "Dale el estilo. No le delegues el mensaje.", foto="crit-diferente.jpg")

s7 = cta_follow("cta-bloque.jpg", "Herramientas de IA para tu negocio", "Te decimos qué sirve hoy y qué todavía no.",
                "IA para negocios, sin humo.", top=640,
                alt="Un bloque naranja enorme en medio de una calle en blanco y negro")

slides = [slide("light", s1, src=SRC), slide("light", s2, src=SRC), slide("surface", s3, src=SRC),
          slide("light", s4, src=SRC), slide("dark", s5, src=SRC5), slide("orange", s6), slide("photo", s7)]

build(HERE, "Pieza 032 · Gemini para pequeños negocios",
      "Fuente editable. 7 láminas de 1080x1350. Noticia. Fuentes: blog.google (20 oct 2026) y workspaceupdates.googleblog.com (21 oct 2026). Imagen oficial de Google en la portada. Láminas 2 y 3 son ilustración.",
      slides, CSS)
