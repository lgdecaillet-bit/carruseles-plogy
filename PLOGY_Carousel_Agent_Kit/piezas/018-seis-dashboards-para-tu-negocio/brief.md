# Brief · pieza 018 · Seis dashboards para tu negocio

Estado: BORRADOR para revisión humana. No publicar. Aprobación humana y fecha: PENDIENTE.

## Qué es

Carrusel de 8 láminas (formato guía + CTA de evento). Luciano compartió como referencia un carrusel de otra cuenta: un dashboard por lámina, fondo oscuro con brillos de color y CTA de palabra clave para recibir un prompt. Se tomó el formato, no el contenido.

**Criterio propio de Plogy:** cada dashboard parte de la pregunta de negocio que responde y de los datos que necesita. Tesis de portada: "Si no tienes la pregunta, no necesitas el dashboard."

## Diferencias con la referencia

- Sin "en 5 minutos": es una promesa que no podemos sostener (depende de los datos de cada negocio).
- Titular de cada lámina = una pregunta, no una categoría.
- Línea "Necesitas:" con los datos de entrada en cada dashboard.
- Dashboards de caja, operaciones y gasto en IA (este último conecta con las piezas 003 y 016).
- Maquetas propias en HTML/SVG con la paleta de marca (naranja y degradado Plogy). No se usan capturas de terceros ni el logo de Claude.
- Sin tarjeta de persona: firma la marca.

## Secuencia

| # | Lámina | Pregunta |
|---|---|---|
| 1 | Portada: collage de dashboards + titular | 6 dashboards que le puedes pedir a Claude |
| 2 | Ejecutivo | ¿Cómo va el negocio este mes? |
| 3 | Ventas | ¿Quién llega a la meta y quién no? |
| 4 | Caja | ¿Te alcanza la caja para el próximo mes? |
| 5 | Marketing | ¿Qué canal te trae clientes que pagan? |
| 6 | Operaciones | ¿Dónde se traban tus pedidos? |
| 7 | Gasto en IA | ¿Cuánto gasta tu equipo en IA, y en qué? |
| 8 | CTA: Comenta CLAUDE | Clase del jueves 22, 19:30: "te enseñamos a crear dashboards para tu negocio" + link de inscripción |

## Datos

Todos los números, nombres (Ana, Bruno, Carla, Diego, Elena), canales y montos son DATOS DE EJEMPLO; cada dashboard lo rotula. Son coherentes entre sí (por ejemplo, $2.100 / 50 clientes = $42; 14 + 9 + 22 = 45 pedidos activos; $186 / 1.240 tareas = $0,15).

Afirmación factual: que Claude puede armar un dashboard interactivo a partir de una planilla en la conversación. Comprobar con el producto vigente antes de publicar.

## CTA

Por pedido de Luciano, el CTA es el mismo de la clase (pieza 016: jueves 22, 19:30, link de inscripción por DM) con la palabra CLAUDE. Luciano definió el texto: "Te enseñamos a crear dashboards para tu negocio". Confirmar que la clase del jueves 22 cubre ese tema (la pieza 016 anuncia la misma fecha con Mods).

`prompt.md` (+ `.html`) ya no es el recurso del CTA: queda como extra opcional para el segundo mensaje del DM.

## Cómo se edita

`carrusel.html` se GENERA con `scripts/build.py` (contenido y datos de cada dashboard) y `scripts/slides.css` (estilos). No editar el HTML a mano: cambiar el script y correr `python -I scripts/build.py`. Cada dashboard es una app de 1400x880 (barra lateral, barra superior, KPIs con minigráfico, gráficos con ejes y tooltip, tablas, kanban) escalada dentro de la lámina. Tipografía de la interfaz: Inter. La versión anterior, más simple, quedó en el scratchpad de la sesión.

## Pendientes antes de publicar

- Confirmar que es la misma clase que la 016 y qué temas cubre.
- Publicar antes del jueves 22 de octubre de 2026 (mañana) o cambiar la lámina 8.
- Enlace de inscripción y flujo del DM (texto en `textos.md`).
- Validez de la palabra CLAUDE en la herramienta de comentarios (y si choca con el CTA MOD de la 016 si salen juntas).
- Si se usa el prompt como extra: enlace público y prueba con una planilla de ejemplo.
- Licencia tipográfica (Screener demo, Space Grotesk, Inter).
- Prueba en móvil y revisión editorial independiente.
- Aprobación humana y fecha.
