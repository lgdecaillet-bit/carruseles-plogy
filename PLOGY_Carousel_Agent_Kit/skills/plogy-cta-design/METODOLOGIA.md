# Metodología del CTA de último slide (registro de la pieza 001)

Registro de cómo se diseñaron las 6 variantes de CTA de la pieza 001, "Automatizar el desorden". Está escrito para que otra sesión de Claude u otro agente pueda generar CTAs equivalentes para otras piezas sin volver a descubrirlo todo. Fecha del trabajo: 2026-10-19.

Nada de lo producido en la pieza 001 se descartó ni se borró. Las 6 variantes (A a F) quedan como biblioteca reutilizable.

## 0. Dónde está cada cosa

| Qué | Ruta (desde `PLOGY_Carousel_Agent_Kit/`) |
| --- | --- |
| Este registro | `skills/plogy-cta-design/METODOLOGIA.md` |
| Instrucciones cortas para agentes | `skills/plogy-cta-design/SKILL.md` |
| Fuente editable de las variantes B a F | `piezas/001-automatizar-el-desorden/cta-variantes.html` |
| Variante A (lámina 06) y las 5 láminas anteriores | `piezas/001-automatizar-el-desorden/carrusel.html` |
| Exportaciones PNG de las variantes | `piezas/001-automatizar-el-desorden/exports/cta/cta-a.png` a `cta-f.png` |
| Derivados de foto (no son originales) | `piezas/001-automatizar-el-desorden/assets/` |
| Originales del moodboard (intactos) | `assets/reference-originals/` |
| Tabla de variantes con estado y derechos | `piezas/001-automatizar-el-desorden/brief.md`, sección "Variantes de CTA" |
| Copia congelada de los HTML de la pieza 001 | `skills/plogy-cta-design/reference/snapshot-pieza-001/` |
| Scripts de recorte y color de fotos | `skills/plogy-cta-design/scripts/derive-*.py` |
| Script de exportación a PNG | `skills/plogy-cta-design/scripts/render-slides.ps1` |
| Referentes de formato que inspiraron el CTA | `skills/plogy-cta-design/reference/inspiracion/` |

Los snapshots en `reference/` son copias. La fuente viva sigue en `piezas/`. Si editas la pieza, no esperes que el snapshot cambie.

## 1. Origen del encargo

Luciano (dueño del proyecto) compartió dos láminas finales de otras cuentas como referencia de formato:

1. **30X** (`reference/inspiracion/30x-boton-vidrio.png`): fondo oscuro, logo arriba, titular con una palabra resaltada con brillo, texto de apoyo con frases en verde fosforescente, y un botón de vidrio gris al pie con el CTA ("Click en el link de nuestro perfil para conocer nuestros programas").
2. **Índice Agro** (`reference/inspiracion/indice-agro-siguenos-foto-oscura.png`): foto a página completa muy oscurecida, logo centrado, "Síguenos" grande y una línea de motivo debajo ("para no perderte ningún hecho importante del agro colombiano").

Lo pedido: un CTA "más de nosotros, más de Plogy", único y no una copia, con **una foto de la biblioteca detrás**, y que **siempre haya un CTA claro** en los carruseles. Luego pidió más variantes. Al final dijo que todas le gustan y que se reutilizarán, y pidió este registro.

Lo que se tomó de los referentes fue solo el formato: botón o tarjeta de vidrio, foto oscurecida detrás, acción única más una línea de motivo, brillo suave en una palabra. No se copió ninguna marca, frase, color ni composición exacta. Los referentes son de terceros: úsalos para entender el formato, no los reproduzcas.

## 2. Principios de diseño (qué hace que un CTA sea "de Plogy")

