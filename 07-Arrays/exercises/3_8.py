# A program that prints an array and the arithmetic mean of its values, using a while loop.

arr = [15, 8, 31, 47, 2, 19]

total = 0
i = 0
while i < len(arr):
    total += arr[i]
    i += 1

mean = total / len(arr)

print('Array:', arr)
print(f'Arithmetic mean: {mean:.2f}')
