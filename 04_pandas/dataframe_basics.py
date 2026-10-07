# Pandas DataFrame Basics
import pandas as pd

data = {
    "Name": ["Ayush", "Rahul", "Priya", "Aman"],
    "Age": [19, 20, 19, 21],
    "Marks": [88, 76, 92, 81]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nFirst 2 students:")
print(df.head(2))

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())