1. **Una sola acción.** Seguir, comentar una palabra o escribir por DM. Nunca dos a la vez.
2. **Acción más motivo.** Debajo de la acción va una línea que explica por qué vale la pena, en voz Plogy: joven, precisa, directa, anti humo. El motivo habla de lo que Plogy hace (implementar IA en negocios), no de promesas de resultado.
3. **Cierre narrativo.** El titular del último slide repite la síntesis de la pieza ("Primero el proceso. Después la IA.") y el CTA llega como consecuencia de ese cierre.
4. **Foto con función.** La foto se elige por lo que dice, no por gusto. Debe seguir visible. La tarjeta de vidrio cubre solo una parte.
5. **Texto y logo por delante.** Siempre por encima de la foto, con degradado de protección donde haga falta.
6. **Vidrio como firma.** La tarjeta de vidrio oscura es la versión Plogy del `.plogy-glass` de `brandkit/tokens.css`. Se mantiene en casi todas las variantes para que la familia se reconozca.
7. **Honestidad.** Sin promesas de alcance, riqueza o garantías. Si el CTA promete un recurso, el recurso debe existir.

## 3. Proceso paso a paso

1. **Leer el contexto.** `AGENTS.md`, las skills, `brandkit/tokens.json`, `brandkit/README.md`, `assets/reference-catalog.csv` y el brief de la pieza. Identifica el objetivo de la pieza (seguimiento, comunidad, recurso, oportunidad comercial) y su síntesis final.
2. **Elegir el tipo de CTA** según el objetivo (sección 5).
3. **Redactar acción y motivo** con la biblioteca de copys (sección 5) y la lista de prohibiciones de `skills/plogy-captions/SKILL.md`.
4. **Elegir la foto.** Abre los candidatos del moodboard con una herramienta de imagen. No decidas solo por el nombre del archivo. Criterios en la sección 6.
5. **Crear el derivado de la foto.** Original intacto. Recorte 4:5 a 1080x1350 (o el formato que pida la variante), y ajuste de color hacia la paleta si hace falta. Scripts en `scripts/`. Guarda el derivado en `assets/` de la pieza con un nombre que diga qué es.
6. **Maquetar en HTML** a 1080x1350 con los tokens y los patrones de la sección 4. Una lámina por variante, accesible con `?v=<letra>`.
7. **Exportar a PNG** con `scripts/render-slides.ps1`.
8. **Mirar cada PNG** (abrirlo como imagen) y corregir. Casi todas las variantes necesitaron un segundo pase. Lista de errores comunes en la sección 8.
9. **Registrar** en el brief de la pieza: variante, objetivo, copy, foto original, transformación y estado de derechos.
10. **Marcar pendientes.** Derechos de las fotos, licencia de la tipografía, recurso preparado si lo hay, aprobación humana.

## 4. Sistema visual

### Lienzo y márgenes

- Lámina de 1080 x 1350 px (4:5), el formato de partida del kit.
- Margen lateral de 96 px.
- Logo arriba a la izquierda: `top:80px; left:58px; width:230px`. El SVG trae área de protección, por eso el símbolo se alinea visualmente en x ≈ 96. En la variante B el logo va centrado.
- Contador `06/06` arriba a la derecha: `top:96px; right:96px`, 30 px, color `#e6dfd8`.
- Puntos de progreso abajo a la izquierda: `bottom:80px; left:96px`, 14 px, el activo en naranja.

### Color (de `brandkit/tokens.json`)

| Uso | Valor |
| --- | --- |
| Fondo oscuro | Ink `#171310` |
| Acción, resaltado | Orange `#ff5b00` |
| Texto sobre claro | Muted `#625951`, orangeText `#b43d00` para texto pequeño |
| Superficie clara | `#f4f1ef` |
| Logo en fondo oscuro | `brandkit/assets/plogy-white.svg` |
| Logo en fondo claro | `brandkit/assets/plogy-color.svg` |
| Símbolo solo | `brandkit/assets/plogy-symbol.svg` |

Naranja en texto grande (titulares de 90 px o más) pasa el contraste de texto grande sobre Ink. Para texto pequeño sobre claro usa `#b43d00`. Sobre un botón naranja el texto va en Ink, no en blanco (el kit lo documenta: el blanco sobre `#FF5B00` no alcanza 4.5:1).

### Tipografía

