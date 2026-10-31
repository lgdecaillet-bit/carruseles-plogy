# Pieza 014 · Un agente calificó nuestras piezas

Estado: BORRADOR PARA REVISIÓN HUMANA. No publicar.

Plogy confirma la redacción en primera persona. Los textos usan el plural ("pedimos", "encontró", "corregimos") solo para lo que consta en los archivos del kit, y está marcado así en `textos.md`.

Pieza documental (Building Plogy) sobre lo que ocurrió el 2026-10-20: un agente revisor independiente calificó las cinco piezas ya hechas (001 a 005). Sin foto de biblioteca salvo el fondo del CTA. Las láminas 01 a 06 son composiciones tipográficas y de datos reales. Sin reporte ni DM: el CTA es de seguimiento.

## Oportunidad

- ID y estado editorial: 014 · borrador completo (carrusel, exports, textos y este brief), pendiente de revisión humana
- Tipo de origen: documental. Archivos internos del propio kit. No parte de una noticia ni de una fuente externa.
- Fuente primaria, fecha y registro interno: los informes `piezas\00N\revision-editorial.md` y `revision-editorial-2.md` (ocho informes, todos del 2026-10-20), `skills\plogy-editorial-review\SKILL.md`, `RUBRICA.md` y `CALIBRACION.md`, y `.claude\agents\plogy-revisor-editorial.md`. Leídos completos el 2026-10-20 por quien escribe esta pieza. No hay enlaces web: no se consultó ninguna fuente de terceros.
- Interés comercial de la fuente: el revisor es un agente de Plogy y evalúa piezas de Plogy. No es un tercero independiente en el sentido externo. "Independiente" significa aquí distinto del agente que escribió la pieza, no ajeno a la empresa. La pieza lo dice en la lámina 02 ("un revisor por pieza, sin ver el razonamiento de quien la escribió").
- Qué afirma la fuente y qué queda sin verificar:
  - Verificado en los archivos (ver tabla de evidencia): veredictos antes y después, conteo de criterios y reglas, qué errores confirmó el revisor, cuáles se corrigieron según los archivos actuales de cada pieza, y las fallas del propio revisor.
  - Verificado visualmente: la mesa de la lámina 07 de 005 recortada muestra tres personas; la foto completa de la lámina 03 de 001 muestra cuatro (se miraron los PNG de ambas).
  - No verificado: que cada hallazgo del revisor sea correcto en sentido absoluto. La pieza reporta lo que el revisor confirmó leyendo la fuente (según sus propios informes); no repite la lectura de OpenAI, The Next Web, AIHubMix ni Vals AI. El estado de las correcciones sale de las fechas y del contenido actual de los archivos, no de un registro de cambios completo.
  - No verificado: que las segundas revisiones de 003 y 004 se hicieran sobre las versiones corregidas. Es un indicio por fechas de archivo (primera revisión hacia las 10:07 y 10:08; archivos de 003 y 004 modificados a las 10:17 y 10:18; segunda revisión a las 10:21), no un registro.
  - Límites: el revisor es un agente de IA, no un editor humano. No publica ni autoriza publicar. La primera ronda fueron cinco revisores, uno por pieza (según `CALIBRACION.md`); la segunda ronda son tres informes más (003, 004 y 005). 001 y 002 no tienen segunda revisión. La columna "Veredicto de la persona" de `CALIBRACION.md` está vacía: ningún humano de Plogy ha calibrado todavía al revisor.
