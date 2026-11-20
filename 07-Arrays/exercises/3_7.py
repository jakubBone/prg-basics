# A program that prints an array and the arithmetic mean of its values, using a for loop.

arr = [15, 8, 31, 47, 2, 19]

total = 0
for value in arr:
    total += value

mean = total / len(arr)

print('Array:', arr)
print(f'Arithmetic mean: {mean:.2f}')
