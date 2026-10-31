

######## instagram · GPT-4o se apaga el 14 de enero (kit 004) · 2636 car.
POR QUÉ: Convierte un aviso técnico en una tesis de quien implementa: un modelo es una dependencia con fecha. Cada cifra, fecha e ID lleva su fuente, y lo que no se sabe se dice («su página no aclara si estos lo son»). La lámina de criterio da tres pasos aplicables mañana, y el cierre pide una acción que nace de lo que enseñó la pieza.

Lámina 1 (portada): IA + automatizaciones · Oct 2026
El 14 de enero tu automatización puede romperse.
OpenAI retira GPT-4o y GPT-4.1 de su API.

Lámina 2: Cinco versiones salen de la API el 14 de enero de 2027.
gpt-4o-2024-08-06
gpt-4o-2024-11-20
gpt-4o-mini-2024-07-18
gpt-4.1-2025-04-14
gpt-4.1-mini-2025-04-14
Las versiones afinadas (fine-tunes) siguen el mismo calendario.
Fuente: OpenAI, página de deprecaciones. Aviso del 14 oct 2026.

Lámina 3: El aviso fue corto.
92 días del aviso al apagado. OpenAI declara al menos 6 meses para modelos de disponibilidad general. Su página no aclara si estos lo son.
Fuente: OpenAI, página de deprecaciones.

Lámina 4: El reemplazo no es un cambio de nombre.
Razona por defecto: esfuerzo de razonamiento medio si no lo cambias.
Llamadas a funciones: en Chat Completions, solo con reasoning_effort: none. Con razonamiento, usa la Responses API.
Sin ajuste fino: gpt-6-luna no admite fine-tuning.
Fuente: OpenAI, ficha de gpt-6-luna, el reemplazo que recomienda.

Lámina 5: Luna cuesta hasta 25 veces menos por token de entrada.
Es frente a GPT-4o: $0,10 contra $2,50 por millón de tokens. Frente a GPT-4o mini, solo 1,5 veces. El razonamiento se factura como salida: mide el costo por tarea.
Fuente: fichas de modelos de OpenAI.

Lámina 6: Criterio de Plogy
Tres pasos antes del 14 de enero.
1. Haz el inventario. Busca el nombre del modelo en el código, en tus herramientas y en lo que te dejó un proveedor.
2. Prueba con casos reales. Compara formato, llamadas a funciones y costo con el modelo nuevo.
3. Deja la vuelta atrás lista. Conserva el modelo viejo en una rama hasta el último día.

Lámina 7 (cierre): Primero el inventario. Después la migración.
Comenta MIGRAR y te mandamos la noticia completa y nuestra lista de revisión.

Caption: OpenAI sacará GPT-4o, GPT-4o mini, GPT-4.1 y GPT-4.1 mini de su API el 14 de enero de 2027. Avisó el 14 de octubre, con 92 días de margen, y recomienda pasar a gpt-6-luna. Si tu negocio tiene una automatización que llama a uno de esos modelos, hay que revisarla antes. Según la ficha de OpenAI, gpt-6-luna razona por defecto, solo admite llamadas a funciones en Chat Completions con el razonamiento apagado y no admite fine-tuning. Es mucho más barato por token que GPT-4o, pero eso no dice cuánto costará una tarea. Lo primero es saber en qué lugares aparece el nombre del modelo: código, herramientas, proveedores y tareas programadas. Fuente: página de deprecaciones de OpenAI, aviso del 14 de octubre de 2026. Comenta MIGRAR y te mandamos la noticia completa y nuestra lista de revisión.

Hashtags: #AutomatizacionConIA #IAParaNegocios #OpenAI


######## linkedin · GPT-4o se apaga el 14 de enero (kit 004) · 1767 car.
POR QUÉ: Convierte un aviso técnico en una tesis de quien implementa: un modelo es una dependencia con fecha. Cada cifra, fecha e ID lleva su fuente, y lo que no se sabe se dice («su página no aclara si estos lo son»). La lámina de criterio da tres pasos aplicables mañana, y el cierre pide una acción que nace de lo que enseñó la pieza.

Un modelo de IA es una dependencia de tu automatización, y las dependencias vencen.

El 14 de octubre de 2026 OpenAI avisó de que retira de su API cinco versiones de GPT-4o y GPT-4.1 el 14 de enero de 2027, junto con las versiones afinadas de esos modelos. Recomienda pasar a gpt-6-luna. Del aviso al apagado pasan 92 días, y la política de OpenAI para modelos de disponibilidad general habla de al menos seis meses, aunque su página no aclara si estos lo son.

