# Revisión editorial · pieza 004
2026-10-20 · Momento: pieza terminada (borrador completo: 7 láminas, caption, LinkedIn, DM y reporte con figuras) · Revisor: agente independiente (segunda revisión, sin haber leído `revision-editorial.md`)

## Veredicto

**Mejorar antes de seguir.**

La pieza es veraz y está bien armada: todas las cifras, fechas e identificadores coinciden con OpenAI y no hay fallas duras de estilo. Pero el CTA (nota 3) pide una acción cuyo recurso no existe todavía (reporte sin publicar, DM sin configurar, palabra clave sin registrar), y el tono y la originalidad quedan en "correcto pero intercambiable" (3). Según la rúbrica, un 3 en CTA impide "Publicar con ajustes". Si el recurso se publica y se prueba el flujo, el CTA sube y la pieza queda a pocos ajustes de revisión humana.

## Parte A · La oportunidad

| Criterio | Nota | Evidencia | Qué cambiaría |
| --- | --- | --- | --- |
| Relevancia para la audiencia | 4 | Una automatización que llama a un modelo por su nombre deja de funcionar el 14 ene 2027 (lámina 1, 2). Cambia una decisión de trabajo hoy. Se queda en 4 porque muchos dueños de negocio no saben qué modelo usan por dentro; le sirve más a quien tiene un desarrollador o un proveedor. | Una línea temprana que diga a quién aplica ("si alguien te armó una automatización con GPT-4o"). |
| Encaje de marca | 4 | Territorio exacto: IA que se implementa bien en negocios, lo que se rompe en silencio (brief, tesis "un modelo es una dependencia"). | Nada de fondo. |
| Evidencia | 5 | Fuente primaria leída y contrastada por mí (ver sección de verificación). Lo no verificado (alias, alcance del 6 de enero, por qué 92 días) está declarado en el reporte. | Nada. |
| Novedad | 3 | La noticia está cubierta por varios medios (Mixed, Digital Applied, FourWeekMBA). "El modelo es una dependencia con fecha" es sabido en ingeniería; la novedad para la audiencia de negocios es el plazo corto y que el reemplazo cambia el comportamiento (láminas 3 y 4). | Poner al frente lo menos repetido: las restricciones del reemplazo y el costo por tarea, no la fecha. |
| Urgencia | 5 | Fecha dura y verificable (14 ene 2027), aviso del 14 oct 2026. | Nada. |
| Potencial de conversación | 3 | LinkedIn cierra con una pregunta útil, pero la experiencia ajena es técnica y específica; el comentario previsible es "gracias" o "MIGRAR". | Preguntar algo que cualquiera pueda contar: "¿quién te armó tus automatizaciones y sabe qué modelo usan?". |
| Ángulo distintivo | 3 | Tesis propia y clara, pero previsible (inventario, pruebas, vuelta atrás). No sale de experiencia migrando: el propio texto admite "no hemos migrado ningún flujo". | Si hay algún caso propio de dependencia rota (incluso pequeño), usarlo. Si no, aprovechar la honestidad: "esto es lo que haríamos y no hemos probado" como rasgo de voz. |
| Repetición | 4 | Frente a 001, 002, 003 y 005 el tema es distinto. Rozan 003 (precio por token vs por tarea) en la lámina 5, y la foto de la lámina 7 es la misma de la variante D de la 001. | Cambiar la foto del CTA o justificar el reuso. |
| Relación comercial | 4 | La lista de revisión lleva de forma natural a una conversación sobre inventario y migración. | Nada. |

## Parte B · La pieza

