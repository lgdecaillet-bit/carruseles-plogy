# Brief · pieza 021 · Mods para vibecodear seguro

Estado: BORRADOR para revisión humana. No publicar. Aprobación humana y fecha: PENDIENTE.

## Qué es

Carrusel de 7 láminas para vibecoders sin formación técnica: cinco Mods de Claude Code para no borrar, no pisar y no exponer. CTA: la próxima clase gratis (Comenta CLASE). Complementa la pieza 016 (qué son los Mods) con un ángulo práctico.

**Criterio propio de Plogy:** hacer vibecoding está bien; hacerlo sin frenos no. Los frenos se ponen antes del accidente, no después.

## Fuentes primarias (documentación oficial de Claude Code)

- Mods overview: https://code.claude.com/docs/en/plugins/mods/overview
- React to events: https://code.claude.com/docs/en/plugins/mods/events
- Create a mod: https://code.claude.com/docs/en/plugins/mods/create

## Qué está confirmado y qué no

| Mod | Origen | Respaldo |
|---|---|---|
| blast-radius | Ejemplo oficial en `anthropics/claude-code-playground` | "holds a risky shell command, such as rm -rf or a force push, and shows what it would change, with buttons to proceed or cancel" |
| /diff | Mod incluido en Claude Code (`cc-plugin-diff`, sesiones interactivas de terminal) | Tabla "Mods built into Claude Code" |
| replay-theater | Ejemplo oficial | "adds a /replay command that steps through the file edits Claude made in the last turn" |
| Guardián de .env | A medida (idea de Plogy) | La documentación muestra cómo negar una llamada a una herramienta (`deny`); no trae un ejemplo específico para .env. Alternativa sin código: una regla de permisos que niegue leer `.env`. |
| Confirmar antes de push a main | A medida | La documentación trae un ejemplo que niega `git push` en `main` y otro que pregunta antes de comandos riesgosos |

Otros datos: los Mods corren con tus permisos y sin sandbox; `claude plugin validate` lista sus hooks y llamadas; `--safe-mode` los apaga; requieren Claude Code 2.1.287 o superior; Claude escribe un Mod con la skill `plugin-authoring` y pide aprobar cada archivo (en los modos default y acceptEdits). Comandos de la lámina 6: `git clone` del repositorio playground, `claude --plugin-dir`, y para dejarlo fijo agregar el directorio de mods como marketplace e instalar desde `claude-code-playground-mods` (el nombre del marketplace sale de la documentación; el comando `/plugin marketplace add` es el estándar de plugins, conviene probarlo).

## Ilustraciones

Las terminales de las láminas 1 y 3 (rm -rf ./src, git push --force, "14 commits en main") y el diff de la 4 son maquetas propias rotuladas "Ilustración", no capturas de los Mods reales.

## Secuencia

| # | Lámina |
|---|---|
| 1 | Portada: terminal con un comando retenido + "¿Haces vibecoding? Ponle frenos a Claude Code." |
| 2 | El riesgo: borra, pisa, toca tus claves |
| 3 | Mod 1 blast-radius (se instala) |
| 4 | Mods 2 y 3: /diff (incluido) y replay-theater (se instala) |
| 5 | Mods 4 y 5 a medida: guardián de .env y confirmación antes de push a main |
| 6 | Cómo probar los de ejemplo + advertencia de permisos (naranja) |
| 7 | CTA variante 30: próxima clase gratis, Comenta CLASE |

## Pendientes antes de publicar

- Fecha de la próxima clase gratis, enlace de inscripción y si la clase cubre la instalación de estos Mods.
- Probar en una máquina los comandos de la lámina 6 y que blast-radius y replay-theater sigan en el repositorio.
- Palabra clave CLASE en la herramienta de comentarios.
- Derechos de la foto `assets/07-pc-viejo.jpg` (variante 30): `unverified_reference_only`.
- Licencias tipográficas, prueba en móvil, revisión editorial independiente y aprobación humana con fecha.
