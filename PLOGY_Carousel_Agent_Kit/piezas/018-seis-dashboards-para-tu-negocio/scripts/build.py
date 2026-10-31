# Genera carrusel.html de la pieza 018 (8 láminas, 1080x1350).
# Uso: python -I scripts/build.py   (desde la carpeta de la pieza)
# Cada dashboard es una app de 1400x880 escalada dentro de la lámina. Todos los datos son DE EJEMPLO
# y son coherentes entre sí (las sumas cuadran); ver brief.md.
import datetime, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "carrusel.html")

# ---------- utilidades ----------
def money(v, dec=False):
    if dec:
        return "$" + ("%.2f" % v).replace(".", ",")
    s = "{:,.0f}".format(v).replace(",", ".")
    return "$" + s

def spark(vals, w=120, h=42, color="var(--g)", fill=True, uid=""):
    mn, mx = min(vals), max(vals)
    rng = (mx - mn) or 1
    pts = []
    for i, v in enumerate(vals):
        x = i * w / (len(vals) - 1)
        y = h - 4 - (v - mn) / rng * (h - 8)
        pts.append((x, y))
    p = " ".join("%.1f,%.1f" % q for q in pts)
    area = ""
    if fill:
        area = '<path d="M0 %d L%s L%d %d Z" fill="url(#sp%s)"/>' % (h, " L".join("%.1f %.1f" % q for q in pts), w, h, uid)
    return ('<svg class="spark" viewBox="0 0 %d %d"><defs><linearGradient id="sp%s" x1="0" y1="0" x2="0" y2="1">'
            '<stop offset="0" stop-color="%s" stop-opacity=".35"/><stop offset="1" stop-color="%s" stop-opacity="0"/></linearGradient></defs>'
            '%s<polyline points="%s" fill="none" stroke="%s" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/></svg>'
            % (w, h, uid, color, color, area, p, color))

ICON = {
 "home": '<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/>',
 "ventas": '<path d="M4 20V11M10 20V5M16 20v-6M21 20H3"/>',
 "caja": '<path d="M3 7h15a3 3 0 0 1 3 3v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM3 7l12-3v3"/><path d="M16 14h2"/>',
 "mkt": '<path d="M3 10v4h4l7 4V6L7 10z"/><path d="M18 9a4 4 0 0 1 0 6"/>',
 "ops": '<path d="M2 6h11v10H2zM13 10h5l3 3v3h-8"/><circle cx="6" cy="18.5" r="2"/><circle cx="17" cy="18.5" r="2"/>',
 "ia": '<path d="M12 3l2 6 6 2-6 2-2 6-2-6-6-2 6-2z"/>',
 "plug": '<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0zM12 18v4"/>',
 "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/>',
 "help": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.7.3-1 .8-1 1.7M12 17h.01"/>',
 "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "bell": '<path d="M6 16v-5a6 6 0 0 1 12 0v5l2 2H4zM10 21h4"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
 "dl": '<path d="M12 4v12M7 11l5 5 5-5M4 20h16"/>',
 "alert": '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18h.01"/>',
 "dot3": '<circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "doc": '<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6"/>',
}
def ic(name, cls=""):
    return '<svg class="i %s" viewBox="0 0 24 24">%s</svg>' % (cls, ICON[name])

NAV = [("home", "Resumen", ""), ("ventas", "Ventas", ""), ("caja", "Caja", "1"),
       ("mkt", "Marketing", ""), ("ops", "Operaciones", "7"), ("ia", "Gasto en IA", "")]

def app(active, crumb, title, body):
    nav = "".join('<a class="%s">%s%s%s</a>' % ("on" if i == active else "", ic(k), t,
                  '<span class="n">%s</span>' % n if n else "") for i, (k, t, n) in enumerate(NAV))
    return f'''<div class="app">
  <aside class="sb">
    <div class="ws"><span class="wl"></span><div><b>Mi negocio</b><small>Espacio de trabajo</small></div></div>
    <div class="srch">{ic("search")}<span>Buscar</span><kbd>Ctrl K</kbd></div>
    <p class="sec">Paneles</p>
    <nav class="nav">{nav}</nav>
    <p class="sec">Cuenta</p>
    <nav class="nav"><a>{ic("plug")}Integraciones</a><a>{ic("gear")}Ajustes</a><a>{ic("help")}Ayuda</a></nav>
    <div class="me"><span class="av">TU</span><div><b>Tu cuenta</b><small>Administrador</small></div>{ic("dot3","mute")}</div>
  </aside>
  <main class="mn">
    <header class="tb">
      <div><small>Paneles / {crumb}</small><h3>{title}</h3></div>
      <div class="tools"><span class="px ex">Datos de ejemplo</span><span class="px">{ic("cal")}1 al 21 oct 2026</span>
        <span class="px">{ic("dl")}Exportar</span><span class="icb">{ic("bell")}<i></i></span><span class="av sm">TU</span></div>
    </header>
    {body}
  </main>
</div>'''

def kpi(label, value, delta=None, down=False, note="", sp=None, uid="", bar=None, icon="dot3"):
    d = ""
    if delta:
        d = '<span class="%s">%s %s</span>' % ("dn" if down else "up", "▼" if down else "▲", delta)
    extra = spark(sp, uid=uid, color="#ff8f7d" if down else "var(--g)") if sp else ""
    b = '<div class="pb"><i style="width:%d%%"></i></div>' % bar if bar is not None else ""
    return f'''<div class="kc"><div class="kh"><span>{label}</span>{ic(icon,"mute")}</div><b>{value}</b><div class="kf">{d}<small>{note}</small></div>{b}{extra}</div>'''

