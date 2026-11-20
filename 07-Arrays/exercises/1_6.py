# A program with a function that returns the name of the day of the week for a given day number.


def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    # day 1 is Monday, which has the index 0, so the index is n - 1
    return weekdays[n - 1]


print('Day 1 is', weekday(1))
print('Day 4 is', weekday(4))
print('Day 7 is', weekday(7))
