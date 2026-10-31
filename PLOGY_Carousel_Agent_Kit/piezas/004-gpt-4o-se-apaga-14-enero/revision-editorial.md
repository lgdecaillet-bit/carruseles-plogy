# Revisión editorial · pieza 004
2026-10-20 · Momento: pieza terminada · Revisor: agente independiente

## Veredicto

**Mejorar antes de seguir.**

La pieza es sólida en idea, orden y honestidad general, y todas las reglas duras se cumplen. Pero no llega a "Publicar con ajustes" porque la rúbrica no admite ningún 3 en evidencia ni en CTA, y aquí hay dos. La honestidad de la evidencia es 3: el titular de la lámina 5 ("25 veces menos") solo vale frente a GPT-4o, y tres de los cinco identificadores que se apagan son modelos mini o GPT-4.1, donde la diferencia es mucho menor. Además una figura del reporte dice que el 6 de enero "no aparece en la página de OpenAI", y sí aparece. El CTA es 3 porque el recurso prometido sigue en borrador (reporte sin URL, DM sin configurar, palabra clave sin registrar). Los arreglos son acotados y la pieza puede volver a revisión pronto.

Todo veredicto termina en revisión humana. Este informe no autoriza ninguna publicación.

## Parte A · La oportunidad

| Criterio | Nota | Evidencia | Qué cambiaría |
| --- | --- | --- | --- |
| Relevancia para la audiencia | 4 | Una automatización que llama a un modelo por nombre se rompe el 14 de enero de 2027 (comprobado en OpenAI). Afecta a quien tiene flujos hechos por un tercero o por una herramienta sin código. | Para un dueño de negocio que no sabe qué modelo usa su herramienta, la lámina 6 dice "busca el nombre" pero no explica dónde mirar sin ser técnico. |
| Encaje de marca | 4 | "Un modelo es una dependencia con fecha" es una tesis de quien implementa. Pero LinkedIn dice "no hemos migrado ningún flujo a este modelo": es honesto, y deja la autoridad en el criterio y no en la práctica. | Si existe algún caso propio de cambio de modelo en un cliente (aunque sea otro modelo), usarlo reforzaría el encaje. Si no, mantener la honestidad. |
| Evidencia | 4 | Leí la entrada del 14 de octubre de 2026, la ficha de gpt-6-luna y las fichas de GPT-4o, GPT-4o mini, GPT-4.1 y GPT-4.1 mini en OpenAI. Coinciden con la pieza (ver "Lo que verifiqué"). Vacíos: la pieza marca como no verificado material que sí se puede verificar en OpenAI. | Actualizar la sección de "sin confirmar" del reporte con lo que ya está en fuente primaria. |
| Novedad | 3 | El apagado lo cubren al menos cinco medios (Mixed, Digital Applied, FourWeekMBA, daily.dev y la propia página). Lo que aporta la pieza es leer la ficha de Luna: razonamiento por defecto, llamadas a funciones solo con `reasoning_effort: none` en Chat Completions, sin fine-tuning. | Dar más peso a eso desde la portada o la lámina 2 (el reemplazo no es un cambio de nombre), que es lo menos visto. |
| Urgencia | 4 | Fecha fija (14 de enero de 2027) y riesgo de fallo silencioso. Quedan unos tres meses desde hoy, así que no es de esta semana. | Nada. |
| Potencial de conversación | 3 | El CTA es de palabra clave y LinkedIn cierra con una pregunta ("¿Sabes en cuántos lugares aparece...?"). Pocos dueños de negocio tendrán una experiencia propia que contar sobre esto. | La pregunta de LinkedIn es buena. En Instagram se puede añadir en el caption una pregunta concreta para quien ya migró (¿qué se rompió primero?). |
| Ángulo distintivo | 4 | La tesis de la dependencia con fecha es clara y se sostiene en las 7 láminas. Es una idea conocida entre ingenieros, poco dicha a negocios. | Nada. |
| Repetición | 4 | Distinta de 001, 002, 005. Comparte terreno con 003 (precio por token frente a costo por tarea): la lámina 5 y la sección "mide la tarea" repiten ese mensaje. La imagen de la lámina 7 es la misma de 001 (variante D). | Remitir a 003 en una línea en vez de repetir el argumento, y usar otra imagen en la lámina 7. |
| Relación comercial | 4 | Un inventario y una migración probada son una conversación natural con Plogy. La lista de revisión es un recurso útil que lleva a "¿quién lo hace por mí?". | El reporte cierra con "Sigue a Plogy..." (sección 7), un segundo CTA genérico. Mejor un siguiente paso concreto (por ejemplo, ofrecer el inventario). |

