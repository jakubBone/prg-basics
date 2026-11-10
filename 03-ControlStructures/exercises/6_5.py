# A program that simulates an electronic thermometer: it prints a verbal description of the temperature.

temperature = int(input('Enter temperature in Celsius: '))

# the conditions are checked from the top, so each elif only sees temperatures below the previous limit
if temperature > 35:
    print('It is extremely hot')
elif temperature > 30:
    print('It is hot')
elif temperature >= 15:
    print('It is warm')
elif temperature >= 0:
    print('It is cold')
else:
    print('Warning, frost')
