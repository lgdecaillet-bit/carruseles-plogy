import sys, colorsys
from PIL import Image

kit, out = sys.argv[1], sys.argv[2]
ref = kit + "/assets/reference-originals/"

# 03: mesa de decisión. El rojo del original se desplaza hacia el Orange de Plogy (#FF5B00, matiz ~21 grados).
im = Image.open(ref + "decission making team.jpg").convert("RGB")
px = im.load()
w, h = im.size
for y in range(h):
    for x in range(w):
        r, g, b = px[x, y]
        hh, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        if s > 0.45 and (hh < 0.05 or hh > 0.95):
            hh = 0.058  # ~21 grados
            r2, g2, b2 = colorsys.hsv_to_rgb(hh, min(1.0, s * 1.05), min(1.0, v * 1.08))
            px[x, y] = (int(r2 * 255), int(g2 * 255), int(b2 * 255))
im.save(out + "/03-mesa-decision.jpg", quality=92)

# 04: explosión. Tono ya cálido, se conserva; solo se reescala a 1080 de ancho.
im = Image.open(ref + "explosion.jpg").convert("RGB")
w, h = im.size
im = im.resize((1080, round(h * 1080 / w)), Image.LANCZOS)
im.save(out + "/04-explosion.jpg", quality=92)

# 06: manos y ventana. Recorte centrado en las manos (franja y 380-780, 6 px menos por lado para quitar el borde).
im = Image.open(ref + "perfection.jpg").convert("RGB")
im = im.crop((6, 380, 1074, 780))
im.save(out + "/06-manos-project-exe.jpg", quality=92)
print("ok")
