# NumPy 2D Arrays
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("2D Array:")
print(data)

print("\nShape:", data.shape)

print("First row:", data[0])
print("First column:", data[:, 0])

print("Element at row 2, column 3:", data[1, 2])

print("\nMean:", np.mean(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))
