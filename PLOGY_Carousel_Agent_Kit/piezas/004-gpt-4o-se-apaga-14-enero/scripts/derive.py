# Derivado de foto de la pieza 004. El original no se toca.
# Uso: python -I derive.py "<ruta del kit>" "<carpeta assets de la pieza>"
import colorsys
import sys
from PIL import Image

kit, out = sys.argv[1], sys.argv[2]
ref = kit + "/assets/reference-originals/"

# Lámina 01: coding.jpg (1121x1494). Computador viejo con un ojo en la pantalla, tono verde azulado.
# Se recorta la zona del monitor y el teclado (4:3.33 aprox.), se desatura todo lo que no sea la pantalla roja
# y los rojos se llevan al naranja de marca (hue ~0.058). El resto queda en grises cálidos sobre Ink.
im = Image.open(ref + "coding.jpg").convert("RGB").crop((0, 250, 1121, 1210))
w, h = im.size
px = im.load()
for y in range(h):
    for x in range(w):
        r, g, b = px[x, y]
        hh, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        red = (hh < 0.08 or hh > 0.90) and s > 0.28 and v > 0.18
        if red:
            hh = 0.058
            s = min(1.0, s * 1.3)
            v = min(1.0, v * 1.6)
        else:
            s = s * 0.12
            hh = 0.07
        r2, g2, b2 = colorsys.hsv_to_rgb(hh, s, v)
        px[x, y] = (int(r2 * 255), int(g2 * 255), int(b2 * 255))
im = im.resize((1080, round(h * 1080 / w)), Image.LANCZOS)
im.save(out + "/01-pc-viejo.jpg", quality=92)
print("ok", im.size)