Para un negocio, lo delicado es que el reemplazo no es un cambio de nombre. Según la ficha de OpenAI, gpt-6-luna razona por defecto con esfuerzo medio, solo admite llamadas a funciones en Chat Completions con el razonamiento apagado, y no admite fine-tuning. Su precio por token es menor que el de GPT-4o (hasta 25 veces en entrada, solo 1,5 veces frente a GPT-4o mini), pero el razonamiento se factura como tokens de salida, así que lo que cuesta una tarea hay que medirlo.

No hemos migrado ningún flujo a este modelo, y no sabemos cómo se comportará el tuyo. Lo que haríamos primero, como criterio y no como garantía:

1. Un inventario de dónde aparece el nombre del modelo: código, herramientas sin código, proveedores, variables y tareas programadas.
2. Una ficha por uso: si llama funciones, si usa un fine-tune y quién responde por él.
3. Pruebas con casos reales y un plan de vuelta atrás hasta el último día.

Un ejemplo hipotético: una automatización de atención al cliente que consulta pedidos con llamadas a funciones sobre un modelo mini puede pasar sin tocar código si el razonamiento queda apagado, o requerir la Responses API si se quiere razonar. En los dos casos hay que probar antes de la fecha.

¿Sabes en cuántos lugares aparece hoy el nombre del modelo que usan tus automatizaciones?


######## instagram · Nadie garantiza que el agente obedezca (kit 008) · 3106 car.
POR QUÉ: Convierte una noticia de política en una decisión de implementación. Separa lo que dijeron de lo que no dijeron, rotula la fuente secundaria y las citas traducidas, y baja el criterio a un caso hipotético rotulado: qué hace solo el agente, qué pregunta antes y qué no toca. La pregunta del cierre se responde con experiencia propia.

Lámina 1 (portada): Nueva York · 5 de octubre de 2026
Nadie garantiza que el agente obedezca.
Ni OpenAI, Anthropic, Meta ni Google lo garantizaron ante el Concejo, bajo juramento.

Lámina 2: Cuatro respuestas, ninguna garantía.
Julie Menin, presidenta del Concejo, pidió a cada una asegurar que sus agentes siempre seguirían las salvaguardas contra daños catastróficos.
OpenAI · Morgan Dwyer
“No es posible que yo garantice que ninguna tecnología esté libre de riesgo.”
Anthropic · Logan Graham
“La ciencia para lograrlo es fundamentalmente difícil y no está resuelta.”
Google · Alice Friend
“Prometer perfección no sería posible con ningún producto del mercado.”
Meta · Shane Cahill
Se comprometió con desplegar IA de forma segura, no con esa garantía.
Fuente secundaria: Fox News, 6 oct. Citas traducidas.

Lámina 3: Admitieron un límite, sin dar la alarma.
Lo que dijeron:
Que no pueden prometer riesgo cero.
Que controlar estos sistemas es ciencia sin cerrar.
Lo que no dijeron:
Que sus agentes sean inseguros.
Cuánto riesgo hay: ninguno dio un número para el peor caso.
Respondieron sobre la tecnología en general; la pregunta era sobre agentes.

Lámina 4: Criterio de Plogy
Diseña como si fuera a equivocarse.
1. Permisos mínimos. Que acceda solo a lo que esa tarea necesita.
2. Revisión humana donde importa. Una persona aprueba lo que cuesta dinero, llega a un cliente o no se puede revertir.
3. Forma de deshacer. Un registro de lo que hizo y una vuelta atrás probada.

Lámina 5: Ejemplo hipotético
Un agente que responde correos de clientes.
Lo hace solo: leer el buzón de soporte y redactar borradores.
Pregunta antes: enviar a un cliente u ofrecer un descuento.
No lo toca: pagos, borrar datos y cambiar permisos.
Y cada acción queda en un registro para poder deshacerla.
No es de ningún cliente. Es una propuesta de diseño.

Lámina 6 (cierre): ¿Qué no le darías acceso a un agente?
Respóndelo en un comentario: qué no le darías y por qué.

