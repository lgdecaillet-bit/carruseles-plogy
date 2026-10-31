# Pieza 006 · Un modelo por tarea (Claude Haiku 5.5)

Estado: BORRADOR PARA REVISIÓN HUMANA. No publicar.

Tercera noticia que aplica el flujo con reporte y DM de `skills/plogy-cta-design/FLUJO-REPORTE-DM.md`: carrusel, reporte web con imágenes y mensajes de DM. Los textos por canal están en `textos.md` y los mensajes en `dm.md`. El reporte está en `reporte.md` con sus figuras.

## Oportunidad

- ID y estado editorial: 006 · borrador de carrusel, figuras, DM y textos; reporte escrito pero sin guardar como archivo, pendiente de revisión humana
- Tipo de origen: noticia
- Fuente primaria, fecha y enlace o registro interno (todas consultadas el 2026-10-20 con la herramienta de lectura web, que resume la página):
  - Anthropic, "Introducing Claude Haiku 5.5", 7 de octubre de 2026. https://www.anthropic.com/claude-haiku-5-5 (leída dos veces, la segunda para confirmar frases y cifras).
  - Anthropic, página de noticias. https://www.anthropic.com/news (confirma que el anuncio es del 7 de octubre y las fechas de Sonnet 5.5, 28 de septiembre, y Opus 5.5, 22 de septiembre).
  - Anthropic, documentación, "Models overview". https://platform.claude.com/docs/en/models/overview (tabla de modelos: precios, contexto, salida máxima, latencia, retiro).
  - Anthropic, documentación, "Claude Haiku 5.5". https://platform.claude.com/docs/en/models/haiku-5-5/overview y "What's new in Claude Haiku 5.5". https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5 (precios por tramo, tokenizador, cambios incompatibles).
  - Anthropic, documentación, "Choosing the right model". https://platform.claude.com/docs/en/about-claude/models/choosing-a-model y "Optimizing for cost and intelligence". https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence (probar con datos propios, esfuerzo como palanca, repetir pruebas en cada lanzamiento; de la segunda se leyó solo la primera mitad).
  - Anthropic, precios. https://claude.com/pricing (contraste de precios).
  - De terceros, vistos solo en resultados de búsqueda, no leídos completos y no usados para ningún dato: letsdatascience.com, gradually.ai, docs.apiyi.com y otros que repiten el lanzamiento; uno de ellos habla de una filtración previa. Ninguna cifra de la pieza viene de terceros.
- Qué afirma la fuente y qué queda sin verificar:
  - Verificado en Anthropic (fuente primaria): lanzamiento el 7 de octubre de 2026; identificador `claude-haiku-5-5`; precio de $0,10 de entrada y $0,50 de salida por millón de tokens para prompts de hasta 100.000 tokens ($0,50 y $2,50 por encima); contexto de 1 millón de tokens; salida máxima de 128.000; Batch con 50% de descuento; Sonnet 5.5 a $2 y $10, Opus 5.5 a $4 y $20; usos que propone Anthropic (resúmenes, compactación, consultas a bases de datos, clasificación, atención en vivo, uso de navegador, subagente; la documentación añade extracción y enrutamiento); "más adecuado para tareas de alcance acotado"; Sonnet 5.5 y Opus 5.5 "siguen siendo mejores" para código agéntico complejo; las dos cifras de pruebas usadas (Terminal-Bench 4.0: 39,2% contra 70,6%; OSWorld 2.1, subconjunto sin conexión: 72,4% contra 83,9%); el tokenizador nuevo cuenta aproximadamente 30% más tokens que en Haiku 4.5; los cambios incompatibles de la sección 7 del reporte. Las diferencias de 31,4 y 11,5 puntos son cuentas de Plogy (70,6 − 39,2 y 83,9 − 72,4).
  - Sin verificar: cómo se corrieron las pruebas (Anthropic remite a la tarjeta del sistema de Haiku 5.5, no leída); cualquier verificación independiente de las cifras; las cifras de pruebas solo se confirmaron en una página (el anuncio); la lectura web resume las páginas, por lo que conviene volver a comprobar precios y cifras en la página original el día de publicar.
  - Interés comercial: Anthropic fabrica y vende Haiku, Sonnet y Opus, y su guía para elegir modelo recomienda empezar por Haiku 5.5 y subir solo si hace falta. La pieza lo dice (lámina 03, lámina 04, figuras y reporte).
  - Criterio de Plogy, no hecho de la fuente: la matriz de cuatro tipos de tarea, la prueba de 20 casos, el umbral fijado antes, la regla de subir primero el esfuerzo, y el ejemplo de las tres tareas (hipotético, cifras inventadas). El 20 es una referencia práctica, no una regla estadística. No se ha aplicado a ningún cliente.
