# A program that tests built-in functions: max, min, len, input, int, bin, hex, ord and abs.

max_number = max(7, 5, 6, 3, 8, 2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4, 7, 2, 3, 9, 8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

# input() always returns a string
letter = input('Enter a letter: ')
print('The letter read from the keyboard is', letter)

# int() converts a string of digits to a number
number = int("20303")
print('The number representing the string "20303" is', number)

# bin() and hex() return strings with the prefixes 0b and 0x
print('Binary string of 304 is', bin(304))
print('Hexadecimal string of 304 is', hex(304))

# ord() returns the Unicode code of a character
print('The Unicode code of the euro sign is', ord("€"))

# abs() returns the absolute value
print('The absolute value of -17 is', abs(-17))
