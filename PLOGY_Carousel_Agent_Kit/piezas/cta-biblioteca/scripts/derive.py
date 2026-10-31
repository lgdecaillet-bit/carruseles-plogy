# Derivados de foto de la biblioteca de CTAs. Los originales no se tocan.
# Uso: python -I derive.py "<ruta del kit>" "<carpeta assets de la biblioteca>"
#
# Tres tratamientos de color hacia la paleta de Plogy:
#   shift_reds(im)      lleva los rojos saturados al Orange de la marca (matiz ~0.058) y deja el resto igual.
#   gradient_map(im, s) reemplaza la luminosidad por un degradado de marca (Ink -> naranja -> crema, o Ink -> violeta -> coral).
#                       Sirve para fotos con colores ajenos a la paleta (azul, verde, amarillo).
#   cover(im, w, h)     recorta a la proporción pedida alrededor de un punto de enfoque y reescala con LANCZOS.
import colorsys
import shutil
import sys

import numpy as np
from PIL import Image

kit, out = sys.argv[1], sys.argv[2]
ref = kit + "/assets/reference-originals/"
piezas = kit + "/piezas/"

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

# 01 gente que camina en diagonal, una figura sola (naranja de origen)
save(cover(open_rgb("c7b553bc932847e004898084613e607e.jpg"), W, H), "01-multitud.jpg")
# 02 escalera naranja con una silueta (643x694: se escala ~2x, va con degradado de protección)
save(cover(open_rgb("d8fea9019dca5fb238936b8b23bb44f9.jpg"), W, H, 0.5, 0.5), "02-escalera.jpg")
# 03 radiografía de una persona encorvada sobre el teléfono: azul -> naranja y crema
save(cover(gradient_map(open_rgb("scrolling through social media.jpg"), WARM, 0.85), W, H, 0.5, 0.5), "03-radiografia.jpg")
# 04 caza sobre arco de degradado: azul -> violeta y coral de marca
save(cover(gradient_map(open_rgb("df8f3f218e4777eee85ea52c1d7f2791.jpg"), BRAND, 0.9), W, H, 0.5, 0.36), "04-despegue.jpg")
# 05 hombre en silla frente a un hongo nuclear en la playa (banda superior 1080x820)
save(cover(open_rgb("ba84b037c1ad6f33424fbf749acdbf72.jpg"), W, 820, 0.5, 0.35), "05-playa.jpg")
# 06 columnas de luz naranja
save(cover(open_rgb("628cfc8869e6813971bfbff4c7988dee.jpg"), W, H), "06-columnas.jpg")
# 07 esferas de degradado sobre crema (se escala a 600 de ancho, queda alta)
im = open_rgb("4f83307ae696136ecb65e68bf387ebfc.jpg")
save(im.resize((600, round(im.size[1] * 600 / im.size[0])), Image.LANCZOS), "07-esferas.jpg")
# 08 ilustración morada de una persona frente al computador
save(cover(open_rgb("6a2084e8a39b2acbbb5ceeb914c1e4cf.jpg"), W, H), "08-morado.jpg")
# 09 ojos enormes en un mural de metro: blanco y negro llevado a Ink y crema
save(cover(gradient_map(open_rgb("7fb56e85450ce028a02b0f8d514f9dfe.jpg"), BW_WARM), W, H, 0.5, 0.45), "09-ojos.jpg")
# 10 platillo con haz verde: verde -> naranja
save(cover(gradient_map(open_rgb("another workd.jpg"), [(0.0, INK), (0.55, ORANGE), (1.0, (255, 225, 180))], 0.8), W, H, 0.5, 0.18), "10-platillo.jpg")
# 11 reunión vista desde arriba, 12 personas (banda 1080x608)
save(cover(open_rgb("a company at work.jpg"), W, 608), "11-reunion.jpg")
# 12 niño frente a un televisor en la oscuridad: el brillo pasa a naranja
save(cover(gradient_map(open_rgb("f5af49add4b18fc5f6be7bcc5553008a.jpg"), WARM_DARK, 0.6), W, H, 0.5, 0.55), "12-nino-tv.jpg")
# 13 rostro en trama de puntos, blanco y negro cálido (banda 1080x800)
save(cover(gradient_map(open_rgb("a face.jpg"), BW_WARM), W, 800, 0.5, 0.3), "13-rostro.jpg")
# 14 mujer en un andén con texto rojo -> naranja
save(cover(shift_reds(open_rgb("0e4f4af3133481983274576f15d5946f.jpg")), W, H, 0.5, 0.45), "14-anden.jpg")
# 15 oficina amarilla con ventanas de error: pasa a naranja y crema
save(cover(gradient_map(open_rgb("0df7100a10bafeeac554662325013596.jpg"), WARM_DARK, 0.9), W, H), "15-oficina-error.jpg")
# 16 figura en caracteres ASCII: Ink, naranja y crema
save(cover(gradient_map(open_rgb("connected.jpg"), WARM, 0.9), W, H), "16-ascii.jpg")
# 17 hombre pintando en un computador (500x692, se escala a 640 de ancho; va como tarjeta)
im = open_rgb("create with pc is art.jpg")
save(im.resize((640, round(im.size[1] * 640 / im.size[0])), Image.LANCZOS), "17-pintor.jpg")
# 18 cursor de píxeles sobre un libro rojo -> naranja
save(cover(shift_reds(open_rgb("eb39dcdf4a4beba4b05f74c88bf51bdf.jpg")), W, H), "18-cursor-libro.jpg")
# 19 cámara sobre trípode en un cuarto naranja
save(cover(open_rgb("cb07f8f7b5f67ac4c3996d02b64d03cd.jpg"), W, H, 0.5, 0.55), "19-camara.jpg")
# 20 mano sobre un teclado: rojo -> naranja
save(cover(shift_reds(open_rgb("4e568284db737bcd62fe36404767dd07.jpg")), W, H, 0.4, 0.5), "20-teclado.jpg")
# 21 silueta tecleando con destello: azul -> naranja y crema
save(cover(gradient_map(open_rgb("1341dd4c343455db0f11332434703375.jpg"), WARM, 0.8), W, H), "21-silueta-destello.jpg")
# 22 bloque rojo en una ciudad en blanco y negro: rojo -> naranja
save(cover(shift_reds(open_rgb("352669cb8bd32f30b5d5e609deae4803.jpg")), W, H, 0.5, 0.25), "22-bloque.jpg")
# 23 manos de trama verde sobre negro: verde -> naranja (564x564, banda 1080x720)
save(cover(gradient_map(open_rgb("step up.jpg"), WARM, 0.8), W, 720), "23-manos.jpg")
# 24 mano con teléfono en collage (459x422, fondo blanco): rojo -> naranja, 1.25x
im = shift_reds(open_rgb("stay informed.jpg"))
save(im.resize((round(im.size[0] * 1.25), round(im.size[1] * 1.25)), Image.LANCZOS), "24-telefono.jpg")
# 25 ojo de pez con un hombre en una sala (550x550, círculo natural)
save(cover(open_rgb("cb17c1767fa914e7663bd1fcfbb4870c.jpg"), 720, 720), "25-ojo-pez.jpg")
# 26 pantalla azul de error sobre un parque: pasa a naranja y crema (banda 1080x904)
save(cover(gradient_map(open_rgb("1c813d1282065f6a8db2e4c582c4d09c.jpg"), WARM_DARK, 0.9), W, 904), "26-pantalla-error.jpg")
# 27 y 30: derivados ya hechos en piezas anteriores (se copian, no se rehacen)
shutil.copy(piezas + "001-automatizar-el-desorden/assets/cta-b-portal.jpg", out + "/27-portal.jpg")
shutil.copy(piezas + "004-gpt-4o-se-apaga-14-enero/assets/01-pc-viejo.jpg", out + "/30-pc-viejo.jpg")
# 28 público con gafas 3D y una silueta roja -> naranja (banda 1080x644)
save(cover(shift_reds(open_rgb("being different.jpg")), W, 644), "28-silueta-publico.jpg")
# 29 hongo nuclear con una persona frente al teléfono
save(cover(open_rgb("explosion.jpg"), W, H, 0.5, 0.4), "29-explosion.jpg")
