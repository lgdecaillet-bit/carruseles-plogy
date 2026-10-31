# DM de la pieza 013 · palabra clave PROCESO

Estado: BORRADOR para revisión humana. Nada está configurado ni enviado.

**Plogy confirma qué ofrece en esa conversación.** Este es un CTA comercial: no hay reporte ni recurso que entregar. La persona escribe PROCESO por DM y entra a una conversación de calificación con una persona de Plogy o con el flujo que Plogy decida. Qué se ofrece al final (llamada, diagnóstico, propuesta u otra cosa), con qué precio y en qué plazo, lo define Plogy. Los textos entre corchetes son pendientes de Plogy.

## Palabra clave

- Palabra: **PROCESO**
- Pieza: 013, "Ponle nivel a tu proceso."
- Acción de la persona: escribir PROCESO por mensaje directo (no por comentario). Así la conversación la inicia la persona. Confirmar en la documentación de Meta cómo queda la ventana de respuesta de 24 horas en ese caso antes de configurar.
- Aceptar mayúsculas, minúsculas y espacios de más. Decidir si se aceptan variantes como "mi proceso".
- Colisiones: ninguna con las palabras usadas hasta ahora (COSTO, MIGRAR, MEDIR, BANCO, MAPA, PROMPT, GUIA, AUDITORIA).
- Vigencia propuesta: 30 días desde la publicación del carrusel. Decidir.

## Guion de conversación

### Primer mensaje (respuesta inmediata al DM con la palabra clave)

> Hola, gracias por escribirnos. Para decirte qué nivel parece pedir tu proceso (automatización, asistente o agente) te hacemos tres preguntas cortas. ¿Empezamos?
> [Botón: Sí, empecemos]

### Tres preguntas de calificación

Cada una corresponde a las cuatro preguntas del carrusel. Se hacen una por mensaje y se espera la respuesta.

1. Pregunta 1 (proceso y volumen):
   > ¿Qué proceso quieres automatizar y más o menos cuántas veces se repite por semana?
2. Pregunta 2 (pasos y juicio, preguntas 1 y 2 del carrusel):
   > ¿Los pasos son siempre los mismos o cambian según el caso? ¿Alguien tiene que leer, interpretar o redactar algo en el camino?
3. Pregunta 3 (sistemas y error, preguntas 3 y 4 del carrusel):
   > ¿Tiene que enviar, cobrar o cambiar datos en algún sistema? ¿Y qué pasaría si se equivoca y quién lo revisa hoy?

### Cierre

> Gracias. Con lo que nos cuentas, una primera lectura: [automatización | asistente | agente con aprobación de una persona], porque [razón en una línea]. Es una lectura inicial, no un diagnóstico.
> [PLOGY CONFIRMA QUÉ OFRECE: por ejemplo, una conversación de [duración] para revisar el proceso con una persona del equipo. Definir oferta, plazo y si tiene costo.]
> Una persona de Plogy te escribe [plazo].

### Lectura inicial según las respuestas

Ayuda para quien responde. No es un diagnóstico y no se promete resultado.

| Lo que cuenta la persona | Lectura inicial | Frase base |
| --- | --- | --- |
| Pasos siempre iguales, o varían pero nadie tiene que juzgar | Automatización | "Parece un proceso de reglas fijas. Antes de pensar en IA conviene dejar escritos los pasos." |
| Los casos varían y hay que leer o redactar, pero una persona envía o decide | Asistente | "Parece un trabajo para un asistente: la IA prepara y una persona revisa y decide." |
| Los casos varían, hay que juzgar y el proceso actúa sobre sistemas | Agente, con una persona que aprueba si el error cuesta caro | "Aquí un agente podría tener sentido, con límites claros y aprobación antes de los pasos que no se pueden deshacer." |

## Reglas de la conversación

- Voz Plogy: directa, sin humo, sin muletillas de IA, sin guiones largos, sin emojis por defecto.
- No prometer ahorro, plazos ni resultados. Una lectura inicial no es una propuesta.
- No pedir contraseñas, claves de acceso, datos de clientes ni información sensible por DM. Si la persona los ofrece, pedirle que no los envíe.
- No pedir correo ni teléfono mientras no esté resuelta la captura de datos (sección 18 de `skills/plogy-cta-design/FLUJO-REPORTE-DM.md`). Si Plogy lo decide, hacerlo con consentimiento.
- Si preguntan por precio: "Depende del proceso. [PLOGY CONFIRMA QUÉ OFRECE Y CÓMO LO COBRA]". Pasar a una persona.
- Si escriben algo fuera de este guion, pasar a una persona. No se improvisa con respuestas automáticas.
- No se insiste a quien no responde.

## Mensaje fuera de vigencia (para quien escriba PROCESO después de la ventana)

> Gracias por escribirnos. Esta conversación ya cerró, pero puedes contarnos tu proceso aquí y una persona del equipo te responde. [PLOGY CONFIRMA QUÉ OFRECE]

## UTM

No hay enlace en el guion. Si Plogy añade un enlace (por ejemplo, para agendar), usar:

| Canal | utm_source | utm_medium | utm_campaign |
| --- | --- | --- | --- |
| DM de Instagram | instagram | dm | 013-proceso |

## Antes de activar

- [ ] Plogy define qué ofrece al cierre de la conversación, con plazo y costo, y reescribe el cierre.
- [ ] Persona asignada para atender las conversaciones y los mensajes fuera de guion, con horario.
- [ ] Textos aprobados por una persona.
- [ ] Herramienta de DM elegida y el flujo probado con una cuenta de prueba: mensaje con PROCESO, primer mensaje, botón, tres preguntas, cierre.
- [ ] Verificado en la documentación de Meta cómo se comporta la ventana de 24 horas cuando la persona inicia el DM.
- [ ] Decidido qué pasa con los datos de la conversación (dónde se guardan y quién los ve).
