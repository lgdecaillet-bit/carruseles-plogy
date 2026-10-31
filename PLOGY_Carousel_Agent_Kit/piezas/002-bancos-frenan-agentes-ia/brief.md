# Pieza 002 · Los bancos frenan a los agentes de IA

Estado: BORRADOR PARA REVISIÓN HUMANA. No publicar.

## Oportunidad

- ID y estado editorial: 002 · borrador completo (texto, diseño y exportaciones), pendiente de revisión humana
- Tipo de origen: noticia
- Fuente primaria, fecha y enlace o registro interno:
  - The Next Web, "Schwab and JPMorgan are blocking AI agents from moving customer money", 16 de octubre de 2026, por Cristian Dina. https://thenextweb.com/news/schwab-blocks-ai-agents-meta-muse (leído completo).
  - Fuentes de ese artículo, no leídas directamente: entrevista de Rick Wurster (CEO de Schwab) en Bloomberg Television del 16 de octubre, y llamada de resultados de JPMorgan con declaraciones de Jamie Dimon, citada por The Next Web a través de Cybernews.
  - Fuentes de corroboración por búsqueda (resúmenes, no leídas completas): Cybernews, Digital Trends, Notebookcheck, TechCity, Officechai. Cybernews devolvió HTTP 403 al intentar leerla.
- Qué afirma la fuente y qué queda sin verificar:
  - Afirma (verificado en The Next Web): Wurster dijo en Bloomberg TV que Schwab bloquea a agentes de IA externos que intentan mover dinero de clientes y planteó la duda de responsabilidad ("We can't control it, the client can't control it, something could go wrong and who's liable?"). Schwab permitirá a IA externas ver saldos e investigar por servidores MCP bajo sus reglas, pero no mover dinero. Dimon dijo en la llamada de resultados que JPMorgan no dejará que agentes externos actúen dentro de sus sistemas y habló de "rogue agents". En JPMorgan, las herramientas externas no pueden enviar dinero ni pagar cuentas, y algunas pueden ver datos de la cuenta.
  - Sin verificar o excluido a propósito: (1) los conteos semanales de bloqueos de Schwab son cifras del propio Wurster y no se usan; (2) los resúmenes de búsqueda difieren en si Schwab dejará operar en bolsa a algunos traders, por eso la pieza solo dice "ver saldos e investigar"; (3) un resumen menciona que los términos de Chase desde el 1 de enero de 2027 harían al cliente responsable de lo que un agente haga con su acceso, y que JPMorgan permite datos de solo lectura por medio de Plaid; ninguna de las dos cosas aparece en el artículo leído, así que se dejaron fuera; (4) la cita de Dimon viene de un reporte secundario, no de la transcripción.
- Audiencia: Negocios
- Vertical: IA y automatizaciones
- Pilar principal: Conocimiento (vale por entender cómo se decide qué permisos darle a un agente)
- Pilar secundario: ninguno
- Subcategoría y confianza de clasificación: noticia explicada con marco de implementación · confianza alta en el pilar, media en la parte factual por depender de fuentes secundarias
- Tesis de Plogy en una frase: darle permisos a un agente es una decisión de diseño, no un interruptor, y el primer paso es separar leer de actuar y saber quién responde.
- Problema o tensión que hace relevante la pieza: los negocios empiezan a conectar agentes a sus sistemas y los bancos acaban de poner en palabras la pregunta que casi nadie se hace: ¿quién responde si algo sale mal?
- Ángulo distintivo y por qué Plogy puede decirlo: Plogy implementa IA en negocios. La noticia sirve de caso para un criterio propio (la escalera de permisos). La escalera es criterio de Plogy, no hecho de la fuente, y así se rotula en la lámina 04.
- Objetivo: conversación y comunidad
- Término principal de búsqueda y términos secundarios reales: "agentes de IA" y "permisos para agentes de IA". Secundarios: "IA para negocios", "automatización con IA".
- CTA del último slide y estado del recurso prometido: "Comenta Plogy" y "dinos qué le dejarías hacer a un agente en tu negocio". No promete recurso. Requiere que alguien del equipo responda los comentarios.

