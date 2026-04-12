import joblib
import pandas as pd
import os

print("🔍 PREDICTION ENGINE STARTED")

model = joblib.load("models/cyber_model.pkl")

feature_names = model.feature_names_in_

# safe dummy input
sample = pd.DataFrame([[0]*len(feature_names)], columns=feature_names)

pred = model.predict(sample)[0]

print("\n🚨 RESULT:")
if pred == 1:
    print("🔴 THREAT DETECTED")
else:
    print("🟢 NORMAL TRAFFIC")