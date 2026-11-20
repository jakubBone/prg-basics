# A program that prints the number of elements of an array that are greater than a value entered from the keyboard.

numbers = [3.5, 1.2, 8.9, 4.4, 7.1, 0.6, 5.0]
value = float(input('Enter a value: '))

count = 0
for number in numbers:
    if number > value:
        count += 1

print('Array:', numbers)
print(f'The number of elements greater than {value}: {count}')