## Parte B · La pieza

| Criterio | Nota | Evidencia | Qué cambiaría |
| --- | --- | --- | --- |
| Tono Plogy | 4 | Directo y sin humo: "El aviso fue corto.", "El reemplazo no es un cambio de nombre.", "Primero el inventario. Después la migración." Algo de jerga técnica para negocios ("una rama", "ficha por uso", "tool calls"). | Cambiar "rama" (lámina 6) por algo que entienda un dueño: "una copia de la configuración actual". |
| Una idea por lámina y progresión | 4 | Orden claro: tensión (01), qué se apaga (02), plazo (03), qué cambia (04), precio (05), qué hacer (06), cierre (07). La lámina 5 mezcla tres ideas (25×, 20×, el razonamiento se factura como salida) y repite "25" en titular y en cifra gigante. | Dejar en la 5 solo la comparación de tarifa, y llevar "el razonamiento se factura como salida" a la 4 o a la 6. |
| Valor para la audiencia | 4 | Se lleva un criterio aplicable mañana: buscar el nombre del modelo, probar con casos reales, dejar vuelta atrás; y un dato accionable: llamadas a funciones solo con `reasoning_effort: none`. Los tres pasos de la lámina 6 son genéricos de ingeniería de software; lo específico está en la lámina 4 y en el reporte. | Que la 6 mencione lo específico de Luna (revisar si usas llamadas a funciones o un fine-tune) y no solo pasos válidos para cualquier migración. |
| Honestidad de la evidencia | 3 | Casi todo lleva fuente y los terceros están rotulados, lo cual es bueno. Fallos concretos: (a) Lámina 5: "Luna cuesta 25 veces menos por token de entrada" compara solo con GPT-4o. En fichas de OpenAI: GPT-4o mini $0,15/$0,60 (Luna sería 1,5 y 1,2 veces menos), GPT-4.1 mini $0,40/$1,60 (4 y 3,2 veces), GPT-4.1 $2/$8 (20 y 16 veces). Tres de los cinco identificadores no son GPT-4o. (b) `fig-calendario.png`: dice "No aparece en la página de OpenAI que leímos" sobre el 6 de enero, y la página de OpenAI sí lo trae (ver abajo). (c) Lámina 3: "El aviso fue corto" sostiene que hay una política de seis meses atribuida a Mixed; la propia página de OpenAI la declara para modelos de disponibilidad general y no dice si estos lo son. | (a) Titular: "Luna cuesta hasta 25 veces menos por token", con el rango por modelo en el reporte. (b) Corregir la nota de la figura y del reporte. (c) Citar la política a OpenAI y decir que la página no aclara si estos modelos son de disponibilidad general. |
| CTA | 3 | Una sola acción, nace del valor y la última lámina la lleva ("Comenta MIGRAR y te mandamos la noticia completa y nuestra lista de revisión"). El recurso es un borrador: reporte sin URL, `dm.md` sin aprobar ni probar, palabra clave sin registrar. "La noticia completa" en el DM es un enlace a OpenAI más un resumen de una línea. | Publicar y revisar el reporte, configurar y probar el DM. Cambiar "la noticia completa" por "el enlace a la noticia y nuestra lista de revisión". |
| Diseño y legibilidad | 4 | Texto y logo por delante, jerarquía nítida, números grandes con el naranja, tamaños legibles (apoyo 34 a 40 px). La lámina 7 usa una foto con fondo rosa que choca con el negro y el naranja de las otras seis, y no se relaciona con un modelo que se apaga. En `fig-calendario.png` el texto "6 ene 2027 · sin confirmar" queda lejos de su nodo discontinuo, sin línea que los una. `fig-llamadas.png` deja el pie muy pegado a la última tarjeta y tiene dos flechas "Sí" sin jerarquía clara. | Imagen propia o licenciada en la 7; unir el texto del 6 de enero con su nodo; dar aire al pie de `fig-llamadas`. |
| Coherencia entre canales | 4 | Misma tesis en láminas, caption, LinkedIn, DM y reporte; cada canal aporta lo suyo (LinkedIn con tres pasos y un ejemplo hipotético rotulado; el reporte con el detalle). Detalle: la tabla UTM de `dm.md` prevé un UTM de LinkedIn y el post no lleva enlace. | Quitar esa fila hasta que exista el enlace o añadirlo al post. |
| Originalidad frente a lo que ya existe | 3 | Un explicador de deprecación con lista de verificación es un género reconocible. La portada (monitor viejo con un ojo naranja) tiene intención; la lámina 7 reutiliza la imagen de 001 y no aporta una voz propia. | Más de la voz de Plogy en la 6 (qué se rompe primero en un negocio real, aunque sea una hipótesis rotulada) y una imagen nueva en la 7. |

