# A module with a function that checks whether a number is within the range <x, y>.

def in_range(number, x, y):
    # a chained comparison: Python checks both sides at once
    return x <= number <= y
