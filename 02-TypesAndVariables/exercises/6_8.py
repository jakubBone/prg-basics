# A program that calculates how many letters are between two given letters.

first = input('Enter first letter: ')
last = input('Enter last letter: ')

first_letter_code = ord(first)
last_letter_code = ord(last)

# for the same letter the difference minus 1 would be -1, so the result is limited to 0
number_of_letters = max(last_letter_code - first_letter_code - 1, 0)

print(f'Between {first} and {last} is {number_of_letters} letters')
