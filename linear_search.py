numbers = list(map(int, input("Enter numbers: ").split()))

target = int(input("Enter number to search: "))

found = False

for index in range(len(numbers)):

    if numbers[index] == target:
        print("Element found at index", index)
        found = True
        break

if found == False:
    print("Element not found")