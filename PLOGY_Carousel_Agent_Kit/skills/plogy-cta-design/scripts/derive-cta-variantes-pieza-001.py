import sys, colorsys
from PIL import Image

kit, out = sys.argv[1], sys.argv[2]
ref = kit + "/assets/reference-originals/"

def shift_reds(im, target=0.058):
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            hh, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            if s > 0.5 and (hh < 0.04 or hh > 0.96):
                r2, g2, b2 = colorsys.hsv_to_rgb(target, s, v)
                px[x, y] = (int(r2 * 255), int(g2 * 255), int(b2 * 255))
    return im

def fit(im, box, size):
    return im.crop(box).resize(size, Image.LANCZOS)

# B: cross the portal (474x710). Recorte 4:5 centrado en el corredor, escalado a 1080x1350.
im = Image.open(ref + "cross the portal.jpg").convert("RGB")
fit(im, (0, 60, 474, 60 + 592), (1080, 1350)).save(out + "/cta-b-portal.jpg", quality=92)

# C: being different (1090x650). Recorte 4:5 alrededor de la silueta roja, con el rojo desplazado al Orange de Plogy.
im = Image.open(ref + "being different.jpg").convert("RGB")
im = shift_reds(im)
fit(im, (320, 0, 840, 650), (1080, 1350)).save(out + "/cta-c-silueta.jpg", quality=92)

# D: tem coding (670x830). Franja superior, 1080 de ancho.
im = Image.open(ref + "tem coding.jpg").convert("RGB")
fit(im, (0, 70, 670, 70 + 507), (1080, 818)).save(out + "/cta-d-clones.jpg", quality=92)

# E: creative working (1113x1560). Recorte 4:5 escalado a 1080x1350.
im = Image.open(ref + "creative working.jpg").convert("RGB")
fit(im, (0, 150, 1113, 150 + 1391), (1080, 1350)).save(out + "/cta-e-oficina.jpg", quality=92)

# F: la explosión ya existe como 04-explosion.jpg (1080 de ancho). No hace falta derivado nuevo.
print("ok")
