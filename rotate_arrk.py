numbers = list(map(int, input("Enter numbers: ").split()))

k = int(input("Enter value of k: "))

n = len(numbers)

k = k % n

for j in range(k):

    last = numbers[-1]

    for i in range(n - 1, 0, -1):
        numbers[i] = numbers[i - 1]

    numbers[0] = last

print("Array after rotation:", numbers)