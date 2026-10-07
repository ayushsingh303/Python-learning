# Python Sets

numbers = {10, 20, 30, 20, 40, 10}

print("Set:", numbers)

numbers.add(50)
print("After adding:", numbers)

numbers.remove(20)
print("After removing:", numbers)

print("\nSet elements:")
for number in numbers:
    print(number)
