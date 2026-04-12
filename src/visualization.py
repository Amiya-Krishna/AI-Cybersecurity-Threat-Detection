import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.metrics import confusion_matrix

os.makedirs("outputs", exist_ok=True)

def plot_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")

    path = "outputs/confusion_matrix.png"
    plt.savefig(path)
    plt.close()

    print("[SAVED]", path)


def plot_feature_importance(model, feature_names):
    import numpy as np

    importance = model.feature_importances_
    idx = importance.argsort()[-10:]

    plt.figure(figsize=(8,5))
    plt.barh(range(len(idx)), importance[idx])
    plt.yticks(range(len(idx)), [feature_names[i] for i in idx])
    plt.title("Top Features")

    path = "outputs/feature_importance.png"
    plt.savefig(path)
    plt.close()

    print("[SAVED]", path)


def plot_class_distribution(y):
    plt.figure(figsize=(5,4))
    sns.countplot(x=y)
    plt.title("Class Distribution")

    path = "outputs/class_distribution.png"
    plt.savefig(path)
    plt.close()

    print("[SAVED]", path)