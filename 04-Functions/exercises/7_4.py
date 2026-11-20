# A program that counts how many times the letter 'e' appears in a text (the function is in the letters module).

import letters

text = 'You never get a second chance to make a first impression'
print(text)
print(f"The number of letter 'e': {letters.count_letter(text, 'e')}")
