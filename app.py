from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

model = joblib.load("models/cyber_model.pkl")
scaler = joblib.load("models/scaler.pkl")
features = joblib.load("models/features.pkl")

@app.route("/")
def home():
    return jsonify({"status": "SOC API Running"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    input_df = pd.DataFrame([data])

    # align features
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=features, fill_value=0)

    scaled = scaler.transform(input_df)

    prediction = model.predict(scaled)[0]

    return jsonify({
        "prediction": "THREAT" if prediction == 1 else "NORMAL",
        "risk_level": "HIGH" if prediction == 1 else "LOW"
    })

if __name__ == "__main__":
    app.run(debug=True)