def card(title, sub, inner, right="", cls=""):
    s = '<small>%s</small>' % sub if sub else ""
    return f'<div class="cd {cls}"><div class="ch"><div><b>{title}</b>{s}</div>{right}</div>{inner}</div>'

def seg(items, on):
    return '<div class="seg">%s</div>' % "".join('<span class="%s">%s</span>' % ("on" if x == on else "", x) for x in items)

def legend(items):
    return '<div class="lg">%s</div>' % "".join('<span><i style="background:%s"></i>%s</span>' % (c, t) for c, t in items)

def donut(parts, center_big, center_small, size=132, sw=20):
    r = (size - sw) / 2
    c = 2 * 3.14159265 * r
    off = 0
    segs = ""
    for frac, color in parts:
        L = frac * c
        segs += ('<circle cx="%g" cy="%g" r="%g" fill="none" stroke="%s" stroke-width="%d" stroke-dasharray="%.1f %.1f" '
                 'stroke-dashoffset="%.1f" transform="rotate(-90 %g %g)"/>' % (size/2, size/2, r, color, sw, max(L-4,0), c-max(L-4,0), -off, size/2, size/2))
        off += L
    return (f'<svg class="dnt" viewBox="0 0 {size} {size}" style="width:{size}px;height:{size}px">'
            f'<circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="rgba(255,255,255,.06)" stroke-width="{sw}"/>{segs}'
            f'<text x="{size/2}" y="{size/2+2}" text-anchor="middle" class="t1">{center_big}</text>'
            f'<text x="{size/2}" y="{size/2+24}" text-anchor="middle" class="t2">{center_small}</text></svg>')

def hbars(rows, maxv, color="var(--g)"):
    out = ""
    for name, val, label, hot in rows:
        out += ('<div class="hb"><div class="hbl"><span>%s</span><b>%s</b></div><div class="hbt"><i style="width:%.1f%%;background:%s"></i></div></div>'
                % (name, label, val / maxv * 100, color if hot else "#5d524a"))
    return out

# ---------- D1 · Ejecutivo ----------
def d1():
    # facturación acumulada de octubre 2026 (1 oct = jueves); fines de semana venden menos
    days = list(range(1, 22))
    w = [0.35 if datetime.date(2026, 10, d).weekday() >= 5 else 1.0 for d in days]
    import math
    w = [x * (1 + 0.18 * math.sin(i * 1.7)) for i, x in enumerate(w)]
    tot = sum(w); acc = 0; cum = []
    for x in w:
        acc += x / tot * 48.2; cum.append(acc)
    X = lambda d: 52 + (d - 1) / 30 * 636
    Y = lambda v: 216 - v / 70 * 200
    real = " ".join("%.1f,%.1f" % (X(d), Y(v)) for d, v in zip(days, cum))
    area = "M%.1f 216 L" % X(1) + " L".join("%.1f %.1f" % (X(d), Y(v)) for d, v in zip(days, cum)) + " L%.1f 216 Z" % X(21)
    grid = "".join('<line x1="52" x2="690" y1="%.1f" y2="%.1f"/>' % (Y(v), Y(v)) for v in (0, 20, 40, 60))
    yl = "".join('<text x="0" y="%.1f">%s</text>' % (Y(v) + 5, "$%dk" % v if v else "$0") for v in (0, 20, 40, 60))
    xl = "".join('<text x="%.1f" y="244" text-anchor="middle">%d oct</text>' % (X(d), d) for d in (1, 8, 15, 22, 29))
    tx, ty = X(21), Y(48.2)
    chart = f'''<svg class="chart" viewBox="0 0 700 250">
      <defs><linearGradient id="ga1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--g)" stop-opacity=".38"/><stop offset="1" stop-color="var(--g)" stop-opacity="0"/></linearGradient></defs>
      <g class="gl">{grid}</g><g class="ax">{yl}{xl}</g>
      <line x1="{X(1):.1f}" y1="{Y(67/31):.1f}" x2="{X(31):.1f}" y2="{Y(67):.1f}" stroke="#8d8279" stroke-width="2.5" stroke-dasharray="8 7"/>
      <path d="{area}" fill="url(#ga1)"/>
      <polyline points="{real}" fill="none" stroke="var(--g)" stroke-width="3.5" stroke-linejoin="round"/>
      <line x1="{tx:.1f}" x2="{tx:.1f}" y1="14" y2="216" stroke="rgba(255,255,255,.25)" stroke-dasharray="4 5"/>
      <circle cx="{tx:.1f}" cy="{ty:.1f}" r="7" fill="#15110e" stroke="var(--g)" stroke-width="4"/>
      <g transform="translate({tx-205:.1f},{ty-6:.1f})"><rect width="190" height="62" rx="10" fill="#2a231e" stroke="rgba(255,255,255,.1)"/>
        <text x="14" y="24" class="tt1">21 oct · $48.200</text><text x="14" y="46" class="tt2">Meta al día: $45.400</text></g>
    </svg>'''
    k = '<div class="kr">' + \
        kpi("Facturación", "$48.200", "8%", note="vs septiembre", sp=[3, 4, 3.6, 5, 4.8, 6, 6.4, 7.2], uid="k11", icon="ventas") + \
        kpi("Margen bruto", "31%", "2 pts", note="vs septiembre", sp=[27, 28, 29, 28.5, 30, 29.5, 31], uid="k12", icon="home") + \
        kpi("Caja disponible", "$12.400", "5%", down=True, note="vs septiembre", sp=[14, 13.6, 13.9, 13.1, 12.8, 12.4], uid="k13", icon="caja") + \
        kpi("Avance de la meta", "72%", note="de $67.000 del mes", bar=72, icon="ia") + '</div>'
    main = card("Facturación acumulada vs meta", "Octubre 2026", chart,
                legend([("var(--g)", "Real"), ("#8d8279", "Meta")]) + seg(["Semana", "Mes", "Trimestre"], "Mes"))
    lines = [("Productos", 28000, .58, "var(--g)"), ("Servicios", 14500, .30, "var(--g2)"), ("Suscripciones", 5700, .12, "#5d524a")]
    side = card("Ingresos por línea", "Del 1 al 21 oct",
                '<div class="dw">' + donut([(f, c) for _, _, f, c in lines], "$48,2k", "total") + '</div>' +
                '<div class="lst">' + "".join('<div><span><i style="background:%s"></i>%s</span><b>%s</b><em>%d%%</em></div>' % (c, n, money(v), round(f * 100)) for n, v, f, c in lines) + '</div>',
                ic("dot3", "mute"))
    gastos = card("Gastos por categoría", "Total $33.300",
                  hbars([("Sueldos", 18600, "$18.600", True), ("Proveedores", 9400, "$9.400", False), ("Arriendo", 3200, "$3.200", False), ("Marketing", 2100, "$2.100", False)], 18600),
                  seg(["Mes", "Año"], "Mes"))
    pend = card("Pendientes", "Esta semana",
                '<div class="tasks">'
                f'<div><span class="ti">{ic("doc")}</span><p><b>3 facturas por cobrar</b><small>Vencen esta semana</small></p><em>$6.800</em></div>'
                f'<div><span class="ti">{ic("caja")}</span><p><b>Pago a proveedor</b><small>28 oct</small></p><em>$6.400</em></div>'
                f'<div><span class="ti">{ic("cal")}</span><p><b>Cierre de mes</b><small>31 oct</small></p><em class="chip">En 10 días</em></div>'
                '</div>', '<span class="lnk">Ver todo</span>')
    body = k + '<div class="g1">' + main + side + '</div><div class="g2">' + gastos + pend + '</div>'
    return app(0, "Resumen", "Resumen del mes", body)