- Display: `Screener, 'Space Grotesk', 'Helvetica Neue', Arial, sans-serif`. **Screener solo tiene licencia demo.** Por eso en los render sale Space Grotesk, cargada desde Google Fonts con `<link>`. Pesos 500 y 700.
- Cuerpo: `'Helvetica Neue', Helvetica, Arial, sans-serif`. En el render de Windows sale Arial.
- Tamaños usados, sobre lienzo de 1080 px: titular 92 a 100 px, título del CTA 60 a 64 px, línea de motivo 34 px, contador 30 px. Nada de texto de lectura por debajo de 34 px.
- Titulares: `letter-spacing:-.035em; line-height:1.06; text-wrap:balance`. Título del CTA: `letter-spacing:-.03em; line-height:1.05`.

### Brillo del titular

La palabra o frase resaltada va en naranja con `text-shadow:0 0 34px rgba(255,91,0,.55)`. Inspirado en el "mindset correcto" brillante de 30X. En fondos que ya tienen naranja (variante C) el brillo desaparece y el texto pasa a blanco.

### Tarjeta de vidrio oscura (la firma)

```css
.glass{
  position:absolute; z-index:3; display:flex; align-items:center; gap:22px;
  border-radius:64px; color:#fff;
  background:linear-gradient(125deg,rgba(255,255,255,.24),rgba(255,255,255,.06)),rgba(23,19,16,.52);
  border:1.5px solid rgba(255,255,255,.42);
  backdrop-filter:blur(22px) saturate(125%);
  box-shadow:0 18px 50px rgba(0,0,0,.4), inset 0 1px 0 rgba(255,255,255,.5);
}
```

Posición base: `left:96px; top:1000px; width:888px`. Con `top:1000` el borde inferior queda cerca de y = 1230, por encima de los puntos de progreso (y ≈ 1263). Si el texto de la tarjeta crece, sube el `top`, no baja.

- Con símbolo: imagen `plogy-symbol.svg` de 116 px con márgenes negativos `-14px -8px -14px -20px` para compensar su área de protección. Texto a la derecha.
- Sin símbolo (C y E): tarjeta en columna, `padding:30px 48px 30px 40px`, título a 62 px y motivo a 34 px.
- La palabra clave del CTA (Plogy, PROCESO) va en naranja dentro del título.
- `backdrop-filter` funciona en Edge headless. Si un navegador no lo soporta, el fondo semitransparente sigue dando legibilidad aceptable.

### Degradados de protección sobre la foto

Cada variante lleva un `div.shade` con un degradado propio. Regla: oscurecer donde va texto, aclarar donde la foto cuenta la historia.

- B: `radial-gradient(ellipse at 50% 38%, rgba(23,19,16,.15) 0%, rgba(23,19,16,.7) 65%)` más `linear-gradient(to top, .92 → .2 → .55)`.
- C: `linear-gradient(to bottom, .85 → .35 en 40% → .25 en 60% → .75 al final)`.
- E: `linear-gradient(to bottom, .92 → .75 en 28% → .3 en 48% → .25 en 62% → .8 al final)`. Necesita más oscuro arriba porque la foto es clara y el cielo competía con el titular.
- F: `linear-gradient(to bottom, 1 → .9 en 22% → .15 en 42% → .1 en 65% → .7)`, y la foto baja 110 px (`top:110px; height:1240px`) para que el titular quede sobre fondo Ink y no sobre la nube.

## 5. Tipos de CTA y biblioteca de copys

El objetivo de la pieza decide el tipo. Las skills de Plogy definen tres acciones válidas más una comercial que aquí se probó como variante E.

| Tipo | Acción | Requisito antes de publicar |
| --- | --- | --- |
| Seguimiento | "Sigue a Plogy" | Ninguno |
| Comunidad | "Comenta Plogy" | Alguien responde los comentarios |
| Recurso | "Comenta <PALABRA>" | El recurso **existe** y la entrega por DM está configurada |
| Oportunidad comercial | "Escríbenos <PALABRA>" por DM | Plogy confirma qué ofrece en esa conversación |

Copys usados en la pieza 001 (úsalos como patrón, no como texto fijo):

