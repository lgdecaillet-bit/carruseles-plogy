# Revisión editorial · pieza 015
2026-10-20 · Momento: pieza terminada (Partes A, B y C) · Revisor: agente independiente

Archivos leídos: `brief.md`, `textos.md`, `comunidad.md`, `carrusel.html` y los siete PNG de `exports/` (vistos uno por uno). Contrastado contra `piezas/cta-biblioteca/` (`CATALOGO.md`, `ctas.html`, `scripts/derive.py`), `evidencia/fix_ctas.py`, `skills/plogy-cta-design/METODOLOGIA.md` y `SKILL.md`, `assets/reference-catalog.csv` y los briefs de las piezas 002 a 005 y 014. La pieza es documental sobre archivos internos y no cita fuentes web, así que no hubo nada que consultar con WebFetch.

## Veredicto

**Mejorar antes de seguir.** No falla ninguna regla dura y las cifras son reales y reproducibles, pero la Parte B deja dos criterios que el kit exige sólidos (evidencia y CTA) en 3, y la oportunidad tiene un 2 en encaje de marca: la pieza no toca la IA. Los problemas son de encuadre y de ejecución del CTA, no de fondo imposible: se arreglan sin cambiar el tema. Todo termina en revisión humana; además hay bloqueos que no son editoriales (derechos de las 30 fotos, quién responde los comentarios).

## Parte A · La oportunidad

| Criterio | Nota | Evidencia | Qué cambiaría |
| --- | --- | --- | --- |
| Relevancia para la audiencia | 3 | Sirve a quien cierra carruseles (Ploggers, responsables de redes). Un dueño de negocio rara vez diseña 30 finales; el brief declara audiencia "Ambos" pero el tema es oficio de contenido. | Decir en la portada o el caption para quién es el criterio (quien publica por Instagram para su negocio). |
| Encaje de marca | 2 | El propio brief dice "la pieza no es de IA". Ninguna lámina menciona IA, agentes ni implementación. El territorio de Plogy (IA que crea valor al implementarse bien en negocios) no aparece. Es Building Plogy, pero a diferencia de la 014 no hay ningún hilo con IA. | Si es cierto, y solo si Plogy lo confirma, mostrar cómo se produjo la biblioteca con el kit y los agentes. Si no, declarar que es pieza de autoridad de oficio, no de territorio. |
| Evidencia | 4 | Reproducido: 30 secciones `class="slide vNN"` en `ctas.html`, 30 PNG, tipos 10/6/8/6 (`CATALOGO.md`), 11 llamadas a `gradient_map` y 6 a `shift_reds` en `derive.py`, 14 variantes tocadas por `fix_ctas.py`, 6 reglas `.hl{color:#fff}` en `ctas.html`, 56 filas `unverified_reference_only`, 3 de 8 recursos con borrador (`reporte.md` y `dm.md` existen en 003, 004 y 005; 002 sin reporte). Falta: orden y autoría de los pasos y los "antes", declarados. | Resolver los matices de la Parte B (honestidad). |
| Novedad | 3 | Ver una biblioteca real de 30 finales con su lista de fallos es poco habitual; las cuatro lecciones (contraste, logo legible, marca en las fotos, prometer solo lo que existe) son conocidas. Solo la 4 es menos común. | Poner la lección 4 como eje y las demás como apoyo. |
| Urgencia | 2 | Sin fecha ni riesgo externo. Es un trabajo hecho el 2026-10-20 y podría salir cualquier semana. | Aceptarlo como pieza evergreen o atarla a un momento (próxima publicación de un CTA de recurso). |
| Potencial de conversación | 3 | La pregunta pide elegir un número entre 30 miniaturas que casi no se leen (ver CTA). La respuesta útil es el porqué, pero la gente no tiene experiencia propia que contar sobre "cuál usarías". La pregunta de LinkedIn ("qué revisa tu equipo antes de publicar el último slide") sí invita a experiencia propia. | Llevar al carrusel la pregunta de LinkedIn, o acotar a 4 o 6 finalistas visibles. |
| Ángulo distintivo | 4 | "Lo que falló en nuestros 30" con archivos que cualquiera puede abrir y un "ninguna se ha publicado ni medido" que ninguna guía genérica diría. Pierde puntos porque las lecciones 1 a 3 salen como hechos de gusto de marca (naranja, Ink) más que como criterio transferible. | Convertir cada lección en una prueba que el lector pueda aplicar. |
| Repetición | 4 | Otra pieza documental de Building Plogy sobre el kit (014), pero tema distinto. La mecánica "Comenta Plogy" ya está en la 002 y la 008; es mecánica, no tema. | Ninguno. |
| Relación comercial | 2 | Es de comunidad: no lleva a un servicio, recurso o conversación de Plogy. El brief lo declara (objetivo comunidad, sin recurso). Se acepta por la nota de la rúbrica, pero se declara. | Una frase final que conecte con lo que Plogy implementa, o aceptar que es solo comunidad. |

## Parte B · La pieza