# ---------- D2 · Ventas ----------
def d2():
    team = [("Ana", "AR", 9440, 8000, "ok", "En meta"), ("Bruno", "BM", 7280, 7000, "ok", "En meta"),
            ("Carla", "CS", 5520, 6000, "mid", "En riesgo"), ("Diego", "DL", 4970, 7000, "warn", "Bajo"),
            ("Elena", "EP", 4290, 9000, "warn", "Bajo")]
    assert sum(t[2] for t in team) == 31500 and sum(t[3] for t in team) == 37000
    rows = ""
    for i, (n, ini, v, m, st, lab) in enumerate(team):
        p = round(v / m * 100)
        rows += (f'<tr><td class="mu">{i+1}</td><td><span class="av xs a{i}">{ini}</span>{n}</td><td class="r">{money(v)}</td>'
                 f'<td class="r mu">{money(m)}</td><td><div class="pb in"><i style="width:{min(p,100)}%;background:{"var(--g)" if p>=100 else "#7a6d63" if p>=80 else "#ff8f7d"}"></i></div></td>'
                 f'<td class="r"><b>{p}%</b></td><td><span class="st {st}">{lab}</span></td></tr>')
    tbl = f'<table class="tbl"><tr><th>#</th><th>Vendedor</th><th class="r">Ventas</th><th class="r">Meta</th><th style="width:150px">Avance</th><th class="r">%</th><th>Estado</th></tr>{rows}</table>'
    k = '<div class="kr">' + \
        kpi("Ventas del mes", "$31.500", "12%", note="vs septiembre", sp=[20, 22, 21, 25, 24, 28, 31.5], uid="k21", icon="ventas") + \
        kpi("Ticket promedio", "$420", "$35", note="vs septiembre", sp=[370, 380, 395, 390, 405, 420], uid="k22", icon="doc") + \
        kpi("Ventas cerradas", "75", "6", note="vs septiembre", sp=[60, 64, 66, 69, 72, 75], uid="k23", icon="home") + \
        kpi("Equipo vs meta", "85%", note="faltan $5.500", bar=85, icon="ia") + '</div>'
    main = card("Avance de cada vendedor", "Meta individual de octubre", tbl, seg(["Mes", "Trimestre"], "Mes"))
    wk = [("S1", 7200), ("S2", 8900), ("S3", 9100), ("S4", 6300)]
    bars = ""
    for i, (s, v) in enumerate(wk):
        h = v / 10000 * 170; x = 20 + i * 78
        cur = i == 3
        bars += (f'<rect x="{x}" y="{200-h:.1f}" width="48" height="{h:.1f}" rx="8" fill="{"url(#hz2)" if cur else "var(--g)"}" {"" if not cur else "stroke=\"var(--g)\" stroke-width=\"2\""}/>'
                 f'<text x="{x+24}" y="{192-h:.1f}" text-anchor="middle" class="vl">{money(v)}</text><text x="{x+24}" y="226" text-anchor="middle" class="axt">{s}</text>')
    side = card("Ventas por semana", "S4 en curso",
                f'''<svg class="chart" viewBox="0 0 330 232"><defs><pattern id="hz2" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="rgba(255,255,255,.04)"/><line x1="0" y1="0" x2="0" y2="8" stroke="var(--g)" stroke-width="3" opacity=".6"/></pattern></defs>
                <line x1="0" x2="330" y1="200" y2="200" stroke="rgba(255,255,255,.08)"/>{bars}</svg>''', ic("dot3", "mute"))
    last = [("#2291", "Cliente 1042", "Ana", 640, "10:42"), ("#2290", "Cliente 0877", "Bruno", 380, "10:15"),
            ("#2289", "Cliente 1310", "Carla", 1120, "09:58"), ("#2288", "Cliente 0456", "Ana", 290, "09:31")]
    t2 = '<table class="tbl"><tr><th>Venta</th><th>Cliente</th><th>Vendedor</th><th class="r">Monto</th><th class="r">Hora</th></tr>' + \
         "".join(f'<tr><td class="mu">{a}</td><td>{b}</td><td>{c}</td><td class="r"><b>{money(d)}</b></td><td class="r mu">{e}</td></tr>' for a, b, c, d, e in last) + '</table>'
    ultimas = card("Últimas ventas", "Hoy", t2, '<span class="lnk">Ver todas</span>')
    alertas = card("Alertas", "Generadas por el panel",
                   '<div class="tasks">'
                   f'<div class="hot"><span class="ti">{ic("alert")}</span><p><b>Diego y Elena bajo el 80%</b><small>de su meta individual</small></p></div>'
                   f'<div><span class="ti">{ic("doc")}</span><p><b>Elena tiene el ticket más bajo</b><small>del equipo este mes</small></p></div>'
                   f'<div><span class="ti">{ic("cal")}</span><p><b>Quedan 7 días hábiles</b><small>para cerrar octubre</small></p></div>'
                   '</div>')
    body = k + '<div class="g1">' + main + side + '</div><div class="g2">' + ultimas + alertas + '</div>'
    return app(1, "Ventas", "Equipo comercial", body)

