# Pieza 004 · Tu automatización vence el 14 de enero

Estado: BORRADOR PARA REVISIÓN HUMANA. No publicar.

Segunda pieza que aplica el flujo con reporte y DM de `skills/plogy-cta-design/FLUJO-REPORTE-DM.md`: carrusel, reporte web con imágenes (`reporte.md`) y mensajes de DM (`dm.md`). Los textos por canal están en `textos.md`.

## Oportunidad

- ID y estado editorial: 004 · borrador completo (carrusel, reporte con figuras, DM y textos), pendiente de revisión humana
- Tipo de origen: noticia
- Fuente primaria, fecha y enlace o registro interno:
  - OpenAI, "Deprecations", entrada "GPT-4 series model deprecations" del 14 de octubre de 2026. https://developers.openai.com/api/docs/deprecations (leída completa).
  - OpenAI, ficha de `gpt-6-luna`. https://developers.openai.com/api/docs/models/gpt-6-luna (leída).
  - OpenAI, guía de razonamiento. https://developers.openai.com/api/docs/guides/reasoning (leída).
  - Mixed, https://mixed-news.com/en/openai-gpt-4o-gpt-4-1-shutdown-january-14-2027-92-days-notice/ (leída). Digital Applied, https://www.digitalapplied.com/blog/gpt-4o-gpt-4-1-api-shutdown-january-2027 (leída; vende servicios de migración).
  - No leída: FourWeekMBA (HTTP 403) y daily.dev (solo vista en búsqueda).