| Tipo | Acción | Motivo |
| --- | --- | --- |
| Seguimiento A | Sigue a Plogy | Aquí la IA se implementa, no se promete. |
| Seguimiento B | Sigue a Plogy | Menos humo. Más IA implementada en negocios. |
| Seguimiento F | Sigue a Plogy | para que tu próxima automatización no termine así. |
| Comunidad C | Comenta Plogy | y cuéntanos qué proceso de tu negocio quieres ordenar primero. |
| Recurso D | Comenta MAPA | y te mandamos el checklist de las 3 preguntas. |
| Comercial E | Escríbenos PROCESO | por DM y vemos contigo por dónde empezar a automatizar. |

Cómo escribir un motivo nuevo:

- Parte de lo que Plogy hace: implementa soluciones en negocios y forma a quienes pueden construirlas. Tesis de marca: la IA crea valor cuando se implementa bien.
- Una frase corta, concreta, con un beneficio verificable o una postura. Sin "descubre cómo", "lleva al siguiente nivel", "en un mundo donde", "es importante destacar", "no se trata de", "sin duda", "el futuro ya llegó".
- Sin guiones largos. Sin emojis en LinkedIn. Sin promesas de revolución, riqueza, ausencia de esfuerzo ni garantías de resultados.
- No uses cifras ni cadencias que no puedas sostener ("cada semana", "+100 empresas") sin evidencia.
- Para recurso: la palabra clave en mayúsculas y corta, y el motivo describe exactamente lo que se entrega.
- Si el CTA cambia, el cierre del caption de Instagram y del post de LinkedIn debe coincidir con la misma acción.

## 6. Elección de la foto

Criterios, en este orden:

1. **Función narrativa.** ¿La foto explica, demuestra, contrasta o sostiene una atmósfera útil para el CTA? Si no, la lámina va solo tipográfica.
2. **Lectura con texto encima.** Debe tener una zona calmada para el titular y otra para la tarjeta.
3. **Resolución.** El lienzo es de 1080 px de ancho. Las fotos de menos de ~700 px de ancho se verán con trama al escalar. La variante B usa una foto de 474 px y funciona solo porque va muy oscurecida.
4. **Paleta.** Mejor si ya es cálida, oscura o en blanco y negro. Si tiene un rojo, se puede desplazar al Orange de Plogy. Colores ajenos (verde fosforescente, rosa fuerte) deben compensarse o evitarse.
5. **Seguridad.** Sin personas reales identificables, sin logos o marcas de agua de terceros, sin imágenes que se lean como promesa o como algo que Plogy no hizo.
6. **Derechos.** Todo el moodboard está como `unverified_reference_only`. Eso no cambia por adaptar el color.

Fotos usadas por variante y su original:

| Variante | Original en `assets/reference-originals/` | Función |
| --- | --- | --- |
| A | `perfection.jpg` | Persona y herramienta a punto de tocarse, con la ventana PROJECT.EXE en medio. |
| B | `cross the portal.jpg` | Alguien que avanza hacia el centro: dar el paso. |
| C | `being different.jpg` | Una silueta que no coincide con el público: la que ordena primero. |
| D | `tem coding.jpg` | Figuras idénticas tecleando: el trabajo repetido que un mapa de procesos ordena. |
| E | `creative working.jpg` | Un escritorio en medio de un campo: empezar desde cero, con ironía. |
| F | `explosion.jpg` | La consecuencia de automatizar sin orden. Ya se usa en la lámina 04. |

Revisadas y descartadas (siguen en la biblioteca, no se borraron):

| Archivo | Motivo del descarte |
| --- | --- |
| `vibe code.jpg` | Marca de agua de TikTok (@devmooreurl). |
| `watch the market.jpg` | Paleta verde fuera de marca y lectura de "información privilegiada", choca con el tono anti humo. |
| `ai watching.jpg` | Lleva el logo de otra marca (SOLTO). |
| `good enough.jpg` | Persona real identificable, sin relación con la tesis. |
| `connected.jpg` | Figura dibujada en ASCII blanco sobre negro, sin relación con la tesis de esta pieza. |
| `step up.jpg` | Dos formas verde neón sobre negro (estética de osciloscopio). El verde queda fuera de paleta y el motivo ya lo cubre `perfection.jpg`. |
| `glorious.jpg` | Caballo en trama de puntos de 1 bit. Sin relación con la tesis de esta pieza. |

