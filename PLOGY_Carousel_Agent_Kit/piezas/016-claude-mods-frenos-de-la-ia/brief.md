# Pieza 016 · Claude Mods, los frenos de la IA

Estado: BORRADOR PARA REVISIÓN HUMANA. No publicar.

Carrusel de invitación a un taller, armado a partir del guion que aportó Luciano y ampliado con la documentación oficial de Anthropic sobre los Mods (centrada en explicar los Mods). Incluye 6 láminas, caption de Instagram y post de LinkedIn (`textos.md`). Por petición, no se construyó el flujo de DM ni un reporte: el CTA promete un enlace de inscripción que hay que preparar aparte.

## Oportunidad

- ID y estado editorial: 016 · borrador completo (carrusel y textos), pendiente de revisión humana
- Tipo de origen: guion aportado por Luciano (Plogy) para promocionar un taller, con una novedad de producto de apoyo (Claude Mods, 1 de octubre de 2026).
- Fuente primaria, fecha y enlace o registro interno (leídas el 2026-10-20 con una herramienta que resume la página):
  - Anthropic, "Customize Claude Code with mods in TypeScript", 1 de octubre de 2026: https://claude.com/resources/articles/claude-code-mods
  - Documentación de Claude Code, "Mods overview": https://code.claude.com/docs/en/plugins/mods/overview
  - Documentación de Claude Code, "Create a mod": https://code.claude.com/docs/en/plugins/mods/create
  - Documentación de Claude Code, "Overview": https://code.claude.com/docs/en/overview
  - Apoyo secundario (alemán): all-ai.de (1 oct 2026) y schieb.de.
- Qué afirma la fuente y qué queda sin verificar:
  - Confirmado en fuente primaria: Claude Code es una herramienta de Anthropic que lee el código, edita archivos y ejecuta comandos, y se usa en terminal, VS Code, app de escritorio y navegador. Un mod es un plugin hecho de funciones JavaScript o TypeScript que Claude Code llama cuando ocurre un evento; la función puede observarlo, cambiarlo o responderlo. Se puede pedir a Claude que escriba el mod (en una sesión interactiva, con aprobación). Se instala con `/plugin install nombre@marketplace` (o `claude plugin install`); `claude --plugin-dir` lo carga en una sola sesión. Mods activados por defecto: terminal 2.1.287 o superior, app de escritorio 2.1.286 o superior. Mods de ejemplo de Anthropic: `blast-radius` (retiene un comando riesgoso como `rm -rf` o un force push y muestra qué cambiaría, con botones para seguir o cancelar), `token-weather` (dibuja un pronóstico de la ventana de contexto sobre el prompt) y `replay-theater` (comando `/replay` que recorre las ediciones de archivos del último turno). Un mod corre con tus permisos (puede leer y escribir archivos, ver secretos y mensajes, aprobar una llamada antes de que te pregunten y gastar tu uso), no está en un entorno aislado y no puede cambiar el aviso de permisos. `claude plugin validate` lista los eventos y llamadas de un mod sin ejecutarlo; `claude --safe-mode` desactiva los mods instalados.
  - Parcialmente respaldado: la "alerta de gasto". La documentación dice que un mod puede leer el uso de tokens de cada solicitud y mostrarlo, pero no hay un mod de ejemplo de alertas con límite de gasto. La lámina 5 lo presenta como parte de los tres ejemplos y su nota dice que la alerta se pide a medida. Tampoco hay que confundir tokens con dinero: conviene aclararlo en el taller.
  - Sin verificar: las capturas son ilustraciones y no muestran ningún mod real;  Las notas se leyeron por resumen: comparar citas textuales con las páginas.
  - Interés comercial: Anthropic vende Claude Code y publica la documentación. Plogy no tiene vínculo declarado con Anthropic en esta pieza.
- Audiencia: Negocios (explicado para quien no programa)
- Vertical: IA y automatizaciones
- Pilar principal: Conocimiento
- Pilar secundario: ninguno
- Subcategoría y confianza de clasificación: herramienta explicada con analogía y llamado a un taller · confianza alta (pilar claro, fuente primaria)
- Tesis de Plogy en una frase: una IA que trabaja sola necesita frenos, avisos y registro, y los Mods permiten ponerlos.
- Problema o tensión que hace relevante la pieza: el miedo razonable a dejar una IA trabajando sola en un negocio (borrar archivos, gastar de más).
- Ángulo distintivo y por qué Plogy puede decirlo: Plogy implementa IA en negocios y lo enseña; la pieza invita a un taller práctico. La analogía del auto y la autoescuela es del guion.
- Objetivo: inscripciones al taller del jueves 22 de octubre de 2026 a las 19:30.
- Término principal de búsqueda y términos secundarios reales: "Claude Mods". Secundarios: "Claude Code", "controlar una IA", "plugins de Claude Code".
- CTA del último slide y estado del recurso prometido: "Comenta MOD y te mandamos el link de inscripción." El enlace de inscripción NO existe todavía en este paquete, ni el flujo de DM. **No se puede publicar hasta que estén definidos** (ver checklist).

