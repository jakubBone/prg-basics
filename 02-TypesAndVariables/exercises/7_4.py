# A program that checks whether a tree can be cut down (diameter of at least 50 cm).
# The diameter is calculated from the circumference entered from the keyboard.

import math

circumference = float(input('Enter tree circumference in cm: '))

# circumference = 2 * pi * radius, so radius = circumference / (2 * pi)
radius = circumference / (2 * math.pi)
diameter = radius * 2
can_be_cut_down = diameter >= 50

print(f'Tree can be cut down: {can_be_cut_down}')
