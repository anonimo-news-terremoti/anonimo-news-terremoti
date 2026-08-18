async function caricaUltimoTerremoto() {

    let italia = await fetch("dati/italia/eventi_italia.json")
        .then(r => r.json());

    let mondo = await fetch("dati/eventi.json")
        .then(r => r.json());


    let eventi = [...italia, ...mondo];


    eventi.sort((a,b) => {

        let dataA = new Date(a.data + " " + a.ora);
        let dataB = new Date(b.data + " " + b.ora);

        return dataB - dataA;

    });


    let ultimo = eventi[0];


    document.getElementById("ultimo-terremoto").innerHTML = `


<h2>🌋 Magnitudo ${ultimo.magnitudo}</h2>

<p>📍 ${ultimo.luogo}</p>

<p>⬇️ Profondità: ${ultimo.profondita}</p>

<p>📅 ${ultimo.data}</p>

<p>🕒 ${ultimo.ora}</p>

<p>📡 Fonte: ${ultimo.fonte}</p>

<p>🌐 Coordinate:
${ultimo.lat}, ${ultimo.lon}
</p>

`;

}


caricaUltimoTerremoto();
