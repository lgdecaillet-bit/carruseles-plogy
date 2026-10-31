# Pieza 013 · Automatización, asistente o agente

Estado: BORRADOR PARA REVISIÓN HUMANA. No publicar.

Pieza educativa (framework de decisión, comparación) que no parte de una noticia. Tiene CTA comercial por DM con palabra clave PROCESO; no hay reporte ni recurso. Los textos por canal están en `textos.md` y el guion de conversación en `dm.md`.

## Oportunidad

- ID y estado editorial: 013 · borrador completo (carrusel, textos y guion de DM), pendiente de revisión humana
- Tipo de origen: criterio propio de Plogy (pieza educativa), con una definición citada de una fuente primaria. Sin noticia.
- Fuente primaria, fecha y enlace:
  - Anthropic, "Building effective agents", Erik S. y Barry Zhang, Engineering at Anthropic, publicada el 19 de diciembre de 2024. https://www.anthropic.com/engineering/building-effective-agents
  - Consultada con WebFetch el 2026-10-20.
- Interés comercial de la fuente: Anthropic vende modelos (Claude) y herramientas para construir agentes. La propia página menciona el Claude Agent SDK, modelos Claude, el Model Context Protocol y Claude Managed Agents. La usamos para la definición de "agente" y para dos advertencias (costo y errores acumulados; empezar por lo simple). Se rotula así en la lámina 02, en la 06, en el caption y en LinkedIn.
- Qué confirma la fuente primaria (leído en la página):
  - "Workflows are systems where LLMs and tools are orchestrated through predefined code paths."
  - "Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks."
  - "We recommend finding the simplest solution possible, and only increasing complexity when needed." (traducida en la lámina 06 como traducción de Plogy).
  - "The autonomous nature of agents means higher costs, and the potential for compounding errors."
  - "Agents can then pause for human feedback at checkpoints or when encountering blockers." (apoya la idea de una persona que aprueba; no se cita en láminas).
- Qué es criterio de Plogy y no de la fuente:
  - La separación en tres niveles (automatización, asistente, agente). La fuente distingue dos (workflows y agents) y no usa "asistente". Nuestra "automatización" equivale a un workflow de pasos fijos, y puede incluir un paso con IA; eso se dice en la lámina 02 ("aunque uno use IA").
  - Las cuatro preguntas, su orden y el árbol de decisión.
  - Los tres procesos de la lámina 05 y el paso "una persona aprueba si el error cuesta caro".
  - La escalera de la lámina 06 (flexibilidad frente a costo y riesgo) es cualitativa, sin cifras.
- Qué queda sin verificar: otras definiciones de "agente" (OpenAI, Google, Microsoft) que pueden dibujar la frontera de otra forma; no se consultaron. La página de Anthropic muestra la fecha original y menciona modelos posteriores, así que se actualizó después de diciembre de 2024; no se verificó qué cambió. No hay estudios ni cifras de terceros. Que el árbol refleje cómo decide Plogy con clientes reales no está verificado (no se ha aplicado a un cliente).
- Audiencia: Negocios
- Vertical: IA y automatizaciones
- Pilar principal: Conocimiento
- Pilar secundario: ninguno
- Subcategoría y confianza de clasificación: framework de decisión con ejemplos hipotéticos · confianza alta en el pilar
- Tesis de Plogy en una frase: no todo proceso necesita un agente; el nivel correcto es el más bajo que resuelve el proceso, y cuatro preguntas ordenadas lo deciden.
- Problema o tensión que hace relevante la pieza: "automatización", "asistente" y "agente" se usan como sinónimos y un negocio puede comprar (o construir) más nivel del que necesita, con más costo y más riesgo.
- Ángulo distintivo y por qué Plogy puede decirlo: Plogy implementa IA en negocios y decide a diario qué nivel pide un proceso. El árbol convierte ese criterio en una herramienta que la audiencia puede usar sola. Complementa la 001 (ordenar antes de automatizar) y la 005 (medir antes de automatizar).
- Objetivo: conversación comercial (leads calificados por DM)
- Término principal de búsqueda y términos secundarios reales: "automatización, asistente o agente de IA". Secundarios: "diferencia entre agente de IA y automatización", "cuándo usar un agente de IA", "agente de IA para negocios".
- CTA del último slide y estado de lo prometido: "Escríbenos PROCESO por DM." Variante 25 de la biblioteca (círculo y maqueta de chat), adaptada. Lo que se promete es una conversación para ver qué nivel pide el proceso; Plogy confirma qué ofrece en esa conversación (`dm.md`). El flujo no está configurado. **El carrusel no se puede publicar hasta cumplir el checklist de salida.**