Que se descartaran para la pieza 001 no significa que sean malas en general. Otra pieza con otra tesis puede usarlas.

## 7. Variantes: especificación

Todas llevan titular "Primero el proceso. Después la IA." (en A, C, D, E y F como titular; en B como entradilla pequeña) y contador 06/06.

| Var | Fondo y foto | Titular | Tarjeta o botón | Notas de composición |
| --- | --- | --- | --- | --- |
| A | Ink. Franja de las manos, 1080 x 440, `top:630`, mezcla `screen` (el negro de la foto se funde con Ink). | 100 px, arriba | Tarjeta de vidrio con símbolo, `top:1000` | La tarjeta cubre solo las puntas de los dedos. Está en `carrusel.html`, lámina 06. |
| B | Foto a página completa, todo centrado. | Entradilla de 44 px | Sin tarjeta. "Sigue a **Plogy**" en 128 px y subtítulo de 44 px | Logo centrado. Texto en `bottom:190`. Es la más limpia. |
| C | Foto a página completa, silueta naranja. | 100 px, blanco | Tarjeta de vidrio en columna, sin símbolo | El titular va en blanco porque el naranja se pierde sobre la silueta. |
| D | Foto clara arriba (1080 x 818) y panel Ink con esquinas superiores de 48 px, `top:790`. | 80 px | Botón naranja de 888 px de ancho con texto en Ink | La única en fondo claro arriba. Logo a color. El contador se oculta porque cae sobre la cabeza de una figura. |
| E | Foto a página completa, tono sepia. | 100 px | Tarjeta de vidrio en columna, sin símbolo | Más oscuro arriba para que el cielo no compita con el titular. |
| F | Foto desplazada 110 px hacia abajo. | 92 px | Tarjeta de vidrio con símbolo, `top:1030` | La tarjeta cubre parte de la silla, no al personaje. |

## 8. Errores encontrados y cómo se corrigieron

Estos errores aparecieron en el primer render. Revisa siempre contra esta lista.

1. **Elemento decorativo pisando el texto.** La esfera de degradado de la lámina 01 tapaba "más rápido." y la línea de apoyo. Se subió a la esquina superior derecha y se redujo. Regla: las formas decorativas no deben tocar el bloque de texto.
2. **Tarjeta tapando el sujeto de la foto.** En A, la tarjeta de vidrio cubría casi todas las manos. Se subió la foto a `top:630` y se bajó la tarjeta a `top:1000`. Regla: la tarjeta cubre solo una parte de la foto, nunca el sujeto.
3. **Texto partido en dos líneas con "text-wrap:balance" y ancho estrecho.** En A, la línea de motivo se rompía mal. Se ensanchó la tarjeta a 888 px.
4. **Pill de "Sigue a Plogy" en B demasiado grande.** A 168 px se partía en dos líneas. Se bajó a 128 px con `white-space:nowrap`.
5. **Selector CSS que afectó al motivo y al símbolo.** `.glass span` alcanzaba un `span.kw` (la palabra clave) y le aplicaba estilos de motivo. Se cambió a `.glass > span, .glass > div > span`.
6. **Contador encima de la cara de una figura.** En D el `06/06` caía sobre la cabeza. Se ocultó en esa variante.
7. **Naranja sobre naranja.** En C el titular "Después la IA." se perdía contra la silueta. Pasó a blanco y se quitó el brillo.
8. **Cielo claro compitiendo con el titular.** En E se oscureció la parte alta con un degradado más fuerte.
9. **Nube de la explosión detrás del titular.** En F se bajó la foto 110 px y se subió el degradado superior a opacidad 1.
10. **Línea clara en el borde de una foto.** El recorte de `perfection.jpg` traía una columna de píxeles más clara en el borde izquierdo. Se recortaron 6 px por lado.
11. **Caja gris visible alrededor de una foto sobre fondo claro (lámina 03).** `mix-blend-mode:multiply` oscurecía el fondo de la foto. Se quitó y se usó `border-radius:24px`.

