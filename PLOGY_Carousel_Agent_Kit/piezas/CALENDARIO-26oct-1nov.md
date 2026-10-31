# Calendario · lunes 26 de octubre a domingo 1 de noviembre de 2026

Estado: BORRADOR para revisión humana. Nada se publica sin aprobación con fecha.

## Mezcla

| Tipo | Meta | Piezas | Real |
|---|---|---|---|
| Noticias de IA | 60% | 027, 029, 030, 032, 035, 036, 038, 039, 040 | 9 de 15 (60%) |
| Clase "Cómo crear tu asistente de IA" (CTA Comenta CLASE, jueves 29) | 25% | 028, 031, 033, 034 | 4 de 15 (27%) |
| Lead magnets | 15% | 037 (CARRUSELES), 041 (TAREAS) | 2 de 15 (13%) |

Las cuatro piezas de la clase salen antes de la clase: de lunes a jueves en la mañana.

## Día por día

| Día | Pieza | Tipo | CTA |
|---|---|---|---|
| Lun 26 | 027 · ChatGPT Ads llega a Colombia | Noticia | Sigue a Plogy |
| Lun 26 | 028 · Tu asistente de IA no es un chat | Clase 1/4 | Comenta CLASE |
| Lun 26 | 029 · Anthropic pide salir a bolsa (noticia de hoy) | Noticia | Sigue a Plogy |
| Mar 27 | 030 · WhatsApp Business vuelve a cobrar | Noticia | Sigue a Plogy |
| Mar 27 | 031 · Cinco tareas para tu asistente | Clase 2/4 | Comenta CLASE |
| Mié 28 | 032 · Gemini para pequeños negocios | Noticia | Sigue a Plogy |
| Mié 28 | 033 · Las instrucciones de tu asistente | Clase 3/4 | Comenta CLASE |
| Jue 29 (mañana) | 034 · Hoy creamos tu asistente | Clase 4/4 | Comenta CLASE |
| Jue 29 | 035 · ILIA 2026: 7 de cada 100 pequeñas empresas | Noticia | Sigue a Plogy |
| Vie 30 | 036 · GPT-6 arma herramientas | Noticia | Sigue a Plogy |
| Vie 30 | 037 · ¿Quieres que tus carruseles se vean así? | Lead magnet | Comenta CARRUSELES |
| Sáb 31 | 038 · Canva Craft | Noticia | Sigue a Plogy |
| Sáb 31 | 039 · Las Gems de Gemini se retiran | Noticia | Sigue a Plogy |
| Dom 1 | 040 · Claude cambia sus reglas de uso | Noticia | Sigue a Plogy |
| Dom 1 | 041 · ¿Qué tarea automatizar primero? | Lead magnet | Comenta TAREAS |

## Cruce de audiencias

- Las piezas de la clase enseñan a crear un asistente personal: es el tema que eligió Plogy para la clase y llevan a la inscripción.
- 037 no enseña a hacer carruseles: muestra el resultado y el método en grande, y el DM abre la conversación comercial. No mandar la skill de la pieza 024 a quien comenta CARRUSELES.
- 041 entrega una plantilla para elegir qué automatizar: deja al negocio con una tarea lista para que Plogy la implemente.

## Pendientes que bloquean la semana

1. **Clase:** confirmar hora (puse 19:30, la de la clase anterior), si es gratis y el link de inscripción. Cambiar en `_comun/clase.py` y regenerar 028, 031, 033 y 034.
2. **Respuestas automáticas:** CLASE (ya se usó antes para otra clase: que apunte a la del 29), CARRUSELES y TAREAS.
3. **Recursos en enlace:** `037/recurso-como-hacemos-carruseles.md` y `041/recurso-plantilla-tareas.md` + `plantilla-tareas.csv`.
4. **Oferta comercial** de 037 y del segundo DM de 041: la tiene que definir Plogy.
5. **029** es de hoy: revisar novedades antes de publicar.
6. **035:** abrir a mano el PDF de CEPAL y confirmar las cifras (el sitio de CEPAL bloquea la lectura automática; las cifras salen del sitio oficial del índice).
7. **037:** usar solo piezas ya publicadas en las láminas.

## Cómo regenerar

Cada pieza tiene `generar.py`, que usa la plantilla compartida `_comun/plogy.py`. Desde `piezas/`:

```
python 028-tu-asistente-no-es-un-chat/generar.py
python _comun/render.py 028-tu-asistente-no-es-un-chat
```
