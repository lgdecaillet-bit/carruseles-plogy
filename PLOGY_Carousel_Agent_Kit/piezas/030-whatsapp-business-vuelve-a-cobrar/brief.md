# Brief · pieza 030 · WhatsApp Business vuelve a cobrar

Estado: BORRADOR para revisión humana. No publicar. Aprobación humana y fecha: PENDIENTE.

## Qué es

- Publicación sugerida: Martes 27 de octubre.
- Tipo dentro de la semana: Noticia (60%).
- Pilar: Conocimiento: noticia explicada. Audiencia: Negocios.
- Fuente editable: `generar.py` (usa la plantilla `../_comun/plogy.py`) genera `carrusel.html`. Exportar con `python _comun/render.py 030-whatsapp-business-vuelve-a-cobrar` desde `piezas/`.

## Secuencia

| # | Lámina |
|---|---|
| 1 | Portada: factura de WhatsApp Business (ilustración) |
| 2 | Qué cambió el 1 de octubre |
| 3 | 1.000 mensajes gratis por número |
| 4 | El agente de IA se cobra por tokens |
| 5 | Ventana de 7 días de los anuncios |
| 6 | Criterio |
| 7 | CTA Sigue a Plogy |

## CTA

Seguimiento. Sigue a Plogy, foto 14 de la biblioteca (andén).

## Hechos que la pieza afirma

- Fuente: https://developers.facebook.com/docs/whatsapp/pricing/updates-to-pricing (verificada el 26 oct 2026).
- Misma página: "Service messages, which became free as of Nov. 1, 2024" (respaldo de 'desde nov 2024').
- Servicio: se cobra "as of 12am by Messaging account timezone on October 1, 2026".
- "Meta provides every business phone number with a free tier of 1,000 service messages per month." "Unused service messages in the free tier do not roll over to the next month."
- Utility en respuesta a usuarios: pasa de `free_customer_service` a `regular` desde el 1 oct 2026.
- Meta Business Agent: "One global rate of $2.00 USD per 1 million (M) tokens." "One message typically consumes 20,000–25,000 tokens, which translates to approximately 4–5 cents (USD) per message." Ejemplos de Meta: consulta simple de 4 mensajes 16 a 20 ¢; compleja de 10, 40 a 50 ¢.
- Ventana FEP: "may remain open for up to 7 days"; sin cobro para marketing, utilidad, autenticación y servicio; "Meta continues to charge for Meta Business Agent messages in the FEP window". Solo desde las apps de Android e iOS.
- Alcance: la página cubre Cloud API y Marketing Messages API. No menciona la app gratuita de WhatsApp Business (la lámina 2 lo dice así).

## Fotos e imágenes

- Portada: `cta-biblioteca/assets/24-telefono.jpg` (collage de la biblioteca).
- Criterio: moodboard `assets/reference-originals/scrolling through social media.jpg` en duotono.
- Derivados hechos con `_comun/fotos.py` (duotono Ink, naranja y crema, o corrección cálida). Los originales no se tocan.

## Pendientes antes de publicar

- La noticia es del 1 de octubre, fuera de la ventana estricta. Se eligió por impacto directo en negocios que venden por WhatsApp.
- Tarifa por país para Colombia: no se revisó. Si se quiere sumar, está en la tabla de precios de Meta.
- Derechos de las fotos del moodboard y del CTA: `unverified_reference_only`. Las fotos reales de clases necesitan el consentimiento de las personas que aparecen (mismo pendiente de la pieza 022).
- Prueba en teléfono, revisión editorial independiente y aprobación humana con fecha.