Por qué este tema: pedido de una pieza educativa de comparación. Es atemporal, ordena un vocabulario que el mercado mezcla y lleva de forma natural a una conversación comercial (el proceso de cada negocio).

## Secuencia (7 láminas)

| Slide | Función narrativa | Titular | Texto de apoyo | Qué aporta al siguiente | Imagen y razón | Composición | Fuente de la afirmación |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | Tensión | ¿Automatización, asistente o agente? | Tu proceso necesita uno. Subir de nivel cuesta más y arriesga más. | ¿Qué distingue a los tres? | Sin foto. Tres pastillas que crecen y se llenan de naranja (1, 2, 3). | Fondo claro | Criterio de Plogy |
| 02 | Definición | Cambia quién decide los pasos. | Tres filas: reglas fijas, persona que pide, IA que decide. Nota de fuente al pie. | ¿Cómo elijo entre ellos? | Sin imagen. Tarjetas con "Decide: las reglas, la persona, la IA". | Fondo Ink | Anthropic (definición de agente, con aviso de interés comercial); resto, criterio de Plogy |
| 03 | Método | Cuatro preguntas deciden el nivel. | Pasos iguales, juicio, actuar sobre sistemas, qué pasa si se equivoca. | ¿En qué orden se responden? | Sin imagen. Lista numerada. | Fondo claro | Criterio de Plogy |
| 04 | Árbol de decisión | Responde en este orden. | Árbol vertical con ramas Sí/No y tres resultados. | ¿Cómo se ve con procesos reales? | Sin imagen. Diagrama. | Fondo superficie | Criterio de Plogy |
| 05 | Ejemplo (hipótesis) | Tres procesos, tres niveles. | Factura (1 sí), respuesta a clientes (1 no, 2 sí, 3 no), reclamo con reembolso (1 no, 2 sí, 3 sí, 4 caro). | ¿Subir siempre es mejor? | Sin imagen. Tarjetas con el recorrido por el árbol. | Etiqueta "Ejemplo hipotético" | Procesos inventados, rotulados |
| 06 | Regla | Sube de nivel solo si el anterior no alcanza. | Escalera de tres niveles y cita traducida de Anthropic. | Cierre y siguiente paso | Sin imagen. Tres bloques que suben. | Fondo Ink | Anthropic (con aviso de interés comercial); escalera, criterio de Plogy |
| 07 | Síntesis y CTA | Ponle nivel a tu proceso. | Escríbenos PROCESO por DM. Respuesta del chat: "Cuéntanos qué proceso es y vemos qué nivel pide." | Cierre | Ojo de pez en un círculo naranja (derivado 25 de la biblioteca): la mirilla de la puerta a la que se toca. | Variante 25 (círculo y maqueta de chat), adaptada | Criterio de Plogy |

## Textos por canal

Ver `textos.md` (caption de Instagram con hashtags y su razón, post de LinkedIn y diferencia de enfoque) y `dm.md` (guion de conversación: primer mensaje, tres preguntas de calificación, cierre, lectura inicial, reglas y "antes de activar"). El CTA del caption coincide con el del último slide ("Escríbenos PROCESO por DM"). LinkedIn no tiene DM por palabra clave: cierra con una pregunta.

## Estado del flujo (checklist de salida, CTA comercial por DM)

- [x] Cada afirmación es una cita verificada de la fuente primaria (con su interés comercial) o criterio de Plogy declarado como tal, con la hipótesis marcada y sin cifras de terceros.
- [x] CTA del carrusel, caption y LinkedIn alineados (LinkedIn cierra con pregunta, no con el CTA de DM).
- [ ] Plogy define qué ofrece al cierre de la conversación (llamada, diagnóstico u otra cosa), con plazo y costo. Hoy: marcado "Plogy confirma qué ofrece" en `dm.md`.
- [ ] Palabra clave PROCESO registrada con vigencia. (Se anota aquí; el registro de palabras clave del flujo aún no existe.)
- [ ] Guion de DM aprobado por una persona. (Hoy: borrador `dm.md`)
- [ ] Flujo de DM probado con una cuenta de prueba y ventana de 24 horas verificada con Meta cuando la persona inicia el DM.
- [ ] Persona asignada para atender las conversaciones y lo que llegue fuera de guion, con horario.
- [ ] Herramienta de DM elegida.
- [ ] Derechos de la foto y licencias de tipografía resueltos.
- [ ] Aprobación humana con fecha.

