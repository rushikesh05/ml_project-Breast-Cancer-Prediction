from pymongo import MongoClient
import pandas as pd

# Create a connection to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB connection details
db = client["ml_project_c"]  # Update with your database name
collection = db["Regression"]  # Update with your collection name

# Retrieve the data from MongoDB
data = collection.find_one()

# Convert the data to a DataFrame
df = pd.DataFrame(data["features"], columns=data["features"])
df["target"] = data["target"]

# Print the DataFrame
print(df.head())
