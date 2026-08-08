numbers = list(map(int, input("Enter numbers: ").split()))

position = 0

for number in numbers:

    if number != 0:
        numbers[position] = number
        position += 1

while position < len(numbers):
    numbers[position] = 0
    position += 1

print("Array after moving zeros:", numbers)