- Audiencia: Negocios
- Vertical: IA y automatizaciones
- Pilar principal: Conocimiento (vale por enseñar a asignar un modelo a cada tarea con una prueba)
- Pilar secundario: ninguno
- Subcategoría y confianza de clasificación: noticia explicada con criterio aplicable · confianza alta en el pilar y en los hechos de la parte Anthropic, media en que las cifras de pruebas sean representativas (son de Anthropic, sin verificación independiente)
- Tesis de Plogy en una frase: un negocio tiene muchas tareas distintas, y el modelo se asigna por tarea con una prueba de 20 casos reales, no se elige uno para todo.
- Problema o tensión que hace relevante la pieza: se usa el modelo más grande para todo por inercia, o el más barato por impulso, sin saber si cada tarea sale bien con él.
- Ángulo distintivo y por qué Plogy puede decirlo: Plogy implementa IA en negocios, donde cada tarea tiene su propio riesgo y tolerancia al error. Complementa la pieza 005 (medir antes de automatizar) y se distingue de la 003: esta no calcula el costo de una tarea, decide qué modelo asignarle según calidad probada. La matriz y la prueba son criterio de Plogy y así se rotulan. No hemos probado Haiku 5.5 ni aplicado la matriz a un cliente.
- Objetivo: recurso (reporte con matriz, prueba y plantilla, por DM)
- Término principal de búsqueda y términos secundarios reales: "Claude Haiku 5.5" y "qué modelo de IA usar para cada tarea". Secundarios: "modelo pequeño de IA", "Haiku vs Sonnet", "IA para negocios".
- CTA del último slide y estado del recurso prometido: "Comenta ELEGIR" con la lista "Matriz de tarea a modelo", "Plantilla de la prueba de 20 casos" y "La noticia, con su fuente" (variante 20 de la biblioteca, vidrio con lista, adaptada). El recurso (reporte con la matriz, la plantilla y la noticia) está redactado pero **no está guardado como archivo ni publicado**. El DM no está configurado. **El carrusel no se puede publicar hasta cumplir el checklist de salida.**

Por qué este tema: la noticia es del 7 de octubre, tiene precio, ficha y casos de uso verificables en la fuente primaria, y toca una decisión concreta de un negocio que automatiza (qué modelo asignar a cada tarea). Es distinta de la 003 (costo por tarea) y de la 004 (un modelo vence). No se usó el tema de reserva: el hecho central se verificó.

## Secuencia (7 láminas)

| Slide | Función narrativa | Titular | Texto de apoyo | Qué aporta al siguiente | Imagen y razón | Composición | Fuente de la afirmación |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | Tensión | No toda tarea necesita el modelo más grande. | El 7 de octubre Anthropic lanzó Claude Haiku 5.5, un modelo pequeño. | ¿Qué es exactamente Haiku 5.5? | Sin foto. Esfera grande y esfera pequeña con etiquetas: el modelo más grande contra un correo por clasificar. | Fondo Ink, esfera de degradado de marca recortada abajo a la derecha | Anthropic, anuncio |
| 02 | Hecho (ficha) | Haiku 5.5 salió el 7 de octubre. | Ficha: `claude-haiku-5-5`, $0,10 y $0,50 por millón de tokens, contexto de 1 millón, salida de 128.000; precios hasta 100.000 tokens por prompt | ¿Para qué lo propone Anthropic? | Sin imagen. Ficha técnica con identificador en monoespaciada. | Fondo superficie | Anthropic, anuncio y ficha del modelo |
| 03 | Hecho (uso) | Lo pensó para trabajo rápido y repetido. | Resumir, compactar contexto, consultar bases de datos, clasificar, atención en vivo; para código agéntico complejo, Anthropic dice que Sonnet 5.5 y Opus 5.5 siguen siendo mejores. Anthropic vende los tres modelos. | ¿Qué tan grande es la diferencia? | Sin imagen. Etiquetas en cápsulas. | Fondo Ink | Anthropic, anuncio |
| 04 | Mecanismo | La brecha cambia según la tarea. | Terminal-Bench 4.0: 39,2% contra 70,6% (31,4 puntos). OSWorld 2.1 sin conexión: 72,4% contra 83,9% (11,5 puntos). Cifras de Anthropic, sin verificación independiente. | Si cambia según la tarea, hay que clasificar las tareas | Sin imagen. Barras emparejadas. | Fondo claro | Anthropic, anuncio; diferencias son cuentas de Plogy |
| 05 | Criterio de Plogy | Clasifica tus tareas antes de elegir. | Cuatro tipos de tarea con el modelo con el que empezar a probar | ¿Cómo se decide? | Sin imagen. Cuatro tarjetas con indicador de tamaño. | Etiqueta "Criterio de Plogy", fondo superficie | Criterio de Plogy |
| 06 | Método | Prueba con 20 casos reales. | Cuatro pasos: tomar los casos, escribir antes qué es bien hecho, correr el modelo pequeño, subir solo si no llega | CTA con el recurso | Sin imagen. Rejilla de 20 casos numerados. | Fondo Ink | Criterio de Plogy |
| 07 | Síntesis y CTA | Elige por tarea. Prueba con 20 casos. | Lo que recibes: matriz, plantilla de la prueba, la noticia con su fuente. Comenta ELEGIR. | Cierre | Mano sobre un teclado de teclas verdes en un cuarto naranja (derivado 20 de la biblioteca): el gesto de elegir una tecla. | Variante 20 de `skills/plogy-cta-design` y `cta-biblioteca` (vidrio con lista), adaptada | Criterio de Plogy |

