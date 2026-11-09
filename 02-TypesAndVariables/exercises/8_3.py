# A program that converts a temperature from Celsius to Kelvin and Fahrenheit.

# read the temperature in Celsius from the keyboard
celsius = float(input('Enter temperature in Celsius: '))

# Kelvin = Celsius + 273.15
kelvin = celsius + 273.15

# Fahrenheit = Celsius * 9 / 5 + 32
fahrenheit = celsius * 9 / 5 + 32

# print the results
print(f'Kelvin: {kelvin:.2f}')
print(f'Fahrenheit: {fahrenheit:.2f}')
