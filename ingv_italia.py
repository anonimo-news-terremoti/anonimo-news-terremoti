import requests
import json
from datetime import datetime


URL = "https://webservices.ingv.it/fdsnws/event/1/query?format=geojson&limit=20&minmag=1"


def scarica_ingv():

    risposta = requests.get(URL)

    dati = risposta.json()

    eventi = []


    for evento in dati["features"]:

        prop = evento["properties"]
        coord = evento["geometry"]["coordinates"]


        eventi.append({

            "magnitudo": prop.get("mag"),

            "luogo": prop.get("place"),

            "profondita": f"{coord[2]} km",

            "data": prop["time"][:10],

            "ora": prop["time"][11:16],


            "fonte": "INGV",

            "lat": coord[1],

            "lon": coord[0]

        })


    return eventi



eventi = scarica_ingv()


with open("dati/italia/eventi_italia.json",
          "w",
          encoding="utf-8") as file:


    json.dump(
        eventi,
        file,
        indent=2,
        ensure_ascii=False
    )


print("✅ INGV Italia aggiornato:", len(eventi))