- Audiencia: Ambos (negocios que dudan de contratar o usar un revisor automático, y quienes construyen flujos con agentes)
- Vertical: IA y automatizaciones
- Pilar principal: Documental
- Pilar secundario: Conocimiento
- Subcategoría y confianza de clasificación: Building Plogy · confianza alta en el pilar (es algo que ocurrió y consta en archivos). El valor de Conocimiento está en el criterio final (lámina 06 y LinkedIn).
- Tesis de Plogy en una frase: un agente revisor independiente encuentra errores reales que quien escribe no ve, pero también se contradice, y por eso la decisión de publicar sigue siendo humana.
- Problema o tensión que hace relevante la pieza: quien produce contenido o automatiza con IA está tentado a dar por buena la revisión de otro agente, o a descartarla del todo.
- Ángulo distintivo y por qué Plogy puede decirlo: Plogy implementa IA en negocios y aquí muestra, con sus propios archivos, qué funcionó y qué no del revisor. No es un caso de cliente. Es evidencia interna, con las limitaciones declaradas.
- Objetivo: seguimiento
- Término principal de búsqueda y secundarios: "revisión editorial con agente de IA". Secundarios: "agente revisor independiente", "rúbrica para calificar contenido con IA".
- CTA del último slide y estado del recurso prometido: "Sigue a Plogy. Aquí mostramos el proceso, con sus errores." Variante 10 de la biblioteca de CTAs (losa naranja con corte diagonal y foto), adaptada. Sin palabra clave, sin reporte ni DM. Sin recurso prometido. Plogy confirma que quiere sostener la frase "Aquí mostramos el proceso, con sus errores", porque es una promesa a futuro.

Por qué este tema: pedido de Luciano de una pieza documental. Muestra a Plogy usando un agente para revisar sus propias piezas y contando con honestidad qué salió bien y qué no. Las cifras y citas no son inventadas: salen de los informes.

## Tabla de evidencia (dato, archivo y dónde está)