| Criterio | Nota | Evidencia | Qué cambiaría |
| --- | --- | --- | --- |
| Tono Plogy | 3 | Preciso y sin humo ("El aviso fue corto", "Primero el inventario. Después la migración."), pero las láminas 2 a 5 suenan a resumen de changelog. La voz propia aparece solo en las láminas 6 y 7. | Un titular con más postura en 2 o 4 (por ejemplo, decir qué se rompe, no qué cambió). |
| Una idea por lámina y progresión | 4 | Secuencia clara: qué se apaga (2), cuánto tiempo (3), qué cambia (4), cuánto cuesta (5), qué hacer (6), cierre (7). La lámina 5 junta tres ideas: el 25×, el 1,5× frente a mini y "mide el costo por tarea". | En la 5, dejar solo el contraste de precio y mover el aviso de razonamiento a un renglón o a la 4. |
| Valor para la audiencia | 4 | Se lleva un criterio aplicable (los tres pasos de la lámina 6) y un dato accionable (`reasoning_effort: none`, Responses API). Los tres pasos son estándar; el valor extra está en el reporte. | Que la lámina 6 incluya algo menos genérico, por ejemplo preguntarle al proveedor qué modelo usa. |
| Honestidad de la evidencia | 4 | Lámina 3 declara que su página no aclara si estos modelos son de disponibilidad general (verificado). "Hasta 25 veces" acotado a GPT-4o en la propia lámina 5. Ejemplos hipotéticos rotulados. Descuentos: lámina 1 dice "OpenAI retira GPT-4o y GPT-4.1" cuando la página lista cinco versiones fechadas y no dice qué pasa con los alias (el reporte sí lo reconoce, la lámina no); y la lámina 6 se llama "Criterio de Plogy" sin decir en la lámina que no se ha aplicado a una migración real (LinkedIn y reporte sí lo dicen). | En la lámina 1 o 2, "versiones" en vez del nombre genérico; en la 6 un renglón "Aún no lo hemos aplicado a Luna". |
| CTA | 3 | Una sola acción ("Comenta MIGRAR"), clara y que nace del valor (la lista de la lámina 6 tiene tres pasos; el reporte tiene seis comprobaciones). Pero el recurso no está listo: reporte sin publicar y sin URL, DM sin herramienta ni prueba, palabra sin registrar (checklist del brief, casillas abiertas). Además "la noticia completa" es un enlace a una página de OpenAI que el lector ya puede buscar; lo que realmente se entrega es la lista. | Publicar el reporte y probar el flujo. Reducir el CTA a "te mandamos la lista de revisión" y dar la noticia en el mismo mensaje. |
| Diseño y legibilidad | 4 | Jerarquía nítida, textos de 34 a 40 px legibles, logo y texto por delante en todas las láminas; contraste correcto del orange sobre Ink. Pulir: la lámina 3 deja un tercio inferior vacío; la foto rosa de la 7 choca con la paleta Ink y naranja y es la de la 001; la foto de la 1 está bien pero el "ojo" es poco legible como metáfora. | Rellenar o reequilibrar la 3; foto de la 7 con tratamiento de marca o distinta. |
| Coherencia entre canales | 4 | La tesis se sostiene en caption, LinkedIn, DM y reporte; los cinco hechos y el CTA coinciden. LinkedIn aporta tesis, ejemplo hipotético y pregunta; Instagram es hecho y acción. El caption de Instagram repite buena parte de las láminas 1 a 5. | Que el caption aporte contexto que las láminas no tienen (el ejemplo de proveedor, por qué importa el alias). |
| Originalidad frente a lo que ya existe | 3 | Bien hecho y fiable, pero el formato "qué se apaga, cuándo, qué cambia, qué hacer" lo publicaría cualquier consultora de IA. Se reconoce como Plogy por el diseño y por la honestidad del "no hemos migrado", no por el contenido. | Ver ángulo distintivo. |

## Parte C · Reglas duras

| Regla | Cumple / Falla | Evidencia |
| --- | --- | --- |
| 1. Sin guiones largos | Cumple | Búsqueda de — y – en `carrusel.html`, `textos.md`, `dm.md`, `reporte.md` y `brief.md`: sin coincidencias. |
| 2. Sin muletillas de IA | Cumple | Búsqueda de las siete frases prohibidas: sin coincidencias. |
| 3. Sin emojis en LinkedIn | Cumple | Texto de LinkedIn en `textos.md` sin emojis. |
| 4. Hasta cinco hashtags | Cumple | Tres: #AutomatizacionConIA #IAParaNegocios #OpenAI. |
| 5. No inventa datos | Cumple | Cifras y cuentas verificadas por mí. Único caso inventado (la pyme de atención al cliente) está rotulado "hipotético" en reporte y LinkedIn. |
| 6. Una idea dominante por lámina y CTA en la última | Cumple | CTA solo en la lámina 7. La lámina 5 es la más cargada pero tiene una idea dominante (el precio). |
| 7. Texto y logo por delante de las imágenes | Cumple | Láminas 1 y 7 con logo y texto sobre foto o panel, legibles; 2 a 6 sin imagen. |
| 8. Recurso del DM preparado en borrador | Cumple (con reserva) | `dm.md` y `reporte.md` existen y contienen lo que prometen el mensaje 2 (calendario, qué cambia, lo no confirmado, lista de seis comprobaciones). Reserva: el reporte no está publicado ni tiene URL, y el mensaje 1 lo promete como entrega inmediata. |
| 9. No afirma publicado/aprobado/configurado | Cumple | `brief.md`, `textos.md`, `dm.md` y `reporte.md` marcan borrador y aprobación humana pendiente. |
| 10. Cifras coinciden con brief y fuente | Cumple | 92 días, 25×, 1,5×, $0,10 / $2,50, y la tabla del reporte (25, 20, 4, 3,2, 1,5, 1,2, 20, 16) coinciden con las fichas y con el brief. Nota menor: el reporte dice "Fecha de la versión" y "Última actualización" 2026-10-19, pero su historial anota cambios del 2026-10-20. |

