array1 = list(map(int, input("Enter first array: ").split()))
array2 = list(map(int, input("Enter second array: ").split()))

merged_array = []

for number in array1:
    merged_array.append(number)

for number in array2:
    merged_array.append(number)

print("Merged array:", merged_array)