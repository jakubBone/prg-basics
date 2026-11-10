# A program that encrypts text using the Caesar code, shifting each character right by one position.

# Caesar code encryption method: every letter is replaced by the letter further in the alphabet. 
# (here 1), e.g. A -> B, B -> C. 
# Shifts also the space: its code 32, so 32 -> 33, which is '!'
# (e.g. 'The early' -> 'Uif!fbsmz').

plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # ord() returns the character's code (a number)
    code = ord(char)

    # add one to the character's code
    new_code = code + 1

    # chr() returns the character that has the given code
    new_char = chr(new_code)

    # add the encrypted character to the encrypted text
    encrypted_text = encrypted_text + new_char

print(plain_text)
print(encrypted_text)