Caption: El 5 de octubre, en el Concejo de Nueva York, Julie Menin pidió a representantes de OpenAI, Anthropic, Meta y Google que aseguraran, bajo juramento, que sus agentes de IA siempre seguirían las salvaguardas contra daños catastróficos. Según Fox News, ninguno dio esa garantía. Conviene leerlo con precisión. Hablaron de la tecnología en general ("no es posible garantizar que ninguna tecnología esté libre de riesgo", "prometer perfección no sería posible con ningún producto") y nadie dio un número de riesgo para el peor caso. No dijeron que sus agentes sean inseguros, y Meta se comprometió con desplegar IA de forma segura, sin dar esa garantía. Admitieron un límite, sin dar la alarma. Para un negocio que ya usa o va a usar agentes de IA, la lectura práctica es diseñar como si el agente fuera a equivocarse: permisos mínimos, revisión humana donde importa y una forma de deshacer. Es criterio de Plogy, no un hallazgo de la audiencia. La fuente es secundaria y no hemos visto la transcripción. Cuéntanos en un comentario: ¿qué no le darías acceso a un agente de IA y por qué?

Hashtags: #AgentesDeIA #SeguridadDeIA #IAParaNegocios


######## linkedin · Nadie garantiza que el agente obedezca (kit 008) · 1920 car.
POR QUÉ: Convierte una noticia de política en una decisión de implementación. Separa lo que dijeron de lo que no dijeron, rotula la fuente secundaria y las citas traducidas, y baja el criterio a un caso hipotético rotulado: qué hace solo el agente, qué pregunta antes y qué no toca. La pregunta del cierre se responde con experiencia propia.

Si ni los laboratorios prometen que un agente obedezca siempre, la seguridad de un agente en tu negocio depende de cómo lo diseñes tú, no de la promesa del proveedor.

El 5 de octubre, el Concejo de la Ciudad de Nueva York celebró una audiencia con representantes de OpenAI (Morgan Dwyer), Anthropic (Logan Graham), Google (Alice Friend) y Meta (Shane Cahill), todos bajo juramento. Según Fox News, la presidenta del Concejo, Julie Menin, pidió a cada uno asegurar que sus agentes siempre seguirían las salvaguardas contra daños catastróficos, y ninguno dio esa garantía. Dwyer dijo que no es posible garantizar que ninguna tecnología esté libre de riesgo; Graham, que la ciencia de controlar estos sistemas es difícil y no está resuelta; Friend, que prometer perfección no sería posible con ningún producto.

Dos matices. Respondieron sobre la tecnología en general, no sobre agentes en concreto, y nadie cuantificó el peor caso aunque Menin lo pidió. Y la fuente de las respuestas es cobertura de prensa: no hemos leído la transcripción.

Lo que sí cambia para un negocio es la pregunta de diseño. En vez de "¿qué tan bueno es este agente?", pregunta "si se equivoca hoy, ¿quién se entera, cuánto cuesta y cómo se revierte?". De ahí salen tres decisiones: dar solo los permisos que la tarea necesita, poner a una persona a aprobar lo que cuesta dinero, llega a un cliente o no se puede revertir, y dejar un registro de lo que hizo con una vuelta atrás probada. Un ejemplo hipotético: un agente que contesta correos de clientes puede leer el buzón y redactar borradores, pregunta antes de enviar o de ofrecer un descuento, y no toca pagos ni borra datos.

Es criterio de Plogy, no un resultado de la audiencia, y no es miedo: es lo mismo que haríamos con cualquier sistema que puede fallar.

¿Cuál fue el primer permiso que le retiraste, o le retirarías, a un agente que ya está en marcha?

#AgentesDeIA #GobernanzaDeIA


######## instagram · Automatizar lo que nadie eligió (kit 009) · 2206 car.
POR QUÉ: Una postura propia y discutible, dicha como postura: cambia el ahorro por la elección como criterio para decidir qué automatizar. Expone sus propios límites (la tarea que enseña el negocio, el tiempo liberado sin dueño) y rotula los ejemplos como genéricos. Frases cortas y afirmativas, con voz reconocible.

Lámina 1 (portada): Postura · Automatización
Nadie eligió esta parte de tu trabajo.
Y es la primera que conviene automatizar.

Lámina 2: Ejemplos
Tareas que nadie eligió.
- Pasar datos de un correo a una hoja
- Renombrar y archivar archivos
- Perseguir a alguien para que responda
- Armar el mismo reporte cada lunes
- Reenviar el mismo PDF a cada cliente
Alguien las hace cada semana. Ninguna es la razón por la que esa persona está en el equipo.