## Lo que verifiqué y lo que no

Verificado hoy (2026-10-20) con WebFetch en OpenAI:

- Página de deprecaciones, entrada del 14 oct 2026: cinco identificadores (`gpt-4o-2024-08-06`, `gpt-4o-2024-11-20`, `gpt-4o-mini-2024-07-18`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`), apagado el 14 ene 2027, reemplazo `gpt-6-luna`, fine-tunes con el calendario de su base. La entrada no menciona la política de seis meses ni el 6 de enero; esos datos están en otras secciones de la misma página (mínimo "At least 6 months" para modelos de disponibilidad general; el 6 de enero aplica al ajuste fino de autoservicio para clientes activos). Esto confirma la formulación cautelosa de la lámina 3 y del reporte.
- Ficha de `gpt-6-luna`: $0,10 entrada, $0,01 caché, $0,50 salida; contexto 1.050.000; salida máxima 128.000; conocimiento 18 may 2026; sin fine-tuning; llamadas a funciones por Responses API y en Chat Completions solo con `reasoning_effort: none`; razonamiento medio por defecto; precios 2× entrada y 1,5× salida por encima de 272.000 tokens (el reporte lo resume como "los precios cambian").
- Fichas de GPT-4o ($2,50 / $10, 128.000, 16.384, oct 2023; sin aviso de retiro visible en la ficha), GPT-4o mini ($0,15 / $0,60), GPT-4.1 ($2 / $8) y GPT-4.1 mini ($0,40 / $1,60). Todas las cuentas del reporte y de la lámina 5 son correctas.
- Guía de razonamiento: el razonamiento se factura como tokens de salida y Luna usa esfuerzo medio por defecto. La guía no trata la restricción de llamadas a funciones de Luna (solo habla de otros modelos GPT-6); esa restricción descansa en la ficha del modelo, como la pieza la cita.
- Los 92 días: 17 + 30 + 31 + 14 = 92. Correcto.
- Terceros: Digital Applied (6 de enero como cierre real de fine-tunes, alias sin respuesta de OpenAI, campo `shutdown_date`, 50 prompts, calendario de otros retiros, vende migraciones) y Mixed (92 días por debajo del piso de seis meses, sin oferta comercial más allá de afiliados de tienda). La pieza los cita y rotula correctamente.

No verifiqué ni pude verificar: qué ocurre con los alias tras el apagado, si el cierre del 6 de enero afecta a estos modelos, por qué el plazo es de 92 días, FourWeekMBA y daily.dev (no leídas), cómo se comporta Luna en una automatización real, ni la legibilidad en un móvil real, los derechos de las fotos y las licencias tipográficas (Screener demo; Space Grotesk, por confirmar).

## Tres cosas que más subirían la pieza

1. Cerrar el recurso: publicar el reporte en su URL, registrar MIGRAR con vigencia y probar el DM con una cuenta de prueba. Con eso el CTA pasa de 3 a 4 o 5, y es lo único que bloquea el veredicto "Publicar con ajustes". De paso, simplificar la promesa a la lista de revisión.
2. Subirle la voz a las láminas 2 a 5, que hoy son resumen de documentación. Un titular que diga qué se rompe en el negocio, y quitar a la lámina 5 su tercera idea. Y un renglón en la lámina 6 que diga que el criterio aún no se ha aplicado a Luna, para igualar la honestidad de LinkedIn y el reporte.
3. Cambiar la foto de la lámina 7 (reuso de la 001, rosa fuera de paleta) y reequilibrar la lámina 3 (tercio inferior vacío).

## Preguntas para la persona que decide

- ¿Quién publica el reporte y cuándo, y se acepta que el carrusel no salga hasta que el DM esté probado? Hoy el brief lo dice, pero conviene fijar una fecha antes del 14 de enero para que el contenido no pierda sentido.
- ¿Plogy reconoce como propio el criterio de las láminas 6 y 7 (inventario, pruebas, vuelta atrás)? El brief lo deja pendiente de confirmar.
- ¿Se prefiere mantener "la noticia completa" en el CTA o quedarse solo con la lista de revisión, que es lo único que no se encuentra en otro lado?
- ¿Se acepta el reuso de la foto de la 001, o se pide una distinta (o propia, por derechos)?
