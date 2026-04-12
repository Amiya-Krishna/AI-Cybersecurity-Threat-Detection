import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    return df

def preprocess_data(df):

    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna()

    label_col = None
    for col in df.columns:
        if col.lower() in ["label", "class", "attack", "target", "attack_label"]:
            label_col = col
            break

    if label_col is None:
        raise Exception("No label column found")

    X = df.drop(label_col, axis=1)
    y = df[label_col]

    X = pd.get_dummies(X)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test, X.columns, scaler