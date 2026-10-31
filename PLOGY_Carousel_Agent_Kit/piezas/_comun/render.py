"""Exporta las láminas de una pieza a PNG (1080x1350) con Edge vía Playwright y revisa desbordes.

Uso: python _comun/render.py <carpeta de la pieza> [n,n,...]
Salida: <pieza>/exports/slide-NN.png. Avisa si algún texto se sale de la lámina o del cuerpo,
o si el cuerpo choca con los puntos o la línea de fuente. Igual hay que mirar cada PNG.
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

CHECK = r"""
(n) => {
  const s = document.querySelector('.slide[data-n="'+n+'"]');
  const R = s.getBoundingClientRect(); const out = [];
  const body = s.querySelector('.body');
  const lim = body ? body.getBoundingClientRect() : null;
  s.querySelectorAll('h1,h2,h3,p,b,span,li,small,strong,em,td,div.msg,div.sticky,div.pill,div.row').forEach(e => {
    const r = e.getBoundingClientRect(); if (!r.width || !r.height) return;
    if (e.closest('.dots,.count,.logo') || getComputedStyle(e).display === 'inline') return;
    if (r.right > R.right + 1 || r.left < R.left - 1 || r.bottom > R.bottom + 1)
      out.push('fuera de la lámina: ' + (e.textContent||'').trim().slice(0,40));
    else if (lim && body.contains(e) && r.bottom > lim.bottom + 2 && getComputedStyle(e).position !== 'absolute')
      out.push('baja del cuerpo ' + Math.round(r.bottom - lim.bottom) + 'px: ' + (e.textContent||'').trim().slice(0,40));
    if (e.scrollWidth > e.clientWidth + 2 && ['nowrap','pre'].includes(getComputedStyle(e).whiteSpace))
      out.push('texto cortado: ' + (e.textContent||'').trim().slice(0,40));
  });
  return [...new Set(out)];
}
"""


def main():
    piece = pathlib.Path(sys.argv[1]).resolve()
    only = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else None
    html = piece / "carrusel.html"
    out = piece / "exports"
    out.mkdir(exist_ok=True)
    url = html.as_uri()
    with sync_playwright() as p:
        b = p.chromium.launch(channel="msedge")
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        pg.goto(url + "?s=1")
        pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        n = pg.evaluate("document.querySelectorAll('.slide').length")
        for i in range(1, n + 1):
            if only and i not in only:
                continue
            pg.evaluate("""(i) => { document.querySelectorAll('.slide').forEach(s => s.classList.toggle('on', s.dataset.n == String(i))); }""", i)
            pg.wait_for_timeout(120)
            pg.screenshot(path=str(out / f"slide-{i:02d}.png"), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
            issues = pg.evaluate(CHECK, i)
            print(f"{piece.name} {i:02d}", "ok" if not issues else "AVISO " + " | ".join(issues))
        b.close()


if __name__ == "__main__":
    main()
