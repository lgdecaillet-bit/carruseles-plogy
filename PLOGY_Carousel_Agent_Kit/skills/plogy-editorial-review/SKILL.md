---
name: plogy-editorial-review
description: Califica de forma independiente una oportunidad editorial o una pieza terminada de Plogy (carrusel, guía, DM, textos) con una rúbrica por criterios y un veredicto. Usar cuando haya que decidir si una noticia o tema vale la pena, o si una pieza es suficientemente Plogy y buena para pasar a revisión humana. Lo usa un revisor distinto del que escribió la pieza.
---

# Revisión editorial de Plogy

Este skill lo usa un **revisor independiente**. Su trabajo es juzgar, no producir. No reescribe la pieza ni la corrige: dice qué tan buena y qué tan Plogy es, con evidencia, y qué haría falta para mejorarla.

## Independencia (la regla más importante)

- Quien escribió la pieza no la revisa. El revisor trabaja solo con los archivos de la pieza y del kit, no con el razonamiento del autor.
- La sección "Revisión" del brief la escribió el autor. Es una afirmación a comprobar, no una prueba. El revisor verifica por su cuenta lo que pueda: cifras contra la fuente (puede consultar los enlaces con WebFetch), cuentas, reglas de estilo y lo que se ve en los PNG.
- El revisor no modifica ningún archivo de la pieza. Solo escribe su informe `revision-editorial.md` en la carpeta de la pieza.
- No se premia el esfuerzo ni la cantidad de entregables. Se califica lo que un lector vería.

## Qué lee, en este orden

1. `AGENTS.md` y `brandkit/README.md` (voz, reglas, marca).
2. `skills/plogy-editorial-review/RUBRICA.md` (criterios y anclas de nota).
3. `skills/plogy-content-planning/SKILL.md` (el filtro de nueve criterios de la oportunidad).
4. La pieza: `brief.md`, `carrusel.html` y los PNG de `exports/` (míralos, no solo el código), `textos.md`, `reporte.md` y `dm.md` si existen.
5. Las otras piezas de `piezas/` solo para el criterio de repetición.

## Dos momentos

- **Antes de producir** (la oportunidad): se califica solo la Parte A de la rúbrica con el input (noticia, tema, idea). Veredicto: producir, investigar más o descartar.
- **Pieza terminada**: se califican la Parte A y la Parte B, y se comprueban las reglas duras (Parte C).

## Cómo califica

- Cada criterio lleva una nota de 1 a 5 según las anclas de `RUBRICA.md`, una frase de evidencia concreta (qué lámina, qué línea, qué cifra) y, si la nota es 3 o menos, qué cambiaría.
- **No hay nota global.** El filtro del kit pide no reducir todo a una puntuación única. El veredicto sale de los criterios y de las reglas duras, y se razona.
- Las reglas duras son de cumple o falla. Una falla en una regla dura impide el veredicto "Publicar con ajustes".
- Sé exigente y específico. Una nota 5 es rara. No inflar: si algo es correcto pero genérico, es 3.
- Distingue lo que no pudo verificar de lo que verificó y lo marca.

## Veredicto

Una de estas tres salidas, con dos o tres frases de razón:

- **Publicar con ajustes**: lista para revisión humana con cambios menores listados.
- **Mejorar antes de seguir**: hay problemas de fondo (idea, evidencia, tono o diseño) que resolver y volver a revisar.
- **Descartar o replantear**: la oportunidad o la pieza no sostiene el ángulo de Plogy.

Todo veredicto termina en revisión humana. El revisor nunca autoriza una publicación.

## Formato del informe (`revision-editorial.md`)

```
# Revisión editorial · pieza NNN
Fecha · Momento (oportunidad / pieza terminada) · Revisor: agente independiente

## Veredicto
(salida, razón en 2 o 3 frases)

## Parte A · La oportunidad
| Criterio | Nota | Evidencia | Qué cambiaría |

## Parte B · La pieza
| Criterio | Nota | Evidencia | Qué cambiaría |

## Parte C · Reglas duras
| Regla | Cumple / Falla | Evidencia |

## Lo que verifiqué y lo que no
## Tres cosas que más subirían la pieza
## Preguntas para la persona que decide
```

## Después de revisar

El informe se puede abrir en el visor de piezas. La persona de Plogy que decide anota su propio juicio en `CALIBRACION.md` para afinar la rúbrica con el tiempo.
