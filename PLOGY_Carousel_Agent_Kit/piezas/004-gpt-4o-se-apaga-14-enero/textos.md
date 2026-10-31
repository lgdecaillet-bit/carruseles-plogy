# Textos por canal · pieza 004

Estado: BORRADOR para revisión humana. No publicar.

## Caption de Instagram

OpenAI sacará GPT-4o, GPT-4o mini, GPT-4.1 y GPT-4.1 mini de su API el 14 de enero de 2027. Avisó el 14 de octubre, con 92 días de margen, y recomienda pasar a gpt-6-luna.

Si tu negocio tiene una automatización que llama a uno de esos modelos, hay que revisarla antes. Según la ficha de OpenAI, gpt-6-luna razona por defecto, solo admite llamadas a funciones en Chat Completions con el razonamiento apagado y no admite fine-tuning. Es mucho más barato por token que GPT-4o, pero eso no dice cuánto costará una tarea. Lo primero es saber en qué lugares aparece el nombre del modelo: código, herramientas, proveedores y tareas programadas.

Fuente: página de deprecaciones de OpenAI, aviso del 14 de octubre de 2026.

Comenta MIGRAR y te mandamos la noticia completa y nuestra lista de revisión.

#AutomatizacionConIA #IAParaNegocios #OpenAI

### Hashtags elegidos y razón

- #AutomatizacionConIA: la vertical de Plogy y el tema de la pieza.
- #IAParaNegocios: marca la audiencia.
- #OpenAI: el nombre que la gente busca en esta noticia.
- Tres de cinco posibles. Decisión deliberada: más no añadirían precisión.

## Post de LinkedIn

Un modelo de IA es una dependencia de tu automatización, y las dependencias vencen.

El 14 de octubre de 2026 OpenAI avisó de que retira de su API cinco versiones de GPT-4o y GPT-4.1 el 14 de enero de 2027, junto con las versiones afinadas de esos modelos. Recomienda pasar a gpt-6-luna. Del aviso al apagado pasan 92 días, y la política de OpenAI para modelos de disponibilidad general habla de al menos seis meses, aunque su página no aclara si estos lo son.

Para un negocio, lo delicado es que el reemplazo no es un cambio de nombre. Según la ficha de OpenAI, gpt-6-luna razona por defecto con esfuerzo medio, solo admite llamadas a funciones en Chat Completions con el razonamiento apagado, y no admite fine-tuning. Su precio por token es menor que el de GPT-4o (hasta 25 veces en entrada, solo 1,5 veces frente a GPT-4o mini), pero el razonamiento se factura como tokens de salida, así que lo que cuesta una tarea hay que medirlo.

No hemos migrado ningún flujo a este modelo, y no sabemos cómo se comportará el tuyo. Lo que haríamos primero, como criterio y no como garantía:

1. Un inventario de dónde aparece el nombre del modelo: código, herramientas sin código, proveedores, variables y tareas programadas.
2. Una ficha por uso: si llama funciones, si usa un fine-tune y quién responde por él.
3. Pruebas con casos reales y un plan de vuelta atrás hasta el último día.

Un ejemplo hipotético: una automatización de atención al cliente que consulta pedidos con llamadas a funciones sobre un modelo mini puede pasar sin tocar código si el razonamiento queda apagado, o requerir la Responses API si se quiere razonar. En los dos casos hay que probar antes de la fecha.

¿Sabes en cuántos lugares aparece hoy el nombre del modelo que usan tus automatizaciones?

## Diferencia de enfoque entre canales

Instagram parte del hecho (la fecha y los modelos), lo traduce a una acción simple (saber dónde está el modelo) y cierra con el CTA de palabra clave ("Comenta MIGRAR"). LinkedIn parte de la tesis (un modelo es una dependencia que vence), explica por qué el reemplazo no es un cambio de nombre, ofrece tres pasos y un ejemplo hipotético, y cierra con una pregunta sustantiva. En LinkedIn no hay comentario a DM: el enlace al reporte se puede poner con los UTM de LinkedIn cuando exista. No comparten estructura ni CTA.
