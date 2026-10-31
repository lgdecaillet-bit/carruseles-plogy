# Brief · pieza 026 · Motion con Claude

Estado: BORRADOR para revisión humana. No publicar. Aprobación humana y fecha: PENDIENTE.

## Qué es

Tercera de la tanda de adaptaciones. La referencia (otra cuenta, en inglés) muestra 16 efectos de movimiento hechos con Claude, cada uno con su línea de prompt para copiar, y cierra con "Comenta STRIPE" para mandar el archivo de estilo y el brief. Sus láminas son animadas.

**Qué cambiamos:**
- Las 16 escenas están hechas por nosotros desde cero con Claude Code: código HTML y canvas, sin copiar las de la referencia. Paleta de Plogy (Ink, crema y el degradado del logo, naranja a violeta) en vez de azul marino y morado.
- Escenas llevadas a negocio: las partículas forman "Plogy", la línea son las ventas del mes, el contador la facturación del año, la tarjeta de vidrio una factura, las tarjetas pedidos del día, el globo pagos entre Bogotá, Ciudad de México y Madrid, el botón "Pagar $48.000" y el confeti "Pedido confirmado".
- Prompts en español, con los corchetes para cambiar.
- La referencia usaba el estilo de otra marca (Stripe, leído de su código). Nosotros no: el archivo de estilo es el de quien lo usa.
- Sumamos una lámina de criterio (18) y el CTA de Plogy con tarjeta de vidrio sobre foto.

**Criterio propio de Plogy (lámina 18):** una animación bonita no explica nada sola. Antes de pedir el movimiento, decide qué dato tiene que ver tu cliente; el movimiento solo lo señala.

## Formato

19 láminas de 1080x1350. Cada una es un MP4 de 6 segundos que se repite sin salto (`exports/slide-NN.mp4`) y tiene un PNG fijo (`exports/slide-NN.png`). La fuente es `carrusel.html`: cada escena se dibuja en función del tiempo y `scripts/capturar.py` la graba cuadro por cuadro (Playwright con Edge y ffmpeg). Abrir `carrusel.html` en el navegador muestra las animaciones en vivo.

## Hechos que la pieza afirma

- "Hecho con Claude Code": cierto, las escenas las escribió Claude Code en esta sesión.
- Claude Motion: no se usó. Si se menciona (en el kit), es como alternativa, con su estado verificado en la pieza 019: beta solo para Team y Enterprise.
- Cifras de negocio (ventas, facturación, factura, pedidos, pago): ejemplos rotulados "Ilustración" en cada lámina donde aparecen.

## CTA y recurso

Comenta MOTION → DM con `kit-motion.md`: archivo de estilo con corchetes, brief de movimiento y las 16 líneas de escena. Ojo: la pieza 019 ya usa MOTION (para el link de la clase). Ver pendientes.

## Autor y cuentas

Cada lámina lleva al pie una barra con la foto y el usuario de Luco (@lucogav8). La pieza se sube en Plogy y en la cuenta personal (por ejemplo como colaboración de Instagram), con la misma versión. La foto sale del perfil de Instagram (`assets/av-autor.png`).

## Pendientes antes de publicar

- La pieza 019 (Claude Motion) también usa "Comenta MOTION", pero para la clase. Si las dos salen, cambiar la palabra de una.
- Publicar el kit en un enlace y configurar la respuesta automática.
- Probar el kit: pegar estilo + brief + una línea en Claude y comprobar que la escena sale.
- Derechos de la foto `assets/19-columnas.jpg` (variante 06 de la biblioteca): `unverified_reference_only`.
- Revisar en un teléfono que los videos se vean nítidos y que la caja de prompt se lea.
- Licencias tipográficas, revisión editorial independiente y aprobación humana con fecha.
