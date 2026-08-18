from staticmap import StaticMap, CircleMarker
from PIL import Image, ImageDraw
import json
import os


FILE = "dati/italia/eventi_italia.json"
OUTPUT = "immagini/citta/zona_evento.png"


def carica_evento():

    with open(FILE, "r", encoding="utf-8") as f:
        eventi = json.load(f)

    return eventi[0]


def crea_mappa(evento):

    lat = float(evento["lat"])
    lon = float(evento["lon"])


    mappa = StaticMap(
        800,
        600,
        url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png"
    )


    # onde sismiche

    magnitudo = float(evento["magnitudo"])

    base = int(20 + (magnitudo * 15))


    for raggio, colore in [
        (base * 3, "#ff9999"),
        (base * 2, "#ff3333"),
        (base, "#ff0000")
    ]:
        mappa.add_marker(
            CircleMarker(
                (lon, lat),
                colore,
                raggio
            )
    )


    # centro epicentro

    mappa.add_marker(
        CircleMarker(
            (lon, lat),
            "#b30000",
            10
        )
    )

    immagine = mappa.render(
        zoom=13
    )


    os.makedirs(
        "immagini/zone",
        exist_ok=True
    )


    # aggiunta onde sismiche sulla mappa

img = Image.open(OUTPUT)

draw = ImageDraw.Draw(img)


centro_x = 400
centro_y = 300


for raggio in [40, 80, 120]:

    draw.ellipse(
        (
            centro_x-raggio,
            centro_y-raggio,
            centro_x+raggio,
            centro_y+raggio
        ),
        outline="#ff0000",
        width=4
    )


    # punto epicentro

    draw.ellipse(
        (
            centro_x-10,
            centro_y-10,
            centro_x+10,
            centro_y+10
        ),
        fill="#ff0000"
    )


    img.save(OUTPUT)


    print("✅ Mappa creata:", OUTPUT)



evento = carica_evento()

crea_mappa(evento)
