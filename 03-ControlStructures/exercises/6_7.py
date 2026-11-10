# A program that checks which age group a person belongs to: child, teen, adult or senior.

age = int(input('Enter your age: '))

if age < 13:
    print('Child')
elif age <= 19:
    print('Teen')
elif age <= 64:
    print('Adult')
else:
    print('Senior')
