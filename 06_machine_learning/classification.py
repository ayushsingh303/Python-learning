# First Classification Model
from sklearn.neighbors import KNeighborsClassifier

# [Study Hours, Attendance %]
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

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X, y)

prediction = model.predict([[5, 78]])

if prediction[0] == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")