Por qué este tema: es el guion de Luciano y conecta con una novedad reciente de Claude Code. Se amplió para que quien no programa entienda qué es Claude Code, qué es un Mod, qué hacen tres ejemplos reales, cómo se consigue uno y qué cuidar.

## Cambios respecto al guion (para que Luciano los apruebe)

1. "Te dan tres cosas" pasa a "tres ejemplos de lo que puede hacer un Mod". Un Mod es código; el freno (`blast-radius`) y la cámara (`replay-theater`) tienen un Mod de ejemplo de Anthropic. La alerta de gasto no tiene un Mod ya hecho: es algo que se pide a medida.
2. Luciano pidió centrar el contenido en explicar qué son los Mods (no Claude Code, que su audiencia ya conoce), sumar fotos y condensar: 9 láminas le parecieron demasiadas. La versión de 6 láminas junta el problema con el gancho, el concepto con la analogía, los tres ejemplos con las otras capacidades y el cómo conseguirlos con los cuidados. Las versiones previas de 11 y 9 láminas se conservan solo como fuente: `carrusel-11-laminas.html` y `carrusel-9-laminas.html`.
3. La salvedad de seguridad (láminas 9 y 10) es parte de la documentación oficial. No estaba en el guion; se puede acortar, pero conviene conservarla porque la audiencia no programa.
4. "Pedal de emergencia" se escribió como "los pedales del copiloto en una autoescuela".
5. La pregunta final del guion ("¿Tú ya confías en la IA...?") quedó en el caption, no en el último slide, para que el CTA tenga una sola acción.
6. El taller: "Jueves 22 a las 19:30" (dato de Luciano). Se entendió hora de 24 h y la zona horaria queda por confirmar.

## Secuencia (6 láminas)

| Slide | Función narrativa | Titular | Texto de apoyo | Qué aporta al siguiente | Imagen y razón | Composición | Fuente de la afirmación |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | Gancho y problema | ¿Le darías las llaves de tu auto a una IA para que maneje sola? | Da miedo, ¿verdad? Con las IA de hoy pasa algo parecido: pueden borrar archivos por error o gastar de más. | ¿Qué lo evita? | Foto retro de los 80: hombre con una taza frente a pantallas (derivado 01, naranja de marca) | Foto a sangre, texto abajo | Guion |
| 02 | Concepto | Para eso existen los Claude Mods. | Como los mods de un videojuego, pero para tu IA: programas pequeños que cambian cómo se comporta Claude Code. | ¿Cómo funciona? | Dos manos que casi se tocan (derivado 03): humano e IA | Texto arriba, foto abajo | Anthropic (artículo y Mods overview). La analogía del videojuego es de Plogy. |
| 03 | Mecanismo | Cada acción de la IA es un evento. | Flujo: evento, Mod, y tres poderes: mira, cambia, toma el control. | Ejemplos | Diagrama dibujado | Fondo claro | Documentación de Anthropic (Mods overview) |
| 04 | Ejemplos | Tres Mods para frenar a tu IA. | Freno de mano, alerta de gasto y cámara de seguridad. Y también: ocultar claves, pedir confirmación antes de tocar producción o reescribir mensajes. | ¿Cómo consigo uno? | Persona detectada por una IA (derivado 05), en la tarjeta de la cámara | Tres tarjetas | blast-radius y replay-theater (Mods de ejemplo de Anthropic). Alerta de gasto: a medida (la documentación dice que un Mod puede leer el uso de tokens). Otras capacidades: artículo de Anthropic. |
| 05 | Cómo y cuidados | No hace falta programarlo. | Pídeselo a Claude, instala uno hecho o pruébalo sin instalar. Ojo: corre con tus permisos; solo de fuentes de confianza, claude plugin validate, claude --safe-mode. | CTA | Sin imagen. Tarjetas con comandos y aviso naranja. | Fondo claro | Documentación (Create a mod y Mods overview) |
| 06 | CTA | Jueves 22, 19:30. Te enseñamos a usar los Mods. | Comenta MOD y te mandamos el link de inscripción. | Cierre | Silueta tecleando con destellos (derivado de la biblioteca, variante 21 adaptada) | Palabra clave gigante | Datos del taller: Luciano |

## Textos por canal

Ver `textos.md` (caption de Instagram con hashtags y razón, post de LinkedIn y diferencia de enfoque).

## Estado del flujo (checklist de salida)

