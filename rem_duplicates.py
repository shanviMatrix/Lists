numbers = list(map(int, input("Enter numbers: ").split()))

unique_numbers = []

for number in numbers:

    if number not in unique_numbers:
        unique_numbers.append(number)

print("Array after removing duplicates:", unique_numbers)