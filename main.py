import pandas as pd
import joblib
import os
import webbrowser

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from src.preprocess import load_data, preprocess_data
from src.visualization import (
    plot_confusion_matrix,
    plot_feature_importance,
    plot_class_distribution
)

print("\n🚀 AI CYBERSECURITY THREAT DETECTION SYSTEM STARTED\n")

# --------------------------
# STEP 1: LOAD DATA
# --------------------------
df = load_data("data/dataset.csv")

# --------------------------
# STEP 2: PREPROCESS
# --------------------------
X_train, X_test, y_train, y_test, feature_names, scaler = preprocess_data(df)

# --------------------------
# STEP 3: TRAIN MODEL
# --------------------------
model = RandomForestClassifier(
    n_estimators=150,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# --------------------------
# STEP 4: PREDICTION
# --------------------------
y_pred = model.predict(X_test)

print("\n📊 MODEL PERFORMANCE")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# --------------------------
# STEP 5: VISUALIZATION
# --------------------------
plot_class_distribution(y_test)
plot_confusion_matrix(y_test, y_pred)
plot_feature_importance(model, feature_names)

# AUTO OPEN OUTPUTS
try:
    import webbrowser
    import os

    def open_image(path):
        abs_path = os.path.abspath(path)
        webbrowser.open("file://" + abs_path)

    open_image("outputs/confusion_matrix.png")
    open_image("outputs/feature_importance.png")
    open_image("outputs/class_distribution.png")

except:
    import os
    os.startfile("outputs/confusion_matrix.png")
    os.startfile("outputs/feature_importance.png")
    os.startfile("outputs/class_distribution.png")
# --------------------------
# STEP 6: SAVE MODEL
# --------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/cyber_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(feature_names, "models/features.pkl")

print("\n💾 Model saved successfully!")

# --------------------------
# STEP 7: START API (OPTIONAL)
# --------------------------
print("\n🌐 Starting Flask API at http://127.0.0.1:5000")
os.system("python app.py")