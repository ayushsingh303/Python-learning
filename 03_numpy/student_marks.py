# Student Marks Analyzer
import numpy as np

marks = np.array([78, 85, 92, 67, 88, 74, 95, 81, 69, 90])

print("Student Marks:", marks)

print("\n--- Analysis ---")
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Standard Deviation:", np.std(marks))

passed = marks[marks >= 40]

print("Students Passed:", len(passed))
print("Students Failed:", len(marks) - len(passed))

print("\nMarks above 80:")
print(marks[marks > 80])