# ---------- D3 · Caja ----------
def d3():
    ev = {2: 3.1, 3: -2.1, 5: 2.4, 7: -6.4, 8: 4.0, 10: -3.2, 12: 1.8, 14: -1.9, 15: 3.5, 18: -2.4, 19: 2.2,
          22: 1.6, 24: -6.4, 26: 1.9, 27: -2.6, 29: 1.5, 30: -2.6}
    assert round(sum(v for v in ev.values() if v > 0), 1) == 22.0 and round(-sum(v for v in ev.values() if v < 0), 1) == 27.6
    X = lambda d: 52 + d / 30 * 636
    Y = lambda v: 216 - v / 15 * 200
    bal = 8.4; pts = [(X(0), Y(bal))]
    for d in range(1, 31):
        if d in ev:
            bal += ev[d]; pts.append((X(d), Y(bal)))
    assert round(bal, 1) == 2.8
    line = " ".join("%.1f,%.1f" % p for p in pts)
    area = "M%.1f 216 L" % pts[0][0] + " L".join("%.1f %.1f" % p for p in pts) + " L%.1f 216 Z" % pts[-1][0]
    grid = "".join('<line x1="52" x2="690" y1="%.1f" y2="%.1f"/>' % (Y(v), Y(v)) for v in (0, 5, 10, 15))
    yl = "".join('<text x="0" y="%.1f">%s</text>' % (Y(v) + 5, "$%dk" % v if v else "$0") for v in (0, 5, 10, 15))
    base = datetime.date(2026, 10, 21)
    xl = "".join('<text x="%.1f" y="244" text-anchor="middle">%s</text>' % (X(d), "Hoy" if d == 0 else "%d %s" % ((base + datetime.timedelta(d)).day, ["", "", "", "", "", "", "", "", "", "", "oct", "nov"][(base + datetime.timedelta(d)).month])) for d in (0, 7, 14, 21, 28))
    tx, ty = X(24), Y(4.6)
    dots_ = "".join('<circle cx="%.1f" cy="%.1f" r="3.5" fill="var(--g)"/>' % p for p in pts[1:])
    bars = "".join('<rect x="%.1f" y="%.1f" width="10" height="%.1f" rx="3" fill="%s" opacity=".55"/>' % (X(d) - 5, 216 - abs(v) / 15 * 200 * 0.5, abs(v) / 15 * 200 * 0.5, "var(--g2)" if v > 0 else "#5d524a") for d, v in ev.items())
    chart = f'''<svg class="chart" viewBox="0 0 700 250">
      <defs><linearGradient id="ga3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--g)" stop-opacity=".32"/><stop offset="1" stop-color="var(--g)" stop-opacity="0"/></linearGradient></defs>
      <g class="gl">{grid}</g><g class="ax">{yl}{xl}</g>
      <line x1="52" x2="690" y1="{Y(5):.1f}" y2="{Y(5):.1f}" stroke="#ff8f7d" stroke-width="2.5" stroke-dasharray="8 7"/>
      <text x="60" y="{Y(5)+20:.1f}" class="mn1">Mínimo $5.000</text>
      <path d="{area}" fill="url(#ga3)"/>
      <polyline points="{line}" fill="none" stroke="var(--g)" stroke-width="3.5" stroke-linejoin="round"/>
      {dots_}
      <circle cx="{tx:.1f}" cy="{ty:.1f}" r="7" fill="#15110e" stroke="#ff8f7d" stroke-width="4"/>
      <line x1="{tx:.1f}" x2="{tx:.1f}" y1="{ty-88:.1f}" y2="{ty-8:.1f}" stroke="rgba(255,143,125,.45)" stroke-dasharray="4 4"/><g transform="translate({tx-215:.1f},{ty-150:.1f})"><rect width="200" height="62" rx="10" fill="#2a231e" stroke="rgba(255,143,125,.5)"/>
        <text x="14" y="24" class="tt1">14 nov · $4.600</text><text x="14" y="46" class="tt2 hot">Bajo el mínimo</text></g>
    </svg>'''
    k = '<div class="kr">' + \
        kpi("Saldo hoy", "$8.400", note="en 2 cuentas", sp=[11, 10.2, 10.8, 9.6, 9.1, 8.4], uid="k31", icon="caja") + \
        kpi("Cobros próximos 30 días", "$22.000", note="9 facturas", icon="doc") + \
        kpi("Pagos próximos 30 días", "$27.600", note="8 pagos", icon="cal") + \
        kpi("Saldo al día 30", "$2.800", "bajo el mínimo", down=True, note="", icon="alert") + '</div>'
    main = card("Saldo proyectado", "Próximos 30 días, día a día", chart,
                legend([("var(--g)", "Saldo proyectado"), ("#ff8f7d", "Mínimo")]) + seg(["30 días", "60 días", "90 días"], "30 días"))
    side = f'''<div class="cd alertc"><div class="ah">{ic("alert")}<span>Aviso</span></div>
      <b>El 14 de noviembre el saldo baja del mínimo.</b>
      <p>Opciones para evitarlo:</p>
      <ul><li>Adelantar el cobro del 16 nov ($1.900)</li><li>Mover el pago del 14 nov al 17 nov</li><li>Pedir un anticipo a un cliente</li></ul></div>'''
    pagos = [("28 oct", "Proveedor de insumos", 6400), ("31 oct", "Arriendo", 3200), ("14 nov", "Sueldos", 6400), ("17 nov", "Impuestos", 2600)]
    cobros = [("23 oct", "Factura #1042", 3100), ("26 oct", "Factura #1047", 2400), ("29 oct", "Factura #1051", 4000), ("2 nov", "Factura #1055", 1800)]
    tp = '<table class="tbl"><tr><th>Fecha</th><th>Concepto</th><th class="r">Monto</th></tr>' + "".join(f'<tr><td class="mu">{a}</td><td>{b}</td><td class="r"><b class="neg">−{money(c)}</b></td></tr>' for a, b, c in pagos) + '</table>'
    tc = '<table class="tbl"><tr><th>Fecha</th><th>Concepto</th><th class="r">Monto</th></tr>' + "".join(f'<tr><td class="mu">{a}</td><td>{b}</td><td class="r"><b class="pos">+{money(c)}</b></td></tr>' for a, b, c in cobros) + '</table>'
    body = k + '<div class="g1">' + main + side + '</div><div class="g2 eq">' + card("Próximos pagos", "", tp, '<span class="lnk">Ver todos</span>') + card("Próximos cobros", "", tc, '<span class="lnk">Ver todos</span>') + '</div>'
    return app(2, "Caja", "Flujo de caja", body)

