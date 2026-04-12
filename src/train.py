import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from preprocess import load_data, preprocess_data
from visualization import (
    plot_confusion_matrix,
    plot_feature_importance,
    plot_class_distribution
)

os.makedirs("models", exist_ok=True)

print("🚀 TRAINING STARTED")

df = load_data("data/dataset.csv")

X_train, X_test, y_train, y_test, feature_names, scaler = preprocess_data(df)

model = RandomForestClassifier(n_estimators=150, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n📊 Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# VISUALS
plot_class_distribution(y_test)
plot_confusion_matrix(y_test, y_pred)
plot_feature_importance(model, feature_names)

# SAVE MODEL + SCALER
joblib.dump(model, "models/cyber_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(feature_names, "models/features.pkl")

print("\n💾 Model + scaler saved successfully!")