###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#

speed_kmh = 70

# 1km=1000m, 1h=3600s
speed_ms = (speed_kmh * 1000) / 3600

print(f'{speed_kmh} km/h = {speed_ms:.2f} m/s')