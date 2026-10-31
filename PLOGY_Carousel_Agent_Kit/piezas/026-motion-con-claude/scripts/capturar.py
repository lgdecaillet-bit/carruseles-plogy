"""Exporta las láminas animadas de carrusel.html a MP4 (y un PNG fijo de cada una).

Uso (desde la carpeta de la pieza):
  python -I scripts/capturar.py                 -> todas las láminas, MP4 + PNG
  python -I scripts/capturar.py --stills 2,5,9  -> solo fotos fijas de prueba en t = 1.5, 3 y 4.5 s

Cada escena se dibuja en función del tiempo (window.renderAt(t)), así que la captura
es cuadro por cuadro y exacta: 6 s a 30 cuadros por segundo, en bucle sin salto.
Requiere Playwright para Python (usa Edge instalado) y ffmpeg.
"""
import pathlib, shutil, subprocess, sys, tempfile
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML = (ROOT / "carrusel.html").as_uri()
OUT = ROOT / "exports"
FPS, DUR, TOTAL = 30, 6, 19
POSTER_T = {1: 2.0, 2: 2.6, 15: 1.0, 16: 4.5, 17: 1.6, 19: 3.0}


def page_for(browser, n):
    page = browser.new_page(viewport={"width": 1080, "height": 1350})
    page.goto(f"{HTML}?s={n}&cap=1")
    page.evaluate("() => window.ready")
    page.wait_for_timeout(300)
    return page


def stills(nums):
    OUT.mkdir(exist_ok=True)
    (OUT / "pruebas").mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(channel="msedge")
        for n in nums:
            pg = page_for(b, n)
            for t in (1.5, 3.0, 4.5):
                pg.evaluate(f"() => renderAt({t})")
                pg.screenshot(path=str(OUT / "pruebas" / f"s{n:02d}-{t}.png"))
            pg.close()
        b.close()


def videos(nums):
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(channel="msedge")
        for n in nums:
            pg = page_for(b, n)
            tmp = pathlib.Path(tempfile.mkdtemp(prefix=f"s{n:02d}_"))
            for f in range(FPS * DUR):
                pg.evaluate(f"() => renderAt({f / FPS})")
                pg.screenshot(path=str(tmp / f"f{f:04d}.jpg"), type="jpeg", quality=95)
            pg.evaluate(f"() => renderAt({POSTER_T.get(n, 3.0)})")
            pg.screenshot(path=str(OUT / f"slide-{n:02d}.png"))
            pg.close()
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(tmp / "f%04d.jpg"),
                            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "slow",
                            "-movflags", "+faststart", str(OUT / f"slide-{n:02d}.mp4")], check=True)
            shutil.rmtree(tmp, ignore_errors=True)
            print(f"ok slide-{n:02d}.mp4", flush=True)
        b.close()


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--stills":
        stills([int(x) for x in args[1].split(",")] if len(args) > 1 else range(1, TOTAL + 1))
    else:
        videos([int(x) for x in args[0].split(",")] if args else range(1, TOTAL + 1))
