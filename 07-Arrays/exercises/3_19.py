# A program that counts how many times a value occurs in a tuple.

numbers = (50, 20, 40, 50, 30, 50)
value = int(input('Value: '))

count = 0
for number in numbers:
    if number == value:
        count += 1

print('Tuple:', numbers)
print('Value:', value)
print('Number of occurrences:', count)
