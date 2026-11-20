# A program with a function that sums the numbers in the range <x, y>
# which are divisible by 2 and 3 and not divisible by 4.


def sum_special(x, y):
    total = 0
    for number in range(x, y + 1):
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total += number
    return total


if __name__ == "__main__":
    print('f(1,20) returns', sum_special(1, 20))  # 24
    print('f(10,30) returns', sum_special(10, 30))  # 48