## Parte C · Reglas duras

| Regla | Cumple / Falla | Evidencia |
| --- | --- | --- |
| 1. Sin guiones largos | Cumple | Busqué — y – en `brief.md`, `textos.md`, `dm.md`, `reporte.md`, `carrusel.html` y `reporte-figuras.html`: ninguno. Tampoco aparecen en los PNG. |
| 2. Sin muletillas de IA | Cumple | Busqué las siete frases de la lista en los mismos archivos: ninguna. |
| 3. Sin emojis en LinkedIn | Cumple | El texto de LinkedIn en `textos.md` no tiene. |
| 4. Hasta cinco hashtags | Cumple | Tres: #AutomatizacionConIA, #IAParaNegocios, #OpenAI, con razón declarada. |
| 5. No inventa datos | Cumple | El único caso inventado (pyme de atención al cliente) está rotulado como hipotético en el reporte y en LinkedIn. Ninguna lámina lo presenta como real. |
| 6. Una idea por lámina y CTA en la última | Cumple con reserva | CTA solo en la lámina 7. La lámina 5 es la más cargada (ver Parte B). |
| 7. Texto y logo por delante | Cumple | En las láminas 1 y 7 el texto va sobre degradado o panel Ink, sin tapar. |
| 8. CTA de recurso con recurso y entrega preparados | Cumple | `reporte.md` y `dm.md` existen y lo que promete el DM (calendario, qué cambia, lo no confirmado, seis comprobaciones) está en el reporte. Siguen en borrador, y así consta. |
| 9. No dice que algo está publicado, aprobado o configurado | Cumple | El brief marca como pendientes la publicación del reporte, el DM, la palabra clave y la aprobación humana. |
| 10. Cifras coinciden con brief y fuente | Cumple con reserva | 92 días (14 oct a 14 ene: 17 + 30 + 31 + 14), 25× (2,50 ÷ 0,10) y 20× (10 ÷ 0,50) son correctas y coinciden en todas las piezas. La reserva es el alcance del 25× (ver honestidad). |

## Lo que verifiqué y lo que no

**Verificado contra OpenAI (hoy, 2026-10-20):**

