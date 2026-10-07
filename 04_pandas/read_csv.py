# Reading CSV Data with Pandas
import pandas as pd

data = {
    "Name": ["Ayush", "Rahul", "Priya", "Aman"],
    "Age": [19, 20, 19, 21],
    "Marks": [88, 76, 92, 81]
}

df = pd.DataFrame(data)

# Save data as CSV
df.to_csv("students.csv", index=False)

print("CSV file created successfully!")

# Read CSV file
students = pd.read_csv("students.csv")

print("\nStudent Data:")
print(students)

print("\nAverage Marks:", students["Marks"].mean())
