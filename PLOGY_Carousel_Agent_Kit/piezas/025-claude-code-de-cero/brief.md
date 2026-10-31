# Brief · pieza 025 · Claude Code de cero

Estado: BORRADOR para revisión humana. No publicar. Aprobación humana y fecha: PENDIENTE.

## Qué es

Segunda de la tanda de tres adaptaciones. La referencia (otra cuenta, en inglés) es una guía "de principiante a pro" de Claude Code: qué es, flujo con plan mode, MCP, CLAUDE.md, skills, usos para fundadores, qué hacer y qué no. CTA de la referencia: un video propio.

**Qué cambiamos:**
- En español, para dueños de negocio que no programan, con estética Plogy.
- Sin comparación con el logo de ChatGPT: el contraste es "un chat" contra Claude Code.
- Corregimos dos datos de la referencia: recomienda "Opus 4.6" (el modelo actual es Opus 5.5; no recomendamos modelo) y dice "Shift+Tab dos veces" para el plan mode (depende del modo en que estés; la documentación dice pulsar hasta ver "plan mode on").
- Sumamos lo que la referencia no tiene: dónde vive (terminal, escritorio, web, editor), permisos y frenos (modos y Mods), y el criterio de Plogy.
- CTA: Comenta CLAUDE y te mandamos nuestra guía de primeros pasos (`guia.md`: instalar, primera sesión, primer encargo con plan, CLAUDE.md, skills, MCP, frenos y tres errores comunes). Tarjeta de vidrio sobre la foto 21 de la biblioteca.

**Criterio propio de Plogy (lámina 9):** la herramienta se aprende en una tarde; saber qué encargarle, no. Lo que separa a quien la domina es escribir un buen encargo y revisar lo que vuelve, y eso se entrena. Conecta con la tesis de la pieza 022 (el talento se forma) y con las clases.

## Fuentes primarias (documentación oficial de Claude Code)

| Dato | Fuente |
|---|---|
| Funciona en cualquier carpeta, no solo código ("notes vault, documentation folder") | code.claude.com/docs/en/common-workflows |
| Plan mode: lee y propone sin editar hasta aprobar; Shift+Tab hasta "plan mode on" | common-workflows y permission-modes |
| Modos: Manual (solo lee sin preguntar), acceptEdits (crea y edita archivos de la carpeta sin preguntar), plan; ciclo con Shift+Tab | code.claude.com/docs/en/permission-modes |
| CLAUDE.md: `./CLAUDE.md` (proyecto, equipo) y `~/.claude/CLAUDE.md` (personal); `/init` genera uno | code.claude.com/docs/en/memory |
| Skills: `.claude/skills/<nombre>/SKILL.md` y `~/.claude/skills/<nombre>/SKILL.md`; Claude las usa cuando son relevantes o con `/nombre` | code.claude.com/docs/en/skills |
| MCP: "open source standard"; acceso a herramientas, bases de datos y APIs; `claude mcp add --transport http notion https://mcp.notion.com/mcp` | code.claude.com/docs/en/mcp |
| Superficies: CLI, app de escritorio (Mac y Windows), web (claude.ai/code), extensiones de VS Code y JetBrains | Información de producto de Claude Code |
| blast-radius retiene `rm -rf` o un force push y pregunta | code.claude.com/docs/en/plugins/mods/overview (ver pieza 021) |

## Ilustraciones

Las ventanas, terminales, el CLAUDE.md, la skill de ejemplo y la retención de blast-radius son maquetas propias rotuladas "Ilustración", no capturas. Los datos de ejemplo (reportes de octubre, tienda con 2 sedes) son inventados para ilustrar.

## Autor y cuentas

Cada lámina lleva al pie una barra con la foto y el usuario de JuanFra Martínez (@juanframartz). La pieza se sube en Plogy y en la cuenta personal (por ejemplo como colaboración de Instagram), con la misma versión. La foto sale del perfil de Instagram (`assets/av-autor.png`).

## Pendientes antes de publicar

- Publicar la guía en un enlace y configurar la respuesta automática a CLAUDE. Ojo: la pieza 018 también usa CLAUDE como palabra (allí lleva al link de la clase). Si se publican cerca, la respuesta automática tiene que distinguirlas o cambiar una de las dos.
- Datos de instalación de la guía: code.claude.com/docs/en/setup (comandos, requisitos, planes que incluyen Claude Code). Revisarlos el día de publicar.
- blast-radius es un Mod de ejemplo que se instala aparte (no viene incluido); la lámina 8 dice "por ejemplo". Revisar si se quiere aclarar.
- Logos de la lámina 7 (Notion, Google Drive, Gmail, GitHub, PostgreSQL, Slack): Simple Icons, CC0, con el color de cada marca; uso nominativo, revisar guías de marca si se quiere.
- Derechos de las fotos de la biblioteca usadas en las láminas 1, 9 y 10 (`01-ascii.jpg`, `09-manos.jpg`, `10-silueta.jpg`, variantes 16, 23 y 21): `unverified_reference_only`.
- Licencias tipográficas, prueba en móvil, revisión editorial independiente y aprobación humana con fecha.
