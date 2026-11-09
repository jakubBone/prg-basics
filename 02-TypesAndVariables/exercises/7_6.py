# A program that checks whether a vehicle speed on a highway is valid (between 40 and 140 km/h).

speed = int(input('Enter vehicle speed: '))
speed_ok = speed >= 40 and speed <= 140

print(f'Speed is valid: {speed_ok}')