## 9. Scripts y herramientas

### Derivados de foto (Python con Pillow)

- `scripts/derive-slides-pieza-001.py`: derivados de las láminas 03, 04 y 06 de la pieza 001.
- `scripts/derive-cta-variantes-pieza-001.py`: derivados de las variantes B a E.
- Uso: `python -I <script> "<ruta del kit>" "<carpeta assets de la pieza>"`.
- Funciones útiles: `shift_reds(im)` desplaza los píxeles rojos saturados hacia el matiz 0.058 (≈ 21°, el Orange de Plogy) conservando el resto de colores. Se usa con `s > 0.45` y matiz < 0.04 o > 0.96. `fit(im, box, size)` recorta y reescala con LANCZOS.
- Los recortes y coordenadas están escritos en el propio script. Son específicos de cada foto: para una foto nueva abre el original, decide el recorte 4:5 mirando la imagen, y copia la función.
- Corre Python con `-I` (modo aislado) cuando proceses archivos descargados o de terceros.

### Exportación

`scripts/render-slides.ps1` usa Edge headless: `--headless=new --window-size=1080,1350 --virtual-time-budget=8000 --screenshot=...`. Ejemplo:

```powershell
.\render-slides.ps1 -Html "<ruta>\cta-variantes.html" -OutDir "<ruta>\exports\cta" -Param v -Keys b,c,d -Prefix cta-
```

Edge está en `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` en esta máquina. No había Chrome instalado.

### Estructura de un HTML de variantes

Un solo archivo con una `<section class="slide v<letra>" data-v="<letra>">` por variante. Un script de 6 líneas al final lee `?v=<letra>` y deja visible solo esa lámina; sin parámetro, muestra todas en cuadrícula con `zoom:.4`. Esto permite revisar y exportar cada una desde el mismo archivo. El patrón se ve completo en `reference/snapshot-pieza-001/cta-variantes.html`.

## 10. Cómo generar un CTA nuevo para otra pieza

1. Lee `SKILL.md` y este archivo.
2. Copia `reference/snapshot-pieza-001/cta-variantes.html` a la carpeta de tu pieza. Ajusta las rutas relativas: `../../brandkit/assets/...` asume que la pieza vive en `piezas/<id>/`.
3. Cambia titular, acción y motivo según el brief de tu pieza. Elige el tipo de CTA según su objetivo.
4. Elige foto (sección 6). Crea el derivado con un script basado en `derive-cta-variantes-pieza-001.py`. Deja el original intacto.
5. Ajusta el degradado `.shade` de esa variante a tu foto. No reutilices los valores a ciegas: depende de dónde esté el sujeto.
6. Exporta, mira el PNG, corrige con la lista de la sección 8.
7. Registra en el brief de la pieza: variante, copy, foto original, transformación, derechos, pendientes.
8. Alinea el final del caption de Instagram y del post de LinkedIn con la acción elegida.

Para una pieza distinta, el patrón que más se reutiliza es: **tarjeta de vidrio (sección 4) + foto con función + degradado de protección + titular de síntesis**.

## 11. Control de calidad antes de entregar

- [ ] Una sola acción en el último slide.
- [ ] Motivo en voz Plogy, sin muletillas de IA, sin guiones largos, sin promesas de resultado.
- [ ] Si hay recurso: existe y la entrega por DM está configurada. Si hay oferta comercial: Plogy confirmó qué ofrece.
- [ ] Texto y logo por delante de la foto. Nada de texto de lectura menor a 34 px sobre el lienzo de 1080.
- [ ] La tarjeta no cubre el sujeto de la foto.
- [ ] Contraste suficiente: titular y motivo legibles sobre la zona de la foto donde caen.
- [ ] Contador y puntos no chocan con la foto ni con la tarjeta.
- [ ] Derivado de foto registrado, original intacto, estado de derechos anotado.
- [ ] Caption de Instagram y LinkedIn alineados con el CTA.
- [ ] Revisión humana antes de publicar. **No se publica nada desde este paquete.**

