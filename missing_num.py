numbers = list(map(int, input("Enter numbers: ").split()))

n = len(numbers)

for i in range(n + 1):

    if i not in numbers:
        print("Missing number:", i)
        break