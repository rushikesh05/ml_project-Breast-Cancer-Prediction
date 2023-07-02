import pandas as pd

def perform_feature_engineering(data):
    # Separate features and target
    X = data.drop("target", axis=1)
    y = data["target"]

    # Perform feature engineering
    # Example: Scaling the features using Min-Max normalization
    X_scaled = (X - X.min()) / (X.max() - X.min())

    # Example: Adding a new feature as a combination of existing features
    X_scaled["mean_radius_area_ratio"] = X_scaled["mean radius"] / X_scaled["mean area"]

    # Example: One-hot encoding categorical variables (if any)
    # Assuming there are no categorical variables in the breast cancer dataset

    # Return the transformed data
    transformed_data = pd.concat([X_scaled, y], axis=1)
    return transformed_data

# Example usage
if __name__ == "__main__":
    # Load the preprocessed data from a CSV file or any other source
    preprocessed_data = pd.read_csv("breast_cancer_dataset.csv")

    # Perform feature engineering
    transformed_data = perform_feature_engineering(preprocessed_data)

    # Print the transformed data
    print(transformed_data.head())
