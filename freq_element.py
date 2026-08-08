numbers = list(map(int, input("Enter numbers: ").split()))

frequency = {}

for number in numbers:

    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("Frequency of each element:")

for number in frequency:
    print(number, ":", frequency[number])