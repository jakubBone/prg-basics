# A program that calculates the distance to the horizon from a height given in meters.

import math

HORIZON_CONST = 3.57

height = float(input('Enter a height in meters: '))
distance = HORIZON_CONST * math.sqrt(height)

print(f'Distance to the horizon: {distance:.2f} km')

# Example runs:
  # height = 1.8  -> Distance to the horizon: 4.79 km
  # height = 20   -> Distance to the horizon: 15.97 km






