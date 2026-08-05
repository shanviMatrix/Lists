array1 = list(map(int, input("Enter first array: ").split()))
array2 = list(map(int, input("Enter second array: ").split()))

common = list(set(array1) & set(array2))

print("Common elements:", common)