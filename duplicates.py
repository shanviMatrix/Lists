numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

duplicates = []

for number in numbers:

    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Duplicate elements:", duplicates)