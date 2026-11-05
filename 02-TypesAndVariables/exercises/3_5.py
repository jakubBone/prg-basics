###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math

a = 5
b = 8

# Pythagorean theorem: 
# diagonal = square root of (a^2 + b^2)
diagonal = math.sqrt(a**2 + b**2)

print(f'Diagonal: {diagonal:.2f}')