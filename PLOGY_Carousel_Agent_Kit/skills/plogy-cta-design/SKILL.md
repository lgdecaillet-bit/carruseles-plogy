---
name: plogy-cta-design
description: Diseñar el CTA del último slide de un carrusel Plogy con tarjeta de vidrio, foto de la biblioteca detrás y una sola acción con motivo en voz Plogy. Usar al diseñar o variar el cierre de un carrusel; incluye 6 variantes ya hechas y el proceso para reproducirlas.
---

# Diseño del CTA de último slide

El último slide de todo carrusel Plogy lleva un CTA claro. Esta skill documenta el formato desarrollado en la pieza 001 ("Automatizar el desorden"): tarjeta de vidrio oscura sobre una foto de la biblioteca, titular de síntesis y una sola acción con una línea de motivo.

Lee primero `METODOLOGIA.md` de esta carpeta. Es el registro completo del proceso, los valores de diseño, los errores encontrados y cómo reproducirlo.

## Reglas

1. Una sola acción: seguir, comentar una palabra o escribir por DM. Nunca dos.
2. Acción más motivo en voz Plogy (joven, precisa, directa, anti humo). El motivo habla de lo que Plogy hace. Sin promesas de resultado, sin guiones largos, sin muletillas de IA (`skills/plogy-captions/SKILL.md`).
3. Un CTA de recurso por DM exige que el recurso exista y que la entrega esté configurada. Una oferta comercial exige que Plogy confirme qué ofrece.
4. La foto sale de `assets/reference-originals/`, se elige por función narrativa, y se trabaja siempre en un derivado. El original no se toca. Todo el moodboard es `unverified_reference_only`: marca los derechos como pendientes.
5. Texto, logo y CTA por delante de la foto. La tarjeta cubre solo una parte de la foto, nunca el sujeto.
6. Los referentes de `reference/inspiracion/` son de terceros. Sirven para entender el formato, no se copian marcas, frases ni composiciones.
7. Nada se publica desde este paquete. Revisión humana antes de publicar.

## Variantes ya hechas (pieza 001)

| Var | Tipo | Acción | Foto original |
| --- | --- | --- | --- |
| A | Seguimiento | Sigue a Plogy | `perfection.jpg` |
| B | Seguimiento | Sigue a Plogy, centrado y grande | `cross the portal.jpg` |
| C | Comunidad | Comenta Plogy | `being different.jpg` |
| D | Recurso | Comenta MAPA | `tem coding.jpg` |
| E | Comercial | Escríbenos PROCESO | `creative working.jpg` |
| F | Seguimiento con gancho | Sigue a Plogy | `explosion.jpg` |

Fuente editable: `piezas/001-automatizar-el-desorden/cta-variantes.html` (B a F) y `carrusel.html` (A). Exportaciones: `piezas/001-automatizar-el-desorden/exports/cta/`. Estado, copys y derechos: `piezas/001-automatizar-el-desorden/brief.md`.

## Biblioteca de 30 variantes más (2026-10-20)

`piezas/cta-biblioteca/` tiene 30 CTAs listos para reutilizar, con 30 fotos (28 derivadas de la biblioteca de referentes y 2 reutilizadas de las piezas 001 y 004) y composiciones variadas: seguimiento (01 a 10), comunidad (11 a 16), recurso (17 a 24) y comercial (25 a 30). Catálogo con copy, foto original, tratamiento y requisitos: `piezas/cta-biblioteca/CATALOGO.md`. Fuente: `ctas.html`. Se ven en `piezas/visor.html` (pestaña CTA). Las palabras clave son de ejemplo.

## Flujo CTA con reporte por DM (propuesta)

Para noticias con reporte propio en la web ("Comenta BANCO y te mandamos la noticia completa y nuestro análisis"), ver `FLUJO-REPORTE-DM.md`. Está en propuesta y no se ha construido: no lo apliques a una pieza sin aprobación.

## Flujo corto

1. Lee el brief de la pieza e identifica objetivo y síntesis final.
2. Elige tipo de CTA y redacta acción y motivo.
3. Elige la foto mirándola (no solo por el nombre). Crea el derivado con `scripts/derive-*.py` como modelo.
4. Copia `reference/snapshot-pieza-001/cta-variantes.html` a la pieza, ajusta rutas y copys, y ajusta el degradado de protección a tu foto.
5. Exporta con `scripts/render-slides.ps1`. Abre cada PNG y revisa con la lista de errores de `METODOLOGIA.md`, sección 8.
6. Registra variante, copy, foto, transformación, derechos y pendientes en el brief de la pieza. Alinea el final del caption y del LinkedIn con la acción elegida.
