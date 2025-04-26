function analyzeSentiment() {
    let text = document.getElementById("text-input").value;
    let resultDiv = document.getElementById("result");

    if (!text.trim()) {
        resultDiv.innerHTML = "⚠️ Please enter some text!";
        return;
    }

    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultDiv.innerHTML = `⚠️ Error: ${data.error}`;
        } else {
            resultDiv.innerHTML = `✅ Sentiment: ${data.sentiment} (Confidence: ${(data.confidence * 100).toFixed(2)}%)`;
        }
    })
    .catch(error => {
        resultDiv.innerHTML = `⚠️ Error: ${error}`;
    });
}
