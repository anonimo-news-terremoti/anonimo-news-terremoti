import requests
import json
from datetime import datetime


URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"


def scarica_terremoti():

    risposta = requests.get(URL)

    dati = risposta.json()

    eventi = []


    for evento in dati["features"][:20]:

        prop = evento["properties"]
        coord = evento["geometry"]["coordinates"]

        eventi.append({

            "magnitudo": prop["mag"],
            "luogo": prop["place"],

            "profondita": f"{coord[2]} km",

            "data": datetime.fromtimestamp(
                prop["time"] / 1000
            ).strftime("%d/%m/%Y"),

            "ora": datetime.fromtimestamp(
                prop["time"] / 1000
            ).strftime("%H:%M"),

            "fonte": "USGS",

            "lat": coord[1],
            "lon": coord[0]

        })


    return eventi



eventi = scarica_terremoti()




print("✅ Eventi terremoti aggiornati:", len(eventi))


import requests
import json
from datetime import datetime


URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"


def scarica_terremoti():

    risposta = requests.get(URL)

    dati = risposta.json()

    eventi = []

    for evento in dati["features"][:20]:

        prop = evento["properties"]
        coord = evento["geometry"]["coordinates"]

        eventi.append({

            "magnitudo": prop["mag"],
            "luogo": prop["place"],

            "profondita": f"{coord[2]} km",

            "data": datetime.fromtimestamp(
                prop["time"] / 1000
            ).strftime("%d/%m/%Y"),

            "ora": datetime.fromtimestamp(
                prop["time"] / 1000
            ).strftime("%H:%M"),

            "fonte": "USGS",

            "lat": coord[1],
            "lon": coord[0]

        })

    return eventi



eventi = scarica_terremoti()


with open("dati/eventi.json", "w", encoding="utf-8") as file:
    json.dump(
        eventi,
        file,
        indent=2,
        ensure_ascii=False
    )


print("✅ Eventi terremoti aggiornati:", len(eventi))


import os

os.system("python3 bot/crea_mappa_epicentro.py")
os.system("python3 bot/grafica_terremoto.py")
