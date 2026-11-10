# A program that calculates total fuel consumption for a given distance and driving mode:
# Auto (A) 7, Manual (M) 9, Eco (E) 6 liters per 100 km.

driving_mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))

fuel_consumption = 0  # liters per 100 km; stays 0 for an incorrect mode
if driving_mode == 'A':
    fuel_consumption = 7
elif driving_mode == 'M':
    fuel_consumption = 9
elif driving_mode == 'E':
    fuel_consumption = 6
else:
    print('Incorrect driving mode')

# consumption is given per 100 km, so the distance is divided by 100
total_consumption = distance * fuel_consumption / 100
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption:g} liters')