| Criterio | Nota | Evidencia | Qué cambiaría |
| --- | --- | --- | --- |
| Tono Plogy | 4 | Directo y sin humo: "Armamos 30 formas de cerrar un carrusel." (01), "Ninguna se ha publicado ni medido." (02). Voz propia en el reconocimiento de límites. Algo seca: casi no hay personalidad fuera de las admisiones. | Una línea con más voz en la portada o en la 06 (por qué duele prometer sin tener). |
| Una idea por lámina y progresión | 4 | Cada lámina lleva una idea (01 tensión, 02 inventario, 03 a 06 lecciones, 07 pregunta). Pero la portada promete "14 hubo que corregirlas. Esto fue lo que falló." y solo las lecciones 2 y 3 (11 de las 14) son correcciones: la 1 es el tratamiento de color de `derive.py` y la 4 es un requisito del catálogo, no una corrección. El resto de las 14 (07, 17 y 25: 3 variantes) queda sin contar. La 02 frena el ritmo como inventario. | Reencuadrar la portada ("cuatro cosas que aprendimos") o ajustar las lecciones para que sean las 14. |
| Valor para la audiencia | 3 | El lector se lleva cuatro comprobaciones, pero tres están dichas sobre las fotos y la paleta de Plogy ("va a la paleta", "naranja sobre foto naranja"), no como criterio general. Lo único que puede usar mañana sin traducir es la 06 (el recurso debe existir). No hay recurso para llevarse. | Reescribir las lecciones 1 a 3 como prueba aplicable ("si el color del titular es el dominante de la foto, pásalo a blanco"; "mira el logo sobre la zona más cargada"). |
| Honestidad de la evidencia | 3 | Muy buena en lo central (nada publicado ni medido, "solo guardamos el después", no se declara qué CTA funciona). Pero: (a) la lámina 03 rotula las 11 fotos con mapa como "(azul, verde, amarillo)", y `derive.py` documenta como blanco y negro la 09 y la 13, como ASCII la 16 y como "brillo" la 12; solo 7 de 11 (03, 04, 10, 15, 21, 23, 26) tienen origen azul, verde o amarillo en los comentarios; (b) la portada y la tesis dicen que lo que falló "se vio al mirar los renders", y el propio brief declara sin verificar quién hizo qué y en qué orden; la lección 4 no se ve en ningún render; (c) LinkedIn pone "una foto cuyos colores no son los de la marca" entre los fallos de las 14 corregidas, pero ninguna corrección de `fix_ctas.py` es de color; (d) "la revisamos render por render" no está respaldado por ningún registro. | Corregir el rótulo de la 03 ("azul, verde, amarillo y blanco y negro", o quitar el paréntesis); quitar el color de la lista de las 14 en LinkedIn; matizar "la revisamos render por render" y "se vio al mirar los renders". |
| CTA | 3 | Una sola acción, nace del tema y la entrega (`comunidad.md`) existe con criterio, tres respuestas modelo y tabla de fuera de tema. Fricción: se pide elegir un número entre miniaturas de unos 115 px de ancho en el lienzo (`hoja-30.png`, 1568 px escalado a 730), unos 41 pt en un teléfono de 390 pt; los titulares no se leen, solo los números; el lector no sabe qué eligió. La palabra "Plogy" no activa nada y aparece como palabra clave, y la nota final mezcla un segundo mensaje ("Ninguna se ha publicado ni medido todavía") con el pedido. Persona que responde: PENDIENTE. | Mostrar entre 4 y 6 finalistas grandes y numeradas, o cambiar la pregunta a una respuesta sin número; quitar "Plogy" como palabra obligatoria; dejar la nota final solo con la acción. |
| Diseño y legibilidad | 4 | Jerarquía nítida, titulares grandes y legibles, logo y texto delante de toda imagen, alternancia Ink y superficie, marca reconocible. Lámina 06 limpia. Detalles: miniaturas ilegibles por diseño (02 a 05); en la 06 la columna de descripciones se desalinea unos píxeles entre filas (x aproximada 466 a 473); en la 03 hay un hueco en la segunda fila; en la 05 el logo de la 11 queda pegado al borde de la foto (el brief lo reconoce). La 04 afirma "el titular se pierde" pero solo muestra los "después", así que el lector no ve el fallo. | Alinear la columna de la 06; en la 04 mostrar un solo ejemplo ampliado con el titular en blanco y describir el antes en una línea. |
| Coherencia entre canales | 4 | Caption, LinkedIn y `comunidad.md` sostienen la misma tesis y las mismas cifras (30, 14, 8 y 3). LinkedIn añade criterio y pregunta distinta; no repite el cierre. Los dos textos recorren el mismo orden de datos y el de LinkedIn repite la afirmación de color de la 14 que el brief no respalda. | Corregir lo ya señalado. |
| Originalidad frente a lo que ya existe | 4 | Se reconocería como de Plogy por el material (30 finales propios con su lista de fallos) y por el "ninguna se ha publicado ni medido". La parte visual es la marca, no una voz formal distinta. | Ninguno. |

## Parte C · Reglas duras

