# A program that converts time from the 24-hour format (hh:mm) to the 12-hour format.

time_24 = input('Enter time (24-hour format): ')

# the format is hh:mm, so the hour is time_24[0:2] and the minutes are time_24[3:5]
hour = int(time_24[0:2])
minutes = time_24[3:5]

if hour < 12:
    period = 'am'
else:
    period = 'pm'

# % 12 maps 13..23 to 1..11; 0 and 12 give 0, which is shown as 12
hour_12 = hour % 12
if hour_12 == 0:
    hour_12 = 12

print(f'Time in 12-hour format: {hour_12}:{minutes}{period}')
