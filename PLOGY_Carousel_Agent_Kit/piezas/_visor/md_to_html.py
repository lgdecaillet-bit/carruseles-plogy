"""Convierte archivos .md de las piezas en .html legibles para el visor (piezas/visor.html).

No modifica los .md. Crea un .html con el mismo nombre al lado de cada uno.

Uso:
    python -I md_to_html.py <archivo.md> [<archivo2.md> ...]

Soporta lo que usan los briefs: títulos, párrafos, listas (con un nivel de sangría y casillas [ ] / [x]),
tablas con tuberías, citas con >, bloques de código, **negrita**, `código`, enlaces sueltos e imágenes
en su propia línea: ![texto alternativo](ruta/relativa.png "pie de figura opcional").
"""
import html
import io
import re
import sys
import os

CSS = """
:root{--ink:#171310;--paper:#fff;--muted:#625951;--orange:#ff5b00;--orangeText:#b43d00;--surface:#f4f1ef;--border:#d9d0c7;
--display:'Space Grotesk','Helvetica Neue',Arial,sans-serif;--body:'Helvetica Neue',Helvetica,Arial,sans-serif}
@media (prefers-color-scheme:dark){:root{--ink:#f4efe9;--paper:#171310;--muted:#bdb2a8;--surface:#211b17;--border:#3a322c;--orangeText:#ff8a4d}}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.65 var(--body)}
main{max-width:820px;margin:0 auto;padding:40px 24px 96px}
h1,h2,h3{font-family:var(--display);letter-spacing:-.025em;line-height:1.15}
h1{font-size:40px;margin:0 0 24px}
h2{font-size:28px;margin:48px 0 12px;padding-top:24px;border-top:1px solid var(--border)}
h3{font-size:21px;margin:32px 0 8px}
p,li{max-width:70ch}
a{color:var(--orangeText);word-break:break-word}
code{font:14px ui-monospace,Consolas,monospace;background:var(--surface);padding:2px 6px;border-radius:6px;word-break:break-word}
pre{background:var(--surface);padding:16px;border-radius:12px;overflow:auto}
pre code{background:none;padding:0}
blockquote{margin:18px 0;padding:6px 0 6px 20px;border-left:6px solid var(--orange);color:var(--ink)}
blockquote p{margin:8px 0}
table{border-collapse:collapse;width:100%;font-size:15px;margin:18px 0;display:block;overflow-x:auto}
th,td{border:1px solid var(--border);padding:10px 12px;text-align:left;vertical-align:top;min-width:120px}
th{background:var(--surface);font-family:var(--display)}
ul,ol{padding-left:24px}
li{margin:6px 0}
li.check{list-style:none;margin-left:-24px}
li.check input{margin-right:10px}
figure{margin:28px 0}
figure img{display:block;width:100%;height:auto;border-radius:14px;border:1px solid var(--border)}
figcaption{margin-top:8px;font-size:14px;line-height:1.4;color:var(--muted)}
hr{border:0;border-top:1px solid var(--border);margin:32px 0}
.tag{display:inline-block;background:var(--orange);color:#171310;font:700 13px var(--display);letter-spacing:.06em;text-transform:uppercase;padding:6px 12px;border-radius:999px;margin-bottom:18px}
"""

URL = re.compile(r"(https?://[^\s<)]+)")


