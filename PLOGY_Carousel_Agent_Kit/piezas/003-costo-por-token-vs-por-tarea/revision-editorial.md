# Revisión editorial · pieza 003
2026-10-20 · Momento: pieza terminada · Revisor: agente independiente

## Veredicto

**Mejorar antes de seguir.**

La pieza es sólida en tono, diseño y honestidad general, pero falla una regla dura (una cifra no coincide con la fuente: Astra figura con "razonamiento alto" cuando la fuente dice "max") y tiene un problema de fondo en la idea: la portada promete "caro por tarea" y los propios datos de la lámina 04 muestran que Argon, con el precio de lanzamiento, es el más barato por tarea de los cinco. Lo que cambia el orden es solo la duplicación de la tarifa, no el mecanismo de la lámina 03. Son arreglos acotados, pero hay que volver a revisar. Como en todo veredicto, la decisión final es de una persona de Plogy; el CTA depende de un reporte y un DM que hoy son borradores sin configurar.

## Parte A · La oportunidad

| Criterio | Nota | Evidencia | Qué cambiaría |
| --- | --- | --- | --- |
| Relevancia para la audiencia | 3 | Un dueño de negocio rara vez elige modelo por token; la utilidad real es el criterio de las tres cuentas (lám. 05 y 06), que vale para quien ya paga API o contrata a quien la integra. Es medio técnico. | Abrir con el costo que ve el negocio (factura mensual de un proceso), no con el nombre del modelo. |
| Encaje de marca | 4 | Costo, tiempo y riesgo al implementar IA en negocios; la noticia es un caso, la tesis es de Plogy y se rotula como criterio (lám. 05, reporte secc. 5). | Nada grave. |
| Evidencia | 4 | Leí AIHubMix y Vals AI. Precios, 62k y 27k tokens, tabla de costo por tarea e índices coinciden con AIHubMix; costos Vals de $15,68, $21,34, $32,14 y los de agentes ($193,78, $57,82, $44,90, $30,45) coinciden. Lo no verificado está declarado en el brief y el reporte. Falta fuente primaria (Artificial Analysis, anuncio de Google). | Contrastar Artificial Analysis antes de publicar. Con eso sube a 5. |
| Novedad | 3 | "Mira el costo por tarea, no por token" es un consejo conocido; lo nuevo es el caso concreto del cruce con Astra en diciembre. | Poner el cruce de diciembre como hallazgo central, no como adorno de la tesis conocida. |
| Urgencia | 3 | Fecha de cambio de precio (30 nov / 1 dic) da un reloj real, pero la fuente no la atribuye a Google y el brief lo reconoce. | Confirmar la fecha con Google o hablar siempre de "fecha reportada". |
| Potencial de conversación | 3 | La pregunta de LinkedIn ("¿cuántos tokens gasta una tarea típica de tu negocio?") la mayoría de la audiencia no sabe responderla; el CTA es palabra clave, no conversación. | Una pregunta que la audiencia sí pueda contestar (qué proceso están pagando por uso y cuánto les llega por factura). |
| Ángulo distintivo | 3 | Tres cuentas y fórmula tokens × precio × intentos: útil y propio, pero previsible; es el consejo estándar de FinOps para LLM. | Aportar un dato propio (aunque sea una medición pequeña real de Plogy) en vez de solo criterio sobre datos de terceros. |
| Repetición | 4 | 001 (orden antes de automatizar), 002 (permisos de agentes), 004 (modelo como dependencia) y 005 (medir línea base) son temas distintos. Cercanía conceptual con 005 ("medir antes") y la misma mecánica de CTA con 004 y 005. | Variar la forma del CTA frente a 004 y 005, que son casi la misma frase. |
| Relación comercial | 3 | Lleva a un reporte de Plogy, pero la primera entrega por DM es un enlace a AIHubMix, una plataforma que vende acceso a Argon (interés comercial declarado en el brief). Conexión con la oferta de Plogy: indirecta. | Que el DM entregue primero el reporte propio y deje AIHubMix como fuente citada, no como primer paso. |

## Parte B · La pieza

