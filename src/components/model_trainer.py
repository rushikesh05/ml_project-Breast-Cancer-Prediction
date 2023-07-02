from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib


def train_model(data):
    # Separate features and target
    X = data.drop("target", axis=1)
    y = data["target"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a Random Forest Classifier
    model = RandomForestClassifier()

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Model accuracy:", accuracy)

    # Return the trained model
    return model

# Example usage
if __name__ == "__main__":
    # Load the preprocessed and transformed data from a CSV file or any other source
    transformed_data = pd.read_csv("breast_cancer_dataset.csv")

    # Train the model
    trained_model = train_model(transformed_data)

    # Save the trained model for future use
    joblib.dump(trained_model, "trained_model.pkl")
