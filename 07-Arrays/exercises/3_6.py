# A program that finds the maximum and the minimum number in an array without the functions max() and min().

arr = [-15, 8, -31, 47, -2, 19]

# start with the first element and compare it with the rest
maximum = arr[0]
minimum = arr[0]
for value in arr:
    if value > maximum:
        maximum = value
    if value < minimum:
        minimum = value

print('Array:', arr)
print('Maximum:', maximum)
print('Minimum:', minimum)
