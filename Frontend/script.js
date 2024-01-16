function predictSurvival() {
    // Get input values
    const pclass = document.getElementById('pclass').value;
    const sex = document.getElementById('sex').value;
    const age = document.getElementById('age').value;
    const sibsp = document.getElementById('sibsp').value;
    const parch = document.getElementById('parch').value;
    const embarked = document.getElementById('embarked').value;
  
    // Prepare data for the POST request
    const data = {
      pclass: pclass,
      sex: sex,
      age: age,
      sibsp: sibsp,
      parch: parch,
      embarked: embarked
    };
  
    // Make a POST request to the Flask server
const formData = new FormData();

// Append each key-value pair from data to the formData object
Object.entries(data).forEach(([key, value]) => {
  formData.append(key, value);
});

// Make a POST request to the Flask server
fetch('http://127.0.0.1:5000/predict', {
  method: 'POST',
  body: formData,
})
  .then(response => response.json())
  .then(result => {
    // Display the prediction result
    const resultContainer = document.getElementById('predictionResult');
    resultContainer.innerHTML = `<p>Prediction Result: ${result.prediction}</p>`;
  })
  .catch(error => console.error('Error:', error));

}