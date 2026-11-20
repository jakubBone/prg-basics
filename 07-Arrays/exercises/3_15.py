# A program with a function that checks whether a number is present in an array.


def occurs(number, array):
    for element in array:
        if element == number:
            return True
    return False


array = [15, 38, 7, 23, 14]
number = int(input('Number: '))

print('Array:', end=' ')
for element in array:
    print(element, end=' ')
print()

if occurs(number, array):
    print(f'Result: number {number} appears in the array')
else:
    print(f'Result: number {number} does not appear in the array')
