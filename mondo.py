import requests
import json


URL = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=50&minmagnitude=4"


def scarica_mondo():

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

            "data": prop["time"],

            "fonte": "USGS",

            "lat": coord[1],

            "lon": coord[0]

        })


    return eventi



eventi = scarica_mondo()


with open(
    "dati/mondo/eventi_mondo.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        eventi,
        file,
        indent=2,
        ensure_ascii=False
    )


print("🌍 Terremoti mondo aggiornati:", len(eventi))
