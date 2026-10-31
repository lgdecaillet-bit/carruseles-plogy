"""Derivados de fotos para las piezas 027 en adelante. El original nunca se toca.

Modos:
  duo    duotono de marca: sombras Ink, medios naranja, luces crema (para fotos con colores fuera de paleta)
  calido corrección suave hacia la paleta (conserva el color original)
  nada   solo recorte y tamaño
"""
import pathlib
from PIL import Image, ImageEnhance, ImageOps

KIT = pathlib.Path(__file__).resolve().parents[2]
REF = KIT / "assets" / "reference-originals"
PIEZAS = KIT / "piezas"

STOPS = [(0.0, (23, 19, 16)), (0.42, (180, 61, 0)), (0.68, (255, 91, 0)), (1.0, (255, 226, 205))]


def _lut():
    lut = {0: [], 1: [], 2: []}
    for v in range(256):
        t = v / 255
        for (a, ca), (b, cb) in zip(STOPS, STOPS[1:]):
            if a <= t <= b:
                k = (t - a) / (b - a)
                c = [round(ca[i] + (cb[i] - ca[i]) * k) for i in range(3)]
                break
        for i in range(3):
            lut[i].append(c[i])
    return lut[0] + lut[1] + lut[2]


def deriva(src, dst, modo="calido", ancho=1080, alto=1350, foco=(0.5, 0.5)):
    src = pathlib.Path(src)
    if not src.is_absolute():
        src = REF / src
    im = Image.open(src).convert("RGB")
    im = ImageOps.fit(im, (ancho, alto), Image.LANCZOS, centering=foco)
    if modo == "duo":
        g = ImageOps.autocontrast(im.convert("L"), cutoff=1)
        im = g.convert("RGB").point(_lut())
    elif modo == "calido":
        im = ImageEnhance.Color(im).enhance(0.85)
        r, g, b = im.split()
        r = r.point(lambda v: min(255, int(v * 1.05)))
        b = b.point(lambda v: int(v * 0.9))
        im = Image.merge("RGB", (r, g, b))
    dst = pathlib.Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, quality=88)
    return dst
