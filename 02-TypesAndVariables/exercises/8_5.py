# A program that reads a SWIFT code and prints the bank code and the country code.

swift = input('Enter SWIFT code: ')

# the first 4 characters are the bank code, the next 2 are the country code
print(f'Bank Code: {swift[0:4]}')
print(f'Country Code: {swift[4:6]}')
