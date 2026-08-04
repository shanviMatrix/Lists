# Number of elements
n = int(input("Enter number of elements: "))

# Input array
arr = []

for i in range(n):
    num = int(input())
    arr.append(num)

# Bubble Sort (Descending)
for i in range(n):
    for j in range(n - i - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Output
print("Sorted array in descending order:")
for num in arr:
    print(num, end=" ")