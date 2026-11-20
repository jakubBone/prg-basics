# A program that counts the even values in an array using a while loop.

arr = [34, 7, 19, 4, 21, 8]

even_count = 0
i = 0
while i < len(arr):
    if arr[i] % 2 == 0:
        even_count += 1
    i += 1

print('Array:', arr)
print('Number of even values:', even_count)
