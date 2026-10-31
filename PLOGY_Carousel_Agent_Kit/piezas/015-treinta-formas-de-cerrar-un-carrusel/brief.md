# Pieza 015 · 30 formas de cerrar un carrusel

Estado: BORRADOR PARA REVISIÓN HUMANA. No publicar.

Pieza documental (Building Plogy): cuenta qué se hizo en la biblioteca de CTAs de `piezas/cta-biblioteca/` y qué se corrigió al mirarla. No hay reporte ni DM: el CTA es de comunidad y su entrega es `comunidad.md`. Los textos por canal están en `textos.md`.

## Oportunidad

- ID y estado editorial: 015 · borrador completo (carrusel, textos, comunidad.md), pendiente de revisión humana.
- Tipo de origen: trabajo propio de Plogy ya hecho y archivado en el kit (biblioteca de 30 variantes de CTA para el último slide, con su catálogo, su script de derivados y un script de correcciones). Sin noticia ni fuente externa.
- Fuente primaria, fecha y enlace o registro interno: registro interno, archivos del kit. Fechas de archivo: 2026-10-20 (derivados, primeros exports, script de correcciones, exports corregidos y catálogo). Ver tabla de evidencia. Solo se afirma lo que se pudo comprobar abriendo esos archivos.
- Qué afirma la fuente y qué queda sin verificar:
  - Verificado en los archivos: que existen 30 variantes, su reparto por tipo (10 seguimiento, 6 comunidad, 8 recurso, 6 comercial), las 30 fotos y su tratamiento de color (11 con mapa de color, 6 con los rojos llevados al naranja), las 14 variantes que recibieron correcciones y de qué tipo, y que de 8 variantes de recurso solo 3 tienen detrás un borrador de recurso.
  - No existe: ningún resultado de publicación. Ninguna variante se ha publicado ni medido. La pieza no dice cuál funciona mejor.
  - No existe como imagen: los "antes" de las correcciones. Las láminas muestran los "después" (los PNG finales) y los "antes" se describen con texto.
  - Sin verificar: quién hizo cada paso y en qué orden exacto (el kit no lo registra por persona). La redacción en primera persona del plural ("armamos", "tuvimos que corregir") la confirma Plogy.
  - Discrepancia detectada y no usada: `skills/plogy-cta-design/SKILL.md` habla de "26 fotos distintas y 14 composiciones". Los archivos dan 30 fotos y 27 descripciones de composición distintas en `CATALOGO.md`. La pieza no usa esas dos cifras. El "14" de la pieza es otro dato: las variantes corregidas.
- Audiencia: Ambos (negocios que cierran carruseles y Ploggers que construyen piezas).
- Vertical: Redes sociales.
- Pilar principal: Documental (subcategoría Building Plogy).
- Pilar secundario: Conocimiento (cuatro criterios aplicables a cualquier último slide).
- Subcategoría y confianza de clasificación: Building Plogy · confianza alta en el pilar principal, porque cuenta algo que ocurrió y quedó archivado; media en la autoría exacta de cada paso.
- Tesis de Plogy en una frase: un final de carrusel se diseña, se mira y se corrige; lo que falló en nuestros 30 se vio al mirar los renders, y de ahí salieron cuatro comprobaciones.
- Problema o tensión que hace relevante la pieza: el último slide suele tratarse como un trámite y es donde se pide la acción. En 14 de 30 hubo algo que corregir antes de poder usarlo.
- Ángulo distintivo y por qué Plogy puede decirlo: Plogy tiene la biblioteca hecha, con sus correcciones y sus requisitos escritos. Es evidencia propia, no una opinión sobre cómo cerrar carruseles.
- Objetivo: comunidad (que la gente elija una variante por su número y cuente por qué).
- Término principal de búsqueda y términos secundarios reales: "cómo cerrar un carrusel de Instagram". Secundarios: "CTA para carruseles", "llamada a la acción en un carrusel", "último slide de un carrusel". No se afirma nada sobre su volumen de búsqueda.
- CTA del último slide y estado del recurso prometido: "¿Cuál usarías para cerrar tu carrusel? Comenta Plogy y dinos el número." No promete recurso. Requiere que una persona de Plogy responda los comentarios (ver `comunidad.md`). Palabra clave de comunidad: Plogy (la que usa la variante 11 de la biblioteca; no hay DM ni automatización).

Por qué este tema: pedido de una pieza documental sobre lo construido en Plogy. Los hechos están en archivos que cualquiera puede abrir, no dependen de memoria ni de métricas.

## Tabla de evidencia (cada dato y su archivo)

