# Guía Plogy · Tus primeros pasos con Claude Code

Estado: BORRADOR para revisión humana. Es el recurso que se manda por DM a quien comenta CLAUDE. Datos de la documentación oficial de Claude Code (code.claude.com/docs), revisados el 23 de octubre de 2026.

## Antes de empezar

- **Cuenta:** necesitas un plan Pro, Max, Team o Enterprise de Claude, o una cuenta de Console. El plan gratis de claude.ai no incluye Claude Code.
- **Computador:** macOS 13 o superior, Windows 10 (1809) o superior, o Linux (Ubuntu 20.04+, Debian 10+). 4 GB de RAM o más, e internet.
- **¿No te llevas con la terminal?** Usa la app de escritorio de Claude: tiene Claude Code sin pasar por la terminal.

## Paso 1. Instálalo (5 minutos)

Abre la terminal y pega el comando de tu sistema:

- **Mac o Linux:** `curl -fsSL https://claude.ai/install.sh | bash`
- **Windows (PowerShell):** `irm https://claude.ai/install.ps1 | iex`

Cuando termine, abre una terminal nueva y escribe `claude --version`. Si ves un número de versión, quedó instalado. Si dice que no encuentra `claude`, cierra y vuelve a abrir la terminal.

## Paso 2. Tu primera sesión

1. Crea una carpeta de prueba y pon dentro 2 o 3 archivos de verdad (un Excel de ventas, un documento, notas). Mejor una copia, no los originales.
2. En la terminal, entra a esa carpeta y escribe `claude`.
3. La primera vez te pide iniciar sesión en el navegador con tu cuenta de Claude.
4. Escribe `/init`: Claude revisa la carpeta y arma un primer CLAUDE.md.

## Paso 3. Tu primer encargo, con plan

1. Pulsa **Shift+Tab** hasta que veas "plan mode on" abajo. En ese modo Claude lee y propone, pero no edita nada.
2. Escribe el encargo con tres cosas: qué quieres, con qué archivos y cómo se ve el resultado. Ejemplo: "Junta las ventas de octubre de estos 3 archivos y arma un resumen de una página, con el total por sede".
3. Lee el plan. Si algo no cuadra, corrígelo ahora: es el momento más barato.
4. Apruébalo y deja que lo ejecute.
5. Revisa el resultado antes de usarlo o mandarlo a alguien.

## Paso 4. Enséñale tu contexto (CLAUDE.md)

Abre el CLAUDE.md que creó `/init` y agrega lo que Claude no puede adivinar:

```markdown
# [Nombre del proyecto]
[Qué es, en una línea]

## Cómo trabajamos
- [Ej.: cifras en pesos, sin decimales]
- [Ej.: un reporte = una página]

## Nunca
- [Ej.: enviar nada a clientes sin aprobación]
```

`./CLAUDE.md` vive en la carpeta del proyecto y lo puede compartir tu equipo. `~/.claude/CLAUDE.md` es solo tuyo y aplica en todos tus proyectos.

## Paso 5. Lo que repites, vuélvelo skill

Si haces la misma tarea cada semana, pídele a Claude: "Convierte lo que acabamos de hacer en una skill llamada reporte-semanal". Queda en `.claude/skills/reporte-semanal/SKILL.md` y la próxima vez la usas con `/reporte-semanal`.

## Paso 6. Conecta solo lo necesario

Con MCP, Claude Code se conecta a herramientas como Notion, Drive o tu base de datos. Ejemplo de la documentación:

`claude mcp add --transport http notion https://mcp.notion.com/mcp`

Nuestro criterio: conecta una herramienta a la vez y solo la que la tarea necesita. Cada conector es una llave más.

## Paso 7. Ponle frenos

- **Manual:** solo lee sin preguntar; todo lo demás te lo consulta.
- **Accept edits:** crea y edita archivos de la carpeta sin preguntar.
- **Plan:** propone y no edita hasta que apruebes.

Se cambian con Shift+Tab. Para empezar, quédate en Manual o Plan. Y trabaja siempre sobre copias hasta que confíes en el resultado.

## Tres errores comunes

1. **Pedir sin plan.** Un encargo vago da un resultado vago. Plan primero.
2. **Usarlo sobre los archivos originales.** Trabaja con copias al principio.
3. **No revisar lo que vuelve.** Claude se equivoca. Revisa antes de mandar.

## ¿Quieres hacerlo acompañado?

En las clases gratis de Plogy lo instalamos contigo y armas tu primer encargo con un caso real. Escríbenos y te avisamos de la próxima.
