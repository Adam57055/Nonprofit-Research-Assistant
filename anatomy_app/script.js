// script.js
const input = document.getElementById("prompt");
const button = document.getElementById("submitBtn");
const output = document.getElementById("output");

button.addEventListener("click", async () => {
    const userPrompt = input.value.trim();
    if (!userPrompt) return;

    button.disabled = true;
    button.textContent = "Thinking...";
    output.textContent = "";

    try {
        const response = await fetch("http://localhost:5000/api/lecture", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt: userPrompt })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        output.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        output.textContent = "Something went wrong: " + err.message;
    } finally {
        button.disabled = false;
        button.textContent = "Submit";
    }
});