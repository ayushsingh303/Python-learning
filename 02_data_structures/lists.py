# Python Lists

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers.append(60)
print("After adding:", numbers)

numbers.remove(20)
print("After removing:", numbers)

print("\nAll numbers:")
for number in numbers:
    print(number)
