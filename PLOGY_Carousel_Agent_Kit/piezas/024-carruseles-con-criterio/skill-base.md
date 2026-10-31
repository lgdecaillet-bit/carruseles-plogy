# Skill base de Plogy · Carruseles con criterio

Estado: BORRADOR para revisión humana. Es el recurso que se manda por DM a quien comenta CRITERIO. Luciano decide qué se comparte antes de enviarlo.

## Cómo usarla

1. En Claude Code, crea la carpeta `.claude/skills/carrusel-con-criterio/` en tu proyecto.
2. Guarda dentro un archivo `SKILL.md` con todo lo que va entre las dos líneas de abajo.
3. Cambia lo que está entre corchetes por lo de tu marca.
4. Pídele a Claude: "Haz un carrusel sobre [tema] con la skill carrusel-con-criterio".

---

```markdown
---
name: carrusel-con-criterio
description: Hacer carruseles de Instagram y LinkedIn para [tu marca] en cinco pasos: brief con opinión propia, datos verificados, texto, diseño con tokens fijos y revisión. Usar cuando pidan un carrusel o un post en láminas.
---

# Carrusel con criterio

## Paso 1. El brief, antes de escribir
Escribe un brief.md con:
- A quién le habla la pieza (una sola audiencia).
- Qué prueba tiene (fuente, caso real o experiencia propia).
- Qué opina [tu marca] sobre esto, en una frase. Esa frase no copia ni parafrasea la fuente.
Si no hay una opinión propia, avisa y no sigas.

## Paso 2. Cada dato con su fuente
- Confirma cada cifra, fecha y nombre en la fuente original, no en un resumen.
- Lo que no puedas confirmar no entra en la pieza. Anótalo en el brief como "no verificado".
- Todo ejemplo inventado o maqueta lleva la etiqueta "Ilustración".
- Pon en el brief una tabla: dato, fuente (URL).

## Paso 3. El texto
- Una idea por lámina. Entre 6 y 10 láminas.
- Portada con tensión, láminas con avance, cierre con una sola acción (CTA).
- Voz de [tu marca]: [tres adjetivos]. Nunca: [palabras o frases que no usas].
- Sin guiones largos ni muletillas de IA.

## Paso 4. El diseño, con tokens fijos
- Cada lámina es HTML de 1080x1350, una sección por lámina.
- Colores y letras solo de estos tokens (no inventes otros):
  - Fondo: [#ffffff] · Texto: [#171310] · Acento: [#ff5b00] · Texto suave: [#625951]
  - Titulares: [fuente] · Texto: [fuente]
- El texto y el logo van por delante de cualquier imagen.
- Exporta cada lámina a PNG y míralas una por una antes de entregar. Si algo se solapa o no se lee, corrige y vuelve a exportar.

## Paso 5. La revisión
- Revisa la pieza con un agente distinto del que la escribió. Que califique: tono, una idea por lámina, valor para la audiencia, honestidad de los datos, CTA y legibilidad.
- Reglas que no se negocian: nada inventado, nada sin fuente, un solo CTA.
- La pieza queda en borrador. La aprueba una persona antes de publicar.

## Entrega
Carpeta con: carrusel.html, las láminas en PNG, brief.md con fuentes, y textos.md con el caption de Instagram y el post de LinkedIn.
```

---

## De dónde sale

Es una versión simplificada del kit de carruseles de Plogy: las skills de clasificación, planeación, narrativa, adaptación visual, captions, CTA, producción y revisión editorial, reducidas a una sola skill para que cualquiera la pueda probar.
