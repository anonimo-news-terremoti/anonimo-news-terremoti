#!/bin/bash

cd ~/anonimo-news-terremoti

if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
fi

python ingv_italia.py

git add dati/italia/eventi_italia.json

git commit -m "Aggiornamento terremoti INGV"

git push
