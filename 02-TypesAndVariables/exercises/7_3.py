# A program that checks whether a number entered from the keyboard is even.

number = int(input('Enter number: '))
# a number is even if the remainder of dividing it by 2 is 0
even = number % 2 == 0

print(f'Number is even: {even}')
