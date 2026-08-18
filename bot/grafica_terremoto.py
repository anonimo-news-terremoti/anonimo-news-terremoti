from PIL import Image, ImageDraw, ImageFont
import json
import os


FILE_ITALIA = "dati/italia/eventi_italia.json"

OUTPUT = "immagini/terremoti/ultimo.png"

LOGO = "immagini/logo/logo.png"

FOTO_CITTA = "immagini/citta/zona_evento.png"

MAPPA = "immagini/zone/epicentro.png"


def carica_evento():

    with open(FILE_ITALIA, "r", encoding="utf-8") as file:
        eventi = json.load(file)

    return eventi[0]


def posizione_epicentro(lat, lon):

    lat_min = 40.0
    lat_max = 42.0

    lon_min = 13.0
    lon_max = 15.0

    x = int(
        (lon - lon_min) /
        (lon_max - lon_min) *
        900
    )

    y = int(
        (lat_max - lat) /
        (lat_max - lat_min) *
        500
    )

    return x + 90, y + 330


def crea_grafica(evento):

    larghezza = 1080
    altezza = 1800


    img = Image.new(
        "RGB",
        (larghezza, altezza),
        "#050b16"
    )


    draw = ImageDraw.Draw(img)



    try:

        titolo = ImageFont.truetype(
            "DejaVuSans-Bold.ttf",
            65
        )

        grande = ImageFont.truetype(
            "DejaVuSans-Bold.ttf",
            120
        )

        testo = ImageFont.truetype(
            "DejaVuSans.ttf",
            42
        )

        ora_font = ImageFont.truetype(
            "DejaVuSans-Bold.ttf",
            45
        )

    except:

        titolo = grande = testo = None



    # LOGO

    if os.path.exists(LOGO):

        logo = Image.open(LOGO)

        logo.thumbnail((250,250))

        img.paste(
            logo,
            (60,40),
            logo if logo.mode == "RGBA" else None
        )



    draw.text(
        (360,100),
        "ANONIMO NEWS",
        fill="white",
        font=titolo
    )

    # ORA EVENTO IN ALTO

    testo_ora = f"ORA EVENTO: {evento['ora']}"

    bbox = draw.textbbox(
        (0,0),
        testo_ora,
        font=grande
    )

    larghezza_testo = bbox[2] - bbox[0]

    x = (1080 - larghezza_testo) // 2


    # linea sinistra
    draw.line(
        (250,285, x-30,285),
        fill="#00aaff",
        width=5
    )

    # testo centrale
    draw.text(
        (265,260),
        testo_ora,
        font=ora_font,
        fill="white"
    )

    # linea destra
    draw.line(
        (x + larghezza_testo + 30,285,783,285),
        fill="#00aaff",
        width=5
    )
    # FOTO CITTA'

    if os.path.exists(FOTO_CITTA):

        foto = Image.open(FOTO_CITTA)

        foto.thumbnail((900,550))

        img.paste(
            foto,
            (90,330)
        )



    # EPICENTRO SULLA FOTO

    centro_x, centro_y = posizione_epicentro(
        float(evento["lat"]),
        float(evento["lon"])
     )

    # onde sismiche

    for raggio in [40, 80, 120]:

        draw.ellipse(
            (
                centro_x-raggio,
                centro_y-raggio,
                centro_x+raggio,
                centro_y+raggio
            ),
            outline="#ff0000",
            width=8
        )


    # punto epicentro

    draw.ellipse(
        (
            centro_x-25,
            centro_y-25,
            centro_x+25,
            centro_y+25
        ),
        fill="#ff0000"
    )


    draw.text(
        (80,980),
        "🚨 TERREMOTO",
        fill="#ff0000",
        font=titolo
    )


    draw.text(
        (80,1080),
        f"M {float(evento['magnitudo']):.1f}",
        fill="white",
        font=grande
    )



    informazioni = f"""
📍 {evento['luogo']}

⬇ Profondità:
{evento['profondita']}

📅 {evento['data']}

draw.text(
    (100, 1600),
    f"🕒 Ora: {evento['ora']}",
    font=font,
    fill="white"
)

draw.text(
    (100, 1660),
    f"📡 Fonte: {evento['fonte']}",
    font=font,
    fill="white"
)

draw.text(
    (100, 1720),
    f"🌐 Coordinate: {evento['lat']} {evento['lon']}",
    font=font,
    fill="white"
)

draw.text(
    (100, 1600),
    f"🕒 Ora: {evento['ora']}",
    font=font,
    fill="white"
)

draw.text(
    (100, 1660),
    f"📡 Fonte: {evento['fonte']}",
    font=font,
    fill="white"
)

draw.text(
    (100, 1720),
    f"🌐 Coordinate: {evento['lat']} {evento['lon']}",
    font=font,
    fill="white"
)

🕒 {evento['ora']}

📡 {evento['fonte']}
"""


    draw.multiline_text(
        (80,1300),
        informazioni,
        fill="white",
        font=testo,
        spacing=25
    )



    os.makedirs(
        "immagini/terremoti",
        exist_ok=True
    )

    draw.text(
        (100, 1215),
        f"Fonte: {evento['fonte']}",
        font=testo,
        fill="white"
    )

    draw.text(
        (100, 1275),
        f"Coordinate: {evento['lat']} {evento['lon']}",
        font=testo,
        fill="white"
    )

    img.save(
        OUTPUT
    )


    print(
        "✅ Grafica creata:",
        OUTPUT
    )




evento = carica_evento()

crea_grafica(evento)