Lámina 3: Automatiza primero lo que nadie eligió.
¿Alguien eligió hacer esto?
No: candidata a automatizar.
Sí: habla primero con esa persona.

Lámina 4: No toda tarea aburrida sobra.
A veces es donde alguien aprende cómo funciona el negocio. Esa se entiende primero y se automatiza después.

Lámina 5: El tiempo que liberas necesita dueño.
[Esquema ilustrativo, sin cifras]
Si nadie decide en qué se usa, se llena con más tareas que nadie eligió.

Lámina 6: Dos preguntas distintas.
Automatizar para recortar: ¿Cuánto cuesta este trabajo?
Automatizar lo que nadie eligió: ¿En qué quieres que piense tu gente?
Plogy trabaja con la segunda.

Lámina 7 (cierre): Que la máquina repita. Tú decides.
Sigue a Plogy. Automatización con criterio, explicada sin humo.

Caption: ¿Qué automatizar primero en un negocio? Nuestra respuesta: lo que nadie eligió hacer. Copiar datos de un correo a una hoja, perseguir una confirmación, armar el mismo reporte cada lunes. Son tareas reales que alguien hace cada semana y que no son la razón por la que esa persona está en el equipo. Para aplicarlo, pide a tu equipo que durante una semana anote sus tareas repetitivas y marque con cuáles se quedaría si pudiera elegir. Las que nadie marca son las candidatas. Las que alguien marca se hablan primero con esa persona, y las que sirven para aprender el negocio se entienden antes de automatizarlas. Queda una decisión que conviene tomar a propósito: en qué se usa el tiempo que libera la automatización. Sin dueño, se llena con más tareas que nadie eligió. Los ejemplos de las láminas son genéricos, no de un cliente. Sigue a Plogy para ver cómo se implementa la IA en negocios, con criterio y sin humo.

Hashtags: #AutomatizacionConIA #IAParaNegocios #AutomatizacionDeProcesos


######## linkedin · Automatizar lo que nadie eligió (kit 009) · 1272 car.
POR QUÉ: Una postura propia y discutible, dicha como postura: cambia el ahorro por la elección como criterio para decidir qué automatizar. Expone sus propios límites (la tarea que enseña el negocio, el tiempo liberado sin dueño) y rotula los ejemplos como genéricos. Frases cortas y afirmativas, con voz reconocible.

Automatizar bien quita la parte del trabajo que nadie eligió. Esa definición tiene una consecuencia incómoda: el criterio para decidir qué automatizar deja de ser el ahorro y pasa a ser la elección.

Muchas conversaciones sobre automatización empiezan por cuánto cuesta hacer algo a mano. Es una pregunta legítima, pero lleva a automatizar lo más caro o lo más visible, aunque sea trabajo que alguien eligió y hace bien. Nuestra postura es empezar por otra pregunta: ¿alguien eligió hacer esto? Pasar datos entre sistemas, perseguir confirmaciones o rearmar un reporte idéntico cada lunes es trabajo que difícilmente alguien dice haber elegido. Eso se automatiza primero.

La regla es discutible y conviene dejar a la vista sus dos límites. Uno: una tarea que nadie eligió puede ser el lugar donde una persona aprende cómo funciona el negocio, y automatizarla antes de entenderla deja a la empresa sin ese conocimiento. Dos: el tiempo liberado no se convierte solo en trabajo de criterio. Si nadie decide en qué se usa, se llena con más tareas que nadie eligió.

Es una postura de Plogy, no un estudio ni un resultado medido con clientes. Los ejemplos son genéricos.

¿Qué tarea de tu equipo pasaría el filtro "nadie la eligió", y quién decidiría en qué se usa ese tiempo?


######## instagram · Un brief de web en seis campos (kit 010) · 2943 car.
POR QUÉ: Un método aplicable en seis campos que avanza de la tensión al concepto, al mecanismo y al ejemplo. El ejemplo está rotulado como hipotético y la prueba se separa de lo que no cuenta («La prueba no se inventa. Se junta.»). El cierre ofrece justo lo que la pieza enseñó.

Lámina 1 (portada): Guía · Web
Una web bonita no es un brief.
Es un deseo. Quien lo recibe, sea una IA o un equipo, adivina el resto.

