# A program that draws the function y = sin(x) for an angle in the range 0-360 degrees using matplotlib.
# matplotlib has to be installed first: py -m pip install matplotlib

import math
import matplotlib.pyplot as plt

x = []
y = []

for angle in range(0, 361):
    x = x + [angle]
    # math.sin() expects radians, so the angle in degrees is converted
    y = y + [math.sin(math.radians(angle))]

plt.plot(x, y)
plt.show()