Por qué esta noticia y no otras de la semana (12 al 19 de octubre de 2026): hubo Gemini 4 Argon (13 oct), modelos de Meta, demandas de fiscales estatales a OpenAI (14 oct), la ronda de 1.000 millones de dólares de Instinct y la caída de acciones de chips. Sonnet 5.5 salió el 28 de septiembre, no esta semana, y no encontré el producto "Apollo". Se eligió el caso de los bancos porque es el que mejor sostiene un criterio aplicable a un negocio.

## Secuencia (7 láminas)

| Slide | Función narrativa | Titular | Texto de apoyo | Qué aporta al siguiente | Imagen y razón | Composición | Fuente de la afirmación |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | Tensión | Los bancos le dijeron no a los agentes de IA. | Schwab y JPMorgan no dejan que agentes externos muevan el dinero de sus clientes. | Abre la deuda: ¿por qué? | Tres figuras desconocidas con cajas "UNKNOWN" frente a una valla de propiedad privada (derivado 01): agentes externos que nadie reconoce. | Texto arriba, foto abajo con degradado a Ink, cajas pasadas al naranja | The Next Web, 16 oct 2026 |
| 02 | Hecho y fuente | La pregunta que frena todo: ¿quién responde? | Cita de Wurster, traducción libre, con atribución | Si el freno es la responsabilidad, ¿qué sí permiten? | Sin imagen | Fondo claro, cita con barra naranja | The Next Web (Bloomberg TV, 16 oct 2026) |
| 03 | Cambio de lectura | No cierran la puerta. La dejan entreabierta. | Sí permiten ver saldos e investigar, por enlaces seguros (MCP) que el banco controla. Mover dinero, no. | Si leer y actuar se separan, eso se puede copiar | Sin imagen | Fondo Ink, titular con brillo naranja | The Next Web, 16 oct 2026 |
| 04 | Mecanismo (criterio de Plogy) | Cuatro niveles de permiso para un agente. | No es un interruptor. Es una escalera. | Falta llevarlo al negocio de quien lee | Sin imagen. Diagrama de escalera: Ver, Proponer, Actuar con aprobación, Actuar solo. | Etiqueta "Criterio de Plogy", escalera ascendente, el nivel 4 en Ink | Criterio de Plogy, no de la fuente |
| 05 | Traslado | Tu negocio no es un banco. La pregunta es la misma. | Si un agente puede mandar un correo, cambiar un precio o pagar una factura, alguien tiene que responder antes de dárselo. | Un ejemplo concreto | Mesa larga con doce personas y el centro vacío (derivado 05): la decisión que nadie ha puesto sobre la mesa. | Foto arriba con mezcla screen sobre Ink, texto abajo | Criterio de Plogy |
| 06 | Ejemplo (hipótesis) | Así subiría un agente de atención al cliente. | Puede leer pedidos desde el día uno. Los reembolsos, solo con tu aprobación. | Cierre | Sin imagen. La misma escalera con los niveles 1 a 3 en naranja y el 4 punteado. | Etiqueta "Ejemplo hipotético" | Escenario inventado y marcado, no es un caso de cliente |
| 07 | Síntesis y CTA | Primero leer. Después actuar. | Comenta Plogy y dinos qué le dejarías hacer a un agente en tu negocio. | Cierre | Público con gafas 3D y una silueta naranja que no coincide (derivado 07): quien hace la pregunta incómoda. | CTA variante C del sistema `skills/plogy-cta-design` | Criterio de Plogy |

## Textos por canal

### Caption de Instagram

Agentes de IA y permisos: Schwab y JPMorgan no dejan que agentes externos muevan el dinero de sus clientes. Sí permiten ver saldos e investigar, por enlaces seguros que el banco controla.