- Qué afirma la fuente y qué queda sin verificar:
  - Afirma (verificado en OpenAI): el aviso del 14 de octubre de 2026; cinco identificadores (`gpt-4o-2024-08-06`, `gpt-4o-2024-11-20`, `gpt-4o-mini-2024-07-18`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`) salen de la API el 14 de enero de 2027; los fine-tunes siguen el calendario de su base; reemplazo recomendado `gpt-6-luna`. Ficha de Luna: $0,10 entrada, $0,01 caché, $0,50 salida; contexto de 1.050.000; salida máxima de 128.000; conocimiento hasta el 18 de mayo de 2026; llamadas a funciones en Chat Completions solo con `reasoning_effort: none`; sin fine-tuning; razonamiento por defecto medio. Guía: el razonamiento se factura como tokens de salida.
  - Verificado en OpenAI el 2026-10-20 tras la revisión independiente: los datos de GPT-4o, GPT-4o mini, GPT-4.1 y GPT-4.1 mini (el 25× solo vale frente a GPT-4o); la política de al menos seis meses para modelos de disponibilidad general (la página no dice si estos lo son); el 6 de enero de 2027 como cierre general del ajuste fino de autoservicio. Sin verificar: que ese cierre afecte a estos modelos (lectura de Digital Applied); qué hacen los alias tras el apagado. Los 92 días se comprobaron por fechas (14 oct a 14 ene).
- Audiencia: Negocios
- Vertical: IA y automatizaciones
- Pilar principal: Conocimiento (vale por enseñar a tratar un modelo como una dependencia con fecha)
- Pilar secundario: ninguno
- Subcategoría y confianza de clasificación: noticia con criterio aplicable · confianza alta en el pilar y en los hechos de la parte OpenAI, media en lo que depende de terceros
- Tesis de Plogy en una frase: un modelo de IA es una dependencia de la automatización, y las dependencias vencen; lo primero es saber dónde está.
- Problema o tensión que hace relevante la pieza: hay automatizaciones que llaman a un modelo por su nombre en varios lugares, y a los 92 días del aviso dejarán de funcionar si nadie las revisa.
- Ángulo distintivo y por qué Plogy puede decirlo: Plogy implementa IA en negocios, donde lo que se rompe en silencio cuesta. El inventario, las pruebas y la vuelta atrás son criterio de Plogy, no hecho de la fuente, y así se rotulan. No hemos migrado ningún flujo a `gpt-6-luna`.
- Objetivo: recurso (reporte y lista de revisión por DM)
- Término principal de búsqueda y términos secundarios reales: "GPT-4o se apaga" y "migrar de GPT-4o". Secundarios: "gpt-6-luna", "GPT-4.1 deprecación", "automatización con IA".
- CTA del último slide y estado del recurso prometido: "Comenta MIGRAR y te mandamos la noticia completa y nuestra lista de revisión." El recurso (reporte con la lista) está en borrador, no publicado. El DM no está configurado. **El carrusel no se puede publicar hasta cumplir el checklist de salida.**

Por qué este tema: la noticia es del 14 de octubre, tiene una fecha límite concreta y verificable en la fuente primaria, y toca el negocio de Plogy (automatizaciones que dependen de un modelo). Las piezas anteriores trataron el desorden previo a automatizar (001), los límites de los agentes (002) y el costo por tarea (003). Otros temas de la semana (agentes de OpenAI "Dots", agentes de Meta) quedaron como candidatos; no se pudieron leer sus fuentes primarias.

## Secuencia (7 láminas)

| Slide | Función narrativa | Titular | Texto de apoyo | Qué aporta al siguiente | Imagen y razón | Composición | Fuente de la afirmación |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | Tensión | El 14 de enero tu automatización puede romperse. | OpenAI retira GPT-4o y GPT-4.1 de su API. | ¿Cuáles, exactamente? | Computador viejo con un ojo en la pantalla (derivado 01): un modelo que se apaga. | Fondo Ink, foto arriba con degradado, texto abajo | OpenAI, deprecaciones |
| 02 | Hecho (qué se apaga) | Cinco versiones salen de la API el 14 de enero de 2027. | Los cinco identificadores; los fine-tunes siguen el mismo calendario | ¿Cuánto tiempo hay? | Sin imagen. Identificadores en tipografía monoespaciada. | Fondo superficie | OpenAI, deprecaciones |
| 03 | Hecho (plazo) | El aviso fue corto. | 92 días. OpenAI declara al menos 6 meses para modelos de disponibilidad general; su página no aclara si estos lo son | ¿Y el reemplazo? | Sin imagen. Número grande con brillo naranja. | Fondo Ink | OpenAI (fechas y política) |
| 04 | Mecanismo | El reemplazo no es un cambio de nombre. | Razona por defecto; llamadas a funciones solo con `reasoning_effort: none` en Chat Completions; sin fine-tuning | ¿Y el costo? | Sin imagen. Tres tarjetas. | Fondo claro | OpenAI, ficha de gpt-6-luna |
| 05 | Hecho (precio) | Luna cuesta hasta 25 veces menos por token de entrada. | $0,10 contra $2,50 de GPT-4o; solo 1,5 veces frente a GPT-4o mini; el razonamiento se factura como salida | ¿Qué hacer? | Sin imagen. Número grande. | Fondo Ink | Fichas de OpenAI |
| 06 | Criterio de Plogy | Tres pasos antes del 14 de enero. | Inventario, pruebas con casos reales, vuelta atrás | Cierre | Sin imagen. Tres pasos numerados. | Etiqueta "Criterio de Plogy", fondo superficie | Criterio de Plogy |
| 07 | Síntesis y CTA | Primero el inventario. Después la migración. | Comenta MIGRAR y te mandamos la noticia completa y nuestra lista de revisión. | Cierre | Tres figuras idénticas con computadores viejos (derivado de la variante D): la misma tarea repetida en muchos lugares. | Variante D de `skills/plogy-cta-design` (foto arriba, panel Ink, botón naranja) | Criterio de Plogy |

## Textos por canal

Ver `textos.md` (caption de Instagram con hashtags y su razón, post de LinkedIn y diferencia de enfoque) y `dm.md` (mensajes 1 y 2, cierre de campaña y UTM).

## Reporte con imágenes

`reporte.md` incluye una portada, cinco figuras (calendario, modelos, comparación, diagrama de llamadas a funciones y lista de revisión) y una foto de la biblioteca. Las figuras se editan en `reporte-figuras.html` y se exportan a `assets/reporte/`. Cada figura dice su fuente; el punto del 6 de enero está marcado como de aplicación sin confirmar.

## Estado del flujo con reporte (checklist de salida)

- [ ] Reporte revisado por una persona y publicado en su URL definitiva. (Hoy: borrador `reporte.md`)
- [x] Cada hecho del reporte tiene fuente, hipótesis marcadas y lo no verificado anotado.
- [x] El reporte tiene portada y figuras revisadas, con la fuente visible en cada una.
- [ ] Palabra clave MIGRAR registrada con vigencia. (Se anota aquí; el registro de palabras clave del flujo aún no existe.)
- [ ] Mensajes de DM aprobados por una persona. (Hoy: borrador `dm.md`)
- [ ] Flujo de DM probado con una cuenta de prueba.
- [ ] Persona asignada para responder lo que llegue por fuera del flujo.
- [ ] Herramienta de DM elegida.
- [x] CTA del carrusel, caption y LinkedIn alineados con el reporte.
- [ ] Derechos de fotos y licencias de tipografía resueltos.
- [ ] Aprobación humana con fecha.

## Revisión

- Evidencia y procedencia de cada dato: ver "Qué afirma la fuente" arriba. Los hechos centrales vienen de tres páginas de OpenAI leídas. Los datos de GPT-4o y de los otros tres modelos se contrastaron en sus fichas de OpenAI el 2026-10-20. Lo que sigue de terceros (que el cierre del 6 de enero afecte a estos modelos) está rotulado en la figura del calendario. La lámina 06 es criterio de Plogy. Las cuentas son de Plogy sobre las fichas: GPT-4o 2,50 ÷ 0,10 = 25 y 10 ÷ 0,50 = 20; GPT-4.1 20 y 16; GPT-4.1 mini 4 y 3,2; GPT-4o mini 1,5 y 1,2. La lámina 05 dice «hasta 25 veces» y lo acota a GPT-4o. Los 92 días: 17 días de octubre desde el 14, 30 de noviembre, 31 de diciembre y 14 de enero.
- Ejemplo hipotético: solo aparece en el reporte y en LinkedIn, rotulado como hipotético. Ninguna lámina presenta un caso inventado como real.
- Derechos de cada asset y licencia de la tipografía: dos fotos del moodboard con derechos sin verificar (ver inventario). Screener solo tiene licencia demo. Space Grotesk se cargó desde Google Fonts: falta confirmar licencia para uso comercial.
- Legibilidad de cada slide a tamaño móvil: revisada a simple vista en los PNG. Textos de apoyo de 34 a 40 px sobre un lienzo de 1080 px; las fuentes y notas bajan a 30 px. Pendiente confirmar en un móvil real.
- Coherencia entre tesis, secuencia, caption y CTA: la tesis (un modelo es una dependencia con fecha), el caption, el LinkedIn y el reporte coinciden. El CTA de las láminas y de Instagram es "Comenta MIGRAR". LinkedIn cierra con una pregunta sustantiva.
- Verificación de estilo: sin guiones largos, sin emojis en LinkedIn, hashtags ≤ 5, sin las muletillas de la lista prohibida.
- Pendiente de aprobación humana:
  1. Volver a comprobar la página de deprecaciones de OpenAI el día de publicar, y contrastar los datos de GPT-4o con una ficha de OpenAI.
  2. Confirmar que el inventario, las pruebas y la vuelta atrás reflejan cómo trabaja Plogy.
  3. Decidir la vigencia de la palabra clave.
  4. Verificar los derechos de las fotos o reemplazarlas por material propio o licenciado.
  5. Verificar licencias de Screener y Space Grotesk.
  6. Ver las láminas en un móvil real.
  7. Publicar el reporte, configurar y probar el DM antes de publicar el carrusel.
  8. Aprobación y fecha.
- Aprobación humana y fecha: PENDIENTE

## Archivos de la pieza

- `carrusel.html`: fuente editable de las 7 láminas (1080x1350). Sin parámetros muestra todas; con `?s=1` a `?s=7`, una sola.
- `exports/slide-01.png` a `slide-07.png`: exportaciones en orden.
- `reporte.md` y `reporte.html`: el reporte para la web, en texto y como página. `reporte-figuras.html`: fuente de las figuras; `assets/reporte/fig-*.png`: figuras exportadas.
- `dm.md`, `textos.md` y `brief.md`: mensajes de DM, textos por canal y este brief. Cada uno tiene también su versión `.html`, generada para el visor.
- `scripts/derive.py`: crea el derivado de la foto 01.
- `assets/`: derivados de foto (no son originales).

## Inventario de assets

| Asset | Origen | Transformación | Lámina | Derechos |
| --- | --- | --- | --- | --- |
| `brandkit/assets/plogy-color.svg` | Brand kit Plogy | Ninguna | 02, 04, 06, 07 y figuras | Propio de Plogy. Trazado derivado de la fuente demo, por verificar. |
| `brandkit/assets/plogy-white.svg` | Brand kit Plogy | Ninguna | 01, 03, 05 y portada del reporte | Igual que el anterior |
| `assets/01-pc-viejo.jpg` | Original: `assets/reference-originals/coding.jpg`. Autor desconocido. | Recorte de la zona del monitor y el teclado, desaturación de todo menos la pantalla roja, rojos llevados al naranja de marca, escalado a 1080 de ancho. Ver `scripts/derive.py`. | 01 | `unverified_reference_only`. NO publicar hasta verificar derechos. |
| `assets/07-cta-clones.jpg` | Copia de `../001-automatizar-el-desorden/assets/cta-d-clones.jpg`. Original: `assets/reference-originals/tem coding.jpg`. Autor desconocido. | Recorte a 1080x818 (derivado de la pieza 001). | 07 y reporte | `unverified_reference_only`. NO publicar hasta verificar derechos. |
| Tarjetas, identificadores, números y figuras del reporte | CSS y texto | Ninguna | 02 a 06 y figuras | Propio |

Los originales siguen intactos en `assets/reference-originals/`.