# ---------- D4 · Marketing ----------
def d4():
    ch = [("Instagram", "IG", 800, 620, 20, [3, 5, 4, 6, 8, 7]), ("Google", "G", 1200, 540, 15, [5, 4, 4, 3, 3, 2]),
          ("Email", "@", 100, 210, 6, [1, 1, 2, 1, 2, 2]), ("Referidos", "R", 0, 240, 9, [1, 2, 2, 3, 3, 4])]
    assert sum(c[2] for c in ch) == 2100 and sum(c[4] for c in ch) == 50 and sum(c[3] for c in ch) == 1610
    rows = ""
    for i, (n, ab, inv, leads, cl, sp) in enumerate(ch):
        cpc = inv / cl
        conv = cl / leads * 100
        cls = "hot" if cpc >= 60 else "okc" if cpc <= 20 else ""
        rows += (f'<tr><td><span class="chn c{i}">{ab}</span>{n}</td><td class="r">{money(inv)}</td><td class="r">{leads}</td>'
                 f'<td class="r">{cl}</td><td class="r">{("%.1f" % conv).replace(".", ",")}%</td><td class="r"><b class="{cls}">{money(cpc)}</b></td>'
                 f'<td class="sp" style="padding-left:14px">{spark(sp, w=90, h=30, fill=False, color="var(--g)" if i != 1 else "#ff8f7d")}</td></tr>')
    tbl = f'<table class="tbl"><tr><th>Canal</th><th class="r">Inversión</th><th class="r">Leads</th><th class="r">Clientes</th><th class="r">Conversión</th><th class="r">Costo/cliente</th><th style="padding-left:14px">Tendencia</th></tr>{rows}</table>'
    k = '<div class="kr">' + \
        kpi("Inversión del mes", "$2.100", note="4 canales", sp=[1.6, 1.8, 1.7, 2.0, 2.1], uid="k41", icon="mkt") + \
        kpi("Clientes nuevos", "50", "9", note="vs septiembre", sp=[35, 38, 41, 44, 50], uid="k42", icon="home") + \
        kpi("Costo por cliente", "$42", "$6", down=True, note="más caro que sept.", sp=[36, 37, 39, 40, 42], uid="k43", icon="caja") + \
        kpi("Conversión", "3,1%", "0,3 pts", note="leads a clientes", sp=[2.6, 2.7, 2.9, 2.8, 3.1], uid="k44", icon="ventas") + '</div>'
    main = card("Rendimiento por canal", "Octubre 2026", tbl, seg(["Mes", "Trimestre"], "Mes"))
    cols = ["var(--g)", "var(--g2)", "#8d8279", "#5d524a"]
    side = card("Clientes por canal", "50 en total",
                '<div class="dw">' + donut([(c[4] / 50, cols[i]) for i, c in enumerate(ch)], "50", "clientes") + '</div>' +
                '<div class="lst">' + "".join('<div><span><i style="background:%s"></i>%s</span><b>%d</b><em>%d%%</em></div>' % (cols[i], c[0], c[4], c[4] * 2) for i, c in enumerate(ch)) + '</div>',
                ic("dot3", "mute"))
    wk = [9, 14, 15, 12]
    X = lambda i: 40 + i * 190
    Y = lambda v: 150 - v / 20 * 130
    pts = " ".join("%d,%.1f" % (X(i), Y(v)) for i, v in enumerate(wk))
    lc = (f'<svg class="chart" viewBox="0 0 640 180"><g class="gl"><line x1="30" x2="640" y1="{Y(0):.1f}" y2="{Y(0):.1f}"/><line x1="30" x2="640" y1="{Y(10):.1f}" y2="{Y(10):.1f}"/><line x1="30" x2="640" y1="{Y(20):.1f}" y2="{Y(20):.1f}"/></g>'
          f'<g class="ax"><text x="0" y="{Y(0)+5:.1f}">0</text><text x="0" y="{Y(10)+5:.1f}">10</text><text x="0" y="{Y(20)+5:.1f}">20</text>'
          + "".join('<text x="%d" y="176" text-anchor="middle">Semana %d</text>' % (X(i), i + 1) for i in range(4)) + '</g>'
          f'<polyline points="{pts}" fill="none" stroke="var(--g)" stroke-width="3.5"/>'
          + "".join('<circle cx="%d" cy="%.1f" r="6" fill="#15110e" stroke="var(--g)" stroke-width="3"/><text x="%d" y="%.1f" text-anchor="middle" class="vl">%d</text>' % (X(i), Y(v), X(i), Y(v) - 14, v) for i, v in enumerate(wk)) + '</svg>')
    sem = card("Clientes nuevos por semana", "", lc)
    ins = f'''<div class="cd alertc"><div class="ah">{ic("ia")}<span>Para revisar</span></div>
      <b>Google cuesta el doble por cliente que Instagram.</b>
      <p>$80 contra $40. Y referidos trae 9 clientes sin inversión.</p></div>'''
    body = k + '<div class="g1">' + main + side + '</div><div class="g2">' + sem + ins + '</div>'
    return app(3, "Marketing", "Canales de adquisición", body)

