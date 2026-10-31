# Derivado de foto de la pieza 012. El original no se toca.
# Uso: python -I derive.py "<ruta del kit>" "<carpeta assets de la pieza>"
#
# Lámina 08 (CTA, variante 19 de la biblioteca) y foto de la guía: la cámara sobre un trípode en un cuarto naranja.
# Original: assets/reference-originals/cb07f8f7b5f67ac4c3996d02b64d03cd.jpg (autor desconocido).
# El derivado ya existe en la biblioteca de CTAs (piezas/cta-biblioteca/assets/19-camara.jpg, creado por
# piezas/cta-biblioteca/scripts/derive.py: recorte a 1080x1350 alrededor del punto de enfoque, sin cambio de color).
# Esta pieza lo copia tal cual, no lo vuelve a derivar, y deja aquí la trazabilidad.
import shutil
import sys

kit, out = sys.argv[1], sys.argv[2]
src = kit + "/piezas/cta-biblioteca/assets/19-camara.jpg"
shutil.copyfile(src, out + "/08-cta-camara.jpg")
print("ok", out + "/08-cta-camara.jpg")
