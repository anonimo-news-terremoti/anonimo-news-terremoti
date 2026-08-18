fetch("dati/eventi.json")
.then(response => response.json())
.then(eventi => {

    let contenitore = document.getElementById("eventi");

    eventi.forEach(evento => {

        contenitore.innerHTML += `

        <div class="scheda">

        <h3>🌋 Magnitudo ${evento.magnitudo}</h3>

        <p>📍 ${evento.luogo}</p>

        <p>⬇️ Profondità: ${evento.profondita}</p>

        <p>📅 ${evento.data}</p>

        <p>🕒 ${evento.ora}</p>

        <p>📡 Fonte: ${evento.fonte}</p>

        <p>🌐 Coordinate: ${evento.lat}, ${evento.lon}</p>

        </div>

        `;

    });

})
.catch(error => {

console.log("Errore caricamento terremoti:", error);

});


fetch("dati/eventi.json")
.then(response => response.json())
.then(eventi => {

    const contenitore = document.getElementById("eventi");

    contenitore.innerHTML = "";

    eventi.forEach(evento => {

        contenitore.innerHTML += `

        <div class="scheda">

            <h2>🌋 Magnitudo ${evento.magnitudo}</h2>

            <p>📍 Luogo: ${evento.luogo}</p>

            <p>⬇️ Profondità: ${evento.profondita}</p>

            <p>📅 Data: ${evento.data}</p>

            <p>🕒 Ora: ${evento.ora}</p>

            <p>📡 Fonte: ${evento.fonte}</p>

            <p>🌐 Coordinate: ${evento.lat}, ${evento.lon}</p>

        </div>

        `;

    });

})
.catch(error => {

    document.getElementById("eventi").innerHTML =
    "Errore caricamento dati terremoti";

    console.log(error);

});
