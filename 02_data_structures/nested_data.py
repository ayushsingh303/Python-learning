# Nested Data Structures

students = [
    {
        "name": "Ayush",
        "age": 19,
        "course": "AI/ML"
    },
    {
        "name": "Rahul",
        "age": 20,
        "course": "CSE"
    },
    {
        "name": "Priya",
        "age": 19,
        "course": "Data Science"
    }
]

for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("-" * 30)
