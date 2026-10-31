# Calibración del revisor editorial

Aquí se compara lo que dice el revisor con lo que opina la persona de Plogy que decide. Sirve para ajustar las anclas de `RUBRICA.md` cuando difieran.

Cómo usarlo: después de cada revisión (`piezas/NNN/revision-editorial.md`), quien decide anota su veredicto y lo que le pareció acertado o equivocado en el informe.

| Pieza | Veredicto del revisor | Veredicto de la persona | Fecha | Dónde discrepan | Ajuste a la rúbrica |
| --- | --- | --- | --- | --- | --- |
| 001 | Mejorar antes de seguir | | 2026-10-20 | | |
| 002 | Mejorar antes de seguir | | 2026-10-20 | | |
| 003 | Mejorar antes de seguir (falla regla dura 10) | | 2026-10-20 | | |
| 004 | Mejorar antes de seguir | | 2026-10-20 | | |
| 005 | Publicar con ajustes | | 2026-10-20 | | |

## Reglas para ajustar

- Si la persona y el revisor discrepan en un criterio dos veces o más, se reescribe la ancla de ese criterio.
- Una discrepancia aislada se anota, pero no cambia la rúbrica.
- Cada ajuste se registra con fecha y motivo. No se borra el historial.

## Primera pasada (2026-10-20), notas del autor del kit

- Cinco revisores independientes, uno por pieza, con la misma rúbrica y sin ver el razonamiento del autor.
- Hallazgo confirmado a mano: la pieza 003 rotula "razonamiento alto" para todos los modelos, y la fuente (AIHubMix) pone Argon en "high", GPT-6 Astra en "max" y no indica nivel para Sonnet 5.5 ni Opus 5.5.
- Inconsistencia entre revisores a corregir en la rúbrica: la pieza 004 recibió CTA 3 porque el recurso sigue en borrador, y la 005, en la misma situación, recibió CTA 4. Falta una regla explícita para "recurso en borrador".
- Un revisor (004) dijo no haber podido leer fuentes de terceros que el autor sí leyó: los informes separan lo verificado de lo no verificado, pero no prueban que el autor mintiera.
- Pendiente: que la persona que decide anote su veredicto y dónde discrepa.
