Heart Health Predictor :
The Heart Health Predictor is a web application that uses a machine learning model to predict whether an individual's heart is healthy or not. The application takes various health parameters as input and provides a prediction based on the trained logistic regression model.

Features:
- Machine Learning Model: Utilizes a logistic regression model trained on heart disease data.
- User-Friendly Interface: Simple and intuitive web interface for inputting health parameters.
- Instant Prediction: Provides immediate feedback on heart health based on the input data.

Input Parameters:
The model requires the following parameters to make a prediction:
- Age
- Chest Pain Type (cp)
- Number of Major Vessels (ca)
- Maximum Heart Rate Achieved (thalach)
- ST Depression Induced by Exercise (oldpeak)
- Thalassemia (thal)
- Resting Blood Pressure (trestbps)
- Serum Cholesterol (chol)
- Exercise Induced Angina (exang)
- Slope of the Peak Exercise ST Segment (slope)

Prediction Output :
- Heart is healthy, you're a fit : The model predicts that the individual's heart is healthy.
- Heart is unhealthy, consult a doctor : The model predicts that the individual's heart may be at risk, and a consultation with a doctor is advised.
