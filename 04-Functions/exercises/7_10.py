# A program with a function that returns the number of negative even numbers in the range <x, y>.


def count_negative_even(x, y):
    count = 0
    # y + 1, because the end of range() is not included
    for number in range(x, y + 1):
        if number < 0 and number % 2 == 0:
            count += 1
    return count


if __name__ == "__main__":
    print('f(-7,8) returns', count_negative_even(-7, 8))  # 3
    print('f(-1,11) returns', count_negative_even(-1, 11))  # 0
