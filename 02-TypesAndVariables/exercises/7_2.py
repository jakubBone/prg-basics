# A program that checks whether a password is at least 8 characters long.

password = input('Enter password: ')
password_ok = len(password) >= 8

print(f'Password length is valid: {password_ok}')
