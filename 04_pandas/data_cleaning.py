# Pandas Data Cleaning
import pandas as pd

data = {
    "Name": ["Ayush", "Rahul", "Priya", "Aman", "Riya"],
    "Age": [19, 20, None, 21, 20],
    "Marks": [88, 76, 92, None, 95]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nCleaned Data:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
