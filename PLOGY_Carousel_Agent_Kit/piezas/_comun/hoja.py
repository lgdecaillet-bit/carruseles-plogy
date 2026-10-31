"""Hoja de contacto de una pieza para revisar todas las láminas de un vistazo: python _comun/hoja.py <pieza> [salida.jpg] [ancho]"""
import pathlib, sys
from PIL import Image
p = pathlib.Path(sys.argv[1]); out = sys.argv[2] if len(sys.argv) > 2 else str(p / "exports" / "_hoja.jpg")
w = int(sys.argv[3]) if len(sys.argv) > 3 else 432
fs = sorted((p / "exports").glob("slide-*.png")); h = int(w * 1350 / 1080); cols = 4
sheet = Image.new("RGB", (cols * w + (cols + 1) * 8, ((len(fs) + cols - 1) // cols) * (h + 8) + 8), "#888")
for i, f in enumerate(fs):
    im = Image.open(f).convert("RGB").resize((w, h), Image.LANCZOS)
    sheet.paste(im, (8 + (i % cols) * (w + 8), 8 + (i // cols) * (h + 8)))
sheet.save(out, quality=85); print(out)
