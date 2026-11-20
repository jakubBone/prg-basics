# A program that prints all unique elements of an array (the elements that appear exactly once).

arr = [2, 3, 2, 5, 8, 1, 9, 8]

print('Array:', end=' ')
for value in arr:
    print(value, end=' ')
print()

print('Unique elements:', end=' ')
for value in arr:
    # count() returns how many times a value appears in the list
    if arr.count(value) == 1:
        print(value, end=' ')
print()