- Entrada "2026-10-14: GPT-4 series model deprecations" en `developers.openai.com/api/docs/deprecations`: notificación del 14 de octubre de 2026; cinco identificadores exactos (`gpt-4o-2024-08-06`, `gpt-4o-2024-11-20`, `gpt-4o-mini-2024-07-18`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`); retiro de la API el 14 de enero de 2027; reemplazo recomendado `gpt-6-luna`; los fine-tunes siguen el calendario de su base.
- Ficha de `gpt-6-luna`: $0,10 entrada, $0,01 caché, $0,50 salida; contexto de 1.050.000; salida máxima de 128.000; conocimiento hasta el 18 de mayo de 2026; llamadas a funciones en Chat Completions solo con `reasoning_effort` en `none`, y en la Responses API a cualquier nivel; sin fine-tuning; razonamiento por defecto `medium`.
- Ficha de GPT-4o: $2,50 entrada, $10 salida, contexto de 128.000, salida máxima de 16.384, corte del 1 de octubre de 2023. Esto confirma datos que el brief y las figuras rotulan como "de terceros, no verificados".
- Política general de la misma página: "At least 6 months" para modelos de disponibilidad general (3 meses para variantes especializadas). La página no dice si estos modelos son de disponibilidad general. Es lo que el brief atribuye solo a Mixed.
- El 6 de enero de 2027 aparece en la página de OpenAI, en la sección de fine-tuning de autoservicio: desde esa fecha los clientes activos ya no pueden crear nuevos trabajos de fine-tuning, y la inferencia de modelos afinados se desactiva solo cuando se retira su modelo base. La sección no nombra modelos. Que ese cierre afecte a estos modelos es la lectura de Digital Applied.
- Alias: la página no dice qué pasa con alias sin fecha tras el apagado. La pieza hace bien en no afirmar nada.
- Fichas de GPT-4o mini ($0,15 / $0,60), GPT-4.1 mini ($0,40 / $1,60) y GPT-4.1 ($2 / $8), usadas para el comentario sobre la lámina 5.
- Aritmética de los 92 días, 25× y 20×.
- Todas las láminas (7) y las seis imágenes del reporte, vistas como PNG.

**No verificado:**

- Mixed y Digital Applied (no los leí; el brief dice que sí). No comprobé cómo citan la política ni las demás cifras.
- La ficha de GPT-4o no muestra aviso de retiro en la lectura de hoy. No sé si es un retraso de la página o una omisión; por eso es útil repetir la comprobación el día de publicar, como ya pide el brief.
- Derechos de las fotos (`unverified_reference_only`) y de las tipografías: sin resolver, y bloquean la publicación.
- Legibilidad en un móvil real y contraste medido: solo a ojo sobre los PNG.
- No revisé el código de `carrusel.html` más allá de buscar guiones y muletillas.
- Si el inventario, las pruebas y la vuelta atrás reflejan el método real de Plogy: es una decisión de quien aprueba.

## Tres cosas que más subirían la pieza

1. **Corregir lo que hoy afirma de más o de menos.** Titular de la lámina 5 ("hasta 25 veces", con el rango por modelo: GPT-4o mini apenas 1,5 veces), la nota de `fig-calendario.png` sobre el 6 de enero, y la atribución de la política de seis meses a la página de OpenAI. De paso, subir a "verificado en OpenAI" los datos de GPT-4o, que ahora se pueden citar de primera mano.
2. **Dejar el recurso realmente preparado.** Publicar el reporte en su URL, aprobar y probar `dm.md`, registrar la palabra clave y ajustar la frase "la noticia completa". Es lo que sube el CTA de 3 a 4 o 5.
3. **Una lámina 7 y una lámina 6 más propias.** Sustituir la foto rosa de 001 por una imagen con derechos claros y relación con el tema, y hacer que la lámina 6 diga lo específico de esta migración (llamadas a funciones, fine-tunes) y no solo pasos válidos para cualquier cambio de modelo.

## Preguntas para la persona que decide

1. ¿Plogy quiere publicar una pieza que dice abiertamente "no hemos migrado ningún flujo a este modelo"? Es honesto y diferencia, pero conviene decidirlo; con un caso propio, aunque sea menor, el encaje sería más fuerte.
2. ¿El titular de la lámina 5 debe mantener el 25× como gancho, aceptando matizarlo ("hasta") y añadir el rango en el reporte, o prefiere quitar la comparación de precio de las láminas y dejarla solo en el reporte (más cerca de 003)?
3. ¿Se acepta la lámina 3 ("El aviso fue corto") con la política de seis meses como referencia, sabiendo que OpenAI no aclara si estos modelos son de disponibilidad general? ¿O se suaviza el titular?
4. ¿Qué vigencia tendrá la palabra clave MIGRAR (hasta el 14 de enero de 2027 o 30 días)?
5. ¿Quién responderá las preguntas técnicas de migración que lleguen por fuera del flujo del DM?
6. ¿Se pueden usar las dos fotos de la biblioteca o hay que reemplazarlas antes de publicar?
