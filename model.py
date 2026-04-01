import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load data
df = pd.read_csv("housing.csv")

# Preprocessing
df["total_bedrooms"] = pd.to_numeric(df["total_bedrooms"], errors='coerce')
df["total_bedrooms"] = df["total_bedrooms"].fillna(df["total_bedrooms"].median())

# One-hot encoding
df = pd.get_dummies(df, columns=["ocean_proximity"])

# Features & target
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ✅ Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

# Save columns
pickle.dump(X.columns, open("columns.pkl", "wb"))

print("Random Forest Model trained & saved ✅")