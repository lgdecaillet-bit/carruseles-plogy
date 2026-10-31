# Derivados de la pieza 015: hojas de contacto con los PNG reales de piezas/cta-biblioteca/exports/.
# Uso: python -I derive.py "<ruta del kit>" "<carpeta assets de la pieza 015>"
#
# No se re-derivan fotos: la foto del CTA (11-reunion.jpg) se COPIA de la biblioteca.
# Las hojas se arman con Pillow a partir de los exports cta-NN.png ya renderizados (los "despues" de las
# correcciones). Los "antes" no existen como imagen y no se dibujan.
# Cada miniatura lleva su numero de variante (el que la persona escribira al comentar).
#
# Salidas (en assets/):
#   11-reunion.jpg          copia de la foto del CTA (variante 11 de la biblioteca)
#   hoja-30.png             las 30 variantes, 6 columnas x 5 filas, con numero y color por tipo
#   hoja-mapa.png           las 11 variantes cuyas fotos pasan por mapa de color (derive.py de la biblioteca)
#   hoja-rojos.png          las 6 variantes cuyos rojos se llevan al naranja
#   hoja-titulares.png      las 6 variantes cuyo titular naranja paso a blanco (fix_ctas.py)
#   hoja-logos.png          recortes de la zona del logo de las 5 variantes tocadas por el logo (fix_ctas.py)
#   hoja-portada.png        mosaico sin numeros para la portada
import shutil
import sys

from PIL import Image, ImageDraw, ImageFont

kit, out = sys.argv[1], sys.argv[2]
lib = kit + "/piezas/cta-biblioteca/"
exp = lib + "exports/"

INK = (23, 19, 16)
ORANGE = (255, 91, 0)
VIOLET = (156, 90, 167)
CORAL = (247, 89, 70)
WHITE = (255, 255, 255)

# Tipos segun piezas/cta-biblioteca/CATALOGO.md
TIPO = {}
for n in range(1, 11):
    TIPO[n] = ("seguimiento", WHITE, INK)
for n in range(11, 17):
    TIPO[n] = ("comunidad", ORANGE, INK)
for n in range(17, 25):
    TIPO[n] = ("recurso", VIOLET, WHITE)
for n in range(25, 31):
    TIPO[n] = ("comercial", INK, WHITE)

FONT = "C:/Windows/Fonts/arialbd.ttf"


def load(n):
    return Image.open(exp + "cta-%02d.png" % n).convert("RGB")


def thumb(n, w, h, crop=None):
    im = load(n)
    if crop:
        im = im.crop(crop)
    return im.resize((w, h), Image.LANCZOS)


def tag(canvas, n, right, y, size):
    """Numero de variante en la esquina superior derecha (en las variantes esa esquina esta libre)."""
    d = ImageDraw.Draw(canvas)
    f = ImageFont.truetype(FONT, size)
    label = "%02d" % n
    tw = d.textlength(label, font=f)
    padx, pady = round(size * 0.32), round(size * 0.18)
    w, h = round(tw + 2 * padx), round(size + 2 * pady)
    _, bg, fg = TIPO[n]
    x = right - w
    d.rounded_rectangle((x, y, x + w, y + h), radius=round(h * 0.28), fill=bg,
                        outline=WHITE if bg == INK else None, width=max(2, size // 14))
    d.text((x + padx, y + pady - round(size * 0.1)), label, font=f, fill=fg)


def sheet(nums, cols, tw, th, gap, numbered=True, crop=None, tagsize=None):
    rows = (len(nums) + cols - 1) // cols
    W = cols * tw + (cols - 1) * gap
    H = rows * th + (rows - 1) * gap
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for i, n in enumerate(nums):
        r, c = divmod(i, cols)
        x, y = c * (tw + gap), r * (th + gap)
        canvas.paste(thumb(n, tw, th, crop), (x, y))
        if numbered:
            tag(canvas, n, x + tw - 10, y + 10, tagsize or round(tw * 0.125))
    return canvas


def save(im, name):
    im.save(out + "/" + name)
    print("ok", name, im.size)


# Foto del CTA: copia, no se re-deriva
shutil.copy(lib + "assets/11-reunion.jpg", out + "/11-reunion.jpg")
print("ok 11-reunion.jpg (copia)")

# Las 30
save(sheet(list(range(1, 31)), 6, 248, 310, 16, tagsize=44), "hoja-30.png")

# Fotos tratadas (derive.py de la biblioteca: gradient_map y shift_reds)
MAPA = [3, 4, 9, 10, 12, 13, 15, 16, 21, 23, 26]
ROJOS = [14, 18, 20, 22, 24, 28]
save(sheet(MAPA, 6, 248, 310, 16), "hoja-mapa.png")
save(sheet(ROJOS, 6, 248, 310, 16), "hoja-rojos.png")

# Titulares naranjas que pasaron a blanco (fix_ctas.py)
TITULARES = [6, 10, 18, 20, 21, 29]
save(sheet(TITULARES, 3, 560, 700, 28, tagsize=60), "hoja-titulares.png")

# Zona del logo y el inicio del titular: x 0-640, y 40-300 (logo en 58..288 x 80..150)
LOGOS = [13, 26, 28, 11]
logos = sheet(LOGOS, 2, 640, 260, 24, crop=(0, 40, 640, 300), tagsize=56)
# la 23 va a ancho completo (1080 x 156 de origen, 1304 x 188 en la hoja)
w23 = 1304
full = Image.new("RGBA", (w23, logos.size[1] + 24 + 188), (0, 0, 0, 0))
full.paste(logos, (0, 0))
full.paste(thumb(23, w23, 188, crop=(0, 40, 1080, 196)), (0, logos.size[1] + 24))
tag(full, 23, w23 - 10, logos.size[1] + 24 + 10, 56)
save(full, "hoja-logos.png")

# Mosaico de portada: 12 variantes, sin numeros, 6 x 2 de 180 x 225 (1080 x 450)
PORTADA = [6, 8, 12, 15, 16, 19, 21, 23, 2, 13, 25, 18]
save(sheet(PORTADA, 6, 180, 225, 0, numbered=False), "hoja-portada.png")
