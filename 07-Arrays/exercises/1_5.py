# A program that modifies the values of an array and prints the array after each change.

arr = [1, 2, 3, 4, 5]
print('Array:', arr)

# an element of a list can be changed by assigning a new value to its index
arr[0] = arr[0] - 1
print('Array:', arr)

arr[len(arr) - 1] += 4
print('Array:', arr)

arr[len(arr) // 2] *= 2
print('Array:', arr)
