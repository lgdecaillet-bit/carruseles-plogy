---
name: plogy-content-classifier
description: Clasificar una referencia u oportunidad de Plogy por territorio, pilar editorial, audiencia y vertical antes de planear contenido. Usar para decidir qué es la pieza; no redacta el carrusel.
---

# Clasificador de contenido Plogy

Clasifica según el valor principal de la pieza, no por palabras aisladas. Si no tiene relación razonable con implementación de IA, capacidad de personas y negocios, Web, redes sociales, construcción de Plogy o criterio para decidir, marca `FUERA_DE_TERRITORIO`. No fuerces un vínculo.

## Pilares

| Pilar | Pregunta | Valor dominante | Señales |
| --- | --- | --- | --- |
| Filosofía | ¿Qué creemos? | Postura, interpretación o principio. | Tensión cultural, opinión argumentada, adopción, trabajo, creatividad, futuro del talento. |
| Conocimiento | ¿Cómo funciona o cómo se hace? | Comprensión aplicable. | Mecanismo, caso de uso, herramienta, noticia explicada, framework, proceso, comparación, implementación o análisis. |
| Documental | ¿Qué estamos haciendo? | Observar a Plogy, clientes o comunidad haciendo algo real. | Decisión, reunión, demo, error, experimento, evento, resultado o avance verificable. |

Una pieza sobre ChatGPT no es automáticamente Conocimiento. La presencia del equipo no la vuelve Documental. Un caso real puede apoyar una postura sin ser la historia principal. Asigna **un pilar principal** y **cero o un pilar secundario distinto**. El principal responde a por qué la pieza sería interesante incluso si se quitara la otra dimensión.

Documental requiere personas o acciones reales y contexto temporal. Una idea sobre lo que Plogy *podría* hacer no es Documental. Las subcategorías documentales son Building Plogy, Building for Clients, Building Ploggers, Building Community y Equipo.

## Campos adicionales

- Relación con el mensaje central: directa, indirecta, débil o nula. Relación nula implica fuera de territorio.
- Audiencia: Negocios, Ploggers o Ambos. Elige Ambos solo si la misma idea sirve a los dos grupos.
- Vertical: IA y automatizaciones, Web, Redes sociales o Transversal.
- Confianza: alta, media o baja. Usa baja cuando falta contexto; no lo inventes.
- Subcategoría y tesis en una frase.

Devuelve una clasificación breve con una justificación de hasta dos frases. La clasificación no es una puntuación de viralidad ni una recomendación de publicación. Para casos ambiguos, consulta `../../source-documents/plogy-content-classifier-source.txt`.
