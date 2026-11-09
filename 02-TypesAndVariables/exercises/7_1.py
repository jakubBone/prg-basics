# A program that checks whether a person is exempt from paying taxes (age up to and including 26).

age = int(input('Enter age: '))
no_tax = age <= 26

print(f'Exemption from paying taxes: {no_tax}')
