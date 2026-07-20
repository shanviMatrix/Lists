numbers = list(map(int, input("Enter numbers: ").split()))

total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)

print("Average of array elements:", average)