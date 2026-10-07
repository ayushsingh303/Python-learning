# Student Performance Predictor

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Features: [study hours, attendance]
X = [
    [1, 50],
    [2, 55],
    [3, 60],
    [4, 65],
    [5, 70],
    [6, 75],
    [7, 80],
    [8, 85],
    [9, 90],
    [10, 95]
]

# Target: marks
y = [45, 52, 58, 64, 71, 77, 83, 88, 93, 97]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

error = mean_absolute_error(y_test, predictions)

print("Actual:", y_test)
print("Predicted:", predictions)
print("Mean Absolute Error:", error)

# Example prediction
new_student = [[7, 82]]

prediction = model.predict(new_student)

print("\nPredicted marks for new student:", prediction[0])