| Criterio | Nota | Evidencia | Qué cambiaría |
| --- | --- | --- | --- |
| Tono Plogy | 4 | Frases cortas y directas ("Mide la tarea. No el token.", lám. 07), sin humo, con cifras y fuente en cada lámina. LinkedIn es seco y denso pero preciso. | Pulir el LinkedIn, que arranca con la tesis pero acumula cuatro cifras en un solo párrafo. |
| Una idea por lámina y progresión | 3 | Hay avance (tensión, precio, mecanismo, cifra, criterio, ejemplo, CTA), pero hay un salto lógico entre 03 y 04: la lámina 03 dice que Argon gasta 2,3 veces más tokens que Astra, y la 04 muestra que, con el precio de lanzamiento, aun así es más barato ($1,99 contra $3,26). El lector se queda sin la pieza que falta: el precio por token de Astra es unos cinco veces mayor ($10 y $50 por millón según el reporte). El titular de portada "Caro por tarea" tampoco se sostiene en los datos: incluso a $3,98 Argon sigue por debajo de Sonnet y Opus. | Reformular la tesis a lo que sí muestran los datos ("el precio por token no te dice el costo de la tarea: cuenta los tokens que se gastan") y añadir en 03 o 04 la tarifa de Astra para que el cruce se entienda. |
| Valor para la audiencia | 4 | Lám. 05 da tres pasos accionables y lám. 06 muestra la cuenta (10.000 × $1,99 = $19.900; 10.000 × $3,98 = $39.800, correcta). Se podría usar mañana. | La cuenta de la lám. 06 usa el costo por tarea de otro; el lector no ve cómo calcular el suyo. Un mini ejemplo con sus propios tokens (entrada + salida) lo cerraría. |
| Honestidad de la evidencia | 3 | Buen rótulo "Ejemplo hipotético", fuente en cada lámina, nota del índice de inteligencia (53, 53, 56, 58) y lo no verificado en el reporte. Pero: (1) la lám. 02 afirma como hecho "se duplica el 1 de diciembre" y "hasta el 30 de nov." mientras el brief admite que la fecha no está confirmada por Google; el DM sí lo deja condicional ("se duplicaría") y las láminas no; (2) la lám. 04 y los textos dicen "razonamiento alto" para todos los modelos, pero AIHubMix rotula a GPT-6 Astra como "max". | Poner en 02 "según lo reportado" en el titular o una nota visible; corregir el rótulo de razonamiento en 04, caption, LinkedIn y reporte. |
| CTA | 3 | Una sola acción y clara ("Comenta COSTO…", lám. 07). Pero el recurso es un borrador, el DM no está configurado ni probado, la URL del reporte no existe y el mensaje 1 promete "la noticia completa" como valor aunque es una nota de un tercero con interés comercial. La promesa "nuestro análisis" sí nace del valor entregado. | Dejar el CTA como "Comenta COSTO y te mandamos el reporte con las tres cuentas" y no ofrecer la noticia ajena como parte principal. Activar solo con el flujo probado. |
| Diseño y legibilidad | 4 | Jerarquía clara, texto y logo siempre por delante; barras de la lám. 04 proporcionales (190, 310, 380, 525, 578 px para 1,99 a 5,98); número 62.000 con brillo naranja bien resuelto; tarjeta de vidrio sobre foto en 07. Detalles: en 05 la foto con cajas de seguimiento sugiere vigilancia y no se relaciona con "medir tokens"; en 07 la foto del hombre con casco y los pies sobre el escritorio no refuerza el mensaje, solo decora; textos de fuente y notas de 30 px a tamaño móvil quedan justos. | Verificar en móvil real; considerar imagen propia o sin imagen en 05; derechos de las dos fotos siguen sin resolver. |
| Coherencia entre canales | 4 | Caption, LinkedIn, DM y reporte sostienen la misma tesis y cada canal cambia de enfoque (caption: regla simple y CTA; LinkedIn: fuentes, comparación con índice y pregunta; DM: noticia y reporte). El DM es condicional en la fecha y las láminas no. El "Siguiente paso" del reporte ("Sigue a Plogy") difiere del CTA de COSTO. | Alinear la certeza de la fecha en todos los canales. |
| Originalidad frente a lo que ya existe | 3 | Reconocible como Plogy por el sistema visual y el tono; el contenido (costo por token contra por tarea) es un tema ya cubierto por muchos posts de IA y por la propia fuente (el título de AIHubMix es casi el de la portada). | Tomar una posición propia que la fuente no tenga (por ejemplo, el cruce con Astra explicado por el precio y no por los tokens). |

## Parte C · Reglas duras

