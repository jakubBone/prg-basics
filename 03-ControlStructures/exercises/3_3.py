# A program that checks whether a person is eligible for a discount (under 18 or 65 and older).

age = int(input('Enter your age: '))

if age < 18 or age >= 65:
    print('Discount is available')
else:
    print('Discount is not available')