# ---------- D5 · Operaciones ----------
def d5():
    cols = [("Recibido", 14, [("#3121", "3 productos", "2 h", ""), ("#3120", "1 producto", "3 h", ""), ("#3119", "5 productos", "5 h", ""), ("#3118", "2 productos", "6 h", "")]),
            ("Preparación", 9, [("#3114", "2 productos", "0,8 d", ""), ("#3112", "4 productos", "1,1 d", ""), ("#3111", "1 producto", "0,6 d", ""), ("#3109", "3 productos", "1,3 d", "")]),
            ("Despacho", 22, [("#3098", "2 productos", "5,1 d", "late"), ("#3101", "3 productos", "4,6 d", "late"), ("#3105", "1 producto", "4,2 d", "late"), ("#3107", "2 productos", "3,8 d", "late")]),
            ("Entregado", 61, [("#3097", "2 productos", "hoy", "done"), ("#3095", "6 productos", "hoy", "done"), ("#3093", "1 producto", "ayer", "done"), ("#3090", "4 productos", "ayer", "done")])]
    assert sum(c[1] for c in cols[:3]) == 45
    kb = ""
    for name, n, cards_ in cols:
        hot = name == "Despacho"
        cs = "".join(f'<div class="oc {st}"><div><b>{oid}</b><span class="tm">{ic("clock")}{t}</span></div><small>{d}</small>'
                     f'{"<em>Atrasado</em>" if st=="late" else ""}</div>' for oid, d, t, st in cards_)
        kb += f'<div class="kcol {"hotc" if hot else ""}"><div class="kch"><b>{name}</b><span>{n}</span>{"<em>" + ic("alert") + "7</em>" if hot else ""}</div>{cs}<div class="more">+{n-4} más</div></div>'
    k = '<div class="kr">' + \
        kpi("Pedidos activos", "45", note="hoy", sp=[38, 41, 40, 43, 44, 45], uid="k51", icon="ops") + \
        kpi("Entregados en octubre", "61", "4", note="vs mismo día de sept.", sp=[40, 45, 50, 54, 58, 61], uid="k52", icon="home") + \
        kpi("Tiempo promedio", "3,2 días", "0,8 días", down=True, note="más lento que sept.", sp=[2.4, 2.5, 2.7, 2.9, 3.0, 3.2], uid="k53", icon="clock") + \
        kpi("Atrasados", "7", "4", down=True, note="todos en despacho", icon="alert") + '</div>'
    main = card("Pedidos por etapa", "Tablero en vivo", '<div class="kb">' + kb + '</div>', seg(["Tablero", "Lista"], "Tablero"), cls="tall")
    st = [("Recibido", 0.4, False), ("Preparación", 0.9, False), ("Despacho", 1.6, True), ("Entrega", 0.3, False)]
    side1 = card("Tiempo promedio por etapa", "Total 3,2 días", hbars([(n, v, ("%.1f d" % v).replace(".", ","), h) for n, v, h in st], 1.6))
    side2 = f'''<div class="cd alertc"><div class="ah">{ic("alert")}<span>Cuello de botella</span></div>
      <b>Despacho junta 22 pedidos.</b><p>7 llevan más de 3 días ahí. Revisa la asignación de transporte.</p></div>'''
    body = k + '<div class="g3">' + main + '<div class="stack">' + side1 + side2 + '</div></div>'
    return app(4, "Operaciones", "Pedidos en curso", body)

