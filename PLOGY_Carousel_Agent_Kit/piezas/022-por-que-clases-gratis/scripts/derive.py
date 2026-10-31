# Recortes de las fotos reales de Plogy (assets/originales -> assets/).
# Los originales no se tocan. 02 y 04 se recortan para sacar del cuadro las pantallas de laptop
# (chat de claude.ai, WhatsApp, LinkedIn, marcadores personales).
# Uso: python -I scripts/derive.py  (desde la carpeta de la pieza)
from PIL import Image, ImageOps, ImageEnhance
import os
SRC = "assets/originales"; OUT = "assets"

def load(name):
    return ImageOps.exif_transpose(Image.open(os.path.join(SRC, name))).convert("RGB")

def crop_frac(im, x0, y0, x1, y1):
    w, h = im.size
    return im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))

def save(im, name, maxside=2000, warm=1.0):
    im = im.copy(); im.thumbnail((maxside, maxside), Image.LANCZOS)
    if warm != 1.0:
        im = ImageEnhance.Color(im).enhance(warm)
    im.save(os.path.join(OUT, name), quality=90)
    print(name, im.size)

save(load("01-publico-amplio-plogy-night.jpg"), "01-clase-noche.jpg")
# 02: se recorta el banner de otra organización a la izquierda
save(crop_frac(load("03-ensenando-frente-a-pantalla.jpg"), 0.24, 0, 1, 1), "02-ensenando.jpg")
save(crop_frac(load("04-estudiantes-en-computadores.jpg"), 0, 0.05, 1, 0.42), "04-estudiantes.jpg")
save(crop_frac(load("02-clase-instructor-y-estudiantes.jpg"), 0, 0, 1, 0.62), "05-clase-dia.jpg")
save(load("06-detalle-bienvenidos-plogy-nights.jpg"), "06-bienvenidos.jpg")
save(load("05-grupo-comunidad-plogy-night.jpg"), "07-grupo.jpg")
