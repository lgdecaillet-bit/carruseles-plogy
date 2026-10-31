# Derivados de foto de la pieza 002. Los originales no se tocan.
# Uso: python -I derive.py "<ruta del kit>" "<carpeta assets de la pieza>"
import sys, colorsys
from PIL import Image

kit, out = sys.argv[1], sys.argv[2]
ref = kit + "/assets/reference-originals/"
INK = (23, 19, 16)

# Lámina 01: ai watching.jpg (1200x1200). Se recorta fuera el logo de otra marca (esquina superior izquierda, y < 130).
# Franja y 300-1060 con las tres figuras. Los grises se invierten y se mapean de Ink a blanco para fundirse con el fondo.
# Los píxeles con color (cajas rojas "UNKNOWN") se desplazan al Orange de Plogy (matiz ~21 grados).
im = Image.open(ref + "ai watching.jpg").convert("RGB").crop((0, 300, 1200, 1060))
im = im.resize((1080, round(760 * 1080 / 1200)), Image.LANCZOS)
px = im.load()
w, h = im.size
for y in range(h):
    for x in range(w):
        r, g, b = px[x, y]
        hh, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        if s > 0.35 and (hh < 0.05 or hh > 0.95):
            r2, g2, b2 = colorsys.hsv_to_rgb(0.058, min(1.0, s * 1.05), min(1.0, max(v, 0.85)))
            px[x, y] = (int(r2 * 255), int(g2 * 255), int(b2 * 255))
        else:
            inv = 255 - round((r + g + b) / 3)
            px[x, y] = tuple(round(INK[i] + (255 - INK[i]) * inv / 255) for i in range(3))
im.save(out + "/01-agentes-unknown.jpg", quality=92)

# Lámina 05: a company at work.jpg (1044x588). Solo reescala a 1080 de ancho. El fondo negro se funde con Ink por mezcla screen en el diseño.
im = Image.open(ref + "a company at work.jpg").convert("RGB")
im = im.resize((1080, round(588 * 1080 / 1044)), Image.LANCZOS)
im.save(out + "/05-mesa-larga.jpg", quality=92)
print("ok")
