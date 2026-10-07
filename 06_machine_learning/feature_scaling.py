# Feature Scaling

from sklearn.preprocessing import StandardScaler

X = [
    [1, 50],
    [2, 55],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80],
    [7, 85],
    [8, 90]
]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("Original Data:")
print(X)

print("\nScaled Data:")
print(X_scaled)