# ---------- D6 · Gasto en IA ----------
def d6():
    ar = [("Ventas", 38, 50), ("Soporte", 74, 60), ("Marketing", 46, 50), ("Admin", 28, 40)]
    assert sum(a[1] for a in ar) == 186 and sum(a[2] for a in ar) == 200
    rows = ""
    for n, v, b in ar:
        over = v > b
        rows += (f'<div class="bv"><div class="bvl"><b>{n}</b><span>{money(v)} <small>de {money(b)}</small></span>'
                 f'{"<em>+" + money(v-b) + "</em>" if over else "<i>" + str(round(v/b*100)) + "%</i>"}</div>'
                 f'<div class="bvt"><i style="width:{v/80*100:.1f}%;background:{"var(--g)" if over else "#5d524a"}"></i><u style="left:{b/80*100:.1f}%"></u></div></div>')
    k = '<div class="kr">' + \
        kpi("Gasto del mes", "$186", note="de $200 previstos", bar=93, icon="caja") + \
        kpi("Tareas hechas", "1.240", "18%", note="vs septiembre", sp=[800, 880, 950, 1010, 1120, 1240], uid="k62", icon="ia") + \
        kpi("Costo por tarea", "$0,15", note="promedio", sp=[0.17, 0.16, 0.16, 0.15, 0.15], uid="k63", icon="doc") + \
        kpi("Áreas sobre presupuesto", "1", note="Soporte", icon="alert") + '</div>'
    main = card("Gasto vs presupuesto por área", "La línea blanca marca el presupuesto", '<div class="bvs">' + rows + '</div>', seg(["Mes", "Trimestre"], "Mes"))
    us = [("Agente de soporte", 74, "var(--g)"), ("Automatizaciones", 60, "var(--g2)"), ("Asistente de chat", 52, "#5d524a")]
    side = card("Por tipo de uso", "$186 en total",
                '<div class="dw">' + donut([(v / 186, c) for _, v, c in us], "$186", "octubre") + '</div>' +
                '<div class="lst">' + "".join('<div><span><i style="background:%s"></i>%s</span><b>%s</b></div>' % (c, n, money(v)) for n, v, c in us) + '</div>',
                ic("dot3", "mute"))
    days = list(range(1, 22))
    cum = [186 * d / 21 * (1 + 0.04 * ((d * 7) % 5 - 2) / 5) for d in days]; cum[-1] = 186
    X = lambda d: 40 + (d - 1) / 30 * 590
    Y = lambda v: 150 - v / 300 * 130
    pts = " ".join("%.1f,%.1f" % (X(d), Y(v)) for d, v in zip(days, cum))
    lc = (f'<svg class="chart" viewBox="0 0 640 180"><g class="gl">' + "".join('<line x1="40" x2="640" y1="%.1f" y2="%.1f"/>' % (Y(v), Y(v)) for v in (0, 100, 200, 300)) + '</g>'
          '<g class="ax">' + "".join('<text x="0" y="%.1f">$%d</text>' % (Y(v) + 5, v) for v in (0, 100, 200, 300)) +
          "".join('<text x="%.1f" y="176" text-anchor="%s">%d oct</text>' % (X(d), "end" if d == 31 else "middle", d) for d in (1, 11, 21, 31)) + '</g>'
          f'<line x1="{X(1):.1f}" y1="{Y(200/31):.1f}" x2="{X(31):.1f}" y2="{Y(200):.1f}" stroke="#8d8279" stroke-width="2.5" stroke-dasharray="8 7"/>'
          f'<polyline points="{pts}" fill="none" stroke="var(--g)" stroke-width="3.5"/>'
          f'<line x1="{X(21):.1f}" y1="{Y(186):.1f}" x2="{X(31):.1f}" y2="{Y(275):.1f}" stroke="var(--g)" stroke-width="2.5" stroke-dasharray="3 6" opacity=".8"/>'
          f'<circle cx="{X(31):.1f}" cy="{Y(275):.1f}" r="6" fill="#15110e" stroke="var(--g)" stroke-width="3"/>'
          f'<text x="{X(31)-10:.1f}" y="{Y(275)+4:.1f}" text-anchor="end" class="vl">Proyección: $275</text></svg>')
    acum = card("Gasto acumulado vs ritmo del presupuesto", "", lc, legend([("var(--g)", "Real"), ("#8d8279", "Presupuesto")]))
    al = f'''<div class="cd alertc"><div class="ah">{ic("alert")}<span>Aviso</span></div>
      <b>Soporte pasó su presupuesto en $14.</b><p>El agente de soporte hizo 410 tareas a $0,18 cada una. Revisa cuáles lo dispararon.</p></div>'''
    body = k + '<div class="g1">' + main + side + '</div><div class="g2">' + acum + al + '</div>'
    return app(5, "Gasto en IA", "Uso de IA del equipo", body)

# ---------- láminas ----------
DASH = [
  ("d2", "#ff5b00", "255,91,0", "#ff9a5c", "Ejecutivo", "¿Cómo va el negocio este mes?", "Facturación, margen, caja y avance contra la meta, en una sola pantalla.", "tus ventas y gastos del mes en una planilla.", d1, "#ff5b00"),
  ("d3", "#f75946", "247,89,70", "#ffab9f", "Ventas", "¿Quién llega a la meta y quién no?", "Ventas por persona, ticket promedio y avance de cada una contra su meta.", "las ventas del mes con el nombre de quien vendió.", d2, "#f75946"),
  ("d4", "#ee5358", "238,83,88", "#f7a3a6", "Caja", "¿Te alcanza la caja para el próximo mes?", "Cobros y pagos que vienen, y un aviso el día que el saldo baja del mínimo.", "cobros y pagos pendientes, cada uno con su fecha.", d3, "#ee5358"),
  ("d5", "#e1556a", "225,85,106", "#f0a3b0", "Marketing", "¿Qué canal te trae clientes que pagan?", "Inversión, clientes nuevos y cuánto te cuesta cada cliente, canal por canal.", "la inversión por canal y de dónde vino cada cliente.", d4, "#e1556a"),
  ("d6", "#e07aa0", "200,89,129", "#f2b8cd", "Operaciones", "¿Dónde se traban tus pedidos?", "Cuántos pedidos hay en cada etapa y cuál acumula atraso.", "los pedidos con la fecha en que pasaron por cada etapa.", d5, "#c85981"),
  ("d7", "#c18bd0", "156,90,167", "#e0c3e8", "Gasto en IA", "¿Cuánto gasta tu equipo en IA, y en qué?", "Gasto por área, costo por tarea y un aviso cuando un área pasa su presupuesto.", "el reporte de consumo que exporta tu proveedor de IA.", d6, "#9c5aa7"),
]