Hay una parte de la historia que el carrusel no cuenta y el reporte sí: el ejemplo hipotético de las tres tareas, los cambios de código al pasar a Haiku 5.5 y lo que la pieza no cubre.

## Textos por canal

Ver `textos.md` (caption de Instagram con hashtags y su razón, post de LinkedIn y diferencia de enfoque) y `dm.md` (mensajes 1 y 2, cierre de campaña y UTM). El mensaje 1 enlaza la fuente primaria de Anthropic.

## Reporte con imágenes

El reporte (`reporte.md` y `reporte.html`) tiene resumen, qué pasó, qué se sabe y qué no, lectura de Plogy, matriz, prueba, ejemplo hipotético, plantilla, cambios al probar Haiku 5.5, lo que no cubre, fuentes e historial. Las siete figuras (portada, ficha de modelos, brecha, matriz, prueba de 20 casos, ejemplo hipotético y plantilla) están en `assets/reporte/fig-*.png`, cada una con su fuente, más la foto de la biblioteca (derivado 20) con su pie.

## Estado del flujo con reporte (checklist de salida)

- [ ] Reporte guardado como `reporte.md`, revisado por una persona y publicado en su URL definitiva. (Hoy: borrador `reporte.md`)
- [x] Cada hecho del reporte tiene fuente, hipótesis marcadas y lo no verificado anotado.
- [x] El reporte tiene portada y figuras revisadas, con la fuente visible en cada una.
- [ ] Palabra clave ELEGIR registrada con vigencia. (Se anota aquí; el registro de palabras clave del flujo aún no existe.)
- [ ] Mensajes de DM aprobados por una persona. (Hoy: borrador `dm.md`)
- [ ] Flujo de DM probado con una cuenta de prueba.
- [ ] Persona asignada para responder lo que llegue por fuera del flujo.
- [ ] Herramienta de DM elegida.
- [x] CTA del carrusel, caption y LinkedIn alineados con el reporte.
- [ ] Derechos de fotos y licencias de tipografía resueltos.
- [ ] Aprobación humana con fecha.

## Revisión

