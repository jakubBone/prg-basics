# A program that prints the contents of an array in reverse order.

arr = [15, 8, 31, 47, 2, 19]

print('existed array:', end=' ')
for value in arr:
    print(value, end=' ')
print()

# range(start, stop, step): from the last index (len - 1) down to 0, so the step is -1
print('reverse array:', end=' ')
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=' ')
print()
