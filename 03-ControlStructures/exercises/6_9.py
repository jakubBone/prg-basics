# A program that prints a name entered from the keyboard, provided it is a Polish female name
# (most Polish female names end with the letter "a").

name = input('Enter name: ')

# name[-1] is the last character of the string
if name[-1] == 'a':
    print(f'{name} -- Polish female name')
