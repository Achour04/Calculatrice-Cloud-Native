//const apiBaseUrl = 'calculatrice-nathanf.polytech-dijon.kiowy.net/api';

document.getElementById('calc-form').addEventListener('submit', async function (e) {
    e.preventDefault(); // Empêcher le rechargement de la page

    // Récupérer les valeurs du formulaire
    const operation = document.getElementById('operation').value.trim();
    const operand1 = parseFloat(document.getElementById('operand1').value.trim());
    const operand2 = parseFloat(document.getElementById('operand2').value.trim());

    


    const operands = [operand1, operand2];
    console.log(operands);

    
    // Vérification de validité des opérandes
    if (isNaN(operand1) || isNaN(operand2)) {
        document.getElementById('result').innerText = "Veuillez entrer des opérandes valides.";
        return; // Sortir de la fonction si les opérandes ne sont pas valides
    }

    // Préparer la requête pour l'API
    const apiUrl = `api/calculate`; // L'API est relative au domaine du frontend
    const payload = { operation, operands };

    try {
        // Envoyer une requête POST à l'API
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });

        if (response.ok) {
            const data = await response.json();
            const resultId = data.id;

            // Afficher le résultat intermédiaire (ID)
            document.getElementById('result').innerText = `Calcul soumis. En attente du résultat...`;

            // Récupérer le résultat du calcul
            await fetchResult(resultId);
        } else {
            const errorData = await response.json();
            document.getElementById('result').innerText = `Erreur : ${errorData.error || 'Impossible de calculer'}`;
        }
    } catch (error) {
        document.getElementById('result').innerText = `Erreur réseau : ${error.message}`;
    }
});

// Fonction pour récupérer le résultat depuis l'API
async function fetchResult(resultId) {
    const resultUrl = `api/result/${resultId}`; // L'API est relative au domaine du frontend

    try {
        let attempts = 0;
        let result;

        // Boucle pour attendre le résultat (polling)
        while (attempts < 10) {
            const response = await fetch(resultUrl);
            if (response.ok) {
                const data = await response.json();
                result = data.result;
                break;
            }

            // Attendre 2 secondes avant de réessayer
            await new Promise(resolve => setTimeout(resolve, 2000));
            attempts++;
        }

        // Afficher le résultat ou un message d'erreur si indisponible
        if (result !== undefined) {
            document.getElementById('result').innerText = `Résultat : ${result}`;
        } else {
            document.getElementById('result').innerText = `Résultat indisponible. Veuillez réessayer plus tard.`;
        }
    } catch (error) {
        document.getElementById('result').innerText = `Erreur réseau lors de la récupération du résultat : ${error.message}`;
    }
}
