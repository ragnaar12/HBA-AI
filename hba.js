// script.js
document.getElementById('analyzeBtn').addEventListener('click', function() {
    var text = document.getElementById('inputText').value;

    if (!text) {
        alert("Veuillez entrer un texte à analyser.");
        return;
    }

    // Envoi du texte à l'API Flask pour analyse
    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'text=' + encodeURIComponent(text)
    })
    .then(response => response.json())
    .then(data => {
        // Afficher l'analyse syntaxique
        var syntaxList = document.getElementById('syntaxList');
        syntaxList.innerHTML = '';
        data.syntax.forEach(function(token) {
            var listItem = document.createElement('li');
            listItem.textContent = `${token.text} (${token.pos}) - Dépendance : ${token.dep}`;
            syntaxList.appendChild(listItem);
        });

        // Afficher l'analyse de sentiment
        document.getElementById('sentiment').textContent = "Sentiment : " + data.sentiment;
        document.getElementById('confidence').textContent = "Confiance : " + data.confidence.toFixed(2);
    })
    .catch(error => {
        console.error('Erreur:', error);
    });
});

