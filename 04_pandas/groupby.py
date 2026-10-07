# Pandas GroupBy
import pandas as pd

data = {
    "Name": ["Ayush", "Rahul", "Priya", "Aman", "Riya", "Karan"],
    "Course": ["AI/ML", "CSE", "AI/ML", "CSE", "AI/ML", "CSE"],
    "Marks": [88, 76, 92, 81, 95, 72]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nAverage Marks by Course:")
print(df.groupby("Course")["Marks"].mean())

print("\nHighest Marks by Course:")
print(df.groupby("Course")["Marks"].max())
