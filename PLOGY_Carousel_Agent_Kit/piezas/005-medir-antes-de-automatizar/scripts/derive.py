# Derivado de foto de la pieza 005. El original no se toca.
# Uso: python -I derive.py "<ruta del kit>" "<carpeta assets de la pieza>"
import colorsys
import sys
from PIL import Image

kit, out = sys.argv[1], sys.argv[2]
ref = kit + "/assets/reference-originals/"

# Lámina 07 y reporte: decission making team.jpg (736x741). Mesa roja con rejilla vista desde arriba y cuatro personas.
# Se recorta hasta el borde inferior de la mesa (y=582), así la persona de abajo queda fuera y la rejilla completa a la vista.
# El rojo se lleva al naranja de marca (hue ~0.058). El fondo claro y las personas en grises no se tocan.
im = Image.open(ref + "decission making team.jpg").convert("RGB").crop((0, 0, 736, 582))
px = im.load()
w, h = im.size
for y in range(h):
    for x in range(w):
        r, g, b = px[x, y]
        hh, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        if (hh < 0.05 or hh > 0.93) and s > 0.35:
            hh = 0.058
            r2, g2, b2 = colorsys.hsv_to_rgb(hh, s, v)
            px[x, y] = (int(r2 * 255), int(g2 * 255), int(b2 * 255))
im = im.resize((1000, round(h * 1000 / w)), Image.LANCZOS)
im.save(out + "/07-cta-mesa.jpg", quality=92)
print("ok", im.size)
