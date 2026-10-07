# Bar Chart
import matplotlib.pyplot as plt

subjects = ["Python", "Maths", "DSA", "AI", "ML"]
marks = [88, 76, 82, 91, 85]

plt.bar(subjects, marks)

plt.title("Subject-wise Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()
