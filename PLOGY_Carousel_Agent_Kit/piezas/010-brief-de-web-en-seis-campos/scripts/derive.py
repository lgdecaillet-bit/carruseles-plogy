# Derivado de foto de la pieza 010. El original no se toca.
# Uso: python -I derive.py "<ruta del kit>" "<carpeta assets de la pieza>"
#
# La foto del CTA (lámina 8 y guía) es el derivado 23 de la biblioteca de CTAs. No se re-deriva: se copia tal cual.
# Cómo lo creó la biblioteca (piezas/cta-biblioteca/scripts/derive.py, línea 139):
#   cover(gradient_map(open_rgb("step up.jpg"), WARM, 0.8), 1080, 720)
#   Original: assets/reference-originals/step up.jpg (564x564, manos de trama verde sobre negro). Autor desconocido.
#   Tratamiento: mapa de luminosidad a Ink, naranja y crema (el verde pasa al naranja de marca); recorte a banda 1080x720.
# Esta pieza no usa ninguna otra foto.
import shutil
import sys

kit, out = sys.argv[1], sys.argv[2]
shutil.copyfile(kit + "/piezas/cta-biblioteca/assets/23-manos.jpg", out + "/23-cta-manos.jpg")
print("ok 23-cta-manos.jpg (copia del derivado 23 de la biblioteca)")
