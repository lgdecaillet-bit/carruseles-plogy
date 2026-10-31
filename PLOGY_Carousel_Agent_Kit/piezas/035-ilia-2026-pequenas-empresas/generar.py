"""Pieza 035 · ILIA 2026: 7 de cada 100 pequeñas empresas usan IA (noticia)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_comun"))
from plogy import build, slide, fondo, polaroid, ic, cta_follow, criterio

HERE = pathlib.Path(__file__).resolve().parent
SRC = 'Fuente: Índice Latinoamericano de Inteligencia Artificial (ILIA) 2026, CEPAL y CENIA, presentado el 20 oct 2026 (indicelatam.cl).'

CSS = """
.dots100{display:grid;grid-template-columns:repeat(20,1fr);gap:9px;width:100%;padding:34px;border-radius:32px;background:rgba(23,19,16,.72);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px)}
.dots100 i{aspect-ratio:1;border-radius:50%;background:rgba(255,255,255,.12)}
.dots100 i.o{background:var(--orange);box-shadow:0 0 16px rgba(255,91,0,.5)}
.hbars{display:flex;flex-direction:column;gap:26px;width:100%}
.hb small{display:flex;justify-content:space-between;font:700 26px/1 var(--display);margin-bottom:12px}
.hb small span{color:var(--orangeText)}
.hb .tr{height:54px;border-radius:14px;background:var(--surface);position:relative;overflow:hidden}
.hb .tr i{position:absolute;left:0;top:0;bottom:0;border-radius:14px;background:var(--border)}
.hb.on .tr i{background:var(--orange)}
.cmp{display:flex;flex-direction:column;gap:30px;width:100%}
.cmp .g b{display:block;font:700 30px/1 var(--display);margin-bottom:14px}
.cmp .ln{display:grid;grid-template-columns:200px 1fr 90px;gap:16px;align-items:center;margin-top:10px;font:500 24px/1 var(--body);color:var(--muted)}
.cmp .ln .tr{height:30px;border-radius:9px;background:var(--surface);position:relative;overflow:hidden}
.cmp .ln .tr i{position:absolute;left:0;top:0;bottom:0;border-radius:9px;background:var(--orange)}
.cmp .ln.x .tr i{background:var(--ink)}
.cmp .ln strong{font:700 30px/1 var(--display);color:var(--ink);text-align:right}
.co{display:flex;gap:18px;width:100%}
.co > div{flex:1;border-radius:30px;padding:34px 28px;background:var(--card);border:2px solid var(--cardLine);text-align:center}
.co > div.o{background:var(--orange);border-color:var(--orange);color:var(--ink)}
.co b{display:block;font:700 54px/1 var(--display);letter-spacing:-.03em}
.co span{display:block;margin-top:14px;font:400 25px/1.3 var(--body);color:var(--soft)}
.co .o span{color:var(--ink)}
"""

dots = "".join(f'<i class="{"o" if k < 7 else ""}"></i>' for k in range(100))

s1 = fondo("fondo-multitud.jpg", "Vista desde arriba de una multitud en movimiento; una persona quieta en el centro") + f"""<div class="body">
    <div class="pills"><div class="pill">Estudio · 20 oct</div><div class="pill ghost src-pill">CEPAL y CENIA</div></div>
    <div class="vis"><div class="dots100">{dots}</div></div>
    <h1>En Latinoamérica, solo <span class="hl">7 de cada 100</span> pequeñas empresas usan IA.</h1>
  </div>"""

def hb(t, v, on=False):
    w = float(v.replace(",", "."))
    return f'<div class="hb{" on" if on else ""}"><small>{t}<span>{v}%</span></small><div class="tr"><i style="width:{w:.0f}%"></i></div></div>'

s2 = f"""<div class="body">
    <h2>En las grandes son 28. <span class="hl t">Cuatro veces más.</span></h2>
    <div class="vis"><div class="hbars">
      {hb('Grandes','27,6')}{hb('Medianas','12,8')}{hb('Pequeñas','6,8',True)}
    </div></div>
    <p class="support">Porcentaje de empresas de América Latina y el Caribe que incorporó IA, según su tamaño. Escala de 0 a 100%.</p>
  </div>"""

def ln(t, v, w, x=False):
    return f'<div class="ln{" x" if x else ""}"><span>{t}</span><div class="tr"><i style="width:{w}%"></i></div><strong>{v}%</strong></div>'

s3 = f"""<div class="body">
    <h2>Fuera de la región, las pequeñas <span class="hl t">llegan a 24%.</span></h2>
    <div class="vis"><div class="cmp">
      <div class="g"><b>Grandes</b>{ln('Latinoamérica','28',28)}{ln('Fuera de la región','66',66,True)}</div>
      <div class="g"><b>Medianas</b>{ln('Latinoamérica','13',13)}{ln('Fuera de la región','41',41,True)}</div>
      <div class="g"><b>Pequeñas</b>{ln('Latinoamérica','7',7)}{ln('Fuera de la región','24',24,True)}</div>
    </div></div>
    <p class="support">El índice compara con un grupo de países de fuera de la región.</p>
  </div>"""

s4 = f"""<div class="body">
    <h2>Colombia es uno de los dos países que <span class="hl">especifica presupuesto</span> para su estrategia de IA.</h2>
    <div class="vis"><div class="co">
      <div class="o"><b>Colombia</b><span>Estrategia con presupuesto especificado</span></div>
      <div class="o"><b>Brasil</b><span>Estrategia con presupuesto especificado</span></div>
      <div><b>El resto</b><span>Sin presupuesto especificado en su estrategia</span></div>
    </div></div>
  </div>"""

s5 = criterio("A una pequeña empresa no le falta el modelo. <span class='w'>Le falta quién lo ponga a trabajar dentro del negocio.</span>",
              "Ese es nuestro trabajo: implementar y formar a quienes implementan.", foto="crit-manos-verdes.jpg")

s6 = cta_follow("cta-portal.jpg", "Formamos a quienes implementan IA", "Llevamos la IA a negocios como el tuyo.",
                "IA aplicada en Latinoamérica.", top=640,
                alt="Una persona corre hacia el centro de un túnel en espiral")

slides = [slide("photo", s1, src=SRC), slide("light", s2, src=SRC), slide("light", s3, src=SRC),
          slide("dark", s4, src=SRC), slide("orange", s5), slide("photo", s6)]

build(HERE, "Pieza 035 · ILIA 2026 y la pequeña empresa",
      "Fuente editable. 6 láminas de 1080x1350. Noticia/estudio. Fuente: ILIA 2026 (CEPAL y CENIA), hallazgos publicados en indicelatam.cl. Ver brief.md: el documento de CEPAL no se pudo abrir.",
      slides, CSS)
