pip install scikit-learn pandas
# ml_prediction.py
# Day 9 – Simple Machine Learning Prediction

import pandas as pd
from sklearn.linear_model import LinearRegression

print("=== Student Marks Prediction ===")

# Dataset
data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 85]
}

df = pd.DataFrame(data)

# Features (input) and Target (output)
X = df[["StudyHours"]]   # input
y = df["Marks"]          # output

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict marks for 6 hours of study
prediction = model.predict([[6]])

print("Predicted marks for 6 hours study:", int(prediction[0]))
