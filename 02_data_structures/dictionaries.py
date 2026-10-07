# Python Dictionaries

student = {
    "name": "Ayush",
    "age": 19,
    "course": "B.Tech AI/ML",
    "year": 1
}

print("Student information:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Year:", student["year"])

# Add new data
student["goal"] = "Become an AI/ML Engineer"

print("\nUpdated information:")
for key, value in student.items():
    print(key, ":", value)