Lámina 2: Una petición, tres webs distintas.
“Hazme una web bonita.”
[Tres versiones: sobria, llamativa y elegante]
Las tres son bonitas. Ninguna dice para qué.

Lámina 3: El brief cabe en seis campos.
1. Objetivo: qué debe lograr
2. Audiencia: quién entra
3. Oferta: qué ofreces
4. Prueba: qué lo demuestra
5. Acción principal: qué debe hacer
6. Restricciones: qué límites hay

Lámina 4: Cada campo se ve en la pantalla.
[Maqueta de una web con cada campo señalado]
Oferta: lo que ofreces, en una frase.
Audiencia: con las palabras de quien entra.
Acción principal: el botón «Agendar ahora».
Prueba: a la vista.
Objetivo y restricciones no se ven: se notan en lo que sobra y en lo que falta.

Lámina 5: La prueba no se inventa. Se junta.
Cuenta como prueba
Reseñas reales, con permiso
Trabajos hechos, con fotos propias
Garantías y certificaciones reales
Años de oficio, si son ciertos
No cuenta
“Somos los mejores.”
Cifras que no puedes mostrar
¿Aún no la tienes? Anótalo: es una tarea.

Lámina 6: Ejemplo hipotético. Antes: “Hazme una web bonita para mi clínica.”
Después, en seis campos:
Objetivo: Más citas de primera consulta
Audiencia: dueños de mascotas del barrio, que buscan desde el celular
Oferta: consulta y vacunas, con cita el mismo día
Prueba: reseñas reales y fotos propias de la clínica
Acción: agendar por WhatsApp
Restricciones: lista en cuatro semanas. Sin tienda en línea.
Clínica inventada para mostrar el brief. No es de ningún cliente.

Lámina 7: El brief también es el examen.
¿Se entiende la oferta de un vistazo? (Oferta)
¿La prueba está a la vista? (Prueba)
¿Se respetaron los límites acordados? (Restricciones)
¿La web logró la acción? (Acción principal) Cuenta cuántas personas la hicieron.

Lámina 8 (cierre): Primero el brief, después la web.
Comenta BRIEF y te mandamos la guía con la plantilla de brief y un ejemplo completo.

Caption: Para pedir una página web a una IA o a un equipo hace falta un brief, y un brief cabe en seis campos: objetivo, audiencia, oferta, prueba, acción principal y restricciones. Cada uno cierra una adivinanza que, si no se cierra, la resuelve quien construye por su cuenta. Una web se ve distinta según quien la entienda: con el mismo pedido salen una versión sobria, una llamativa y una elegante, y las tres cumplen. Con el brief, la oferta se vuelve el titular, la acción principal el botón que manda y la prueba (reseñas reales, trabajos con fotos propias) tiene su lugar. Cuando la web está lista, los mismos campos sirven de examen: la pregunta clave es cuántas personas hicieron la acción. El ejemplo de la lámina 6, una clínica con su brief, es hipotético: el negocio y los datos son inventados. Comenta BRIEF y te mandamos la guía con la plantilla de brief y un ejemplo completo.

Hashtags: #DisenoWeb #PaginaWebParaNegocios #BriefWeb


######## linkedin · Un brief de web en seis campos (kit 010) · 1403 car.
POR QUÉ: Un método aplicable en seis campos que avanza de la tensión al concepto, al mecanismo y al ejemplo. El ejemplo está rotulado como hipotético y la prueba se separa de lo que no cuenta («La prueba no se inventa. Se junta.»). El cierre ofrece justo lo que la pieza enseñó.

Una web se puede evaluar solo contra lo que se pidió. Si lo que se pidió fue "bonita", no hay contra qué evaluarla.

Cuando un negocio le encarga una web a una IA o a un equipo con una frase, quien la recibe completa los huecos: para quién es, qué se destaca, qué botón manda. Cada hueco es una decisión que alguien toma sin saberlo, y después aparece como una ronda de cambios.

Un brief de seis campos las anticipa. Objetivo: qué debe lograr la web. Audiencia: quién entra y qué resuelve. Oferta: qué se ofrece, en una frase. Prueba: qué evidencia real tiene el negocio, que se junta y no se inventa. Acción principal: una sola. Restricciones: plazo, presupuesto y límites.

Un ejemplo hipotético, con una clínica veterinaria inventada: de "hazme una web bonita" pasa a "más citas de primera consulta, para dueños de mascotas del barrio que buscan desde el celular, con reseñas reales y un único botón para agendar por WhatsApp". Con eso la oferta es el titular, el botón tiene dueño y la prueba tiene lugar.

