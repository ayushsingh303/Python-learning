# First Machine Learning Model
from sklearn.linear_model import LinearRegression

# Training data
study_hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
marks = [45, 52, 60, 65, 72, 78, 85, 92]

# Create model
model = LinearRegression()

# Train model
model.fit(study_hours, marks)

# Make prediction
prediction = model.predict([[9]])

print("Predicted marks for 9 hours of study:", prediction[0])
