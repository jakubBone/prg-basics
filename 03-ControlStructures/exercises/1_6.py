# A program that checks whether a number entered from the keyboard is even or odd.

number = int(input('Enter number: '))

# the remainder of dividing an even number by 2 is 0
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
