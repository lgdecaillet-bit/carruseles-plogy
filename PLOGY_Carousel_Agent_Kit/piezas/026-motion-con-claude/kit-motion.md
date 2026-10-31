# Kit Plogy · Motion con Claude

Estado: BORRADOR para revisión humana. Es el recurso que se manda por DM a quien comenta MOTION.

Tres piezas: el archivo de estilo (tu marca), el brief de movimiento (cómo se anima) y 16 líneas de escena (lo único que cambias). Pegas las tres en Claude y te devuelve una animación que puedes abrir en el navegador y grabar.

## Cómo usarlo

1. Abre Claude (claude.ai o Claude Code).
2. Pega el **archivo de estilo** con tus colores y letras.
3. Debajo, pega el **brief de movimiento** tal cual.
4. Al final, pega **una línea de escena** y cambia lo que está entre corchetes.
5. Abre el archivo HTML que te entrega en el navegador. Para tenerlo en video, grábalo con la grabadora de pantalla o pídele a Claude que lo exporte a MP4.

Si tienes Claude Motion (beta en planes Team y Enterprise), también puedes pedirlo ahí y exportar el MP4 directo.

---

## 01 · El archivo de estilo

```
ESTILO DE MARCA
Marca: [nombre]
Fondo claro: [#ffffff]   Fondo oscuro: [#171310]
Texto: [#171310]   Texto suave: [#625951]
Acento: [#ff5b00]
Degradado de marca: [#ff5b00 → #e1556a → #9c5aa7]
Titulares: [fuente, peso]   Texto: [fuente]
Esquinas: redondeadas, [24] px en tarjetas.
Sombras: suaves y difusas, nunca negras duras.
Nada de colores fuera de esta lista.
```

## 02 · El brief de movimiento

```
BRIEF DE MOVIMIENTO
Haz una sola escena animada en un archivo HTML que se abra en el navegador.
- Lienzo de 1080x1350 (vertical, formato de carrusel), escena centrada.
- Dibuja con canvas o SVG. Sin librerías externas salvo la fuente.
- Dura 6 segundos y se repite en bucle sin salto: el último cuadro empalma con el primero.
- Todo se mueve en función del tiempo, con curvas suaves (ease-in-out), nunca lineal ni brusco.
- Un solo foco de movimiento. Nada parpadea más de una vez.
- Respeta el archivo de estilo: solo esos colores y esas fuentes.
- Si hay cifras o nombres de clientes, son de ejemplo: agrega una etiqueta pequeña "Ilustración".
- Entrega el archivo completo y dime cómo cambiar el texto de la escena.
```

## 03 · Las 16 líneas de escena

Elige una, pégala al final y cambia lo que está entre corchetes.

1. **Partículas → logo.** Unos 600 puntos pequeños en los colores del degradado entran desde los bordes, forman [tu logo o tu marca, en una línea], brillan una vez, estallan en un anillo y se van.
2. **Degradado → flujo.** Un degradado inclinado llena el cuadro. Franjas de color lo recorren como líquido lento, con "[una palabra]" en texto pequeño arriba a la izquierda.
3. **Vidrio → giro.** Una tarjeta de vidrio esmerilado con [tu dato: una factura, un pedido, un cliente] gira suave en 3D sobre colores que se mueven en fondo oscuro, y una franja de luz cruza su cara.
4. **Globo → arcos.** Un globo de puntos sobre fondo oscuro da una vuelta por ciclo. Arcos en degradado viajan entre [tres ciudades] y aterrizan con un pulso.
5. **Línea → dibujo.** Una tarjeta con "[tu métrica]" y la cifra "[tu número]". Una línea en degradado se dibuja de izquierda a derecha con la punta brillante, el área de abajo se llena y al final aparece un chip "[+x%]".
6. **Forma → cambio.** Una forma brillante en degradado pasa de círculo a cuadrado, a estrella, a gota y vuelve a círculo. Una etiqueta pequeña dice el nombre de cada forma. Sombra suave debajo.
7. **Puntos → ola.** Una superficie 3D de puntos pequeños se mueve como un mar en calma sobre fondo claro. El color sigue la altura: [color 1] en los valles, [color 2] en las crestas.
8. **Tarjetas → abanico.** Una pila de cinco tarjetas de [tus pedidos, clientes o productos] se abre en abanico, se cierra, y la de arriba sale y vuelve a su lugar.
9. **Número → contador.** Una tarjeta "[tu etiqueta]". La cifra "[tu número]" sube desde cero como un odómetro, con desenfoque en los dígitos rápidos, y sigue sumando en vivo. Un chip "[+x% vs año anterior]" y una fila de barras debajo.
10. **Cinta → giro.** Una cinta de unas 26 hebras finas en degradado se tuerce en 3D sobre fondo oscuro, con luz distinta por delante y por detrás.
11. **Líquido → unión.** Gotas de metal líquido en [los colores de tu marca], iluminadas desde arriba a la izquierda, se juntan en una sola y se vuelven a separar. Sombra suave debajo.
12. **Teléfono → capas.** Un teléfono isométrico se separa en las capas de [la pantalla de tu app] (fondo, tarjeta, textos, botón), las capas flotan y vuelven a encajar.
13. **Anillos → órbita.** Un núcleo brillante en degradado sobre fondo oscuro con tres órbitas inclinadas. Lunas pequeñas pasan por delante y por detrás del núcleo.
14. **Palabras → golpe.** "[LÍNEA UNO] [LÍNEA DOS] [LÍNEA TRES]" entra línea por línea en letra gruesa, la última palabra en degradado, sale hacia arriba y "[tu segunda frase]" hace lo mismo. Un contador 01/02 en la esquina.
15. **Botón → pago.** Un botón "Pagar [tu monto]" con candado. Un puntero se acerca y lo presiona, se vuelve un círculo de carga, el anillo se llena, aparece un check con destellos y vuelve como "Pagado [tu monto]".
16. **Confeti → festejo.** Un botón redondo en degradado con un check blanco. Explota, unos 70 papelitos salen, revolotean y caen, y debajo aparece "[tus palabras]".

---

## Nuestro criterio

Una animación bonita no explica nada sola. Antes de elegir la escena, decide qué dato tiene que ver tu cliente: la venta del mes, el pedido confirmado, el pago recibido. El movimiento solo lo señala.

Si quieres que armemos las de tu negocio con tus datos reales, escríbenos.
