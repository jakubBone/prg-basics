# A program that tests the functions from the converters module (centimeters to inches, feet and inches to centimeters).

import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'170 cm is {converters.cm_to_inch(170):.2f} inches')
print(f'5 feet 7 inches is {converters.feet_inches_to_cm(5, 7):.2f} cm')