Rutas relativas al kit (`PLOGY_Carousel_Agent_Kit\`).

| # | Dato en la pieza | Dónde se verificó | Cómo se comprobó | Estado |
| --- | --- | --- | --- | --- |
| 1 | Existen 30 variantes de CTA | `piezas/cta-biblioteca/ctas.html`, `exports/cta-01.png` a `cta-30.png`, `CATALOGO.md` | 30 secciones `class="slide vNN"` en el HTML, 30 PNG en `exports/`, 30 filas en el catálogo | Verificado |
| 2 | 10 seguimiento, 6 comunidad, 8 recurso, 6 comercial | `piezas/cta-biblioteca/CATALOGO.md`, tabla "Catálogo" (columna Tipo) | Conteo por tipo de las 30 filas | Verificado |
| 3 | 30 fotos, una por variante | `piezas/cta-biblioteca/assets/` (30 .jpg), `scripts/derive.py`, `assets/reference-catalog.csv` | `derive.py` procesa 28 originales distintos (28 hashes sha256 distintos en el catálogo de referencias) y copia 2 derivados ya hechos: `27-portal.jpg` (pieza 001, `cta-b-portal.jpg`) y `30-pc-viejo.jpg` (pieza 004, `01-pc-viejo.jpg`) | Verificado |
| 4 | 11 fotos con mapa de color a la paleta | `derive.py` (llamadas a `gradient_map`) y `CATALOGO.md` ("Fotos tratadas") | Variantes 03, 04, 09, 10, 12, 13, 15, 16, 21, 23, 26. Los comentarios de `derive.py` dicen que los colores originales eran azul, verde o amarillo | Verificado |
| 5 | 6 fotos con los rojos llevados al naranja | `derive.py` (llamadas a `shift_reds`) y `CATALOGO.md` | Variantes 14, 18, 20, 22, 24, 28 | Verificado |
| 6 | Las otras 13 no pasan por esos dos tratamientos | `derive.py`, `CATALOGO.md` | 11 sin tratamiento (01, 02, 05, 06, 07, 08, 11, 17, 19, 25, 29), más 27 y 30, copiados de piezas 001 y 004 (la 30 ya viene en gris cálido con la pantalla en naranja, según el catálogo) | Verificado. La pieza dice solo "17 de 30 pasaron por un tratamiento de color" |
| 7 | 14 variantes recibieron correcciones | `scripts` de correcciones: copia en `evidencia/fix_ctas.py` (original en el scratchpad de la sesión, fuera del kit) | El script toca las variantes 06, 07, 10, 11, 13, 17, 18, 20, 21, 23, 25, 26, 28 y 29 (14). Se comprobó que los cambios están aplicados en `ctas.html` (reglas `.hl{color:#fff}` en 06, 10, 18, 20, 21 y 29; sombra `.v13/.v26/.v28 .shade`; logo `plogy-black.svg` en la 23; foto de la 11 en `top:130px`). Los exports de la 11 son posteriores al script | Verificado |
| 8 | En 6 variantes el titular naranja pasó a blanco (06, 10, 18, 20, 21, 29) | `evidencia/fix_ctas.py`, `ctas.html` | Reglas `.vNN .hl{color:#fff;text-shadow:none}` presentes en las seis. Es un juicio visual, no una medición de contraste | Verificado (juicio visual) |
| 9 | 5 correcciones por el logo: sombra superior en 13, 26 y 28; foto bajada en 11; logo negro sobre naranja en 23 | `evidencia/fix_ctas.py`, `ctas.html` | Reglas y HTML presentes. El logo de la 11 sigue rozando el borde de la foto en el export (se aprecia en la lámina 05 y en `exports/cta-11.png`) | Verificado |
| 10 | Otras 3 correcciones de composición (07: texto sin chocar con las esferas y titular nuevo; 17: salto de línea; 25: separación de la nota). No se cuentan como lecciones | `evidencia/fix_ctas.py` | Suman con los grupos 8 y 9 las 14 variantes | Verificado |
| 11 | De 8 CTAs de recurso, 3 tienen detrás un borrador: MEDIR (19), MIGRAR (20), COSTO (21) | `CATALOGO.md`, sección "Requisitos antes de publicar cada tipo"; `piezas/005-.../brief.md`, `piezas/004-.../brief.md`, `piezas/003-.../brief.md` (existen `reporte.md` y `dm.md` en las tres) | Los tres briefs dicen "El recurso está en borrador, no publicado. El DM no está configurado" | Verificado: existen como borrador, ninguno publicado |
| 12 | Las otras 5 no tienen recurso: PROMPT (17), GUIA (18), AUDITORIA (23) son "ejemplo por preparar"; MAPA (22) está descrito en la pieza 001 y "no preparado"; BANCO (24) apunta a una noticia con reporte propio y la pieza 002 no tiene reporte | `CATALOGO.md` (sección de requisitos), carpeta `piezas/002-bancos-frenan-agentes-ia/` sin `reporte.md`, `brief.md` de 002 ("No promete recurso") | Lectura de archivos y listado de carpetas | Verificado |
| 13 | Ninguna variante se ha publicado ni medido | `CATALOGO.md` ("Son plantillas, no piezas publicadas"; "Aprobación humana: pendiente"); no hay ningún archivo de resultados en el kit | Búsqueda de datos de rendimiento: ninguno | Verificado por ausencia. Plogy confirma que no se publicó fuera del kit |
| 14 | Variante 11: comunidad, "foto en banda y maqueta de comentario", foto `a company at work.jpg`, sin tratamiento | `CATALOGO.md`, `ctas.html` (`.v11`), `exports/cta-11.png` | Lectura directa. La foto de origen mide 1044 x 588 y se usa a 1080 x 608 | Verificado |
| 15 | Las 56 imágenes del catálogo de referencias tienen derechos `unverified_reference_only` | `assets/reference-catalog.csv` (columna `rights_status`) | Conteo | Verificado. Aplica a las 30 fotos |
| 16 | Los "antes" no existen como imagen | El kit no contiene capturas previas a las correcciones | Búsqueda en `piezas/cta-biblioteca/` | Verificado por ausencia. Plogy confirma que no hay copias fuera del kit |
| 17 | La biblioteca se hizo y corrigió el 2026-10-20 | Fechas de modificación de `derive.py`, `exports/`, `ctas.html`, `CATALOGO.md` y del script de correcciones | Lectura de fechas de archivo | Verificado como fecha de archivo, no como relato de quién hizo qué |

Lo que NO se afirma en la pieza: qué CTA rinde mejor, cuánta gente interactúa con cualquiera de ellos, que las correcciones "mejoraron" un resultado, ni cuánto tiempo costó hacerlo.

## Secuencia (7 láminas)

| Slide | Función narrativa | Titular | Texto de apoyo | Qué aporta al siguiente | Imagen y razón | Composición | Fuente de la afirmación |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | Tensión | Armamos 30 formas de cerrar un carrusel. | 14 hubo que corregirlas. Esto fue lo que falló. | ¿Cuáles son las 30? | Mosaico de 12 PNG reales de la biblioteca, oscurecido (`assets/hoja-portada.png`) | Fondo Ink, mosaico abajo | Filas 1 y 7 |
| 02 | Qué hicimos | 30 finales, cuatro tipos. | Leyenda con 10, 6, 8 y 6. Pie: Ninguna se ha publicado ni medido. | ¿Qué falló? | Hoja de contacto de las 30, con número y color por tipo (`assets/hoja-30.png`) | Fondo superficie, leyenda y cuadrícula | Filas 1, 2, 13 |
| 03 | Lección 1 | Una foto fuera de marca va a la paleta. | 17 de las 30 fotos pasaron por un tratamiento de color. 11 con mapa (azul, verde, amarillo), 6 con rojos llevados al naranja. | Otro fallo: el titular | Dos hojas de contacto (`assets/hoja-mapa.png`, `hoja-rojos.png`) | Fondo Ink | Filas 4 y 5 |
| 04 | Lección 2 | Naranja sobre foto naranja, el titular se pierde. | En 6 variantes el titular pasó a blanco. Solo guardamos el después, no el antes. | Otro fallo: el logo | Hoja de contacto de las 6 (`assets/hoja-titulares.png`) | Fondo superficie | Fila 8 y 16 |
| 05 | Lección 3 | Sobre una foto ocupada, el logo se pierde. | 5 correcciones: sombra arriba en 13, 26 y 28, foto más abajo en 11 y logo negro sobre naranja en 23. | Otro fallo: prometer sin tener | Recortes de la zona del logo de los PNG reales (`assets/hoja-logos.png`) | Fondo Ink | Fila 9 |
| 06 | Lección 4 | Un CTA de recurso solo sirve si el recurso existe. | Lista de 8 con "Borrador" o "No existe". De 8, solo 3 tienen algo detrás, y ninguno está publicado. | Pregunta | Sin foto. Lista tipográfica | Fondo superficie | Filas 11 y 12 |
| 07 | CTA comunidad | ¿Cuál usarías para cerrar tu carrusel? | Comenta Plogy y dinos el número. Ninguna se ha publicado ni medido todavía. | Cierre | Variante 11 de la biblioteca: foto en banda (derivado `11-reunion.jpg`) y maqueta de comentario con "Plogy" y "y el número" | Fondo Ink | Filas 13, 14 |

Notas de diseño:
- Los "antes" no se dibujan. Las láminas 04 y 05 lo dicen en texto ("Solo guardamos el después"). Los recortes de la 05 son de los PNG finales.
- Para poder responder "dinos el número", cada miniatura de las hojas lleva su número de variante (01 a 30), con color por tipo en la hoja de las 30. Los números se dibujan encima con Pillow, en la esquina superior derecha, y no son parte de los PNG originales.
- La variante 11 se adaptó: foto bajada a `top:176px` para que el logo caiga entero sobre Ink; el titular y la nota son de esta pieza; el campo de comentario muestra "Plogy" escrito y el texto tenue "y el número"; se añaden contador y puntos; la nota incluye el aviso de que nada se ha publicado ni medido (un solo pedido de acción: comentar).

## Textos por canal

Ver `textos.md` (caption de Instagram con hashtags y su razón, post de LinkedIn y diferencia de enfoque) y `comunidad.md` (quién responde, tres respuestas modelo, comentarios fuera de tema).

## Estado del flujo (checklist de salida, versión comunidad)

- [x] Cada afirmación material tiene archivo de origen (tabla de evidencia) y lo no verificado está escrito.
- [x] Ninguna cifra de rendimiento: la pieza dice que nada se ha publicado ni medido.
- [x] Los "antes" no se muestran como capturas; se describen con texto.
- [x] CTA del carrusel, caption y comunidad.md alineados: comentar Plogy y decir el número.
- [x] La pieza no promete ningún recurso.
- [ ] Redacción en primera persona del plural confirmada por Plogy ("armamos", "tuvimos que corregir").
- [ ] Persona de Plogy asignada para responder los comentarios (ver `comunidad.md`) y ventana de respuesta definida.
- [ ] Plogy confirma que no existen capturas del antes ni datos de publicación fuera del kit.
- [ ] Derechos de las 30 fotos de las hojas de contacto (todas `unverified_reference_only`) y de la foto del CTA resueltos o reemplazados. Sin esto no se publica.
- [ ] Licencias de Screener y Space Grotesk resueltas.
- [ ] Revisión de las láminas en un móvil real.
- [ ] Aprobación humana con fecha.

## Revisión

- Evidencia y procedencia de cada dato: tabla de evidencia, 17 filas, todas con archivo. Dos cifras del SKILL.md de CTAs (26 fotos, 14 composiciones) no coinciden con los archivos y no se usan.
- Derechos de cada asset y licencia de la tipografía: todas las fotos de las hojas de contacto son derivados de originales `unverified_reference_only`; la lámina 02 reúne las 30. Hay tres con tono fuerte según el propio catálogo (05, 10 y 29: hongo nuclear y titulares fuertes); aparecen en miniatura en la lámina 02, y la 10 y la 29 también en la lámina 04. Screener solo tiene licencia demo y Space Grotesk se carga desde Google Fonts: falta confirmar licencia comercial.
- Legibilidad a tamaño móvil: revisada a simple vista en los PNG. Las miniaturas de las hojas son pequeñas a propósito (son evidencia, no se leen sus textos); lo legible son los números, de unos 40 px, y los titulares. Apoyos de 36 a 38 px; notas de pie de 32 px; filas de la lámina 06 con notas de 32 px. Pendiente confirmar en un móvil real.
- Coherencia entre tesis, secuencia, caption y CTA: la tesis (los fallos se vieron al mirar los renders y de ahí salieron cuatro comprobaciones) se apoya en las cuatro lecciones. El CTA de láminas, caption y comunidad.md es el mismo.
- Verificación de estilo: sin guiones largos, sin emojis en LinkedIn, hashtags de Instagram ≤ 5, sin las muletillas de la lista prohibida (revisado con búsqueda de texto).
- Riesgos de la pieza:
  1. "Armamos" y "tuvimos que corregir" suponen autoría de Plogy; Plogy confirma.
  2. La variante 11 del carrusel no es la 11 de la biblioteca copiada: tiene otro titular, otra nota y la foto en otra posición. El número "11" de la biblioteca sigue siendo el mismo diseño base.
  3. Al pedir "el número", algunos comentarios elegirán una variante por la foto o por su titular, no por la función. Eso es opinión, no medición, y así se trata en `comunidad.md`.
  4. Las 30 miniaturas muestran 30 fotos con derechos sin verificar en una sola lámina; es el mayor riesgo de publicación de la pieza.
- Pendiente de aprobación humana:
  1. Confirmar la autoría en plural y que no hay datos de publicación.
  2. Asignar quién responde y cuándo.
  3. Resolver derechos de fotos o sustituirlas.
  4. Licencias de Screener y Space Grotesk.
  5. Ver las láminas en un móvil real.
  6. Aprobación y fecha.
- Aprobación humana y fecha: PENDIENTE

## Archivos de la pieza

- `carrusel.html`: fuente editable de las 7 láminas (1080x1350). Sin parámetros muestra todas; con `?s=1` a `?s=7`, una sola.
- `exports/slide-01.png` a `slide-07.png`: exportaciones en orden.
- `textos.md`: caption de Instagram, post de LinkedIn y diferencia de enfoque.
- `comunidad.md`: criterio de quién responde, tres respuestas modelo y qué hacer con comentarios fuera de tema.
- `brief.md`: este archivo. Cada `.md` tiene también su versión `.html` para el visor.
- `scripts/derive.py`: arma las hojas de contacto con Pillow a partir de `piezas/cta-biblioteca/exports/` y copia la foto del CTA. Uso: `python -I scripts\derive.py "<kit>" "<assets de la pieza>"`.
- `assets/`: `hoja-30.png`, `hoja-mapa.png`, `hoja-rojos.png`, `hoja-titulares.png`, `hoja-logos.png`, `hoja-portada.png` y `11-reunion.jpg`.
- `evidencia/fix_ctas.py`: copia del script de correcciones, que vive fuera del kit (en el scratchpad de la sesión). Se guarda aquí para que la tabla cite un archivo estable. No se ejecuta desde aquí.

## Inventario de assets

| Asset | Origen | Transformación | Lámina | Derechos |
| --- | --- | --- | --- | --- |
| `brandkit/assets/plogy-color.svg` | Brand kit Plogy | Ninguna | 02, 04, 06 | Propio de Plogy. Trazado derivado de la fuente demo, por verificar. |
| `brandkit/assets/plogy-white.svg` | Brand kit Plogy | Ninguna | 01, 03, 05, 07 | Igual que el anterior |
| `brandkit/assets/plogy-symbol.svg` | Brand kit Plogy | Ninguna (avatar de la maqueta de comentario) | 07 | Igual |
| `assets/11-reunion.jpg` | Derivado de la biblioteca `piezas/cta-biblioteca/assets/11-reunion.jpg`, a su vez de `assets/reference-originals/a company at work.jpg` (1044 x 588). Autor desconocido. | Copia sin cambios; el derivado original es un recorte a 1080 x 608 sin tratamiento de color | 07 | `unverified_reference_only`. NO publicar hasta verificar derechos. |
| `assets/hoja-30.png` | 30 PNG de `piezas/cta-biblioteca/exports/cta-01.png` a `cta-30.png` (derivan de 30 fotos `unverified_reference_only`) | Miniaturas de 248 x 310 en 6 columnas, número de variante dibujado con Pillow | 02 | `unverified_reference_only` en las 30 fotos. NO publicar hasta verificar derechos. |
| `assets/hoja-mapa.png`, `hoja-rojos.png` | PNG de las variantes 03, 04, 09, 10, 12, 13, 15, 16, 21, 23, 26 y 14, 18, 20, 22, 24, 28 | Miniaturas con número | 03 | Igual |
| `assets/hoja-titulares.png` | PNG de las variantes 06, 10, 18, 20, 21, 29 | Miniaturas de 560 x 700 con número | 04 | Igual |
| `assets/hoja-logos.png` | PNG de las variantes 13, 26, 28, 11 y 23 | Recorte de la zona del logo (x 0 a 640, y 40 a 300; la 23 a ancho completo y recorte de 156 px de alto) con número | 05 | Igual |
| `assets/hoja-portada.png` | PNG de las variantes 06, 08, 12, 15, 16, 19, 21, 23, 02, 13, 25, 18 | Mosaico 6 x 2 sin números, oscurecido en la lámina con un degradado Ink | 01 | Igual |
| Titulares, leyenda, lista de la lámina 06, maqueta de comentario | CSS y texto | Ninguna | 01 a 07 | Propio |

Los originales siguen intactos en `assets/reference-originals/`. No se usó ninguna foto fuera de la biblioteca ni de personas públicas identificables (las del catálogo se evaluaron en `CATALOGO.md`, "Personas en las fotos"). Ninguna lleva la foto "juanfra pp plogy".
