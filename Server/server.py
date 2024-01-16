from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the pickled model
with open('your_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request
    data = request.get_json()

    # Extract features from the input data
    pclass = data['Pclass']
    sex = data['Sex']
    age = data['Age']
    sibsp = data['SibSp']
    parch = data['Parch']
    embarked = data['Embarked']

    # Perform necessary mappings and conversions
    sex_mapping = {'male': 0, 'female': 1}
    sex_numeric = sex_mapping.get(sex.lower(), 0)

    embarked_mapping = {'s': 0, 'c': 1, 'q': 2}
    embarked_numeric = embarked_mapping.get(embarked.lower(), 0)

    # Create an input vector
    input_vector = np.array([pclass, sex_numeric, age, sibsp, parch, embarked_numeric])

    # Make the prediction
    prediction = model.predict([input_vector])[0]

    # Assuming the model returns 1 for survival and 0 for non-survival
    result = "Survived" if prediction == 1 else "Not Survived"

    # Return the result as JSON
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
