import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Ayush", "Rahul", "Priya", "Aman", "Riya", "Karan"],
    "Study_Hours": [2, 3, 4, 5, 6, 7],
    "Marks": [55, 62, 68, 75, 82, 90]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Average Study Hours:", df["Study_Hours"].mean())

plt.scatter(df["Study_Hours"], df["Marks"])

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()
