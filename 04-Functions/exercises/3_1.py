# A program that uses the math module: square root of 7, natural logarithm of 5, sine of 90 degrees.

# to use the functions of an external module, the module must be imported
import math

square_root = math.sqrt(7)
print('A square root of 7 is', square_root)

# math.log(x) is the natural logarithm (base e)
logarithm = math.log(5)
print('A natural logarithm of 5 is', logarithm)

# math.sin() expects radians, so degrees are converted with math.radians()
sine = math.sin(math.radians(90))
print('A sine of 90 degrees is', sine)
