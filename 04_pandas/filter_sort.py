# Pandas Filtering and Sorting
import pandas as pd

data = {
    "Name": ["Ayush", "Rahul", "Priya", "Aman", "Riya"],
    "Age": [19, 20, 19, 21, 20],
    "Marks": [88, 76, 92, 81, 95]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nStudents with marks above 85:")
print(df[df["Marks"] > 85])

print("\nStudents aged 20:")
print(df[df["Age"] == 20])

print("\nSorted by marks:")
print(df.sort_values("Marks", ascending=False))