| Regla | Cumple / Falla | Evidencia |
| --- | --- | --- |
| 1. Sin guiones largos | Cumple | Búsqueda de — y – en brief, textos, reporte, DM y carrusel: sin resultados. Láminas sin ninguno. |
| 2. Sin muletillas de IA | Cumple | Búsqueda de la lista de la rúbrica: sin coincidencias. |
| 3. Sin emojis en LinkedIn | Cumple | No hay emojis en el post (lectura y búsqueda). |
| 4. Hasta cinco hashtags | Cumple | Tres: #CostoDeIA, #IAParaNegocios, #AutomatizacionConIA, con razón explicada. |
| 5. No inventa datos; hipótesis rotuladas | Cumple | Lám. 06 rotulada "Ejemplo hipotético" con volumen inventado declarado; criterio rotulado como de Plogy. Reserva: la lám. 02 presenta la fecha como firme (ver Parte B, honestidad). |
| 6. Una idea por lámina y CTA en la última | Cumple | 7 láminas con una idea dominante cada una; CTA único en la 07. La 04 mezcla gráfico y nota de índice, pero es una sola idea. |
| 7. Texto y logo por delante de las imágenes | Cumple | Logo y texto sobre foto en 05 y 07, nada tapado; en 07 hay degradado de protección. |
| 8. CTA de recurso con recurso y entrega preparados | Cumple | `reporte.md` y `dm.md` existen y lo que promete el mensaje 2 (números con fuente, tres cuentas, lo no sabido) está en el reporte (secc. 1, 4 y 2). Siguen en borrador, la URL y el enlace de la noticia son marcadores. |
| 9. No dice que algo está publicado, aprobado o configurado | Cumple | El brief y los textos marcan BORRADOR, DM sin configurar y aprobación humana PENDIENTE. |
| 10. Cifras coinciden con brief y fuente | **Falla** | Todas las cifras de dólares, tokens e índices coinciden con AIHubMix y Vals AI, salvo el rótulo "razonamiento alto" aplicado a todos los modelos (lám. 04, caption, LinkedIn, reporte): AIHubMix pone a GPT-6 Astra en "max". Además, el reporte dice "primero entre 50 modelos" en Vals Index, y lo que yo leí en la página es "#1 de 41" en la sección de actualización y "3 de 22" en el bloque principal (69,24 %, $13,37), que el reporte no menciona. |

## Lo que verifiqué y lo que no

Verifiqué (leyendo las fuentes con WebFetch el 2026-10-20):
- AIHubMix (13 oct 2026): precios de lanzamiento y estándar, caché $0,10 y $0,20, fin del precio el 30 de noviembre sin atribuirlo a Google, 62k y 27k tokens de salida, tabla de costo por tarea e índices, y el sexto modelo (Gemini 3.1 Pro Preview, $1,30, índice 30) que el brief explica haber excluido.
- Vals AI: fecha de lanzamiento (30 sep 2026), 68,90 % y $15,68, Sonnet 5.5 (67,04 % y $21,34), Opus 5.5 (66,97 % y $32,14) y los cuatro costos de agentes.
- Las cuentas de la lámina 06 y las proporciones de las barras de la 04.
- Los siete PNG de `exports/` y los seis de `assets/reporte/` vistos como imagen. Las figuras del reporte son legibles, sus cifras coinciden con la tabla del reporte y la figura de precios sí lleva la salvedad "la fecha de fin del precio de lanzamiento es reportada, no confirmada por Google", que la lámina 02 del carrusel no lleva. La figura de costo por tarea ("El orden cambia solo por el precio") expresa mejor la tesis que la portada. La barra de GPT-6 Astra (27.000) está rotulada como cálculo de Plogy, y coincide con el dato de AIHubMix. Reglas de estilo con búsqueda de texto; `reporte.md` leído completo.

No verifiqué:
- Los números de Artificial Analysis en su propio sitio (solo vistos a través de AIHubMix) ni el anuncio original de Google.
- Qué modelo de razonamiento se usó para Sonnet 5.5 y Opus 5.5.
- Derechos de las dos fotos y licencias de Screener y Space Grotesk.
- La legibilidad en un móvil real.
- La discrepancia de Vals (rank y número de modelos): puede ser un error de mi lectura de la página; conviene que quien decide la mire.
- Que la afirmación "Google lo anunció el 30 de septiembre" (LinkedIn) tenga respaldo primario; las fuentes leídas hablan de lanzamiento, no del anuncio.

## Tres cosas que más subirían la pieza

1. Arreglar la tesis y el paso de la lámina 03 a la 04: quitar o matizar "Caro por tarea", mostrar el precio por token de Astra y decir claramente que el cruce de diciembre lo causa la tarifa, no los tokens. Es lo que más cambia la fuerza de la idea.
2. Corregir las dos cifras que no coinciden con la fuente (razonamiento de Astra y puesto en Vals) y hacer que la lámina 02 diga "según lo reportado" como ya hace el DM.
3. Cambiar la entrega del CTA: reporte propio primero, enlace a AIHubMix como fuente y no como regalo; tener el reporte publicado y el flujo de DM probado antes de salir. Aprovechar para sustituir las fotos 05 y 07 por material con derechos resueltos.

## Preguntas para la persona que decide

1. ¿Prefieres sostener "caro por tarea" (más provocador, pero con la salvedad de que solo se cumple frente a Astra en diciembre) o la versión más precisa "el costo de una tarea no se lee en la tarifa"?
2. ¿La fecha del 1 de diciembre se publica como hecho (confirmada con Google) o como "reportada" en todas las láminas?
3. ¿Quieres que el DM entregue una noticia de un proveedor con interés comercial, o solo el reporte de Plogy?
4. ¿Hay material propio o licenciado para sustituir las fotos 05 y 07, o se publica con una versión sin foto en 05?
5. ¿Alguien de Plogy puede aportar una medición real de tokens por tarea (aunque sea pequeña) para que la pieza deje de depender solo de datos de terceros?
