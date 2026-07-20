numbers = list(map(int, input("Enter numbers: ").split()))

total = 0

for num in numbers:
    total = total + num

print("Sum of array elements:", total)