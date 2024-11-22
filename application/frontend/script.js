let display = document.getElementById("display");

function appendNumber(number) {
    if (display.innerText === "0") {
        display.innerText = number;
    } else {
        display.innerText += number;
    }
}

function appendOperator(operator) {
    const lastChar = display.innerText.slice(-1);
    if (["+", "-", "*", "/"].includes(lastChar)) {
        return; // Prevent multiple operators in a row
    }
    display.innerText += operator;
}

function clearDisplay() {
    display.innerText = "0";
}

function calculate() {
    try {
        display.innerText = eval(display.innerText);
    } catch (error) {
        display.innerText = "Erreur";
    }
}
