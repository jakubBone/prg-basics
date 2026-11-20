# A program that prints some elements of an array (a list).

# a Python list is used instead of an array: it can change its size and keep values of different types
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
# indexes start from 0, so the first element has the index 0
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[len(arr) - 1])
print('Last but one value', arr[len(arr) - 2])
print('Sum of the first and last value', arr[0] + arr[len(arr) - 1])
# // is the integer division, so len(arr) // 2 is the index of the middle element
print('Middle value', arr[len(arr) // 2])

print('All values:', end=' ')
for value in arr:
    print(value, end=' ')
print()
