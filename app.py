from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('final_logreg_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        features = [float(x) for x in request.form.values()]
        feature_array = np.array([features])
        prediction = model.predict(feature_array)
        if prediction[0] == 1:
            output = "Heart is unhealthy, consult a doctor :("
        else:
            output = "Heart is healthy, you're fit ;)"
        return render_template('result.html', prediction=output)

if __name__ == '__main__':
    app.run(debug=True)
