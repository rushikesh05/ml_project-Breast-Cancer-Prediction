from sklearn.datasets import load_breast_cancer
from pymongo import MongoClient

# Load the breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Create a connection to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB connection details
db = client["ml_project_c"]  # Update with your database name
collection = db["Regression"]  # Update with your collection name

# Prepare the data for MongoDB insertion
data_dict = {"features": X.tolist(), "target": y.tolist()}

# Insert the data into MongoDB
collection.insert_one(data_dict)

# Confirm the data insertion
print("Data inserted successfully into MongoDB.")