def inline(text):
    codes = []

    def keep_code(m):
        codes.append(m.group(1))
        return "\x00%d\x00" % (len(codes) - 1)

    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)

    def link(m):
        u = m.group(1)
        tail = ""
        while u and u[-1] in ".,;:":
            tail = u[-1] + tail
            u = u[:-1]
        return '<a href="%s" target="_blank" rel="noopener">%s</a>%s' % (u, u, tail)

    text = URL.sub(link, text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: "<code>%s</code>" % html.escape(codes[int(m.group(1))], quote=False), text)
    return text


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def convert(md):
    lines = md.replace("\r\n", "\n").split("\n")
    out = []
    i = 0
    para = []

    def flush():
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if s.startswith("```"):
            flush()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            out.append("<pre><code>%s</code></pre>" % html.escape("\n".join(buf), quote=False))
            i += 1
            continue

        if not s:
            flush()
            i += 1
            continue

        m = re.match(r"^(#{1,3})\s+(.*)$", s)
        if m:
            flush()
            n = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (n, inline(m.group(2)), n))
            i += 1
            continue

        img = re.match(r'^!\[(.*?)\]\((\S+?)(?:\s+"(.*)")?\)$', s)
        if img:
            flush()
            alt, src, cap = img.group(1), img.group(2), img.group(3)
            fig = '<figure><img src="%s" alt="%s" loading="lazy">' % (html.escape(src), html.escape(alt))
            if cap:
                fig += "<figcaption>%s</figcaption>" % inline(cap)
            out.append(fig + "</figure>")
            i += 1
            continue

        if s == "---":
            flush()
            out.append("<hr>")
            i += 1
            continue

        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1]):
            flush()
            head = split_row(s)
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            t = ["<table><thead><tr>" + "".join("<th>%s</th>" % inline(c) for c in head) + "</tr></thead><tbody>"]
            for r in rows:
                t.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue

        if s.startswith(">"):
            flush()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            out.append("<blockquote>" + "".join("<p>%s</p>" % inline(b) for b in buf if b) + "</blockquote>")
            continue

        if re.match(r"^(\s*)([-*]|\d+\.)\s+", line):
            flush()
            ordered = bool(re.match(r"^\s*\d+\.\s+", line))
            tag = "ol" if ordered else "ul"
            items = []
            while i < len(lines) and re.match(r"^(\s*)([-*]|\d+\.)\s+", lines[i]):
                items.append(lines[i])
                i += 1
            out.append(render_list(items, tag))
            continue

        para.append(s)
        i += 1

    flush()
    return "\n".join(out)


def render_list(items, tag):
    base = min(len(it) - len(it.lstrip()) for it in items)
    html_parts = ["<%s>" % tag]
    idx = 0
    while idx < len(items):
        it = items[idx]
        indent = len(it) - len(it.lstrip())
        body = re.sub(r"^\s*([-*]|\d+\.)\s+", "", it)
        subs = []
        idx += 1
        while idx < len(items) and (len(items[idx]) - len(items[idx].lstrip())) > indent:
            subs.append(items[idx])
            idx += 1
        check = re.match(r"^\[( |x)\]\s+(.*)$", body)
        if check:
            box = '<input type="checkbox" disabled%s> ' % (" checked" if check.group(1) == "x" else "")
            li = '<li class="check">%s%s' % (box, inline(check.group(2)))
        else:
            li = "<li>%s" % inline(body)
        if subs:
            sub_tag = "ol" if re.match(r"^\s*\d+\.\s+", subs[0]) else "ul"
            li += render_list(subs, sub_tag)
        li += "</li>"
        html_parts.append(li)
    html_parts.append("</%s>" % tag)
    return "".join(html_parts)


def page(title, body):
    return """<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<!-- Generado automáticamente desde el .md del mismo nombre con piezas/_visor/md_to_html.py. Edita el .md, no este archivo. -->
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<style>%s</style></head>
<body><main>
%s
</main></body></html>
""" % (html.escape(title), CSS, body)


def main(paths):
    for p in paths:
        md = io.open(p, encoding="utf-8").read()
        m = re.search(r"^#\s+(.+)$", md, re.M)
        title = m.group(1) if m else os.path.basename(p)
        out = os.path.splitext(p)[0] + ".html"
        io.open(out, "w", encoding="utf-8", newline="\n").write(page(title, convert(md)))
        print("ok", out)


if __name__ == "__main__":
    main(sys.argv[1:])
