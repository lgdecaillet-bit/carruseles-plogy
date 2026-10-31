# Brief · pieza 024 · Carruseles con criterio

Estado: BORRADOR para revisión humana. No publicar. Aprobación humana y fecha: PENDIENTE.

## Qué es

Primera de una tanda de tres adaptaciones. La referencia (otra cuenta) dice que Claude hace carruseles feos porque le falta un sistema y propone 5 pasos con escenas de juguete generadas por IA. CTA de la referencia: Comenta CARRUSEL.

**Qué cambiamos:** no copiamos sus pasos. Contamos el sistema real con el que Plogy hace sus carruseles en este kit, con prueba de cada paso (archivos y piezas reales). Las imágenes no son escenas generadas: son exports de nuestras piezas, el código de una lámina y extractos de los archivos del kit.

**Criterio propio de Plogy:** un carrusel hecho con IA no falla por feo, falla por vacío. El sistema empieza por la opinión de la marca y termina en una revisión que no hace quien escribió. Es la regla del kit ("el Criterio de Plogy es lo más importante de la pieza").

## Secuencia

| # | Lámina | Prueba que se muestra |
|---|---|---|
| 1 | Portada: "Tu carrusel con IA no es feo. Le falta criterio." | Portadas reales de 019, 020, 021 y 023 |
| 2 | Paso 1: primero, qué opinas | Extracto de `023/brief.md` (audiencia, prueba, criterio) |
| 3 | Paso 2: cada dato con su fuente | Extracto de la tabla de fuentes de 023 y las dos citas que se sacaron |
| 4 | Paso 3: una skill por oficio | Las 8 carpetas reales de `skills/` |
| 5 | Paso 4: la marca en un archivo | Valores reales de `brandkit/tokens.json` |
| 6 | Paso 5: quien escribe no se califica | Los 8 criterios de la Parte B de `RUBRICA.md`, sus 10 reglas duras y los 3 veredictos |
| 7 | El truco: Claude programa las láminas | Código real de la lámina 9 de 023 (resumido con "...") y su PNG |
| 8 | CTA: Comenta CRITERIO | Tarjeta de vidrio sobre la foto 20 de la biblioteca |

## Verificación interna

- 8 skills: `skills/` tiene plogy-captions, carousel-production, content-classifier, content-planning, cta-design, editorial-review, narrative-language y visual-adaptation.
- Rúbrica: Parte B con 8 criterios, Parte C con 10 reglas duras, 3 veredictos; todo veredicto termina en revisión humana (`skills/plogy-editorial-review/`).
- Tokens: ink #171310, orange #ff5b00, surface #f4f1ef, muted #625951 (`brandkit/tokens.json`). Space Grotesk es el respaldo del display (Screener solo tiene licencia DEMO).
- Citas sacadas en 023: frases de Dan Shipper y Peter Yang de la referencia, no presentes en el anuncio de Anthropic (`023/brief.md`).
- El brief de 023 no tiene campos llamados "Audiencia" y "Prueba" con esas palabras exactas: la lámina 2 los resume a partir de su contenido. Se rotula como extracto del archivo.

## CTA y recurso

Comenta CRITERIO → DM con `skill-base.md`, una versión simplificada del kit en una sola skill, con corchetes para la marca de quien la usa. Se eligió CRITERIO en vez de CARRUSEL para no repetir la palabra de la referencia y porque es la idea de la pieza.

## Autor y cuentas

Cada lámina lleva al pie una barra con la foto y el usuario de JuanFra Martínez (@juanframartz). La pieza se sube en Plogy y en la cuenta personal (por ejemplo como colaboración de Instagram), con la misma versión. La foto sale del perfil de Instagram (`assets/av-autor.png`).

## Pendientes antes de publicar

- Luciano decide si se comparte la skill base tal como está y dónde se aloja el enlace.
- Las portadas de la lámina 1 son de piezas que siguen en borrador: si alguna cambia o no se publica, actualizar.
- Respuesta automática para CRITERIO.
- Derechos de las fotos de la biblioteca usadas en las láminas 2, 3 y 8 (`02-camara.jpg`, `03-ojos.jpg`, `08-teclado.jpg`, variantes 19, 09 y 20): `unverified_reference_only`.
- Licencias tipográficas, prueba en móvil, revisión editorial independiente y aprobación humana con fecha.
