# A program that asks for a name until the user enters a non-empty text and prints a greeting.

name = ''

# input() returns '' when the user just presses Enter, so the loop asks again
while name == '':
    name = input('Enter your name: ')

print(f'Hello {name}')