- Evidencia y procedencia de cada dato: ver "Qué afirma la fuente" arriba. Los hechos centrales vienen de páginas de Anthropic leídas el 2026-10-20 (anuncio, noticias, documentación y precios). Los precios se contrastaron en tres páginas. Las cifras de pruebas solo en el anuncio, leído dos veces. Las cuentas son de Plogy: 70,6 − 39,2 = 31,4; 83,9 − 72,4 = 11,5. En el ejemplo hipotético, los aciertos y umbrales son inventados y se rotulan en la figura, en el reporte y en LinkedIn. Las láminas 05 y 06 son criterio de Plogy, rotuladas en la 05 y en la nota de la 06.
- Ejemplo hipotético: aparece en el reporte, en las figuras y en LinkedIn, rotulado como hipotético. Ninguna lámina presenta un caso inventado como real.
- Derechos de cada asset y licencia de la tipografía: una foto del moodboard con derechos sin verificar (ver inventario). Screener solo tiene licencia demo. Space Grotesk se cargó desde Google Fonts: falta confirmar licencia para uso comercial.
- Legibilidad de cada slide a tamaño móvil: revisada a simple vista en los PNG. Texto de apoyo de 33 a 40 px sobre un lienzo de 1080 px; las fuentes y notas inferiores bajan a 30 px, como en las piezas anteriores. Los números de la rejilla de la lámina 06 y las etiquetas pequeñas de la lámina 04 son de 28 a 30 px. Pendiente confirmar en un móvil real.
- Coherencia entre tesis, secuencia, caption y CTA: la tesis (un modelo por tarea, decidido con 20 casos), la matriz, la prueba, el caption, el LinkedIn y el reporte coinciden. El CTA de las láminas y de Instagram es "Comenta ELEGIR". LinkedIn cierra con una pregunta sustantiva.
- Verificación de estilo: sin guiones largos ni rayas en ningún texto de la pieza, sin emojis en LinkedIn, 4 hashtags, sin las muletillas de la lista prohibida.
- Pendiente de aprobación humana:
  1. Revisar `reporte.md` (leído por resumen: comparar cifras y citas con las páginas de Anthropic).
  2. Volver a comprobar anuncio, ficha y precios de Anthropic el día de publicar, y contrastar las cifras de Terminal-Bench y OSWorld con la página original.
  3. Confirmar que la matriz y la prueba reflejan cómo trabaja Plogy, y que 20 casos y los umbrales de ejemplo son un punto de partida aceptable.
  4. Decidir la vigencia de la palabra clave ELEGIR y confirmar que no choca con otra pieza.
  5. Verificar los derechos de la foto o reemplazarla por material propio o licenciado.
  6. Verificar licencias de Screener y Space Grotesk.
  7. Ver las láminas en un móvil real.
  8. Publicar el reporte, configurar y probar el DM antes de publicar el carrusel.
  9. Aprobación y fecha.
- Aprobación humana y fecha: PENDIENTE

## Archivos de la pieza

- `carrusel.html`: fuente editable de las 7 láminas (1080x1350). Sin parámetros muestra todas; con `?s=1` a `?s=7`, una sola.
- `exports/slide-01.png` a `slide-07.png`: exportaciones en orden.
- `reporte-figuras.html`: fuente de las figuras del reporte; `assets/reporte/fig-*.png`: figuras exportadas (portada, ficha, brecha, matriz, prueba, ejemplo, plantilla). `reporte.md` y `reporte.html`: el reporte en texto y como página.
- `dm.md`, `textos.md` y `brief.md`: mensajes de DM, textos por canal y este brief. Cada uno tiene también su versión `.html`, generada para el visor.
- `assets/`: derivado de foto copiado de la biblioteca (no es original).

## Inventario de assets

| Asset | Origen | Transformación | Lámina | Derechos |
| --- | --- | --- | --- | --- |
| `brandkit/assets/plogy-color.svg` | Brand kit Plogy | Ninguna | 02, 04, 05 y figuras | Propio de Plogy. Trazado derivado de la fuente demo, por verificar. |
| `brandkit/assets/plogy-white.svg` | Brand kit Plogy | Ninguna | 01, 03, 06, 07, portada y figura de la prueba | Igual que el anterior |
| `assets/20-teclado.jpg` | Copia de `piezas/cta-biblioteca/assets/20-teclado.jpg`. Original: `assets/reference-originals/4e568284db737bcd62fe36404767dd07.jpg` (variante 20 de la biblioteca, mano sobre un teclado; confirmado en `cta-biblioteca/scripts/derive.py`). Autor desconocido. | Recorte a 1080x1350 y rojos llevados al naranja de marca (derivado de la biblioteca, no se volvió a derivar). | 07 y reporte | `unverified_reference_only`. NO publicar hasta verificar derechos. |
| Esferas, ficha, cápsulas, barras, tarjetas, rejilla y figuras del reporte | CSS y texto | Ninguna | 01 a 06 y figuras | Propio |

Fotos revisadas y descartadas: `good enough.jpg` muestra a una persona pública identificable (excluida por regla) y `perfection.jpg` (manos en trama con una ventana de programa) no explica nada de esta pieza. Ninguna se usó. Los originales siguen intactos en `assets/reference-originals/`.