El brief también sirve al final, como criterio de revisión: ¿se entiende la oferta?, ¿la prueba está a la vista?, ¿se respetaron los límites?, y sobre todo, ¿cuántas personas hicieron la acción? Es criterio de Plogy y todavía no lo hemos aplicado a un cliente. Preparamos una guía con la plantilla y un ejemplo completo.

De los seis campos, ¿cuál te costaría más llenar hoy para tu negocio?


######## instagram · ¿Automatización, asistente o agente? (kit 013) · 3225 car.
POR QUÉ: Un marco de decisión con un orden de preguntas que el lector aplica a su propio proceso. Separa la definición de la fuente (Anthropic, con su interés comercial declarado) del criterio de Plogy, y rotula los procesos como inventados. El CTA comercial abre una conversación sobre el proceso del lector, sin vender en las láminas.

Lámina 1 (portada): Guía · Decisión
¿Automatización, asistente o agente?
Tu proceso necesita uno. Subir de nivel cuesta más y arriesga más.
1. Automatización 2. Asistente 3. Agente

Lámina 2: Cambia quién decide los pasos.
Automatización: reglas fijas. Los mismos pasos, siempre, aunque uno use IA.
Decide: las reglas.
Asistente: una persona pide y la IA responde. La persona decide qué hacer.
Decide: la persona.
Agente: la IA decide los pasos y usa herramientas para actuar.
Decide: la IA.
Agente según Anthropic: el modelo dirige sus propios procesos y herramientas. Anthropic las vende.

Lámina 3: Cuatro preguntas deciden el nivel.
1. ¿Los pasos son siempre iguales? Si sí, bastan reglas.
2. ¿Hay que juzgar? Leer, interpretar o redactar pide un modelo.
3. ¿Tiene que actuar sobre sistemas? Enviar, cobrar o cambiar datos sube el nivel.
4. ¿Qué pasa si se equivoca? Define cuánto control humano lleva.

Lámina 4: Responde en este orden.
1. ¿Los pasos son siempre iguales? Sí: automatización.
2. ¿Hay que juzgar? No: automatización con condiciones.
3. ¿Actúa sobre sistemas? No: asistente.
4. ¿Qué pasa si se equivoca? Agente. Si cuesta caro, una persona aprueba.

Lámina 5: Ejemplo hipotético
Tres procesos, tres niveles.
Guardar cada factura que llega por correo y anotarla en una hoja.
→ Automatización
Redactar respuestas a clientes que preguntan cosas distintas.
→ Asistente
Gestionar un reclamo: leer el caso, revisar el pedido y reembolsar.
→ Agente con aprobación humana
Procesos inventados, no son de ningún cliente.

Lámina 6: Sube de nivel solo si el anterior no alcanza.
Automatización: predecible.
Asistente: flexible, con una persona al mando.
Agente: más flexible. También más costo y errores que se acumulan.
“Buscar la solución más simple posible y subir la complejidad solo cuando haga falta.” Anthropic, Building effective agents, 2024 (traducción de Plogy). Anthropic vende herramientas de agentes.

Lámina 7 (cierre): Ponle nivel a tu proceso.
Cuéntanos qué proceso es y vemos qué nivel pide.
Escríbenos PROCESO por DM.

Caption: Antes de montar un agente de IA, mira si tu proceso no se resuelve con una automatización o con un asistente. Son tres niveles distintos y cada proceso de un negocio pide uno. Lo que los separa es quién decide los pasos. En una automatización los decide una regla y son siempre los mismos, aunque uno de ellos use IA para clasificar un correo. En un asistente una persona pide y la IA responde; la persona decide qué hacer con eso. En un agente la IA decide los pasos y usa herramientas para actuar. Esa última definición es la de Anthropic en su guía "Building effective agents" (2024). Ojo: Anthropic vende modelos y herramientas para agentes, así que la usamos como definición. Los tres niveles y el orden de decisión son criterio de Plogy. Cuatro preguntas, en este orden: ¿los pasos son siempre iguales?, ¿hay que juzgar?, ¿tiene que actuar sobre sistemas?, ¿qué pasa si se equivoca? Los tres procesos de la lámina 5 son ejemplos hipotéticos, no de un cliente. Y la regla de la lámina 6: sube de nivel solo si el anterior no alcanza. Escríbenos PROCESO por DM y cuéntanos qué proceso quieres automatizar.

