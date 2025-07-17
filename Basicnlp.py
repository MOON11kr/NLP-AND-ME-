import pandas as pd
from sklearn.model_selection import train_test_split  # This is correct - scikit-learn uses sklearn in imports
from sklearn.ensemble import RandomForestClassifier  # This is correct
from sklearn.metrics import accuracy_score, confusion_matrix  # This is correct
from sklearn.preprocessing import StandardScaler  # This is correct
import matplotlib.pyplot as plt
import seaborn as sns
import os


def load_data():
    """Load diabetes dataset from local CSV."""
    try:
        df = pd.read_csv("diabetes.csv")
        if df.empty:
            raise ValueError("Dataset is empty")
        return df
    except FileNotFoundError:
        print("Error: diabetes.csv not found. Please download from:")
        print("https://raw.githubusercontent.com/plotly/datasets/master/"
              "diabetes.csv")
        exit(1)


def train_model(df):
    """Train a Random Forest Classifier."""
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Evaluate
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    return model, scaler, accuracy, cm


def predict_diabetes(model, scaler, user_input):
    """Predict diabetes probability."""
    input_scaled = scaler.transform([user_input])
    proba = model.predict_proba(input_scaled)[0][1] * 100
    return round(proba, 2)


def plot_confusion_matrix(cm):
    """Generate and save confusion matrix plot."""
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/confusion_matrix.png")
    plt.close()


def plot_feature_importance(model, feature_names):
    """Generate and save feature importance plot."""
    importances = model.feature_importances_
    indices = importances.argsort()[::-1]
    plt.figure(figsize=(10, 6))
    plt.title("Feature Importances")
    plt.bar(range(len(indices)),
            importances[indices],
            align="center")
    plt.xticks(range(len(indices)),
               [feature_names[i] for i in indices],
               rotation=45)
    plt.tight_layout()
    plt.savefig("output/feature_importance.png")
    plt.close()


def main():
    """Run the diabetes prediction system."""
    df = load_data()
    model, scaler, accuracy, cm = train_model(df)

    # Create output directory
    os.makedirs("output", exist_ok=True)

    # Generate plots
    plot_confusion_matrix(cm)
    plot_feature_importance(model, df.columns[:-1])

    print("=== Diabetes Prediction System ===")
    print("Enter your health metrics:")

    features = df.columns[:-1]
    user_input = []
    for feature in features:
        while True:
            try:
                value = float(input(f"{feature}: "))
                user_input.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    probability = predict_diabetes(model, scaler, user_input)
    print(f"\nProbability of having diabetes: {probability:.2f}%")
    print(f"Model Accuracy: {accuracy:.2%}")
    print("\nGraphs saved to output directory:")
    print("- output/confusion_matrix.png")
    print("- output/feature_importance.png")


if __name__ == "__main__":
    main()