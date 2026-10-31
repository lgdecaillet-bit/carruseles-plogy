# El prompt para armar tu dashboard con Claude

Estado: BORRADOR para revisión humana. No enviar hasta aprobar. Aprobación humana y fecha: PENDIENTE.

Extra opcional: ya no es el recurso del CTA (la pieza ahora lleva a la clase con "Comenta CLAUDE"). Se puede mandar en el segundo mensaje del DM. Funciona en claude.ai: Claude arma el dashboard como una página interactiva que puedes ver en la misma conversación.

## Antes de empezar

1. **Elige la pregunta.** Un dashboard sin pregunta es una pantalla bonita que nadie mira. Elige una de las seis de abajo o escribe la tuya.
2. **Junta los datos.** Una planilla (Excel, Google Sheets exportado a CSV) con una fila por venta, pago, pedido o lo que corresponda. No hace falta que esté perfecta.
3. **Quita lo sensible.** Antes de subir el archivo, borra o reemplaza nombres de clientes, documentos de identidad, teléfonos y cualquier dato que no deba salir de tu empresa. Revisa también qué permite la política de datos de tu plan de Claude.

## El prompt

Copia esto, completa lo que está entre corchetes y adjunta tu archivo:

```
Quiero un dashboard para responder esta pregunta de mi negocio:
[pega aquí la pregunta]

Mi negocio: [qué vendes, a quién, y cuántas personas trabajan]
Te adjunto: [nombre del archivo] con [qué tiene cada fila y qué columnas importan]
Periodo: [por ejemplo, octubre de 2026]

Antes de construir nada:
1. Revisa el archivo y dime qué columnas vas a usar, qué datos faltan o se ven raros.
2. Propón máximo 3 indicadores y 2 gráficos que respondan la pregunta. Nada más.
3. Espera mi confirmación.

Cuando confirme, arma el dashboard como una página interactiva:
- Arriba, los indicadores con su comparación contra el periodo anterior o contra la meta.
- Un aviso en color cuando algo pase el límite que te indique: [tu límite, por ejemplo "caja bajo $5.000"].
- Abajo, un texto corto con lo que el dashboard muestra y qué revisaría primero.
- No inventes datos. Si un cálculo depende de un supuesto, escríbelo debajo del gráfico.
```

## Las seis preguntas del carrusel

Elige una y pégala en el prompt, junto con su límite:

| Dashboard | Pregunta | Datos que necesitas | Límite de ejemplo para el aviso |
|---|---|---|---|
| Ejecutivo | ¿Cómo va el negocio este mes? | Ventas y gastos del mes | Avance de la meta bajo el 60% a mitad de mes |
| Ventas | ¿Quién llega a la meta y quién no? | Ventas con el nombre de quien vendió y la meta de cada persona | Alguien bajo el 80% de su meta |
| Caja | ¿Me alcanza la caja para el próximo mes? | Cobros y pagos pendientes con su fecha, y el saldo de hoy | Saldo proyectado bajo tu mínimo |
| Marketing | ¿Qué canal me trae clientes que pagan? | Inversión por canal y de qué canal vino cada cliente | Costo por cliente sobre tu máximo |
| Operaciones | ¿Dónde se traban mis pedidos? | Pedidos con la fecha en que pasaron por cada etapa | Pedidos con más de 3 días en una etapa |
| Gasto en IA | ¿Cuánto gasta mi equipo en IA, y en qué? | El reporte de consumo de tu proveedor de IA, con área o persona | Un área sobre su presupuesto mensual |

## Después

- Pídele a Claude que te explique cada número. Si no puedes explicar un indicador en una frase, sácalo.
- Mira el dashboard una vez por semana, a la misma hora. Si en un mes no cambió ninguna decisión, cambia la pregunta.
- Para que se actualice solo hace falta conectar la fuente de datos. Ese es otro paso: escríbenos si quieres hacerlo.

Plogy