## Revisión

- Evidencia y procedencia de cada dato: la definición de agente y las dos advertencias son citas de Anthropic, leídas el 2026-10-20 en la página (ver arriba). Todo lo demás es criterio de Plogy. Los tres procesos de la lámina 05 son inventados y rotulados "Ejemplo hipotético" en la lámina, en el caption y en LinkedIn. No hay cifras.
- Derechos de cada asset y licencia de la tipografía: una foto del moodboard con derechos sin verificar (ver inventario). Parece un fotograma de película con un hombre de gabardina; no se identifica a la persona ni la obra, y conviene reemplazarlo por material propio o licenciado antes de publicar. Screener solo tiene licencia demo. Space Grotesk se cargó desde Google Fonts: falta confirmar licencia para uso comercial.
- Legibilidad de cada slide a tamaño móvil: revisada a simple vista en los PNG. Textos de apoyo de 32 a 40 px sobre un lienzo de 1080 px; las etiquetas del árbol (lámina 04) y la nota de fuente (lámina 06, 30 px) son las más pequeñas. Pendiente confirmar en un móvil real.
- Coherencia entre tesis, secuencia, caption y CTA: la tesis (el nivel más bajo que resuelve el proceso), los tres niveles, las cuatro preguntas, el caption, LinkedIn y el guion de DM coinciden. El árbol de la lámina 04 y el recorrido de los ejemplos de la 05 dan los mismos resultados. El CTA de la lámina y de Instagram es "Escríbenos PROCESO por DM".
- Una limitación del árbol que conviene conocer: es una guía de primera lectura. No considera costos de construir y mantener cada nivel, ni la calidad de los datos, ni las reglas de cada sector (por ejemplo, regulación). La pregunta 4 se responde con criterio: "cuesta caro" depende del negocio.
- Verificación de estilo: sin guiones largos, sin emojis en LinkedIn, hashtags ≤ 5, sin las muletillas de la lista prohibida.
- Pendiente de aprobación humana:
  1. Confirmar que el árbol y los tres niveles reflejan cómo decide Plogy con clientes, y si se quiere contrastar la definición con otra fuente además de Anthropic.
  2. Definir qué ofrece Plogy en la conversación de PROCESO, y quién la atiende.
  3. Decidir la vigencia de la palabra clave.
  4. Verificar los derechos de la foto o reemplazarla por material propio o licenciado.
  5. Verificar licencias de Screener y Space Grotesk.
  6. Ver las láminas en un móvil real.
  7. Configurar y probar el DM antes de publicar el carrusel.
  8. Aprobación y fecha.
- Aprobación humana y fecha: PENDIENTE

## Archivos de la pieza

- `carrusel.html`: fuente editable de las 7 láminas (1080x1350). Sin parámetros muestra todas; con `?s=1` a `?s=7`, una sola.
- `exports/slide-01.png` a `slide-07.png`: exportaciones en orden.
- `dm.md`, `textos.md` y `brief.md`: guion de DM, textos por canal y este brief. Cada uno tiene también su versión `.html`, generada para el visor.
- `assets/25-ojo-pez.jpg`: derivado de la biblioteca de CTAs (copiado de `piezas/cta-biblioteca/assets/`, sin volver a derivar).

## Inventario de assets

| Asset | Origen | Transformación | Lámina | Derechos |
| --- | --- | --- | --- | --- |
| `brandkit/assets/plogy-color.svg` | Brand kit Plogy | Ninguna | 01, 03, 04, 05 | Propio de Plogy. Trazado derivado de la fuente demo, por verificar. |
| `brandkit/assets/plogy-white.svg` | Brand kit Plogy | Ninguna | 02, 06, 07 | Igual que el anterior |
| `assets/25-ojo-pez.jpg` | Biblioteca de CTAs `piezas/cta-biblioteca/assets/25-ojo-pez.jpg`, derivada de `assets/reference-originals/cb17c176...870c.jpg` (ojo de pez). Autor desconocido. | Ninguna sobre el derivado de la biblioteca (el catálogo registra "ninguno"). Recorte circular y borde naranja por CSS en la lámina. | 07 | `unverified_reference_only`. NO publicar hasta verificar derechos. |
| Pastillas, tarjetas, árbol, chips, escalera y chat | CSS y texto | Ninguna | 01 a 07 | Propio |

Los originales siguen intactos en `assets/reference-originals/`. No se usó ninguna foto extra.
