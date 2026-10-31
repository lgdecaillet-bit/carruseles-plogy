# Derivados de foto de la pieza 003. Los originales no se tocan.
# Uso: python -I derive.py "<ruta del kit>" "<carpeta assets de la pieza>"
import sys
from PIL import Image

kit, out = sys.argv[1], sys.argv[2]
ref = kit + "/assets/reference-originals/"

# Lámina 05: ai watching 2.jpg (736x1104). Tiene un marco negro de ~55 px. Se recorta la franja de la cabeza y el teléfono,
# con las cajas de seguimiento naranja, y se escala a 1080 de ancho. Los puntos ya son naranja, no se recolorea.
im = Image.open(ref + "ai watching 2.jpg").convert("RGB").crop((60, 170, 676, 470))
im = im.resize((1080, round(300 * 1080 / 616)), Image.LANCZOS)
im.save(out + "/05-medir.jpg", quality=92)
print("ok")