def dots(n, total=8):
    return '<div class="dots">' + "".join('<i class="on"></i>' if i == n else "<i></i>" for i in range(1, total + 1)) + '</div>'

slides = []
for i, (did, g, rgb, g2, name, q, m, need, fn, blob) in enumerate(DASH):
    n = i + 2
    slides.append(f'''
<!-- {n:02d} · {name} -->
<section class="slide" data-n="{n}">
  <div class="grid"></div>
  <div class="blob" style="width:900px;height:620px;left:90px;top:640px;background:{blob}"></div>
  <img class="logo" src="../../brandkit/assets/plogy-white.svg" alt="Plogy">
  <div class="count">{n:02d}/08</div>
  <div class="top">
    <div class="eb" style="color:{g}">Dashboard {i+1} <b>· {name}</b></div>
    <h2>{q}</h2>
    <p class="m">{m}</p>
    <div class="dash" id="{did}" style="--g:{g};--g2:{g2};--ga:rgba({rgb},.55);--gt:rgba({rgb},.16)">{fn()}</div>
  </div>
  <p class="need"><b>Necesitas:</b> {need}</p>
  {dots(n)}
</section>''')

CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "slides.css"), encoding="utf-8").read()

html = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Pieza 018 · Seis dashboards para tu negocio</title>
<!-- GENERADO por scripts/build.py (no editar a mano; editar el script y scripts/slides.css).
     8 láminas de 1080x1350. Una lámina sola: carrusel.html?s=1 ... ?s=8
     Exportar: skills/plogy-cta-design/scripts/render-slides.ps1 -Param s -Keys 1,2,3,4,5,6,7,8 -Prefix slide-0
     Formato inspirado en un carrusel de referencia; el ángulo (pregunta + datos que necesitas) es de Plogy.
     Dashboards: maquetas propias con DATOS DE EJEMPLO, rotuladas en cada pantalla.
     Tipografía: Space Grotesk (display, respaldo de Screener DEMO) e Inter (interfaz de los dashboards). -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>

<!-- 01 · Portada -->
<section class="slide p1" data-n="1">
  <div class="grid"></div>
  <div class="blob" style="width:700px;height:600px;left:-100px;top:100px;background:#ff5b00"></div>
  <div class="blob" style="width:600px;height:500px;right:-150px;top:0;background:#9c5aa7"></div>
  <div class="mini m1" data-clone="d3"></div>
  <div class="mini m2" data-clone="d7"></div>
  <div class="mini m3" data-clone="d2"></div>
  <div class="shade"></div>
  <img class="logo" src="../../brandkit/assets/plogy-white.svg" alt="Plogy">
  <div class="count">01/08</div>
  <span class="pill">Guía</span>
  <div class="bottom">
    <h1>6 dashboards que le puedes pedir a <span class="hl">Claude</span> para tu negocio.</h1>
    <p class="sub">Y la pregunta que responde cada uno. <b>Si no tienes la pregunta, no necesitas el dashboard.</b></p>
  </div>
  {dots(1)}
</section>
{"".join(slides)}

<!-- 08 · CTA: misma clase que la pieza 016 (jueves 22, 19:30), palabra clave CLAUDE -->
<section class="slide p8" data-n="8">
  <div class="grid"></div>
  <div class="blob" style="width:520px;height:420px;left:-120px;top:120px;background:#f75946"></div>
  <div class="blob" style="width:520px;height:420px;right:-120px;top:150px;background:#9c5aa7"></div>
  <div class="blob" style="width:520px;height:420px;left:-120px;bottom:60px;background:#ee5358"></div>
  <div class="blob" style="width:520px;height:420px;right:-120px;bottom:40px;background:#ff5b00"></div>
  <div class="mini m1" data-clone="d3"></div>
  <div class="mini m2" data-clone="d7"></div>
  <div class="mini m3" data-clone="d4"></div>
  <div class="mini m4" data-clone="d2"></div>
  <div class="shade"></div>
  <img class="logo" src="../../brandkit/assets/plogy-white.svg" alt="Plogy">
  <div class="center">
    <p class="ev">Jueves 22, 19:30. Te enseñamos a <strong>crear dashboards para tu negocio.</strong></p>
    <small>Comenta</small>
    <b>CLAUDE</b>
    <p>y te mandamos el link de inscripción.</p>
  </div>
</section>

<script>
  // Copia los dashboards en la portada y el CTA; renombra los id de SVG para que los degradados funcionen en la copia.
  document.querySelectorAll('[data-clone]').forEach(function (h, n) {{
    var src = document.getElementById(h.getAttribute('data-clone'));
    if (!src) return;
    var c = src.cloneNode(true);
    c.removeAttribute('id');
    c.innerHTML = c.innerHTML.replace(/id="([^"]+)"/g, 'id="$1-c' + n + '"').replace(/url\\(#([^)]+)\\)/g, 'url(#$1-c' + n + ')');
    h.appendChild(c);
  }});
  var m = location.search.match(/s=(\\d+)/);
  if (m) {{
    document.body.classList.add('single');
    var el = document.querySelector('.slide[data-n="' + m[1] + '"]');
    if (el) el.classList.add('on');
  }}
</script>
</body>
</html>
'''
open(OUT, "w", encoding="utf-8", newline="\n").write(html)
print("ok", OUT)
