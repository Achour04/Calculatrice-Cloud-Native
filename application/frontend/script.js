document.addEventListener("DOMContentLoaded", function () {
    const operationForm = document.getElementById('operation-form');
    const resultForm = document.getElementById('result-form');

    // Envoyer une opération
    operationForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const operation = document.getElementById('operation').value;
        const operand1 = document.getElementById('operand1').value;
        const operand2 = document.getElementById('operand2').value;

        const response = await fetch('http://127.0.0.1:5000/api/calculate', {  // URL mise à jour
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ num1: Number(operand1), num2: Number(operand2), operator: operation })
        });

        const result = await response.json();
        document.getElementById('operation-result').innerText = `ID généré : ${result.id}`;
    });

    // Récupérer un résultat
    resultForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const operationId = document.getElementById('operation-id').value;

        const response = await fetch(`http://127.0.0.1:5000/api/result/${operationId}`, {  // URL mise à jour
            method: 'GET',
        });
        const result = await response.json();

        if (result.error) {
            document.getElementById('result-output').innerText = `Erreur : ${result.error}`;
        } else {
            document.getElementById('result-output').innerText = `Résultat : ${result.result}`;
        }
    });
});
