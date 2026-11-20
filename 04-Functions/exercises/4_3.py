# A program that calculates the area of a triangle from the lengths of its sides using Heron's formula.

import math


def triangle_area(a, b, c):
    # Heron's formula: s is half of the perimeter, area = sqrt(s * (s - a) * (s - b) * (s - c))
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))

area = triangle_area(side_a, side_b, side_c)
print(f'The area of a triangle with sides {side_a:g}, {side_b:g}, {side_c:g} is {area:g}')

# expected results: 3, 4, 5 -> 6; 5, 12, 13 -> 30; 7, 24, 25 -> 84