Hashtags: #AutomatizacionConIA #AgentesDeIA #IAParaNegocios


######## linkedin · ¿Automatización, asistente o agente? (kit 013) · 1761 car.
POR QUÉ: Un marco de decisión con un orden de preguntas que el lector aplica a su propio proceso. Separa la definición de la fuente (Anthropic, con su interés comercial declarado) del criterio de Plogy, y rotula los procesos como inventados. El CTA comercial abre una conversación sobre el proceso del lector, sin vender en las láminas.

Antes de preguntarte si tu proceso necesita un agente de IA, pregúntate cuál es el nivel más bajo que lo resuelve.

Hay tres niveles y se distinguen por quién decide los pasos. Una automatización sigue reglas fijas: los pasos son siempre los mismos, y puede incluir un paso con IA, como clasificar un correo, sin dejar de ser automatización. Un asistente responde a lo que una persona le pide, y esa persona decide qué hacer con la respuesta. Un agente decide los pasos por su cuenta y usa herramientas para actuar.

La definición de agente es la de Anthropic en "Building effective agents" (19 de diciembre de 2024). Anthropic vende modelos y herramientas para agentes, así que la usamos como definición y no como argumento de venta. La misma guía recomienda buscar la solución más simple posible y advierte que la autonomía de un agente implica más costos y la posibilidad de errores que se acumulan. La separación en tres niveles y las preguntas de abajo son criterio de Plogy, no de esa guía.

Subir de nivel compra flexibilidad y cobra costo y riesgo. Por eso el orden importa:

1. ¿Los pasos son siempre iguales? Si sí, reglas.
2. ¿Hay que juzgar? Si no, reglas con condiciones.
3. ¿Tiene que actuar sobre sistemas? Si no, un asistente alcanza.
4. ¿Qué pasa si se equivoca? Si cuesta caro, el agente necesita una persona que apruebe el paso final.

Ejemplos hipotéticos: guardar las facturas que llegan por correo es una automatización. Redactar respuestas a clientes que preguntan cosas distintas es un asistente. Gestionar un reclamo que termina en un reembolso es un agente, con aprobación humana antes de pagar.

¿Cuál de tus procesos tiene hoy pasos que cambian en cada caso y un error costoso? Ese es el que más criterio pide antes de automatizarlo.


######## instagram · Otro agente calificó nuestras piezas (kit 014) · 3425 car.
POR QUÉ: Documental con evidencia propia: cuenta un trabajo real de Plogy con cifras que se pueden recontar, incluidos sus fallos (17 = 17; 3, 3 y 4). Una idea por lámina, la fuente al pie y una regla de trabajo como conclusión. Muestra el proceso con sus errores, que es justo lo que promete el CTA de seguir.

Lámina 1 (portada): Building Plogy · Revisión editorial
Le pedimos a un agente que calificara nuestras cinco piezas.
Cuatro recibieron «Mejorar antes de seguir». Una, «Publicar con ajustes».

Lámina 2: Un revisor que juzga. No corrige ni publica.
Un revisor por pieza, sin ver el razonamiento de quien la escribió.
17 criterios, cada uno con nota de 1 a 5. No hay nota global.
10 reglas duras de cumple o falla. Una falla impide «Publicar con ajustes».
El 3 es la nota de lo correcto pero genérico. Un 5 es raro.
Fuente: SKILL.md y RUBRICA.md de plogy-editorial-review, CALIBRACION.md y plogy-revisor-editorial.md.

Lámina 3: Una sola salió «Publicar con ajustes». Al repetir, bajó.
[Tabla con la primera y la segunda revisión de las piezas 001 a 005]
Mejorar = «Mejorar antes de seguir». Publicar = «Publicar con ajustes». Informes del 2026-10-20; 001 y 002 solo tienen una revisión.

Lámina 4: Lo que confirmó leyendo la fuente.
002 (sin corregir): Dijimos que los dos bancos permiten ver saldos. La fuente lo dice de Schwab.
003 (corregido): Pusimos «razonamiento alto» a todos los modelos. La fuente dice «max» para GPT-6 Astra.
003 (a medias): Dimos el 1 de diciembre como fecha firme. Ninguna fuente la confirma con Google.
004 (corregido): «25 veces menos» valía solo frente a GPT-4o. Frente a GPT-4o mini, 1,5.
Estado según los archivos actuales de cada pieza.

