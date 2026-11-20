# A program that draws a line in a diagram from position (1, 3) to position (8, 10) using matplotlib.
# matplotlib has to be installed first: py -m pip install matplotlib

import matplotlib.pyplot as plt

xpoints = [1, 8]
ypoints = [3, 10]

plt.plot(xpoints, ypoints)
plt.show()