El motivo que dio el CEO de Schwab fue de responsabilidad: si algo sale mal, ¿quién responde? Es la misma pregunta para cualquier negocio que quiera meter un agente en sus procesos. Nuestro punto de partida es una escalera de cuatro niveles: ver, proponer, actuar con aprobación y actuar solo. Se sube un nivel cuando alguien responde por lo que el agente hace y queda un registro de sus acciones.

Fuente: The Next Web, 16 oct 2026, con la entrevista de Wurster en Bloomberg TV.

Comenta Plogy y dinos qué le dejarías hacer a un agente en tu negocio.

#AgentesDeIA #IAParaNegocios #AutomatizacionConIA

### Hashtags elegidos y razón

- #AgentesDeIA: tema central y término de búsqueda.
- #IAParaNegocios: marca la audiencia.
- #AutomatizacionConIA: la vertical de Plogy.
- Tres de cinco posibles. Decisión deliberada: más no añadirían precisión.

### Post de LinkedIn

Dos de los bancos más grandes de Estados Unidos acaban de decir que no a los agentes de IA externos que quieren mover dinero de sus clientes. Lo útil no es el bloqueo, es el argumento.

El CEO de Schwab, Rick Wurster, lo planteó en Bloomberg TV el 16 de octubre con una pregunta (traducción libre): no lo controlamos nosotros, no lo controla el cliente, algo puede salir mal, ¿y quién responde? Según The Next Web, Schwab permitirá que IA externas vean saldos e investiguen por enlaces MCP que el banco controla, pero no que muevan dinero. Jamie Dimon, de JPMorgan, habló de "agentes descontrolados" en la llamada de resultados, en un dato que The Next Web toma de Cybernews.

Para un negocio que implementa agentes hay una consecuencia práctica: el permiso es una decisión de diseño y no un interruptor. Una escalera que nosotros usaríamos como punto de partida: ver, proponer, actuar con aprobación y actuar solo. Se sube un escalón cuando una persona concreta responde por lo que el agente hace y existe un registro de sus acciones.

Un ejemplo hipotético, no un caso de cliente: un agente de atención podría empezar leyendo pedidos, pasar a proponer respuestas y enviar reembolsos solo con aprobación humana.

¿En tu empresa, quién respondería hoy si un agente se equivoca?

### Diferencia de enfoque entre canales

Instagram parte del hecho y lo traduce a una regla simple, con la fuente al pie y un CTA de comunidad ("Comenta Plogy"). LinkedIn parte de la tesis, atribuye cada dato a su fuente y cierra con una pregunta sustantiva sobre quién responde. No comparten estructura ni CTA.

## Revisión

- Evidencia y procedencia de cada dato: ver "Qué afirma la fuente" arriba. Cada afirmación factual de las láminas 01 a 03 se apoya en The Next Web del 16 de octubre de 2026. Las láminas 04 a 07 son criterio de Plogy o ejemplo hipotético y están rotuladas como tales. No hay cifras en la pieza.
- Cita en la lámina 02: es traducción libre al español del inglés "We can't control it, the client can't control it, something could go wrong and who's liable?". La lámina lo indica. Revisar si se prefiere mostrar la cita original en inglés.
- Derechos de cada asset y licencia de la tipografía: tres fotos del moodboard con derechos sin verificar (ver inventario). Screener solo tiene licencia demo. Space Grotesk se cargó desde Google Fonts: falta confirmar licencia para uso comercial.
- Legibilidad de cada slide a tamaño móvil: revisada a simple vista en los PNG. Texto de apoyo de 40 px y titulares de 80 a 108 px sobre lienzo de 1080 px. Los textos más pequeños son los contadores (30 px), las fuentes (30 px) y las etiquetas de la escalera (28 px). Pendiente confirmar en un móvil real.
- Coherencia entre tesis, secuencia, caption y CTA: la tesis (permisos como decisión de diseño), la escalera, el caption y el LinkedIn coinciden. El CTA de las láminas y de Instagram es "Comenta Plogy". LinkedIn cierra con una pregunta sustantiva.
- Verificación de estilo: sin guiones largos, sin emojis en LinkedIn, hashtags ≤ 5, sin las muletillas de la lista prohibida.
- Pendiente de aprobación humana:
  1. Confirmar que la escalera de cuatro niveles refleja cómo trabaja Plogy (el caption y el LinkedIn la presentan como "nuestro punto de partida" y "usaríamos").
  2. Contrastar la noticia con una fuente primaria (la entrevista de Bloomberg o el reporte de Cybernews), porque se trabajó con The Next Web como fuente principal.
  3. Verificar los derechos de las tres fotos o reemplazarlas por material propio o licenciado.
  4. Verificar licencias de Screener y Space Grotesk.
  5. Ver las láminas en un móvil real.
  6. Que alguien del equipo pueda responder los comentarios que genere "Comenta Plogy".
  7. Aprobación y fecha.
