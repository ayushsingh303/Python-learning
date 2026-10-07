# Complete Machine Learning Pipeline

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X = [
    [1, 50],
    [2, 55],
    [2, 60],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80],
    [7, 85],
    [8, 90],
    [9, 95]
]

y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# 1. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# 2. Scale features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Create model
model = KNeighborsClassifier(n_neighbors=3)

# 4. Train model
model.fit(X_train_scaled, y_train)

# 5. Predict
predictions = model.predict(X_test_scaled)

# 6. Evaluate
accuracy = accuracy_score(y_test, predictions)

print("Actual:", y_test)
print("Predicted:", predictions)
print("Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")