## 12. Estado y pendientes conocidos al 2026-10-19

- **Derechos de fotos:** las 6 fotos usadas siguen `unverified_reference_only`. Ninguna variante es publicable hasta verificar derechos o reemplazar la foto por material propio o licenciado.
- **Tipografía:** Screener solo tiene licencia demo. Space Grotesk se cargó desde Google Fonts: falta confirmar licencia para uso comercial.
- **Móvil real:** la legibilidad se comprobó a ojo en los PNG, no en un teléfono.
- **Variante B:** foto de baja resolución escalada. Funciona por el oscurecido.
- **Variante D:** requiere preparar el checklist de las 3 preguntas y la entrega por DM.
- **Variante E:** requiere confirmar qué ofrece Plogy en esa conversación.
- **Variante F:** revisar que "no termine así" no se lea como promesa de resultado.
- **Requisito de red:** el render depende de Google Fonts para Space Grotesk. Sin red, la tipografía cae a Helvetica/Arial y el layout cambia.
- **Aprobación humana:** pendiente, con fecha.

## 13. Reutilizaciones registradas

- **Pieza 002, "Los bancos frenan a los agentes de IA" (2026-10-19):** se reutilizó la variante C ("Comenta Plogy", tarjeta de vidrio sin símbolo sobre `being different.jpg` con el rojo pasado a naranja) en la lámina 07. Se copió el derivado `cta-c-silueta.jpg` a `piezas/002-bancos-frenan-agentes-ia/assets/07-cta-silueta.jpg`, se cambió el titular a "Primero leer. Después actuar." y se dejó en blanco, sin brillo naranja, por el mismo motivo que en la pieza 001 (el naranja se pierde contra la silueta). Se cambió el motivo a "y dinos qué le dejarías hacer a un agente en tu negocio." Funcionó sin ajustes de posición. El HTML de esa lámina está en `piezas/002-bancos-frenan-agentes-ia/carrusel.html`, sección `.s7`.
- **Aprendizaje de la pieza 002 sobre foto clara:** una foto casi blanca (`ai watching.jpg`) no admite texto blanco encima. Solución usada: invertir los píxeles de bajo color y mapearlos de Ink a blanco, de modo que el fondo pase a ser Ink y solo los elementos de color (cajas rojas pasadas a naranja) conserven su matiz. El código está en `piezas/002-bancos-frenan-agentes-ia/scripts/derive.py`.
- **Aprendizaje sobre logos ajenos:** si una foto trae el logo de otra marca, se puede recortar fuera, pero eso no resuelve los derechos de la obra. Se anota en el inventario.
- **Pieza 003, "Barato por token, caro por tarea" (2026-10-19):** primera pieza que aplica el flujo con reporte y DM. Se usó la variante E (tarjeta de vidrio sin símbolo sobre `creative working.jpg`) con una palabra clave: "Comenta COSTO y te mandamos la noticia completa y nuestro análisis." Se copió `cta-e-oficina.jpg` a `piezas/003-costo-por-token-vs-por-tarea/assets/07-cta-oficina.jpg`. Funcionó sin ajustes de posición. El titular de la lámina 07 va en dos líneas, la primera en blanco y la segunda en naranja con brillo. Los mensajes de DM están en `piezas/003-costo-por-token-vs-por-tarea/dm.md` y el reporte en `reporte.md`.
- **Aprendizaje de la pieza 003 sobre fotos con marco:** `ai watching 2.jpg` traía un marco negro de unos 55 px. Se recortó fuera antes de escalar, y se usó solo la franja de la cabeza y el teléfono como banda superior, con el texto debajo.
- **Aprendizaje sobre cifras en láminas:** cuando una lámina lleva números (precios, barras, facturas), cada cifra debe aparecer en la fuente o ser una cuenta aritmética visible a partir de cifras de la fuente, y la lámina nombra la fuente al pie. Los volúmenes inventados se rotulan "Ejemplo hipotético" y se dice que son inventados.
- **Aprendizaje sobre gráficos comparativos:** si la fuente incluye modelos o datos que no entran en el gráfico, se explica el criterio de exclusión en el brief y en el reporte, y se muestra en la lámina cualquier dato que cambie la lectura (por ejemplo, el índice de inteligencia al lado del costo).