- Aprobación humana y fecha: PENDIENTE

## Archivos de la pieza

- `carrusel.html`: fuente editable de las 7 láminas (1080x1350). Sin parámetros muestra todas; con `?s=1` a `?s=7`, una sola.
- `exports/slide-01.png` a `slide-07.png`: exportaciones en orden, hechas con `skills/plogy-cta-design/scripts/render-slides.ps1`.
- `scripts/derive.py`: crea los derivados de las fotos 01 y 05.
- `assets/`: derivados de foto (no son originales).

## Inventario de assets

| Asset | Origen | Transformación | Lámina | Derechos |
| --- | --- | --- | --- | --- |
| `brandkit/assets/plogy-white.svg` | Brand kit Plogy | Ninguna | 01, 03, 05, 07 | Propio de Plogy. Trazado derivado de la fuente demo, por verificar. |
| `brandkit/assets/plogy-color.svg` | Brand kit Plogy | Ninguna | 02, 04, 06 | Igual que el anterior |
| `assets/01-agentes-unknown.jpg` | Original: `assets/reference-originals/ai watching.jpg`. Cuenta con logo de otra marca (SOLTO) en la esquina superior izquierda. | Recorte de la franja y 300-1060, que deja fuera el logo ajeno. Grises invertidos y mapeados de Ink a blanco. Cajas rojas pasadas al Orange de Plogy. Degradado a Ink arriba. | 01 | `unverified_reference_only`. NO publicar hasta verificar derechos. El logo de otra marca se eliminó por recorte, lo cual no resuelve la autoría de la obra. |
| `assets/05-mesa-larga.jpg` | Original: `assets/reference-originals/a company at work.jpg` | Reescala a 1080 px de ancho. Mezcla screen sobre Ink. Recorte por object-fit a 510 px de alto. | 05 | `unverified_reference_only`. NO publicar hasta verificar derechos. |
| `assets/07-cta-silueta.jpg` | Copia de `../001-automatizar-el-desorden/assets/cta-c-silueta.jpg`. Original: `assets/reference-originals/being different.jpg` | Recorte 4:5, rojo desplazado al Orange. Degradado de protección en el diseño. | 07 | `unverified_reference_only`. NO publicar hasta verificar derechos. |
| Escalera, etiquetas y cita | Texto y CSS | Ninguna | 02, 04, 06 | Propio |

Los originales siguen intactos en `assets/reference-originals/`.

Por qué cada foto: 01 muestra agentes sin identificar frente a una propiedad privada, la imagen del "no". 05 es una mesa de decisión donde el centro está vacío hasta que alguien pone la responsabilidad encima. 07 es la silueta que no coincide con el público, la pregunta incómoda. Las láminas 02, 03, 04 y 06 quedan tipográficas porque llevan una cita, un dato o un diagrama que ya explica la idea.
