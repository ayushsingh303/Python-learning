# Train-Test Split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

study_hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
marks = [45, 52, 60, 65, 72, 78, 85, 92, 96, 98]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    study_hours,
    marks,
    test_size=0.2,
    random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict test data
predictions = model.predict(X_test)

print("Actual marks:", y_test)
print("Predicted marks:", predictions)

# Evaluate model
error = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", error)
