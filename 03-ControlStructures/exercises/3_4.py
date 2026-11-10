# A program that checks whether at least one of two entered numbers is not negative.

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print(f'Both numbers {x} and {y} are negative')
