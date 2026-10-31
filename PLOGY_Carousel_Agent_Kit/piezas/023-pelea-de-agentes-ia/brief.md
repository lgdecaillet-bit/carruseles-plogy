# Brief · pieza 023 · La pelea de los agentes

Estado: BORRADOR para revisión humana. No publicar. Aprobación humana y fecha: PENDIENTE.

## Qué es

Carrusel de 10 láminas en formato "pelea por rondas", a partir de una referencia de otra cuenta que Luciano mandó (comparación de Claude Duet contra Dots, Muse y Grok Bot). Fondo Ink con foco naranja. CTA: Comenta AGENTE y te mandamos nuestra guía (`guia.md`), en tarjeta de vidrio sobre la foto 10 de la biblioteca.

**Qué cambiamos de la referencia:** la referencia termina "6 rounds, 6 wins" y abre con "Claude just destroyed...". Plogy no hace ese hype. Aquí cada ronda la gana quien la gana según los datos publicados: Duet gana 3 de 5, Muse gana en precio y Dots en disponibilidad desde Latinoamérica. Quitamos la ronda del "cerebro" (modelo) porque no hay una prueba independiente que compare a los cuatro; el modelo de cada uno queda en el cartel (lámina 2). No usamos frases de testers de la referencia (Dan Shipper, Peter Yang): no aparecen en el anuncio de Anthropic y no las pudimos verificar.

**Criterio propio de Plogy (lámina 9):** ningún agente ordena un negocio desordenado. Antes de elegir cuál, hay que decidir qué tareas le entregas, quién aprueba y qué no se toca nunca. Con eso claro, cualquiera rinde; sin eso, ninguno. Sigue la línea de las piezas 001 y 020 (automatizar el desorden).

## Secuencia

| # | Lámina |
|---|---|
| 1 | Portada: las 4 imágenes oficiales + "4 agentes que trabajan mientras duermes." |
| 2 | El cartel: nombre, empresa, fecha y modelo de cada uno |
| 3 | Ronda 1 · Precio: gana Muse |
| 4 | Ronda 2 · El trabajo: para un negocio, gana Duet |
| 5 | Ronda 3 · Apps: 6.000+ contra 4.000+, gana Duet |
| 6 | Ronda 4 · Dónde usarlo: desde Latinoamérica, gana Dots |
| 7 | Ronda 5 · Confianza: aprobaciones y bloqueos de Duet |
| 8 | Veredicto: Duet 3 de 5 + dónde pierde |
| 9 | Criterio de Plogy (naranja) |
| 10 | CTA: Comenta AGENTE |

## Datos y fuentes primarias

| Dato | Fuente |
|---|---|
| Claude Duet: 21 oct 2026, vista previa por lista de espera, Pro y Max en EE. UU., iOS, Android y claude.ai, Claude Opus 5.5, más de 6.000 conectores y plugins, ejemplos QuickBooks/Stripe/Gusto/DocuSign/Shopify, pide aprobación antes de enviar, pagar, firmar o borrar, bloquea operar en bolsa y mover dinero entre cuentas, no ve contraseñas, usa los límites del plan, no deja ver su navegador, puede equivocarse con lo urgente | claude.com/resources/articles/claude-duet |
| Duet: bloquea entrar a la cuenta de otra persona; solo EE. UU.; Team y Enterprise no incluidos | support.claude.com/en/articles/17631495-get-started-with-claude-duet |
| Claude Pro: 20 dólares al mes (EE. UU.) | claude.com/pricing, support.claude.com/en/articles/8325606 |
| Dots: 29 sep 2026, GPT-6 Astra, computador propio en la nube, más de 4.000 apps | openai.com/index/introducing-dots, notas de versión de ChatGPT |
| Dots: Pro (18+) fuera del EEE, Suiza y Reino Unido; Business Premium en regiones soportadas; despliegue gradual | help.openai.com/en/articles/20001530-getting-started-with-your-dot |
| ChatGPT Pro desde 100 dólares | help.openai.com/en/articles/20001354 (Pro $100 y Pro $200) |
| Muse: 8 sep 2026, EE. UU., iOS, Android, muse.ai y WhatsApp, Muse Spark, gratis para lo básico con planes pagos, ejemplos (viajes, negociar, entreno, lista del mercado desde un reel), pide permiso antes de enviar un correo o comprar, no ve contraseñas | about.fb.com/news/2026/09/introducing-muse-personal-ai-agent |
| Grok Bot: agosto, "durable AI teammates" en un computador persistente en la nube | docs.x.ai/developers/release-notes |
| Grok Bot: Premium 30, Super 100, Ultra 200 dólares al mes | x.ai/bot (leído vía buscador; la página bloqueó la lectura directa) |

## Dudas y decisiones

- **Grok Bot, fecha exacta:** las notas de versión de xAI solo dicen "agosto". Medios secundarios dan el 11 de agosto; en la lámina queda "agosto".
- **Grok Bot, modelo y regiones:** xAI no los publica en sus notas. Quedan "Modelo no publicado" y "Sin dato".
- **Precios de Muse:** Meta no da montos; medios citan 20 y 100 dólares. Solo usamos "gratis para lo básico".
- **"Gana Duet" en confianza:** Muse también pide permiso y no ve contraseñas (se dice en la lámina 7). Duet gana la ronda por publicar una lista explícita de acciones bloqueadas aunque se aprueben; es criterio de Plogy, no un dato de las empresas.
- **"Dots llega aquí":** confirmado por regiones excluidas (EEE, Suiza, Reino Unido). El despliegue es gradual, así que puede no estar aún en todas las cuentas.

## Imágenes y logos

Los logos, íconos y mascotas son los oficiales de cada producto, tomados de sus páginas de lanzamiento (originales en `assets/originales/`):

| Archivo | Origen |
|---|---|
| `av-duet.svg`, `kv-duet.jpg` | claude.com/product/claude-duet (ícono de la app e imagen para compartir) |
| `av-dots.jpg`, `kv-dots.jpg` | openai.com/index/introducing-dots (imagen principal con las mascotas) |
| `av-muse.jpg`, `kv-muse.jpg` | about.fb.com, anuncio de Muse (imagen para compartir; el avatar es la mascota recortada) |
| `av-grok.jpg`, `kv-grok.jpg` | x.ai/bot (imagen para compartir; el avatar es el ícono recortado) |

Uso editorial y comparativo: se nombra y se muestra cada producto tal cual, sin alterar los logos. La tarjeta "Necesita tu OK" de la lámina 7 sigue siendo una maqueta rotulada "Ilustración".

## Pendientes antes de publicar

- Publicar la guía (`guia.md`) en un enlace y configurar la respuesta automática a AGENTE.
- Volver a revisar precios y disponibilidad el día de publicar: los cuatro están en despliegue.
- Uso de logos e imágenes de terceros: revisar las guías de marca de Anthropic, OpenAI, Meta y xAI antes de publicar (en contenido editorial suele estar permitido, pero no lo verificamos).
- Derechos de la foto `assets/10-foco.jpg` (variante 10 de la biblioteca): `unverified_reference_only`.
- Licencias tipográficas, prueba en móvil, revisión editorial independiente y aprobación humana con fecha.