- [x] Fecha y hora del taller: jueves 22 de octubre de 2026, 19:30 (dato de Luciano).
- [ ] Datos del taller que faltan: zona horaria, plataforma o lugar, duración, si tiene costo y cupos.
- [ ] Publicar antes del jueves 22. Si se publica después, hay que cambiar la lámina 8.
- [ ] Enlace de inscripción creado y probado.
- [ ] Palabra clave MOD registrada con vigencia (hasta el taller). Decidir si se aceptan "mod", "mods" y "Mod".
- [ ] Flujo de DM configurado y probado: comentario, mensaje con el enlace. (No escrito: se pidió solo el carrusel y los textos.)
- [ ] Persona asignada para responder lo que llegue por fuera del flujo.
- [ ] Comparar las citas y los comandos con la documentación vigente (las versiones y los comandos pueden cambiar entre lanzamientos) y decidir cómo se presenta la alerta de gasto (lámina 4).
- [ ] Derechos de la foto y licencias de tipografía resueltos.
- [ ] Aprobación humana con fecha.

## Revisión

- Evidencia y procedencia de cada dato: lo técnico viene de la documentación oficial de Anthropic (ver arriba). No hay capturas de Mods: los diagramas y tarjetas de las láminas 4 y 5 son dibujos de Plogy. La alerta de gasto con límite no tiene un Mod de ejemplo. Los datos del taller son de Luciano.
- Derechos de cada asset y licencia de la tipografía: una foto del moodboard (`unverified_reference_only`). Screener solo tiene licencia demo; Space Grotesk se cargó desde Google Fonts y falta confirmar licencia comercial.
- Legibilidad en móvil: revisada a ojo en los PNG; apoyos de 33 a 44 px sobre 1080 px y notas de 28 px. Pendiente confirmar en un móvil real.
- Coherencia entre tesis, secuencia, caption y CTA: el CTA de las láminas y del caption es "Comenta MOD". LinkedIn cierra con una pregunta y un enlace por definir.
- Verificación de estilo: sin guiones largos, sin emojis en LinkedIn, tres hashtags, sin las muletillas de la lista prohibida.
- Pendiente de revisión independiente: no se ha pasado por el revisor editorial.
- Aprobación humana y fecha: PENDIENTE

## Archivos de la pieza

- `carrusel.html`: fuente editable de las 6 láminas (1080x1350). Sin parámetros muestra todas; con `?s=1` a `?s=6`, una sola.
- `exports/slide-01.png` a `slide-06.png`: exportaciones en orden. 
- `textos.md` y `brief.md`, con su versión `.html` para el visor.
- `assets/`: derivados de foto (no son originales). `scripts/derive.py` crea 01, 02, 03 y 05 (el 02, oficina con ventanas de error, quedó sin usar en esta versión); `07-cta-silueta.jpg` es copia del derivado 21 de la biblioteca de CTAs.

## Inventario de assets

| Asset | Origen | Transformación | Lámina | Derechos |
| --- | --- | --- | --- | --- |
| `brandkit/assets/plogy-color.svg` | Brand kit Plogy | Ninguna | 03, 04, 05 | Propio de Plogy. Trazado derivado de la fuente demo, por verificar. |
| `brandkit/assets/plogy-white.svg` | Brand kit Plogy | Ninguna | 01, 02, 06 | Igual que el anterior |
| `brandkit/assets/plogy-black.svg` | Brand kit Plogy | Ninguna | Ninguna | Igual que el anterior |
| `assets/01-retro.jpg` | Original: `5fc091d4c9d6625b9177ae9e6f5988c5.jpg`. Autor desconocido; parece una imagen de los años 80 (posiblemente generada). | Mapa de color a Ink, naranja y crema, recorte 1080x1350. `scripts/derive.py`. | 01 | `unverified_reference_only`. NO publicar hasta verificar derechos y que la persona no sea identificable. |
| `assets/02-error.jpg` | Original: `0df7100a10bafeeac554662325013596.jpg` | Mapa de color a Ink, naranja y crema, banda 1080x620. | Ninguna (solo en la versión de 9 láminas) | `unverified_reference_only`. NO publicar hasta verificar derechos. |
| `assets/03-manos.jpg` | Original: `perfection.jpg` | Mapa de color a Ink, naranja y crema, banda 1080x560. | 02 | `unverified_reference_only`. NO publicar hasta verificar derechos. |
| `assets/05-vigilancia.jpg` | Original: `ai watching 2.jpg` (también usada en las piezas 002 y 003) | Recorte de bandas negras, banda 1080x560, aclarada x1,6. | 05 | `unverified_reference_only`. NO publicar hasta verificar derechos. |
| `assets/07-cta-silueta.jpg` | Original: `1341dd4c343455db0f11332434703375.jpg`. Autor desconocido. | Mapa de color a Ink, naranja y crema, recorte 1080x1350 (copia del derivado 21 de `piezas/cta-biblioteca/`). | 06 | `unverified_reference_only`. NO publicar hasta verificar derechos. |
| Diagramas, tarjetas y comandos | CSS y SVG | Ninguna | 03 a 05 | Propio |

Los originales siguen intactos en `assets/reference-originals/`.
