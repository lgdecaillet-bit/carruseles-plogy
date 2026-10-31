import io, sys
p = sys.argv[1]
s = io.open(p, encoding="utf-8").read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)


# 06: titular legible sobre columnas naranja
rep(".v06 .shade{background:linear-gradient(to bottom,rgba(23,19,16,.8) 0%,rgba(23,19,16,.35) 40%,rgba(23,19,16,.55) 100%)}",
    ".v06 .shade{background:linear-gradient(to bottom,rgba(23,19,16,.92) 0%,rgba(23,19,16,.7) 30%,rgba(23,19,16,.4) 52%,rgba(23,19,16,.6) 100%)}\n.v06 .hl{color:#fff;text-shadow:none}")
# 07: texto sin chocar con las esferas y titular distinto del botón
rep(".v07 .big{position:absolute;z-index:3;left:96px;bottom:430px;font:700 150px/.95 var(--display);letter-spacing:-.05em}",
    ".v07 .big{position:absolute;z-index:3;left:96px;bottom:440px;font:700 138px/.95 var(--display);letter-spacing:-.05em}")
rep(".v07 .sub{position:absolute;z-index:3;left:96px;width:700px;bottom:300px;",
    ".v07 .sub{position:absolute;z-index:3;left:96px;width:480px;bottom:270px;")
rep('<p class="big">Sigue a<br><em>Plogy</em></p>\n  <p class="sub">Para quienes prefieren entender antes de automatizar.</p>',
    '<p class="big">Primero<br><em>entender.</em></p>\n  <p class="sub">Sigue a Plogy para ver cómo se implementa la IA en negocios.</p>')
# 10: titular en blanco sobre la trama naranja
rep(".v10 .h{top:200px;font-size:88px}", ".v10 .h{top:200px;font-size:88px}\n.v10 .hl{color:#fff;text-shadow:none}")
# 11: foto bajada para que el logo caiga sobre Ink
rep(".v11 .photo{position:absolute;left:0;top:0;width:1080px;height:608px;object-fit:cover}\n.v11 .h{top:660px;font-size:78px}\n.v11 .cm{top:960px}\n.v11 .cmnote{top:1130px}",
    ".v11 .photo{position:absolute;left:0;top:130px;width:1080px;height:608px;object-fit:cover}\n.v11 .h{top:770px;font-size:78px}\n.v11 .cm{top:1000px}\n.v11 .cmnote{top:1160px}")
# 13, 26, 28: sombra superior para el logo
rep(".v13{background:var(--surface);color:var(--ink)}",
    ".v13 .shade,.v26 .shade,.v28 .shade{bottom:auto;height:320px;background:linear-gradient(to bottom,rgba(23,19,16,.78),rgba(23,19,16,0))}\n.v13{background:var(--surface);color:var(--ink)}")
rep('<img class="photo" src="assets/13-rostro.jpg" alt="Un rostro en trama de puntos en blanco y negro">',
    '<img class="photo" src="assets/13-rostro.jpg" alt="Un rostro en trama de puntos en blanco y negro">\n  <div class="shade"></div>')
rep('<img class="photo" src="assets/26-pantalla-error.jpg" alt="Un parque lleno de gente bajo una pantalla de error, en tonos naranja">',
    '<img class="photo" src="assets/26-pantalla-error.jpg" alt="Un parque lleno de gente bajo una pantalla de error, en tonos naranja">\n  <div class="shade"></div>')
rep('<img class="photo" src="assets/28-silueta-publico.jpg" alt="Un público con gafas 3D en el que una silueta naranja no coincide con los demás">',
    '<img class="photo" src="assets/28-silueta-publico.jpg" alt="Un público con gafas 3D en el que una silueta naranja no coincide con los demás">\n  <div class="shade"></div>')
# 17: salto de línea del titular
rep('<h2 class="h">Tú diriges. <span class="hl">La IA ejecuta.</span></h2>',
    '<h2 class="h">Tú diriges.<br><span class="hl">La IA ejecuta.</span></h2>')
# 18: titular blanco con sombra superior más fuerte
rep(".v18 .shade{background:linear-gradient(to bottom,rgba(23,19,16,.8) 0%,rgba(23,19,16,.35) 30%,rgba(23,19,16,0) 50%)}",
    ".v18 .shade{background:linear-gradient(to bottom,rgba(23,19,16,.92) 0%,rgba(23,19,16,.6) 32%,rgba(23,19,16,0) 54%)}\n.v18 .hl{color:#fff;text-shadow:none}")
# 20 y 21 y 29: titular en blanco donde el naranja se pierde
rep(".v20 .h{top:200px;font-size:92px}", ".v20 .h{top:200px;font-size:92px}\n.v20 .hl{color:#fff;text-shadow:none}")
rep(".v21 .h{top:200px;font-size:104px}", ".v21 .h{top:200px;font-size:104px}\n.v21 .hl{color:#fff;text-shadow:none}")
rep(".v29 .h{top:215px}", ".v29 .h{top:215px}\n.v29 .hl{color:#fff;text-shadow:none}")
# 23: logo negro sobre naranja
rep('<img class="logo" src="../../brandkit/assets/plogy-color.svg" alt="Plogy">\n  <h2 class="h">Tu proceso, <span class="nogl">en una lista.</span></h2>',
    '<img class="logo" src="../../brandkit/assets/plogy-black.svg" alt="Plogy">\n  <h2 class="h">Tu proceso, <span class="nogl">en una lista.</span></h2>')
# 25: nota bajo el chat con espacio y palabra resaltada
rep(".v25 .cmnote{top:1190px;text-align:center;font:700 40px/1.2 var(--display)}",
    ".v25 .cmnote{top:1222px;text-align:center;font:700 42px/1.2 var(--display)}")
rep('<p class="cmnote">Escríbenos PROCESO por DM.</p>',
    '<p class="cmnote">Escríbenos <span class="kw">PROCESO</span> por DM.</p>')
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("ok")