| Regla | Cumple / Falla | Evidencia |
| --- | --- | --- |
| 1. Sin guiones largos | Cumple | Búsqueda de — y – en `brief.md`, `textos.md`, `comunidad.md` y `carrusel.html`: 0 coincidencias. |
| 2. Sin muletillas de IA | Cumple | Búsqueda de las expresiones prohibidas y variantes: 0 coincidencias. |
| 3. Sin emojis en LinkedIn | Cumple | Búsqueda de emojis en `textos.md`: 0. El post tiene unas 211 palabras. |
| 4. Hasta cinco hashtags en el caption | Cumple | Tres: #CarruselesDeInstagram, #LlamadaALaAccion, #DisenoDeContenido (decisión declarada). Sin ñe ni tilde. |
| 5. No inventa datos ni casos | Cumple, con reservas | Ninguna cifra inventada; las hipótesis y límites están rotulados. Las generalizaciones de la Parte B (rótulo de color de la 03, "se vio al mirar los renders") no son datos inventados sino encuadres no respaldados por el propio kit. |
| 6. Una idea por lámina y un CTA en la última | Cumple | Una idea por lámina; CTA único en la 07 (la nota "ninguna se ha publicado" acompaña, no compite). |
| 7. Texto y logo por delante de las imágenes | Cumple | En las siete láminas el logo y el texto están encima o fuera de la imagen. En la 07 el logo va sobre la banda Ink por encima de la foto. |
| 8. CTA de recurso con recurso y entrega preparados | No aplica | El CTA no promete recurso. `comunidad.md` existe como borrador y no promete enviar nada. |
| 9. No dice que algo está publicado o aprobado | Cumple | "Aprobación humana y fecha: PENDIENTE" en el brief; `textos.md` y `comunidad.md` marcan "No publicar". |
| 10. Cifras coinciden con brief y fuente | Cumple | 30, 10/6/8/6, 17 = 11 + 6, 6 titulares, 5 de logo, 14 = 6 + 5 + 3, 8 y 3 coinciden entre láminas, caption, LinkedIn, brief y archivos. Matiz: el brief nombra una discrepancia con `SKILL.md` ("26 fotos, 14 composiciones") que hoy no se reproduce: `SKILL.md` ya dice 30 fotos (28 más 2). Nota del brief desactualizada. |

## Lo que verifiqué y lo que no

Verifiqué por mi cuenta, contra los archivos del kit: el conteo de 30 variantes y sus tipos; los tratamientos de color (listas de `derive.py` y catálogo) y que coinciden con las láminas 03; que las 14 variantes de `fix_ctas.py` están aplicadas en `ctas.html` (reglas de titular blanco, sombras, logo negro en la 23); los estados de los recursos 003, 004 y 005 y la ausencia de reporte en 002; los 56 `unverified_reference_only`; la foto de la 11 (1044 por 588); las cifras de caption y LinkedIn; las reglas de estilo con búsqueda. Vi los siete PNG.

No pude verificar: que ninguna variante se haya publicado ni medido (el kit no lo prueba; lo confirma Plogy); quién hizo cada corrección y en qué orden, y por tanto que "se vio al mirar los renders"; que los "antes" no existan fuera del kit; si el tratamiento de color (lección 1) fue una corrección o parte del diseño inicial; la legibilidad en un teléfono real (calculada, no vista); el estado de derechos de las 30 fotos y de las tipografías.

## Tres cosas que más subirían la pieza

1. Arreglar el CTA para que se pueda responder: finalistas grandes y numeradas, sin "Plogy" como palabra obligatoria y sin el segundo mensaje en la nota. Hoy el lector no puede elegir con lo que ve.
2. Alinear el encuadre con la evidencia: la portada, el rótulo de la 03 (las 4 fotos que no son azul, verde o amarillo) y LinkedIn (color entre los 14) y quitar la afirmación "se vio al mirar los renders" para la lección 4.
3. Convertir las lecciones 1 a 3 en criterios aplicables por el lector y decidir el encaje de marca: o se ancla en cómo se implementa IA en Plogy (si es cierto) o se declara como pieza de autoridad de oficio.

## Preguntas para la persona que decide

- ¿La biblioteca se produjo con el kit y los agentes? Si sí, eso resuelve el encaje de marca; si no, ¿se acepta una pieza sin hilo de IA?
- ¿El tratamiento de color de las fotos fue una corrección posterior a ver los renders o parte del diseño inicial? De eso depende la portada y la lección 1.
- ¿Quién responde los comentarios y en qué ventana? Hoy figura PENDIENTE.
- ¿Se resuelven o se reemplazan los derechos de las 30 fotos antes de publicar? La lámina 02 las reúne todas y las miniaturas 05, 10 y 29 tienen tono fuerte según el catálogo.
- ¿Se confirma el plural ("armamos", "tuvimos que corregir") y que no hay capturas del antes ni datos de publicación fuera del kit?

Calibración (umbral usado): CTA 3 cuando el pedido tiene fricción de ejecución o un segundo mensaje, aunque la entrega esté preparada en borrador; 4 si la acción es única, nace del valor, se puede ejecutar con lo que el lector ve y la entrega existe. Honestidad 3 cuando una etiqueta pública no coincide con el archivo fuente aunque las cifras sí.
