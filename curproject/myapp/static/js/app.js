const c1 = document.querySelector("#currency_input");
const c2 = document.querySelector("#currency_output");
c2.addEventListener("change", calculate);



const amount1 = document.getElementById("input_field");
const amount2 = document.getElementById("output_field");

const swap = document.getElementById("swap");
const theRate = document.getElementById("result");
// fetch exchange rate from the api
function calculate() {
    const curr1 = c1.value; // Get the selected currency value
    const curr2 = c2.value; // Get the selected currency value

    fetch(`https://v6.exchangerate-api.com/v6/eb41d6043cc2d4b7ef6b7094/latest/${curr1}`)
    .then((res) => res.json())
    .then((data) => {
        const rate = data.conversion_rates[curr2];
        theRate.innerText = `1 ${curr1} = ${rate} ${curr2}`;
        amount2.value = (amount1.value * rate).toFixed(2);
    });
}

// Event listeners
c1.addEventListener("change", calculate);
amount1.addEventListener("input", calculate);

c2.addEventListener("change", calculate);
amount2.addEventListener("input", calculate);

swap.addEventListener("click", () => {
    // Swap the selected currency values
    const temp = c1.value;
    c1.value = c2.value;
    c2.value = temp;

    // Call calculate() after the swap
    calculate();
});