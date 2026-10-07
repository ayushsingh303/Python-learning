# Data Structures Practice

# 1. Find the largest number
numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number:", largest)


# 2. Calculate the average
total = 0

for number in numbers:
    total += number

average = total / len(numbers)

print("Average:", average)


# 3. Count even numbers
even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1

print("Even numbers:", even_count)
