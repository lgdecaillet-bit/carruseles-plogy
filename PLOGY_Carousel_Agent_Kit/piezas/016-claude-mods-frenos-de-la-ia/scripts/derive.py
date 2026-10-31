# Derivados de foto de la pieza 016. Los originales no se tocan.
# Uso: python -I derive.py "<ruta del kit>" "<carpeta assets de la pieza>"
#   01-retro.jpg      5fc091d4c9d6625b9177ae9e6f5988c5.jpg: hombre con una taza frente a muchas pantallas, estética de los 80.
#                     Mapa de color a Ink, naranja y crema (las pantallas azules pasan a naranja de marca).
#   02-error.jpg      0df7100a10bafeeac554662325013596.jpg: oficina amarilla con ventanas de error. Mapa a Ink, naranja y crema.
#   03-manos.jpg      perfection.jpg: dos manos casi se tocan (punteado blanco sobre negro). Mapa a Ink, naranja y crema.
#   05-vigilancia.jpg ai watching 2.jpg: persona detectada por una IA (cajas y puntos naranja de origen). Sin mapa de color; se aclara x1,6 porque el original es muy oscuro.
import colorsys
import sys

import numpy as np
from PIL import Image

kit, out = sys.argv[1], sys.argv[2]
ref = kit + "/assets/reference-originals/"

INK = (23, 19, 16)
ORANGE = (255, 91, 0)
CREAM = (255, 238, 225)
VIOLET = (156, 90, 167)
CORAL = (247, 89, 70)
WARM = [(0.0, INK), (0.5, ORANGE), (1.0, CREAM)]
WARM_DARK = [(0.0, INK), (0.35, (150, 52, 8)), (0.65, ORANGE), (1.0, CREAM)]
BRAND = [(0.0, INK), (0.35, VIOLET), (0.7, CORAL), (1.0, (255, 205, 160))]
BW_WARM = [(0.0, INK), (1.0, (255, 244, 235))]


def open_rgb(name):
    return Image.open(ref + name).convert("RGB")


def cover(im, w, h, fx=0.5, fy=0.5):
    iw, ih = im.size
    target = w / h
    if iw / ih > target:
        cw, ch = round(ih * target), ih
    else:
        cw, ch = iw, round(iw / target)
    x = round((iw - cw) * fx)
    y = round((ih - ch) * fy)
    return im.crop((x, y, x + cw, y + ch)).resize((w, h), Image.LANCZOS)


def gradient_map(im, stops, gamma=1.0):
    g = np.asarray(im.convert("L"), dtype=np.float32) / 255.0
    g = np.clip(g, 0, 1) ** gamma
    xs = [s[0] for s in stops]
    res = np.zeros(g.shape + (3,), dtype=np.float32)
    for c in range(3):
        res[..., c] = np.interp(g, xs, [s[1][c] for s in stops])
    return Image.fromarray(res.astype(np.uint8), "RGB")


def shift_reds(im, smin=0.35, vmin=0.2):
    a = np.asarray(im, dtype=np.float32) / 255.0
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx = a.max(-1)
    mn = a.min(-1)
    d = mx - mn + 1e-9
    h = np.zeros_like(mx)
    h = np.where(mx == r, ((g - b) / d) % 6, h)
    h = np.where(mx == g, (b - r) / d + 2, h)
    h = np.where(mx == b, (r - g) / d + 4, h)
    h = h / 6.0
    s = np.where(mx > 0, d / (mx + 1e-9), 0)
    mask = ((h < 0.06) | (h > 0.93)) & (s > smin) & (mx > vmin)
    h2 = np.where(mask, 0.058, h)
    # hsv -> rgb vectorizado
    i = np.floor(h2 * 6).astype(int) % 6
    f = h2 * 6 - np.floor(h2 * 6)
    p = mx * (1 - s)
    q = mx * (1 - f * s)
    t = mx * (1 - (1 - f) * s)
    v = mx
    rr = np.choose(i, [v, q, p, p, t, v])
    gg = np.choose(i, [t, v, v, q, p, p])
    bb = np.choose(i, [p, p, t, v, v, q])
    res = np.stack([rr, gg, bb], -1)
    return Image.fromarray((np.clip(res, 0, 1) * 255).astype(np.uint8), "RGB")


def save(im, name, q=92):
    im.save(out + "/" + name, quality=q)
    print("ok", name, im.size)



W, H = 1080, 1350

save(cover(gradient_map(open_rgb("5fc091d4c9d6625b9177ae9e6f5988c5.jpg"), WARM_DARK, 1.25), W, H, 0.5, 0.6), "01-retro.jpg")
save(cover(gradient_map(open_rgb("0df7100a10bafeeac554662325013596.jpg"), WARM_DARK, 0.9), W, 620, 0.5, 0.45), "02-error.jpg")
save(cover(gradient_map(open_rgb("perfection.jpg"), WARM, 0.8), W, 560, 0.5, 0.5), "03-manos.jpg")
im = open_rgb("ai watching 2.jpg")
iw, ih = im.size
# se recortan las bandas negras laterales del original
im = im.crop((round(iw * 0.1), 0, round(iw * 0.9), ih))
im = cover(im, W, 560, 0.5, 0.35)
# la foto es muy oscura: se aclara para que se vea la persona detectada (los puntos naranja se conservan)
arr = np.clip(np.asarray(im, dtype=np.float32) * 1.6, 0, 255).astype(np.uint8)
save(Image.fromarray(arr, "RGB"), "05-vigilancia.jpg")
