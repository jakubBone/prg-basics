# A program with a function that returns time as a string in the 24-hour or 12-hour format.


def time_string(hours, minutes, time_format):
    if time_format == '24':
        # :02d prints a number with at least 2 digits, padded with a zero (8 -> 08)
        return f'{hours:02d}:{minutes:02d}'

    # 12-hour format: before 12:00 it is am, from 12:00 it is pm
    if hours < 12:
        period = 'am'
    else:
        period = 'pm'

    # % 12 maps 13..23 to 1..11; 0 and 12 give 0, which is shown as 12
    hours_12 = hours % 12
    if hours_12 == 0:
        hours_12 = 12

    return f'{hours_12}:{minutes:02d}{period}'


if __name__ == "__main__":
    # tests: the expected result is in the comment
    print(time_string(15, 38, '24'))  # 15:38
    print(time_string(8, 3, '24'))  # 08:03
    print(time_string(0, 5, '24'))  # 00:05
    print(time_string(11, 15, '12'))  # 11:15am
    print(time_string(0, 7, '12'))  # 12:07am
    print(time_string(7, 30, '12'))  # 7:30am
    print(time_string(12, 46, '12'))  # 12:46pm
    print(time_string(13, 10, '12'))  # 1:10pm
    print(time_string(19, 2, '12'))  # 7:02pm
