# Derivado de foto de la pieza 008. El original no se toca.
# Uso: python -I derive.py "<ruta del kit>" "<carpeta assets de la pieza>"
#
# Lámina 01: 742e66127844125977fb2c25c2b4265e.jpg (1200x1200). Una mano sostiene una carpeta que brilla, rodeada de archivos.
# Transformación:
#   1. Recorte (100,215)-(1100,895): mano, carpeta y archivos. Se quita el aviso "Parental Advisory" y el borde.
#   2. Los nombres de archivo (nombres de canciones y de artistas) se rellenan con el color del fondo: no son de Plogy ni aportan.
#      Queda el rótulo "demos 2!!!" bajo la carpeta.
#   3. El azul de la carpeta se lleva al violeta de marca (matiz ~0.79, más oscuro y menos saturado). La mano y el brillo ya son naranjas.
#   4. Se escala a 1080 de ancho.
import colorsys
import sys

import numpy as np
from PIL import Image, ImageFilter

kit, out = sys.argv[1], sys.argv[2]
ref = kit + "/assets/reference-originals/"

im = Image.open(ref + "742e66127844125977fb2c25c2b4265e.jpg").convert("RGB").crop((100, 215, 1100, 895))

# cajas de los nombres de archivo, en coordenadas del recorte (izq, arriba, der, abajo)
labels = [
    (396, 60, 464, 85), (284, 116, 338, 138), (532, 105, 592, 128), (672, 86, 712, 101),
    (408, 149, 472, 171), (742, 174, 820, 199), (204, 224, 290, 250), (326, 220, 394, 243),
    (516, 200, 596, 224), (618, 200, 672, 222), (680, 292, 764, 316), (296, 319, 356, 343),
]
rng = np.random.default_rng(8)
arr = np.asarray(im, dtype=np.float32)
for (l, t, r, b) in labels:
    # relleno por difusión: cada píxel de la caja toma el promedio de sus vecinos hasta que se alisa con el borde
    pad = 8
    reg = arr[t - pad:b + pad, l - pad:r + pad].copy()
    m = np.zeros(reg.shape[:2], bool)
    m[pad:-pad, pad:-pad] = True
    reg[m] = reg[~m].mean(0)
    for _ in range(600):
        nb = (np.roll(reg, 1, 0) + np.roll(reg, -1, 0) + np.roll(reg, 1, 1) + np.roll(reg, -1, 1)) / 4
        reg[m] = nb[m]
    reg[m] += rng.normal(0, 2.5, (m.sum(), 1))
    arr[t - pad:b + pad, l - pad:r + pad][m] = reg[m]
im = Image.fromarray(arr.astype(np.uint8), "RGB")

# azul a violeta de marca
a = np.asarray(im, dtype=np.float32) / 255.0
r, g, b = a[..., 0], a[..., 1], a[..., 2]
mx, mn = a.max(-1), a.min(-1)
d = mx - mn + 1e-9
h = np.zeros_like(mx)
h = np.where(mx == r, ((g - b) / d) % 6, h)
h = np.where(mx == g, (b - r) / d + 2, h)
h = np.where(mx == b, (r - g) / d + 4, h)
h = h / 6.0
s = np.where(mx > 0, d / (mx + 1e-9), 0)
mask = (h > 0.5) & (h < 0.7) & (s > 0.3)
h2 = np.where(mask, 0.79, h)
s2 = np.where(mask, s * 0.72, s)
i = np.floor(h2 * 6).astype(int) % 6
f = h2 * 6 - np.floor(h2 * 6)
p = mx * (1 - s2)
q = mx * (1 - f * s2)
t = mx * (1 - (1 - f) * s2)
v = np.where(mask, mx * 0.7, mx)
rr = np.choose(i, [v, q, p, p, t, v])
gg = np.choose(i, [t, v, v, q, p, p])
bb = np.choose(i, [p, p, t, v, v, q])
res = np.stack([rr, gg, bb], -1)
im = Image.fromarray((np.clip(res, 0, 1) * 255).astype(np.uint8), "RGB")
im = im.resize((1080, round(im.size[1] * 1080 / im.size[0])), Image.LANCZOS)
im.save(out + "/01-mano-carpeta.jpg", quality=92)
print("ok", im.size)