Lámina 5: Y lo que vio en nuestras láminas.
005 · lógica invertida (corregido): «En el ejemplo ocurre lo contrario: el reproceso baja de 8 a 4 casos, así que omitirlo subestima el ahorro.»
005 · cuatro, eran tres (corregido): «En la lámina 7 la mesa tiene tres personas visibles.» El brief decía cuatro.
001 · cifra sin explicar (sin corregir): «“6 formas de anotar” a partir de tres canales no se explica (¿por qué seis?)»
Citas textuales de revision-editorial.md y revision-editorial-2.md.

Lámina 6: El revisor también falló.
17 = 17. Mismas notas, otro veredicto. Dos revisiones de 005 con las mismas 17 notas: «Publicar con ajustes» y «Mejorar antes de seguir».
3, 3 y 4. Sin regla para el recurso en borrador. Nota de CTA en 003, 004 y 005, con el recurso en borrador en las tres.
«No los leí». Fuentes de terceros sin leer. Así lo dijo la 1.ª revisión de 004 sobre Mixed y Digital Applied.
Y la columna «Veredicto de la persona» de CALIBRACION.md sigue vacía.

Lámina 7 (cierre): Quien escribe la pieza no la califica.
Sigue a Plogy. Aquí mostramos el proceso, con sus errores.

Caption: Le pedimos a un agente de IA que hiciera la revisión editorial de nuestras cinco primeras piezas, con una rúbrica de 17 criterios y 10 reglas duras. No escribe ni publica: califica y explica por qué. Cuatro piezas salieron «Mejorar antes de seguir» y una, «Publicar con ajustes». Al repetir la revisión, esa también bajó. En el camino confirmó errores contra las fuentes: un nivel de razonamiento puesto a todos los modelos, una fecha dada como firme, un «25 veces menos» que solo valía frente a un modelo y una figura con la lógica al revés. Corregimos la mayoría. Otros siguen abiertos y los marcamos en el carrusel. El revisor también falló: con las mismas notas dio dos veredictos distintos, y la rúbrica no decía qué hacer con un recurso en borrador. Un agente revisor ayuda, pero la decisión de publicar sigue siendo de una persona. Sigue a Plogy. Aquí mostramos el proceso, con sus errores.

Hashtags: #AgentesDeIA #AutomatizacionConIA #BuildingInPublic


######## linkedin · Otro agente calificó nuestras piezas (kit 014) · 1509 car.
POR QUÉ: Documental con evidencia propia: cuenta un trabajo real de Plogy con cifras que se pueden recontar, incluidos sus fallos (17 = 17; 3, 3 y 4). Una idea por lámina, la fuente al pie y una regla de trabajo como conclusión. Muestra el proceso con sus errores, que es justo lo que promete el CTA de seguir.

Un agente revisor encontró errores que nuestro propio control no vio. También se contradijo.

El 20 de octubre de 2026 le pedimos a un agente de IA, distinto del que escribe las piezas, que calificara las cinco primeras de este kit de contenido. Trabaja con una rúbrica de 17 criterios y 10 reglas duras, no da nota global y no puede publicar. Dejó ocho informes: cinco primeras revisiones y tres segundas (003, 004 y 005).

Lo útil fue que leyó las fuentes y las puso al lado de nuestras láminas. De los trece hallazgos de hecho que registramos en el brief, siete están corregidos, uno quedó a medias y cinco siguen abiertos. Entre ellos, una fecha dada como firme sin confirmación y una comparación de precio que valía solo frente a un modelo.

Lo que no funcionó también cuenta. En la pieza 005, las dos revisiones dieron las mismas 17 notas y veredictos distintos. La rúbrica no define qué hacer con un recurso en borrador, y por eso la misma situación recibió 3, 3 y 4 en el criterio de CTA. Un revisor dijo no haber leído dos fuentes de terceros que la pieza citaba. Y nadie de Plogy ha anotado todavía su veredicto en el archivo de calibración.

Lo que sacamos, como criterio y no como resultado probado: quien escribe no califica; antes de revisar hay que escribir qué significa cada veredicto, con umbrales; conviene comprobar qué fuentes leyó el revisor y cuáles no; y publicar sigue siendo una decisión humana.

¿Qué regla le pondrías a un agente revisor antes de dejarlo opinar sobre tu contenido?
