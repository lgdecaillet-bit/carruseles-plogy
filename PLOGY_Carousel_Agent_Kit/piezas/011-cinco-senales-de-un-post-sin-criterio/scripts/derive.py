# Derivado de foto de la pieza 011. El original no se toca.
# Uso: python -I derive.py "<ruta del kit>" "<carpeta assets de la pieza>"
#
# La lámina 07 usa la variante 22 de la biblioteca de CTAs. Su derivado ya existe en
# piezas/cta-biblioteca/assets/22-bloque.jpg y se COPIA, no se rehace. Para reproducirlo desde el original,
# este es el tratamiento que usó la biblioteca (shift_reds + cover, ver piezas/cta-biblioteca/scripts/derive.py):
#   original: assets/reference-originals/352669cb8bd32f30b5d5e609deae4803.jpg (1200x1699)
#   transformación: rojos saturados llevados al naranja de marca (matiz ~0.058), recorte a 1080x1350 con foco (0.5, 0.25).
# No se usa ninguna foto extra: "vibe code.jpg" (lleva marca de agua de TikTok) y la otra sugerida no explican la idea.
import shutil
import sys

kit, out = sys.argv[1], sys.argv[2]
shutil.copy(kit + "/piezas/cta-biblioteca/assets/22-bloque.jpg", out + "/22-bloque.jpg")
print("ok 22-bloque.jpg")