Todas las rutas son relativas a `PLOGY_Carousel_Agent_Kit\`.

### A. Qué es el revisor y cómo califica (lámina 02)

| Dato en la pieza | Archivo y lugar | Estado |
| --- | --- | --- |
| Es un agente que juzga y no produce; no es el autor de la pieza | `.claude\agents\plogy-revisor-editorial.md`, párrafo inicial ("Juzgas, no produces") | Verificado |
| No corrige la pieza | `skills\plogy-editorial-review\SKILL.md`, "Este skill lo usa un revisor independiente... No reescribe la pieza ni la corrige" y "El revisor no modifica ningún archivo de la pieza" | Verificado. Nota: el agente tiene la herramienta Write en su definición (Read, Glob, Grep, WebFetch, Write) y la restricción es una instrucción, no un bloqueo técnico. La lámina dice "no corrige ni publica" |
| No publica ni autoriza publicar | `.claude\agents\plogy-revisor-editorial.md`, "Nunca autorices una publicación: todo termina en revisión humana"; no tiene herramienta de publicación | Verificado |
| Un revisor por pieza, sin ver el razonamiento del autor | `skills\plogy-editorial-review\CALIBRACION.md`, "Primera pasada": "Cinco revisores independientes, uno por pieza, con la misma rúbrica y sin ver el razonamiento del autor" | Verificado (solo aplica a la primera ronda) |
| 17 criterios con nota de 1 a 5 | `skills\plogy-editorial-review\RUBRICA.md`, Parte A (9 criterios) y Parte B (8 criterios) | Verificado |
| No hay nota global | `SKILL.md`, "Cómo califica": "No hay nota global" | Verificado |
| 10 reglas duras de cumple o falla; una falla impide "Publicar con ajustes" | `RUBRICA.md`, Parte C y cierre de la Parte C | Verificado |
| Un 5 es raro; lo correcto pero genérico es un 3 | `SKILL.md`, "Cómo califica": "Una nota 5 es rara... si algo es correcto pero genérico, es 3" | Verificado |

### B. Veredictos por pieza, antes y después (lámina 03)

| Pieza | Primera revisión | Segunda revisión | Archivos y lugar |
| --- | --- | --- | --- |
| 001 | Mejorar antes de seguir | No existe | `piezas\001-automatizar-el-desorden\revision-editorial.md`, "Veredicto" |
| 002 | Mejorar antes de seguir | No existe | `piezas\002-bancos-frenan-agentes-ia\revision-editorial.md`, "Veredicto" |
| 003 | Mejorar antes de seguir (falla la regla dura 10) | Mejorar antes de seguir, "cerca de Publicar con ajustes", sin fallas duras | `piezas\003-costo-por-token-vs-por-tarea\revision-editorial.md` y `revision-editorial-2.md`, "Veredicto" y Parte C |
| 004 | Mejorar antes de seguir | Mejorar antes de seguir | `piezas\004-gpt-4o-se-apaga-14-enero\revision-editorial.md` y `revision-editorial-2.md`, "Veredicto" |
| 005 | Publicar con ajustes | Mejorar antes de seguir | `piezas\005-medir-antes-de-automatizar\revision-editorial.md` y `revision-editorial-2.md`, "Veredicto" |

Los veredictos de la primera ronda coinciden con `CALIBRACION.md` (tabla, columna "Veredicto del revisor"). De los ocho informes, solo uno marca una falla dura: 003, primera revisión, regla 10 (`revision-editorial.md`, Parte C). Las segundas revisiones de 003, 004 y 005 no marcan fallas duras.

### C. Hallazgos de hecho que el revisor confirmó y estado hoy (láminas 04 y 05)

Trece hallazgos. Los que citan "leyendo la fuente" (H1 a H9) el revisor los comprobó con WebFetch según su informe. H10 a H13 salen de leer la pieza. La columna Estado se verificó mirando los archivos actuales de la pieza.

| ID | Pieza | Hallazgo | Informe y lugar | Estado hoy | Evidencia del estado |
| --- | --- | --- | --- | --- | --- |
| H1 | 002 | Lámina 03 dice que los dos bancos permiten ver saldos por MCP; la fuente (The Next Web) lo dice de Schwab. De JPMorgan solo consta que algunas herramientas ven datos de cuenta | `002\revision-editorial.md`, Parte B "Honestidad de la evidencia" (a) | Sin corregir | `002\carrusel.html` línea 148 sigue igual; la pieza no se ha modificado desde el 2026-10-19 y no hay segunda revisión |
| H2 | 002 | LinkedIn dice "dos de los bancos más grandes de Estados Unidos", dato sin fuente | `002\revision-editorial.md`, Parte B "Honestidad de la evidencia" (d) | Sin corregir | `002\brief.md` línea 65 sigue igual. No sale en las láminas de 014 |
| H3 | 003 | "Razonamiento alto" para todos los modelos; AIHubMix pone a GPT-6 Astra en "max" y no indica nivel para Sonnet 5.5 ni Opus 5.5 | `003\revision-editorial.md`, Parte C regla 10; `CALIBRACION.md`, "Hallazgo confirmado a mano" | Corregido | `003\carrusel.html` línea 199 ("alto en Argon, max en Astra"); `003\textos.md` líneas 11 y 32; `003\reporte.md` historial del 2026-10-20 |
| H4 | 003 | El reporte decía "primero entre 50 modelos" en Vals; la página dice 41 y 22 | `003\revision-editorial.md`, Parte C regla 10 | Corregido | `003\reporte.md` línea 53 ("primero entre 41 modelos") y historial |
| H5 | 003 | Lámina 02 da "se duplica el 1 de diciembre" como hecho; la fecha no está confirmada por Google | `003\revision-editorial.md`, Parte B "Honestidad" (1); `revision-editorial-2.md`, Parte B "Honestidad" (b) | A medias | `003\carrusel.html` línea 167 ya lleva "reportada, no confirmada por Google", pero el titular de la línea 152 sigue afirmando la fecha y la segunda revisión aún pide repetir la nota en las láminas 04 y 06 |
| H6 | 003 | LinkedIn dice "el costo por tarea que midió Artificial Analysis" para $3,98 y $39.800, que son una proyección con el precio de diciembre | `003\revision-editorial-2.md`, Parte B "Honestidad" (a) | Sin corregir | `003\textos.md` línea 36 sigue igual; el archivo no cambió después de la segunda revisión |
| H7 | 004 | "Luna cuesta 25 veces menos por token de entrada" solo vale frente a GPT-4o; frente a GPT-4o mini son 1,5 veces | `004\revision-editorial.md`, Parte B "Honestidad" (a) | Corregido | `004\carrusel.html` línea 180 ("hasta 25 veces menos"); `004\reporte.md` línea 56 y tabla por modelo |
| H8 | 004 | `fig-calendario` decía que el 6 de enero no aparece en la página de OpenAI; sí aparece (cierre general de fine-tuning de autoservicio, sin nombrar modelos) | `004\revision-editorial.md`, Parte B "Honestidad" (b) | Corregido | `004\reporte.md` líneas 29 y 69; `004\reporte-figuras.html` línea 100 |
| H9 | 004 | La política de seis meses de aviso se atribuía solo a Mixed; la página de OpenAI también la declara, para modelos de disponibilidad general | `004\revision-editorial.md`, Parte B "Honestidad" (c) | Corregido | `004\reporte.md` línea 27 y historial |
| H10 | 005 | Lógica invertida: la figura decía que olvidar el reproceso hace que el ahorro "se vea mayor de lo que es"; en el ejemplo omitirlo lo subestima | `005\revision-editorial.md`, "Tres cosas que más subirían la pieza" 1 | Corregido | `005\reporte-figuras.html` línea 132 ("la comparación engaña"); `005\reporte.md` historial |
| H11 | 005 | "Cuatro personas" donde la lámina 07 muestra tres (la foto está recortada) | `005\revision-editorial-2.md`, "Encontré, además" | Corregido | `005\carrusel.html` línea 219, `005\brief.md` línea 40 y `005\reporte.md` línea 70 dicen "tres". En 001 la foto completa sí muestra cuatro, por eso allí no es error |
| H12 | 005 | La fórmula del costo ("tiempo por caso × volumen × costo de la hora") no convierte minutos a horas | `005\revision-editorial-2.md`, "Encontré, además" | Sin corregir | `005\reporte.md` línea 39 y `005\textos.md` línea 30 siguen sin ÷ 60; solo el checklist (línea 89) lo lleva |
| H13 | 001 | "6 formas de anotar" a partir de tres canales no se explica | `001\revision-editorial.md`, Parte B "Honestidad" (a) | Sin corregir | `001\carrusel.html` líneas 119 a 127 sin cambios desde el 2026-10-19; no hay segunda revisión |

Recuento: 7 corregidos (H3, H4, H7, H8, H9, H10, H11), 1 a medias (H5), 5 sin corregir (H1, H2, H6, H12, H13). La lámina 04 muestra H1, H3, H5 y H7; la lámina 05 muestra H10, H11 y H13. El recuento de LinkedIn sale de aquí.

Citas textuales de la lámina 05, verificadas por búsqueda exacta en el informe:
- «En el ejemplo ocurre lo contrario: el reproceso baja de 8 a 4 casos, así que omitirlo subestima el ahorro.» (`005\revision-editorial.md`)
- «En la lámina 7 la mesa tiene tres personas visibles» (`005\revision-editorial-2.md`)
- «"6 formas de anotar" a partir de tres canales no se explica (¿por qué seis?)» (`001\revision-editorial.md`)

### D. Lo que no funcionó del revisor (lámina 06)

| Dato en la pieza | Archivo y lugar | Estado |
| --- | --- | --- |
| Las dos revisiones de 005 tienen las mismas 17 notas (nueve 4, siete 3, un 2) y veredictos distintos | `005\revision-editorial.md` y `revision-editorial-2.md`, tablas de Parte A y B. Secuencia en ambas: Parte A 4,4,3,3,2,3,3,3,4; Parte B 4,4,4,4,4,4,3,3. El segundo informe cita "siete notas 3" y que "supera el umbral de 'pocos 3'"; el primero con las mismas notas dio "Publicar con ajustes" | Verificado (contado por script sobre las tablas de los ocho informes) |
| Nota de CTA 3, 3 y 4 en 003, 004 y 005 con el recurso en borrador en las tres | Fila "CTA" de Parte B en los seis informes (003: 3 y 3; 004: 3 y 3; 005: 4 y 4). `CALIBRACION.md`, "Primera pasada": "Falta una regla explícita para 'recurso en borrador'" | Verificado. La regla dura 8 solo exige que el borrador exista; la nota de CTA no define cuánto vale un recurso en borrador |
| Un revisor dijo "no los leí" sobre Mixed y Digital Applied | `004\revision-editorial.md`, "No verificado": "Mixed y Digital Applied (no los leí; el brief dice que sí)". `CALIBRACION.md`: "Un revisor (004) dijo no haber podido leer fuentes de terceros que el autor sí leyó" | Verificado. La segunda revisión de 004 sí las leyó y deja sin leer FourWeekMBA y daily.dev |
| Otras fuentes no leídas | 003 (ambas revisiones): Artificial Analysis y el anuncio de Google. 002: la entrevista de Bloomberg y la llamada de resultados de JPMorgan. 005 primera revisión: leyó solo las primeras 40 líneas del brief de 003 para el criterio de repetición | Verificado (secciones "No verifiqué") |
| La columna "Veredicto de la persona" está vacía | `CALIBRACION.md`, tabla de calibración: las cinco filas en blanco | Verificado |
| El revisor tampoco verificó derechos de fotos, licencias de tipografía ni legibilidad en móvil real | Sección "No verifiqué" de los ocho informes | Verificado |

Lo que el revisor sí hizo bien y la pieza no exagera: encontró errores contra fuentes que él mismo leyó, declaró en cada informe lo que no pudo verificar, y no autorizó ninguna publicación.

## Secuencia (7 láminas)

| Slide | Función narrativa | Titular | Texto de apoyo | Qué aporta al siguiente | Imagen y razón | Composición | Fuente de la afirmación |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | Tensión | Le pedimos a un agente que calificara nuestras cinco piezas. | Cuatro recibieron «Mejorar antes de seguir». Una, «Publicar con ajustes». | ¿Quién es ese revisor y cómo califica? | Sin foto. Cinco cuadros numerados: cuatro con borde, uno relleno | Fondo Ink | Tabla B |
| 02 | Cómo califica | Un revisor que juzga. No corrige ni publica. | 17 criterios, 10 reglas duras, el 3 es lo correcto pero genérico | ¿Qué salió? | Sin foto. Tres tarjetas con cifra | Fondo superficie | Tabla A |
| 03 | Resultado | Una sola salió «Publicar con ajustes». Al repetir, bajó. | Tabla de 5 piezas con primera y segunda revisión | ¿Qué errores encontró de verdad? | Sin foto. Tabla de datos | Fondo claro | Tabla B |
| 04 | Hallazgos contra la fuente | Lo que confirmó leyendo la fuente. | Cuatro errores con su estado (corregido, sin corregir, a medias) | ¿Y en lo que escribimos nosotros? | Sin foto. Tarjetas | Fondo Ink | Tabla C (H1, H3, H5, H7) |
| 05 | Hallazgos en las láminas | Y lo que vio en nuestras láminas. | Tres fragmentos textuales de informes reales | ¿Qué falló del revisor? | Sin foto. Fragmentos de informe renderizados | Fondo superficie | Tabla C (H10, H11, H13) |
| 06 | Reverso | El revisor también falló. | Mismas notas y otro veredicto; sin regla para el recurso en borrador; fuentes sin leer; calibración vacía | Cierre | Sin foto. Tres tarjetas con dato | Fondo claro | Tabla D |
| 07 | CTA seguimiento | Quien escribe la pieza no la califica. | Sigue a Plogy. Aquí mostramos el proceso, con sus errores. | Cierre | Haz de luz sobre terreno de trama (derivado 10 de la biblioteca de CTAs) con losa naranja diagonal | Variante 10 adaptada | `AGENTS.md`: "quien escribe una pieza no la califica" |

Cada lámina lleva contador y puntos de progreso. En la 07 los puntos son Ink sobre la losa naranja y el contador es blanco sobre la foto.

## Textos por canal

Ver `textos.md`: caption de Instagram con hashtags y su razón, post de LinkedIn y diferencia de enfoque. El CTA del caption (seguir a Plogy) coincide con el de la lámina 07. Plogy confirma la redacción en primera persona.

## Estado del flujo (checklist de salida)

CTA de seguimiento: no hay recurso, reporte ni DM, y la biblioteca de CTAs no exige nada previo para este tipo.

- [x] Cada afirmación factual tiene su archivo de origen en la tabla de evidencia, con lo no verificado escrito.
- [x] Sin hipótesis ni cifras inventadas. Todas las cifras salen de los informes de revisión, de la rúbrica o de `CALIBRACION.md`.
- [x] CTA del carrusel y del caption alineados (seguir a Plogy).
- [ ] Plogy confirma la redacción en primera persona.
- [ ] Plogy confirma que quiere publicar errores propios de las piezas 001 a 005, incluidas menciones a terceros (Schwab, JPMorgan, OpenAI, Mixed, Digital Applied), y que las piezas 001 a 005 aún están en borrador y no publicadas.
- [ ] Plogy confirma que la promesa "Aquí mostramos el proceso, con sus errores" es una política que quiere sostener.
- [ ] Revalidar el estado de las correcciones (tabla C) el día de publicar: los archivos de 001 a 005 cambian.
- [ ] Decidir si se repite la revisión de 001 y 002 antes de publicar, para no dejar solo una revisión en dos de las cinco piezas.
- [ ] Derechos de la foto del fondo de la lámina 07 y licencias de tipografía resueltos.
- [ ] Ver las láminas en un móvil real.
- [ ] Aprobación humana con fecha.

## Revisión

- Evidencia y procedencia de cada dato: ver la tabla de evidencia. Todo sale de archivos internos del kit leídos completos. No hay fuentes de terceros.
- Derechos de cada asset y licencia de la tipografía: una foto de la biblioteca con derechos sin verificar (ver inventario). Screener solo tiene licencia demo. Space Grotesk se cargó desde Google Fonts: falta confirmar licencia para uso comercial.
- Legibilidad de cada slide a tamaño móvil: revisada a simple vista en los PNG exportados, una a una. Titulares de 74 a 104 px; apoyo de 33 a 40 px; los textos de fuente y notas, el contador y los puntos bajan a 30 px; las etiquetas de estado (chips) y los encabezados de tabla, a 26 a 28 px. Pendiente confirmar en un móvil real.
- Coherencia entre tesis, secuencia, caption y CTA: la tesis (el revisor acierta y se contradice, por eso decide una persona), el recuento de hallazgos y el CTA de seguir coinciden entre carrusel, caption y LinkedIn.
- Verificación de estilo: sin guiones largos, sin emojis en LinkedIn, hashtags ≤ 5, sin las muletillas de la lista prohibida (búsqueda de texto en el carrusel, `textos.md` y este brief).
- Honestidad: no se afirma que nada esté publicado, aprobado o configurado. El revisor se presenta como agente de IA, no como editor humano, y se dice que no publica.
- Pendiente de aprobación humana: ver el checklist de arriba.
- Aprobación humana y fecha: PENDIENTE

## Archivos de la pieza

- `carrusel.html`: fuente editable de las 7 láminas (1080x1350). Sin parámetros muestra todas; con `?s=1` a `?s=7`, una sola.
- `exports/slide-01.png` a `slide-07.png`: exportaciones en orden.
- `textos.md` y `brief.md`: textos por canal y este brief. Cada uno tiene también su versión `.html`, generada para el visor.
- `assets/10-platillo.jpg`: derivado de foto del CTA (copia del derivado de la biblioteca).

## Inventario de assets

| Asset | Origen | Transformación | Lámina | Derechos |
| --- | --- | --- | --- | --- |
| `brandkit/assets/plogy-color.svg` | Brand kit Plogy | Ninguna | 02, 03, 05, 06 | Propio de Plogy. Trazado derivado de la fuente demo, por verificar. |
| `brandkit/assets/plogy-white.svg` | Brand kit Plogy | Ninguna | 01, 04, 07 | Igual que el anterior |
| `assets/10-platillo.jpg` | Copia exacta (mismo SHA-256) de `piezas/cta-biblioteca/assets/10-platillo.jpg`. Original: `assets/reference-originals/another workd.jpg` (haz de luz). Autor desconocido. | Derivado de la biblioteca: mapa a Ink, naranja y crema. No se re-derivó. En la pieza se aplica un degradado Ink superior por CSS. | 07 | `unverified_reference_only`. NO publicar hasta verificar derechos. |
| Cuadros, tarjetas, tabla, fragmentos y chips | CSS y texto | Ninguna | 01 a 06 | Propio |

El original sigue intacto en `assets/reference-originals/`. No hay fotos de personas en la pieza. Ninguna de las otras láminas usa foto.

Por qué una sola foto: la pieza es documental y su evidencia son los datos de los informes. La foto solo sostiene el CTA, siguiendo la variante 10.
