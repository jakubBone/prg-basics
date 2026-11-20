# A program that prints the numbers from the first array that do not appear in the second array.

first = [4, 36, 12, 28, 9, 44, 5]
second = [5, 1, 36]

print('Numbers from the first array that are not in the second one:', end=' ')
for number in first:
    # the in operator checks whether a value is an element of a list
    if number not in second:
        print(number, end=' ')
print()