### Reportes con imágenes (2026-10-19)

Los reportes que acompañan a un CTA de recurso llevan portada y figuras propias. Método, reglas y la ruta de exportación están en `FLUJO-REPORTE-DM.md`, sección 21. `render-slides.ps1` ahora acepta `-Width` y `-Height` (por defecto 1080x1350) para exportar figuras 1600x900.

### Pieza 004 (2026-10-19)

Usa la variante D (foto clara arriba, panel Ink, botón naranja) con la palabra clave MIGRAR. Ajustes frente a la variante original: panel desde top:770, h2 de 72 px y foto de 800 px de alto para que el botón de dos líneas no choque con los puntos de progreso. La foto de portada (`coding.jpg`) se desatura salvo la pantalla roja, que se lleva al naranja (ver `piezas/004-gpt-4o-se-apaga-14-enero/scripts/derive.py`). Detalles del flujo en `FLUJO-REPORTE-DM.md`, sección 22.

### Pieza 005 (2026-10-20): variante G, recurso con foto clara

Foto clara con fondo liso (`decission making team.jpg`, rojo llevado al naranja) y tarjeta Ink sólida con la palabra clave, en lugar de vidrio, porque el vidrio oscuro sobre fondo claro pierde el efecto. Se usa el color exacto del fondo de la foto como color de la lámina (244,243,239) para que el borde de la foto no se note. Titular arriba, foto en el centro recortada para que no la toque la tarjeta, tarjeta desde top:1030. En el selector de la tarjeta usar `.card > span` para no dar formato de bloque a la palabra clave. Ver `FLUJO-REPORTE-DM.md`, sección 23.

### Biblioteca de 30 CTAs (2026-10-20)

Pedido de Luciano: muchas más variaciones, con más imágenes. Se hicieron 30 (`piezas/cta-biblioteca/`). Qué se aprendió:

- **Mapa de color a la paleta.** Las fotos con colores ajenos (azul, verde, amarillo) se llevan a la marca reemplazando su luminosidad por un degradado Ink, naranja y crema (o Ink, violeta y coral). Un radiografía azul, un parque verde y una oficina amarilla pasan a naranja y siguen siendo reconocibles. Ver `gradient_map` en `piezas/cta-biblioteca/scripts/derive.py`. Los rojos se siguen llevando al naranja con `shift_reds`.
- **Familias de composición:** vidrio (con y sin símbolo), botón naranja ancho, panel Ink con botón, panel claro con botón Ink, panel con degradado de marca, texto grande, palabra clave gigante, texto impreso sobre una forma de la foto, cinta diagonal, losa naranja con corte, fondo naranja sólido, círculo con anillo, tarjeta inclinada, foto sobre crema, lista de lo que se recibe y maquetas de interfaz (perfil, comentario, comentario fijado, chat).
- **Titular naranja sobre foto naranja se pierde.** En seis variantes (06, 10, 18, 20, 21, 29) el titular pasó a blanco sin brillo y el naranja quedó solo en la palabra clave o el botón.
- **Logo blanco sobre foto clara o con ruido.** En 11, 13, 26 y 28 se añadió un degradado oscuro arriba (360 px) o se bajó la foto para que el logo caiga sobre Ink. En fondo naranja sólido el logo va en negro (`plogy-black.svg`).
- **Selector del texto de una tarjeta.** Usar `> span` para que no afecte a la palabra clave, como ya se anotó en la sección 8.
- **Evitar fotos de personas públicas.** Se descartaron las de fundadores de empresas y políticos del moodboard; quedaron figuras anónimas e ilustraciones.
