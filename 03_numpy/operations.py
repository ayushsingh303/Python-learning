# NumPy Array Operations
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])

print("Array A:", a)
print("Array B:", b)

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("\nSquare of A:", a ** 2)

print("Mean:", np.mean(a))
print("Standard Deviation:", np.std(a))
